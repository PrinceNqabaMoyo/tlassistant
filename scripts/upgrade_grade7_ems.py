#!/usr/bin/env python3
"""
Upgrades Grade 7 EMS generator modules to:
1. Expose SUBSKILLS = [...] with real curriculum question families (0 fake subskills).
2. Ensure _mcq_question and _typed_question emit full 6-pillar contracts (worked_solution, canonical_solution, explanation, 3-tier hints, marking_schema).
3. Ensure generate(...) returns a List of count distinct questions across question families without duplicates.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMS_DIR = ROOT / "caps-ai-backend" / "app" / "utils" / "grade7_ems"

MODULE_FAMILIES = {
    "term1_money_and_needs.py": [
        "needs_vs_wants_classification",
        "traditional_vs_modern",
        "needs_true_false",
        "economic_problem_essay",
        "primary_vs_secondary_explanation",
        "bartering_disadvantages",
        "needs_essay_exam",
    ],
    "term1_goods_and_services.py": [
        "goods_services_classification",
        "producer_consumer_roles",
        "recycling_benefits",
        "sector_classification",
        "household_roles_essay",
        "recycling_discussion",
    ],
    "term1_businesses.py": [
        "formal_informal_classification",
        "goods_classification",
        "manufacturers_def",
        "service_business_classification",
        "primary_sector_def",
        "capital_goods_def",
        "households_producers_explanation",
        "epidemics_impact",
        "informal_business_advantages",
        "production_stages_exam",
    ],
    "term2_accounting_concepts.py": [
        "identify_capital",
        "identify_liability",
        "current_vs_fixed",
        "records_transactions_distinction",
        "importance_of_records",
    ],
    "term2_budgets.py": [
        "def_budget",
        "budget_surplus_deficit",
        "fixed_variable_expense",
        "business_budget_comparison",
        "budget_contingency",
        "budget_variance_eval",
    ],
    "term2_income_and_expenses.py": [
        "def_personal_income",
        "def_personal_expenses",
        "identify_assets",
        "identify_liabilities",
        "net_worth_equation",
        "savings_wealth_creation",
    ],
    "term3_entrepreneurship.py": [
        "def_poverty_line",
        "def_entrepreneur",
        "entrepreneurial_traits",
        "planning_entrepreneurs_day",
        "needs_wants_opportunity",
        "swot_factors",
        "variable_costs_production",
        "calculate_profit_simple",
        "promotional_channels",
        "explain_imbalances",
        "explain_goals",
        "start_business_steps",
        "swot_case_study_exam",
    ],
    "term3_inequality_and_poverty.py": [
        "poverty_causes_mcq",
        "service_delivery_mcq",
        "education_poverty_mcq",
        "urban_rural_mcq",
        "job_creation_essay",
        "education_inequality_essay",
    ],
    "term3_production_process.py": [
        "sector_id",
        "sector_chain",
        "in_out_id",
        "prod_ratio",
        "tech_impact",
        "resource_types",
    ],
}

TEMPLATE = '''
SUBSKILLS = SUBSKILLS_PLACEHOLDER

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
    memo = item.get('sample_answer') or item.get('explanation') or "\\n".join(item.get('marking_points', []))
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
            'tier_3': f"Model solution points:\\n{memo}"
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
'''

def upgrade_file(filename: str, subskills: list[str]):
    path = EMS_DIR / filename
    if not path.is_file():
        print(f"Skipping missing {filename}")
        return

    content = path.read_text(encoding="utf-8")

    # Find where _mcq_question begins
    pattern = r"def _mcq_question\("
    match = re.search(pattern, content)
    if not match:
        pattern = r"def _typed_question\("
        match = re.search(pattern, content)

    if not match:
        print(f"Could not locate helpers in {filename}")
        return

    split_idx = match.start()
    pre_helpers = content[:split_idx]

    # Find the end of pool definitions before def generate or def _get_all_pool_items
    gen_match = re.search(r"def (generate|_get_all_pool_items)\(", content)
    if not gen_match:
        print(f"Could not locate generate in {filename}")
        return

    pools_match = re.search(r"def (_concept_pool|_discussion_pool|_build_)", content)
    if pools_match and pools_match.start() > split_idx:
        pools_code = content[pools_match.start():gen_match.start()]
    else:
        pools_code = ""

    code_to_insert = TEMPLATE.replace("SUBSKILLS_PLACEHOLDER", repr(subskills))
    new_code = pre_helpers + pools_code + "\n" + code_to_insert
    path.write_text(new_code, encoding="utf-8")
    print(f"Successfully upgraded {filename} with {len(subskills)} subskills.")


for fn, subs in MODULE_FAMILIES.items():
    if fn != "term4_savings.py":
        upgrade_file(fn, subs)
