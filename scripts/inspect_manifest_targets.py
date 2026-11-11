import json

entries = json.load(open('caps-ai-backend/app/services/caps_term_registry_data.json', encoding='utf-8'))
print("=== ACCOUNTING GR 10 ===")
for idx, e in enumerate(entries):
    if e['subject'] == 'Accounting' and str(e['grade']) == '10':
        print(f"{idx} T{e['term']}: '{e['name']}' -> {e['generator_key']}")
