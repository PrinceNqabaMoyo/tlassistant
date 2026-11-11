import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_arch = {
    "id": "tech11_analytical_geometry",
    "name": "Technical Mathematics Straight Line Equation & Gradient Geometry",
    "subject": "Technical Mathematics",
    "grade": 11,
    "term": 2,
    "topic": "Analytical geometry",
    "source": "generated",
    "spec_key": "diagram_spec",
    "renderer": "DiagramModalityRenderer",
    "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
    "generator_file": "caps-ai-backend/app/utils/grade10_mathematics/term_2/analytical_geometry_generator.py",
    "required_fields": ["kind", "points", "vertices"],
    "evidence": [
        "curriculum_docs_auto/TechnicalMathematics_Gr11/Term 2/02. Analytical geometry.md"
    ],
    "need_tier": "Essential",
    "test_id": "diagram-canvas-container",
    "status": "built"
}

existing_ids = {a['id'] for a in data['archetypes']}
if new_arch['id'] not in existing_ids:
    data['archetypes'].append(new_arch)
    print("Added tech11_analytical_geometry!")

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Total registered archetypes: {len(data['archetypes'])}")
