import csv
import json

with open('reports/topic_diagram_review.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    essential = [row for row in reader if row['proposed_need_tier'] == 'Essential']

with open('curriculum_diagram_registry.json', encoding='utf-8') as f:
    reg = json.load(f)
built_archetypes = reg['archetypes']

print(f"Total Essential topics in CSV: {len(essential)}")
print(f"Current archetypes in registry: {len(built_archetypes)}")

by_subject = {}
for e in essential:
    subj = e['subject']
    by_subject.setdefault(subj, []).append(e)

for subj, topics in by_subject.items():
    print(f"\n--- {subj} ({len(topics)} topics) ---")
    for t in topics:
        print(f"  Gr {t['grade']} T{t['term']}: {t['topic']} -> {t['proposed_modality']} (gen: {t['current_generator_state']}, rend: {t['current_renderer_state']})")
