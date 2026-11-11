import sys
from pathlib import Path

BACKEND_DIR = Path("caps-ai-backend")
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key, get_topic_archetypes
import json

manifest_path = Path("caps-ai-backend/app/services/caps_term_registry_data.json")
with open(manifest_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    if str(r.get("grade")) == "10" and "mathematical literacy" in r.get("subject", "").lower():
        tname = r.get("name")
        gkey = r.get("generator_key")
        res_key = resolve_generator_key(tname, grade="10", subject="Mathematical Literacy")
        gen_fn = ALL_GENERATORS.get(res_key)
        arch_info = get_topic_archetypes(tname, grade="10", subject="Mathematical Literacy")
        archs = arch_info.get("archetypes", [])
        print(f"Topic: '{tname}' | Manifest key: '{gkey}' | Resolved: '{res_key}' | Archetypes Count: {len(archs)}")
        # Generate 1 question to see what module it comes from
        try:
            sample = gen_fn(subskill=archs[0] if archs else None, seed=101)
            q = sample[0] if isinstance(sample, list) else sample
            print(f"   -> Sample Q ID: {q.get('question_id')}, Subskill: {q.get('subskill')}")
        except Exception as e:
            print(f"   -> ERROR generating: {e}")
