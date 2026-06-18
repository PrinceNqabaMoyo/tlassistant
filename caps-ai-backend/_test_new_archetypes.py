import json, sys
from app.utils.grade12_accounting.financial_statements_notes_generator import generate_questions as gq

results = {}
for sub in ['fixed-assets-note', 'trade-payables-note', 'cash-flow-statement']:
    try:
        q = gq(subskill=sub, difficulty='hard', mode='', count=1, seed=1)[0]
        qtype = q.get('question_type', '?')
        akey = q.get('meta', {}).get('archetype_key', '?')
        if qtype == 'bundle':
            parts = [p.get('meta', {}).get('archetype_key', '?') for p in q.get('parts', [])]
            akey = f"{akey} -> {parts}"
        results[sub] = {'ok': True, 'type': qtype, 'archetype': akey}
    except Exception as e:
        results[sub] = {'ok': False, 'error': str(e)}

out_path = r'c:\Users\princ\fundile-tlassistant-vite\_test_results.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print('Written to', out_path)
