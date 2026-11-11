import sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.natural_sciences.grade9 import (
    compounds_generator,
    chemical_reactions_gen,
    reactions_metals_oxygen,
    reactions_nonmetals_ox,
    acids_bases_ph_gen,
    reactions_acids_bases,
    reactions_acids_metals,
)

gens = [
    ('compounds_generator', compounds_generator),
    ('chemical_reactions_gen', chemical_reactions_gen),
    ('reactions_metals_oxygen', reactions_metals_oxygen),
    ('reactions_nonmetals_ox', reactions_nonmetals_ox),
    ('acids_bases_ph_gen', acids_bases_ph_gen),
    ('reactions_acids_bases', reactions_acids_bases),
    ('reactions_acids_metals', reactions_acids_metals),
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
        assert res.get('term') == 2, f"{name} invalid term {res.get('term')}"
        assert len(res.get('question', '')) > 20, f"{name} invalid question"
        assert len(res.get('sample_answer', '')) > 20, f"{name} invalid sample"
        assert ('marking_guide' in res) or ('marking_schema' in res), f"{name} missing marking"
        assert len(res.get('hints', [])) >= 3, f"{name} missing hints"
        passed += 1
        print(f"PASS: {name} (seed {s}) -> subskill: {res.get('subskill')} | title: {res.get('title')}")

print(f"\nTERM 2 ALL PASS: {passed}/{total} verified (100%)")
