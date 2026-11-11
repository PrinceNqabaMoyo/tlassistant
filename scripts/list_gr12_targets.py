import json

data = json.load(open('reports/data/mathlit_audit_classified.json', 'r', encoding='utf-8'))
items = [v for v in data.values() if v.get('grade') in (12, '12') and (v.get('d2b_outcome') in ('MISSING', 'GENERATED_NOT_RENDERED') or v.get('d2a_need_class') == 'DESCRIBED_NOT_DRAWN')]
print(f"Total target items in Gr12: {len(items)}")
for i, item in enumerate(items):
    print(f"{i+1}. [{item.get('topic')}] {item.get('sub_id')}")
    print(f"   d2a={item.get('d2a_need_class')} d2b={item.get('d2b_outcome')} type={item.get('diagram_type')} failures={item.get('trace_failures')}")
