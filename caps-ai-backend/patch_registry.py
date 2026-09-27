import sys

registry_path = "app/services/generator_registry.py"

with open(registry_path, "r", encoding="utf-8") as f:
    content = f.read()

imports = """
from app.utils.grade10_physical_sciences import waves_sound_light_generator as phys10_waves
from app.utils.grade10_physical_sciences import matter_materials_generator as phys10_matter
from app.utils.grade11_physical_sciences import vectors_newton_generator as phys11_vec
from app.utils.grade12_physical_sciences import vertical_projectile_generator as phys12_proj
from app.utils.grade12_physical_sciences import doppler_effect_generator as phys12_doppler
from app.utils.life_sciences import meiosis_human_reproduction_generator as ls_meiosis

PHYS_LS_GENERATORS = {
    "grade10_physical_sciences_waves_sound_light": phys10_waves.generate,
    "grade10_physical_sciences_matter_materials": phys10_matter.generate,
    "grade11_physical_sciences_vectors_newton": phys11_vec.generate,
    "grade12_physical_sciences_vertical_projectile": phys12_proj.generate,
    "grade12_physical_sciences_doppler_effect": phys12_doppler.generate,
    "life_sciences_meiosis_human_reproduction": ls_meiosis.generate,
}
"""

aliases = """    "waves sound and light": "grade10_physical_sciences_waves_sound_light",
    "waves": "grade10_physical_sciences_waves_sound_light",
    "matter and materials": "grade10_physical_sciences_matter_materials",
    "matter": "grade10_physical_sciences_matter_materials",
    "vectors and newtons laws": "grade11_physical_sciences_vectors_newton",
    "vectors": "grade11_physical_sciences_vectors_newton",
    "vertical projectile motion": "grade12_physical_sciences_vertical_projectile",
    "vertical projectile": "grade12_physical_sciences_vertical_projectile",
    "doppler effect": "grade12_physical_sciences_doppler_effect",
    "doppler": "grade12_physical_sciences_doppler_effect",
    "meiosis": "life_sciences_meiosis_human_reproduction",
    "human reproduction": "life_sciences_meiosis_human_reproduction",
"""

if "PHYS_LS_GENERATORS" not in content:
    # insert before ALL_GENERATORS = {
    content = content.replace("ALL_GENERATORS: Dict[str, Callable] = {", imports + "\nALL_GENERATORS: Dict[str, Callable] = {\n    **PHYS_LS_GENERATORS,")
    
    # insert aliases
    content = content.replace("TOPIC_ALIASES: Dict[str, str] = {", "TOPIC_ALIASES: Dict[str, str] = {\n" + aliases)

    with open(registry_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched generator_registry.py")
else:
    print("Already patched")
