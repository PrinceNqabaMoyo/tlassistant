import json

# 1. Update caps-ai-backend/app/services/generator_registry.py
p_reg = 'caps-ai-backend/app/services/generator_registry.py'
with open(p_reg, 'r', encoding='utf-8') as f:
    c = f.read()

import_target = '''    ns9_forces_electric_cells_generator as ns9_electric_cells,
    ns8_solar_system_seasons_generator as ns8_solar_gen,
)'''

import_replacement = '''    ns9_forces_electric_cells_generator as ns9_electric_cells,
    ns8_solar_system_seasons_generator as ns8_solar_gen,
    ns8_photosynthesis_respiration_generator as ns8_photosynth,
    ns8_ecology_interactions_generator as ns8_ecology,
    ns8_atoms_subatomic_generator as ns8_atoms,
    ns8_chemical_reactions_generator as ns8_chem_reactions,
    ns8_microorganisms_generator as ns8_microorganisms,
    ns8_energy_transfer_electrical_generator as ns8_energy_transfer,
    ns8_static_electricity_generator as ns8_static_elec,
    ns8_visible_light_generator as ns8_visible_light,
    ns8_beyond_solar_system_generator as ns8_beyond_solar,
    ns8_telescopes_space_exploration_generator as ns8_telescopes,
)'''

if import_target in c:
    c = c.replace(import_target, import_replacement, 1)
    print("Added Grade 8 NS imports to generator_registry.py")
else:
    print("Import target not found in generator_registry.py")

# Add entries to ALL_GENERATORS dictionary
entries_target = '''    "natural_sciences_particle_model_matter": ns8_particles.generate,
    "grade8_natural_sciences_particle_model_matter": ns8_particles.generate,
    "natural_sciences_series_parallel_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_electric_circuits": ns8_circuits_gen.generate,'''

entries_replacement = '''    "natural_sciences_particle_model_matter": ns8_particles.generate,
    "grade8_natural_sciences_particle_model_matter": ns8_particles.generate,
    "natural_sciences_series_parallel_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_electric_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_photosynthesis": ns8_photosynth.generate,
    "grade8_natural_sciences_ecology": ns8_ecology.generate,
    "grade8_natural_sciences_atoms": ns8_atoms.generate,
    "grade8_natural_sciences_chemical_reactions": ns8_chem_reactions.generate,
    "grade8_natural_sciences_microorganisms": ns8_microorganisms.generate,
    "grade8_natural_sciences_energy_transfer": ns8_energy_transfer.generate,
    "grade8_natural_sciences_static_electricity": ns8_static_elec.generate,
    "grade8_natural_sciences_visible_light": ns8_visible_light.generate,
    "grade8_natural_sciences_beyond_solar_system": ns8_beyond_solar.generate,
    "grade8_natural_sciences_telescopes": ns8_telescopes.generate,'''

if entries_target in c:
    c = c.replace(entries_target, entries_replacement, 1)
    print("Added Grade 8 NS generator mapping to ALL_GENERATORS")
else:
    print("Entries target not found in generator_registry.py")

with open(p_reg, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Update caps_term_registry_data.json
p_json = 'caps-ai-backend/app/services/caps_term_registry_data.json'
with open(p_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

mapping = {
    "Photosynthesis and respiration": "grade8_natural_sciences_photosynthesis",
    "Interactions and interdependence within the environment": "grade8_natural_sciences_ecology",
    "Atoms": "grade8_natural_sciences_atoms",
    "Particle model of matter": "grade8_natural_sciences_particle_model_matter",
    "Chemical reactions": "grade8_natural_sciences_chemical_reactions",
    "Microorganisms": "grade8_natural_sciences_microorganisms",
    "Energy transfer in electrical systems": "grade8_natural_sciences_energy_transfer",
    "Static electricity": "grade8_natural_sciences_static_electricity",
    "Series and parallel circuits": "grade8_natural_sciences_electric_circuits",
    "Visible light": "grade8_natural_sciences_visible_light",
    "Beyond the solar system": "grade8_natural_sciences_beyond_solar_system",
    "The Solar System": "grade8_natural_sciences_solar_system",
    "Looking into space": "grade8_natural_sciences_telescopes",
}

updated_count = 0
for t in data:
    if str(t.get('grade')) == '8' and t.get('subject') == 'Natural Sciences':
        name = t.get('name')
        if name in mapping:
            t['generator_key'] = mapping[name]
            updated_count += 1

with open(p_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {updated_count} Grade 8 Natural Sciences topics in caps_term_registry_data.json")
