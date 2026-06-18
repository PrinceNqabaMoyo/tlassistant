import re

with open('src/components/workspace/registry/grade10Registry.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Available Modes matches:")
print(re.findall(r"availableModes:\s*\['scaffold',\s*'practice'\]", text))

print("Scaffold matches:")
print(repr(re.findall(r"if\s*\(\s*workspaceMode\s*===\s*'((?:grade10|grade11)_accounting_[a-zA-Z0-9_\-]+)_scaffold'\s*\)", text)))

print("Components found:")
print(repr(re.findall(r"(h\(\s*Grade10Accounting[a-zA-Z0-9]+Scaffold\s*,\s*\{)", text)))

print("Practice block matches:")
print(repr(re.findall(r"if\s*\(\s*workspaceMode\s*===\s*'(?:grade10|grade11)_accounting_[a-zA-Z0-9_\-]+_practice'\s*\)", text)))
