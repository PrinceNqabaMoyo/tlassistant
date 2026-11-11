import json

with open("caps-ai-backend/app/services/caps_term_registry_data.json", encoding="utf-8") as f:
    data = json.load(f)

gr9_math = [x for x in data if str(x.get("grade")) in ("9", "Grade 9") and "Math" in str(x.get("subject"))]
print(f"Total Grade 9 Mathematics topics in registry: {len(gr9_math)}")
for i, x in enumerate(gr9_math, 1):
    print(f"{i:02d}. Term {x.get('term')} | {x.get('name')} -> {x.get('generator_key')}")
