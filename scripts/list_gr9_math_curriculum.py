import os
import json

base_dir = 'caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9'
terms = ['Term 1', 'Term 2', 'Term 3', 'Term 4']

curriculum_topics = {}

for term in terms:
    t_path = os.path.join(base_dir, term)
    curriculum_topics[term] = []
    if os.path.exists(t_path):
        for f in sorted(os.listdir(t_path)):
            if f.endswith('.md'):
                curriculum_topics[term].append(f)

print(json.dumps(curriculum_topics, indent=2))
