import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    records = json.load(f)

gr8 = [r for r in records if str(r.get('grade')) == '8']
print(f'Total Grade 8 records: {len(gr8)}')
for r in gr8:
    s = r.get('subject')
    n = r.get('name')
    g = r.get('generator_key')
    a = r.get('archetypes', [])
    print(f"{s[:10]} | {n:<45} | gen={g:<35} | archs({len(a)})={a[:2]}")
