import json

data = json.load(open('reports/data/mathlit_audit_classified.json', 'r', encoding='utf-8'))
gnrs = [v for v in data.values() if v.get('grade') in (12, '12') and v.get('d2b_outcome') == 'GENERATED_NOT_RENDERED']
print(f"Total GNRs in Gr12: {len(gnrs)}")
for g in gnrs:
    print(f"{g['sub_id']} -> type: {g.get('diagram_type')} -> failures: {g.get('trace_failures')}")
