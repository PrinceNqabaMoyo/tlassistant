import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    reg = json.load(f)

batch3_archetypes = [
    {
        'id': 'ps10_transverse_waves',
        'name': 'Periodic Transverse Wave Anatomy & Sinusoidal Profile',
        'subject': 'Physical Sciences',
        'grade': 10,
        'term': 1,
        'topic': 'Transverse waves',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade10_physical_sciences/waves_sound_light_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/08. Transverse waves.md'],
        'need_tier': 'Essential',
        'test_id': 'transverse-wave-canvas',
        'status': 'built'
    },
    {
        'id': 'ps11_newton_horizontal_friction',
        'name': 'Newtonian Horizontal Surface & Kinetic Friction Free-Body Diagram',
        'subject': 'Physical Sciences',
        'grade': 11,
        'term': 2,
        'topic': "Newton's laws",
        'source': 'generated',
        'spec_key': 'fbd_spec',
        'renderer': 'FbdModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/FbdModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/physical_sciences/mechanics_generator.py',
        'required_fields': ['mass_kg', 'angle_deg', 'forces'],
        'evidence': ["curriculum_docs_auto/PhysicalSciences_Gr11/Term 2/01. Newton's laws.md"],
        'need_tier': 'Essential',
        'test_id': 'fbd-canvas',
        'status': 'built'
    },
    {
        'id': 'ns9_forces_fbd',
        'name': 'Gravitational Weight & Normal Force Equilibrium Free-Body Diagram',
        'subject': 'Natural Sciences',
        'grade': 9,
        'term': 3,
        'topic': 'Forces',
        'source': 'generated',
        'spec_key': 'fbd_spec',
        'renderer': 'FbdModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/FbdModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/natural_sciences/term3_energy_change_forces_generator.py',
        'required_fields': ['mass_kg', 'angle_deg', 'forces'],
        'evidence': ['curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md'],
        'need_tier': 'Essential',
        'test_id': 'fbd-canvas',
        'status': 'built'
    }
]

existing_ids = {a['id'] for a in reg['archetypes']}
for a in batch3_archetypes:
    if a['id'] not in existing_ids:
        reg['archetypes'].append(a)

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(reg, f, indent=2)

print(f"Done! Total archetypes now: {len(reg['archetypes'])}")
