import json
from pathlib import Path

p = Path("caps-ai-backend/app/services/caps_term_registry_data.json")
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    if str(r.get("grade")) == "10" and "mathematical literacy" in r.get("subject", "").lower():
        print(f"Term {r.get('term')}: {r.get('name')} -> {r.get('generator_key')}")
