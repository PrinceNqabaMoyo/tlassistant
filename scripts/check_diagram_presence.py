import sys
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import generate_variant

topics_to_check = [
    (10, "grade10_mathlit_measurement_of_perimeter_and_area"),
    (10, "grade10_mathlit_assembly_diagrams_floor_plans_packaging"),
    (10, "grade10_mathlit_scale_maps_and_plans"),
    (11, "grade11_mathlit_plans_and_other_representations"),
    (11, "grade11_mathlit_maps"),
    (11, "grade11_mathlit_area_and_volume")
]

for grade, key in topics_to_check:
    print(f"\nChecking {key} (Grade {grade})...")
    res = generate_variant(topic=key, grade=str(grade), subject="Mathematical Literacy", seed=101, count=10)
    questions = res if isinstance(res, list) else res.get("questions", [res])
    diagram_count = 0
    table_count = 0
    text_diagram_count = 0
    for q in questions:
        if q.get("diagram") or q.get("diagram_spec") or q.get("svg_data"):
            diagram_count += 1
        if q.get("table") or q.get("table_data"):
            table_count += 1
        p = q.get("prompt", "")
        if "```" in p or "|" in p or "<svg" in p:
            text_diagram_count += 1
    print(f"  Out of 10 sampled: {diagram_count} have diagram object, {table_count} have table object, {text_diagram_count} have ASCII/table/SVG in prompt")
