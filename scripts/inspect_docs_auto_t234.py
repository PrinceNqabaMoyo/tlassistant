import os

base = 'caps-ai-backend/curriculum_docs_auto/Mathematics_Gr9'

for term in ['Term 2', 'Term 3', 'Term 4']:
    t_path = os.path.join(base, term)
    print(f'=== {term} ===')
    for f in sorted(os.listdir(t_path)):
        if f.endswith('.md'):
            fp = os.path.join(t_path, f)
            sz = os.path.getsize(fp)
            with open(fp, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            exercises = [l.strip() for l in lines if 'exercise' in l.lower() or 'activity' in l.lower() or l.startswith('## ') or l.startswith('### ')]
            print(f'  {f} ({sz} bytes, {len(lines)} lines):')
            for ex in exercises[:4]:
                clean_ex = ex.encode('ascii', 'replace').decode('ascii')
                print(f'     - {clean_ex}')
