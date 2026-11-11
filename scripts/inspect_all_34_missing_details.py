import json

data = json.load(open('reports/data/mathlit_audit_classified.json', 'r', encoding='utf-8'))
missing = [v for v in data.values() if v.get('grade') in (12, '12') and v.get('d2b_outcome') == 'MISSING']

print(f"Missing count: {len(missing)}")

# Load gr12_missing_map.json
with open('reports/data/gr12_missing_map.json', 'r', encoding='utf-8') as f:
    map_list = json.load(f)
map_by_sub = {m['sub_id']: m for m in map_list}

for m in missing:
    sid = m['sub_id']
    info = map_by_sub.get(sid, {})
    fn_name = info.get('fn_name', 'UNKNOWN')
    fpath = info.get('file', 'UNKNOWN')
    rel = fpath.split('caps-ai-backend')[-1] if 'caps-ai-backend' in fpath else fpath
    print(f"[{sid}] -> {fn_name} in {rel}")
