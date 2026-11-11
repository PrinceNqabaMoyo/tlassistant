import re

content = open("src/components/workspace/UniversalWorkspace.jsx", encoding="utf-8").read()

for mod in ['geometric_nets', 'organic_chemistry', 'electrodynamics']:
    pos = content.find(f"'{mod}'")
    if pos == -1:
        pos = content.find(f'"{mod}"')
    if pos != -1:
        start = max(0, pos - 200)
        end = min(len(content), pos + 400)
        print(f"=== {mod} ===")
        print(content[start:end])
        print("...")
