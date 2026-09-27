import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.generator_registry import ALL_GENERATORS

keys_to_test = [
    "grade12_bs_legislation_hr",
    "grade12_bs_investments_management",
    "grade11_bs_marketing_production",
    "grade8_ems_gap"
]

success = True
for key in keys_to_test:
    try:
        gen = ALL_GENERATORS[key]
        print(f"Testing {key} (compound)...")
        res_compound = gen(mode="compound")
        assert "parts" in res_compound
        print(f"Testing {key} (elementary 1)...")
        
        # Test elementary modes based on the key
        if key == "grade12_bs_legislation_hr":
            gen(mode="elementary_legislation")
            gen(mode="elementary_hr_recruitment")
            gen(mode="elementary_salary_calc")
        elif key == "grade12_bs_investments_management":
            gen(mode="elementary_insurance")
            gen(mode="elementary_investments")
            gen(mode="elementary_management")
        elif key == "grade11_bs_marketing_production":
            gen(mode="elementary_marketing")
            gen(mode="elementary_production")
        elif key == "grade8_ems_gap":
            gen(mode="elementary_savings")
            gen(mode="elementary_production")
            
        print(f"SUCCESS for {key}")
    except Exception as e:
        print(f"FAILED for {key}: {e}")
        success = False

if success:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
