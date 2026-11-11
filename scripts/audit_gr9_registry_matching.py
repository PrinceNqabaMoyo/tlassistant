import os
import json

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    registry = json.load(f)

gr9_math = [x for x in registry if str(x.get('grade')) == '9' and 'math' in x.get('subject', '').lower()]

docs_auto_base = 'caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9'
files_in_auto = []
for root, dirs, files in os.walk(docs_auto_base):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), docs_auto_base)
            files_in_auto.append(rel)

print(f"Total Registry Entries for Grade 9 Math: {len(gr9_math)}")
for i, reg in enumerate(gr9_math):
    term = reg.get('term')
    name = reg.get('name')
    gen_key = reg.get('generator_key')
    # find matching file
    matches = [f for f in files_in_auto if name.lower() in f.lower() or f.lower().endswith(name.lower() + '.md')]
    match_str = matches[0] if matches else 'NO DIRECT MATCH'
    print(f"[{i+1:02d}] T{term} '{name}' -> key: '{gen_key}' | auto_file: {match_str}")
