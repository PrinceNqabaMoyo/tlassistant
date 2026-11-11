"""Functional smoke test for Business Studies generators.

Usage:  python scripts/bs_generator_smoke.py grade10   (or grade11 / grade12 / all)
Prints, per topic, the pool sizes and question-type mix for every subskill key,
and flags pools that fail to generate or emit unknown shapes.
"""
import sys
import os
import collections

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caps-ai-backend'))

from app.api import grade10_business_studies as g10
from app.api import grade11_business_studies as g11
from app.api import grade12_business_studies as g12

SUBSKILLS = ['concepts', 'application', 'discussion', 'word_bank', 'matching',
             'crossword', 'essay', 'mixed']

VALID_TYPES = {'mcq', 'typed', 'word_bank', 'matching_columns', 'crossword', 'essay'}


def check(label, gens):
    print(f'\n===== {label} — {len(gens)} topics =====')
    problems = []
    for topic, gen in gens.items():
        fn = gen if (callable(gen) and not hasattr(gen, 'generate')) else gen.generate
        summary = {}
        for sk in SUBSKILLS:
            try:
                qs = fn(subskill=sk, difficulty='medium', count=200, seed=42)
            except TypeError:
                qs = fn(subskill=sk, difficulty='medium', count=200, seed=42)
            except Exception as exc:
                problems.append(f'{topic}/{sk}: ERROR {exc}')
                continue
            if not qs:
                continue
            types = collections.Counter(q.get('question_type', '?') for q in qs)
            summary[sk] = dict(types)
            for q in qs:
                if q.get('question_type') not in VALID_TYPES:
                    problems.append(f'{topic}/{sk}: unknown type {q.get("question_type")}')
        print(f'\n{topic}')
        for sk, t in summary.items():
            print(f'   {sk:14s} {sum(t.values()):3d}  {t}')
        keys = set(summary)
        missing = {'concepts', 'discussion', 'application', 'word_bank', 'matching', 'crossword', 'essay'} - keys
        if missing:
            print(f'   (no dedicated pool for: {sorted(missing)} -> falls back to mixed)')
    if problems:
        print('\n--- PROBLEMS ---')
        for p in problems:
            print('  !', p)
    return problems


targets = sys.argv[1] if len(sys.argv) > 1 else 'all'
all_problems = []
if targets in ('grade10', 'all'):
    all_problems += check('GRADE 10', g10.GENERATORS)
if targets in ('grade11', 'all'):
    all_problems += check('GRADE 11', g11.GENERATORS)
if targets in ('grade12', 'all'):
    all_problems += check('GRADE 12', g12.GENERATORS)
print('\nTOTAL PROBLEMS:', len(all_problems))
