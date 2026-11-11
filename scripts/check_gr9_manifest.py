import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import get_topic_archetypes, generate_variant

recs = [r for r in _ALL_TOPIC_RECORDS if str(r.get('grade')) == '9']
print(f'Total Gr9 topics: {len(recs)}')
issues = []
for r in recs:
    subj, top = r['subject'], r['name']
    info = get_topic_archetypes(top, '9', subj)
    archs = info.get('archetypes') or []
    if len(archs) < 3:
        issues.append(f'Few archetypes: {subj} | Gr9 | {top} -> {archs}')
    try:
        qs = generate_variant(top, grade='9', subject=subj, seed=101, count=max(len(archs), 5))
        if not qs:
            issues.append(f'Zero questions: {subj} | Gr9 | {top}')
    except Exception as e:
        issues.append(f'Crash: {subj} | Gr9 | {top}: {e}')

print(f'Grade 9 dry-run finished. Total issues: {len(issues)}')
for iss in issues[:20]:
    print('  -', iss)
