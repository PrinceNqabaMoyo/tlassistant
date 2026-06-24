import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term1_source_documents'
CURRICULUM_REFERENCE = 'Term 1 > Source Documents'

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
    return [
        _with_metadata({
            'title': 'Purpose of a Receipt',
            'prompt': "What is the main purpose of a receipt as a source document?",
            'options': ["To request payment from a customer", "To provide proof that money has been received", "To record money owed to suppliers", "To calculate profit for the month"],
            'correct_index': 1,
            'explanation': "A receipt is a written acknowledgement that a specific amount of money has been received. It serves as proof of payment for both the buyer and the seller.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the role of a receipt in the accounting cycle.'},
                {'title': 'Reasoning path', 'text': 'Think about what happens when you buy something and receive a slip.'}
            ],
            'guidelines': ['Select the option about proof of payment.']
        }, subskill='concepts', learning_objective_id='lo_receipt_purpose', question_family_id='receipt_purpose_mcq', concept_id='receipt', concept_group='source_documents'),
        
        _with_metadata({
            'title': 'Deposit Slip Function',
            'prompt': "A deposit slip is used to:",
            'options': ["Withdraw cash from a bank account", "Record money paid to a supplier", "Deposit cash or cheques into a bank account", "Issue a receipt to a customer"],
            'correct_index': 2,
            'explanation': "A deposit slip is a form you fill out to deposit cash or cheques into a bank account. The bank stamps a copy as proof of the deposit.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose of a deposit slip.'},
                {'title': 'Reasoning path', 'text': 'The word "deposit" means to put money INTO an account.'}
            ],
            'guidelines': ['Select the option that describes putting money into the bank.']
        }, subskill='concepts', learning_objective_id='lo_deposit_slip', question_family_id='deposit_slip_mcq', concept_id='deposit_slip', concept_group='source_documents'),
        
        _with_metadata({
            'title': 'Source Document Rule',
            'prompt': "In accounting, the rule is: no source document, no entry in the books. Why is this rule important?",
            'options': ["It makes bookkeeping more complicated", "It ensures there is proof for every transaction recorded", "It prevents customers from paying", "It reduces the need for a bank account"],
            'correct_index': 1,
            'explanation': "The rule ensures that every transaction recorded in the books has an original source document as proof. This helps prevent fraud and provides evidence if disputes arise.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the importance of source documents in the accounting cycle.'},
                {'title': 'Reasoning path', 'text': 'Think about why businesses need proof of transactions.'}
            ],
            'guidelines': ['Select the option about proof and verification.']
        }, subskill='concepts', learning_objective_id='lo_source_document_rule', question_family_id='source_document_rule_mcq', concept_id='source_document_rule', concept_group='source_documents'),
        
        _with_metadata({
            'title': 'Bank Statement',
            'prompt': "Which of the following details would you find on a bank statement?",
            'options': ["The business's list of employees", "Deposits, withdrawals, and the bank balance", "The company's marketing strategy", "A list of suppliers' phone numbers"],
            'correct_index': 1,
            'explanation': "A bank statement shows all transactions that have gone through the bank account, including deposits, withdrawals, bank charges, and the current balance.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the content of a bank statement.'},
                {'title': 'Reasoning path', 'text': 'Think about what information your own bank sends you each month.'}
            ],
            'guidelines': ['Select the option about financial transactions.']
        }, subskill='concepts', learning_objective_id='lo_bank_statement', question_family_id='bank_statement_mcq', concept_id='bank_statement', concept_group='source_documents'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({
            'title': 'Source Documents Importance',
            'prompt': "Explain why source documents are considered the starting point of the accounting cycle. Mention two examples of source documents and what they prove. (4 marks)",
            'marks': 4,
            'marking_points': [
                "Source documents provide proof that a financial transaction took place.",
                "They contain details like date, amount, and reason for the transaction.",
                "Example: A receipt proves money was received.",
                "Example: A deposit slip proves money was deposited into the bank."
            ],
            'sample_answer': "Source documents are the starting point of the accounting cycle because they provide the original proof that a financial transaction took place. For example, a receipt proves that money was received from a customer, and a deposit slip proves that cash or cheques were deposited into the business bank account.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the role of source documents in accounting.'},
                {'title': 'Reasoning path', 'text': 'Think about what information an accountant needs before recording a transaction.'}
            ],
            'guidelines': ['Require an explanation of the role and two valid examples.']
        }, subskill='discussion', learning_objective_id='lo_source_documents_importance', question_family_id='source_documents_importance_essay', concept_id='source_documents_role', concept_group='source_documents'),
        
        _with_metadata({
            'title': 'Flow of Documents',
            'prompt': "Describe the flow of a receipt from the moment cash is received until it is used in the Cash Receipts Journal. (4 marks)",
            'marks': 4,
            'marking_points': [
                "The business receives cash from a customer.",
                "The business issues the original receipt to the customer.",
                "The business keeps a duplicate (copy) for records.",
                "The duplicate receipt is used as the source document to record in the CRJ."
            ],
            'sample_answer': "When a business receives cash from a customer, it issues the original receipt to the customer as proof of payment. The business keeps a duplicate copy for its own records. This duplicate receipt then becomes the source document used to record the transaction in the Cash Receipts Journal.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the flow of source documents in the accounting cycle.'},
                {'title': 'Reasoning path', 'text': 'Follow the journey of a receipt from customer hand to journal entry.'}
            ],
            'guidelines': ['Require the complete flow with all four steps.']
        }, subskill='discussion', learning_objective_id='lo_document_flow', question_family_id='document_flow_essay', concept_id='receipt_flow', concept_group='source_documents'),
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
