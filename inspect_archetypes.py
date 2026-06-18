import sys
import os
import json
import random

# Add backend directory to sys.path so we can import modules
sys.path.append(os.path.abspath(os.path.join('caps-ai-backend')))

try:
    from app.utils.grade10_accounting.sole_trader_generator import generate_questions as g10_st
    
    from app.utils.grade11_accounting.fixed_assets_generator import generate_questions as g11_fa
    from app.utils.grade11_accounting.partnership_ledger_generator import generate_questions as g11_pl
    from app.utils.grade11_accounting.partnership_balance_sheet_generator import generate_questions as g11_pbs
    from app.utils.grade11_accounting.reconciliation_generator import generate_questions as g11_recon
    from app.utils.grade11_accounting.income_statement_generator import generate_questions as g11_is
    
    from app.utils.grade12_accounting.company_general_ledger_generator import generate_questions as g12_gl
    from app.utils.grade12_accounting.financial_statements_notes_generator import generate_questions as g12_fs
    from app.utils.grade12_accounting.cash_flow_generator import generate_questions as g12_cf
    from app.utils.grade12_accounting.analysis_interpretation_generator import generate_questions as g12_ai
except Exception as e:
    print(f"Import error: {e}")
    sys.exit(1)

generators = [
    ("G10_SoleTrader", g10_st),
    ("G11_FixedAssets", g11_fa),
    ("G11_PartnershipLedger", g11_pl),
    ("G11_PartnershipBalanceSheet", g11_pbs),
    ("G11_Reconciliation", g11_recon),
    ("G11_IncomeStatement", g11_is),
    ("G12_CompanyLedger", g12_gl),
    ("G12_FinancialStatements", g12_fs),
    ("G12_CashFlow", g12_cf),
    ("G12_AnalysisInterpretation", g12_ai)
]

seen_archetypes = {}

# Generate a bunch of questions to discover archetypes
for name, gen_func in generators:
    # try multiple seeds to get variety
    for seed in range(5):
        try:
            questions = gen_func(
                subskill="mixed",
                difficulty="mixed",
                question_type="mixed",
                count=10, # 10 questions per call
                seed=seed,
                mode="scaffold"
            )
            for q in questions:
                # if it's a bundle, look at its parts
                if q.get('question_type') == 'bundle':
                    bundle_prompt = q.get('prompt', '')
                    parts = q.get('parts', [])
                else:
                    bundle_prompt = ''
                    parts = [q]
                
                for part in parts:
                    q_type = part.get('question_type')
                    if q_type not in ('journal', 'ledger', 'calc', 'table_wordbank', 'accounting_equation'):
                        continue # focus on tabular and calc
                    
                    arch_key = part.get('meta', {}).get('archetype_key') or part.get('archetype_key')
                    if not arch_key:
                        arch_key = f"{name}_unknown_{q_type}"
                    
                    if arch_key not in seen_archetypes:
                        # Extract the required info
                        extracted = {
                            "grade_module": name,
                            "archetype_key": arch_key,
                            "question_type": q_type,
                            "full_prompt": (bundle_prompt + "\n\n" + part.get('prompt', '')).strip(),
                            "title_fields": part.get('journal', {}).get('title_fields') or part.get('title_fields', []),
                        }
                        
                        if q_type in ('journal', 'ledger', 'accounting_equation'):
                            # get the correct map and the headers
                            cmap = part.get('journal', {}).get('correct_map') or part.get('correct_map')
                            extracted['correct_map'] = cmap
                            extracted['headers'] = part.get('journal', {}).get('headers') or part.get('headers')
                            extracted['rows'] = part.get('journal', {}).get('rows') or part.get('rows')
                        elif q_type == 'table_wordbank':
                            cmap = part.get('correct_map')
                            extracted['correct_map'] = cmap
                            extracted['headers'] = part.get('headers')
                            extracted['rows'] = part.get('rows')
                        elif q_type == 'calc':
                            extracted['correct_value'] = part.get('correct_value')
                            extracted['unit'] = part.get('unit', '')
                        
                        seen_archetypes[arch_key] = extracted
        except Exception as e:
            pass # ignore errors, maybe some combinations fail

output_file = 'archetypes_sample_full.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(list(seen_archetypes.values()), f, indent=2)

print(f"Sampled {len(seen_archetypes)} archetypes. Written to {output_file}")
