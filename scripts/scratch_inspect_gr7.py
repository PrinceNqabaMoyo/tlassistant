import json

with open("caps-ai-backend/app/services/caps_term_registry_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

gr7 = [t for t in data if str(t.get("grade")) == "7" and str(t.get("subject")).lower() == "mathematics"]
if gr7:
    print("Keys in gr7[0]:", list(gr7[0].keys()))
    print("Item 0:", gr7[0])
