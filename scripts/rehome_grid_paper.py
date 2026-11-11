"""Re-home Grid Paper archetypes into Perimeter & Area and Transformation Geometry.
Grounded in: Rule 0d-13 & grade8_remediation_plan.md (GP-8).
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G7_DIR = os.path.join(ROOT, "caps-ai-backend", "app", "utils", "grade7_mathematics")
REG_JSON = os.path.join(ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")
ALIASES_PY = os.path.join(ROOT, "caps-ai-backend", "app", "services", "generator_aliases.py")
REGISTRY_PY = os.path.join(ROOT, "caps-ai-backend", "app", "services", "generator_registry.py")

# 1. Update perimeter_area_2d_generator.py
perim_path = os.path.join(G7_DIR, "perimeter_area_2d_generator.py")
with open(perim_path, "r", encoding="utf-8") as f:
    perim_code = f.read()

if "_gen_grid_perimeter" not in perim_code:
    grid_funcs = '''

def _gen_grid_perimeter(rng: random.Random) -> Dict[str, Any]:
    length_sq = rng.randint(4, 9)
    width_sq = rng.randint(2, 6)
    perimeter_cm = 2 * (length_sq + width_sq)
    shape_name = "rectangle" if length_sq != width_sq else "square"
    prompt = (
        f"A {shape_name} is drawn on standard $1\\\\text{{ cm}} \\\\times 1\\\\text{{ cm}}$ square grid paper.\\n"
        f"The shape is **{length_sq} grid squares** long and **{width_sq} grid squares** wide.\\n\\n"
        f"1. Given that each grid square side represents exactly $1\\\\text{{ cm}}$, calculate the perimeter ($P$) of this {shape_name}.\\n"
        f"2. State the formula used to find the perimeter."
    )
    sol = (
        f"**Step 1:** State perimeter formula:\\n"
        f"$$P = 2 \\\\times (\\\\text{{length}} + \\\\text{{width}})$$\\n\\n"
        f"**Step 2:** Substitute values:\\n"
        f"$$P = 2 \\\\times ({length_sq}\\\\text{{ cm}} + {width_sq}\\\\text{{ cm}}) = 2 \\\\times {length_sq + width_sq}\\\\text{{ cm}} = \\\\mathbf{{{perimeter_cm}\\\\text{{ cm}}}}$$"
    )
    correct_ans = f"1. {perimeter_cm} cm; 2. P = 2 x (length + width) or sum of all sides."
    return {
        "id": f"g7_math_grid_perim_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "diagram_spec": {
            "diagram_role": "context",
            "kind": "grid_paper",
            "length": length_sq,
            "width": width_sq,
            "unit": "cm",
            "caption": f"Rectangle on 1 cm x 1 cm grid ({length_sq} squares long by {width_sq} squares wide)"
        },
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "grid_perimeter_calculation",
        "learning_objective_id": "math_g7_grid_perimeter",
        "hints": {
            "tier_1": "Perimeter is the total boundary distance around the outside edge.",
            "tier_2": f"Add all 4 sides: {length_sq} + {width_sq} + {length_sq} + {width_sq}.",
            "tier_3": f"Perimeter = {perimeter_cm} cm."
        },
        "misconception_tags": ["confused_perimeter_with_area_on_grid"]
    }


def _gen_grid_area(rng: random.Random) -> Dict[str, Any]:
    length_sq = rng.randint(3, 8)
    width_sq = rng.randint(2, 6)
    area_cm2 = length_sq * width_sq
    prompt = (
        f"A geometric shape drawn on a $1\\\\text{{ cm}} \\\\times 1\\\\text{{ cm}}$ square grid completely encloses a rectangle "
        f"measuring **{length_sq} squares** in length by **{width_sq} squares** in width.\\n\\n"
        f"1. What is the area of a single grid square on this resource sheet?\\n"
        f"2. Calculate the total area ($A$) enclosed by the rectangle in $\\\\text{{cm}}^2$."
    )
    sol = (
        f"**Step 1:** Area of one unit square:\\n"
        f"$$\\\\text{{Area of 1 unit square}} = 1\\\\text{{ cm}} \\\\times 1\\\\text{{ cm}} = 1\\\\text{{ cm}}^2$$\\n\\n"
        f"**Step 2:** Calculate total area:\\n"
        f"$$\\\\text{{Area}} = \\\\text{{length}} \\\\times \\\\text{{width}} = {length_sq}\\\\text{{ cm}} \\\\times {width_sq}\\\\text{{ cm}} = \\\\mathbf{{{area_cm2}\\\\text{{ cm}}^2}}$$\\n"
        f"(Or counting {length_sq} rows of {width_sq} squares = {area_cm2} total squares)."
    )
    correct_ans = f"1. 1 cm^2; 2. {area_cm2} cm^2."
    return {
        "id": f"g7_math_grid_area_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "diagram_spec": {
            "diagram_role": "context",
            "kind": "grid_paper",
            "length": length_sq,
            "width": width_sq,
            "unit": "cm",
            "caption": f"Rectangle on 1 cm x 1 cm grid ({length_sq} squares long by {width_sq} squares wide)"
        },
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "grid_area_calculation",
        "learning_objective_id": "math_g7_grid_area",
        "hints": {
            "tier_1": "Multiply length by width, or count the total number of square centimetre blocks inside.",
            "tier_2": f"Area = {length_sq} x {width_sq}.",
            "tier_3": f"Area = {area_cm2} cm^2."
        },
        "misconception_tags": ["omitted_squared_units_area"]
    }
'''
    perim_code = perim_code.replace('SUBSKILLS = [', grid_funcs + '\n\nSUBSKILLS = [')
    perim_code = perim_code.replace(
        '"area_perimeter_compound_shape"',
        '"area_perimeter_compound_shape",\n    "grid_perimeter_calculation",\n    "grid_area_calculation"'
    )
    perim_code = perim_code.replace(
        'if "triang" in sub_name and "area" in sub_name:',
        'if "grid" in sub_name and "perim" in sub_name:\n            return _gen_grid_perimeter(rng)\n        elif "grid" in sub_name and "area" in sub_name:\n            return _gen_grid_area(rng)\n        elif "triang" in sub_name and "area" in sub_name:'
    )
    with open(perim_path, "w", encoding="utf-8") as f:
        f.write(perim_code)
    print("Updated perimeter_area_2d_generator.py")

# 2. Update transformation_geometry_generator.py
trans_path = os.path.join(G7_DIR, "transformation_geometry_generator.py")
with open(trans_path, "r", encoding="utf-8") as f:
    trans_code = f.read()

if "_gen_grid_translation" not in trans_code:
    grid_trans_funcs = '''

def _gen_grid_translation(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([3, 4, 5, 6])
    dy = rng.choice([2, 3, 4])
    dir_x = rng.choice(["right", "left"])
    dir_y = rng.choice(["up", "down"])
    orig_x = rng.randint(2, 6)
    orig_y = rng.randint(2, 6)
    new_x = orig_x + dx if dir_x == "right" else orig_x - dx
    new_y = orig_y + dy if dir_y == "up" else orig_y - dy
    prompt = (
        f"Triangle $ABC$ is plotted on square grid paper with vertex $A$ located at grid coordinates $({orig_x}; {orig_y})$.\\n"
        f"The triangle is translated by sliding it **{dx} units {dir_x}** and **{dy} units {dir_y}**.\\n\\n"
        f"1. What are the new grid coordinates of image vertex $A'$?\\n"
        f"2. Does the size or shape of triangle $ABC$ change under this translation? Explain."
    )
    sol = (
        f"**Step 1:** Apply translation:\\n"
        f"- $x$-coordinate: ${orig_x} {'+' if dir_x == 'right' else '-'} {dx} = {new_x}$\\n"
        f"- $y$-coordinate: ${orig_y} {'+' if dir_y == 'up' else '-'} {dy} = {new_y}$\\n\\n"
        f"$$\\\\therefore A'({new_x}; {new_y})$$\\n\\n"
        f"**Step 2:** Congruence:\\n"
        f"No, translation is an isometry (rigid transformation). The size and shape remain unchanged (congruent)."
    )
    correct_ans = f"1. ({new_x}; {new_y}); 2. No, translation preserves size and shape (the figures are congruent)."
    return {
        "id": f"g7_math_grid_trans_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "grid_shape_translation",
        "learning_objective_id": "math_g7_grid_translation",
        "hints": {
            "tier_1": "Right adds to x, Left subtracts from x. Up adds to y, Down subtracts from y.",
            "tier_2": f"Calculate: x = {orig_x} {dir_x} {dx}, y = {orig_y} {dir_y} {dy}.",
            "tier_3": f"Coordinates are ({new_x}; {new_y}). Size and shape do not change."
        },
        "misconception_tags": ["translation_sign_inversion"]
    }


def _gen_grid_reflection(rng: random.Random) -> Dict[str, Any]:
    line_type = rng.choice(["vertical grid line (x = 5)", "horizontal grid line (y = 4)"])
    prompt = (
        f"On a square grid sheet, a polygon is reflected across a {line_type} that acts as a mirror line of symmetry.\\n\\n"
        f"1. What is the relationship between the distance from each original vertex to the mirror line, "
        f"and the distance from the reflected vertex to the mirror line?\\n"
        f"2. What line segment connects any original vertex to its reflected image relative to the mirror line?"
    )
    sol = (
        f"**Step 1:** Distance relationship:\\n"
        f"Each original vertex and its reflected image are **equidistant** (at the exact same perpendicular distance) from the mirror line.\\n\\n"
        f"**Step 2:** Angle of connection:\\n"
        f"The line segment connecting an original vertex to its image is **perpendicular** ($90^\\\\circ$) to the line of symmetry, "
        f"and is bisected by the mirror line."
    )
    correct_ans = "1. Equal distance (equidistant) from the mirror line; 2. Perpendicular to the line of symmetry."
    return {
        "id": f"g7_math_grid_refl_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "grid_shape_reflection",
        "learning_objective_id": "math_g7_grid_reflection",
        "hints": {
            "tier_1": "When you look into a mirror, how far behind the mirror does your reflection appear?",
            "tier_2": "The distance from the object to the mirror equals the distance from the image to the mirror.",
            "tier_3": "1. Equidistant (equal distance). 2. Perpendicular (at right angles)."
        },
        "misconception_tags": ["reflection_perpendicular_distance_misconception"]
    }


def _gen_grid_scale_factor(rng: random.Random) -> Dict[str, Any]:
    orig_w = rng.randint(2, 4)
    orig_h = rng.randint(2, 4)
    k = rng.choice([2, 3])
    new_w = orig_w * k
    new_h = orig_h * k
    orig_area = orig_w * orig_h
    new_area = new_w * new_h
    prompt = (
        f"A rectangle measuring **{orig_w}\\\\text{{ cm}} \\\\times {orig_h}\\\\text{{ cm}}** is drawn on square grid paper.\\n"
        f"It is enlarged by a **scale factor of {k}**.\\n\\n"
        f"1. Calculate the new dimensions (length and width) of the enlarged rectangle.\\n"
        f"2. Calculate the area of the original rectangle and the area of the enlarged rectangle.\\n"
        f"3. By what factor did the area increase? (Hint: compare the ratio of areas to the scale factor)."
    )
    sol = (
        f"**Step 1:** Calculate new linear dimensions:\\n"
        f"- Length: ${orig_w} \\\\times {k} = \\\\mathbf{{{new_w}\\\\text{{ cm}}}}$\\n"
        f"- Width: ${orig_h} \\\\times {k} = \\\\mathbf{{{new_h}\\\\text{{ cm}}}}$\\n\\n"
        f"**Step 2:** Calculate areas:\\n"
        f"- Original Area: ${orig_w} \\\\times {orig_h} = \\\\mathbf{{{orig_area}\\\\text{{ cm}}^2}}$\\n"
        f"- Enlarged Area: ${new_w} \\\\times {new_h} = \\\\mathbf{{{new_area}\\\\text{{ cm}}^2}}$\\n\\n"
        f"**Step 3:** Area increase factor:\\n"
        f"$$\\\\frac{{\\\\text{{New Area}}}}{{\\\\text{{Original Area}}}} = \\\\frac{{{new_area}}}{{{orig_area}}} = {k**2} = k^2$$\\n"
        f"The area increased by a factor of **${k**2}$** (which is the square of the linear scale factor: ${k}^2$)."
    )
    correct_ans = f"1. {new_w} cm by {new_h} cm; 2. Original: {orig_area} cm^2, Enlarged: {new_area} cm^2; 3. Factor of {k**2} (scale factor squared)."
    return {
        "id": f"g7_math_grid_scale_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "grid_scale_factor_enlargement",
        "learning_objective_id": "math_g7_grid_scale_factor",
        "hints": {
            "tier_1": f"Multiply each side length by the scale factor {k}.",
            "tier_2": f"Linear dimensions multiply by {k}, but area multiplies by {k}^2 = {k**2}.",
            "tier_3": f"1. {new_w} cm x {new_h} cm. 2. {orig_area} cm^2 and {new_area} cm^2. 3. Factor of {k**2}."
        },
        "misconception_tags": ["area_scale_factor_linear_fallacy"]
    }
'''
    trans_code = trans_code.replace('SUBSKILLS = [', grid_trans_funcs + '\n\nSUBSKILLS = [')
    trans_code = trans_code.replace(
        '"parallelogram_symmetry"',
        '"parallelogram_symmetry",\n    "grid_shape_translation",\n    "grid_shape_reflection",\n    "grid_scale_factor_enlargement"'
    )
    trans_code = trans_code.replace(
        'if "translation" in sub_str or "translat" in sub_str:',
        'if "grid" in sub_str and "trans" in sub_str:\n            q = _gen_grid_translation(rng)\n        elif "grid" in sub_str and ("refl" in sub_str or "mirror" in sub_str):\n            q = _gen_grid_reflection(rng)\n        elif "grid" in sub_str and ("scale" in sub_str or "enlarge" in sub_str):\n            q = _gen_grid_scale_factor(rng)\n        elif "translation" in sub_str or "translat" in sub_str:'
    )
    with open(trans_path, "w", encoding="utf-8") as f:
        f.write(trans_code)
    print("Updated transformation_geometry_generator.py")

# 3. Update caps_term_registry_data.json: remove "graph paper types" entry
with open(REG_JSON, "r", encoding="utf-8") as f:
    reg_content = f.read()

import json
reg_data = json.loads(reg_content)
initial_len = len(reg_data)
reg_data = [item for item in reg_data if not (item.get("name") == "graph paper types" or item.get("generator_key") == "grade7_math_graph_paper_types")]
print(f"Registry data entries: {initial_len} -> {len(reg_data)}")

with open(REG_JSON, "w", encoding="utf-8") as f:
    json.dump(reg_data, f, indent=2)
print("Updated caps_term_registry_data.json")

# 4. Update generator_aliases.py
with open(ALIASES_PY, "r", encoding="utf-8") as f:
    aliases_code = f.read()

aliases_code = re.sub(r'^\s*"graph paper types":\s*"[^"]*",?\n', '', aliases_code, flags=re.MULTILINE)
with open(ALIASES_PY, "w", encoding="utf-8") as f:
    f.write(aliases_code)
print("Updated generator_aliases.py")

# 5. Update generator_registry.py: remove graph_paper_types
with open(REGISTRY_PY, "r", encoding="utf-8") as f:
    registry_code = f.read()

registry_code = re.sub(r'^\s*"grade[789]_math_graph_paper_types":\s*[^,\n]+,?\n', '', registry_code, flags=re.MULTILINE)
with open(REGISTRY_PY, "w", encoding="utf-8") as f:
    f.write(registry_code)
print("Updated generator_registry.py")
print("GP-8 Re-homing Complete!")
