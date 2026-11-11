import os
import sys
import json
import traceback

sys.path.insert(0, os.path.abspath('caps-ai-backend'))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key, generate_variant
with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    registry = json.load(f)

gr9_math = [x for x in registry if str(x.get('grade')) == '9' and 'math' in x.get('subject', '').lower()]

print(f"Auditing {len(gr9_math)} Grade 9 Math registry topics...")

results = []

for i, reg in enumerate(gr9_math):
    term = reg.get('term')
    topic_name = reg.get('name')
    gen_key = reg.get('generator_key')
    
    resolved_key = resolve_generator_key(topic_name, grade='9', subject='Mathematics')
    
    status = 'OK'
    error_msg = ''
    sample_prompt = ''
    sample_ans = ''
    has_hints = False
    has_diagram = False
    archetypes = set()
    
    try:
        if resolved_key not in ALL_GENERATORS:
            status = 'MISSING_GENERATOR'
            error_msg = f"Key '{resolved_key}' not in ALL_GENERATORS"
        else:
            for seed in [1, 42, 99]:
                q = generate_variant(resolved_key, seed=seed, difficulty='medium', count=1)
                if isinstance(q, list):
                    q = q[0]
                if not q:
                    status = 'EMPTY_QUESTION'
                    break
                sample_prompt = q.get('prompt') or q.get('question') or ''
                sample_ans = str(q.get('correct_answer') or q.get('answer') or '')
                hints = q.get('hints') or []
                if hints:
                    has_hints = True
                if q.get('diagram') or q.get('diagram_spec') or q.get('diagram_type'):
                    has_diagram = True
                arch = q.get('subskill') or q.get('archetype') or q.get('type')
                if arch:
                    archetypes.add(arch)
    except Exception as e:
        status = 'CRASH'
        error_msg = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
    
    res = {
        'idx': i + 1,
        'term': term,
        'topic_name': topic_name,
        'reg_key': gen_key,
        'resolved_key': resolved_key,
        'status': status,
        'error': error_msg,
        'has_hints': has_hints,
        'has_diagram': has_diagram,
        'archetypes': list(archetypes),
        'sample_prompt': sample_prompt[:120].replace('\n', ' '),
        'sample_ans': sample_ans[:50]
    }
    results.append(res)
    print(f"[{i+1:02d}] T{term} '{topic_name}' -> key: {resolved_key} | Status: {status} | Hints: {has_hints} | Diag: {has_diagram} | Archs: {list(archetypes)[:2]}")

with open('reports/grade9_maths_live_audit.json', 'w', encoding='utf-8') as fp:
    json.dump(results, fp, indent=2)

print("\nAudit complete! Saved to reports/grade9_maths_live_audit.json")
