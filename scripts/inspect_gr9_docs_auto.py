import os

base = 'caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9'
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if f.endswith('.md') and f != 'Syllabus.md':
            path = os.path.join(root, f)
            rel = os.path.relpath(path, base)
            with open(path, 'r', encoding='utf-8') as fp:
                lines = [fp.readline() for _ in range(15)]
            heading = [l.strip() for l in lines if l.startswith('#') or l.startswith('###') or l.startswith('**')]
            print(f"{rel}:")
            for h in heading[:3]:
                print(f"   {h}")
