import re
from pathlib import Path

ROOT = Path(".")
with open("caps-ai-backend/app/services/generator_registry.py", encoding="utf-8") as f:
    c = f.read()

for m in re.finditer(r'["\'](grade11_mathlit_\w+)["\']:\s*(\w+)', c):
    print(m.group(1), "->", m.group(2))

# Find imports of those functions
for line in c.splitlines():
    if "from app.utils" in line and ("gr11" in line or "grade11" in line or "mathematical_literacy" in line):
        print(line)
