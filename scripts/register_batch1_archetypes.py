import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    reg = json.load(f)

new_archetypes = [
    {
        'id': 'ls12_human_ear_anatomy',
        'name': 'Human Ear Longitudinal Section Anatomy & Hearing Transduction Schematic',
        'subject': 'Life Sciences',
        'grade': 12,
        'term': 2,
        'topic': 'Human responses to the environment',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/life_sciences/human_organ_systems_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr12/Term 2/01. Human responses to the environment.md'],
        'need_tier': 'Essential',
        'test_id': 'human-ear-canvas',
        'status': 'built'
    },
    {
        'id': 'ls11_alveolus_gas_exchange',
        'name': 'Pulmonary Alveolus & Capillary Microscopic Gas Exchange Schematic',
        'subject': 'Life Sciences',
        'grade': 11,
        'term': 3,
        'topic': 'Gaseous exchange',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/life_sciences/human_organ_systems_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr11/Term 3/01. Gaseous exchange.md'],
        'need_tier': 'Essential',
        'test_id': 'alveolus-gas-exchange-canvas',
        'status': 'built'
    },
    {
        'id': 'ls11_intestinal_villus_anatomy',
        'name': 'Intestinal Villus Longitudinal Section & Nutrient Absorption Schematic',
        'subject': 'Life Sciences',
        'grade': 11,
        'term': 2,
        'topic': 'Animal Nutrition',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/life_sciences/human_organ_systems_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr11/Term 2/02. Animal Nutrition.md'],
        'need_tier': 'Essential',
        'test_id': 'intestinal-villus-canvas',
        'status': 'built'
    },
    {
        'id': 'ls10_mitosis_stages',
        'name': 'Mitosis Four-Stage Somatic Division & Cytokinesis Schematic',
        'subject': 'Life Sciences',
        'grade': 10,
        'term': 1,
        'topic': 'Cell division',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/grade10_life_sciences/cytology_mitosis_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr10/Term 1/02. Cell division.md'],
        'need_tier': 'Essential',
        'test_id': 'mitosis-stages-canvas',
        'status': 'built'
    },
    {
        'id': 'ls12_meiosis_crossing_over',
        'name': 'Meiosis Prophase I Synapsis & Chiasma Crossing Over Schematic',
        'subject': 'Life Sciences',
        'grade': 12,
        'term': 1,
        'topic': 'Meiosis',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/life_sciences/meiosis_human_reproduction_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr12/Term 1/03. Meiosis.md'],
        'need_tier': 'Essential',
        'test_id': 'meiosis-crossing-over-canvas',
        'status': 'built'
    },
    {
        'id': 'ls12_endocrine_system_map',
        'name': 'Human Endocrine System Glandular Map & Chemical Coordination Schematic',
        'subject': 'Life Sciences',
        'grade': 12,
        'term': 2,
        'topic': 'The human endocrine system and homeostasis',
        'source': 'banked',
        'spec_key': 'diagram_spec',
        'renderer': 'BioDiagramModalityRenderer',
        'renderer_path': 'src/components/workspace/modalities/BioDiagramModalityRenderer.jsx',
        'generator_file': 'caps-ai-backend/app/utils/life_sciences/human_organ_systems_generator.py',
        'required_fields': ['image_type', 'labels'],
        'evidence': ['curriculum_docs_auto/LifeSciences_Gr12/Term 2/04. The human endocrine system and homeostasis.md'],
        'need_tier': 'Essential',
        'test_id': 'endocrine-system-canvas',
        'status': 'built'
    }
]

existing_ids = {a['id'] for a in reg['archetypes']}
for a in new_archetypes:
    if a['id'] not in existing_ids:
        reg['archetypes'].append(a)

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(reg, f, indent=2)

print(f"Done! Total archetypes now: {len(reg['archetypes'])}")
