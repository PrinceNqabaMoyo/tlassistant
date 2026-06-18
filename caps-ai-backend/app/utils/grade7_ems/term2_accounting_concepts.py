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
    """Dynamic concept pool that utilizes ems_namelist and random money values for variations."""
    scenario = get_ems_scenario()
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
            'prompt': "Which of the following describes a 'Current Asset'?",
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
    scenario = get_ems_scenario()
    
    return [
        _with_metadata({
            'title': 'Financial Records vs Transactions',
            'prompt': "Distinguish between financial records and financial transactions. (4 marks)",
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
