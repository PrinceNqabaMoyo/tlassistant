with open('caps-ai-backend/app/services/generator_registry.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '"grade9_math_' in l:
        print(f'{i+1}: {l.rstrip()}')
