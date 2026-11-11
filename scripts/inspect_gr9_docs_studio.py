import os

base = 'caps-ai-backend/curriculum_docs/Mathematics_Gr9'
for f in sorted(os.listdir(base)):
    if f.endswith('.md'):
        path = os.path.join(base, f)
        with open(path, 'r', encoding='utf-8') as fp:
            first_few = [fp.readline().strip() for _ in range(8)]
        print(f"=== {f} ===")
        for line in first_few:
            if line:
                print("  ", line)
