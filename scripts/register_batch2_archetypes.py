import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    reg = json.load(f)

batch2_archetypes = [
    {
        'id': 'ns8_circuit_schematic',
        'name': 'Series and Parallel Direct Current Circuits Schematic',
        'subject': 'Natural Sciences',
        'grade': 8,
        'term': 3,
        'topic': 'Series and parallel circuits',
        'source': 'generated',
        'spec_key': 'circuit_spec',
        'renderer': 'CircuitModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/CircuitModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/natural_sciences/electric_circuits_generator.py',
        'required_fields': ['type', 'voltage', 'components'],
        'evidence': ['curriculum_docs_auto/NaturalSciences_Gr8/Term 3/03. Series and parallel circuits.md'],
        'need_tier': 'Essential',
        'test_id': 'circuit-schematic-canvas',
        'status': 'built'
    },
    {
        'id': 'ns9_circuit_schematic',
        'name': 'Direct Current Circuit Analysis with Resistor Combinations',
        'subject': 'Natural Sciences',
        'grade': 9,
        'term': 3,
        'topic': 'Series and parallel circuits',
        'source': 'generated',
        'spec_key': 'circuit_spec',
        'renderer': 'CircuitModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/CircuitModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/natural_sciences/electric_circuits_generator.py',
        'required_fields': ['type', 'voltage', 'components'],
        'evidence': ['curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Series and parallel circuits.md'],
        'need_tier': 'Essential',
        'test_id': 'circuit-schematic-canvas',
        'status': 'built'
    },
    {
        'id': 'ps11_circuit_energy_network',
        'name': 'Series-Parallel Resistor Combination and Potential Divider Schematic',
        'subject': 'Physical Sciences',
        'grade': 11,
        'term': 3,
        'topic': 'Electric circuits',
        'source': 'generated',
        'spec_key': 'circuit_spec',
        'renderer': 'CircuitModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/CircuitModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade11_physical_sciences/electric_circuits_energy_generator.py',
        'required_fields': ['type', 'voltage', 'components'],
        'evidence': ['curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/01. Electric circuits.md'],
        'need_tier': 'Essential',
        'test_id': 'circuit-schematic-canvas',
        'status': 'built'
    },
    {
        'id': 'ps12_internal_resistance_circuit',
        'name': 'Battery Internal Resistance & Lost Volts Circuit Schematic',
        'subject': 'Physical Sciences',
        'grade': 12,
        'term': 3,
        'topic': 'Electric circuits',
        'source': 'generated',
        'spec_key': 'circuit_spec',
        'renderer': 'CircuitModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/CircuitModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade12_physical_sciences/electrodynamics_circuits_generator.py',
        'required_fields': ['type', 'voltage', 'components'],
        'evidence': ['curriculum_docs_auto/PhysicalSciences_Gr12/Term 3/02. Electric circuits.md'],
        'need_tier': 'Essential',
        'test_id': 'circuit-schematic-canvas',
        'status': 'built'
    }
]

existing_ids = {a['id'] for a in reg['archetypes']}
for a in batch2_archetypes:
    if a['id'] not in existing_ids:
        reg['archetypes'].append(a)

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(reg, f, indent=2)

print(f"Done! Total archetypes now: {len(reg['archetypes'])}")
