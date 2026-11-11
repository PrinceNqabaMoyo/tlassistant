import sys
sys.path.insert(0, "caps-ai-backend")
import json
from app.services.generator_registry import ALL_GENERATORS, get_topic_archetypes

with open("caps-ai-backend/app/services/caps_term_registry_data.json", "r", encoding="utf-8") as f:
    reg = json.load(f)

gr8 = [t for t in reg if str(t.get("grade")) == "8" and str(t.get("subject")).lower() == "mathematics"]
print(f"Total Gr8 topics: {len(gr8)}")
for t in gr8:
    name = t.get("name")
    key = t.get("generator_key")
    gen = ALL_GENERATORS.get(key)
    arch = get_topic_archetypes(name, grade="8", subject="Mathematics")
    subskills = arch.get("subskills", [])
    mod_name = getattr(gen, "__module__", "unknown") if gen else "NONE"
    print(f"Topic: {name:<42} | Key: {key:<40} | Count: {len(subskills):<2} | Module: {mod_name}")
