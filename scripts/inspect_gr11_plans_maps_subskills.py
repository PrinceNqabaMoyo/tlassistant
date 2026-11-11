"""Inspect the exact subskills in gr11 plans and maps."""
import re
from pathlib import Path

ROOT = Path(".")
base_plans = Path("caps-ai-backend/app/utils/mathematical_literacy/gr11_plans_representations")
base_maps = Path("caps-ai-backend/app/utils/mathematical_literacy/gr11_maps")

plans_subs = [
    "subskill_2", "subskill_3", "subskill_11", "subskill_12", "subskill_13",
    "subskill_14", "subskill_15", "subskill_17", "subskill_29", "subskill_30",
    "subskill_33", "subskill_34", "subskill_36", "subskill_42"
]

maps_subs = [
    "subskill_3", "subskill_5", "subskill_7", "subskill_9", "subskill_16",
    "subskill_17", "subskill_37", "subskill_38", "subskill_39", "subskill_41", "subskill_43"
]

def find_subs(base_dir, subs):
    for f in base_dir.glob("*.py"):
        if f.name in ("common.py", "__init__.py"):
            continue
        c = f.read_text(encoding="utf-8")
        for s in subs:
            if s in c:
                m = re.search(rf'def _gen_{s}.*?(?=\ndef |$)', c, re.DOTALL)
                if not m:
                    m = re.search(rf'def {s}.*?(?=\ndef |$)', c, re.DOTALL)
                print(f"[{f.name}] {s}")
                if m:
                    # print first 6 lines of function
                    lines = m.group(0).splitlines()[:10]
                    for l in lines:
                        print("  ", l)

print("=== PLANS ===")
find_subs(base_plans, plans_subs)
print("\n=== MAPS ===")
find_subs(base_maps, maps_subs)
