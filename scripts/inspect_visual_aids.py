"""Inspect visualAidRegistry.js to understand registered visual aids and topic mappings."""
import re
from pathlib import Path

path = Path("src/components/workspace/visual_aids/visualAidRegistry.js")
text = path.read_text(encoding="utf-8")

aid_ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", text)
print(f"Total visual aid IDs found: {len(aid_ids)}")
for aid in aid_ids:
    print(" -", aid)

print("\n--- Topic mappings / getAvailableVisualAids ---")
lines = text.splitlines()
in_func = False
for l in lines:
    if "function getAvailableVisualAids" in l or "export const getAvailableVisualAids" in l:
        in_func = True
    if in_func:
        print(l)
        if l.strip() == "}":
            break
