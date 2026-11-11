import sys
import json
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import get_topic_archetypes

data = json.load(open('caps-ai-backend/app/services/caps_term_registry_data.json', encoding='utf-8'))
gr9 = [x for x in data if x.get('grade') == '9' and 'natural' in x.get('subject', '').lower()]

print(f"Testing topic archetypes for {len(gr9)} Grade 9 topics...")
for item in gr9:
    top = item.get('name')
    term = item.get('term')
    gen_key = item.get('generator_key')
    res = get_topic_archetypes(topic=top, grade='9', subject='Natural Sciences')
    archs = res.get('archetypes', [])
    resolved_key = res.get('generator_key')
    print(f"Term {term} | {resolved_key} (expected {gen_key}) | archetypes: {len(archs)} | {top}")
    assert len(archs) >= 4, f"Fewer than 4 archetypes for {top}: {archs}"

print("\nALL 24 TOPICS SUCCESSFULLY DISCOVER ARTYCHETYPES (>=4 SUBSKILLS EACH)!")
