import os

source_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_scheme.svg")
target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "female_reproductive_cleaned.svg")

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('id="layer2"', 'id="layer2" style="display:none"'),
    ('id="g16826"', 'id="g16826" style="display:none"'),
    ('id="g16821"', 'id="g16821" style="display:none"'),
    ('id="path5057"', 'id="path5057" style="display:none"'),
    ('id="path5047"', 'id="path5047" style="display:none"'),
    ('id="path5049"', 'id="path5049" style="display:none"'),
]

for old, new in replacements:
    assert old in content, f"Expected {old} in content"
    content = content.replace(old, new, 1)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {target_path} ({os.path.getsize(target_path)} bytes)")
