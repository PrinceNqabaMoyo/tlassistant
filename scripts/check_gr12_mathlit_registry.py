import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    reg = json.load(f)

gr12_ml = [x for x in reg if str(x.get('grade')) == '12' and x.get('subject') == 'Mathematical Literacy']
for i, x in enumerate(gr12_ml):
    print(f"{i+1}. Term {x.get('term')}: name='{x.get('name')}', key='{x.get('generator_key')}'")
