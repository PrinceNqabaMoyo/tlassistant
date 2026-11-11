"""Comprehensive verification of all 24 Grade 9 Natural Sciences dedicated generators across 4 distinct seeds."""

import sys
import json
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import ALL_GENERATORS

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    term_data = json.load(f)

gr9_ns_entries = [
    x for x in term_data
    if x.get('grade') == '9' and 'natural' in x.get('subject', '').lower()
]

SEEDS = [1, 7, 42, 99]
total_runs = 0
passed_runs = 0

print("=" * 80)
print(f"VERIFYING ALL 24 GRADE 9 NATURAL SCIENCES TOPIC GENERATORS ACROSS {len(SEEDS)} SEEDS")
print("=" * 80)

for entry in gr9_ns_entries:
    key = entry.get('generator_key')
    name = entry.get('name')
    term = entry.get('term')

    assert key in ALL_GENERATORS, f"Generator key '{key}' not in ALL_GENERATORS"
    fn = ALL_GENERATORS[key]

    for s in SEEDS:
        total_runs += 1
        res = fn(seed=s)

        # 1. Structural checks
        assert 'title' in res and res['title'], f"{key} (seed {s}) missing title"
        assert 'topic' in res and res['topic'], f"{key} (seed {s}) missing topic"
        assert res.get('grade') == '9', f"{key} (seed {s}) invalid grade: {res.get('grade')}"
        assert res.get('term') == term, f"{key} (seed {s}) term mismatch: {res.get('term')} vs {term}"

        # 2. Content checks
        q = res.get('question') or res.get('prompt') or res.get('question_text')
        assert q and len(q) > 20, f"{key} (seed {s}) question too short: {q}"

        ans = res.get('sample_answer') or res.get('correct_answer')
        assert ans and len(ans) > 20, f"{key} (seed {s}) sample answer too short"

        # 3. Marking guide
        marking = res.get('marking_guide') or res.get('marking_schema')
        assert marking, f"{key} (seed {s}) missing marking schema/guide"

        # 4. Hints (3-tier)
        hints = res.get('hints', [])
        assert len(hints) >= 3, f"{key} (seed {s}) fewer than 3 hints: {hints}"

        # 5. Misconception tags
        misconceptions = res.get('misconception_tags', [])
        assert isinstance(misconceptions, list), f"{key} (seed {s}) invalid misconception_tags"

        passed_runs += 1

    print(f"PASS (Term {term}) [4/4 seeds]: {key:38} | {name}")

print("=" * 80)
print(f"AUDIT COMPLETE: {passed_runs}/{total_runs} verification runs PASSED (100.0%)")
print("=" * 80)
