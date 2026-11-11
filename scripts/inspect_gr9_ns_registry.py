import json

with open("caps-ai-backend/app/services/caps_term_registry_data.json", encoding="utf-8") as f:
    d = json.load(f)

gr9_ns = [x for x in d if str(x.get("grade")) in ("9", "Grade 9") and "natural" in str(x.get("subject")).lower()]
print(f"Total Grade 9 Natural Sciences topics in registry: {len(gr9_ns)}")
for i, x in enumerate(gr9_ns, 1):
    print(f"{i:02d}. Term {x.get('term')} | {x.get('name')} -> {x.get('generator_key')}")
