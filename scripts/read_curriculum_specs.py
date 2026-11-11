from pathlib import Path

docs = [
    'Term 2/04. Algebraic expressions 1.md',
    'Term 2/04. Algebraic expressions 2.md',
    'Term 2/05. Algebraic equations 1.md',
    'Term 2/05. Algebraic equations 2.md',
    'Term 1/04. Graphs.md',
    'Term 2/03. Relationships between variables.md',
    'Term 1/03. Numeric and geometric patterns.md',
    'Term 2/05. Numeric patterns.md',
]

for doc in docs:
    p = Path('curriculum_docs_auto/Mathematics_Gr7') / doc
    print(f'=== {doc} ===')
    if p.exists():
        lines = p.read_text(encoding='utf-8').splitlines()
        headings = [l for l in lines if l.startswith('#')]
        print('Headings:', headings[:8])
        print('Sample lines:\n', '\n'.join(lines[10:25]))
    else:
        print('NOT FOUND!')
