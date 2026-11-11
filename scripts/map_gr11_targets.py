"""Map each Grade 11 issue to its source file and function name."""
import json
import re
from pathlib import Path

ROOT = Path(".")
BASE = Path("caps-ai-backend/app/utils/mathematical_literacy")

with open("reports/data/mathlit_audit_classified.json", encoding="utf-8") as f:
    data = json.load(f)

target = [v for v in data.values() if str(v.get("grade")) == "11"]
issues = [v for v in target if v.get("d2b_outcome") == "MISSING" or v.get("d2a_need_class") == "DESCRIBED_NOT_DRAWN"]

print(f"Total Gr11 issues to map: {len(issues)}")

mapped = []
for v in issues:
    sub_id = v["sub_id"]
    gen_key = v.get("generator_key", "")
    sub = v.get("subskill", "")
    topic = v.get("topic", "")
    need = v.get("d2a_need_class", "")
    outcome = v.get("d2b_outcome", "")
    
    # Locate where sub is defined
    found_file = None
    found_fn = None
    
    # 1. Search in BASE / gen_key or BASE / topic_dir
    # Try all .py files in BASE and its subdirs
    for py_file in BASE.glob("**/*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue
        if sub in content:
            # Look for def generate_{sub} or def _gen_{sub} or def {sub}
            m = re.search(rf'def\s+(_gen_{sub}|generate_{sub}|{sub})\s*\(', content)
            if m:
                found_file = py_file
                found_fn = m.group(1)
                break
            # Or in DISPATCH_TABLE
            if f'"{sub}":' in content or f"'{sub}':" in content:
                m2 = re.search(rf'["\']{sub}["\']:\s*(\w+)', content)
                if m2:
                    found_file = py_file
                    found_fn = m2.group(1)
                    break
    mapped.append({
        "sub_id": sub_id,
        "gen_key": gen_key,
        "subskill": sub,
        "topic": topic,
        "need": need,
        "outcome": outcome,
        "file": str(found_file.relative_to(ROOT)).replace("\\", "/") if found_file else "NOT_FOUND",
        "fn": found_fn or "NOT_FOUND",
    })

print(f"Mapped {len(mapped)} subskills:")
by_file = {}
for m in mapped:
    by_file.setdefault(m["file"], []).append(m)

for f, subs in sorted(by_file.items()):
    print(f"\n=== {f} ({len(subs)}) ===")
    for s in subs:
        print(f"  {s['subskill']} -> {s['fn']} (need:{s['need']}, out:{s['outcome']})")

with open("reports/data/gr11_mapped_issues.json", "w", encoding="utf-8") as fp:
    json.dump(mapped, fp, indent=2)
