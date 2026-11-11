import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

gr9_math = [x for x in data if str(x.get('grade')) == '9' and 'math' in x.get('subject', '').lower()]
for i, x in enumerate(gr9_math):
    print(f"{i+1:2d}. Term {x.get('term')}: '{x.get('name')}' -> generator_key='{x.get('generator_key')}'")
