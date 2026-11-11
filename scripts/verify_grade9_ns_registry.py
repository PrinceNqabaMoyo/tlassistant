import sys
import json
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import ALL_GENERATORS, get_generator_for_topic

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    term_data = json.load(f)

gr9_ns_entries = [
    x for x in term_data
    if x.get('grade') == '9' and 'natural' in x.get('subject', '').lower()
]

print(f"Total Grade 9 Natural Sciences curriculum topics in registry: {len(gr9_ns_entries)}")
assert len(gr9_ns_entries) == 24, f"Expected 24 topics, found {len(gr9_ns_entries)}"

missing = []
for entry in gr9_ns_entries:
    key = entry.get('generator_key')
    name = entry.get('name')
    term = entry.get('term')
    if key not in ALL_GENERATORS:
        missing.append((term, key, name))
    else:
        fn = ALL_GENERATORS[key]
        assert callable(fn), f"Generator for {key} is not callable!"
        # Test call
        res = fn(seed=42)
        assert res.get('grade') == '9', f"Grade mismatch for {key}: {res.get('grade')}"
        assert res.get('term') == term, f"Term mismatch for {key}: {res.get('term')} vs expected {term}"
        assert len(res.get('question', '')) > 20, f"Empty question for {key}"
        assert len(res.get('sample_answer', '')) > 20, f"Empty sample_answer for {key}"
        assert ('marking_guide' in res) or ('marking_schema' in res), f"Missing marking for {key}"
        assert len(res.get('hints', [])) >= 3, f"Fewer than 3 hints for {key}"
        print(f"PASS (Term {term}): '{key}' -> {res.get('title')} ({name})")

if missing:
    print(f"\nFAILED: Missing {len(missing)} generator keys:")
    for term, key, name in missing:
        print(f"  Term {term} | {key} | {name}")
    sys.exit(1)

print("\nALL 24 GRADE 9 NATURAL SCIENCES TOPICS ARE PERFECTLY WIRED AND EXECUTABLE (100%)!")
