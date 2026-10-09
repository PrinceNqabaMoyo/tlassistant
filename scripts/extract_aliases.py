with open("caps-ai-backend/app/services/generator_registry.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

alias_start = None
alias_end = None
for i, line in enumerate(lines):
    if line.startswith("TOPIC_ALIASES: Dict[str, str] = {"):
        alias_start = i
    if alias_start is not None and line.startswith("}"):
        alias_end = i
        break

print(f"Found TOPIC_ALIASES from line {alias_start+1} to {alias_end+1}")
alias_content = "".join(lines[alias_start:alias_end+1])

header = '"""Topic alias mapping table for curriculum generators."""\nfrom typing import Dict\n\n'
with open("caps-ai-backend/app/services/generator_aliases.py", "w", encoding="utf-8") as f:
    f.write(header + alias_content + "\n")

print("Wrote generator_aliases.py successfully!")
