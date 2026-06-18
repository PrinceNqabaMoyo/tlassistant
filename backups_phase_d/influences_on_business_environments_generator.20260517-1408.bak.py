import random

from ..names import MANUFACTURING_SUFFIXES
from ..names import RETAIL_AND_LIFESTYLE_SUFFIXES
from ..names import pick_business_name as _pick_business_name
from ..names import pick_supplier_name as _pick_supplier_name


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
SUBTOPIC_ID = 'influences_on_business_environments'
CURRICULUM_REFERENCE = 'Term 1 > Influences on business environments'


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
        'id': f"g11_bs_inf_mcq_{rng.randint(1000, 999999)}",
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
        'id': f"g11_bs_inf_typed_{rng.randint(1000, 999999)}",
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
            'title': 'Internal vs external influence',
            'prompt': 'Which influence is part of the internal business environment?',
            'options': ['Exchange rates', 'Mission and vision', 'Inflation', 'Legislation'],
            'correct_index': 1,
            'explanation': 'The mission and vision form part of the internal direction of the business and therefore belong to the internal business environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Separate internal influences from external influences.'},
                {'title': 'Reasoning path', 'text': 'Ask which option is controlled or defined by the business itself.'},
                {'title': 'Transfer idea', 'text': 'Internal influences usually come from inside the organisation, such as culture, goals, resources and structure.'}
            ],
            'guidelines': ['Identify whether each option comes from inside or outside the business.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='internal_vs_external_influence', concept_id='internal_vs_external_influences', concept_group='environment_components', misconception_tags=['confuses_internal_with_external'], diagnostic_tags=['classification', 'internal_external']),
        _with_metadata({
            'title': 'Macro influence',
            'prompt': 'A sudden increase in fuel prices is best classified as a(n) ... influence on business environments.',
            'options': ['internal', 'micro', 'macro', 'organisational'],
            'correct_index': 2,
            'explanation': 'Fuel prices are shaped by broad economic conditions outside the direct control of the business, so they are a macro influence.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You must recognise broad external pressures that affect many businesses at once.'},
                {'title': 'Scenario evidence', 'text': 'Fuel prices are not controlled by one business and usually reflect wider economic conditions.'},
                {'title': 'Transfer idea', 'text': 'Inflation, legislation and interest rates are usually macro influences.'}
            ],
            'guidelines': ['Look for influences that affect the whole business environment, not just one firm.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='macro_influence_classification', concept_id='macro_environment_classification', concept_group='environment_components', misconception_tags=['confuses_macro_with_internal'], diagnostic_tags=['classification', 'macro']),
        _with_metadata({
            'title': 'Control over influences',
            'prompt': 'Why do managers pay close attention to changes in legislation?',
            'options': [
                'Because legislation is fully controlled by the business',
                'Because legislation can shape how the business operates and complies',
                'Because legislation only affects the marketing department',
                'Because legislation is part of organisational culture'
            ],
            'correct_index': 1,
            'explanation': 'Legislation affects compliance requirements, operating procedures and costs, so managers must monitor it carefully.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'This asks about the effect of a macro influence on day-to-day business decisions.'},
                {'title': 'Reasoning path', 'text': 'Choose the option that explains the practical effect of laws on business operations.'},
                {'title': 'Transfer idea', 'text': 'External influences matter because they create risks, constraints and opportunities.'}
            ],
            'guidelines': ['Pick the option that explains business impact, not ownership or control.']
        }, subskill='concepts', learning_objective_id='lo_control_over_business_environments', question_family_id='control_over_influences', concept_id='monitoring_legal_influences', concept_group='extent_of_control', misconception_tags=['assumes_business_controls_legislation'], diagnostic_tags=['control_reasoning', 'macro']),
        _with_metadata({
            'title': 'Stakeholder influence',
            'prompt': 'Suppliers mainly influence a business by affecting its ...',
            'options': ['internal culture', 'access to inputs and cost structures', 'code of ethics only', 'ownership structure'],
            'correct_index': 1,
            'explanation': 'Suppliers affect the availability, quality and cost of the inputs a business needs to operate.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Suppliers are external stakeholders with a direct effect on business operations.'},
                {'title': 'Scenario evidence', 'text': 'Think about what suppliers provide to the business.'},
                {'title': 'Transfer idea', 'text': 'Any party that affects supply, demand or costs can influence the business environment.'}
            ],
            'guidelines': ['Link suppliers to stock, raw materials, quality and cost.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='stakeholder_influence', concept_id='market_environment_suppliers', concept_group='market_environment_components', misconception_tags=['treats_suppliers_as_internal'], diagnostic_tags=['market_components', 'stakeholders']),
        _with_metadata({
            'title': 'Technological influence',
            'prompt': 'A business adopts new production software to improve efficiency. This shows management responding mainly to a ... influence.',
            'options': ['technological', 'social', 'ethical', 'ownership'],
            'correct_index': 0,
            'explanation': 'New production software reflects a technological influence because it changes processes, efficiency and competitiveness.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You need to identify the category of external influence.'},
                {'title': 'Reasoning path', 'text': 'If the change centres on systems, tools or innovation, technology is usually the driver.'},
                {'title': 'Transfer idea', 'text': 'Technology influences production, communication, marketing and data use.'}
            ],
            'guidelines': ['Classify the influence by the source of change described in the scenario.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='technological_influence', concept_id='macro_environment_technology', concept_group='macro_environment_components', misconception_tags=['confuses_technology_with_internal_change'], diagnostic_tags=['macro_components', 'technology']),
        _with_metadata({
            'title': 'Micro environment components',
            'prompt': 'Which option is a component of the micro environment of a business?',
            'options': ['Organisational culture', 'Inflation', 'Competitors', 'Interest rates'],
            'correct_index': 0,
            'explanation': 'Organisational culture is part of the internal functioning of the business and therefore belongs to the micro environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You must identify a component that exists inside the business itself.'},
                {'title': 'Reasoning path', 'text': 'Micro environment components are internal matters such as culture, goals, resources and structure.'},
                {'title': 'Transfer idea', 'text': 'If the business can directly manage or shape it internally, it is likely part of the micro environment.'}
            ],
            'guidelines': ['Choose the option that belongs inside the business rather than outside it.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='micro_market_macro_components_naming', concept_id='micro_environment_components', concept_group='environment_components', retry_variant='core', misconception_tags=['confuses_internal_and_external_components'], diagnostic_tags=['components', 'micro']),
        _with_metadata({
            'title': 'Market environment components',
            'prompt': 'Which of the following is a component of the market environment?',
            'options': ['Suppliers', 'Mission statement', 'Organisational culture', 'Management structure'],
            'correct_index': 0,
            'explanation': 'Suppliers form part of the immediate external environment and therefore belong to the market environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You must recognise the immediate external parties that affect the business.'},
                {'title': 'Reasoning path', 'text': 'Suppliers, customers and competitors sit outside the business but directly influence its operations.'},
                {'title': 'Transfer idea', 'text': 'The market environment is not inside the business, but it is still close enough to affect daily decisions.'}
            ],
            'guidelines': ['Pick the option that belongs to the immediate external environment.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='micro_market_macro_components_naming', concept_id='market_environment_components', concept_group='environment_components', retry_variant='reworded', misconception_tags=['treats_market_factors_as_internal'], diagnostic_tags=['components', 'market']),
        _with_metadata({
            'title': 'Macro environment components',
            'prompt': 'Labour laws and recent legislation are examples of the ... component of the macro environment.',
            'options': ['legal', 'micro', 'market', 'internal'],
            'correct_index': 0,
            'explanation': 'Labour laws and legislation belong to the legal component of the macro environment because they come from the broad external environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You must match a broad external factor to the correct macro component.'},
                {'title': 'Reasoning path', 'text': 'Legislation and labour laws are part of the legal environment, which sits in the macro environment.'},
                {'title': 'Transfer idea', 'text': 'Macro components include legal, economic, social, political and technological forces.'}
            ],
            'guidelines': ['Match the example to the correct broad external category.']
        }, subskill='concepts', learning_objective_id='lo_components_of_business_environments', question_family_id='micro_market_macro_components_naming', concept_id='macro_environment_components', concept_group='environment_components', retry_variant='guided', misconception_tags=['confuses_macro_components_with_market_environment'], diagnostic_tags=['components', 'macro']),
        _with_metadata({
            'title': 'Control extent reasoning',
            'prompt': 'Why does a business usually have more control over the micro environment than the market environment?',
            'options': [
                'Because the micro environment includes internal policies, resources and structures managed by the business',
                'Because competitors and suppliers are employed by the business',
                'Because the market environment is always controlled by directors',
                'Because the macro environment is the same as the micro environment'
            ],
            'correct_index': 0,
            'explanation': 'A business controls the micro environment more directly because it manages its own internal resources, structures, leadership and policies, while the market environment includes outside parties such as customers, suppliers and competitors.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'This question asks for the reason behind the different levels of control across environments.'},
                {'title': 'Reasoning path', 'text': 'Think about which environment is internal to the business and which includes outside stakeholders.'},
                {'title': 'Transfer idea', 'text': 'Businesses can manage internal operations directly, but can only influence outside stakeholders to a limited extent.'}
            ],
            'guidelines': ['Choose the option that explains direct internal control, not external influence.']
        }, subskill='concepts', learning_objective_id='lo_control_over_business_environments', question_family_id='control_extent_reasoning', concept_id='extent_of_control_levels', concept_group='extent_of_control', retry_variant='core', misconception_tags=['assumes_market_environment_is_fully_controllable'], diagnostic_tags=['control_reasoning', 'micro_market']),
        _with_metadata({
            'title': 'Control extent reasoning with cues',
            'prompt': 'Which statement BEST explains why the market environment is only partly under the control of a business?',
            'options': [
                'The market environment includes customers, suppliers and competitors who are outside the business',
                'The market environment is created completely by internal policies',
                'The market environment is more controllable than the micro environment',
                'The market environment only refers to laws passed by government'
            ],
            'correct_index': 0,
            'explanation': 'The market environment is only partly controllable because it includes outside stakeholders such as customers, suppliers and competitors. A business can influence them to some extent, but it cannot manage them directly like internal resources.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This version gives stronger cues about who belongs in the market environment.'},
                {'title': 'Reasoning path', 'text': 'If the factor sits outside the business, managers can influence it but not command it directly.'},
                {'title': 'Transfer idea', 'text': 'Full control usually applies to the micro environment, limited control to the market environment, and no control to the macro environment.'}
            ],
             'guidelines': ['Choose the option that mentions outside stakeholders rather than internal structures.']
         }, subskill='concepts', learning_objective_id='lo_control_over_business_environments', question_family_id='control_extent_reasoning', concept_id='extent_of_control_levels', concept_group='extent_of_control', retry_variant='guided', misconception_tags=['assumes_market_environment_is_fully_controllable'], diagnostic_tags=['control_reasoning', 'market_environment']),
         _with_metadata({
             'title': 'Control extent reasoning reworded',
             'prompt': 'Customers and suppliers affect business performance every day. What does this show about a business’s control over the market environment?',
             'options': [
                 'The business has limited control because these stakeholders are outside the business',
                 'The business has full control because it trades with them regularly',
                 'The business has no control because customers and suppliers are part of the macro environment',
                 'The business has complete control because directors make all market decisions'
             ],
             'correct_index': 0,
             'explanation': 'Customers and suppliers are part of the market environment. They affect the business strongly, but because they are external stakeholders the business has only limited control over them.',
             'difficulties': ['medium', 'hard'],
             'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This question rephrases the same control idea using examples from the market environment.'},
                {'title': 'Reasoning path', 'text': 'Do not confuse regular interaction with direct control. A business works with customers and suppliers, but does not own them.'},
                {'title': 'Transfer idea', 'text': 'Limited control means the business can respond, negotiate or adapt, but it cannot decide for the external stakeholder.'}
            ],
            'guidelines': ['Pick the option that distinguishes interaction from direct control.']
        }, subskill='concepts', learning_objective_id='lo_control_over_business_environments', question_family_id='control_extent_reasoning', concept_id='extent_of_control_levels', concept_group='extent_of_control', retry_variant='reworded', misconception_tags=['confuses_market_interaction_with_full_control'], diagnostic_tags=['control_reasoning', 'stakeholders'])
    ]

