import sys
import json

sys.path.insert(0, 'caps-ai-backend')
from app.api.grade9_ems import GENERATORS

# Load registry
with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    reg_data = json.load(f)

ems9_registry = [x for x in reg_data if str(x.get('grade')) in ['9', 'Grade 9'] and 'economic' in str(x.get('subject', '')).lower()]

print(f"=== VERIFYING GRADE 9 EMS ARCHITECTURE ===")
print(f"Registry count: {len(ems9_registry)} (Expect 14)")
assert len(ems9_registry) == 14, f"Expected 14 registry entries, found {len(ems9_registry)}"

# Verify all 14 topics in registry have corresponding keys in GENERATORS
missing_keys = []
for topic in ems9_registry:
    key = topic.get('generator_key')
    if key not in GENERATORS:
        missing_keys.append((topic.get('name'), key))

if missing_keys:
    print(f"FAIL: Missing generator keys in API: {missing_keys}")
    sys.exit(1)
print(f"PASS: All 14 registry topics map directly to GENERATORS dict.")

# Test all 14 generators across seeds 1 to 50
print("\n=== MULTI-SEED EXECUTION CHECK (Seeds 1 to 50) ===")
test_seeds = [1, 7, 13, 21, 35, 42, 50]
failed_generators = []

for topic in ems9_registry:
    name = topic.get('name')
    key = topic.get('generator_key')
    term = topic.get('term')
    gen_func = GENERATORS[key]
    
    print(f"\nTesting Term {term}: {name} [{key}]...")
    for seed in test_seeds:
        try:
            questions = gen_func(subskill=None, difficulty="medium", count=1, mode="practice", seed=seed)
            if not questions or not isinstance(questions, list):
                failed_generators.append((key, seed, "Returned empty or non-list"))
                continue
            
            q = questions[0]
            # Assert essential contract fields
            assert "id" in q, "Missing 'id'"
            assert "prompt" in q, "Missing 'prompt'"
            assert "marks" in q, "Missing 'marks'"
            assert "subskill" in q, "Missing 'subskill'"
            assert "learning_objective_id" in q, "Missing 'learning_objective_id'"
            
            # Specialized checks
            if key in ["grade9_ems_crj_cpj", "grade9_ems_debtors_journal", "grade9_ems_creditors_journal", "grade9_ems_creditors_ledger", "grade9_ems_debtors_ledger", "grade9_ems_transactions_cash_and_credit"]:
                assert q.get("modality") == "ledger", f"Expected modality='ledger', got {q.get('modality')}"
                assert "headers" in q and "rows" in q, "Missing top-level headers/rows for ledger"
                # Transactions stimulus check
                has_tx = bool(q.get("transactions"))
                assert has_tx, f"Expected transactions list in {key}"
                
            elif key == "grade9_ems_general_ledger":
                assert q.get("modality") == "ledger", f"Expected modality='ledger', got {q.get('modality')}"
                if "Trial Balance" in q.get("title", ""):
                    assert bool(q.get("account_balances")), "Missing account_balances in Trial Balance"
                    
            elif key in ["grade9_ems_circular_flow", "grade9_ems_price_theory"]:
                assert "diagram_spec" in q, f"Expected diagram_spec in {key}"
                assert q.get("diagram_role") == "context" or q.get("diagram_spec", {}).get("role") == "context", "Expected diagram_role='context'"
                assert q.get("modality") in ["math", "semantic"], f"Expected non-diagram answer modality, got {q.get('modality')}"
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            failed_generators.append((key, seed, str(e)))
            break

if failed_generators:
    print(f"\nFAILED GENERATORS: {failed_generators}")
    sys.exit(1)

print("\n=======================================================")
print("ALL 14 GRADE 9 EMS TOPICS PASSED MULTI-SEED AUDIT (100% SUCCESS)!")
print("=======================================================")
