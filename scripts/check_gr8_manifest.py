import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

gr8 = [r for r in data if str(r.get('grade')) == '8']
print(f'Total Gr8 records in manifest: {len(gr8)}')
for r in gr8:
    print(r.get('subject'), '| Term', r.get('term'), '|', r.get('name'), '->', r.get('generator_key'))
