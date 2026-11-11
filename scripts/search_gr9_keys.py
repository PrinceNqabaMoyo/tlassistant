import os

keys = [
    'grade9_math_data_handling',
    'grade9_math_algebraic_equations_fractions',
    'grade9_math_whole_numbers',
    'grade9_math_integers',
    'grade9_math_exponents',
    'grade9_math_patterns',
    'grade9_math_functions',
    'grade9_math_algebraic_expressions',
    'grade9_math_graphs',
    'grade9_math_geometry_of_straight_lines',
    'grade9_math_geometry',
    'grade9_math_construction_of_geometric_figures',
    'grade9_math_transformation_geometry',
    'grade9_math_theorem_of_pythagoras',
    'grade9_math_area_and_perimeter_of_2d_shapes',
    'grade9_math_geometry_of_3d_objects',
    'grade9_math_surface_area_and_volume_of_3d_objects',
    'grade9_math_probability'
]

print("Searching for generator keys in caps-ai-backend...")
for root, dirs, files in os.walk('caps-ai-backend/app'):
    for f in files:
        if f.endswith('.py') or f.endswith('.json'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                    matches = [k for k in keys if k in content]
                    if matches and not path.endswith('caps_term_registry_data.json'):
                        print(f"{path}: matches {len(matches)} keys: {matches[:3]}...")
            except Exception as e:
                pass
