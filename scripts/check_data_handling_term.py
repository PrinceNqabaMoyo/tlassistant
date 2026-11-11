with open('caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9/Syllabus.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'collect' in l.lower() or 'probability' in l.lower():
        if any(h in l for h in ['#', '|', '**']):
            print(f'L{i+1}: {l.strip()[:100]}')
