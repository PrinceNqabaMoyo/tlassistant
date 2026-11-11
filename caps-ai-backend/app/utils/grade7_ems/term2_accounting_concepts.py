import random
from app.utils.ems_namelist import get_ems_scenario, FINANCIAL_TERMS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade7_ems'
SUBTOPIC_ID = 'term2_accounting_concepts'
CURRICULUM_REFERENCE = 'Term 2 > Accounting Concepts'

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
    """Dynamic concept pool that utilizes ems_namelist and random money values for variations."""
    scenario = get_ems_scenario(rng)
    money_value = rng.randint(500, 10000)
    
    return [
        _with_metadata({
            'title': 'Identifying Capital',
            'prompt': f"{scenario['entrepreneur']} wants to start a business selling {scenario['item_sold']} in {scenario['area']}. They use R{money_value} of their own savings to start the business. In accounting terms, what is this money called?",
            'options': [
                "Assets", 
                "Capital", 
                "Liabilities", 
                "Expenses"
            ],
            'correct_index': 1,
            'explanation': "The money an owner uses to start a business is called Capital.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Identifying the accounting term for money used to start a business.'},
                {'title': 'Reasoning path', 'text': 'Think about what we call the owner\'s initial investment or contribution to the business.'},
                {'title': 'Transfer idea', 'text': 'Capital represents the owner\'s financial interest in the business.'}
            ],
            'guidelines': ['Identify the correct accounting term for start-up money.']
        }, subskill='concepts', learning_objective_id='lo_capital', question_family_id='identify_capital', concept_id='capital', concept_group='accounting_concepts', misconception_tags=['confuses_capital_with_income'], diagnostic_tags=['classification', 'accounting']),
        
        _with_metadata({
            'title': 'Identifying Liabilities',
            'prompt': f"{scenario['entrepreneur']} borrows R{money_value} from a bank to buy equipment for their business. What is this borrowed money called?",
            'options': [
                "Income", 
                "Owner's Equity", 
                "Liability", 
                "Current Asset"
            ],
            'correct_index': 2,
            'explanation': "Money that is owed to another party (like a bank loan) is a liability for the business.",
            'difficulties': ['easy', 'medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Classifying borrowed money in accounting.'},
                {'title': 'Reasoning path', 'text': 'If you borrow money, you owe it to someone else. What do we call a debt in accounting?'},
                {'title': 'Transfer idea', 'text': 'Liabilities are obligations or debts that the business must repay in the future.'}
            ],
            'guidelines': ['Select the term representing a debt owed by the business.']
        }, subskill='concepts', learning_objective_id='lo_liabilities', question_family_id='identify_liability', concept_id='liability', concept_group='accounting_concepts', misconception_tags=['thinks_loans_are_income'], diagnostic_tags=['classification', 'accounting']),
        
        _with_metadata({
            'title': 'Fixed vs Current Assets',
            'prompt': f"{scenario['entrepreneur']} in {scenario['area']} reviews business possessions. Which of the following describes a 'Current Asset'?",
            'options': [
                "Assets that are expected to last for a long time, like vehicles and buildings.", 
                "Temporary assets that can be converted into cash quite easily within a short period.", 
                "Money that is owed to a bank over a number of years.", 
                "The total profit made by a business in a year."
            ],
            'correct_index': 1,
            'explanation': "Current assets are temporary in nature and can be converted into cash quite easily (usually within a year). Fixed assets last a long time (like vehicles).",
            'difficulties': ['medium'],
            'marks': 1,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Differentiating between fixed and current assets.'},
                {'title': 'Reasoning path', 'text': 'Look at the word "current". It implies something happening now or in the short term. How does this apply to assets?'},
                {'title': 'Transfer idea', 'text': 'Cash in the bank or trading stock are current assets because they flow in and out constantly.'}
            ],
            'guidelines': ['Identify the definition of a current asset.']
        }, subskill='concepts', learning_objective_id='lo_current_assets', question_family_id='current_vs_fixed', concept_id='current_assets', concept_group='accounting_concepts', misconception_tags=['confuses_current_with_fixed'], diagnostic_tags=['definition', 'accounting']),
    ]

