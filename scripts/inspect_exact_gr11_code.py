"""Inspect exact code of targets across all Gr11 files."""
import re
from pathlib import Path

BASE = Path("caps-ai-backend/app/utils/mathematical_literacy")

targets = [
    ("gr11_finance_tax", ["_gen_net_salary_calculation", "_gen_annual_net_tax_after_rebates", "_gen_net_paye_after_medical_credits", "_gen_salary_increase_net_impact", "_gen_budgeting_net_income_living_expenses"]),
    ("gr11_patterns_relationships/linear_patterns.py", ["generate_subskill_4"]),
    ("gr11_patterns_relationships/inverse_proportion.py", ["generate_subskill_10"]),
    ("gr11_patterns_relationships/constant_ratio_exponential.py", ["generate_subskill_26"]),
    ("gr11_patterns_relationships/breakeven_business.py", ["_gen_subskill_42"]),
    ("gr11_data_handling", ["41", "43", "47"]),
    ("gr11_financial_documents_tariffs_generator.py", ["subskill_9", "subskill_27", "subskill_35"]),
    ("gr11_weight_and_temperature_generator.py", ["subskill_32", "subskill_52"]),
    ("gr11_probability_generator.py", ["subskill_8", "subskill_45"]),
    ("gr11_exchange_rates", ["44"]),
    ("gr11_interest_banking_inflation", ["8"]),
]

for loc, fns in targets:
    p = BASE / loc
    print(f"\n==================== {loc} ====================")
    if p.is_file():
        files = [p]
    else:
        files = list(p.glob("*.py"))
    for f in files:
        if f.name in ("__init__.py", "common.py"):
            continue
        c = f.read_text(encoding="utf-8")
        for fn in fns:
            if fn in c:
                m = re.search(rf'def\s+(_gen_{fn}|generate_{fn}|{fn}|_gen_subskill_{fn}|generate_subskill_{fn})\s*\(.*?\)(?:\s*->\s*[^:]+)?:.*?(?=\ndef |\Z)', c, re.DOTALL)
                if m:
                    print(f"[{f.name}] {m.group(0).splitlines()[0]}")
                    # print first 5 and last 5 lines
                    lines = m.group(0).splitlines()
                    for l in lines[:4]:
                        print("  ", l)
                    print("   ...")
                    for l in lines[-4:]:
                        print("  ", l)
