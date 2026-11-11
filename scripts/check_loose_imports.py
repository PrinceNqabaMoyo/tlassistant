import os

loose_modules = [
    'grade9_whole_numbers_generator',
    'grade9_integers_generator',
    'grade9_fractions_generator',
    'grade9_decimal_notation_generator',
    'grade9_exponents_generator',
    'grade9_patterns_generator',
    'grade9_functions_generator',
    'grade9_algebraic_expressions_generator',
    'grade9_algebraic_equations_generator'
]

print("Searching app/ for imports...")
for root, dirs, files in os.walk('caps-ai-backend/app'):
    if any(ignore in root for ignore in ['venv', '__pycache__', '.pytest_cache']):
        continue
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                try:
                    content = fp.read()
                    for m in loose_modules:
                        if m in content:
                            print(f"  {path}: references {m}")
                except:
                    pass