def _discussion_pool(rng):
    """Dynamic discussion pool that utilizes ems_namelist for variations."""
    scenario = get_ems_scenario(rng)
    
    return [
        _with_metadata({
            'title': 'Financial Records vs Transactions',
            'prompt': f"{scenario['entrepreneur']} conducts daily business activities in {scenario['area']}. Distinguish between financial records and financial transactions. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Financial transactions are the events where buyers and sellers exchange goods/services for money.",
                "Financial records are the physical/digital documents or records of those transactions."
            ],
            'sample_answer': "Financial transactions are the actual events at which buyers and sellers exchange assets or goods for money. Financial records are the written or electronic documents that keep a record of those transactions (like a till slip).",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the difference between an economic event and the documentation of that event.'},
                {'title': 'Reasoning path', 'text': 'When you buy something at a shop, the act of handing over cash and taking the item is the transaction. What is the till slip they give you?'},
                {'title': 'Transfer idea', 'text': 'Transactions happen in real life; records are how we track them for accounting.'}
            ],
            'guidelines': ['Ensure the answer defines both terms and explicitly states the difference (event vs documentation).'],
            'teaching_note': 'Learners often use the terms interchangeably. Emphasize that the record PROVES the transaction happened.'
        }, subskill='discussion', learning_objective_id='lo_records_vs_transactions', question_family_id='records_transactions_distinction', concept_id='financial_records', concept_group='accounting_concepts', misconception_tags=['confuses_record_with_transaction'], diagnostic_tags=['explanation', 'accounting']),
        
        _with_metadata({
            'title': 'Importance of Financial Records',
            'prompt': f"{scenario['entrepreneur']} runs a business in {scenario['area']}. Explain why it is important for businesses like theirs to keep financial records. (4 marks)",
            'marks': 4,
            'marking_points': [
                "To prevent fraud or theft within the business.",
                "To provide documentation to the South African Revenue Services (SARS).",
                "To prove that the earnings and profits declared are correct.",
                "It is illegal not to keep financial records."
            ],
            'sample_answer': "It is important to keep financial records to prevent fraud. Furthermore, businesses must provide documentation to the South African Revenue Services (SARS) to prove that their declared earnings are correct. In fact, it is illegal not to keep financial records of a business’s earnings.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Explaining the legal and practical reasons for bookkeeping.'},
                {'title': 'Reasoning path', 'text': 'What happens if a business doesn\'t write down its income? How does the government know how much tax to charge? What stops employees from stealing?'},
                {'title': 'Transfer idea', 'text': 'Financial records are the ultimate proof of a business\'s operations and are legally required for tax purposes.'}
            ],
            'guidelines': ['Look for points on fraud prevention and SARS/legal requirements.'],
            'teaching_note': 'Ensure they mention SARS or tax requirements, as this is a key curriculum focus.'
        }, subskill='discussion', learning_objective_id='lo_importance_of_records', question_family_id='importance_of_records', concept_id='keeping_records', concept_group='accounting_concepts', misconception_tags=['thinks_records_are_optional'], diagnostic_tags=['explanation', 'accounting']),
    ]



