"""Quick smoke test for all Term 2 generator imports and basic generation."""
import sys

tests = []

# Grade 10 Term 2
try:
    from app.utils.grade10_accounting.term2.salaries_wages_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr10 salaries_wages: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr10 salaries_wages: {e}")

try:
    from app.utils.grade10_accounting.term2.final_accounts_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr10 final_accounts: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr10 final_accounts: {e}")

try:
    from app.utils.grade10_accounting.term2.vat_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr10 vat: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr10 vat: {e}")

# Grade 11 Term 2
try:
    from app.utils.grade11_accounting.term2.clubs_nonprofit_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr11 clubs_nonprofit: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr11 clubs_nonprofit: {e}")

try:
    from app.utils.grade11_accounting.term2.analysis_interpretation_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr11 analysis_interpretation: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr11 analysis_interpretation: {e}")

# Grade 12 Term 2
try:
    from app.utils.grade12_accounting.term2.fixed_assets_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr12 fixed_assets: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr12 fixed_assets: {e}")

try:
    from app.utils.grade12_accounting.term2.inventory_systems_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr12 inventory_systems: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr12 inventory_systems: {e}")

try:
    from app.utils.grade12_accounting.term2.reconciliation_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr12 reconciliation: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr12 reconciliation: {e}")

try:
    from app.utils.grade12_accounting.term2.vat_generator import generate_questions as g
    qs = g(subskill="mixed", difficulty="easy", count=1, seed=42, mode="practice")
    tests.append(f"✓ Gr12 vat: {qs[0]['question_type']}")
except Exception as e:
    tests.append(f"✗ Gr12 vat: {e}")

print("\n=== Term 2 Generator Tests ===")
for t in tests:
    print(t)

passed = sum(1 for t in tests if t.startswith("✓"))
print(f"\n{passed}/{len(tests)} passed")
