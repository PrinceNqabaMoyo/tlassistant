import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
reg_path = os.path.join(ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")
reg = json.load(open(reg_path, encoding="utf-8"))

ems_g8 = [t for t in reg if t.get("grade") == "8" and t.get("subject", "").lower() == "economic and management sciences"]
print(f"Total G8 EMS entries: {len(ems_g8)}")
for t in ems_g8:
    print(f"Term {t.get('term')}: '{t.get('name')}' -> key: '{t.get('generator_key')}'")

sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
from app.services.generator_registry import GRADE8_EMS_GENERATORS

print("\n--- Generator Modules for G8 EMS ---")
for t in ems_g8:
    key = t.get('generator_key')
    gen = GRADE8_EMS_GENERATORS.get(key)
    mod = getattr(gen, '__module__', 'UNKNOWN')
    print(f"Key: {key:<35} -> module: {mod}")
