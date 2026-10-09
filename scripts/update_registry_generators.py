"""Script to update generator_registry.py with newly built generator engines."""
import re

with open("caps-ai-backend/app/services/generator_registry.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Grade 8 Math import
old_g8_import = """from app.utils.grade8_mathematics import (
    pythagoras_generator as g8_math_pyth,
    integers_generator as g8_math_int,
    algebraic_expressions_equations_generator as g8_math_alg,
    geometry_straight_lines_generator as g8_math_lines,
    measurement_3d_generator as g8_math_meas3d,
    fractions_decimals_generator as g8_math_frac_dec,
    geometry_2d_shapes_generator as g8_math_geom2d,
)"""

new_g8_import = """from app.utils.grade8_mathematics import (
    pythagoras_generator as g8_math_pyth,
    integers_generator as g8_math_int,
    algebraic_expressions_equations_generator as g8_math_alg,
    geometry_straight_lines_generator as g8_math_lines,
    measurement_3d_generator as g8_math_meas3d,
    fractions_decimals_generator as g8_math_frac_dec,
    geometry_2d_shapes_generator as g8_math_geom2d,
    geometry_3d_objects_generator as g8_math_3d_obj,
)"""

assert old_g8_import in content, "Could not find old_g8_import"
content = content.replace(old_g8_import, new_g8_import)

# 2. Update Grade 12 Physical Sciences imports
old_g12_ps_import = """from app.utils.grade12_physical_sciences import (
    stoichiometry_equilibrium_generator as phys_chem_eq,
    momentum_impulse_generator as phys_momentum,
)"""

new_g12_ps_import = """from app.utils.grade12_physical_sciences import (
    stoichiometry_equilibrium_generator as phys_chem_eq,
    momentum_impulse_generator as phys_momentum,
    vertical_projectile_generator as phys12_proj,
    doppler_effect_generator as phys12_doppler,
    organic_chemistry_generator as phys12_organic,
    acids_bases_generator as phys12_acids_bases,
    electrodynamics_circuits_generator as phys12_electrodyn,
    optical_phenomena_photoelectric_generator as phys12_photoelectric,
)"""

assert old_g12_ps_import in content, "Could not find old_g12_ps_import"
content = content.replace(old_g12_ps_import, new_g12_ps_import)

# 3. Update Grade 11 Physical Sciences imports
old_g11_ps_import = """from app.utils.grade11_physical_sciences import (
    chemical_bonding_intermolecular_generator as phys11_chem,
)"""

new_g11_ps_import = """from app.utils.grade11_physical_sciences import (
    vectors_newton_generator as phys11_vec,
    chemical_bonding_intermolecular_generator as phys11_chem,
    electric_circuits_energy_generator as phys11_circuits,
    energy_chemical_change_generator as phys11_energy,
    stoichiometry_limiting_generator as phys11_stoich,
)"""

assert old_g11_ps_import in content, "Could not find old_g11_ps_import"
content = content.replace(old_g11_ps_import, new_g11_ps_import)

# 4. Update Technical Mathematics imports
old_tech_import = """from app.utils.technical_mathematics import (
    complex_numbers_generator as tech_cplx,
    mensuration_calculus_generator as tech_mens,
)"""

new_tech_import = """from app.utils.technical_mathematics import (
    complex_numbers_generator as tech_cplx,
    mensuration_calculus_generator as tech_mens,
    circles_angular_movement_generator as tech_circles,
)"""

assert old_tech_import in content, "Could not find old_tech_import"
content = content.replace(old_tech_import, new_tech_import)

# 5. Update Grade 10 Physical Sciences imports around line 850
old_ps_strand_imports = """from app.utils.grade10_physical_sciences import waves_sound_light_generator as phys10_waves
from app.utils.grade10_physical_sciences import matter_materials_generator as phys10_matter
from app.utils.grade11_physical_sciences import vectors_newton_generator as phys11_vec
from app.utils.grade12_physical_sciences import vertical_projectile_generator as phys12_proj
from app.utils.grade12_physical_sciences import doppler_effect_generator as phys12_doppler
from app.utils.life_sciences import meiosis_human_reproduction_generator as ls_meiosis
from app.utils.physical_sciences import electrostatics_electromagnetism_generator as phys_electro"""

new_ps_strand_imports = """from app.utils.grade10_physical_sciences import (
    waves_sound_light_generator as phys10_waves,
    matter_materials_generator as phys10_matter,
    electric_circuits_magnetism_generator as phys10_circuits,
    chemical_change_stoichiometry_generator as phys10_chem,
    motion_energy_generator as phys10_motion,
)
from app.utils.life_sciences import meiosis_human_reproduction_generator as ls_meiosis
from app.utils.physical_sciences import electrostatics_electromagnetism_generator as phys_electro"""

assert old_ps_strand_imports in content, "Could not find old_ps_strand_imports"
content = content.replace(old_ps_strand_imports, new_ps_strand_imports)

# 6. Update GRADE8_MATH_GENERATORS 3D mapping
old_g8_3d = '"grade8_math_geometry_of_3d_objects": g7_math_nets.generate,'
new_g8_3d = '"grade8_math_geometry_of_3d_objects": g8_math_3d_obj.generate,\n    "grade8_math_3d_objects": g8_math_3d_obj.generate,'
assert old_g8_3d in content, "Could not find old_g8_3d"
content = content.replace(old_g8_3d, new_g8_3d)

# 7. Update SCIENCES_AND_TECH_GENERATORS
old_tech_dict = """    "technical_mathematics_analytical_geometry": g12_math_circles.generate,
    "grade11_physical_sciences_chemistry": phys11_chem.generate,"""

new_tech_dict = """    "technical_mathematics_analytical_geometry": g12_math_circles.generate,
    "technical_mathematics_circles_angles": tech_circles.generate,
    "technical_mathematics_angular_movement": tech_circles.generate,
    "grade11_physical_sciences_chemistry": phys11_chem.generate,"""

assert old_tech_dict in content, "Could not find old_tech_dict"
content = content.replace(old_tech_dict, new_tech_dict)

# 8. Update PHYS_LS_GENERATORS
old_phys_dict = """PHYS_LS_GENERATORS = {
    "grade10_physical_sciences_waves_sound_light": phys10_waves.generate,
    "grade10_physical_sciences_waves": phys10_waves.generate,
    "grade10_physical_sciences_matter_materials": phys10_matter.generate,
    "grade10_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_vectors_newton": phys11_vec.generate,
    "grade11_physical_sciences_vectors": phys11_vec.generate,
    "grade11_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_electromagnetism": phys_electro.generate,
    "grade12_physical_sciences_vertical_projectile": phys12_proj.generate,
    "grade12_physical_sciences_doppler_effect": phys12_doppler.generate,
    "grade12_physical_sciences_doppler": phys12_doppler.generate,
    "life_sciences_meiosis_human_reproduction": ls_meiosis.generate,
    "physical_sciences_electrostatics": phys_electro.generate,
    "physical_sciences_electromagnetism": phys_electro.generate,"""

new_phys_dict = """PHYS_LS_GENERATORS = {
    # Grade 10 Physical Sciences
    "grade10_physical_sciences_waves_sound_light": phys10_waves.generate,
    "grade10_physical_sciences_waves": phys10_waves.generate,
    "grade10_physical_sciences_matter_materials": phys10_matter.generate,
    "grade10_physical_sciences_electrostatics": phys_electro.generate,
    "grade10_physical_sciences_electric_circuits": phys10_circuits.generate,
    "grade10_physical_sciences_chemical_change": phys10_chem.generate,
    "grade10_physical_sciences_stoichiometry": phys10_chem.generate,
    "grade10_physical_sciences_motion_energy": phys10_motion.generate,
    # Grade 11 Physical Sciences
    "grade11_physical_sciences_vectors_newton": phys11_vec.generate,
    "grade11_physical_sciences_vectors": phys11_vec.generate,
    "grade11_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_electromagnetism": phys_electro.generate,
    "grade11_physical_sciences_electric_circuits": phys11_circuits.generate,
    "grade11_physical_sciences_energy_chemical_change": phys11_energy.generate,
    "grade11_physical_sciences_stoichiometry_limiting": phys11_stoich.generate,
    # Grade 12 Physical Sciences
    "grade12_physical_sciences_vertical_projectile": phys12_proj.generate,
    "grade12_physical_sciences_doppler_effect": phys12_doppler.generate,
    "grade12_physical_sciences_doppler": phys12_doppler.generate,
    "grade12_physical_sciences_organic_chemistry": phys12_organic.generate,
    "grade12_physical_sciences_organic_molecules": phys12_organic.generate,
    "grade12_physical_sciences_acids_bases": phys12_acids_bases.generate,
    "grade12_physical_sciences_electrodynamics": phys12_electrodyn.generate,
    "grade12_physical_sciences_electric_circuits": phys12_electrodyn.generate,
    "grade12_physical_sciences_optical_phenomena": phys12_photoelectric.generate,
    "grade12_physical_sciences_photoelectric_effect": phys12_photoelectric.generate,
    "life_sciences_meiosis_human_reproduction": ls_meiosis.generate,
    "physical_sciences_electrostatics": phys_electro.generate,
    "physical_sciences_electromagnetism": phys_electro.generate,"""

assert old_phys_dict in content, "Could not find old_phys_dict"
content = content.replace(old_phys_dict, new_phys_dict)

# 9. Update routing logic in resolve_generator_key
old_phys_routing = """    # Physical Sciences grade-specific chemistry / physics routing
    if is_phys:
        if grade_num == "11" and any(w in clean for w in ["atomic", "intermolecular", "bonding", "vsepr", "molecular", "lithosphere"]):
            return "grade11_physical_sciences_chemistry"
        if grade_num == "11" and any(w in clean for w in ["vector", "newton", "force", "unit"]):
            return "grade11_physical_sciences_vectors_newton"
        if grade_num == "10" and any(w in clean for w in ["wave", "sound", "light"]):
            return "grade10_physical_sciences_waves_sound_light"
        if grade_num == "10" and any(w in clean for w in ["matter", "material"]):
            return "grade10_physical_sciences_matter_materials"
        if grade_num == "12" and any(w in clean for w in ["momentum", "impulse"]):
            return "grade12_physical_sciences_momentum"
        if grade_num == "12" and any(w in clean for w in ["projectile", "vertical", "skill"]):
            return "grade12_physical_sciences_vertical_projectile"
        if grade_num == "12" and "doppler" in clean:
            return "grade12_physical_sciences_doppler_effect" """

new_phys_routing = """    # Physical Sciences grade-specific chemistry / physics routing
    if is_phys:
        if grade_num == "12":
            if any(w in clean for w in ["organic", "alkane", "alkene", "alkyne", "haloalkane", "alcohol", "ester", "aldehyde", "ketone", "carboxylic", "iupac", "isomer"]):
                return "grade12_physical_sciences_organic_chemistry"
            if any(w in clean for w in ["acid", "base", "ph", "titrat", "hydrolysis", "neutralis", "amphiprotic", "ampholyte", "kw", "h3o"]):
                return "grade12_physical_sciences_acids_bases"
            if any(w in clean for w in ["electrodynamic", "generator", "motor", "alternat", "rms", "internal resistance", "lost volt", "circuit", "slip ring", "commutator"]):
                return "grade12_physical_sciences_electrodynamics"
            if any(w in clean for w in ["photoelectric", "optical", "work function", "threshold frequency", "photon", "cut off", "spectra"]):
                return "grade12_physical_sciences_optical_phenomena"
            if any(w in clean for w in ["momentum", "impulse"]):
                return "grade12_physical_sciences_momentum"
            if any(w in clean for w in ["projectile", "vertical", "skill"]):
                return "grade12_physical_sciences_vertical_projectile"
            if "doppler" in clean:
                return "grade12_physical_sciences_doppler_effect"
            if any(w in clean for w in ["rate", "extent", "equilibrium", "le chatelier", "kc", "chemical industry", "fertilizer", "haber", "contact"]):
                return "physical_sciences_chemistry_equilibrium"
            if any(w in clean for w in ["work", "energy", "power"]):
                return "physical_sciences_work_energy_power"
            if any(w in clean for w in ["galvanic", "electrolytic", "electrochem", "cell"]):
                return "physical_sciences_electrochemistry"

        if grade_num == "11":
            if any(w in clean for w in ["circuit", "ohm", "resistor", "series", "parallel", "tariff", "kwh", "cost"]):
                return "grade11_physical_sciences_electric_circuits"
            if any(w in clean for w in ["enthalpy", "delta h", "bond energy", "activated complex", "activation energy", "exothermic", "endothermic"]):
                return "grade11_physical_sciences_energy_chemical_change"
            if any(w in clean for w in ["limiting", "excess", "yield", "purity", "stoichiometr"]):
                return "grade11_physical_sciences_stoichiometry_limiting"
            if any(w in clean for w in ["atomic", "intermolecular", "bonding", "vsepr", "molecular", "lithosphere"]):
                return "grade11_physical_sciences_chemistry"
            if any(w in clean for w in ["vector", "newton", "force", "unit"]):
                return "grade11_physical_sciences_vectors_newton"
            if any(w in clean for w in ["ideal gas", "boyle", "charles", "gas"]):
                return "physical_sciences_ideal_gases_thermal"
            if any(w in clean for w in ["optics", "snell", "refraction", "critical angle", "reflection", "wavefront"]):
                return "physical_sciences_geometrical_optics"
            if any(w in clean for w in ["electrostatic", "coulomb", "electric field"]):
                return "physical_sciences_electrostatics"
            if any(w in clean for w in ["electromagnet", "faraday", "magnetic flux"]):
                return "physical_sciences_electromagnetism"

        if grade_num == "10":
            if any(w in clean for w in ["circuit", "magnet", "charge", "current", "potential difference", "emf", "resistor"]):
                return "grade10_physical_sciences_electric_circuits"
            if any(w in clean for w in ["mole", "empirical", "composition", "stoichiometr", "stoichiometry", "aqueous", "stp", "chemical change"]):
                return "grade10_physical_sciences_chemical_change"
            if any(w in clean for w in ["motion", "kinematic", "acceleration", "displacement", "velocity", "mechanical energy", "potential energy", "kinetic energy"]):
                return "grade10_physical_sciences_motion_energy"
            if any(w in clean for w in ["wave", "sound", "light", "pulse", "radiation"]):
                return "grade10_physical_sciences_waves_sound_light"
            if any(w in clean for w in ["matter", "material", "atom", "periodic", "bonding", "hydrosphere"]):
                return "grade10_physical_sciences_matter_materials"
            if any(w in clean for w in ["electrostatic"]):
                return "physical_sciences_electrostatics" """

# Strip trailing spaces for robust matching
content = re.sub(
    r"\s*# Physical Sciences grade-specific chemistry / physics routing\s+if is_phys:.*?if grade_num == \"12\" and \"doppler\" in clean:\s+return \"grade12_physical_sciences_doppler_effect\"",
    "\n" + new_phys_routing.strip(),
    content,
    flags=re.DOTALL
)

# 10. Update Grade 8 Math 3D routing in resolve_generator_key
old_g8_math_routing = """        if grade_num == "8":
            if any(w in clean for w in ["pythagoras", "hypotenuse", "right-angled"]):
                return "grade8_math_pythagoras" """

new_g8_math_routing = """        if grade_num == "8":
            if any(w in clean for w in ["3d", "polyhedr", "euler", "platonic", "solid"]):
                return "grade8_math_geometry_of_3d_objects"
            if any(w in clean for w in ["pythagoras", "hypotenuse", "right-angled"]):
                return "grade8_math_pythagoras" """

content = content.replace(old_g8_math_routing.strip(), new_g8_math_routing.strip())

# 11. Update Technical Mathematics routing in resolve_generator_key
old_tech_routing = """        if "analytical" in clean:
            return "technical_mathematics_analytical_geometry" """

new_tech_routing = """        if any(w in clean for w in ["circle", "angle", "angular", "movement", "arc", "sector", "radian"]):
            return "technical_mathematics_circles_angles"
        if "analytical" in clean:
            return "technical_mathematics_analytical_geometry" """

content = content.replace(old_tech_routing.strip(), new_tech_routing.strip())

with open("caps-ai-backend/app/services/generator_registry.py", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated generator_registry.py successfully! Total lines: {len(content.splitlines())}")
