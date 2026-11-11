import json

with open('curriculum_diagram_registry.json', encoding='utf-8') as f:
    d = json.load(f)

for a in d['archetypes']:
    if 'net' in a['id']:
        print(json.dumps(a, indent=2))
