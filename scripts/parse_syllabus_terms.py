with open('caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9/Syllabus.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
terms = re.findall(r'(###\s+.*?(?:GRADE\s+9\s+TERM\s+[1-4]|Term\s+[1-4]).*?)(?=(?:###\s+.*?(?:GRADE\s+9\s+TERM\s+[1-4]|Term\s+[1-4]))|\Z)', text, re.DOTALL | re.IGNORECASE)

print(f"Found {len(terms)} Term blocks in Syllabus.md:")
for i, t in enumerate(terms):
    header = t.split('\n')[0]
    print(f"\n--- BLOCK {i+1}: {header} ---")
    # print tables or bullet points
    lines = [l for l in t.split('\n') if '|' in l or l.startswith('####')]
    for l in lines[:10]:
        print("  ", l)
