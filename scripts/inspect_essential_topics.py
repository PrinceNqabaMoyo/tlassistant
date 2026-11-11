import csv
import json

with open('reports/topic_diagram_review.csv', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

print(f"Total topics: {len(rows)}")

tiers = {}
for r in rows:
    t = r.get('proposed_need_tier', '')
    tiers[t] = tiers.get(t, 0) + 1

print("Tiers breakdown:", tiers)

with open('curriculum_diagram_registry.json', encoding='utf-8') as f:
    registry = json.load(f)

registered_archetypes = registry.get('archetypes', {})
print(f"Currently registered archetypes: {len(registered_archetypes)}")

essential = [r for r in rows if r.get('proposed_need_tier') == 'Essential']
print(f"Total Essential topics: {len(essential)}")

for idx, r in enumerate(essential, 1):
    print(f"[{idx}] Gr{r['grade']} {r['subject']} - T{r['term']}: {r['topic']} (Kinds: {r['source_diagram_kinds']}, Modality: {r['proposed_modality']})")
