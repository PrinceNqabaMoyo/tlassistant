import json
from pathlib import Path

p = Path("caps-ai-backend/app/data/diagram_archetypes_catalog.json")
if p.exists():
    data = json.load(open(p, encoding="utf-8"))
    print("Total in diagram_archetypes_catalog.json:", len(data))
    for a in data:
        if "math" in a.get("subject", "").lower():
            print(f"ID: {a.get('archetype_id')} | Topic: {a.get('topic')} | Grade: {a.get('grade')} | Subskill: {a.get('subskill_param')}")
else:
    print("diagram_archetypes_catalog.json does not exist!")
