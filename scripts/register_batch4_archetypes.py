import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    reg = json.load(f)

batch4_archetypes = [
    {
        'id': 'math9_congruence_similarity',
        'name': 'Triangles Congruence & Similarity 2D Geometry Proof',
        'subject': 'Mathematics',
        'grade': 9,
        'term': 2,
        'topic': 'Geometry of 2D shapes',
        'source': 'generated',
        'spec_key': 'diagram_spec',
        'renderer': 'DiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/DiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade9_mathematics/congruence_similarity_generator.py',
        'required_fields': ['kind', 'points', 'vertices'],
        'evidence': ['curriculum_docs_auto/Mathematics_Gr9/Term 2/04. Geometry of 2D shapes.md'],
        'need_tier': 'Essential',
        'test_id': 'diagram-canvas-container',
        'status': 'built'
    },
    {
        'id': 'math10_euclidean_quadrilaterals',
        'name': 'Special Quadrilaterals & Parallelograms Euclidean Geometry Construction',
        'subject': 'Mathematics',
        'grade': 10,
        'term': 3,
        'topic': 'Euclidean geometry 1',
        'source': 'generated',
        'spec_key': 'diagram_spec',
        'renderer': 'DiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/DiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade10_mathematics/term_2/euclidean_geometry_generator.py',
        'required_fields': ['kind', 'points', 'vertices'],
        'evidence': ['curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 1.md'],
        'need_tier': 'Essential',
        'test_id': 'diagram-canvas-container',
        'status': 'built'
    },
    {
        'id': 'math10_midpoint_theorem',
        'name': 'Triangle Midpoint Theorem Euclidean Geometry Construction',
        'subject': 'Mathematics',
        'grade': 10,
        'term': 3,
        'topic': 'Euclidean geometry 2',
        'source': 'generated',
        'spec_key': 'diagram_spec',
        'renderer': 'DiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/DiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade10_mathematics/term_2/euclidean_geometry_generator.py',
        'required_fields': ['kind', 'points', 'vertices'],
        'evidence': ['curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 2.md'],
        'need_tier': 'Essential',
        'test_id': 'diagram-canvas-container',
        'status': 'built'
    },
    {
        'id': 'math12_circle_tangent_geometry',
        'name': 'Cartesian Circle and Perpendicular Tangent Line Geometry',
        'subject': 'Mathematics',
        'grade': 12,
        'term': 2,
        'topic': 'Analytical geometry',
        'source': 'generated',
        'spec_key': 'diagram_spec',
        'renderer': 'DiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/DiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade12_mathematics/analytical_geometry_circles_generator.py',
        'required_fields': ['kind', 'points', 'vertex_labels'],
        'evidence': ['curriculum_docs_auto/Mathematics_Gr12/Term 2/02. Analytical geometry.md'],
        'need_tier': 'Essential',
        'test_id': 'diagram-canvas-container',
        'status': 'built'
    }
]

existing_ids = {a['id'] for a in reg['archetypes']}
for a in batch4_archetypes:
    if a['id'] not in existing_ids:
        reg['archetypes'].append(a)

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(reg, f, indent=2)

print(f"Done! Total archetypes now: {len(reg['archetypes'])}")
