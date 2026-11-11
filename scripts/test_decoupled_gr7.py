import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant, get_topic_archetypes

topics = [
    'Functions and relationships 1',
    'Functions and relationships 2',
    'Functions and relationships 3',
    'Collect organise and summarise data',
    'Represent data',
    'Interpret analyse and report on data',
    'Probability'
]

for t in topics:
    info = get_topic_archetypes(t, '7', 'Mathematics')
    archs = info.get('archetypes', [])
    q = generate_variant(topic=t, subskill=archs[0], grade='7', subject='Mathematics', seed=101)[0]
    prompt = q.get("question") or q.get("prompt") or ""
    print(f"{t:<35} | {info['generator_key']:<35} | {archs[0]} -> {prompt[:50]}")
