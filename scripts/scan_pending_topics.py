import os

files_to_check = [
    ("Gr10 Life Sciences Cells", "caps-ai-backend/app/utils/grade10_life_sciences/cytology_mitosis_generator.py"),
    ("Gr7 Math 2D", "caps-ai-backend/app/utils/grade7_mathematics/geometry_2d_generator.py"),
    ("Gr7 Math 3D Nets", "caps-ai-backend/app/utils/grade7_mathematics/geometric_nets_3d_generator.py"),
    ("Gr8 Math 2D", "caps-ai-backend/app/utils/grade8_mathematics/geometry_2d_shapes_generator.py"),
    ("Gr8 Math 3D", "caps-ai-backend/app/utils/grade8_mathematics/geometry_3d_objects_generator.py"),
    ("Gr8 Math 3D Meas", "caps-ai-backend/app/utils/grade8_mathematics/measurement_3d_generator.py"),
    ("Gr9 Math 3D Meas", "caps-ai-backend/app/utils/grade9_mathematics/measurement_3d_generator.py"),
    ("Gr10 Math Analytical", "caps-ai-backend/app/utils/grade10_mathematics/term_2/analytical_geometry_generator.py"),
    ("Gr11 Math Analytical", "caps-ai-backend/app/utils/grade11_mathematics/functions_graphs_generator.py"),
    ("Gr9 NS Resistance", "caps-ai-backend/app/utils/natural_sciences/electric_circuits_generator.py"),
    ("Gr10 PS Vectors", "caps-ai-backend/app/utils/grade10_physical_sciences/motion_energy_generator.py"),
    ("Gr11 PS Intermolecular", "caps-ai-backend/app/utils/grade11_physical_sciences/chemical_bonding_intermolecular_generator.py"),
    ("Gr11 PS Wavefronts", "caps-ai-backend/app/utils/physical_sciences/waves_sound_light_generator.py"),
    ("Gr12 PS Organic Chem", "caps-ai-backend/app/utils/grade12_physical_sciences/organic_chemistry_generator.py"),
    ("Gr12 PS Electrodynamics", "caps-ai-backend/app/utils/grade12_physical_sciences/electrodynamics_circuits_generator.py"),
    ("Gr10 Tech Math Analytical", "caps-ai-backend/app/utils/technical_mathematics/circles_angular_movement_generator.py"),
    ("Gr11 Tech Math Circles", "caps-ai-backend/app/utils/technical_mathematics/circles_angular_movement_generator.py"),
    ("Gr11 Tech Math Euclidean", "caps-ai-backend/app/utils/grade11_mathematics/circle_geometry_theorems_generator.py"),
    ("Gr12 Tech Math Analytical", "caps-ai-backend/app/utils/technical_mathematics/circles_angular_movement_generator.py"),
    ("Gr12 Tech Math Euclidean", "caps-ai-backend/app/utils/grade12_mathematics/analytical_geometry_circles_generator.py"),
]

for label, path in files_to_check:
    exists = os.path.exists(path)
    if exists:
        content = open(path, encoding='utf-8').read()
        has_diagram_spec = "diagram_spec" in content
        has_modality = "modality" in content
        print(f"[{label}] {path} -> Exists: True, has diagram_spec: {has_diagram_spec}, has modality: {has_modality}")
    else:
        print(f"[{label}] {path} -> MISSING FILE!")