def _application_pool(rng):
    r = rng or random.Random()
    bavi_case = _build_bavi_scenario_context(r)
    macro_case = _build_macro_involvement_context(r)
    table_case = _build_table_response_context(r)
    joes_case = _build_joes_supermarket_context()
    return [
        _with_metadata({
            'title': 'Scenario analysis',
            'prompt': 'BrightPath Traders has good internal leadership and clear goals, but rising interest rates and load shedding are making it difficult to expand. Identify TWO influences on the business environments from this scenario and explain how each one affects the business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Internal influence: leadership and clear goals support planning and decision-making.',
                'Macro influence: rising interest rates make borrowing and expansion more expensive.',
                'Macro influence: load shedding disrupts operations, productivity and service delivery.',
                'A clear explanation must link each influence to a business effect.'
            ],
            'sample_answer': 'One internal influence is leadership and clear goals, which help BrightPath plan effectively and guide employees. A macro influence is rising interest rates, which increase the cost of borrowing for expansion. Another macro influence is load shedding, which interrupts operations and reduces productivity.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Name influences and explain the effect of each one.'},
                {'title': 'Scenario evidence', 'text': 'Leadership and goals point to internal influences. Interest rates and load shedding point to broad external influences.'},
                {'title': 'Reasoning path', 'text': 'Do not stop at naming the influence; explain how it changes cost, productivity or decision-making.'}
            ],
            'answer_part_hints': [
                'Part 1: Identify one internal influence from the scenario.',
                'Part 2: Identify one broad external influence from the scenario.',
                'Part 3: Explain the effect of each influence on the business.'
            ],
            'guidelines': [
                'Use the wording from the scenario as evidence.',
                'Pair each influence with a clear business consequence.'
            ],
            'teaching_note': 'Strong answers classify the influence correctly and then connect it to business performance or decision-making.',
            'keywords': ['leadership', 'goals', 'interest rates', 'load shedding', 'cost of borrowing', 'productivity']
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='scenario_analysis_general', concept_id='scenario_influence_identification', concept_group='scenario_reasoning', scenario_family_id='brightpath_internal_macro_mix', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['identify', 'explain_effect'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Influence classification',
            'prompt': 'A fashion retailer is dealing with new consumer trends, stronger online competitors and pressure from labour laws. Explain how these influences can affect the business environment of the retailer. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Consumer trends influence demand and product choices.',
                'Online competitors increase competition and pressure pricing or service quality.',
                'Labour laws affect compliance, staffing policies and operating costs.',
                'The answer should show that several external influences can operate at the same time.'
            ],
            'sample_answer': 'New consumer trends affect what products the retailer must stock and how it markets them. Stronger online competitors increase competitive pressure and may force the retailer to improve prices, service or online presence. Labour laws influence staffing rules, compliance requirements and labour costs. Together these influences shape the retailer’s decisions and performance.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'You must explain how different external influences shape business decisions.'},
                {'title': 'Scenario evidence', 'text': 'Consumer trends relate to the market and social environment, online competitors relate to competition, and labour laws relate to the legal environment.'},
                {'title': 'Transfer idea', 'text': 'In Business Studies, influences matter because they change demand, cost, compliance and strategy.'}
            ],
            'answer_part_hints': [
                'Explain the effect of consumer trends.',
                'Explain the effect of competitors.',
                'Explain the effect of labour laws.'
            ],
            'guidelines': ['Use cause-and-effect sentences such as “This leads to ...” or “This means the business must ...”.'],
            'teaching_note': 'Better answers show that one business is affected by market, legal and social influences simultaneously.',
            'keywords': ['consumer trends', 'demand', 'competitors', 'pricing', 'labour laws', 'compliance']
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='influence_classification_written', concept_id='multiple_external_influences', concept_group='scenario_reasoning', scenario_family_id='retailer_multi_influence_case', diagnostic_tags=['scenario_analysis', 'external_influences'], answer_structure_tags=['classify', 'explain_effect'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Opportunity and risk',
            'prompt': 'Explain why technological change can be both an opportunity and a challenge for a business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Technology can improve efficiency and productivity.',
                'Technology can improve communication, quality or competitiveness.',
                'Technology may require expensive upgrades or training.',
                'Technology can create pressure to adapt quickly to remain relevant.'
            ],
            'sample_answer': 'Technological change can be an opportunity because it improves efficiency, communication and competitiveness. It can also be a challenge because businesses may need to spend money on upgrades and training, and they must adapt quickly to avoid falling behind competitors.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'Give one side showing benefits and one side showing difficulties.'},
                {'title': 'Reasoning path', 'text': 'Think about productivity and competitiveness for opportunities, then cost and adaptation for challenges.'},
                {'title': 'Transfer idea', 'text': 'Many influences create both opportunities and risks at the same time.'}
            ],
            'answer_part_hints': [
                'State one opportunity created by technology.',
                'State one challenge created by technology.',
                'Link both ideas back to the business.'
            ],
            'guidelines': ['Balance the answer by covering both positive and negative effects.'],
            'teaching_note': 'A complete answer avoids treating technology as only positive or only negative.',
            'keywords': ['efficiency', 'productivity', 'competitiveness', 'upgrades', 'training', 'adapt']
        }, subskill='application', learning_objective_id='lo_control_over_business_environments', question_family_id='technology_opportunity_and_risk', concept_id='technology_opportunities_and_challenges', concept_group='adaptation_and_response', scenario_family_id='technology_change_response', diagnostic_tags=['technology', 'opportunity_risk'], answer_structure_tags=['opportunity', 'challenge', 'effect'], minimum_mastery_score=0.6),

        _with_metadata({
            'title': 'Challenge identification from scenario',
            'prompt': f"{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries. Identify THREE challenges from the scenario. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees’ high rate of absenteeism is a challenge.',
                'Increased interest rates are a challenge.',
                'Late deliveries by suppliers are a challenge.',
                'Answers should identify three separate challenge statements from the scenario.'
            ],
            'sample_answer': 'The three challenges are employees’ absenteeism, increased interest rates that make borrowing difficult, and suppliers who are late with deliveries.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must pull out three challenge statements directly from the scenario.'},
                {'title': 'Scenario evidence', 'text': 'Look for a worker issue, a finance-related issue and a supplier-related issue.'},
                {'title': 'Reasoning path', 'text': 'Do not explain yet; first identify the challenge phrases clearly.'}
            ],
            'answer_part_hints': [
                'Identify the employee-related challenge.',
                'Identify the finance-related challenge.',
                'Identify the supplier-related challenge.'
            ],
            'guidelines': ['Use wording that stays close to the scenario evidence.'],
            'teaching_note': 'This family checks whether the learner can extract relevant challenge evidence before classifying it.',
            'keywords': ['absenteeism', 'interest rates', 'borrow loans', 'late deliveries', 'suppliers'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['quote_or_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario with cues',
            'prompt': f"Read the {bavi_case['business_name']} case again. Identify the THREE challenges by completing these prompts: one worker-related challenge, one borrowing or finance-related challenge, and one supplier-related challenge. (6 marks)\n\n{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries.",
            'marks': 6,
            'marking_points': [
                'Employees’ high rate of absenteeism is a challenge.',
                'Increased interest rates are a challenge.',
                'Late deliveries by suppliers are a challenge.',
                'Answers should identify three separate challenge statements from the scenario.'
            ],
            'sample_answer': 'The worker-related challenge is employees’ high absenteeism. The finance-related challenge is increased interest rates that make borrowing difficult. The supplier-related challenge is late deliveries by suppliers.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version tells you what type of challenge to find in each part of the scenario.'},
                {'title': 'Scenario evidence', 'text': 'Look for the sentence about workers, the sentence about borrowing money, and the sentence about suppliers.'},
                {'title': 'Reasoning path', 'text': 'Copy or closely paraphrase the challenge itself before trying to explain anything.'}
            ],
            'answer_part_hints': [
                'Write the worker-related challenge exactly or nearly exactly from the scenario.',
                'Write the borrowing or finance-related challenge.',
                'Write the supplier-related challenge.'
            ],
            'guidelines': ['Keep each answer focused on the challenge statement itself, not on its solution.'],
            'teaching_note': 'This guided retry narrows the search space by cueing the three evidence categories directly.',
            'keywords': ['absenteeism', 'interest rates', 'borrow', 'late deliveries', 'suppliers'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='guided', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['guided_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario reworded',
            'prompt': f"{bavi_case['business_name']} faces three separate difficulties. Workers are often absent, banks have raised interest rates, and {bavi_case['supplier_name']} delivers raw materials late. Identify the three challenges shown in this case. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees’ high rate of absenteeism is a challenge.',
                'Increased interest rates are a challenge.',
                'Late deliveries by suppliers are a challenge.',
                'Answers should identify three separate challenge statements from the scenario.'
            ],
            'sample_answer': 'The three challenges are workers’ absenteeism, higher interest rates that make borrowing difficult, and a supplier that delivers raw materials late.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version keeps the same challenge line but with a cleaner surface form.'},
                {'title': 'Scenario evidence', 'text': 'The three difficulties are already grouped for you: workers, banks and suppliers.'},
                {'title': 'Reasoning path', 'text': 'Name each difficulty clearly as a challenge without changing the meaning.'}
            ],
            'answer_part_hints': [
                'Name the worker problem.',
                'Name the borrowing or interest-rate problem.',
                'Name the supplier problem.'
            ],
            'guidelines': ['Use short, precise challenge phrases.'],
            'teaching_note': 'This retry keeps the same objective but removes some of the original wording load.',
            'keywords': ['absenteeism', 'interest rates', 'borrowing', 'late', 'supplier'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='reworded', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['reworded_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Challenge identification from scenario transfer',
            'prompt': f"Use the notes below to identify three challenges facing {bavi_case['business_name']}. Write one challenge for each bullet. (6 marks)\n\n- Employees are absent from work often.\n- Borrowing money has become difficult because interest rates increased.\n- {bavi_case['supplier_name']} delivers materials late.",
            'marks': 6,
            'marking_points': [
                'Employees’ high rate of absenteeism is a challenge.',
                'Increased interest rates are a challenge.',
                'Late deliveries by suppliers are a challenge.',
                'Answers should identify three separate challenge statements from the scenario.'
            ],
            'sample_answer': 'The challenges are frequent employee absenteeism, increased interest rates that make borrowing difficult, and late supplier deliveries.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version reduces the reading load by presenting the same challenge line as bullet notes.'},
                {'title': 'Scenario evidence', 'text': 'Each bullet already points to one challenge category: employees, finance and suppliers.'},
                {'title': 'Reasoning path', 'text': 'Turn each note into a clear challenge statement.'}
            ],
            'answer_part_hints': [
                'Bullet 1 becomes the employee challenge.',
                'Bullet 2 becomes the finance challenge.',
                'Bullet 3 becomes the supplier challenge.'
            ],
            'guidelines': ['Write one clear challenge per bullet and avoid adding new information.'],
            'teaching_note': 'This reduced-complexity transfer retry preserves the same objective while lowering scenario-processing demand.',
            'keywords': ['absent', 'interest rates', 'borrowing', 'supplier', 'late deliveries'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='transfer', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['transfer_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Environment classification from scenario',
            'prompt': f"{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries. Classify EACH challenge according to the micro, market and macro environments. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees’ absenteeism belongs to the micro environment.',
                'Late deliveries by suppliers belong to the market environment.',
                'Increased interest rates belong to the macro environment.',
                'The answer should match each challenge to the correct environment.'
            ],
            'sample_answer': 'Employees’ absenteeism is a micro-environment challenge. Late supplier deliveries are a market-environment challenge. Increased interest rates are a macro-environment challenge.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must link each challenge to the correct business environment.'},
                {'title': 'Scenario evidence', 'text': 'Employees point to micro, suppliers point to market, and interest rates point to macro.'},
                {'title': 'Reasoning path', 'text': 'Classify by asking whether the challenge is inside the business, in the immediate market, or in the broad external environment.'}
            ],
            'answer_part_hints': [
                'Classify the absenteeism challenge.',
                'Classify the supplier-delivery challenge.',
                'Classify the interest-rate challenge.'
            ],
            'guidelines': ['Name both the challenge and the environment when responding.'],
            'teaching_note': 'This family checks whether learners can sort scenario evidence across the three environments.',
            'keywords': ['absenteeism', 'micro', 'suppliers', 'market', 'interest rates', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='environment_classification_from_scenario', concept_id='environment_classification', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['classify_all_three'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Environment classification from scenario with cues',
            'prompt': f"Read the {bavi_case['business_name']} case and classify each challenge. Write one answer for the worker issue, one for the supplier issue, and one for the interest-rate issue. (6 marks)\n\n{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries.",
            'marks': 6,
            'marking_points': [
                'Employees’ absenteeism belongs to the micro environment.',
                'Late deliveries by suppliers belong to the market environment.',
                'Increased interest rates belong to the macro environment.',
                'The answer should match each challenge to the correct environment.'
            ],
            'sample_answer': 'Employees’ absenteeism is a micro-environment challenge. Late supplier deliveries are a market-environment challenge. Increased interest rates are a macro-environment challenge.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version tells you which three challenge lanes to classify.'},
                {'title': 'Scenario evidence', 'text': 'Workers point to micro, suppliers point to market, and interest rates point to macro.'},
                {'title': 'Reasoning path', 'text': 'Match each challenge to the environment where it belongs before writing full sentences.'}
            ],
            'answer_part_hints': [
                'Classify the worker issue.',
                'Classify the supplier issue.',
                'Classify the interest-rate issue.'
            ],
            'guidelines': ['Write the environment name next to each challenge.'],
            'teaching_note': 'This guided retry narrows the classification task into three explicit slots.',
            'keywords': ['absenteeism', 'micro', 'suppliers', 'market', 'interest rates', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='environment_classification_from_scenario', concept_id='environment_classification', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='guided', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['guided_classify', 'classify_all_three'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Environment classification from scenario reworded',
            'prompt': f"In the {bavi_case['business_name']} case, workers are often absent, banks have raised interest rates, and {bavi_case['supplier_name']} delivers raw materials late. Classify these three challenges into the micro, market and macro environments. (6 marks)",
            'marks': 6,
            'marking_points': [
                'Employees’ absenteeism belongs to the micro environment.',
                'Late deliveries by suppliers belong to the market environment.',
                'Increased interest rates belong to the macro environment.',
                'The answer should match each challenge to the correct environment.'
            ],
            'sample_answer': 'Workers’ absenteeism is a micro challenge. Late deliveries by the supplier are a market challenge. Increased interest rates are a macro challenge.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version keeps the same classification target with a shorter case form.'},
                {'title': 'Scenario evidence', 'text': 'Employees are internal, suppliers are immediate external stakeholders, and interest rates are broad external influences.'},
                {'title': 'Reasoning path', 'text': 'Classify by level: inside the business, close external environment, or broad external environment.'}
            ],
            'answer_part_hints': [
                'Place absenteeism in the correct environment.',
                'Place the supplier problem in the correct environment.',
                'Place the interest-rate problem in the correct environment.'
            ],
            'guidelines': ['Use one clear classification for each challenge.'],
            'teaching_note': 'This reworded retry reduces the reading load while keeping the same memo line.',
            'keywords': ['absenteeism', 'micro', 'supplier', 'market', 'interest rates', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='environment_classification_from_scenario', concept_id='environment_classification', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='reworded', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['reworded_classify', 'classify_all_three'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Environment classification from scenario transfer',
            'prompt': f"Classify the notes below into the micro, market and macro environments. (6 marks)\n\n- Employees are absent from work often at {bavi_case['business_name']}.\n- {bavi_case['supplier_name']} delivers raw materials late.\n- Interest rates have increased, making borrowing difficult.",
            'marks': 6,
            'marking_points': [
                'Employees’ absenteeism belongs to the micro environment.',
                'Late deliveries by suppliers belong to the market environment.',
                'Increased interest rates belong to the macro environment.',
                'The answer should match each challenge to the correct environment.'
            ],
            'sample_answer': 'Employee absenteeism is a micro challenge. Late deliveries by the supplier are a market challenge. Increased interest rates are a macro challenge.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version gives the same challenge line as short notes.'},
                {'title': 'Scenario evidence', 'text': 'Each bullet already points to one environment type.'},
                {'title': 'Reasoning path', 'text': 'Turn each note into an environment label.'}
            ],
            'answer_part_hints': [
                'Bullet 1 belongs to which environment?',
                'Bullet 2 belongs to which environment?',
                'Bullet 3 belongs to which environment?'
            ],
            'guidelines': ['Focus on classification only; do not explain the challenge.'],
            'teaching_note': 'This reduced-complexity transfer retry lowers reading demands while preserving the classification task.',
            'keywords': ['absenteeism', 'micro', 'supplier', 'market', 'interest rates', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='environment_classification_from_scenario', concept_id='environment_classification', concept_group='scenario_reasoning', scenario_family_id='bavi_three_environment_challenges', retry_variant='transfer', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['transfer_classify', 'classify_all_three'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Extent of control from scenario',
            'prompt': f"{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries. State the extent of control the business has over EACH environment represented in the scenario. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business has full or complete control over the micro environment.',
                'The business has limited or little control over the market environment.',
                'The business has no control over the macro environment.',
                'The answer should link the level of control to the correct environment.'
            ],
            'sample_answer': 'The business has full or complete control over the micro environment, limited control over the market environment, and no control over the macro environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This question asks for the level of control over each environment, not the challenges themselves.'},
                {'title': 'Reasoning path', 'text': 'Micro is internal and therefore fully controllable, market is only partly influenceable, and macro is not directly controllable.'},
                {'title': 'Transfer idea', 'text': 'This full-limited-none pattern is a core Grade 11 rule for business environments.'}
            ],
            'answer_part_hints': [
                'State the level of control for micro.',
                'State the level of control for market.',
                'State the level of control for macro.'
            ],
            'guidelines': ['Use the standard wording full/complete, limited/little, and no control where possible.'],
            'teaching_note': 'This family checks the foundational control pattern across the three environments.',
            'keywords': ['full control', 'complete control', 'limited control', 'little control', 'no control', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='extent_of_control_from_scenario', concept_id='extent_of_control_levels', concept_group='extent_of_control', scenario_family_id='bavi_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'extent_of_control'], answer_structure_tags=['state_control_levels'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Extent of control from scenario with cues',
            'prompt': f"Use the {bavi_case['business_name']} case to state the level of control for each environment. Write one answer for the micro environment, one for the market environment, and one for the macro environment. (6 marks)\n\n{bavi_case['business_name']} is experiencing a decline in profit due to employees’ high rate of absenteeism. Banks have increased interest rates, making it difficult for the business to borrow loans. {bavi_case['business_name']} buys raw materials from {bavi_case['supplier_name']}, who are late with deliveries.",
            'marks': 6,
            'marking_points': [
                'The business has full or complete control over the micro environment.',
                'The business has limited or little control over the market environment.',
                'The business has no control over the macro environment.',
                'The answer should link the level of control to the correct environment.'
            ],
            'sample_answer': 'The business has full control over the micro environment, limited control over the market environment, and no control over the macro environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you the three environment slots directly.'},
                {'title': 'Reasoning path', 'text': 'Use the Grade 11 control ladder: full for micro, limited for market, none for macro.'},
                {'title': 'Transfer idea', 'text': 'The question is about level of control, not naming the challenge again.'}
            ],
            'answer_part_hints': [
                'Write the control level for micro.',
                'Write the control level for market.',
                'Write the control level for macro.'
            ],
            'guidelines': ['Keep the wording close to full, limited and no control.'],
            'teaching_note': 'This guided retry makes the full-limited-none structure explicit.',
            'keywords': ['full control', 'limited control', 'no control', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='extent_of_control_from_scenario', concept_id='extent_of_control_levels', concept_group='extent_of_control', scenario_family_id='bavi_three_environment_challenges', retry_variant='guided', diagnostic_tags=['scenario_analysis', 'extent_of_control'], answer_structure_tags=['guided_control_levels', 'state_control_levels'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Extent of control from scenario reworded',
            'prompt': f"In the {bavi_case['business_name']} case, workers are often absent, banks have raised interest rates, and {bavi_case['supplier_name']} delivers raw materials late. State the extent of control the business has over the micro, market and macro environments. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business has full or complete control over the micro environment.',
                'The business has limited or little control over the market environment.',
                'The business has no control over the macro environment.',
                'The answer should link the level of control to the correct environment.'
            ],
            'sample_answer': 'The business has full control over the micro environment, limited control over the market environment, and no control over the macro environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version keeps the same control ladder in a shorter case form.'},
                {'title': 'Reasoning path', 'text': 'Focus on the environment category, then attach the correct level of control.'},
                {'title': 'Transfer idea', 'text': 'Internal equals full control, immediate external equals limited control, and broad external equals no control.'}
            ],
            'answer_part_hints': [
                'State the control level for micro.',
                'State the control level for market.',
                'State the control level for macro.'
            ],
            'guidelines': ['Answer with the control level for each environment, not a description of the challenge.'],
            'teaching_note': 'This retry shortens the case wording but keeps the same conceptual demand.',
            'keywords': ['full control', 'complete control', 'limited control', 'little control', 'no control', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='extent_of_control_from_scenario', concept_id='extent_of_control_levels', concept_group='extent_of_control', scenario_family_id='bavi_three_environment_challenges', retry_variant='reworded', diagnostic_tags=['scenario_analysis', 'extent_of_control'], answer_structure_tags=['reworded_control_levels', 'state_control_levels'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Extent of control from scenario transfer',
            'prompt': f"Use the notes below and state the level of control the business has over each environment. (6 marks)\n\n- Employees are absent from work often at {bavi_case['business_name']}.\n- {bavi_case['supplier_name']} delivers raw materials late.\n- Interest rates have increased, making borrowing difficult.",
            'marks': 6,
            'marking_points': [
                'The business has full or complete control over the micro environment.',
                'The business has limited or little control over the market environment.',
                'The business has no control over the macro environment.',
                'The answer should link the level of control to the correct environment.'
            ],
            'sample_answer': 'The business has full control over the micro environment, limited control over the market environment, and no control over the macro environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version presents the same three environments as short notes.'},
                {'title': 'Reasoning path', 'text': 'Match each environment to the standard control ladder: full, limited, none.'},
                {'title': 'Transfer idea', 'text': 'This is the same rule you use in structured tables and scenario questions.'}
            ],
            'answer_part_hints': [
                'What is the control level for micro?',
                'What is the control level for market?',
                'What is the control level for macro?'
            ],
            'guidelines': ['Keep the response to one control level per environment.'],
            'teaching_note': 'This reduced-complexity transfer retry lowers reading demand while preserving the same control objective.',
            'keywords': ['full control', 'limited control', 'no control', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='extent_of_control_from_scenario', concept_id='extent_of_control_levels', concept_group='extent_of_control', scenario_family_id='bavi_three_environment_challenges', retry_variant='transfer', diagnostic_tags=['scenario_analysis', 'extent_of_control'], answer_structure_tags=['transfer_control_levels', 'state_control_levels'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': "Challenge identification from Joe's Supermarket scenario",
            'prompt': f"{joes_case['business_name']} employed a manager who lacked management skills. The increase in the minimum wages of employees that are enforced by legislation is making it difficult to make a profit. Recently {joes_case['competitor_description']} opened across the street from {joes_case['business_name']}. Identify THREE challenges from the scenario. (6 marks)",
            'marks': 6,
            'marking_points': [
                'A manager who lacked management skills is a challenge.',
                'The increase in minimum wages enforced by legislation is a challenge.',
                'A new 24-hour supermarket opening across the street is a challenge.',
                'Answers should identify three separate challenge statements from the scenario.'
            ],
            'sample_answer': 'The three challenges are poor management skills, an increase in minimum wages enforced by legislation, and a new 24-hour supermarket that opened across the street.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': "You must pull out three challenge statements directly from the Joe's Supermarket case."},
                {'title': 'Scenario evidence', 'text': 'Look for one internal management issue, one legislation-related issue, and one competitor-related issue.'},
                {'title': 'Reasoning path', 'text': 'Do not explain the challenges yet; identify each problem clearly from the scenario.'}
            ],
            'answer_part_hints': [
                'Identify the management-related challenge.',
                'Identify the legislation or wage-related challenge.',
                'Identify the competitor-related challenge.'
            ],
            'guidelines': ['Keep your wording close to the scenario evidence.'],
            'teaching_note': "This curriculum-backed case mirrors the same three-environment extraction task using Joe's Supermarket from the notes.",
            'keywords': ['management skills', 'minimum wages', 'legislation', '24-hour supermarket', 'competitor'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='challenge_identification_from_scenario', concept_id='challenge_extraction', concept_group='scenario_reasoning', scenario_family_id='joes_supermarket_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'challenge_extraction'], answer_structure_tags=['quote_or_identify', 'three_challenges'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': "Environment classification from Joe's Supermarket scenario",
            'prompt': f"{joes_case['business_name']} employed a manager who lacked management skills. The increase in the minimum wages of employees that are enforced by legislation is making it difficult to make a profit. Recently {joes_case['competitor_description']} opened across the street from {joes_case['business_name']}. Classify EACH challenge according to the micro, market and macro environments. (6 marks)",
            'marks': 6,
            'marking_points': [
                'A manager who lacked management skills belongs to the micro environment.',
                'A new 24-hour supermarket opening across the street belongs to the market environment.',
                'The increase in minimum wages enforced by legislation belongs to the macro environment.',
                'The answer should match each challenge to the correct environment.'
            ],
            'sample_answer': 'Poor management skills are a micro-environment challenge. A new 24-hour supermarket across the street is a market-environment challenge. Increasing minimum wages enforced by legislation are a macro-environment challenge.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': "You must link each Joe's Supermarket challenge to the correct business environment."},
                {'title': 'Scenario evidence', 'text': 'Management skills point to micro, the new supermarket points to market, and legislation on minimum wages points to macro.'},
                {'title': 'Reasoning path', 'text': 'Classify by asking whether the challenge is inside the business, in the immediate market, or in the broad external environment.'}
            ],
            'answer_part_hints': [
                'Classify the management challenge.',
                'Classify the competitor challenge.',
                'Classify the legislation or wage challenge.'
            ],
            'guidelines': ['Name both the challenge and the environment when responding.'],
            'teaching_note': "This family uses the Joe's Supermarket case from the topic notes to test three-environment classification.",
            'keywords': ['management skills', 'micro', '24-hour supermarket', 'market', 'minimum wages', 'legislation', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='environment_classification_from_scenario', concept_id='environment_classification', concept_group='scenario_reasoning', scenario_family_id='joes_supermarket_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'classification'], answer_structure_tags=['classify_all_three'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': "Extent of control from Joe's Supermarket scenario",
            'prompt': f"{joes_case['business_name']} employed a manager who lacked management skills. The increase in the minimum wages of employees that are enforced by legislation is making it difficult to make a profit. Recently {joes_case['competitor_description']} opened across the street from {joes_case['business_name']}. State the extent of control the business has over EACH environment represented in the scenario. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business has full or complete control over the micro environment.',
                'The business has limited or little control over the market environment.',
                'The business has no control over the macro environment.',
                'The answer should link the level of control to the correct environment.'
            ],
            'sample_answer': 'The business has full or complete control over the micro environment, limited control over the market environment, and no control over the macro environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': "This question asks for the level of control over each environment represented in the Joe's case, not the challenges themselves."},
                {'title': 'Reasoning path', 'text': 'Micro is internal and therefore fully controllable, market is only partly influenceable, and macro is not directly controllable.'},
                {'title': 'Transfer idea', 'text': 'This full-limited-none pattern stays the same even when the scenario changes.'}
            ],
            'answer_part_hints': [
                'State the level of control for micro.',
                'State the level of control for market.',
                'State the level of control for macro.'
            ],
            'guidelines': ['Use the standard wording full/complete, limited/little, and no control where possible.'],
            'teaching_note': "This family applies the same control ladder to the Joe's Supermarket curriculum case.",
            'keywords': ['full control', 'limited control', 'no control', 'micro', 'market', 'macro'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='extent_of_control_from_scenario', concept_id='extent_of_control_levels', concept_group='extent_of_control', scenario_family_id='joes_supermarket_three_environment_challenges', retry_variant='core', diagnostic_tags=['scenario_analysis', 'extent_of_control'], answer_structure_tags=['state_control_levels'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': "Table-guided three-environment response from Joe's Supermarket",
            'prompt': f"{joes_case['business_name']} employed a manager who lacked management skills. The increase in the minimum wages of employees that are enforced by legislation is making it difficult to make a profit. Recently {joes_case['competitor_description']} opened across the street from {joes_case['business_name']}. Complete the response by identifying one challenge in each business environment and stating the extent of control the business has over each environment. (9 marks)",
            'marks': 9,
            'marking_points': [
                'Micro challenge: a manager who lacked management skills.',
                'Market challenge: a new 24-hour supermarket opened across the street.',
                'Macro challenge: minimum wages enforced by legislation are increasing costs.',
                'Micro environment: full or complete control.',
                'Market environment: limited or little control.',
                'Macro environment: no control.',
                'Answers should link the correct challenge and control level to each environment.'
            ],
            'sample_answer': 'The micro-environment challenge is a manager who lacked management skills, and the business has full control over that environment. The market-environment challenge is a new 24-hour supermarket across the street, and the business has limited control over that environment. The macro-environment challenge is increasing minimum wages enforced by legislation, and the business has no control over that environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This is a structured three-row response: one row for micro, one for market and one for macro.'},
                {'title': 'Reasoning path', 'text': 'First identify the challenge, then classify the environment, then state the matching level of control.'},
                {'title': 'Transfer idea', 'text': "This mirrors the Joe's Supermarket table-guided task shown in the curriculum notes."}
            ],
            'answer_part_hints': [
                'Micro row: challenge plus level of control.',
                'Market row: challenge plus level of control.',
                'Macro row: challenge plus level of control.'
            ],
            'guidelines': ['Answer in a clear row-by-row structure even if no actual table is shown.'],
            'teaching_note': "This family uses Joe's Supermarket to approximate the table-guided response pattern from the Grade 11 notes.",
            'keywords': ['management skills', '24-hour supermarket', 'minimum wages', 'legislation', 'full control', 'limited control', 'no control'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='table_guided_three_environment_response', concept_id='three_environment_table_response', concept_group='scenario_reasoning', scenario_family_id='joes_supermarket_table_case', retry_variant='core', diagnostic_tags=['table_guided', 'scenario_analysis'], answer_structure_tags=['structured_rows', 'challenge_plus_control'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Macro environment involvement recommendations',
            'prompt': f"{macro_case['business_name']} is keeping up with new technologies to improve production and has started exporting {macro_case['product']} to {macro_case['country']}. Recommend other ways in which the business can be involved in the macro environment. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can create job opportunities in the community.',
                'The business can undertake social responsibility programmes.',
                'The business can provide education and training programmes for workers.',
                'The business can engage in lobbying or collective bargaining to influence change.',
                'The business can enter public-private partnerships or improve infrastructure.',
                'The answer should recommend practical ways businesses can contribute beyond internal operations.'
            ],
            'sample_answer': 'The business can create job opportunities in the community, provide training for workers, and engage in lobbying or partnerships that improve the wider environment. It can also run social responsibility programmes and support infrastructure development.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must suggest practical ways the business can contribute to the broader external environment.'},
                {'title': 'Reasoning path', 'text': 'Think beyond daily business operations and focus on how a business can influence society, government or economic development.'},
                {'title': 'Transfer idea', 'text': 'Macro-environment involvement often includes jobs, CSI, training, lobbying, partnerships and expansion into wider markets.'}
            ],
            'answer_part_hints': [
                'Recommend one community-focused action.',
                'Recommend one worker or skills-development action.',
                'Recommend one broader influence or partnership action.'
            ],
            'guidelines': ['Use action verbs such as create, provide, engage, support or partner.'],
            'teaching_note': 'Strong answers move from vague goodwill to concrete forms of macro-environment involvement.',
            'keywords': ['job opportunities', 'social responsibility', 'training', 'lobbying', 'partnerships', 'infrastructure', 'community'],
        }, subskill='application', learning_objective_id='lo_recommend_macro_environment_involvement', question_family_id='macro_environment_involvement_recommendations', concept_id='macro_environment_involvement', concept_group='macro_involvement', scenario_family_id='majeed_tiles_macro_involvement', retry_variant='core', diagnostic_tags=['recommendation', 'macro_involvement'], answer_structure_tags=['recommend', 'practical_actions'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Macro environment involvement recommendations with cues',
            'prompt': f"{macro_case['business_name']} is keeping up with new technologies to improve production and has started exporting {macro_case['product']} to {macro_case['country']}. Recommend other ways in which the business can be involved in the macro environment. Include one community action, one worker-development action, and one broader influence or partnership action. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can create job opportunities in the community.',
                'The business can undertake social responsibility programmes.',
                'The business can provide education and training programmes for workers.',
                'The business can engage in lobbying or collective bargaining to influence change.',
                'The business can enter public-private partnerships or improve infrastructure.',
                'The answer should recommend practical ways businesses can contribute beyond internal operations.'
            ],
            'sample_answer': 'The business can create job opportunities in the community, provide training for workers, and engage in lobbying or partnerships that improve the wider environment. It can also run social responsibility programmes and support infrastructure development.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you three categories for your recommendations.'},
                {'title': 'Reasoning path', 'text': 'Think of one action for the community, one for workers, and one for wider external influence.'},
                {'title': 'Transfer idea', 'text': 'Macro-environment involvement goes beyond production and sales into social, economic and policy influence.'}
            ],
            'answer_part_hints': [
                'Recommend one community action.',
                'Recommend one worker or skills action.',
                'Recommend one partnership, lobbying or infrastructure action.'
            ],
            'guidelines': ['Group your recommendations into clear action categories.'],
            'teaching_note': 'This guided retry supports structured recommendation writing while keeping the same memo line.',
            'keywords': ['job opportunities', 'social responsibility', 'training', 'lobbying', 'partnerships', 'infrastructure', 'community'],
        }, subskill='application', learning_objective_id='lo_recommend_macro_environment_involvement', question_family_id='macro_environment_involvement_recommendations', concept_id='macro_environment_involvement', concept_group='macro_involvement', scenario_family_id='majeed_tiles_macro_involvement', retry_variant='guided', diagnostic_tags=['recommendation', 'macro_involvement'], answer_structure_tags=['guided_recommend', 'practical_actions'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Macro environment involvement recommendations reworded',
            'prompt': f"{macro_case['business_name']} already responds to change by using new technology and exporting {macro_case['product']} to {macro_case['country']}. Explain other practical ways the business can participate positively in the wider macro environment. (6 marks)",
            'marks': 6,
            'marking_points': [
                'The business can create job opportunities in the community.',
                'The business can undertake social responsibility programmes.',
                'The business can provide education and training programmes for workers.',
                'The business can engage in lobbying or collective bargaining to influence change.',
                'The business can enter public-private partnerships or improve infrastructure.',
                'The answer should recommend practical ways businesses can contribute beyond internal operations.'
            ],
            'sample_answer': 'The business can participate positively in the macro environment by creating jobs, supporting social responsibility programmes, training workers, and engaging in partnerships or lobbying that improve wider conditions. It can also support infrastructure and community development.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version asks for the same practical recommendations using a participation frame.'},
                {'title': 'Reasoning path', 'text': 'Move from what the business already does to other broader forms of involvement.'},
                {'title': 'Transfer idea', 'text': 'Positive macro participation can benefit communities, workers and the business itself.'}
            ],
            'answer_part_hints': [
                'Explain one community-focused action.',
                'Explain one worker-development action.',
                'Explain one policy, partnership or infrastructure action.'
            ],
            'guidelines': ['Use practical recommendations, not vague statements about being responsible.'],
            'teaching_note': 'This reworded retry keeps the same memo but changes the framing from recommend to participate positively.',
            'keywords': ['job opportunities', 'social responsibility', 'training', 'lobbying', 'partnerships', 'infrastructure', 'community'],
        }, subskill='application', learning_objective_id='lo_recommend_macro_environment_involvement', question_family_id='macro_environment_involvement_recommendations', concept_id='macro_environment_involvement', concept_group='macro_involvement', scenario_family_id='majeed_tiles_macro_involvement', retry_variant='reworded', diagnostic_tags=['recommendation', 'macro_involvement'], answer_structure_tags=['reworded_recommend', 'practical_actions'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Macro environment involvement recommendations transfer',
            'prompt': f"Use the prompts below to recommend other ways {macro_case['business_name']} can be involved in the macro environment. (6 marks)\n\n- One action that supports the community\n- One action that develops workers or skills\n- One action that influences or partners with the wider environment",
            'marks': 6,
            'marking_points': [
                'The business can create job opportunities in the community.',
                'The business can undertake social responsibility programmes.',
                'The business can provide education and training programmes for workers.',
                'The business can engage in lobbying or collective bargaining to influence change.',
                'The business can enter public-private partnerships or improve infrastructure.',
                'The answer should recommend practical ways businesses can contribute beyond internal operations.'
            ],
            'sample_answer': 'The business can support the community through jobs or social responsibility, develop workers through education and training, and influence the wider environment through lobbying, partnerships or infrastructure support.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version turns the same recommendation task into three simple prompts.'},
                {'title': 'Reasoning path', 'text': 'Give one clear action for each prompt rather than repeating the same idea.'},
                {'title': 'Transfer idea', 'text': 'Macro involvement can be organised into community, skills and wider influence actions.'}
            ],
            'answer_part_hints': [
                'Write one community action.',
                'Write one worker or training action.',
                'Write one lobbying, partnership or infrastructure action.'
            ],
            'guidelines': ['Answer each prompt with a practical action verb.'],
            'teaching_note': 'This reduced-complexity transfer retry supports idea generation without changing the learning objective.',
            'keywords': ['job opportunities', 'social responsibility', 'training', 'lobbying', 'partnerships', 'infrastructure', 'community'],
        }, subskill='application', learning_objective_id='lo_recommend_macro_environment_involvement', question_family_id='macro_environment_involvement_recommendations', concept_id='macro_environment_involvement', concept_group='macro_involvement', scenario_family_id='majeed_tiles_macro_involvement', retry_variant='transfer', diagnostic_tags=['recommendation', 'macro_involvement'], answer_structure_tags=['transfer_recommend', 'practical_actions'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Strategic responses and adaptation',
            'prompt': 'Explain how strategic responses help businesses adapt to challenges in business environments. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses can use lobbying or collective action to influence regulations or policies.',
                'Businesses can form strategic alliances or networks to share ideas and resources.',
                'Businesses can hedge against inflation or rising costs through financial strategies.',
                'Businesses can improve training and internal planning to respond to change.',
                'Businesses can conduct market research and adjust products or services to customer needs.',
                'The answer should show that strategic responses help businesses adapt rather than remain passive.'
            ],
            'sample_answer': 'Strategic responses help businesses adapt because they allow firms to influence policy through lobbying, share resources through alliances, and protect themselves through financial strategies such as hedging. Businesses can also train staff, improve planning and use market research to respond to customer and environmental changes.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This core version asks broadly how strategic responses support adaptation.'},
                {'title': 'Reasoning path', 'text': 'Think about both actions that influence the environment and actions that help the business adjust internally.'},
                {'title': 'Transfer idea', 'text': 'A strategic response is any deliberate step that helps the business cope with pressure or change.'}
            ],
            'answer_part_hints': [
                'Give one external influence strategy.',
                'Give one internal adaptation strategy.',
                'Explain how these help the business adjust.'
            ],
            'guidelines': ['Explain how the strategy helps adaptation, not only what the strategy is called.'],
            'teaching_note': 'This core version keeps the advice objective but with a more open response frame.',
            'keywords': ['lobbying', 'strategic alliances', 'networking', 'hedge', 'training', 'market research', 'adapt'],
        }, subskill='application', learning_objective_id='lo_adapt_to_business_environment_challenges', question_family_id='strategic_responses_lobbying_networking_adaptation', concept_id='strategic_responses', concept_group='adaptation_and_response', scenario_family_id='strategic_response_advice', retry_variant='core', diagnostic_tags=['advice', 'adaptation'], answer_structure_tags=['explain', 'strategy', 'adapt'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Strategic responses and adaptation',
            'prompt': 'Advise businesses on how strategic responses can be used to adapt to the challenges of business environments. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses can use lobbying or collective action to influence regulations or policies.',
                'Businesses can form strategic alliances or networks to share ideas and resources.',
                'Businesses can hedge against inflation or rising costs through financial strategies.',
                'Businesses can improve training and internal planning to respond to change.',
                'Businesses can conduct market research and adjust products or services to customer needs.',
                'The answer should show that strategic responses help businesses adapt rather than remain passive.'
            ],
            'sample_answer': 'Businesses can adapt to challenges by lobbying together for changes in regulations, forming strategic alliances to share resources, and using financial strategies such as hedging against inflation. They can also train staff, improve planning, and conduct market research so that they respond effectively to changing customer needs and external pressures.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must advise businesses on actions they can take to adapt to challenges across environments.'},
                {'title': 'Reasoning path', 'text': 'Think about both external influence strategies and internal adaptation strategies.'},
                {'title': 'Transfer idea', 'text': 'A strategic response is a deliberate action that helps the business cope with change, risk or pressure.'}
            ],
            'answer_part_hints': [
                'Give one collective or external influence strategy.',
                'Give one internal adaptation strategy.',
                'Explain how these strategies help the business respond to challenges.'
            ],
            'guidelines': ['Use advice language such as businesses should, can or ought to.'],
            'teaching_note': 'Better answers combine influence tactics with adaptive operational responses.',
            'keywords': ['lobbying', 'strategic alliances', 'networking', 'hedge', 'training', 'market research', 'adapt'],
        }, subskill='application', learning_objective_id='lo_adapt_to_business_environment_challenges', question_family_id='strategic_responses_lobbying_networking_adaptation', concept_id='strategic_responses', concept_group='adaptation_and_response', scenario_family_id='strategic_response_advice', retry_variant='guided', diagnostic_tags=['advice', 'adaptation'], answer_structure_tags=['advise', 'strategy', 'adapt'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Strategic responses and adaptation reworded',
            'prompt': 'A business is facing inflation, stronger competition and changing customer needs. Explain how strategic responses such as lobbying, alliances, training and market research can help it adapt. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses can use lobbying or collective action to influence regulations or policies.',
                'Businesses can form strategic alliances or networks to share ideas and resources.',
                'Businesses can hedge against inflation or rising costs through financial strategies.',
                'Businesses can improve training and internal planning to respond to change.',
                'Businesses can conduct market research and adjust products or services to customer needs.',
                'The answer should show that strategic responses help businesses adapt rather than remain passive.'
            ],
            'sample_answer': 'The business can adapt by lobbying or working collectively to influence external conditions, forming alliances to share resources, and using financial strategies such as hedging against inflation. It can also train staff and use market research to respond to competition and customer needs.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version anchors the same response in a shorter challenge frame.'},
                {'title': 'Reasoning path', 'text': 'Link each strategic response to one of the pressures in the prompt.'},
                {'title': 'Transfer idea', 'text': 'Good answers show how a deliberate strategy changes the business response to pressure.'}
            ],
            'answer_part_hints': [
                'Explain one policy or collective-response strategy.',
                'Explain one financial or alliance strategy.',
                'Explain one internal adaptation strategy.'
            ],
            'guidelines': ['Use cause-and-effect wording such as this helps the business to ...'],
            'teaching_note': 'This reworded retry keeps the memo line but gives a cleaner pressure context.',
            'keywords': ['lobbying', 'strategic alliances', 'networking', 'hedge', 'training', 'market research', 'adapt'],
        }, subskill='application', learning_objective_id='lo_adapt_to_business_environment_challenges', question_family_id='strategic_responses_lobbying_networking_adaptation', concept_id='strategic_responses', concept_group='adaptation_and_response', scenario_family_id='strategic_response_advice', retry_variant='reworded', diagnostic_tags=['advice', 'adaptation'], answer_structure_tags=['reworded_advice', 'strategy', 'adapt'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Strategic responses and adaptation transfer',
            'prompt': 'Use the prompts below to show how businesses can adapt to environmental challenges. (6 marks)\n\n- One strategy to influence policies or regulations\n- One strategy to work with other businesses or share resources\n- One strategy to improve internal response to change',
            'marks': 6,
            'marking_points': [
                'Businesses can use lobbying or collective action to influence regulations or policies.',
                'Businesses can form strategic alliances or networks to share ideas and resources.',
                'Businesses can hedge against inflation or rising costs through financial strategies.',
                'Businesses can improve training and internal planning to respond to change.',
                'Businesses can conduct market research and adjust products or services to customer needs.',
                'The answer should show that strategic responses help businesses adapt rather than remain passive.'
            ],
            'sample_answer': 'Businesses can use lobbying to influence policy, form alliances or networks to share resources, and improve training, planning or market research to respond internally to change.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This transfer version breaks the strategy task into three simple prompts.'},
                {'title': 'Reasoning path', 'text': 'Give one clear strategy for each prompt and link it to adaptation.'},
                {'title': 'Transfer idea', 'text': 'External influence, collaboration and internal adaptation are three common strategy lanes.'}
            ],
            'answer_part_hints': [
                'Write one lobbying or collective-action strategy.',
                'Write one alliance or networking strategy.',
                'Write one training, planning or market-research strategy.'
            ],
            'guidelines': ['Do not repeat the same strategy idea in all three prompts.'],
            'teaching_note': 'This reduced-complexity transfer retry supports retrieval of distinct strategy types.',
            'keywords': ['lobbying', 'strategic alliances', 'networking', 'hedge', 'training', 'market research', 'adapt'],
        }, subskill='application', learning_objective_id='lo_adapt_to_business_environment_challenges', question_family_id='strategic_responses_lobbying_networking_adaptation', concept_id='strategic_responses', concept_group='adaptation_and_response', scenario_family_id='strategic_response_advice', retry_variant='transfer', diagnostic_tags=['advice', 'adaptation'], answer_structure_tags=['transfer_advice', 'strategy', 'adapt'], minimum_mastery_score=0.6),
        _with_metadata({
            'title': 'Table-guided three-environment response',
            'prompt': f"{table_case['business_name']} has hired stylists who are always late for work. The business operates in an area with high unemployment and crime. It also buys material from {table_case['supplier_name']}, a supplier that charges high prices. Complete the response by identifying one challenge in each business environment and stating the extent of control the business has over each environment. (9 marks)",
            'marks': 9,
            'marking_points': [
                'Micro challenge: stylists who are always late for work.',
                'Market challenge: supplier that charges high prices for materials.',
                'Macro challenge: high unemployment and crime in the area.',
                'Micro environment: full or complete control.',
                'Market environment: limited or little control.',
                'Macro environment: no control.',
                'Answers should link the correct challenge and control level to each environment.'
            ],
            'sample_answer': 'The micro-environment challenge is stylists who are always late for work, and the business has full control over that environment. The market-environment challenge is the supplier charging high prices, and the business has limited control over that environment. The macro-environment challenge is high unemployment and crime, and the business has no control over that environment.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This is a structured three-row response: one row for micro, one for market and one for macro.'},
                {'title': 'Reasoning path', 'text': 'First identify the challenge, then classify the environment, then state the matching level of control.'},
                {'title': 'Transfer idea', 'text': 'This mirrors table-guided exam questions where the learner must complete each environment row correctly.'}
            ],
            'answer_part_hints': [
                'Micro row: challenge plus level of control.',
                'Market row: challenge plus level of control.',
                'Macro row: challenge plus level of control.'
            ],
            'guidelines': ['Answer in a clear row-by-row structure even if no actual table is shown.'],
            'teaching_note': 'This family is designed to approximate structured table responses in a typed-answer format.',
            'keywords': ['late for work', 'supplier', 'high prices', 'unemployment', 'crime', 'full control', 'limited control', 'no control'],
        }, subskill='application', learning_objective_id='lo_identify_challenges_and_control_from_scenarios', question_family_id='table_guided_three_environment_response', concept_id='three_environment_table_response', concept_group='scenario_reasoning', scenario_family_id='vincent_sportswear_table_case', retry_variant='transfer', diagnostic_tags=['table_guided', 'scenario_analysis'], answer_structure_tags=['structured_rows', 'challenge_plus_control'], minimum_mastery_score=0.6)
    ]


