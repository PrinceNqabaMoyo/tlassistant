from pathlib import Path

p = Path("caps-ai-backend/app/utils/mathematical_literacy/tariffs_tax_brackets_generator.py")
lines = p.read_text(encoding="utf-8").splitlines()

new_lines = []
skip = False
for line in lines:
    if '"diagram_spec": None,' in line:
        new_lines.append(line)
        skip = True
        continue
    if skip:
        if '"term": 1,' in line:
            skip = False
            new_lines.append(line)
        continue
    new_lines.append(line)

p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
print("Cleaned lines 291-295 successfully")
