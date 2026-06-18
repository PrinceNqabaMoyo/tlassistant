import sys, os
sys.path.insert(0, '.')
from app.utils.grade10_accounting.indigenous_bookkeeping_generator_v2 import generate_questions

out_path = os.path.join(os.path.dirname(__file__), 'test_output.txt')

qs = generate_questions(subskill='mixed', count=20, seed=42)
lines = []
lines.append(f"Generated {len(qs)} questions\n")

types = {}
for q in qs:
    t = q['question_type']
    types[t] = types.get(t, 0) + 1
lines.append(f"Question type breakdown: {types}\n")

for i, q in enumerate(qs, 1):
    label = q['question_type'].upper()
    prompt = q['prompt'][:100]
    det = "DETERMINISTIC" if q['question_type'] not in ('typed', 'table') else "LLM-REQUIRED"
    lines.append(f"{i:2}. [{label:15}] [{det:13}] {prompt}...")

with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Output written to {out_path}")
