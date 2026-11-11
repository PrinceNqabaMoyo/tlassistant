import sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.natural_sciences.grade9 import (
    forces_generator,
    electric_cells_gen,
    resistance_generator,
    series_parallel_circuits,
    safety_electricity_gen,
    national_grid_generator,
    cost_electrical_energy,
)

gens = [
    ('forces_generator', forces_generator),
    ('electric_cells_gen', electric_cells_gen),
    ('resistance_generator', resistance_generator),
    ('series_parallel_circuits', series_parallel_circuits),
    ('safety_electricity_gen', safety_electricity_gen),
    ('national_grid_generator', national_grid_generator),
    ('cost_electrical_energy', cost_electrical_energy),
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
        assert res.get('term') == 3, f"{name} invalid term {res.get('term')}"
        assert len(res.get('question', '')) > 20, f"{name} invalid question"
        assert len(res.get('sample_answer', '')) > 20, f"{name} invalid sample"
        assert ('marking_guide' in res) or ('marking_schema' in res), f"{name} missing marking"
        assert len(res.get('hints', [])) >= 3, f"{name} missing hints"
        passed += 1
        print(f"PASS: {name} (seed {s}) -> subskill: {res.get('subskill')} | title: {res.get('title')}")

print(f"\nTERM 3 ALL PASS: {passed}/{total} verified (100%)")
