import sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.natural_sciences.grade9 import (
    earth_system_generator,
    lithosphere_generator,
    mining_resources_gen,
    atmosphere_generator,
    stellar_evolution_gen,
)

gens = [
    ('earth_system_generator', earth_system_generator),
    ('lithosphere_generator', lithosphere_generator),
    ('mining_resources_gen', mining_resources_gen),
    ('atmosphere_generator', atmosphere_generator),
    ('stellar_evolution_gen', stellar_evolution_gen),
]

seeds = [1, 7, 42, 99]
total = 0
passed = 0

for name, mod in gens:
    for s in seeds:
        total += 1
        res = mod.generate(seed=s)
        assert 'title' in res, f"{name} missing title"
        assert 'topic' in res, f"{name} missing topic"
        assert res.get('grade') == '9', f"{name} invalid grade {res.get('grade')}"
        assert res.get('term') == 4, f"{name} invalid term {res.get('term')}"
        assert len(res.get('question', '')) > 20, f"{name} invalid question"
        assert len(res.get('sample_answer', '')) > 20, f"{name} invalid sample"
        assert ('marking_guide' in res) or ('marking_schema' in res), f"{name} missing marking"
        assert len(res.get('hints', [])) >= 3, f"{name} missing hints"
        passed += 1
        print(f"PASS: {name} (seed {s}) -> subskill: {res.get('subskill')} | title: {res.get('title')}")

print(f"\nTERM 4 ALL PASS: {passed}/{total} verified (100%)")
