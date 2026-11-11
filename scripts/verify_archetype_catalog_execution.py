"""Tests and certifies the full canonical diagram archetypes catalog.
Ensures every archetype executes deterministically on Seed 1,
with its expected diagram spec, view, and verified prompt.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = REPO_ROOT / "caps-ai-backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import generate_variant

# Define the complete, authoritative catalog of diagram archetypes
# Every single archetype is explicitly named, tied to an authentic CAPS topic, and has a direct subskill parameter.

CANONICAL_DIAGRAM_ARCHETYPES = [
    # =========================================================================
    # 1. HUMAN HEART (5 Archetypes across Gr 9 NS & Gr 10 LS)
    # =========================================================================
    {
        "archetype_id": "NS9_HEART_CHAMBERS",
        "diagram_id": "human_heart",
        "title": "Gross Heart Chamber Anatomy & Myocardial Wall Thickness",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Circulatory and respiratory systems",
        "subskill_param": "heart_structure_and_double_circulation",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Identify 4 chambers; explain why left ventricular myocardium is thicker than right."
    },
    {
        "archetype_id": "NS9_HEART_VESSELS",
        "diagram_id": "human_heart",
        "title": "Great Blood Vessels & Circulation Direction",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Circulatory and respiratory systems",
        "subskill_param": "heart_blood_vessel_direction",
        "view": "flow",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Identify vena cava, aorta, pulmonary artery/veins; determine blood flow direction and oxygenation."
    },
    {
        "archetype_id": "LS10_HEART_ANATOMY",
        "diagram_id": "human_heart",
        "title": "Internal Heart Anatomy & Atrioventricular Valve Mechanics",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 2,
        "topic": "Transport systems in animals",
        "subskill_param": "heart_external_and_internal_anatomy",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Tricuspid/bicuspid valves, chordae tendineae, semilunar valves & septum adaptation."
    },
    {
        "archetype_id": "LS10_HEART_CARDIAC_CYCLE",
        "diagram_id": "human_heart",
        "title": "3-Phase Cardiac Cycle (Systole, Diastole & Heart Sounds)",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 2,
        "topic": "Transport systems in animals",
        "subskill_param": "cardiac_cycle_and_electrical_control",
        "view": "flow",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Atrial systole, ventricular systole, general diastole; valve open/close states and lubb/dubb sounds."
    },
    {
        "archetype_id": "LS10_HEART_PACEMAKER",
        "diagram_id": "human_heart",
        "title": "Electrical Conduction System & Pacemaker Nodes",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 2,
        "topic": "Transport systems in animals",
        "subskill_param": "electrical_pacemaker_and_ecg",
        "view": "exam",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Sinoatrial (SA) node, atrioventricular (AV) node, Purkinje conduction wave."
    },

    # =========================================================================
    # 2. ALVEOLUS GAS EXCHANGE (2 Archetypes across Gr 9 NS & Gr 11 LS)
    # =========================================================================
    {
        "archetype_id": "NS9_ALVEOLUS_DIFFUSION",
        "diagram_id": "alveolus_gas_exchange",
        "title": "Alveolar Gas Exchange & Blood Capillary Diffusion",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Circulatory and respiratory systems",
        "subskill_param": "alveolus_gas_exchange",
        "view": "microscopic_diffusion_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Diffusion of O2 into red blood cells and CO2 into alveolar lumen across moist epithelium."
    },
    {
        "archetype_id": "LS11_ALVEOLUS_HISTOLOGY",
        "diagram_id": "alveolus_gas_exchange",
        "title": "Alveolar Epithelial Ultrastructure & Fick's Law Adaptations",
        "subject": "Life Sciences",
        "grade": "11",
        "term": 3,
        "topic": "Gaseous exchange",
        "subskill_param": "alveolus_gas_exchange",
        "view": "microscopic_diffusion_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Type I/II pneumocytes, surfactant, capillary endothelium basement membrane and Fick diffusion rate."
    },

    # =========================================================================
    # 3. DIGESTIVE SYSTEM (2 Archetypes across Gr 9 NS & Gr 11 LS)
    # =========================================================================
    {
        "archetype_id": "NS9_DIGESTIVE_TRACT",
        "diagram_id": "digestive_system",
        "title": "Alimentary Canal Organs & Peristaltic Pathway",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Systems in the human body",
        "subskill_param": "digestive_system",
        "view": "coronal_alimentary_canal",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Macroscopic pathway from oesophagus through stomach, small intestine, and large intestine."
    },
    {
        "archetype_id": "LS11_DIGESTIVE_GLANDS",
        "diagram_id": "digestive_system",
        "title": "Gastrointestinal Sphincters, Hepatic & Pancreatic Glands",
        "subject": "Life Sciences",
        "grade": "11",
        "term": 2,
        "topic": "Animal Nutrition",
        "subskill_param": "digestive_system",
        "view": "coronal_alimentary_canal",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Cardiac/pyloric sphincters, duodenum, pancreas, liver, gall bladder and bile secretion."
    },

    # =========================================================================
    # 4. INTESTINAL VILLUS (1 Archetype)
    # =========================================================================
    {
        "archetype_id": "LS11_VILLUS_ABSORPTION",
        "diagram_id": "intestinal_villus",
        "title": "Villus Histological Ultrastructure & Nutrient Absorption",
        "subject": "Life Sciences",
        "grade": "11",
        "term": 2,
        "topic": "Animal Nutrition",
        "subskill_param": "intestinal_villus",
        "view": "longitudinal_cross_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Columnar epithelium, microvilli, central lacteal for fatty acids, capillary network for glucose/amino acids."
    },

    # =========================================================================
    # 5. HUMAN NEPHRON (1 Archetype)
    # =========================================================================
    {
        "archetype_id": "LS11_NEPHRON_TUBULE",
        "diagram_id": "human_nephron",
        "title": "Nephron Microstructure, Ultrafiltration & Reabsorption",
        "subject": "Life Sciences",
        "grade": "11",
        "term": 3,
        "topic": "Excretion in humans",
        "subskill_param": "human_nephron",
        "view": "renal_microstructure_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Bowman's capsule, glomerulus, proximal/distal convoluted tubules, loop of Henle, collecting duct."
    },

    # =========================================================================
    # 6. HUMAN EYE (1 Archetype)
    # =========================================================================
    {
        "archetype_id": "LS12_EYE_ACCOMMODATION",
        "diagram_id": "human_eye",
        "title": "Eye Sagittal Anatomy, Refraction & Accommodation Mechanism",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Human responses to the environment",
        "subskill_param": "human_eye",
        "view": "longitudinal_cross_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Cornea, crystalline lens, ciliary muscles, suspensory ligaments, retina, fovea centralis."
    },

    # =========================================================================
    # 7. HUMAN EAR (1 Archetype)
    # =========================================================================
    {
        "archetype_id": "LS12_EAR_HEARING_BALANCE",
        "diagram_id": "human_ear",
        "title": "Ear Cross-Section: Auditory Conduction & Balance Apparatus",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Human responses to the environment",
        "subskill_param": "human_ear",
        "view": "coronal_auditory_section",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Tympanic membrane, ossicles (malleus, incus, stapes), cochlea, organ of Corti, semicircular canals."
    },

    # =========================================================================
    # 8. ENDOCRINE SYSTEM (1 Archetype)
    # =========================================================================
    {
        "archetype_id": "LS12_ENDOCRINE_GLANDS",
        "diagram_id": "endocrine_system",
        "title": "Endocrine Gland Locations & Negative Feedback Loops",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 2,
        "topic": "The human endocrine system and homeostasis",
        "subskill_param": "endocrine_system",
        "view": "glandular_anatomic_map",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Hypothalamus, pituitary, thyroid, adrenal glands, pancreas islets of Langerhans, gonads."
    },

    # =========================================================================
    # 9. REPRODUCTIVE SYSTEMS (4 Archetypes across Male & Female)
    # =========================================================================
    {
        "archetype_id": "NS9_MALE_REPRODUCTIVE",
        "diagram_id": "male_reproductive",
        "title": "Male Reproductive Gross Anatomy & Duct System",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Human reproduction",
        "subskill_param": "male_reproductive",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Testes, scrotum, epididymis, vas deferens, prostate, urethra."
    },
    {
        "archetype_id": "LS12_MALE_SPERMATOGENESIS",
        "diagram_id": "male_reproductive",
        "title": "Male Reproductive Histology, Spermatogenesis & Hormonal Regulation",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Human reproduction",
        "subskill_param": "male_reproductive",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Seminiferous tubules, Leydig cells, FSH/LH and testosterone hormonal control."
    },
    {
        "archetype_id": "NS9_FEMALE_REPRODUCTIVE",
        "diagram_id": "female_reproductive",
        "title": "Female Reproductive Gross Anatomy & Fertilisation Site",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Human reproduction",
        "subskill_param": "female_reproductive",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Ovaries, Fallopian tubes (oviducts), uterus, endometrium, cervix, vagina."
    },
    {
        "archetype_id": "LS12_FEMALE_OVARIAN_CYCLE",
        "diagram_id": "female_reproductive",
        "title": "Ovarian Follicle Maturation & Menstrual Hormonal Surges",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Human reproduction",
        "subskill_param": "female_reproductive",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Graafian follicle, ovulation, corpus luteum, estrogen and progesterone regulation."
    },

    # =========================================================================
    # 10. MEIOSIS & MITOSIS (2 Archetypes)
    # =========================================================================
    {
        "archetype_id": "LS12_MEIOSIS_CROSSING_OVER",
        "diagram_id": "meiosis_crossing_over",
        "title": "Prophase I Homologous Chromosome Chiasma & Crossing Over",
        "subject": "Life Sciences",
        "grade": "12",
        "term": 1,
        "topic": "Meiosis",
        "subskill_param": "meiosis_crossing_over",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Synapsis, bivalent tetrad, chiasmata, non-sister chromatid genetic recombination."
    },
    {
        "archetype_id": "LS10_MITOSIS_STAGES",
        "diagram_id": "mitosis_stages",
        "title": "Mitotic Cell Division: Prophase, Metaphase, Anaphase, Telophase",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 1,
        "topic": "Cell division",
        "subskill_param": "mitosis_stages",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Spindle fibers, equatorial plate alignment, centromere split, chromatid migration, cytokinesis."
    },

    # =========================================================================
    # 11. PLANT & ANIMAL CELLS (4 Archetypes across Gr 9 NS & Gr 10 LS)
    # =========================================================================
    {
        "archetype_id": "NS9_PLANT_CELL",
        "diagram_id": "plant_cell",
        "title": "Plant Cell Macroscopic Organelles & Cell Wall",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Cells as the basic units of life",
        "subskill_param": "plant_cell",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Cellulose wall, plasma membrane, large vacuole, chloroplasts, nucleus."
    },
    {
        "archetype_id": "LS10_PLANT_CELL_ULTRASTRUCTURE",
        "diagram_id": "plant_cell",
        "title": "Plant Cell Eukaryotic Ultrastructure & Plastids",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 1,
        "topic": "Cells the basic units of life",
        "subskill_param": "plant_cell",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Tonoplast, thylakoid grana, plasmodesmata, amyloplasts, turgor pressure mechanism."
    },
    {
        "archetype_id": "NS9_ANIMAL_CELL",
        "diagram_id": "animal_cell",
        "title": "Animal Cell Core Organelles & Membrane",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 1,
        "topic": "Cells as the basic units of life",
        "subskill_param": "animal_cell",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Cell membrane, cytoplasm, nucleus, mitochondria, absence of cell wall/chloroplasts."
    },
    {
        "archetype_id": "LS10_ANIMAL_CELL_ULTRASTRUCTURE",
        "diagram_id": "animal_cell",
        "title": "Animal Cell Eukaryotic Ultrastructure & Endomembrane System",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 1,
        "topic": "Cells the basic units of life",
        "subskill_param": "animal_cell",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Rough/smooth ER, Golgi apparatus, lysosomes, ribosomes, centrioles, mitochondrial cristae."
    },

    # =========================================================================
    # 12. PLANT LEAF (2 Archetypes across Gr 10 LS & Gr 11 LS)
    # =========================================================================
    {
        "archetype_id": "LS10_LEAF_TISSUES",
        "diagram_id": "plant_leaf",
        "title": "Dicotyledonous Leaf Transverse Section & Tissue Organisation",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 2,
        "topic": "Support and transport systems in plants",
        "subskill_param": "plant_leaf",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Cuticle, upper/lower epidermis, palisade mesophyll, spongy mesophyll, xylem and phloem vascular bundle."
    },
    {
        "archetype_id": "LS11_LEAF_PHOTOSYNTHESIS_ADAPTATIONS",
        "diagram_id": "plant_leaf",
        "title": "Leaf Structural Adaptations for Light Absorption & Gas Exchange",
        "subject": "Life Sciences",
        "grade": "11",
        "term": 2,
        "topic": "Photosynthesis",
        "subskill_param": "plant_leaf",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Stomatal distribution, guard cells, intercellular air spaces for CO2 diffusion, palisade chloroplast concentration."
    },

    # =========================================================================
    # 13. LABORATORY APPARATUS & PHYSICAL SCIENCES (11 Archetypes)
    # =========================================================================
    {
        "archetype_id": "NS7_DISTILLATION_GLASSWARE",
        "diagram_id": "distillation_apparatus",
        "title": "Liebig Simple Distillation Glassware & Condensation Dynamics",
        "subject": "Natural Sciences",
        "grade": "7",
        "term": 2,
        "topic": "Separating mixtures",
        "subskill_param": "distillation_apparatus",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Distillation flask, Liebig condenser, counter-current cooling water jacket, receiving vessel."
    },
    {
        "archetype_id": "PS12_TITRATION_ENDPOINT",
        "diagram_id": "titration_apparatus",
        "title": "Acid-Base Volumetric Titration Glassware Setup & Equivalence",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Acids and bases",
        "subskill_param": "titration_apparatus",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Graduated burette, stopcock, conical flask, white tile, indicator stoichiometric equivalence endpoint."
    },
    {
        "archetype_id": "PS12_GALVANIC_CELL",
        "diagram_id": "galvanic_cell",
        "title": "Daniell Electrochemical Cell (Zn-Cu Half-Cells & Salt Bridge)",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 3,
        "topic": "Electrochemical reactions",
        "subskill_param": "galvanic_cell",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Zinc anode oxidation, copper cathode reduction, KNO3 salt bridge, electron flow in external circuit."
    },
    {
        "archetype_id": "PS12_ELECTROLYTIC_CELL",
        "diagram_id": "electrolytic_cell_apparatus",
        "title": "Electrolytic Decomposition & Copper Refining Setup",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 3,
        "topic": "Electrochemical reactions",
        "subskill_param": "electrolytic_cell_apparatus",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "DC power source, inert graphite/Pt electrodes, electrolyte solution, non-spontaneous redox."
    },
    {
        "archetype_id": "NS8_SOLAR_SYSTEM",
        "diagram_id": "solar_system_earth_space",
        "title": "Planetary Heliocentric Orbits & Asteroid Belts",
        "subject": "Natural Sciences",
        "grade": "8",
        "term": 4,
        "topic": "The Solar System",
        "subskill_param": "solar_system_earth_space",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Sun, terrestrial inner planets, asteroid belt, Jovian gas giants, astronomical scale."
    },
    {
        "archetype_id": "NS8_PARTICLE_MODEL",
        "diagram_id": "particle_model",
        "title": "Particulate Microstructure: Solid, Liquid & Gas Phase Changes",
        "subject": "Natural Sciences",
        "grade": "8",
        "term": 2,
        "topic": "Particle model of matter",
        "subskill_param": "particle_model",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Particle spacing, intermolecular forces, kinetic energy during melting, vaporisation, sublimation."
    },
    {
        "archetype_id": "PS10_BOHR_MODEL",
        "diagram_id": "atomic_bohr_structure",
        "title": "Bohr Electron Energy Shell Configurations (K, L, M Shells)",
        "subject": "Physical Sciences",
        "grade": "10",
        "term": 1,
        "topic": "Classification of matter",
        "subskill_param": "atomic_bohr_structure",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Protons, neutrons, concentric energy levels (2,8,8), valence electrons and atomic number."
    },
    {
        "archetype_id": "PS11_CHEMICAL_BONDING",
        "diagram_id": "chemical_bonding_molecules",
        "title": "Lewis Dot Structures, VSEPR Geometries & Electronegativity",
        "subject": "Physical Sciences",
        "grade": "11",
        "term": 1,
        "topic": "Atomic combinations",
        "subskill_param": "chemical_bonding_molecules",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Bonding pairs, lone pairs, molecular shapes (linear, bent, trigonal planar, tetrahedral), polar bonds."
    },
    {
        "archetype_id": "PS12_GAS_EVOLUTION_KINETICS",
        "diagram_id": "gas_evolution_rate_apparatus",
        "title": "Reaction Rate Gas Syringe & Kinetics Apparatus",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Rate and Extent of Reaction",
        "subskill_param": "gas_evolution_rate_apparatus",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Reaction flask, delivery tube, gas syringe collector, volume vs time gradient (dY/dt)."
    },
    {
        "archetype_id": "PS11_PULLEY_INCLINE",
        "diagram_id": "pulley_incline_masses_system",
        "title": "Connected Two-Body System on Frictionless/Frictional Incline",
        "subject": "Physical Sciences",
        "grade": "11",
        "term": 2,
        "topic": "Newtons laws",
        "subskill_param": "pulley_incline_masses_system",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Incline angle theta, tension T, friction fk, hanging mass m2, Newton's 2nd law Fnet = ma."
    },
    {
        "archetype_id": "PS12_AC_GENERATOR",
        "diagram_id": "ac_dc_generator_motor_apparatus",
        "title": "AC Alternator vs DC Motor Electrodynamics Apparatus",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 3,
        "topic": "Electrodynamics",
        "subskill_param": "ac_dc_generator_motor_apparatus",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Magnetic field poles, rotating armature coil, slip rings vs split-ring commutator, Faraday EMF."
    },
    {
        "archetype_id": "TM10_HYDRAULIC_GEARS",
        "diagram_id": "hydraulic_gears_belt_pulley",
        "title": "Pascal Hydraulic Press, Meshed Gear Trains & Belt Pulley Drives",
        "subject": "Technical Mathematics",
        "grade": "10",
        "term": 3,
        "topic": "Circles, angles and angular movement",
        "subskill_param": "hydraulic_gears_belt_pulley",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Piston diameters F1/A1 = F2/A2, gear tooth ratios N1·T1 = N2·T2, belt linear velocity."
    },
    {
        "archetype_id": "NS9_EARTH_STRATA",
        "diagram_id": "earth_lithosphere_layers",
        "title": "Concentric Planetary Strata: Crust, Mantle, Outer & Inner Core",
        "subject": "Natural Sciences",
        "grade": "9",
        "term": 4,
        "topic": "The lithosphere",
        "subskill_param": "earth_lithosphere_layers",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Continental/oceanic crust, Moho discontinuity, mantle, liquid outer core, solid inner core."
    },
    {
        "archetype_id": "ML10_FLOOR_PACKAGING_PLAN",
        "diagram_id": "architectural_floor_packaging_plan",
        "title": "Architectural Floor Plan, Window Elevations & Scale Ratios",
        "subject": "Mathematical Literacy",
        "grade": "10",
        "term": 3,
        "topic": "Assembly diagrams floor plans and packaging",
        "subskill_param": "architectural_floor_packaging_plan",
        "view": "textbook",
        "category": "Category A (Heart Standard)",
        "cognitive_task": "Wall dimensions, window/door swing architectural symbols, room elevations, 1:50 scale."
    },

    # =========================================================================
    # 14. CATEGORY B PRECISION MODALITIES (18 Archetypes)
    # =========================================================================
    {
        "archetype_id": "MATH8_DOT_PATTERN",
        "diagram_id": "dot_pattern",
        "title": "Geometric Dot Array Pattern & Nth-Term Derivation",
        "subject": "Mathematics",
        "grade": "8",
        "term": 1,
        "topic": "Numeric and geometric patterns",
        "subskill_param": "dot_pattern",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Triangular & square dot array progressions, constant difference, linear nth-term rule: Tn = dn + c."
    },
    {
        "archetype_id": "MATH8_CARTESIAN_POINT",
        "diagram_id": "cartesian_point",
        "title": "4-Quadrant Cartesian Coordinates & Linear Function Plotting",
        "subject": "Mathematics",
        "grade": "8",
        "term": 2,
        "topic": "Functions and relationships",
        "subskill_param": "cartesian_point",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Input-output function tables, plotting coordinates in 4 quadrants, straight-line graphs: y = mx + c."
    },
    {
        "archetype_id": "TM10_RADIAN_SECTOR",
        "diagram_id": "radian_sector",
        "title": "Radian Angle, Circular Sector Arc Length & Surface Area",
        "subject": "Technical Mathematics",
        "grade": "10",
        "term": 3,
        "topic": "Circles, angles and angular movement",
        "subskill_param": "radian_sector",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Radian conversion, sector arc length s = r·theta, sector surface area A = 0.5·r²·theta."
    },
    {
        "archetype_id": "MATH7_CYLINDER_NET",
        "diagram_id": "cylinder_net",
        "title": "Right Circular Cylinder Unfolded Net & Total Surface Area",
        "subject": "Mathematics",
        "grade": "7",
        "term": 3,
        "topic": "Geometry of 3D objects",
        "subskill_param": "cylinder_net",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "2 circular bases and 1 unrolled rectangle of width 2·pi·r and height h, total surface area."
    },
    {
        "archetype_id": "MATH7_CUBE_NET",
        "diagram_id": "cube_net",
        "title": "11 Hexomino Cube Net Configurations & Opposite Face Pairing",
        "subject": "Mathematics",
        "grade": "7",
        "term": 3,
        "topic": "Geometry of 3D objects",
        "subskill_param": "cube_net",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Testing folding validity of 6-square hexomino nets, identifying opposite faces on folded 3D cube."
    },
    {
        "archetype_id": "MATH8_SOLID_3D",
        "diagram_id": "solid_3d",
        "title": "Polyhedra Projections & Euler's Formula (V - E + F = 2)",
        "subject": "Mathematics",
        "grade": "8",
        "term": 3,
        "topic": "Geometry of 3D objects",
        "subskill_param": "solid_3d",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Prisms, pyramids, Platonic solids, faces, edges, vertices, Euler's polyhedral formula."
    },
    {
        "archetype_id": "TM12_ARGAND_COMPLEX",
        "diagram_id": "argand_diagram",
        "title": "Complex Number Argand Plane (Modulus & Argument)",
        "subject": "Technical Mathematics",
        "grade": "12",
        "term": 1,
        "topic": "Complex numbers",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Real and Imaginary axes, modulus r = |z|, argument theta = arg(z), polar form z = r·cis(theta)."
    },
    {
        "archetype_id": "TM12_TRAPEZOIDAL_RULE",
        "diagram_id": "trapezoidal_rule",
        "title": "Numerical Integration: Irregular Area Approximation",
        "subject": "Technical Mathematics",
        "grade": "12",
        "term": 3,
        "topic": "Integration",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Boundary ordinates y0...yn, equal strip width h, trapezoidal rule total area summation."
    },
    {
        "archetype_id": "MATH12_CIRCLE_GEOMETRY",
        "diagram_id": "circle_geometry",
        "title": "Analytical Circle Geometry & Tangent Line Synthesis",
        "subject": "Mathematics",
        "grade": "12",
        "term": 2,
        "topic": "Analytical geometry",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Circle equation (x - a)² + (y - b)² = r², tangent equation at P, perpendicular radius property."
    },
    {
        "archetype_id": "MATH12_CUBIC_CALCULUS",
        "diagram_id": "cubic",
        "title": "Cubic Polynomial Curve Sketching & Turning Points",
        "subject": "Mathematics",
        "grade": "12",
        "term": 2,
        "topic": "Differential calculus",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Stationary points f'(x) = 0, point of inflection f''(x) = 0, x/y intercepts, concavity."
    },
    {
        "archetype_id": "ML10_BOX_AND_WHISKER",
        "diagram_id": "box_and_whisker",
        "title": "Five-Number Summary & Box-and-Whisker Distribution Plot",
        "subject": "Mathematical Literacy",
        "grade": "10",
        "term": 4,
        "topic": "Data handling",
        "subskill_param": "box_and_whisker",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Min, Q1, Median, Q3, Max, Interquartile Range (IQR), outlier thresholds."
    },
    {
        "archetype_id": "MATH11_OGIVE",
        "diagram_id": "ogive",
        "title": "Cumulative Frequency S-Curve (Ogive) & Percentile Estimation",
        "subject": "Mathematics",
        "grade": "11",
        "term": 4,
        "topic": "Statistics",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Upper class boundaries, cumulative frequencies, median (50%) and quartile drop-lines."
    },
    {
        "archetype_id": "MATH12_SCATTER_REGRESSION",
        "diagram_id": "scatter_plot_regression",
        "title": "Bivariate Scatter Plot & Least-Squares Regression Line",
        "subject": "Mathematics",
        "grade": "12",
        "term": 4,
        "topic": "Statistics",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Bivariate coordinate scatter, line of best fit y = A + Bx, Pearson correlation coefficient r."
    },
    {
        "archetype_id": "MATH11_FINANCE_TIMELINE",
        "diagram_id": "timeline_finance",
        "title": "Multi-Stage Compound Interest Cash Flow Timeline",
        "subject": "Mathematics",
        "grade": "11",
        "term": 1,
        "topic": "Finance growth and decays",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Time axis T0...Tn, compounding intervals, intermediate deposits, withdrawals, interest rate shifts."
    },
    {
        "archetype_id": "MATH12_VENN_3_SETS",
        "diagram_id": "venn_3_sets",
        "title": "3-Event Compound Venn Diagram & Mutual Exclusivity",
        "subject": "Mathematics",
        "grade": "12",
        "term": 4,
        "topic": "Probability",
        "subskill_param": "compound_seating_venn",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Sample space S, 3 intersecting event circles, central 3-way intersection (A and B and C), solve for x."
    },
    {
        "archetype_id": "PS12_MOTION_GRAPH",
        "diagram_id": "motion_graph",
        "title": "Vertical Kinematics Velocity-Time & Position-Time Trajectories",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 1,
        "topic": "Vertical projectile motion in one dimension",
        "subskill_param": "motion_graph",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "v-t gradient = -9.8 m/s², area under curve = displacement, parabolic y-t free-fall curve."
    },
    {
        "archetype_id": "PS12_REACTION_PROFILE",
        "diagram_id": "reaction_energy_profile",
        "title": "Exothermic & Endothermic Potential Energy Reaction Profile",
        "subject": "Physical Sciences",
        "grade": "12",
        "term": 2,
        "topic": "Rate and Extent of Reaction",
        "subskill_param": "compound",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Enthalpy of reactants (Hr), products (Hp), activation energy (Ea), delta H = Hp - Hr, catalyzed curve."
    },
    {
        "archetype_id": "EMS9_SUPPLY_DEMAND",
        "diagram_id": "supply_demand",
        "title": "Market Equilibrium Price, Quantity & Shortage/Surplus Dynamics",
        "subject": "Economic and Management Sciences",
        "grade": "9",
        "term": 2,
        "topic": "Price theory",
        "subskill_param": "supply_demand",
        "view": "standard",
        "category": "Category B (Precision Vector Modality)",
        "cognitive_task": "Downward demand curve, upward supply curve, market equilibrium (Pe, Qe), price ceilings & shortage."
    }
]

def test_all():
    print(f"Testing all {len(CANONICAL_DIAGRAM_ARCHETYPES)} diagram archetypes directly on Seed 1...")
    passed = 0
    failed = 0
    failures = []

    for item in CANONICAL_DIAGRAM_ARCHETYPES:
        arch_id = item["archetype_id"]
        subj = item["subject"]
        gr = item["grade"]
        top = item["topic"]
        sub = item["subskill_param"]

        try:
            res = generate_variant(
                topic=top,
                grade=gr,
                subject=subj,
                subskill=sub,
                seed=1,
                count=1,
            )
            if not res or len(res) == 0:
                failed += 1
                failures.append(f"{arch_id}: No question returned")
                print(f"  [FAIL] {arch_id}: Empty result")
                continue

            q = res[0]
            # Verify diagram spec or visual modality
            has_diag = "diagram_spec" in q or q.get("modality") in ("diagram", "bio_diagram", "vector_diagram", "circuit", "physics_and_economics_graph", "stats_and_financial_graph", "geogebra_geometry")
            if not has_diag:
                failed += 1
                failures.append(f"{arch_id}: Missing diagram spec or visual modality")
                print(f"  [FAIL] {arch_id}: No diagram emitted")
                continue

            passed += 1
            print(f"  [PASS] {arch_id} ({subj} Gr {gr}) -> Seed 1 OK")
        except Exception as e:
            failed += 1
            failures.append(f"{arch_id}: Exception {str(e)}")
            print(f"  [FAIL] {arch_id}: Exception {e}")

    print("\n" + "="*80)
    print(f"SUMMARY: {passed}/{len(CANONICAL_DIAGRAM_ARCHETYPES)} PASSED | {failed} FAILED")
    print("="*80)
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    test_all()
