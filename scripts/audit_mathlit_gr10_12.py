"""Audit all Mathematical Literacy topics for Grades 10, 11, and 12."""
import json
import inspect
import sys
from pathlib import Path

# Add backend to sys.path
backend_dir = Path("caps-ai-backend").resolve()
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.services.generator_registry import ALL_GENERATORS

term_reg_path = Path("caps-ai-backend/app/services/caps_term_registry_data.json")
data = json.loads(term_reg_path.read_text(encoding="utf-8"))

print("=" * 80)
print("AUDIT: MATHEMATICAL LITERACY GRADES 10 TO 12 TOPICS & GENERATORS")
print("=" * 80)

results = {}

for grade in ["10", "11", "12"]:
    print(f"\n--- GRADE {grade} MATHEMATICAL LITERACY ---")
    topics = [r for r in data if str(r.get("grade")) == grade and "Mathematical Literacy" in r.get("subject", "")]
    print(f"Total topics registered in curriculum: {len(topics)}")

    results[grade] = []

    for idx, t in enumerate(topics, 1):
        name = t.get("name")
        term = t.get("term")
        gen_key = t.get("generator_key")
        registered = gen_key in ALL_GENERATORS

        subskills_count = 0
        mod_name = "N/A"
        if registered:
            fn = ALL_GENERATORS[gen_key]
            wrapped = getattr(fn, "_wrapped_func", fn)
            mod = inspect.getmodule(wrapped)
            if mod:
                mod_name = mod.__name__
                # Check get_subskills
                if hasattr(mod, "get_subskills"):
                    try:
                        subs = mod.get_subskills()
                        subskills_count = len(subs)
                    except Exception:
                        pass
                elif hasattr(mod, "SUBSKILLS"):
                    subskills_count = len(mod.SUBSKILLS)
                elif hasattr(mod, "SUBSKILL_LIST"):
                    subskills_count = len(mod.SUBSKILL_LIST)
                elif hasattr(mod, "DISPATCH_TABLE"):
                    subskills_count = len(mod.DISPATCH_TABLE)

        status_str = "PASS" if subskills_count >= 50 else f"FAIL ({subskills_count})"
        print(f"  [{idx:02d}] Term {term} | '{name}' | key: '{gen_key}' | subskills: {subskills_count} ({status_str}) | mod: {mod_name}")
        results[grade].append({
            "term": term,
            "name": name,
            "generator_key": gen_key,
            "subskills_count": subskills_count,
            "status": status_str,
            "module": mod_name
        })