def _tabular_pool(rng):
    scenario = get_ems_scenario(rng)
    equip_val = rng.randint(12, 35) * 1000
    loan_val = rng.randint(8, 20) * 1000
    cap_val = equip_val + rng.randint(5, 15) * 1000 - loan_val
    total_assets = equip_val + (cap_val + loan_val - equip_val)
    cash_val = total_assets - equip_val
    return [
        _with_metadata({
            'title': 'Accounting Concepts Classification & Net Worth Table',
            'question_type': 'journal',
            'modality': 'ledger',
            'solution_type': 'tabular_cells',
            'prompt': (
                f"{scenario['entrepreneur']} operates a {scenario['business_type']} in {scenario['area']}.\n\n"
                f"Complete the Accounting Concepts Schedule below using the following balances:\n"
                f"• Equipment & Tools (Fixed Asset): R{equip_val}\n"
                f"• Cash in Bank (Current Asset): R{cash_val}\n"
                f"• Bank Loan (Liability): R{loan_val}\n"
                f"Calculate Total Assets and Owner's Equity (Capital = Total Assets - Total Liabilities)."
            ),
            'marks': 4,
            'headers': ['Accounting Element / Item', 'Category', 'Amount (R)'],
            'rows': [
                [{'cell_id': 'r0_c0', 'value': 'Equipment & Tools', 'editable': False}, {'cell_id': 'r0_c1', 'value': 'Fixed Asset', 'editable': False}, {'cell_id': 'r0_c2', 'value': '', 'expected': str(equip_val), 'editable': True}],
                [{'cell_id': 'r1_c0', 'value': 'Cash in Bank', 'editable': False}, {'cell_id': 'r1_c1', 'value': 'Current Asset', 'editable': False}, {'cell_id': 'r1_c2', 'value': '', 'expected': str(cash_val), 'editable': True}],
                [{'cell_id': 'r2_c0', 'value': 'Total Assets', 'editable': False}, {'cell_id': 'r2_c1', 'value': 'Assets', 'editable': False}, {'cell_id': 'r2_c2', 'value': '', 'expected': str(total_assets), 'editable': True}],
                [{'cell_id': 'r3_c0', 'value': 'Bank Loan', 'editable': False}, {'cell_id': 'r3_c1', 'value': 'Liability', 'editable': False}, {'cell_id': 'r3_c2', 'value': str(loan_val), 'editable': False}],
                [{'cell_id': 'r4_c0', 'value': "Owner's Equity (Capital)", 'editable': False}, {'cell_id': 'r4_c1', 'value': 'Capital', 'editable': False}, {'cell_id': 'r4_c2', 'value': '', 'expected': str(cap_val), 'editable': True}],
            ],
            'correct_map': {
                'r0_c2': str(equip_val),
                'r1_c2': str(cash_val),
                'r2_c2': str(total_assets),
                'r4_c2': str(cap_val),
            },
            'sample_answer': f"Equipment: R{equip_val}, Cash: R{cash_val}, Total Assets: R{total_assets}, Capital: R{cap_val}",
            'explanation': f"Total Assets = R{equip_val} + R{cash_val} = R{total_assets}. Owner's Equity = R{total_assets} - R{loan_val} = R{cap_val}.",
        }, subskill='accounting_classification_table', learning_objective_id='lo_accounting_table', question_family_id='accounting_classification_table', concept_id='accounting_table', concept_group='accounting_concepts')
    ]

SUBSKILLS = ['accounting_classification_table', 'identify_capital', 'identify_liability', 'current_vs_fixed', 'records_transactions_distinction', 'importance_of_records']





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
    for fn_name in ['_tabular_pool', '_concept_pool', '_discussion_pool', '_build_sectors_questions', '_build_inputs_outputs_questions', '_build_productivity_questions', '_build_resources_questions', '_build_savings_pool']:
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
        fn = (lambda r_arg, it_arg, mode='scaffold': it_arg) if item.get('modality') == 'ledger' else (_mcq_question if 'options' in item else _typed_question)
        return [fn(rng, item, mode=mode)]

    # Substring / partial match on subskill
    if target_sub and target_sub not in ("concepts", "discussion", "compound", "all", "mixed", "auto", "default", "none"):
        for k, it in fam_map.items():
            if target_sub in str(k).lower():
                fn = (lambda r_arg, it_arg, mode='scaffold': it_arg) if it.get('modality') == 'ledger' else (_mcq_question if 'options' in it else _typed_question)
                return [fn(rng, it, mode=mode)]

    # If count requested, generate count distinct questions cycling through SUBSKILLS
    results = []
    for i in range(count):
        sub_key = SUBSKILLS[i % len(SUBSKILLS)]
        item = fam_map.get(sub_key, all_items[i % len(all_items)])
        fn = (lambda r_arg, it_arg, mode='scaffold': it_arg) if item.get('modality') == 'ledger' else (_mcq_question if 'options' in item else _typed_question)
        results.append(fn(rng, item, mode=mode))
    return results
