import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', encoding='utf-8') as f:
    data = json.load(f)

for g in ['7', '8', '9', '10', '11', '12']:
    print(f"\n==================== GRADE {g} ====================")
    by_subj = {}
    for r in data:
        if str(r['grade']) == g:
            s = r['subject']
            if s not in by_subj:
                by_subj[s] = []
            by_subj[s].append(r['name'])
    for s, tops in sorted(by_subj.items()):
        print(f"  [{s}] ({len(tops)} topics): {', '.join(tops[:4])}")
