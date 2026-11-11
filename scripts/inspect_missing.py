import json

data = json.load(open('reports/data/mathlit_audit_classified.json', 'r', encoding='utf-8'))
missing = [v for v in data.values() if v.get('grade') in (12, '12') and v.get('d2b_outcome') == 'MISSING']
print(f"Total MISSING in Gr12: {len(missing)}")
for m in missing:
    print(f"{m['topic']} | {m['sub_id']}")
