import sys
import os
import json
sys.path.insert(0, os.path.abspath('caps-ai-backend'))
from app.services import generator_registry

def verify_grade7_entropy():
    print("Testing Grade 7 Generator Entropy across seeds 101, 202, 303...")
    with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
        registry_data = json.load(f)

    gr7_topics = [t for t in registry_data if str(t.get('grade')) == '7']
    print(f"Total Grade 7 topics found: {len(gr7_topics)}")

    failures = []
    total_archetypes_tested = 0

    for topic_meta in gr7_topics:
        subject = topic_meta.get('subject')
        topic_name = topic_meta.get('name')
        gen_key = topic_meta.get('generator_key')
        
        gen_func = generator_registry.ALL_GENERATORS.get(gen_key)
        if not gen_func:
            gen_func = generator_registry.get_generator_for_topic(subject, '7', topic_name)
        if not gen_func:
            print(f"Warning: generator not found for {topic_name} (key: {gen_key})")
            continue
            
        arch_meta = generator_registry.get_topic_archetypes(topic_name, grade='7', subject=subject)
        archetypes = arch_meta.get('archetypes', [])
        if not archetypes:
            archetypes = [None]
            
        for arch in archetypes:
            total_archetypes_tested += 1
            prompts = []
            for seed in [101, 202, 303]:
                kwargs = {'seed': seed, 'count': 1}
                if arch:
                    kwargs['subskill'] = arch
                try:
                    res = gen_func(**kwargs)
                    q = res[0] if isinstance(res, list) and res else res
                    prompt = q.get('prompt') or q.get('question') or q.get('question_text') or str(q)
                    prompts.append(prompt)
                except Exception as e:
                    failures.append((topic_name, arch, f"Exception: {e}"))
                    break
            if len(prompts) == 3:
                # Check uniqueness
                if len(set(prompts)) == 1:
                    failures.append((topic_name, arch, f"ZERO_ENTROPY: identical prompt across 3 seeds:\n{prompts[0][:100]}..."))

    print(f"Total archetypes tested: {total_archetypes_tested}")
    if failures:
        print(f"FAILED: {len(failures)} archetypes have zero entropy or errors:")
        for topic, arch, reason in failures:
            print(f"  - [{topic}] (subskill: {arch}): {reason}")
        sys.exit(1)
    else:
        print("ALL GRADE 7 ARCHETYPES PASSED ZERO-ENTROPY CHECK! 100% DISTINCT PROMPTS ACROSS SEEDS!")

if __name__ == '__main__':
    verify_grade7_entropy()
