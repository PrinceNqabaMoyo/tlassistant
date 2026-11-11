import json

with open('curriculum_diagram_registry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {a['id'] for a in data['archetypes']}
print(f"Existing count: {len(existing_ids)}")

new_archetypes = [
    {
        "id": "ls10_plant_cell_cytology",
        "name": "Plant & Animal Cell Organelle Ultrastructure Labelling",
        "subject": "Life Sciences",
        "grade": 10,
        "term": 1,
        "topic": "Cells the basic units of life",
        "source": "banked",
        "spec_key": "diagram_spec",
        "renderer": "BioDiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/BioDiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade10_life_sciences/cytology_mitosis_generator.py",
        "required_fields": ["image_type", "labels"],
        "evidence": [
            "curriculum_docs_auto/LifeSciences_Gr10/Term 1/01. Cells the basic units of life.md"
        ],
        "need_tier": "Essential",
        "test_id": "bio-diagram-canvas",
        "status": "built"
    },
    {
        "id": "math7_geometry_2d_triangles",
        "name": "Triangle & Quadrilateral Interior Angles Construction",
        "subject": "Mathematics",
        "grade": 7,
        "term": 1,
        "topic": "Geometry of 2D shapes",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade7_mathematics/geometry_2d_generator.py",
        "required_fields": ["kind", "points", "vertices"],
        "evidence": [
            "curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of 2D shapes.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "math7_geometric_nets_3d",
        "name": "Polyhedron Unfolded 2D Surface Geometric Net & Euler Analysis",
        "subject": "Mathematics",
        "grade": 7,
        "term": 3,
        "topic": "Geometry of 3D objects",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade7_mathematics/geometric_nets_3d_generator.py",
        "required_fields": ["kind"],
        "evidence": [
            "curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Geometry of 3D objects.md",
            "curriculum_docs_auto/Mathematics_Gr7/Term 3/01. Surface area and volume of 3D objects.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "math8_geometry_2d_triangles_quads",
        "name": "Triangles & Quadrilaterals Angles & Exterior Theorem Geometric Construction",
        "subject": "Mathematics",
        "grade": 8,
        "term": 2,
        "topic": "Geometry of 2D shapes",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade8_mathematics/geometry_2d_shapes_generator.py",
        "required_fields": ["kind", "points", "vertices"],
        "evidence": [
            "curriculum_docs_auto/Mathematics_Gr8/Term 2/04. Geometry of 2D shapes.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "math9_geometric_nets_3d",
        "name": "Cylinder & Right Prism Unfolded Surface Net & Capacity",
        "subject": "Mathematics",
        "grade": 9,
        "term": 4,
        "topic": "Geometry of 3D objects",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade9_mathematics/measurement_3d_generator.py",
        "required_fields": ["kind"],
        "evidence": [
            "curriculum_docs_auto/Mathematics_Gr9/Term 4/01. Surface area volume and capacity of 3D objects.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "math10_analytical_geometry_line",
        "name": "Cartesian Coordinate Plane Distance, Midpoint & Gradient Construction",
        "subject": "Mathematics",
        "grade": 10,
        "term": 2,
        "topic": "Analytical geometry",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade10_mathematics/term_2/analytical_geometry_generator.py",
        "required_fields": ["kind", "points", "vertices"],
        "evidence": [
            "curriculum_docs_auto/Mathematics_Gr10/Term 2/02. Analytical geometry.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "math11_analytical_geometry_inclination",
        "name": "Line Inclination Angle & Collinear Points Cartesian Geometry",
        "subject": "Mathematics",
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
            "curriculum_docs_auto/Mathematics_Gr11/Term 2/02. Analytical geometry.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "ns9_resistance_circuit",
        "name": "Ohm's Law & Resistor Network Potential Divider Circuit Analysis",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 2,
        "topic": "Resistance",
        "source": "generated",
        "spec_key": "circuit_spec",
        "renderer": "CircuitModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/CircuitModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/natural_sciences/electric_circuits_generator.py",
        "required_fields": ["type", "voltage", "components"],
        "evidence": [
            "curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Resistance.md"
        ],
        "need_tier": "Essential",
        "test_id": "circuit-schematic-canvas",
        "status": "built"
    },
    {
        "id": "ps10_vectors_fbd",
        "name": "1D/2D Kinematic Vectors & Gravitational Normal Equilibrium Free-Body Diagram",
        "subject": "Physical Sciences",
        "grade": 10,
        "term": 3,
        "topic": "Vectors and scalars",
        "source": "generated",
        "spec_key": "fbd_spec",
        "renderer": "FbdModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/FbdModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade10_physical_sciences/motion_energy_generator.py",
        "required_fields": ["mass_kg", "angle_deg", "forces"],
        "evidence": [
            "curriculum_docs_auto/PhysicalSciences_Gr10/Term 3/03. Vectors and scalars.md"
        ],
        "need_tier": "Essential",
        "test_id": "fbd-canvas",
        "status": "built"
    },
    {
        "id": "ps11_intermolecular_forces",
        "name": "Molecular Geometry & Intermolecular Forces Boiling Point Comparison",
        "subject": "Physical Sciences",
        "grade": 11,
        "term": 1,
        "topic": "Intermolecular forces",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "OrganicChemistry3DViewer",
        "renderer_path": "src/components/workspace/modalities/OrganicChemistry3DViewer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade11_physical_sciences/chemical_bonding_intermolecular_generator.py",
        "required_fields": ["formula", "name", "imf"],
        "evidence": [
            "curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/02. Intermolecular forces.md"
        ],
        "need_tier": "Essential",
        "test_id": "organic-chem-canvas",
        "status": "built"
    },
    {
        "id": "ps11_wavefront_diffraction",
        "name": "Huygens' Principle & Single Slit Wavefront Diffraction",
        "subject": "Physical Sciences",
        "grade": 11,
        "term": 2,
        "topic": "2D and 3D wavefronts",
        "source": "generated",
        "spec_key": "optics_spec",
        "renderer": "OpticsRayModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/OpticsRayModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/physical_sciences/geometrical_optics_generator.py",
        "required_fields": ["medium_1", "angle_incidence_deg"],
        "evidence": [
            "curriculum_docs_auto/PhysicalSciences_Gr11/Term 2/03. 2D and 3D wavefronts.md"
        ],
        "need_tier": "Essential",
        "test_id": "optics-ray-canvas",
        "status": "built"
    },
    {
        "id": "ps12_organic_molecules_3d",
        "name": "Homologous Series & Structural Isomers 3D CPK Molecular Geometry",
        "subject": "Physical Sciences",
        "grade": 12,
        "term": 1,
        "topic": "Organic molecules",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "OrganicChemistry3DViewer",
        "renderer_path": "src/components/workspace/modalities/OrganicChemistry3DViewer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade12_physical_sciences/organic_chemistry_generator.py",
        "required_fields": ["formula", "name", "imf"],
        "evidence": [
            "curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/04. Organic molecules.md"
        ],
        "need_tier": "Essential",
        "test_id": "organic-chem-canvas",
        "status": "built"
    },
    {
        "id": "ps12_electrodynamics_generator_motor",
        "name": "AC Generator Alternator & DC Motor Armature Electrodynamics",
        "subject": "Physical Sciences",
        "grade": 12,
        "term": 3,
        "topic": "Electrodynamics",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "ElectrodynamicsMotorViewer",
        "renderer_path": "src/components/workspace/modalities/ElectrodynamicsMotorViewer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade12_physical_sciences/electrodynamics_circuits_generator.py",
        "required_fields": ["mode"],
        "evidence": [
            "curriculum_docs_auto/PhysicalSciences_Gr12/Term 3/01. Electrodynamics.md"
        ],
        "need_tier": "Essential",
        "test_id": "electrodynamics-canvas",
        "status": "built"
    },
    {
        "id": "tech10_analytical_geometry",
        "name": "Technical Mathematics Cartesian Distance, Midpoint & Gradient Construction",
        "subject": "Technical Mathematics",
        "grade": 10,
        "term": 2,
        "topic": "Analytical Geometry",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade10_mathematics/term_2/analytical_geometry_generator.py",
        "required_fields": ["kind", "points", "vertices"],
        "evidence": [
            "curriculum_docs_auto/TechnicalMathematics_Gr10/Term 2/02. Analytical Geometry.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "tech11_circles_angular_movement",
        "name": "Technical Mathematics Circular Arc, Sector & Angular Velocity Construction",
        "subject": "Technical Mathematics",
        "grade": 11,
        "term": 3,
        "topic": "Circles angles and angular movement",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/technical_mathematics/circles_angular_movement_generator.py",
        "required_fields": ["kind", "points", "vertex_labels"],
        "evidence": [
            "curriculum_docs_auto/TechnicalMathematics_Gr11/Term 3/01. Circles angles and angular movement.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "tech11_circle_geometry_tangent",
        "name": "Technical Mathematics Circle Geometry Tangent & Chord Theorem Construction",
        "subject": "Technical Mathematics",
        "grade": 11,
        "term": 3,
        "topic": "Euclidean geometry",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade11_mathematics/circle_geometry_theorems_generator.py",
        "required_fields": ["kind", "points", "vertex_labels"],
        "evidence": [
            "curriculum_docs_auto/TechnicalMathematics_Gr11/Term 3/03. Euclidean geometry.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "tech12_analytical_circles",
        "name": "Technical Mathematics Cartesian Circle Tangents & Perpendicular Radii",
        "subject": "Technical Mathematics",
        "grade": 12,
        "term": 2,
        "topic": "Analytical geometry",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade12_mathematics/analytical_geometry_circles_generator.py",
        "required_fields": ["kind", "points", "vertex_labels"],
        "evidence": [
            "curriculum_docs_auto/TechnicalMathematics_Gr12/Term 2/02. Analytical geometry.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    },
    {
        "id": "tech12_euclidean_proportionality",
        "name": "Technical Mathematics Triangles Proportionality & Similarity Proof Construction",
        "subject": "Technical Mathematics",
        "grade": 12,
        "term": 2,
        "topic": "Euclidean Geometry Proportionality and similarity",
        "source": "generated",
        "spec_key": "diagram_spec",
        "renderer": "DiagramModalityRenderer",
        "renderer_path": "src/components/workspace/modalities/DiagramModalityRenderer.jsx",
        "generator_file": "caps-ai-backend/app/utils/grade12_mathematics/analytical_geometry_circles_generator.py",
        "required_fields": ["kind", "points", "vertex_labels"],
        "evidence": [
            "curriculum_docs_auto/TechnicalMathematics_Gr12/Term 2/03. Euclidean Geometry Proportionality and similarity.md"
        ],
        "need_tier": "Essential",
        "test_id": "diagram-canvas-container",
        "status": "built"
    }
]

added = 0
for a in new_archetypes:
    if a['id'] not in existing_ids:
        data['archetypes'].append(a)
        existing_ids.add(a['id'])
        added += 1

print(f"Added {added} new archetypes. Total now: {len(data['archetypes'])}")

with open('curriculum_diagram_registry.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Saved curriculum_diagram_registry.json successfully!")
