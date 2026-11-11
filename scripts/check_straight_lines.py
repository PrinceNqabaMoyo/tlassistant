import json
with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for t in d:
    name = t.get('name', '')
    if 'straight' in name.lower() or 'line' in name.lower() or 'graph' in name.lower():
        print(f"Gr{t.get('grade')} | {name} -> {t.get('generator_key')}")
