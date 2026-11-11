"""Automated Coverage Gate for diagrams.md (All 386 Items -> 116 Master Components).

Parses diagrams.md directly from the repository root, verifies that every single
numbered/listed item across Grades 7-12 (Biology, Chemistry, Physics, Earth & Space)
is mapped exactly once to an authoritative Master Component and Renderer Class.

Fails (exit 1) if any item in diagrams.md is unmapped or mapped more than once.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_MD = ROOT / "diagrams.md"


def parse_diagrams_md(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    grade = None
    topic = None
    items = []
    unnumbered_counter = 0

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("# "):
            continue
        m_grade = re.match(r"^##\s+Grade\s+(\d+)", line, re.IGNORECASE)
        if m_grade:
            grade = int(m_grade.group(1))
            topic = None
            continue
        m_topic = re.match(r"^###\s+(.+)$", line)
        if m_topic:
            topic = m_topic.group(1).strip()
            unnumbered_counter = 0
            continue
        if grade and topic:
            m_num = re.match(r"^(\d+)\\?\.\s*(.+)$", line)
            if m_num:
                n = int(m_num.group(1))
                item_text = m_num.group(2).strip()
                items.append({"grade": grade, "topic": topic, "n": n, "text": item_text})
                unnumbered_counter = n
            else:
                if (grade, topic) == (9, "Reaction of acids with a metal") and line.startswith("through water"):
                    unnumbered_counter += 1
                    items.append({"grade": grade, "topic": topic, "n": unnumbered_counter, "text": line})
                elif (grade, topic) in ((9, "Digestive system"), (9, "Resistance"), (12, "Meiosis")):
                    unnumbered_counter += 1
                    items.append({"grade": grade, "topic": topic, "n": unnumbered_counter, "text": line})
    return items


# Renderer classes
VEC = "anatomy_vector"
ILL = "curated_illustration"
APP = "apparatus_vector"
GRF = "graph_plotly"
NOD = "node_graph"
MOL = "molecular_particle_2d"
CIR = "circuit_schematic"
OPT = "optics_ray"
FBD = "mechanics_fbd"
AST = "astronomy_2d_3d"

# Authoritative 116-Master Mapping Table covering all 386 items in diagrams.md
MASTER_COVERAGE = {
    # DOMAIN A: BIOLOGICAL & LIFE SCIENCES (274 items -> 88 masters)
    "heart": ("Biology", VEC, "cardiac_cycle", [(9,"Circulatory and respiratory systems",[8,9]),(10,"Transport systems in animals",[7,8,10])]),
    "circulation_map": ("Biology", VEC, "blood_flow_loop", [(9,"Circulatory and respiratory systems",[2,7]),(9,"Systems in the human body",[2]),(10,"Transport systems in animals",[3,4,5,6,9])]),
    "circulation_types": ("Biology", VEC, None, [(10,"Transport systems in animals",[1,2]),(11,"Biodiversity of animals",[3])]),
    "ecg_rhythms": ("Biology", GRF, "cardiac_cycle", [(10,"Transport systems in animals",[11])]),
    "blood_vessels": ("Biology", VEC, None, [(9,"Circulatory and respiratory systems",[10]),(10,"Transport systems in animals",[12,13])]),
    "cardiovascular_disease": ("Biology", VEC, "plaque_progression", [(10,"Transport systems in animals",[16,17,18,19])]),
    "lymphatic_system": ("Biology", ILL, None, [(10,"Transport systems in animals",[14,15])]),
    "respiratory_system": ("Biology", VEC, "breathing_mechanics", [(9,"Circulatory and respiratory systems",[1,3,4,5]),(9,"Systems in the human body",[3]),(11,"Gaseous exchanges",[1,2,3])]),
    "bell_jar_model": ("Biology", APP, "breathing_mechanics", [(11,"Gaseous exchanges",[4])]),
    "alveolus_exchange": ("Biology", VEC, "gas_diffusion", [(9,"Circulatory and respiratory systems",[6,11]),(11,"Gaseous exchanges",[5,6])]),
    "digestive_system": ("Biology", ILL, None, [(9,"Digestive system",[1]),(9,"Systems in the human body",[1]),(11,"Animal nutrition",[2])]),
    "peristalsis": ("Biology", VEC, "peristalsis", [(11,"Animal nutrition",[3])]),
    "villus": ("Biology", VEC, "absorption", [(11,"Animal nutrition",[4])]),
    "teeth_dentition": ("Biology", ILL, None, [(11,"Animal nutrition",[1]),(10,"Support systems in animals",[3])]),
    "urinary_system": ("Biology", ILL, None, [(9,"Systems in the human body",[5]),(11,"Excretion in humans",[1])]),
    "kidney_ls": ("Biology", ILL, None, [(11,"Excretion in humans",[2,3])]),
    "nephron": ("Biology", VEC, "nephron_processes", [(11,"Excretion in humans",[4,5,6])]),
    "skeleton": ("Biology", ILL, None, [(9,"Systems in the human body",[4]),(10,"Support systems in animals",[1,2,4,5,6,7,8,9,16])]),
    "bone_joint_muscle": ("Biology", VEC, "muscle_contraction", [(10,"Support systems in animals",[10,11,12,13,14,15])]),
    "nervous_system": ("Biology", ILL, None, [(9,"Systems in the human body",[6]),(12,"Human responses to the environment",[1])]),
    "brain": ("Biology", ILL, None, [(12,"Human responses to the environment",[2])]),
    "spinal_cord_reflex": ("Biology", VEC, "reflex_arc", [(12,"Human responses to the environment",[3,8])]),
    "neurons_synapse": ("Biology", VEC, "impulse_transmission", [(10,"Plant and animal tissues",[6]),(12,"Human responses to the environment",[4,5,6,7])]),
    "eye": ("Biology", VEC, "accommodation_pupil", [(8,"Looking into space",[1]),(8,"Visible light",[6,10]),(12,"Human responses to the environment",[9,10,11,12,13,14,15,16])]),
    "ear": ("Biology", VEC, "hearing_balance", [(12,"Human responses to the environment",[17,18,19,20])]),
    "endocrine_glands": ("Biology", ILL, None, [(12,"The human endocrine system and homeostasis",[1,2,3,4,5,6,8])]),
    "glucose_homeostasis": ("Biology", NOD, "negative_feedback", [(12,"The human endocrine system and homeostasis",[7,9,10])]),
    "skin_thermoregulation": ("Biology", VEC, "thermoregulation", [(12,"The human endocrine system and homeostasis",[11,12])]),
    "male_reproductive": ("Biology", ILL, None, [(7,"Sexual reproduction",[3]),(9,"Human reproduction",[1]),(12,"Human reproduction",[2,3])]),
    "female_reproductive": ("Biology", ILL, None, [(7,"Sexual reproduction",[4]),(9,"Human reproduction",[2]),(12,"Human reproduction",[4,7,8])]),
    "reproductive_overview": ("Biology", ILL, None, [(9,"Systems in the human body",[7])]),
    "gametes_fertilisation": ("Biology", VEC, "fertilisation_to_implantation", [(7,"Sexual reproduction",[5]),(9,"Human reproduction",[3]),(12,"Human reproduction",[1,5,6,11])]),
    "foetus_placenta": ("Biology", ILL, None, [(9,"Human reproduction",[4]),(12,"Human reproduction",[12,13])]),
    "menstrual_cycle": ("Biology", GRF, "menstrual_cycle", [(12,"Human reproduction",[9,10])]),
    "amniotic_egg": ("Biology", ILL, None, [(12,"Reproductive strategies in vertebrates",[1])]),
    "animal_cell": ("Biology", VEC, None, [(9,"Cells as the basic units of life",[1,2,3]),(10,"Biodiversity and classification",[2]),(10,"Cells-the basic units of life",[2,9,10,11,12,13,14]),(12,"DNA-The code of life",[1,2]),(12,"Human evolution",[4]),(11,"Cellular respiration",[1])]),
    "plant_cell": ("Biology", VEC, None, [(9,"Cells as the basic units of life",[4]),(10,"Cells-the basic units of life",[15,16]),(11,"Photosynthesis",[2])]),
    "prokaryote": ("Biology", VEC, "binary_fission", [(10,"Biodiversity and classification",[1]),(11,"Biodiversity and classification of micro-organisms",[3,4,5])]),
    "virus": ("Biology", VEC, None, [(11,"Biodiversity and classification of micro-organisms",[2,6,7])]),
    "immunity": ("Biology", VEC, None, [(11,"Biodiversity and classification of micro-organisms",[8])]),
    "immune_response_graph": ("Biology", GRF, None, [(11,"Biodiversity and classification of micro-organisms",[10])]),
    "recombinant_dna": ("Biology", NOD, "gene_cloning", [(11,"Biodiversity and classification of micro-organisms",[9]),(12,"Genetics and inheritance",[7])]),
    "cell_membrane_transport": ("Biology", VEC, "membrane_transport", [(10,"Cells-the basic units of life",[3,4,5,7,8])]),
    "osmosis_cells": ("Biology", VEC, "osmosis", [(10,"Cells-the basic units of life",[6]),(10,"Plant and animal tissues",[15])]),
    "microscope": ("Biology", ILL, None, [(9,"Cells as the basic units of life",[5]),(10,"Cells-the basic units of life",[1])]),
    "levels_of_organisation": ("Biology", ILL, None, [(9,"Cells as the basic units of life",[6]),(10,"Plant and animal tissues",[1])]),
    "animal_tissues": ("Biology", ILL, None, [(10,"Plant and animal tissues",[4,5,7])]),
    "plant_tissues": ("Biology", ILL, None, [(10,"Plant and animal tissues",[2,3])]),
    "leaf": ("Biology", VEC, "stomatal_gas_exchange", [(10,"Plant and animal tissues",[9])]),
    "root": ("Biology", VEC, "water_uptake", [(10,"Plant and animal tissues",[10])]),
    "stem": ("Biology", VEC, "secondary_thickening", [(10,"Plant and animal tissues",[11,12])]),
    "water_transport": ("Biology", VEC, "transpiration_translocation", [(10,"Plant and animal tissues",[16,17])]),
    "transpiration_graphs": ("Biology", GRF, None, [(10,"Plant and animal tissues",[13])]),
    "potometer": ("Biology", APP, "transpiration_translocation", [(10,"Plant and animal tissues",[14])]),
    "cloning": ("Biology", NOD, None, [(10,"Plant and animal tissues",[8])]),
    "flower": ("Biology", VEC, "pollination", [(7,"Sexual reproduction",[1,2]),(11,"Biodiversity of plants",[1,2,3])]),
    "seeds": ("Biology", ILL, None, [(11,"Biodiversity of plants",[4,5])]),
    "photosynthesis_overview": ("Biology", VEC, "photosynthesis_phases", [(7,"Relation of the sun to the earth",[8]),(8,"Photosynthesis and respiration",[1]),(11,"Photosynthesis",[1,3,4])]),
    "photosynthesis_graphs": ("Biology", GRF, None, [(11,"Photosynthesis",[5])]),
    "photosynthesis_experiments": ("Biology", APP, None, [(11,"Photosynthesis",[6,7,8])]),
    "respiration_experiments": ("Biology", APP, None, [(8,"Photosynthesis and respiration",[2]),(11,"Cellular respiration",[2,3])]),
    "tropisms": ("Biology", VEC, "tropism_growth", [(12,"Plant responses to the environment",[1])]),
    "classification_trees": ("Biology", NOD, None, [(7,"Biodiversity",[1,2,4,5]),(8,"Microorganisms",[1]),(11,"Biodiversity and classification of micro-organisms",[1])]),
    "vertebrates_invertebrates": ("Biology", ILL, None, [(7,"Biodiversity",[3])]),
    "body_plans": ("Biology", VEC, None, [(11,"Biodiversity of animals",[1,2])]),
    "food_webs_pyramids": ("Biology", NOD, None, [(8,"Interactions and interdepence within the environment",[1]),(10,"Biospheres to ecosystems",[2])]),
    "biomes_map": ("Biology", ILL, None, [(10,"Biospheres to ecosystems",[1])]),
    "nutrient_cycles": ("Biology", NOD, "cycle_flow", [(7,"The biosphere",[1]),(10,"Biospheres to ecosystems",[3,4,5,6])]),
    "population_graphs": ("Biology", GRF, None, [(11,"Population ecology",[1,2,3,4,5,6,7,10])]),
    "community_structure": ("Biology", ILL, "succession", [(11,"Population ecology",[8,9])]),
    "human_impact": ("Biology", ILL, None, [(11,"Human impact on the environment",[2,3,4,5,6,7])]),
    "atmosphere_pie": ("Biology", GRF, None, [(11,"Human impact on the environment",[1])]),
    "history_of_life": ("Biology", NOD, "continental_drift", [(10,"History of life on earth",[1,2])]),
    "radiometric_graph": ("Biology", GRF, None, [(10,"History of life on earth",[3])]),
    "eutrophication": ("Biology", NOD, None, [(10,"The chemistry of life",[1])]),
    "biomolecules": ("Biology", MOL, None, [(10,"The chemistry of life",[2,3,5,6])]),
    "food_tests": ("Biology", APP, None, [(10,"The chemistry of life",[4])]),
    "enzymes": ("Biology", VEC, "lock_and_key", [(10,"The chemistry of life",[8])]),
    "enzyme_graphs": ("Biology", GRF, None, [(10,"The chemistry of life",[7,9])]),
    "dna_rna_structure": ("Biology", MOL, "dna_replication", [(10,"The chemistry of life",[10]),(12,"DNA-The code of life",[3,4])]),
    "protein_synthesis": ("Biology", VEC, "protein_synthesis", [(12,"DNA-The code of life",[6,7])]),
    "dna_profiling": ("Biology", VEC, None, [(12,"DNA-The code of life",[5])]),
    "chromosomes_division": ("Biology", VEC, "mitosis_meiosis", [(10,"Cell division",[1,2]),(12,"Meiosis",[1,2,3,4,5]),(12,"Genetics and inheritance",[1])]),
    "genetic_crosses_karyotypes": ("Biology", VEC, None, [(12,"Genetics and inheritance",[2,3,6])]),
    "pedigrees": ("Biology", NOD, None, [(12,"Genetics and inheritance",[4,5])]),
    "evolution_models": ("Biology", GRF, "natural_selection", [(12,"Evolution by natural selection",[1,2])]),
    "human_evolution_trees": ("Biology", NOD, None, [(12,"Human evolution",[1,2,3])]),
    "tongue": ("Biology", ILL, None, [(7,"Acids and bases",[1])]),

    # DOMAIN B: MATTER, CHEMISTRY & LAB APPARATUS (36 items -> 9 masters)
    "periodic_table_element_tile": ("Chemistry", MOL, None, [
        (7,"The periodic table",[1]),
        (8,"Atoms",[1]),
        (9,"Compounds",[4,5]),
    ]),
    "atomic_bohr_structure": ("Chemistry", MOL, None, [
        (8,"Atoms",[2]),
        (8,"Particle model of matter",[2]),
    ]),
    "particle_states_of_matter": ("Chemistry", MOL, "phase_change_kinetics", [
        (7,"Properties of materials",[1]),
        (8,"Particle model of matter",[1,3,4,5,6]),
    ]),
    "submicroscopic_atoms_molecules_reactions": ("Chemistry", MOL, "reaction_rearrangement", [
        (8,"Atoms",[3,4,5,6]),
        (8,"Chemical reactions",[1]),
        (9,"Chemical reactions",[1,2]),
        (9,"Compounds",[1]),
        (9,"Reactions of metals with oxygen",[1]),
        (9,"The atmosphere",[2,3,4]),
    ]),
    "crystal_lattices": ("Chemistry", MOL, None, [
        (9,"Compounds",[2,3]),
    ]),
    "separation_distillation_chromatography": ("Chemistry", APP, "chromatography_elution", [
        (7,"Separating mixtures",[1,2]),
    ]),
    "ph_scale_indicators": ("Chemistry", GRF, "indicator_titration_color", [
        (9,"Acids, bases and the pH value",[1,2]),
        (9,"Acids and bases",[1]),
    ]),
    "gas_reactions_acid_metal_apparatus": ("Chemistry", APP, "hydrogen_pop_test", [
        (9,"Reaction of acids with a metal",[1,2,3]),
    ]),
    "electrochemistry_cells_apparatus": ("Chemistry", APP, "ion_electron_migration", [
        (8,"Energy transfer in electrical system",[4]),
        (9,"Electric cells as energy systems",[1]),
    ]),

    # DOMAIN C: ENERGY, ELECTRICITY, OPTICS & MECHANICS (49 items -> 11 masters)
    "sankey_energy_flow": ("Physics", GRF, None, [
        (7,"Energy transfer to the surroundings",[1]),
        (9,"Resistance",[1]),
    ]),
    "heat_transfer_mechanisms": ("Physics", APP, "convection_conduction_flow", [
        (7,"Energy transfer to the surroundings",[2,3,4]),
        (7,"Heat insulation and energy transfer",[1]),
    ]),
    "power_stations_national_grid": ("Physics", ILL, "power_generation_flow", [
        (7,"Potential and kinetic energy",[3]),
        (7,"The national electricity supply system",[1,2]),
        (9,"Energy and the national electricity grid",[1,2,3]),
    ]),
    "mechanics_inclines_pulleys_forces": ("Physics", FBD, "mechanical_advantage", [
        (7,"Potential and kinetic energy",[1,2]),
        (9,"Forces",[1,2,4]),
    ]),
    "metallic_conduction_sea_of_electrons": ("Physics", MOL, "electron_drift", [
        (8,"Energy transfer in electrical system",[1]),
        (8,"Series and parallel- circuits",[1]),
    ]),
    "electric_circuits_ammeter": ("Physics", CIR, "circuit_current_flow", [
        (8,"Energy transfer in electrical system",[2]),
        (8,"Series and parallel- circuits",[2,3]),
    ]),
    "electrical_safety_mains_plug": ("Physics", CIR, "circuit_breaker_trip", [
        (9,"Safety with electricity",[1,2,3,4]),
    ]),
    "magnetism_field_lines": ("Physics", FBD, "magnetic_field_interaction", [
        (8,"Energy transfer in electrical system",[3]),
        (9,"Forces",[5,6,7,8]),
    ]),
    "electrostatics_charge_transfer": ("Physics", FBD, "charge_induction", [
        (8,"Static electricity",[1]),
        (9,"Forces",[9,10,11]),
    ]),
    "optics_rays_lenses_prisms": ("Physics", OPT, "ray_refraction_dispersion", [
        (8,"Visible light",[1,2,3,4,5,7,8,9]),
    ]),
    "telescopes_optics": ("Physics", OPT, "telescope_ray_path", [
        (8,"Looking into space",[2,3,4,5,6,7]),
    ]),

    # DOMAIN D: EARTH SYSTEMS, MINING & ASTRONOMY (27 items -> 8 masters)
    "solar_system_planets": ("Earth & Space", AST, "orbital_motion", [
        (7,"Historical development of astronomy",[1]),
        (7,"Relation of the sun to the earth",[1,7]),
        (8,"The solar system",[1]),
        (9,"Forces",[3]),
    ]),
    "earth_rotation_seasons_sun_path": ("Earth & Space", AST, "seasons_insolation", [
        (7,"Relation of the sun to the earth",[2,3,4,5,6]),
        (7,"Sources of energy",[1]),
    ]),
    "moon_orbit_tides": ("Earth & Space", AST, "spring_neap_tides", [
        (7,"Relationship of the moon to the earth",[1,2]),
    ]),
    "milky_way_stellar_neighborhood": ("Earth & Space", AST, None, [
        (8,"Beyond the solar system",[1,2]),
        (9,"Birth, life, and the death of a star",[1]),
    ]),
    "earth_spheres_internal_layers": ("Earth & Space", ILL, None, [
        (9,"the earth as a system",[1]),
        (9,"the lithosphere",[1,2]),
    ]),
    "rock_water_cycles_earth": ("Earth & Space", NOD, "rock_cycle_transitions", [
        (9,"the lithosphere",[3,4]),
    ]),
    "atmosphere_greenhouse_acid_rain": ("Earth & Space", ILL, "greenhouse_radiation_balance", [
        (9,"Acids and bases",[2]),
        (9,"The atmosphere",[1,5]),
    ]),
    "mining_mineral_extraction": ("Earth & Space", ILL, "blast_furnace_smelting", [
        (9,"Mining of mineral resources",[1,2,3]),
    ]),
}


def main():
    items = parse_diagrams_md(DIAGRAMS_MD)
    idx = {(i["grade"], i["topic"], i["n"]): i for i in items}
    assigned = defaultdict(list)
    errors = []

    for mid, (dom, rend, sim, refs) in MASTER_COVERAGE.items():
        for g, t, ns in refs:
            for n in ns:
                k = (g, t, n)
                if k not in idx:
                    errors.append(f"BAD REF in {mid}: {k} not found in diagrams.md")
                assigned[k].append(mid)

    for i in items:
        k = (i["grade"], i["topic"], i["n"])
        if not assigned.get(k):
            errors.append(f"UNMAPPED ITEM: G{k[0]} {k[1]} #{k[2]}: {i['text'][:70]}")
        elif len(assigned[k]) > 1:
            errors.append(f"DUPLICATE MAPPING: {k} -> {assigned[k]}")

    if errors:
        print("[FAIL] diagrams.md Coverage Gate failed with errors:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    print(
        f"[PASS] diagrams.md Coverage Gate: {len(items)}/{len(items)} items mapped across "
        f"{len(MASTER_COVERAGE)} Master Components (0 gaps, 0 duplicates)."
    )


if __name__ == "__main__":
    main()
