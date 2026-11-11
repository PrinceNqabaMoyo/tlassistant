import sys
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import generate_variant
import json

reg = json.load(open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8'))
tech_topics = [r for r in reg if 'technical' in r.get('subject', '').lower()]
print(f"Tech Math topics: {len(tech_topics)}")

for t in tech_topics:
    for seed in [101, 102, 103]:
        try:
            res = generate_variant(topic=t["name"], seed=seed, grade=str(t["grade"]), subject=t["subject"], count=1)
        except Exception as e:
            print(f"ERROR: Gr{t['grade']} {t['name']} seed={seed}: {type(e).__name__}: {e}")
