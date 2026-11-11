import re

content = open("src/components/workspace/UniversalWorkspace.jsx", encoding="utf-8").read()
print("Length of UniversalWorkspace:", len(content))

# Look for modality routing
matches = re.findall(r"modality\s*===?\s*['\"]([^'\"]+)['\"]", content)
print("Modality string matches:", set(matches))
