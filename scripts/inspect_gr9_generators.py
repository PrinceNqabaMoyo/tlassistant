import os
import sys

sys.path.insert(0, os.path.abspath('caps-ai-backend'))

files = [
    'caps-ai-backend/app/utils/grade9_whole_numbers_generator.py',
    'caps-ai-backend/app/utils/grade9_integers_generator.py',
    'caps-ai-backend/app/utils/grade9_fractions_generator.py',
    'caps-ai-backend/app/utils/grade9_decimal_notation_generator.py',
    'caps-ai-backend/app/utils/grade9_exponents_generator.py',
    'caps-ai-backend/app/utils/grade9_patterns_generator.py',
    'caps-ai-backend/app/utils/grade9_functions_generator.py',
    'caps-ai-backend/app/utils/grade9_algebraic_expressions_generator.py',
    'caps-ai-backend/app/utils/grade9_algebraic_equations_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/factorisation_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/congruence_similarity_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/pythagoras_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/geometry_straight_lines_triangles_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/measurement_3d_generator.py',
    'caps-ai-backend/app/utils/grade9_mathematics/algebraic_equations_fractions_generator.py'
]

for fp in files:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"=== {os.path.basename(fp)} ({len(lines)} lines) ===")
        # Look for def generate or def generate_
        defs = [l.strip() for l in lines if l.startswith('def ')]
        for d in defs[:5]:
            print(f"   {d}")
