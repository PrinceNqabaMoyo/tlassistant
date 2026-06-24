import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade9_ems'
SUBTOPIC_ID = 'term2_sectors_of_economy'
CURRICULUM_REFERENCE = 'Term 2 > Sectors of the Economy'

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
            'title': 'Primary Sector',
            'prompt': "Which of the following is an example of a business operating in the PRIMARY sector?",
            'options': ["A clothing factory", "A coal mining company", "A supermarket", "A bank"],
            'correct_index': 1,
            'explanation': "The primary sector involves the extraction or harvesting of raw materials from the earth. Coal mining extracts raw materials, making it a primary sector activity.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the primary sector of the economy.'},
                {'title': 'Reasoning path', 'text': 'Primary = raw materials from nature. Secondary = manufacturing. Tertiary = services.'}
            ],
            'guidelines': ['Select the business that extracts raw materials.']
        }, subskill='concepts', learning_objective_id='lo_primary_sector', question_family_id='primary_sector_mcq', concept_id='primary_sector', concept_group='sectors_of_economy'),
        
        _with_metadata({
            'title': 'Secondary Sector',
            'prompt': "Which activity BEST describes the SECONDARY sector?",
            'options': ["Providing financial advice", "Manufacturing cars from steel and rubber", "Growing wheat on a farm", "Delivering parcels to customers"],
            'correct_index': 1,
            'explanation': "The secondary sector involves manufacturing and processing raw materials into finished goods. Manufacturing cars from raw materials like steel and rubber is a classic secondary sector activity.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the secondary sector.'},
                {'title': 'Reasoning path', 'text': 'Secondary = taking raw materials and making them into products.'}
            ],
            'guidelines': ['Select the manufacturing activity.']
        }, subskill='concepts', learning_objective_id='lo_secondary_sector', question_family_id='secondary_sector_mcq', concept_id='secondary_sector', concept_group='sectors_of_economy'),
        
        _with_metadata({
            'title': 'Tertiary Sector Example',
            'prompt': "Tourism and hospitality in South Africa are examples of the:",
            'options': ["primary sector", "secondary sector", "tertiary sector", "informal sector"],
            'correct_index': 2,
            'explanation': "Tourism and hospitality provide services to people, placing them in the tertiary sector. The tertiary sector includes all service-based industries.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the tertiary sector.'},
                {'title': 'Reasoning path', 'text': 'Tourism is a service industry, not extraction or manufacturing.'}
            ],
            'guidelines': ['Select the tertiary sector.']
        }, subskill='concepts', learning_objective_id='lo_tertiary_sector', question_family_id='tertiary_sector_mcq', concept_id='tertiary_sector', concept_group='sectors_of_economy'),
        
        _with_metadata({
            'title': 'Contribution to GDP',
            'prompt': "In South Africa, which sector contributes the largest percentage to the country's GDP?",
            'options': ["Primary sector", "Secondary sector", "Tertiary sector", "Informal sector"],
            'correct_index': 2,
            'explanation': "The tertiary (services) sector contributes the largest percentage to South Africa's GDP. This includes finance, retail, tourism, transport, and government services.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Knowing the relative contribution of each sector to South African GDP.'},
                {'title': 'Reasoning path', 'text': 'South Africa is a developing but service-oriented economy. Think about where most people work.'}
            ],
            'guidelines': ['Select the tertiary sector.']
        }, subskill='concepts', learning_objective_id='lo_gdp_contribution', question_family_id='gdp_contribution_mcq', concept_id='gdp_sectors', concept_group='sectors_of_economy'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({
            'title': 'Sectors Description',
            'prompt': "Describe the three main sectors of the South African economy and give one example of a business in each sector. (6 marks)",
            'marks': 6,
            'marking_points': [
                "Primary sector extracts or harvests raw materials from nature.",
                "Example: mining, agriculture, forestry, fishing.",
                "Secondary sector manufactures or processes raw materials into finished goods.",
                "Example: car factory, steel mill, food processing.",
                "Tertiary sector provides services to consumers and businesses.",
                "Example: bank, school, hospital, retail store, transport company."
            ],
            'sample_answer': "The primary sector involves the extraction of raw materials from nature, such as mining for coal, farming wheat, or fishing. The secondary sector takes these raw materials and manufactures them into finished products, such as a car factory that uses steel and rubber to build cars. The tertiary sector provides services rather than physical goods, such as banks offering financial services, schools providing education, and hospitals delivering healthcare.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Comprehensive knowledge of the three economic sectors.'},
                {'title': 'Reasoning path', 'text': 'Define each sector and match it to a specific South African example.'}
            ],
            'guidelines': ['Award marks for correct definition and valid example of each sector.']
        }, subskill='discussion', learning_objective_id='lo_sectors_description', question_family_id='sectors_essay', concept_id='economic_sectors', concept_group='sectors_of_economy'),
        
        _with_metadata({
            'title': 'Interdependence of Sectors',
            'prompt': "Explain how the three sectors of the economy are interdependent. Use a practical example to illustrate your answer. (4 marks)",
            'marks': 4,
            'marking_points': [
                "The primary sector provides raw materials to the secondary sector.",
                "The secondary sector produces goods that the tertiary sector sells or uses.",
                "The tertiary sector provides services that support both primary and secondary sectors.",
                "A valid practical example linking all three sectors."
            ],
            'sample_answer': "The three sectors are interdependent because each relies on the others. The primary sector extracts raw materials, such as a farmer growing cotton. The secondary sector processes these materials, such as a textile factory making cloth from the cotton. The tertiary sector then transports, markets, and sells the finished clothing to consumers. Without the farmer, the factory has no raw materials; without the factory, the retailer has no products to sell.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the interdependence of economic sectors.'},
                {'title': 'Reasoning path', 'text': 'Trace a product from raw material to finished good to sale, showing how each sector depends on the others.'}
            ],
            'guidelines': ['Require explanation of interdependence and a practical example.']
        }, subskill='discussion', learning_objective_id='lo_sectors_interdependence', question_family_id='interdependence_essay', concept_id='sector_interdependence', concept_group='sectors_of_economy'),
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
