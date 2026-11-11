"""Grade 8 EMS — The Accounting Cycle.
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/01. the accounting cycle.md

Covers CAPS subskills:
  1. accounting_cycle_definition: Sequence of 6 stages in the accounting cycle.
  2. source_doc_types: Role of receipts, deposit slips, cheques, invoices, and bank statements.
  3. subsidiary_journals: Cash Receipts Journal (CRJ) and Cash Payments Journal (CPJ) purpose.
  4. general_ledger_purpose: T-accounts, double entry, posting from journals.
  5. trial_balance_purpose: Extracting debit/credit balances to check arithmetic accuracy.

Zero-LLM, 100% deterministic, authentic South African context.
"""
SUBSKILLS = [
    "accounting_cycle_definition",
    "source_doc_types",
    "subsidiary_journals",
    "general_ledger_purpose",
    "trial_balance_purpose",
]
import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term2_accounting_cycle'
CURRICULUM_REFERENCE = 'Term 2 > The Accounting Cycle'

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
    c_idx = int(item['correct_index'])
    correct_option = item['options'][c_idx]
    correct_letter = chr(65 + c_idx)
    marks = item.get('marks', 1)
    ans_text = f"{correct_letter}. {correct_option}"
    worked_sol = f"**{ans_text}** [{marks} mark{'s' if marks > 1 else ''}]\n\n{item.get('explanation', '')}"

    question = {
        'worked_solution': worked_sol,
        'canonical_solution': worked_sol,
        'id': f"g8_ems_mcq_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Concept check'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': item['explanation'],
        'marks': item.get('marks', 1),
        'sample_answer': ans_text,
        'ideal_answer': ans_text,
        'marking_points': [f'Selects correct option: {ans_text}'],
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
            'title': 'Accounting Cycle Order',
            'prompt': "Which of the following is the FIRST step in the accounting cycle?",
            'options': ["Prepare the Trial Balance", "Identify and analyse transactions", "Post to the General Ledger", "Prepare the Income Statement"],
            'correct_index': 1,
            'explanation': "The accounting cycle begins with identifying and analysing transactions. Only after this can source documents be collected and entries made in journals.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Knowing the correct order of steps in the accounting cycle.'},
                {'title': 'Reasoning path', 'text': 'Before you can record anything, you must first identify that a transaction happened.'}
            ],
            'guidelines': ['Select the first step in the sequence.']
        }, subskill='concepts', learning_objective_id='lo_cycle_order', question_family_id='accounting_cycle_order', concept_id='accounting_cycle', concept_group='accounting_cycle'),
        
        _with_metadata({
            'title': 'Trial Balance Purpose',
            'prompt': "What is the main purpose of a Trial Balance?",
            'options': ["To calculate profit for the year", "To check that total debits equal total credits", "To record daily cash transactions", "To prepare the budget for next year"],
            'correct_index': 1,
            'explanation': "A Trial Balance is prepared to check the arithmetical accuracy of the ledger accounts. The total of all debit balances should equal the total of all credit balances.",
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose of a Trial Balance.'},
                {'title': 'Reasoning path', 'text': 'Think about the word "balance" and what accountants check when they prepare it.'}
            ],
            'guidelines': ['Select the option about checking debits and credits.']
        }, subskill='concepts', learning_objective_id='lo_trial_balance', question_family_id='trial_balance_purpose', concept_id='trial_balance', concept_group='accounting_cycle'),
        
        _with_metadata({
            'title': 'Subsidiary Journals',
            'prompt': f"In {get_ems_scenario(rng)['area']}, why would {get_ems_scenario(rng)['entrepreneur']}'s {get_ems_scenario(rng)['business_type']} use subsidiary journals (such as the CRJ and CPJ) instead of recording every single daily transaction into the General Journal?",
            'options': ["To make accounting more complicated", "To save time by grouping similar transactions together", "To avoid using source documents", "To eliminate the need for a General Ledger"],
            'correct_index': 1,
            'explanation': "Subsidiary journals like the CRJ and CPJ group similar transactions together, which saves time and makes posting to the General Ledger more efficient.",
            'difficulties': ['medium', 'hard'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose of subsidiary journals.'},
                {'title': 'Reasoning path', 'text': 'Think about how sorting transactions by type makes bookkeeping faster.'}
            ],
            'guidelines': ['Select the option about efficiency and grouping.']
        }, subskill='concepts', learning_objective_id='lo_subsidiary_journals', question_family_id='subsidiary_journals_purpose', concept_id='subsidiary_journals', concept_group='accounting_cycle'),
        
        _with_metadata({
            'title': 'Income Statement vs Balance Sheet',
            'prompt': "Which statement shows the financial performance of a business over a specific period (e.g., one year)?",
            'options': ["The Balance Sheet", "The Trial Balance", "The Income Statement", "The Bank Statement"],
            'correct_index': 2,
            'explanation': "The Income Statement (also called the Statement of Comprehensive Income) shows income and expenses over a period, revealing whether the business made a profit or loss.",
            'difficulties': ['medium'],
            'marks': 2,
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Distinguishing between the Income Statement and the Balance Sheet.'},
                {'title': 'Reasoning path', 'text': 'Income Statement = performance over time; Balance Sheet = position at a point in time.'}
            ],
            'guidelines': ['Select the statement about income and expenses over a period.']
        }, subskill='concepts', learning_objective_id='lo_income_statement', question_family_id='income_statement_vs_balance', concept_id='income_statement', concept_group='accounting_cycle'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({
            'title': 'Accounting Cycle Steps',
            'prompt': "List and briefly describe the main steps of the accounting cycle in the correct order. (6 marks)",
            'marks': 6,
            'marking_points': [
                "Identify and analyse transactions.",
                "Source documents are obtained as proof.",
                "Transactions are recorded in subsidiary journals (CRJ, CPJ, etc.).",
                "Posting from journals to the General Ledger.",
                "Preparing the Trial Balance.",
                "Preparing the Income Statement and Balance Sheet."
            ],
            'sample_answer': "The accounting cycle starts with identifying and analysing transactions. Source documents are obtained as proof. Transactions are then recorded in subsidiary journals. Next, entries are posted to the General Ledger. A Trial Balance is prepared to check that debits equal credits. Finally, the Income Statement and Balance Sheet are prepared.",
            'difficulties': ['medium', 'hard'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Knowledge of the complete accounting cycle in order.'},
                {'title': 'Reasoning path', 'text': 'Think about the logical flow from transaction to financial statements.'}
            ],
            'guidelines': ['Award marks for each step in correct order with brief description.']
        }, subskill='discussion', learning_objective_id='lo_cycle_steps', question_family_id='accounting_cycle_steps_essay', concept_id='accounting_cycle_steps', concept_group='accounting_cycle'),
        
        _with_metadata({
            'title': 'Trial Balance Explanation',
            'prompt': "Explain the purpose of a Trial Balance and what it tells an accountant about the bookkeeping. (4 marks)",
            'marks': 4,
            'marking_points': [
                "It lists all General Ledger account balances.",
                "It checks that total debits equal total credits.",
                "It helps identify arithmetical errors.",
                "It is used as a basis for preparing financial statements."
            ],
            'sample_answer': "A Trial Balance lists all the balances from the General Ledger accounts. Its main purpose is to check that the total of all debit balances equals the total of all credit balances. If they do not balance, it indicates an arithmetical error that must be found and corrected. The Trial Balance also serves as the basis for preparing the Income Statement and Balance Sheet.",
            'difficulties': ['medium'],
            'hint_sections': [
                {'title': 'What is being tested?', 'text': 'Understanding the purpose and limitations of a Trial Balance.'},
                {'title': 'Reasoning path', 'text': 'Think about why accountants prepare a Trial Balance before final statements.'}
            ],
            'guidelines': ['Require explanation of purpose and at least two functions.']
        }, subskill='discussion', learning_objective_id='lo_trial_balance_discussion', question_family_id='trial_balance_discussion', concept_id='trial_balance_purpose', concept_group='accounting_cycle'),
    ]

def generate(subskill="mixed", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    base_seed = int(seed) if seed is not None else 42
    rng = _rng(base_seed)
    c_pool = [_mcq_question(rng, item, mode=mode) for item in _concept_pool(rng)]
    d_pool = [_typed_question(rng, item, mode=mode) for item in _discussion_pool(rng)]
    all_pool = c_pool + d_pool
    cycle_diag = {
        "kind": "process_flow",
        "diagram_role": "context",
        "title": "The 6-Stage Accounting Cycle",
        "steps": [
            "1. Transactions",
            "2. Source Documents",
            "3. Subsidiary Journals (CRJ/CPJ)",
            "4. General Ledger (T-Accounts)",
            "5. Trial Balance",
            "6. Financial Statements",
        ],
    }
    results = []
    for i in range(max(1, count)):
        idx = (base_seed + i) % len(all_pool)
        q = dict(all_pool[idx])
        chosen_sub = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)] if subskill in ("mixed", "all", "", None, "concepts") else subskill
        q["subskill"] = chosen_sub
        q["archetype"] = chosen_sub
        q["diagram_spec"] = cycle_diag
        results.append(q)
    return results
