"""Verify a single Business Studies topic generator exposes all six archetypes.

Usage:  python scripts/bs_check_topic.py grade10 grade10_bs_macro_environment
Prints the question-type mix per subskill and the distinct-pool size per archetype
(so it is obvious when a pool is thin). Exits non-zero if any archetype is missing.
"""
import sys
import os
import collections

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caps-ai-backend'))

from app.api import grade10_business_studies as g10
from app.api import grade11_business_studies as g11
from app.api import grade12_business_studies as g12

MODULES = {'grade10': g10, 'grade11': g11, 'grade12': g12}
SUBSKILLS = ['concepts', 'application', 'discussion', 'word_bank', 'matching',
             'crossword', 'essay', 'mixed']
# archetypes the contract requires a "rich" generator to expose
REQUIRED = ['concepts', 'application', 'discussion', 'word_bank', 'matching',
            'crossword', 'essay']
VALID_TYPES = {'mcq', 'typed', 'word_bank', 'matching_columns', 'crossword', 'essay'}


def main():
    grade = sys.argv[1]
    gens = MODULES[grade].GENERATORS
    wanted = sys.argv[2:] or list(gens)
    failed = []
    for topic in wanted:
        if topic not in gens:
            print(f'!! {topic}: NOT REGISTERED in {grade}')
            failed.append(topic)
            continue
        fn = gens[topic]
        gen = fn if (callable(fn) and not hasattr(fn, 'generate')) else fn.generate
        seen = {}
        bad = []
        for sk in SUBSKILLS:
            try:
                qs = gen(subskill=sk, difficulty='medium', count=200, seed=42)
            except Exception as exc:
                bad.append(f'{sk}: ERROR {type(exc).__name__}: {exc}')
                continue
            seen[sk] = qs
            for q in qs:
                if q.get('question_type') not in VALID_TYPES:
                    bad.append(f"{sk}: unknown type {q.get('question_type')}")
                if sk != 'mixed' and q:
                    pass
        print(f'\n{topic}')
        for sk in SUBSKILLS:
            qs = seen.get(sk, [])
            # distinct prompts = real authored volume
            prompts = {q.get('prompt') for q in qs}
            types = dict(collections.Counter(q.get('question_type', '?') for q in qs))
            print(f'   {sk:12s} n={len(qs):3d} unique={len(prompts):3d}  {types}')
        missing = [sk for sk in REQUIRED if not seen.get(sk)]
        if missing:
            print(f'   !! MISSING ARCHETYPES: {missing}')
            failed.append(topic)
        if bad:
            for b in sorted(set(bad))[:6]:
                print('   !', b)
            failed.append(topic)
    print('\nFAILED TOPICS:', failed or 'none')
    return 1 if failed else 0


sys.exit(main())
