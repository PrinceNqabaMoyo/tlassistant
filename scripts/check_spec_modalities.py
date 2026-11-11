content = open("e2e/visual/diagrammatic_archetypes.spec.js", encoding="utf-8").read()
import re
sections = re.findall(r"// MODALITY \d+.*", content)
for s in sections:
    print(s)