def _discussion_pool():
    return [
        _with_metadata({
            'title': 'Extended discussion',
            'prompt': 'Discuss the importance of understanding influences on business environments when managers make decisions. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Managers identify opportunities and threats more effectively.',
                'Managers can plan responses to external changes such as legislation, competition or economic trends.',
                'Understanding influences supports better risk management and strategic planning.',
                'Managers can allocate resources more effectively when they understand internal and external pressures.',
                'Businesses can remain competitive by adapting to changes in the environment.',
                'Good decisions depend on linking environmental influences to business objectives.'
            ],
            'sample_answer': 'Understanding influences on business environments helps managers identify opportunities and threats before making decisions. It allows them to respond to changes in legislation, competition and economic conditions, and to plan strategically. Managers can allocate resources more effectively, manage risks and adapt the business to stay competitive while still working towards business objectives.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This is a discussion about why environmental awareness matters in decision-making.'},
                {'title': 'Structure hint', 'text': 'Write linked points about planning, risk, adaptation, competitiveness and objectives.'},
                {'title': 'Transfer idea', 'text': 'When discussing importance, move from idea to consequence: why does this matter for managers?'}
            ],
            'answer_part_hints': [
                'Explain how managers identify risks and opportunities.',
                'Explain how this supports planning and resource allocation.',
                'Explain how this helps the business remain competitive.'
            ],
            'guidelines': [
                'Use full sentences and connect each point to managerial decision-making.',
                'Aim for several distinct reasons rather than repeating one idea.'
            ],
            'teaching_note': 'Top responses show that understanding the environment improves both short-term decisions and long-term strategy.',
            'keywords': ['opportunities', 'threats', 'risk management', 'strategic planning', 'resources', 'competitive']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='importance_of_environmental_awareness', concept_id='importance_of_environmental_awareness', concept_group='discussion_reasoning', retry_variant='core', diagnostic_tags=['discussion', 'importance'], answer_structure_tags=['importance', 'managerial_decision_making'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Extended discussion with structure cues',
            'prompt': 'Discuss why it is important for managers to understand influences on business environments. In your answer, refer to identifying risks or opportunities, planning responses, and helping the business remain competitive. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Managers identify opportunities and threats more effectively.',
                'Managers can plan responses to external changes such as legislation, competition or economic trends.',
                'Understanding influences supports better risk management and strategic planning.',
                'Managers can allocate resources more effectively when they understand internal and external pressures.',
                'Businesses can remain competitive by adapting to changes in the environment.',
                'Good decisions depend on linking environmental influences to business objectives.'
            ],
            'sample_answer': 'It is important for managers to understand influences on business environments because they can identify opportunities and threats earlier, plan suitable responses, and manage risks more effectively. This helps them allocate resources wisely and keep the business competitive while still working towards its objectives.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you three discussion lanes: risks and opportunities, planning, and competitiveness.'},
                {'title': 'Structure hint', 'text': 'Use one paragraph or point for each lane instead of mixing all ideas together.'},
                {'title': 'Transfer idea', 'text': 'Strong importance answers explain both what managers notice and what they can do better because they noticed it.'}
            ],
            'answer_part_hints': [
                'Explain one reason linked to risks or opportunities.',
                'Explain one reason linked to planning or resource use.',
                'Explain one reason linked to competitiveness or objectives.'
            ],
            'guidelines': [
                'Build the answer around the three cues in the prompt.',
                'Explain why each point matters for managerial decisions.'
            ],
            'teaching_note': 'This guided retry supports stronger discussion structure without changing the memo line.',
            'keywords': ['opportunities', 'threats', 'risk management', 'strategic planning', 'resources', 'competitive']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='importance_of_environmental_awareness', concept_id='importance_of_environmental_awareness', concept_group='discussion_reasoning', retry_variant='guided', diagnostic_tags=['discussion', 'importance'], answer_structure_tags=['importance', 'managerial_decision_making', 'guided_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Extended discussion reworded',
            'prompt': 'Managers who understand business environments usually make better decisions. Explain why this is true. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Managers identify opportunities and threats more effectively.',
                'Managers can plan responses to external changes such as legislation, competition or economic trends.',
                'Understanding influences supports better risk management and strategic planning.',
                'Managers can allocate resources more effectively when they understand internal and external pressures.',
                'Businesses can remain competitive by adapting to changes in the environment.',
                'Good decisions depend on linking environmental influences to business objectives.'
            ],
            'sample_answer': 'Managers who understand business environments make better decisions because they recognise threats and opportunities sooner, plan more effectively, and manage risks better. They can allocate resources more wisely and help the business adapt so that it remains competitive and focused on its objectives.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version keeps the same importance discussion in a shorter claim-and-explain form.'},
                {'title': 'Structure hint', 'text': 'Start with a main reason, then add consequences for planning, risk and competitiveness.'},
                {'title': 'Transfer idea', 'text': 'When the prompt says explain why, connect business awareness directly to better managerial action.'}
            ],
            'answer_part_hints': [
                'Explain how awareness helps managers notice important changes.',
                'Explain how awareness improves planning or risk management.',
                'Explain how awareness supports competitiveness or business objectives.'
            ],
            'guidelines': [
                'Keep the explanation focused on decision quality, not only on naming influences.',
                'Use linked reasons rather than isolated phrases.'
            ],
            'teaching_note': 'This reworded retry reduces prompt complexity while preserving the same discussion target.',
            'keywords': ['opportunities', 'threats', 'risk management', 'strategic planning', 'resources', 'competitive']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='importance_of_environmental_awareness', concept_id='importance_of_environmental_awareness', concept_group='discussion_reasoning', retry_variant='reworded', diagnostic_tags=['discussion', 'importance'], answer_structure_tags=['importance', 'managerial_decision_making', 'reworded_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Internal and external balance',
            'prompt': 'Differentiate between internal influences and external influences on business environments, and explain why both matter to a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Internal influences come from within the business, such as leadership, culture, resources or goals.',
                'External influences come from outside the business, such as legislation, technology, competitors or economic conditions.',
                'Internal influences matter because they shape the business’s capacity and decisions.',
                'External influences matter because they create opportunities, threats and constraints the business must respond to.'
            ],
            'sample_answer': 'Internal influences come from within the business and include factors such as leadership, culture, resources and goals. External influences come from outside the business and include legislation, technology, competitors and economic conditions. Internal influences matter because they shape how capable and organised the business is, while external influences matter because they create opportunities, threats and constraints that the business must respond to.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must define both categories and then explain their significance.'},
                {'title': 'Answer shape', 'text': 'Start with the difference, then add why each category matters.'},
                {'title': 'Transfer idea', 'text': 'Business Studies answers are stronger when they move from definition to implication.'}
            ],
            'answer_part_hints': [
                'Define internal influences.',
                'Define external influences.',
                'Explain why each category matters to the business.'
            ],
            'guidelines': ['Do not only list examples; explain the importance of the two categories.'],
            'teaching_note': 'This question rewards both conceptual clarity and explanation of impact.',
            'keywords': ['internal influences', 'external influences', 'leadership', 'resources', 'legislation', 'competitors']
        }, subskill='discussion', learning_objective_id='lo_components_of_business_environments', question_family_id='internal_vs_external_balance', concept_id='internal_vs_external_influences', concept_group='discussion_reasoning', retry_variant='core', diagnostic_tags=['discussion', 'differentiation'], answer_structure_tags=['differentiate', 'explain_importance'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Internal and external balance with cues',
            'prompt': 'Differentiate between internal influences and external influences on business environments. Then explain why internal influences matter and why external influences matter to a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Internal influences come from within the business, such as leadership, culture, resources or goals.',
                'External influences come from outside the business, such as legislation, technology, competitors or economic conditions.',
                'Internal influences matter because they shape the business’s capacity and decisions.',
                'External influences matter because they create opportunities, threats and constraints the business must respond to.'
            ],
            'sample_answer': 'Internal influences come from inside the business and include factors such as leadership, culture, resources and goals. External influences come from outside the business and include legislation, technology, competitors and economic conditions. Internal influences matter because they shape what the business can do, while external influences matter because they create opportunities, threats and limits that the business must respond to.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version splits the task into difference first, then significance.'},
                {'title': 'Answer shape', 'text': 'Write one part for internal, one part for external, then explain why each one matters.'},
                {'title': 'Transfer idea', 'text': 'Good differentiation answers compare source and effect, not just examples.'}
            ],
            'answer_part_hints': [
                'Say where internal influences come from.',
                'Say where external influences come from.',
                'Explain why each type matters to business decisions or performance.'
            ],
            'guidelines': ['Use both difference language and explanation language.'],
            'teaching_note': 'This guided retry makes the compare-then-explain structure explicit.',
            'keywords': ['internal influences', 'external influences', 'leadership', 'resources', 'legislation', 'competitors']
        }, subskill='discussion', learning_objective_id='lo_components_of_business_environments', question_family_id='internal_vs_external_balance', concept_id='internal_vs_external_influences', concept_group='discussion_reasoning', retry_variant='guided', diagnostic_tags=['discussion', 'differentiation'], answer_structure_tags=['differentiate', 'explain_importance', 'guided_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Internal and external balance reworded',
            'prompt': 'A business must understand what happens inside the business and what happens outside it. Explain this difference and why both sides matter. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Internal influences come from within the business, such as leadership, culture, resources or goals.',
                'External influences come from outside the business, such as legislation, technology, competitors or economic conditions.',
                'Internal influences matter because they shape the business’s capacity and decisions.',
                'External influences matter because they create opportunities, threats and constraints the business must respond to.'
            ],
            'sample_answer': 'What happens inside the business refers to internal influences such as leadership, culture, resources and goals. What happens outside the business refers to external influences such as legislation, technology, competitors and economic conditions. Both matter because internal influences shape how capable the business is, while external influences create pressures and opportunities that require a response.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version uses inside-versus-outside language instead of the formal labels only.'},
                {'title': 'Answer shape', 'text': 'Explain the difference first, then explain why each side matters.'},
                {'title': 'Transfer idea', 'text': 'Inside affects business capacity; outside affects business pressure, risk and opportunity.'}
            ],
            'answer_part_hints': [
                'Explain the inside-business side.',
                'Explain the outside-business side.',
                'State why both sides matter for business performance or decisions.'
            ],
            'guidelines': ['Translate the simpler wording back into clear Business Studies terms.'],
            'teaching_note': 'This reworded retry keeps the same conceptual demand with less formal prompt wording.',
            'keywords': ['internal influences', 'external influences', 'leadership', 'resources', 'legislation', 'competitors']
        }, subskill='discussion', learning_objective_id='lo_components_of_business_environments', question_family_id='internal_vs_external_balance', concept_id='internal_vs_external_influences', concept_group='discussion_reasoning', retry_variant='reworded', diagnostic_tags=['discussion', 'differentiation'], answer_structure_tags=['differentiate', 'explain_importance', 'reworded_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Adaptation discussion',
            'prompt': 'Explain why businesses that ignore environmental influences are likely to struggle in the long term. (4 marks)',
            'marks': 4,
            'marking_points': [
                'They may fail to identify threats in time.',
                'They may miss opportunities for innovation or growth.',
                'They may become less competitive than rivals.',
                'They may make poor strategic decisions because they are not responding to change.'
            ],
            'sample_answer': 'Businesses that ignore environmental influences often fail to identify threats or opportunities in time. They may become less competitive than rivals and make poor strategic decisions because they are not adapting to changes in the environment.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'This question focuses on the consequences of ignoring the environment.'},
                {'title': 'Reasoning path', 'text': 'Think about what happens when managers do not adapt to change.'},
                {'title': 'Transfer idea', 'text': 'Long-term struggle often comes from poor planning, weak competitiveness and missed opportunities.'}
            ],
            'answer_part_hints': [
                'Give at least two consequences of ignoring influences.',
                'Connect those consequences to long-term business survival.'
            ],
            'guidelines': ['Use words such as threats, opportunities, competitiveness and strategic decisions.'],
            'teaching_note': 'The core idea is that environmental awareness supports sustainability and relevance.',
            'keywords': ['threats', 'opportunities', 'competitive', 'strategic decisions', 'adapt']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='ignoring_influences_consequences', concept_id='ignoring_influences_consequences', concept_group='discussion_reasoning', retry_variant='core', diagnostic_tags=['discussion', 'consequences'], answer_structure_tags=['consequences', 'long_term_effect'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Adaptation discussion with cues',
            'prompt': 'Explain why businesses that ignore environmental influences are likely to struggle in the long term. In your answer, refer to threats, missed opportunities, competitiveness and strategic decisions. (4 marks)',
            'marks': 4,
            'marking_points': [
                'They may fail to identify threats in time.',
                'They may miss opportunities for innovation or growth.',
                'They may become less competitive than rivals.',
                'They may make poor strategic decisions because they are not responding to change.'
            ],
            'sample_answer': 'Businesses that ignore environmental influences may miss threats and opportunities, become less competitive and make weaker strategic decisions. Over time this makes it harder for them to survive and grow because they are not responding to change.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This guided version gives you four discussion cues to use as your answer structure.'},
                {'title': 'Reasoning path', 'text': 'Turn each cue into a consequence of ignoring the environment.'},
                {'title': 'Transfer idea', 'text': 'The business struggles long term because missed awareness leads to weak response.'}
            ],
            'answer_part_hints': [
                'Explain one problem linked to threats or opportunities.',
                'Explain one problem linked to competitiveness.',
                'Explain one problem linked to planning or strategic decisions.'
            ],
            'guidelines': ['Do not only list the cues; explain how each one causes long-term struggle.'],
            'teaching_note': 'This guided retry helps learners organise the same consequence discussion more clearly.',
            'keywords': ['threats', 'opportunities', 'competitive', 'strategic decisions', 'adapt']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='ignoring_influences_consequences', concept_id='ignoring_influences_consequences', concept_group='discussion_reasoning', retry_variant='guided', diagnostic_tags=['discussion', 'consequences'], answer_structure_tags=['consequences', 'long_term_effect', 'guided_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Adaptation discussion reworded',
            'prompt': 'What usually happens when managers fail to pay attention to changes in the business environment over time? Explain briefly. (4 marks)',
            'marks': 4,
            'marking_points': [
                'They may fail to identify threats in time.',
                'They may miss opportunities for innovation or growth.',
                'They may become less competitive than rivals.',
                'They may make poor strategic decisions because they are not responding to change.'
            ],
            'sample_answer': 'When managers fail to pay attention to environmental changes, they may miss threats and opportunities, become less competitive and make poor strategic decisions. Over time the business struggles because it does not adapt to change.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version asks for the same long-term consequences using a shorter manager-focused prompt.'},
                {'title': 'Reasoning path', 'text': 'Think about what poor awareness does to planning, growth and competitiveness.'},
                {'title': 'Transfer idea', 'text': 'Ignoring change usually leads to late reactions and weaker strategy.'}
            ],
            'answer_part_hints': [
                'State one result linked to missed change.',
                'State one result linked to competition or growth.',
                'State one result linked to weak decision-making.'
            ],
            'guidelines': ['Keep the answer concise but still explain the consequences clearly.'],
            'teaching_note': 'This reworded retry lowers prompt complexity while keeping the same consequence memo line.',
            'keywords': ['threats', 'opportunities', 'competitive', 'strategic decisions', 'adapt']
        }, subskill='discussion', learning_objective_id='lo_importance_of_understanding_influences', question_family_id='ignoring_influences_consequences', concept_id='ignoring_influences_consequences', concept_group='discussion_reasoning', retry_variant='reworded', diagnostic_tags=['discussion', 'consequences'], answer_structure_tags=['consequences', 'long_term_effect', 'reworded_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Benefits of macro-environment involvement',
            'prompt': 'Discuss the benefits or advantages of businesses that are involved in the macro environment. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses gain good publicity and can attract loyal customers.',
                'Businesses can attract and retain skilful employees.',
                'Businesses may access tenders, contracts or tax-related benefits.',
                'Businesses can anticipate likely challenges and turn them into opportunities.',
                'Investors are attracted to businesses that are positively involved in the wider environment.',
                'The answer should explain why broad environmental involvement supports long-term business success.'
            ],
            'sample_answer': 'Businesses that are involved in the macro environment often gain good publicity and attract loyal customers. They can also attract skilled employees, appeal to investors and sometimes benefit from tenders or tax-related advantages. Their involvement helps them anticipate challenges, respond earlier to change and build stronger long-term success.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'You must discuss the advantages that come from positive involvement in the wider environment.'},
                {'title': 'Structure hint', 'text': 'Write several separate benefit points and explain why each one helps the business.'},
                {'title': 'Transfer idea', 'text': 'Think about reputation, staff, investors, opportunities, resilience and community support.'}
            ],
            'answer_part_hints': [
                'Explain one reputation or publicity advantage.',
                'Explain one employee or investor advantage.',
                'Explain one strategic or long-term advantage.'
            ],
            'guidelines': ['Avoid listing only one benefit repeatedly; aim for distinct advantages.'],
            'teaching_note': 'Top responses link macro-environment involvement to reputation, resources and strategic advantage.',
            'keywords': ['good publicity', 'loyal customers', 'skilful employees', 'investors', 'tenders', 'opportunities'],
        }, subskill='discussion', learning_objective_id='lo_benefits_of_macro_environment_involvement', question_family_id='benefits_of_macro_environment_involvement', concept_id='macro_environment_involvement_benefits', concept_group='macro_involvement', retry_variant='core', diagnostic_tags=['discussion', 'benefits'], answer_structure_tags=['discuss', 'advantages'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Benefits of macro-environment involvement with structure cues',
            'prompt': 'Businesses that are involved in the macro environment often benefit in more than one way. Discuss these benefits by writing about: reputation or publicity, employees or investors, and long-term opportunities. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses gain good publicity and can attract loyal customers.',
                'Businesses can attract and retain skilful employees.',
                'Businesses may access tenders, contracts or tax-related benefits.',
                'Businesses can anticipate likely challenges and turn them into opportunities.',
                'Investors are attracted to businesses that are positively involved in the wider environment.',
                'The answer should explain why broad environmental involvement supports long-term business success.'
            ],
            'sample_answer': 'Businesses involved in the macro environment often gain good publicity and attract loyal customers. They can also attract skilled employees and investors. In the long term they are better able to anticipate challenges, access opportunities such as tenders or contracts, and build stronger business success.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This version gives you three idea buckets for your discussion.'},
                {'title': 'Structure hint', 'text': 'Use one point from each bucket so your answer is balanced.'},
                {'title': 'Transfer idea', 'text': 'Macro involvement can help a business socially, financially and strategically.'}
            ],
            'answer_part_hints': [
                'Explain one reputation or publicity benefit.',
                'Explain one employee or investor benefit.',
                'Explain one long-term strategic benefit.'
            ],
            'guidelines': ['Cover more than one type of advantage instead of repeating reputation only.'],
            'teaching_note': 'This guided retry helps learners organise benefits into recognisable categories.',
            'keywords': ['good publicity', 'loyal customers', 'skilful employees', 'investors', 'tenders', 'opportunities'],
        }, subskill='discussion', learning_objective_id='lo_benefits_of_macro_environment_involvement', question_family_id='benefits_of_macro_environment_involvement', concept_id='macro_environment_involvement_benefits', concept_group='macro_involvement', retry_variant='guided', diagnostic_tags=['discussion', 'benefits'], answer_structure_tags=['discuss', 'advantages', 'guided_discussion'], minimum_mastery_score=0.7),
        _with_metadata({
            'title': 'Benefits of macro-environment involvement reworded',
            'prompt': 'Explain why businesses that participate positively in the wider macro environment often gain an advantage over time. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Businesses gain good publicity and can attract loyal customers.',
                'Businesses can attract and retain skilful employees.',
                'Businesses may access tenders, contracts or tax-related benefits.',
                'Businesses can anticipate likely challenges and turn them into opportunities.',
                'Investors are attracted to businesses that are positively involved in the wider environment.',
                'The answer should explain why broad environmental involvement supports long-term business success.'
            ],
            'sample_answer': 'Businesses that participate positively in the wider macro environment often gain good publicity, attract loyal customers and appeal to skilled employees and investors. Their involvement can also help them access tenders or contracts, anticipate challenges earlier and build stronger long-term success.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being asked?', 'text': 'This reworded version frames the same discussion as long-term advantage.'},
                {'title': 'Structure hint', 'text': 'Explain how involvement improves reputation, resources and future opportunities.'},
                {'title': 'Transfer idea', 'text': 'Advantage over time often comes from trust, talent, support and better positioning.'}
            ],
            'answer_part_hints': [
                'Explain one advantage linked to image or customer support.',
                'Explain one advantage linked to people or finance.',
                'Explain one advantage linked to long-term opportunities or resilience.'
            ],
            'guidelines': ['Use explanation language such as this helps the business to ...'],
            'teaching_note': 'This reworded retry preserves the same memo line while changing the framing to long-term advantage.',
            'keywords': ['good publicity', 'loyal customers', 'skilful employees', 'investors', 'tenders', 'opportunities'],
        }, subskill='discussion', learning_objective_id='lo_benefits_of_macro_environment_involvement', question_family_id='benefits_of_macro_environment_involvement', concept_id='macro_environment_involvement_benefits', concept_group='macro_involvement', retry_variant='reworded', diagnostic_tags=['discussion', 'benefits'], answer_structure_tags=['discuss', 'advantages', 'reworded_discussion'], minimum_mastery_score=0.7),
    ]


