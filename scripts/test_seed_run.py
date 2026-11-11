import os
import sys
import json

backend_dir = os.path.abspath('caps-ai-backend')
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.services.generator_registry import generate_variant

test_cases = [
    ("Vectors in two dimensions", "11", "Physical Sciences"),
    ("Electric circuits", "10", "Physical Sciences"),
    ("Euclidean Geometry", "11", "Mathematics"),
    ("Genetics and inheritance", "12", "Life Sciences"),
    ("Cells as the basic units of life", "9", "Natural Sciences"),
    ("Cash receipts journal", "8", "Economic & Management Sciences"),
    ("Accounting principles", "10", "Accounting"),
    ("Micro environment", "10", "Business Studies"),
]

for topic, grade, subject in test_cases:
    print(f"\n--- Testing: {subject} Gr{grade} - {topic} ---")
    try:
        q1 = generate_variant(topic, grade=grade, subject=subject, seed=1)
        q2 = generate_variant(topic, grade=grade, subject=subject, seed=42)
        q = q1[0] if isinstance(q1, list) else q1
        q_alt = q2[0] if isinstance(q2, list) else q2
        modality = q.get("modality")
        specs = [k for k in q.keys() if 'spec' in k or k in ('circuit', 'fbd', 'diagram', 'journal', 'rows')]
        print(f"Modality: {modality}")
        print(f"Specs present: {specs}")
        if 'fbd_spec' in q:
            print("fbd_spec seed 1:", q['fbd_spec'])
            print("fbd_spec seed 42:", q_alt['fbd_spec'])
        elif 'circuit_spec' in q:
            print("circuit_spec seed 1:", q['circuit_spec'].get('battery'), q['circuit_spec'].get('resistors'))
            print("circuit_spec seed 42:", q_alt['circuit_spec'].get('battery'), q_alt['circuit_spec'].get('resistors'))
        elif 'punnett_spec' in q:
            print("punnett_spec seed 1:", q['punnett_spec'])
        elif 'diagram_spec' in q:
            print("diagram_spec seed 1 kind:", q['diagram_spec'].get('kind'))
    except Exception as e:
        print(f"Error: {e}")
