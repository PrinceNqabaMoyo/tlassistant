content = open("caps-ai-backend/app/utils/grade10_life_sciences/cytology_mitosis_generator.py", encoding="utf-8").read()
import re
for m in re.finditer(r"diagram_spec", content):
    p = m.start()
    print(content[max(0, p-60):min(len(content), p+80)])
    print("---")
