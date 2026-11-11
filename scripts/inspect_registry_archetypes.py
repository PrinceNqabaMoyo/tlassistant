import json

with open('curriculum_diagram_registry.json', encoding='utf-8') as f:
    reg = json.load(f)

print(f"Total archetypes: {len(reg['archetypes'])}")
for a in reg['archetypes']:
    print(f"- {a['id']}: {a['subject']} Gr{a['grade']} T{a['term']} '{a['topic']}' -> {a['renderer']} (spec_key: {a.get('spec_key')})")

print(f"\nTotal visual aids: {len(reg.get('visual_aids', []))}")
for v in reg.get('visual_aids', []):
    print(f"- {v['id']}: {v['name']} ({v['subject']})")
