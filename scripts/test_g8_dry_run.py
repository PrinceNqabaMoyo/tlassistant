import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import get_topic_archetypes, generate_variant

g8_records = [r for r in _ALL_TOPIC_RECORDS if str(r.get('grade')) == '8']
print(f"Total Grade 8 topic records: {len(g8_records)}")

errors = []
total_archetypes = 0

for r in g8_records:
    subj = r['subject']
    top = r['name']
    info = get_topic_archetypes(top, '8', subj)
    archs = info.get('archetypes') or []
    if not archs:
        archs = ['default']
    
    for a in archs:
        total_archetypes += 1
        subskill = None if a == 'default' else a
        try:
            res = generate_variant(topic=top, grade='8', subject=subj, subskill=subskill, seed=101, count=1)
            q = res[0] if res else {}
            if not q or not isinstance(q, dict):
                errors.append(f"[{subj} | {top} | {a}] returned empty or non-dict: {type(q)}")
            elif not q.get('prompt') and not q.get('question'):
                errors.append(f"[{subj} | {top} | {a}] missing prompt/question: keys={list(q.keys())}")
        except Exception as e:
            errors.append(f"[{subj} | {top} | {a}] Exception: {e}")

print(f"Tested {total_archetypes} archetypes across {len(g8_records)} topics.")
print(f"Errors found: {len(errors)}")
for err in errors[:30]:
    print("  ERR:", err)
