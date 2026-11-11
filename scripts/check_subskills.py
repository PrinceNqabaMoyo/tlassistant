with open('caps-ai-backend/app/utils/grade7_mathematics/geometric_nets_3d_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'"subskill":\s*"([^"]+)"', text)
print('Subskills in q dicts in geometric_nets_3d_generator:', set(matches))

with open('caps-ai-backend/app/utils/grade7_mathematics/measurement_generator.py', 'r', encoding='utf-8') as f:
    text2 = f.read()

matches2 = re.findall(r'"subskill":\s*"([^"]+)"', text2)
print('Subskills in q dicts in measurement_generator:', set(matches2))
