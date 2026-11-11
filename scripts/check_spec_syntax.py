import re

content = open("e2e/visual/diagrammatic_archetypes.spec.js", encoding="utf-8").read()
matches = [m.start() for m in re.finditer(r"physTabAid9", content)]
print(f"Matches for physTabAid9: {len(matches)}")
for p in matches:
    print(content[max(0, p-60):min(len(content), p+80)])
