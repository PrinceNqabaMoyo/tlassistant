import json

d = json.load(open("caps-ai-backend/app/services/caps_term_registry_data.json", encoding="utf-8"))
for item in d:
    if item.get("grade") in (11, "11", "Grade 11") and "Literacy" in item.get("subject", ""):
        if item.get("term") in (3, "3", 4, "4"):
            print(json.dumps(item, indent=2))
