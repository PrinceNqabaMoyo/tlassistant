import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import get_generator_for_topic

tests = [
    ('Circulatory and respiratory systems', '9', 'Natural Sciences', 'respiratory'),
    ('Digestive system', '9', 'Natural Sciences', 'digestive_diagram'),
    ('Animal Nutrition', '11', 'Life Sciences', 'villus_and_macroscopic_anatomy'),
    ('Gaseous exchange', '11', 'Life Sciences', 'alveolus_gas_exchange_anatomy'),
    ('Excretion in humans', '11', 'Life Sciences', 'nephron_microstructure_anatomy'),
]

for t, g, s, sub in tests:
    fn = get_generator_for_topic(t, grade=g, subject=s)
    print(f"\n{s} Gr{g} '{t}' (subskill='{sub}'):")
    if fn:
        res = fn(seed=42, subskill=sub)
        q = res if isinstance(res, dict) else res[0]
        spec = q.get('diagram_spec') or q.get('diagram') or {}
        print(f"  master / image_type: {spec.get('image_type') or spec.get('master')}")
        print(f"  modality: {q.get('modality')}")
        print(f"  pins: {len(spec.get('pins', []))}")
        print(f"  prompt: {q.get('question') or q.get('prompt', '')[:60]}...")
