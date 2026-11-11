import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx in range(303, 328):
    item = data[idx]
    print(f'{idx}: T{item.get("term")} "{item.get("name")}" -> {item.get("generator_key")}')
