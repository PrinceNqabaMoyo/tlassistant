import sys

sys.path.insert(0, r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend")

from app.utils.grade11_business_studies.term_1 import influences_on_business_environments_generator as m

items = m.generate(subskill='application', difficulty='medium', count=12, seed=7)
scenario_ids = [q.get('scenario_family_id') for q in items]
print(len(items))
print(any(s == 'supplier_competitor_regulator_response_case' for s in scenario_ids))
print(sorted({s for s in scenario_ids if s}))
