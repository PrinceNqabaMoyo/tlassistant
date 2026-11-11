import json

with open("caps-ai-backend/app/services/caps_term_registry_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

gr8 = [t for t in data if str(t.get("grade")) == "8" and str(t.get("subject")).lower() == "mathematics"]
for i, t in enumerate(gr8, 1):
    print(f"{i:02d}: term={t.get('term')}, name='{t.get('name')}', key='{t.get('generator_key')}'")
