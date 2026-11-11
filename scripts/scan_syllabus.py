import re

with open('caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9/Syllabus.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract lines that define topics in tables or headers
matches = re.findall(r'\|(?:\s*\*\*.*?\*\*|\s*[^|]+)\|\s*([0-9\.]+\s+[^|]+)\|', text)
topics = []
for m in matches:
    t = m.strip()
    if t not in topics and not t.startswith('Topic') and not t.startswith('---'):
        topics.append(t)

print("Unique topics found in tables:")
for t in topics:
    print(" -", t)
