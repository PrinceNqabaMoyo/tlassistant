import random
from app.utils.ems_namelist import NAMES, AREAS, get_ems_scenario

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term3_production_process'
CURRICULUM_REFERENCE = 'Term 3 > The Economy: The Production Process'

def _with_metadata(
    item,
    *,
    subskill,
    learning_objective_id,
    question_family_id,
    concept_id=None,
    concept_group="production_process",
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
        'term': 3,
        'caps_weight_percent': 15,
        'suggested_duration_mins': 15,
    })
    if minimum_mastery_score is not None:
        enriched['minimum_mastery_score'] = minimum_mastery_score
    return enriched

def _build_sectors_questions(rng):
    scenarios = [
        {
            "name": rng.choice(NAMES),
            "area": rng.choice(AREAS),
            "raw": "timber/wood",
            "primary": "a forestry plantation owner",
            "secondary": "a furniture factory",
            "tertiary": "a retail furniture showroom",
            "product": "solid oak dining tables"
        },
        {
            "name": rng.choice(NAMES),
            "area": rng.choice(AREAS),
            "raw": "wheat",
            "primary": "a commercial grain farmer",
            "secondary": "an industrial flour mill and bakery",
            "tertiary": "a local supermarket",
            "product": "fresh loaves of bread"
        },
        {
            "name": rng.choice(NAMES),
            "area": rng.choice(AREAS),
            "raw": "iron ore",
            "primary": "an open-cast mining company",
            "secondary": "a steel manufacturing plant and automotive assembly factory",
            "tertiary": "an authorized motor vehicle dealership",
            "product": "passenger delivery bakkies"
        },
        {
            "name": rng.choice(NAMES),
            "area": rng.choice(AREAS),
            "raw": "cows/cattle",
            "primary": "a livestock farmer",
            "secondary": "a meat processing abattoir and packaging plant",
            "tertiary": "a community butchery and family restaurant",
            "product": "packaged beef cuts and prepared meals"
        }
    ]
    sc = rng.choice(scenarios)
    
    return [
        _with_metadata({
            'title': 'Economic Sectors in Production',
            'diagram_spec': {
        "diagram_role": "context",
                'kind': 'production_chain',
                'raw': sc['raw'],
                'primary': sc['primary'],
                'secondary': sc['secondary'],
                'tertiary': sc['tertiary'],
                'product': sc['product']
            },
            'prompt': (
                f"{sc['name']} in {sc['area']} operates {sc['secondary']} that converts {sc['raw']} "
                f"into {sc['product']}. Into which sector of the economy does this business fall?"
            ),
            'options': [
                "Primary sector",
                "Secondary sector",
                "Tertiary sector",
                "Quaternary financial sector"
            ],
            'correct_index': 1,
            'explanation': (
                f"The business operates in the Secondary sector because it takes raw materials ({sc['raw']}) "
                f"and manufactures/processes them into finished products ({sc['product']})."
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Identify whether this business is extracting raw materials, manufacturing them, or selling them.",
                'tier_2': "Primary extracts raw materials; Secondary processes or manufactures goods; Tertiary provides services or retail.",
                'tier_3': "A factory that processes raw materials into finished goods belongs to the Secondary sector."
            },
            'misconception_tags': ['secondary_vs_primary_confusion', 'secondary_vs_tertiary_confusion']
        }, subskill='elementary_sectors', learning_objective_id='lo_ems_prod_sectors', question_family_id='sector_id', concept_id='secondary_manufacturing'),

        _with_metadata({
            'title': 'Interdependence of Production Sectors',
            'prompt': (
                f"In the production chain for {sc['product']}, explain what happens to the {sc['tertiary']} "
                f"if a prolonged drought or strike prevents {sc['primary']} from supplying {sc['raw']}. (4 marks)"
            ),
            'marks': 4,
            'marking_points': [
                f"Without raw materials ({sc['raw']}), the secondary processor cannot produce {sc['product']}.",
                "The supply chain halts due to the interdependence of economic sectors.",
                f"The {sc['tertiary']} will face stock shortages and cannot make sales to consumers.",
                "The business loses revenue, which threatens jobs and business profitability."
            ],
            'sample_answer': (
                f"Because economic sectors are interdependent, if the primary producer cannot supply {sc['raw']}, "
                f"the secondary factory cannot manufacture {sc['product']}. As a result, the {sc['tertiary']} "
                f"will have no goods to sell to consumers, causing lost revenue, stock shortages, and potential worker layoffs."
            ),
            'difficulties': ['medium', 'hard'],
            'hints': {
                'tier_1': "Consider the domino effect across the three sectors of production.",
                'tier_2': "Explain how a failure in the primary sector directly stops the secondary and tertiary sectors.",
                'tier_3': "Point 1: Secondary cannot produce. Point 2: Tertiary has no stock to sell. Point 3: Lost sales and income."
            },
            'misconception_tags': ['sector_interdependence_omission']
        }, subskill='elementary_sectors', learning_objective_id='lo_ems_prod_interdependence', question_family_id='sector_chain', concept_id='interdependence')
    ]

