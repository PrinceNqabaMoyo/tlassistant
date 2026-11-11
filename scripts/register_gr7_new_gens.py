import json

# 1. Update caps-ai-backend/app/services/generator_registry.py
p_reg = 'caps-ai-backend/app/services/generator_registry.py'
with open(p_reg, 'r', encoding='utf-8') as f:
    c = f.read()

import_target = '''    transformation_geometry_generator as g7_math_trans,
)'''

import_replacement = '''    transformation_geometry_generator as g7_math_trans,
    geometry_straight_lines_generator as g7_math_lines,
    grid_paper_types_generator as g7_math_grid,
)'''

assert import_target in c, "import_target not found in generator_registry.py"
c = c.replace(import_target, import_replacement, 1)

# Add to ALL_GENERATORS dictionary
entries_target = '''    "grade7_math_transformation_geometry": g7_math_trans.generate,'''
entries_replacement = '''    "grade7_math_transformation_geometry": g7_math_trans.generate,
    "grade7_math_geometry_of_straight_lines": g7_math_lines.generate,
    "grade7_math_graph_paper_types": g7_math_grid.generate,'''

assert entries_target in c, "entries_target not found in generator_registry.py"
c = c.replace(entries_target, entries_replacement, 1)

with open(p_reg, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated generator_registry.py with Grade 7 straight lines and grid paper generators")

# 2. Update caps_term_registry_data.json
p_json = 'caps-ai-backend/app/services/caps_term_registry_data.json'
with open(p_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = 0
for t in data:
    if str(t.get('grade')) == '7' and t.get('subject') == 'Mathematics':
        name = t.get('name')
        if name == 'Geometry of straight lines':
            t['generator_key'] = 'grade7_math_geometry_of_straight_lines'
            updated += 1
        elif name == 'graph paper types':
            t['generator_key'] = 'grade7_math_graph_paper_types'
            updated += 1

with open(p_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {updated} topics in caps_term_registry_data.json")
