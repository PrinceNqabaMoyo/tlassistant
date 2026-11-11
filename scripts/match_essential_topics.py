import csv
import json

with open('reports/topic_diagram_review.csv', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

essential = [r for r in rows if r.get('proposed_need_tier') == 'Essential']

with open('curriculum_diagram_registry.json', encoding='utf-8') as f:
    registry = json.load(f)

raw_archetypes = registry.get('archetypes', [])
registered = {arch['id']: arch for arch in raw_archetypes}

print(f"Loaded {len(registered)} registered archetypes.")

# Let's list all registered archetypes and their evidence docs
print("\n--- REGISTERED ARCHETYPES ---")
for aid, arch in registered.items():
    print(f"  {aid}: {arch.get('name')} | Gr{arch.get('grade')} {arch.get('subject')} T{arch.get('term')} | {arch.get('topic')}")

print("\n--- Cross-referencing 52 Essential topics with registered archetypes ---")
matched = []
unmatched = []

for idx, r in enumerate(essential, 1):
    subj = r['subject']
    gr = int(r['grade'])
    top = r['topic']
    term = int(r['term'])
    
    found_keys = []
    for k, arch in registered.items():
        arch_subj = arch.get('subject')
        arch_gr = int(arch.get('grade', 0))
        arch_term = int(arch.get('term', 0))
        arch_top = arch.get('topic', '')
        arch_name = arch.get('name', '')
        
        # Check matching subject and grade
        if arch_subj == subj and arch_gr == gr:
            # Check topic match or term match
            top_words = [w.lower() for w in top.replace('&', ' ').replace('-', ' ').split() if len(w) > 3 and w.lower() not in ['geometry', 'term', 'systems', 'human', 'units', 'basic', 'objects', 'shapes']]
            if any(w in arch_top.lower() or w in arch_name.lower() or w in k.lower() for w in top_words):
                found_keys.append(k)
            elif arch_term == term and ('geometry' in top.lower() and 'geometry' in arch_top.lower()):
                found_keys.append(k)
            elif arch_term == term and ('circuit' in top.lower() and 'circuit' in arch_top.lower()):
                found_keys.append(k)
                
    if found_keys:
        matched.append((idx, gr, subj, top, found_keys))
    else:
        unmatched.append((idx, gr, subj, top, r['proposed_modality'], term))

print(f"\nMatched count: {len(matched)}")
for m in matched:
    print(f"  [OK] [{m[0]}] Gr{m[1]} {m[2]} (T{m[3]}): -> {m[4]}")

print(f"\nUnmatched count: {len(unmatched)}")
for u in unmatched:
    print(f"  [PENDING] [{u[0]}] Gr{u[1]} {u[2]} (Term {u[5]}): {u[3]} (Modality: {u[4]})")
