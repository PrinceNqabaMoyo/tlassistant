"""Inspect Grade 11 issues."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(".")
with open("reports/data/mathlit_audit_classified.json", encoding="utf-8") as f:
    data = json.load(f)

target = [v for v in data.values() if str(v.get("grade")) == "11"]
missing = [v for v in target if v.get("d2b_outcome") == "MISSING"]
gnr = [v for v in target if v.get("d2b_outcome") == "GENERATED_NOT_RENDERED"]
narrated = [v for v in target if v.get("d2a_need_class") == "DESCRIBED_NOT_DRAWN"]

print(f"Total Gr11: {len(target)}")
print(f"RENDERED: {len([v for v in target if v.get('d2b_outcome') == 'RENDERED'])}")
print(f"MISSING: {len(missing)}")
print(f"GNR: {len(gnr)}")
print(f"DESCRIBED: {len(narrated)}")

issues = {}
for v in missing + gnr + narrated:
    sub_id = v["sub_id"]
    issues[sub_id] = {
        "topic": v.get("topic"),
        "gen_key": v.get("generator_key"),
        "subskill": v.get("subskill"),
        "d2a_need": v.get("d2a_need_class"),
        "d2b_outcome": v.get("d2b_outcome"),
        "trace_fails": v.get("trace_failures"),
        "signals": v.get("signals"),
    }

with open("reports/data/mathlit_audit_payloads.json", encoding="utf-8") as f:
    payloads = json.load(f)

for sub_id, info in sorted(issues.items()):
    p_data = payloads.get(sub_id, {}).get("seeds", {}).get("101", {})
    prompt = p_data.get("prompt_text", "")
    refs = p_data.get("prompt_refs", [])
    desc = p_data.get("prompt_desc", {})
    print(f"\n[{sub_id}] ({info['topic']}) -> need:{info['d2a_need']} outcome:{info['d2b_outcome']}")
    print(f"  refs: {refs} | desc: {desc}")
    print(f"  prompt: {repr(prompt)[:180]}")
