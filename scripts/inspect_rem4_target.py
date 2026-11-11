import json

data = json.load(open('reports/data/mathlit_audit_classified.json', encoding='utf-8'))
target = [
    v for v in data.values()
    if str(v.get('grade')) == '10' and v.get('topic') in (
        'Scale maps and plans',
        'Assembly diagrams floor plans and packaging'
    )
]

for v in target:
    print(f"{v['topic'][:15]} | {v['subskill']} | need={v.get('d2a_need_class')} | outcome={v.get('d2b_outcome')}")
