import json

with open('curriculum_diagram_pipeline_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total topics where generator omits diagrams: {len(data['generator_omits_diagram'])}")
print(f"Total topics where generator is missing/crashing: {len(data['generator_missing'])}\n")

# Sample 15 topics across subjects
for item in data['generator_omits_diagram'][:15]:
    t = item['topic']
    sg = t['subject_grade']
    top = t['topic']
    ctx = t['diagram_contexts'][0] if t['diagram_contexts'] else 'None'
    q = t['sample_question'][:140] if t['sample_question'] else 'None'
    print(f"[{sg}] {top}")
    print(f"   Context: {ctx}")
    print(f"   Question: {q}...\n")