def _build_bavi_scenario_context(rng):
    return {
        'business_name': _pick_business_name(r=rng, suffixes=MANUFACTURING_SUFFIXES),
        'supplier_name': _pick_supplier_name(r=rng),
    }


def _build_joes_supermarket_context():
    return {
        'business_name': "Joe's Supermarket",
        'competitor_description': 'a new 24-hour supermarket',
    }


def _build_macro_involvement_context(rng):
    return {
        'business_name': _pick_business_name(r=rng, suffixes=MANUFACTURING_SUFFIXES),
        'product': rng.choice(['tiles', 'processed foods', 'school uniforms', 'furniture']),
        'country': rng.choice(['Botswana', 'Namibia', 'Lesotho', 'Mozambique']),
    }


def _build_table_response_context(rng):
    return {
        'business_name': _pick_business_name(r=rng, suffixes=RETAIL_AND_LIFESTYLE_SUFFIXES),
        'supplier_name': _pick_supplier_name(r=rng),
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
        mixed_pool = [
            ('mcq', item) for item in concepts
        ] + [
            ('typed', item) for item in application
        ] + [
            ('typed', item) for item in discussion
        ]
        selected = _select_items(rng, mixed_pool, count, difficulty)
        questions = []
        for kind, item in selected:
            questions.append(_mcq_question(rng, item) if kind == 'mcq' else _typed_question(rng, item))
        return questions
    return [_mcq_question(rng, item) for item in _select_items(rng, concepts, count, difficulty)]