def _build_inputs_outputs_questions(rng):
    sc = get_ems_scenario(rng)
    batches = [
        {
            'business': f"{sc['entrepreneur']}'s Bakery in {sc['area']}",
            'inputs': ['Flour', 'Yeast', 'Water', "Baker's labour", 'Electric ovens'],
            'process': ['Mixing ingredients', 'Kneading dough', 'Baking in ovens'],
            'outputs': ['Loaves of fresh bread', 'Breadcrumbs'],
            'waste': 'Empty flour sacks and burnt crusts'
        },
        {
            'business': f"{f"{sc['entrepreneur']} Enterprises"} (a school uniform manufacturer in {sc['area']})",
            'inputs': ['Cotton fabric', 'Buttons', 'Sewing machine operators', 'Industrial sewing machines'],
            'process': ['Pattern cutting', 'Stitching seams', 'Attaching buttons and ironing'],
            'outputs': ['Completed school shirts and skirts'],
            'waste': 'Off-cut fabric scraps'
        },
        {
            'business': f"{sc['entrepreneur']}'s Fruit Juice Plant in {sc['area']}",
            'inputs': ['Fresh oranges', 'Purified water', 'Cardboard cartons', 'Factory workers', 'Juicing presses'],
            'process': ['Washing fruit', 'Pressing juice', 'Pasteurisation and bottling'],
            'outputs': ['Sealed 1-litre orange juice cartons'],
            'waste': 'Orange peel and pulp'
        },
        {
            'business': f"{f"{sc['entrepreneur']} Enterprises"} (a wooden furniture workshop in {sc['area']})",
            'inputs': ['Pine timber boards', 'Wood glue and varnish', 'Carpenters', 'Table saws and sanders'],
            'process': ['Measuring and cutting wood', 'Assembling joints', 'Sanding and varnishing'],
            'outputs': ['Handcrafted dining tables and chairs'],
            'waste': 'Wood shavings and sawdust'
        },
        {
            'business': f"{sc['entrepreneur']}'s Dairy Creamery in {sc['area']}",
            'inputs': ["Raw cow's milk", 'Starter cultures', 'Cream separators', 'Pasteurisers'],
            'process': ['Separating cream', 'Churning and fermenting', 'Moulding and packaging'],
            'outputs': ['Blocks of cheddar cheese and butter'],
            'waste': 'Liquid whey by-product'
        },
        {
            'business': f"{f"{sc['entrepreneur']} Enterprises"} (a brick manufacturing yard in {sc['area']})",
            'inputs': ['Clay', 'Sand', 'Water', 'Kiln operators', 'Mixing pugmills'],
            'process': ['Extruding clay into brick shapes', 'Sun drying', 'Firing in high-heat kilns'],
            'outputs': ['Fired building bricks and paving stones'],
            'waste': 'Cracked unusable brick fragments'
        }
    ]
    b = rng.choice(batches)
    
    return [
        _with_metadata({
            'title': 'Inputs, Processing, and Outputs',
            'prompt': (
                f"Consider {b['business']}. Which of the following correctly classifies an INPUT versus an OUTPUT in this production process?"
            ),
            'options': [
                f"Input: {b['inputs'][0]} | Output: {b['outputs'][0]}",
                f"Input: {b['outputs'][0]} | Output: {b['inputs'][0]}",
                f"Input: {b['process'][0]} | Output: {b['inputs'][1]}",
                f"Input: {b['waste']} | Output: {b['process'][1]}"
            ],
            'correct_index': 0,
            'explanation': (
                f"Inputs are the raw resources and materials brought into the business (e.g. {b['inputs'][0]}), "
                f"while outputs are the final finished goods created for sale (e.g. {b['outputs'][0]})."
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Distinguish between what enters the factory versus what leaves the factory as a finished good.",
                'tier_2': "Inputs = resources/materials used up. Processing = manufacturing actions. Outputs = final finished goods.",
                'tier_3': f"Input is {b['inputs'][0]} and output is {b['outputs'][0]}."
            },
            'misconception_tags': ['input_output_inversion']
        }, subskill='elementary_inputs_outputs', learning_objective_id='lo_ems_inputs_outputs', question_family_id='in_out_id', concept_id='inputs_and_outputs')
    ]

