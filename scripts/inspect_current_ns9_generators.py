import sys
import os

sys.path.insert(0, os.path.abspath("caps-ai-backend"))

from app.utils.natural_sciences import (
    ns9_cells_units_of_life_generator,
    ns9_circulatory_respiratory_generator,
    ns9_digestive_system_generator,
    ns9_forces_electric_cells_generator,
    ns9_human_reproduction_generator,
    term1_life_and_living_generator,
    term2_matter_materials_generator,
    term3_energy_change_forces_generator,
    term4_planet_earth_beyond_generator,
    chemical_reactions_generator,
    electric_circuits_generator,
)

gens = [
    ("ns9_cells", ns9_cells_units_of_life_generator.generate),
    ("ns9_circ_resp", ns9_circulatory_respiratory_generator.generate),
    ("ns9_digestive", ns9_digestive_system_generator.generate),
    ("ns9_forces_cells", ns9_forces_electric_cells_generator.generate),
    ("ns9_reproduction", ns9_human_reproduction_generator.generate),
    ("term1_life", term1_life_and_living_generator.generate),
    ("term2_matter", term2_matter_materials_generator.generate),
    ("term3_energy", term3_energy_change_forces_generator.generate),
    ("term4_earth", term4_planet_earth_beyond_generator.generate),
]

for name, fn in gens:
    try:
        res = fn(seed=42)
        q = res["questions"][0] if isinstance(res, dict) and "questions" in res else (res[0] if isinstance(res, list) else res)
        sub = q.get("subskill")
        topic = q.get("topic")
        diag = q.get("diagram_spec", {}).get("kind") if q.get("diagram_spec") else q.get("modality")
        print(f"[OK] {name:<18} -> topic: {topic} | sub: {sub} | diag: {diag}")
    except Exception as e:
        print(f"[FAIL] {name:<18} -> Error: {e}")