def _build_productivity_questions(rng):
    scenario = get_ems_scenario(rng)
    workers_1 = rng.choice([4, 5, 6])
    hours_1 = 8
    output_1 = workers_1 * hours_1 * rng.choice([5, 6, 8])
    prod_1 = output_1 / (workers_1 * hours_1)
    
    workers_2 = workers_1
    hours_2 = 8
    # After installing new machinery
    output_2 = int(output_1 * rng.choice([1.4, 1.5, 1.6]))
    prod_2 = output_2 / (workers_2 * hours_2)

    return [
        _with_metadata({
            'title': 'Calculating Productivity Ratio',
            'prompt': (
                f"A workshop employs {workers_1} workers who each work {hours_1} hours in a day (total {workers_1 * hours_1} labour hours). "
                f"In one working day, the workshop produces {output_1} wooden chairs. "
                f"Calculate the labour productivity per hour."
            ),
            'options': [
                f"{prod_1:.1f} chairs per labour hour",
                f"{1/prod_1:.2f} chairs per labour hour",
                f"{output_1 / workers_1:.1f} chairs per labour hour",
                f"{workers_1 * hours_1 / 10:.1f} chairs per labour hour"
            ],
            'correct_index': 0,
            'explanation': (
                f"Productivity = Total Output / Total Input. "
                f"Here: {output_1} chairs / ({workers_1} × {hours_1} hours) = {output_1} / {workers_1 * hours_1} = {prod_1:.1f} chairs per hour."
            ),
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hints': {
                'tier_1': "Use the standard productivity formula: Productivity = Output ÷ Input.",
                'tier_2': f"Total output is {output_1} chairs. Total input is {workers_1} × {hours_1} = {workers_1 * hours_1} hours.",
                'tier_3': f"{output_1} ÷ {workers_1 * hours_1} = {prod_1:.1f} chairs per labour hour."
            },
            'misconception_tags': ['productivity_inversion_error', 'omitted_labour_hours']
        }, subskill='elementary_productivity', learning_objective_id='lo_ems_productivity_calc', question_family_id='prod_ratio', concept_id='productivity_formula'),

        _with_metadata({
            'title': 'Impact of Technology on Productivity',
            'prompt': (
                f"A factory in {scenario['area']} operated by {scenario['entrepreneur']} considers machinery upgrades. Explain how investing in automated machinery allows a business to increase productivity "
                f"and contribute to South Africa's economic growth. (4 marks)"
            ),
            'marks': 4,
            'marking_points': [
                "Automated machinery speeds up production and reduces errors/waste.",
                "More output is produced in the same or less time (higher Output/Input ratio).",
                "Lower production cost per unit allows the business to lower prices or expand.",
                "Higher national output contributes directly to Gross Domestic Product (GDP) growth."
            ],
            'sample_answer': (
                "Investing in modern machinery increases productivity by speeding up the manufacturing process and reducing errors, "
                "meaning more finished goods are produced from the same labour hours. Lowering the cost per unit enables the business "
                "to sell more competitively, hire skilled technicians, and boost overall national production (GDP)."
            ),
            'difficulties': ['medium', 'hard'],
            'hints': {
                'tier_1': "Relate machinery to output speed, waste reduction, and unit costs.",
                'tier_2': "Show how producing more output with the same input raises productivity and expands GDP.",
                'tier_3': "Point 1: Faster output and less waste. Point 2: Higher output/input ratio. Point 3: Contribution to national GDP."
            },
            'misconception_tags': ['vague_technology_answer']
        }, subskill='elementary_productivity', learning_objective_id='lo_ems_tech_productivity', question_family_id='tech_impact', concept_id='technology_and_gdp')
    ]

def _build_resources_questions(rng):
    scenario = get_ems_scenario(rng)
    return [
        _with_metadata({
            'title': 'Sustainable Resource Use in Production',
            'prompt': (
                f"A manufacturing plant in {scenario['area']} evaluates resource inputs. Which pair correctly identifies a RENEWABLE resource and a NON-RENEWABLE resource used in industrial production?"
            ),
            'options': [
                "Renewable: Pine timber from planted forests | Non-renewable: Coal burned in power stations",
                "Renewable: Crude petroleum oil | Non-renewable: Solar photovoltaic energy",
                "Renewable: Iron ore in open mines | Non-renewable: Wind energy",
                "Renewable: Gold bullion | Non-renewable: Fresh river water"
            ],
            'correct_index': 0,
            'explanation': (
                "Pine timber can be replanted and grown sustainably (renewable), whereas coal is a finite fossil fuel "
                "that cannot be replaced once extracted and combusted (non-renewable)."
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Recall which resources naturally replenish over a human lifetime versus those that exist in finite amounts.",
                'tier_2': "Renewable resources naturally replenish (trees, solar, wind). Non-renewable are finite (coal, oil, mineral ores).",
                'tier_3': "Planted timber is renewable; coal is a non-renewable fossil fuel."
            },
            'misconception_tags': ['renewable_vs_nonrenewable_confusion']
        }, subskill='elementary_resources', learning_objective_id='lo_ems_sustainability', question_family_id='resource_types', concept_id='sustainability')
    ]



SUBSKILLS = ['sector_id', 'sector_chain', 'in_out_id', 'prod_ratio', 'tech_impact', 'resource_types']



SUBSKILLS = ['sector_id', 'sector_chain', 'in_out_id', 'prod_ratio', 'tech_impact', 'resource_types']

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
