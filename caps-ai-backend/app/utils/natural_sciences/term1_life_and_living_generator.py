"""Natural Sciences Senior Phase (Grades 7–9) — Term 1: Life and Living Generator.
Deterministic 6-pillar CAPS question generator covering:
- Grade 7: The Biosphere, Biodiversity, Angiosperm Reproduction (flower anatomy & pollination), Inherited Variation.
- Grade 8: Photosynthesis (chloroplasts & starch test), Cellular Respiration, Ecosystem Ecology (trophic webs & energy pyramids), Microorganisms.
- Grade 9: Cell Cytology (organelles, plant vs animal cells), Human Organ Systems (Digestive, Circulatory, Respiratory, Excretory).
Supports compound exam questions and atomic elementary sub-drills.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    fmt_sa,
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_life_and_living"
LO = "ns_senior_life_and_living"

# ============================================================================
# ARCHETYPE 1: PHOTOSYNTHESIS & CELLULAR RESPIRATION (Grades 8–9)
# ============================================================================

PHOTOSYNTHESIS_SCENARIOS = [
    {
        "plant": "Variegated geranium (Pelargonium)",
        "leaf_desc": "green in the centre with white (non-chlorophyll) margins",
        "treatment": "de-starched in the dark for 48 hours, then exposed to bright sunlight for 6 hours",
        "starch_result": "The green central region turned blue-black with iodine; the white margin remained yellow-brown.",
        "conclusion": "Chlorophyll is essential for photosynthesis and starch production.",
        "reactant_focus": "Carbon dioxide and water in the presence of radiant energy absorbed by chlorophyll",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
    {
        "plant": "Canadian pondweed (Elodea)",
        "leaf_desc": "submerged freshwater aquatic weed",
        "treatment": "placed under a glass funnel with test tube inverted over the stem in sodium bicarbonate solution (carbon dioxide source)",
        "starch_result": "Gas bubbles were released at a rate proportional to light intensity.",
        "conclusion": "Light intensity directly affects the rate of photosynthesis.",
        "reactant_focus": "Dissolved carbon dioxide and water",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
    {
        "plant": "Bean seedling (Phaseolus vulgaris)",
        "leaf_desc": "broad green dicotyledonous leaf",
        "treatment": "one leaf enclosed in a flask containing potassium hydroxide (KOH / soda lime pellets to absorb CO2), illuminated for 8 hours",
        "starch_result": "The enclosed leaf remained yellow-brown with iodine solution; the control leaf turned blue-black.",
        "conclusion": "Carbon dioxide is an indispensable reactant for photosynthesis.",
        "reactant_focus": "Carbon dioxide gas absorbed through open stomata",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
    {
        "plant": "Water thyme (Hydrilla verticillata)",
        "leaf_desc": "translucent whorled submersed aquatic leaves",
        "treatment": "incubated in thermostatic water baths at 10°C, 25°C, 40°C, and 60°C under uniform illuminance",
        "starch_result": "Bubble release accelerated up to 35°C but ceased completely above 50°C.",
        "conclusion": "Temperature acts as an environmental limiting factor through thermal denaturation of photosynthetic enzymes.",
        "reactant_focus": "Thermal kinetic energy and stomatal gas conductance",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
    {
        "plant": "Potted hibiscus (Hibiscus rosa-sinensis)",
        "leaf_desc": "broad glossy green perennial leaf",
        "treatment": "covered with an opaque black cardboard stencil mask forming a cross on both sides, then exposed to direct sunlight for 7 hours",
        "starch_result": "Only the uncovered sun-exposed cruciform zone turned blue-black with iodine; masked sections remained pale brown.",
        "conclusion": "Radiant solar energy is an absolute prerequisite for starch synthesis.",
        "reactant_focus": "Photonic excitation of thylakoid reaction centres",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
    {
        "plant": "Coleus blumei (Painted nettle)",
        "leaf_desc": "ornamental leaf with green chlorophyll perimeter, purple anthocyanin center, and white pigment-free patches",
        "treatment": "destarched for 36 hours, illuminated under high-intensity PAR lamps for 5 hours, followed by hot ethanol extraction",
        "starch_result": "Only areas containing green chlorophyll stained dark blue-black with iodine; anthocyanin and albino zones gave a negative result.",
        "conclusion": "Only chlorophyll-containing chloroplasts possess the metabolic machinery for light-dependent starch synthesis.",
        "reactant_focus": "Photosystem II and I pigments in grana stacks",
        "gas_produced": "Oxygen (O2)",
        "test_for_gas": "Relights a glowing wooden splint.",
    },
]


def _gen_photosynthesis_question(r: random.Random, grade: int = 8, mode: str = "compound") -> Dict[str, Any]:
    scen_idx = int(r.randint(0, 10000)) % len(PHOTOSYNTHESIS_SCENARIOS)
    scen = PHOTOSYNTHESIS_SCENARIOS[scen_idx]
    
    if mode == "elementary_equation" or mode == "elementary":
        prompt = (
            f"Write the balanced symbolic or word equation for photosynthesis in green plants, "
            f"identifying the energy transformation that takes place."
        )
        prompt_latex = (
            r"\text{Write the complete word or chemical equation for photosynthesis,}" "\n"
            r"\text{specifying the energy transformation from reactant to product.}"
        )
        answer_latex = (
            r"\text{Carbon dioxide} + \text{Water} \xrightarrow[\text{chlorophyll}]{\text{radiant energy}} "
            r"\text{Glucose} + \text{Oxygen}" "\n"
            r"\quad [6\text{CO}_2 + 6\text{H}_2\text{O} \to \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2]"
        )
        sample = (
            "Word equation: Carbon dioxide + Water (in the presence of sunlight and chlorophyll) -> Glucose + Oxygen. "
            "Energy conversion: Radiant (light) energy is transformed into chemical potential energy stored in glucose."
        )
        schema = {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Correct reactants (Carbon dioxide + Water)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct products (Glucose + Oxygen)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Reaction conditions stated (Sunlight / Chlorophyll)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Energy transformation (Radiant -> Chemical potential energy)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Consider what green plants absorb from the air and soil, and what organic sugar and gas they produce.",
            "concept": "Photosynthesis traps radiant solar energy in chemical bonds of carbohydrate molecules.",
            "breakdown": "Reactants: CO2 + H2O. Products: C6H12O6 + O2. Catalyst/Conditions: Chlorophyll & light energy.",
        }
        return make_science_question(
            prefix="ns_photo_elem",
            topic=TOPIC,
            subskill="photosynthesis_equation_energy_conversion",
            learning_objective_id=f"{LO}_photosynthesis_equation",
            prompt=prompt,
            prompt_latex=prompt_latex,
            answer_latex=answer_latex,
            sample_answer=sample,
            marking_schema=schema,
            hints=hints,
            misconception_tags=["confusing_photosynthesis_with_respiration", "omitting_energy_conversion"],
            keywords=["photosynthesis", "glucose", "chlorophyll", "radiant energy", "oxygen"],
            term=1,
            caps_weight_percent=25,
            suggested_duration_mins=5,
            mode=mode,
            difficulty="medium",
            marks=4,
        )

    # Compound investigation question
    prompt = (
        f"A group of Grade {grade} Natural Sciences learners investigated factors affecting plant nutrition using a {scen['plant']}. "
        f"The plant had leaves described as {scen['leaf_desc']}. As part of the experiment, it was {scen['treatment']}. "
        f"After boiling the leaf in alcohol to extract the pigment and adding iodine solution, the learners recorded the following observation: "
        f"'{scen['starch_result']}'\n\n"
        f"1. Name the pigment responsible for absorbing radiant light in plant leaves.\n"
        f"2. Explain why the leaf was boiled in ethanol (alcohol) during the starch test procedure.\n"
        f"3. State the biological purpose of testing for starch rather than directly for glucose.\n"
        f"4. Formulate the scientific conclusion supported by the learners' observations.\n"
        f"5. Identify the gas produced during this metabolic process and describe the chemical test used to confirm its identity."
    )
    prompt_latex = (
        rf"\textbf{{Investigation: Nutritional Physiology of {scen['plant']}}}" "\n\n"
        rf"\text{{Treatment: {scen['treatment']}.}}" "\n"
        rf"\text{{Observed Starch Result: {scen['starch_result']}}}" "\n\n"
        r"\text{Answer the 5 analytical questions on pigment function, laboratory procedure, and gaseous outputs.}"
    )
    answer_latex = (
        r"\text{1. Chlorophyll (located inside chloroplasts).}" "\n"
        r"\text{2. To decolourise / extract green chlorophyll so colour change with iodine is clearly visible.}" "\n"
        r"\text{3. Glucose is rapidly converted to insoluble starch for compact storage without altering osmotic potential.}" "\n"
        rf"\text{{4. Conclusion: {scen['conclusion']}}}" "\n"
        rf"\text{{5. Gas: {scen['gas_produced']}. Confirmatory test: {scen['test_for_gas']}}}"
    )
    sample = (
        f"1. Chlorophyll.\n"
        f"2. Boiling in ethanol decolourises the leaf by dissolving and removing green chlorophyll, enabling the yellow-brown to blue-black iodine colour change to be observed unambiguously.\n"
        f"3. Excess glucose produced during photosynthesis is immediately condensed into insoluble starch for storage, which does not dissolve into cytoplasm or affect cell osmotic pressure.\n"
        f"4. {scen['conclusion']}\n"
        f"5. Gas: {scen['gas_produced']}. Test: {scen['test_for_gas']}"
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Identify chlorophyll pigment", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explain ethanol boiling (extract chlorophyll/decolourise)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explain why starch is tested (storage form of excess glucose)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Valid empirical conclusion matching the experimental treatment", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Gas identity and splint test", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Think about why iodine turns dark blue-black on certain leaf sections and what ethanol does to green pigments.",
        "concept": "Starch is the storage polysaccharide synthesised from glucose monomers produced during light-dependent reactions.",
        "breakdown": f"Key facts: Pigment = Chlorophyll; Ethanol dissolves pigment; Iodine tests starch; Conclusion: {scen['conclusion']}.",
    }
    return make_science_question(
        prefix="ns_photo_comp",
        topic=TOPIC,
        subskill="photosynthesis_starch_investigation",
        learning_objective_id=f"{LO}_photosynthesis_investigation",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["boiling_in_water_vs_ethanol_confusion", "inaccurate_iodine_colour_interpretation"],
        keywords=["photosynthesis", "starch", "iodine", "chlorophyll", "ethanol", "oxygen"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=8,
        mode=mode,
        difficulty="hard",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 2: CELL CYTOLOGY & ORGANELLES (Grade 9)
# ============================================================================

ORGANELLES = [
    {
        "name": "Mitochondrion",
        "structure": "Double-membraned organelle with folded inner cristae",
        "function": "Site of cellular respiration; converts glucose into usable ATP energy for cellular work",
        "found_in": "Both plant and animal cells",
        "adaptation": "Folded inner cristae dramatically increase surface area for enzyme activity",
    },
    {
        "name": "Chloroplast",
        "structure": "Double-membraned organelle containing green chlorophyll pigments arranged in thylakoid grana",
        "function": "Site of photosynthesis; absorbs radiant solar energy to synthesise organic sugars",
        "found_in": "Plant cells only (green photosynthetic tissues)",
        "adaptation": "Stacked grana provide an extensive surface area for capturing light photons",
    },
    {
        "name": "Cell Wall",
        "structure": "Rigid outer layer composed of tough, fibrous cellulose",
        "function": "Provides structural support, mechanical protection, and prevents the cell from bursting under turgor pressure",
        "found_in": "Plant cells only",
        "adaptation": "Freely permeable cellulose fibres maintain rigid plant posture without internal skeleton",
    },
    {
        "name": "Cell Membrane (Plasma Membrane)",
        "structure": "Thin, flexible phospholipid bilayer with embedded protein channels",
        "function": "Selectively permeable barrier controlling the movement of substances into and out of the cytoplasm",
        "found_in": "Both plant and animal cells",
        "adaptation": "Selectively permeable nature maintains stable internal cellular homeostasis",
    },
    {
        "name": "Nucleus",
        "structure": "Enclosed by a double nuclear membrane containing nuclear pores and chromatin network (DNA)",
        "function": "Controls all metabolic activities of the cell and stores hereditary genetic information",
        "found_in": "Both plant and animal cells (eukaryotes)",
        "adaptation": "Nuclear pores allow messenger RNA (mRNA) molecules to pass into the cytoplasm",
    },
    {
        "name": "Large Central Vacuole",
        "structure": "Large fluid-filled membrane-bound sac surrounded by the tonoplast and filled with cell sap",
        "function": "Stores water, sugars, and mineral salts; exerts turgor pressure outward to keep plant cells firm and upright",
        "found_in": "Mature plant cells (animal cells have small temporary vacuoles)",
        "adaptation": "High osmotic concentration draws water in, maintaining essential turgidity",
    },
]


def _gen_cell_cytology_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    selected = r.sample(ORGANELLES, 3)
    o1, o2, o3 = selected[0], selected[1], selected[2]
    
    if mode == "elementary_plant_vs_animal" or mode == "elementary":
        prompt = (
            "Tabulate THREE distinct structural differences between a typical plant cell and a typical animal cell."
        )
        prompt_latex = (
            r"\text{Construct a comparison table stating THREE distinct structural differences}" "\n"
            r"\text{between a typical plant cell and an animal cell.}"
        )
        answer_latex = (
            r"\begin{array}{|l|l|l|} \hline"
            r"\textbf{Feature} & \textbf{Plant Cell} & \textbf{Animal Cell} \\ \hline "
            r"\text{Outer boundary} & \text{Rigid cellulose cell wall present} & \text{Only flexible cell membrane (no cell wall)} \\ "
            r"\text{Plastids} & \text{Chloroplasts present in green cells} & \text{No chloroplasts} \\ "
            r"\text{Vacuole} & \text{Single large permanent central vacuole} & \text{Small, temporary vacuoles or absent} \\ "
            r"\text{Shape} & \text{Fixed, regular, rectangular shape} & \text{Irregular, flexible shape} \\ \hline"
            r"\end{array}"
        )
        sample = (
            "Comparison Table:\n"
            "1. Cell wall: Present (made of cellulose) in plant cells; Absent in animal cells.\n"
            "2. Chloroplasts: Present (contain chlorophyll for photosynthesis) in plant cells; Absent in animal cells.\n"
            "3. Vacuole: Large, permanent central vacuole filled with cell sap in plant cells; Small, temporary vacuoles in animal cells."
        )
        schema = {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Cell wall difference correctly stated", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Chloroplasts difference correctly stated", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Vacuole size/permanence difference correctly stated", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "not_in_table_format", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "nudge": "Consider the rigid outer structures and photosynthetic organelles unique to plant leaves.",
            "concept": "Plant cells possess cell walls, chloroplasts, and large permanent central vacuoles which animal cells lack.",
            "breakdown": "3 main differences: 1) Cell wall (cellulose); 2) Chloroplasts; 3) Large central permanent vacuole.",
        }
        return make_science_question(
            prefix="ns_cell_elem",
            topic=TOPIC,
            subskill="plant_vs_animal_cells_comparison",
            learning_objective_id=f"{LO}_cell_cytology_comparison",
            prompt=prompt,
            prompt_latex=prompt_latex,
            answer_latex=answer_latex,
            sample_answer=sample,
            marking_schema=schema,
            hints=hints,
            misconception_tags=["assuming_plant_cells_lack_mitochondria", "confusing_cell_wall_with_cell_membrane"],
            keywords=["cell wall", "chloroplast", "vacuole", "mitochondria", "cellulose"],
            term=1,
            caps_weight_percent=25,
            suggested_duration_mins=6,
            mode=mode,
            difficulty="medium",
            marks=6,
        )

    # Dynamic specimens and microscopy calculations
    specimens = [
        {"name": "onion epidermal tissue", "type": "plant", "mag": 400, "img_mm": 48},
        {"name": "human buccal (cheek) epithelial cells", "type": "animal", "mag": 500, "img_mm": 35},
        {"name": "Elodea freshwater leaf cells", "type": "plant", "mag": 200, "img_mm": 40},
        {"name": "Amoeba proteus protozoan specimen", "type": "protist", "mag": 100, "img_mm": 25},
        {"name": "guard cells surrounding a leaf stoma", "type": "plant", "mag": 600, "img_mm": 36},
        {"name": "Spirogyra filamentous green algae", "type": "protist", "mag": 300, "img_mm": 45},
        {"name": "human blood smear showing erythrocytes", "type": "animal", "mag": 1000, "img_mm": 50},
        {"name": "moss leaflet (Funaria) cells", "type": "plant", "mag": 400, "img_mm": 32},
    ]
    specimen = r.choice(specimens)
    img_mm = specimen["img_mm"]
    mag = specimen["mag"]

    cell_inquiries = [
        f"A Grade 9 learner viewed a slide of {specimen['name']} under a compound light microscope.",
        f"During a practical laboratory session, life science students examined stained cells of {specimen['name']} at high power.",
        f"Microscopic analysis of {specimen['name']} reveals specialized cytological adaptations under illumination.",
        f"In a cell cytology investigation, a biological specimen of {specimen['name']} was mounted and observed under magnification.",
    ]
    inquiry_lead = r.choice(cell_inquiries)

    # Compound organelle function and structure
    prompt = (
        f"{inquiry_lead}\n\n"
        f"1. Identify the organelle described as '{o1['structure']}'. State its primary cellular function.\n"
        f"2. Organelle '{o2['name']}' is found in {o2['found_in']}. Explain one structural adaptation of this organelle that maximizes its efficiency.\n"
        f"3. What metabolic crisis would a cell experience if all of its {o3['name']}s were enzymatically deactivated?\n"
        f"4. Calculate the actual width of the {specimen['name']} in micrometres (µm) if its magnified image measures {img_mm} mm under a magnification of {mag}x."
    )
    prompt_latex = (
        rf"\textbf{{Cell Cytology Analysis: {specimen['name'].title()}}}" "\n\n"
        rf"\text{{1. Organelle 1 Description: {o1['structure']}. Name and function?}}" "\n"
        rf"\text{{2. Organelle 2 ({o2['name']}): Structural adaptation for efficiency?}}" "\n"
        rf"\text{{3. Consequence of deactivated {o3['name']}?}}" "\n"
        rf"\text{{4. Magnification Calculation: }}" "\n"
        rf"\text{{Actual size }} = \frac{{\text{{Image size}}}}{{\text{{Magnification}}}} \quad [\text{{Image}} = {img_mm}\text{{ mm}}, \text{{ Mag}} = {mag}\times]"
    )
    actual_um = (img_mm * 1000) / mag
    actual_str = fmt_sa(actual_um, 2)
    answer_latex = (
        rf"\text{{1. Organelle: {o1['name']}. Function: {o1['function']}.}}" "\n"
        rf"\text{{2. Adaptation: {o2['adaptation']}.}}" "\n"
        rf"\text{{3. Impact: Loss of {o3['name']} impairs: {o3['function']}.}}" "\n"
        rf"\text{{4. Actual size}} = \frac{{{img_mm}\text{{ mm}} \times 1\,000}}{{{mag}}} = \frac{{{img_mm * 1000}}}{{{mag}}} = {actual_str}\text{{ }}\mu\text{{m}}"
    )
    sample = (
        f"1. Name: {o1['name']}. Function: {o1['function']}.\n"
        f"2. Adaptation: {o2['adaptation']}.\n"
        f"3. Deactivating {o3['name']} stops its vital role: {o3['function']}.\n"
        f"4. Formula: Actual size = Image size / Magnification.\n"
        f"   Convert {img_mm} mm to micrometres: {img_mm} mm x 1000 = {img_mm * 1000} µm.\n"
        f"   Actual size = {img_mm * 1000} µm / {mag} = {actual_str} µm."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": f"Correctly identify {o1['name']} and function", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct structural adaptation for {o2['name']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate biological deduction for deactivated {o3['name']}", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Correct conversion ({img_mm} mm to {img_mm * 1000} µm) and division by {mag}x", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Remember that 1 millimetre contains 1 000 micrometres (µm).",
        "concept": "Magnification formula: Actual size (A) = Image size (I) / Magnification (M). Ensure units match before dividing.",
        "breakdown": f"{img_mm} mm = {img_mm * 1000} µm. {img_mm * 1000} / {mag} = {actual_str} µm. Organelle 1 is {o1['name']}.",
    }
    return make_science_question(
        prefix="ns_cell_comp",
        topic=TOPIC,
        subskill="organelle_identification_and_magnification_calculation",
        learning_objective_id=f"{LO}_organelles_and_microscopy",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["mm_to_um_unit_conversion_error", "confusing_nucleus_with_nucleolus"],
        keywords=["mitochondria", "chloroplast", "magnification", "micrometre", "cytoplasm"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=8,
        mode=mode,
        difficulty="hard",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 3: HUMAN BODY SYSTEMS (Grade 9)
# ============================================================================

SYSTEMS_DATA = [
    {
        "system": "Digestive System",
        "organs": "Mouth, Oesophagus, Stomach, Small intestine (Duodenum & Ileum), Large intestine (Colon), Rectum",
        "main_function": "Breakdown of insoluble food into soluble nutrients and absorption into bloodstream",
        "processes": "Ingestion -> Digestion (mechanical & chemical) -> Absorption -> Assimilation -> Egestion",
        "health_issue": "Gastric ulcers / constipation / malnourishment",
    },
    {
        "system": "Circulatory System",
        "organs": "Heart, Arteries, Veins, Capillaries, Blood",
        "main_function": "Transport of oxygen, nutrients, hormones, and metabolic wastes throughout the body",
        "processes": "Double circulation: Pulmonary circuit (lungs) and Systemic circuit (body organs)",
        "health_issue": "Hypertension (high blood pressure) / coronary heart disease / stroke",
    },
    {
        "system": "Respiratory System",
        "organs": "Nasal cavity, Pharynx, Trachea, Bronchi, Bronchioles, Alveoli, Lungs, Diaphragm",
        "main_function": "Gaseous exchange: uptake of oxygen and expulsion of carbon dioxide",
        "processes": "Inhalation (diaphragm contracts down, volume increases) and Exhalation (diaphragm relaxes up)",
        "health_issue": "Asthma / bronchitis / lung cancer",
    },
    {
        "system": "Excretory System",
        "organs": "Kidneys, Ureters, Bladder, Urethra",
        "main_function": "Filtration of metabolic waste products (urea, excess salts, water) from blood to form urine",
        "processes": "Renal filtration -> Selective reabsorption -> Secretion -> Excretion",
        "health_issue": "Kidney stones / renal failure",
    },
]


def _gen_human_systems_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    sys_item = r.choice(SYSTEMS_DATA)
    intros = [
        "In human physiology, coordinated organ systems maintain internal homeostasis under changing metabolic demands.",
        "The human body functions as an integrated biological machine comprising specialized, interdependent organ systems.",
        "Clinical life sciences examine how vital human organ systems work collaboratively to sustain internal balance.",
        "To maintain life, human physiology depends on continuous biochemical coordination across major organ systems.",
    ]
    intro = r.choice(intros)
    
    prompt = (
        f"{intro}\n\n"
        f"1. State the primary physiological function of the human **{sys_item['system']}**.\n"
        f"2. Name TWO major organs that belong to this system and describe their specific contributions.\n"
        f"3. Distinguish between the following biological concepts associated with this system:\n"
        f"   - If Digestive: Distinguish between **absorption** and **assimilation**.\n"
        f"   - If Circulatory: Distinguish between the structure and blood pressure in **arteries** versus **veins**.\n"
        f"   - If Respiratory: Distinguish between **breathing** and **cellular respiration**.\n"
        f"   - If Excretory: Distinguish between **excretion** and **egestion**.\n"
        f"4. Suggest ONE healthy lifestyle choice that reduces the risk of {sys_item['health_issue']}."
    )
    prompt_latex = (
        rf"\textbf{{Human Physiology: {sys_item['system']}}}" "\n\n"
        rf"\text{{1. Primary physiological function of the {sys_item['system']}}}" "\n"
        rf"\text{{2. Two major organs and their structural roles}}" "\n"
        rf"\text{{3. Conceptual distinctions: Critical pathway analysis}}" "\n"
        rf"\text{{4. Lifestyle intervention to mitigate {sys_item['health_issue']}}}"
    )
    
    if sys_item["system"] == "Digestive System":
        dist_ans = "Absorption is the uptake of digested soluble nutrients through villi into blood/lymph; Assimilation is the incorporation of those absorbed nutrients into cellular protoplasm for growth and repair."
    elif sys_item["system"] == "Circulatory System":
        dist_ans = "Arteries carry blood away from the heart under high pressure with thick muscular elastic walls; Veins carry blood back to the heart under low pressure with thinner walls and one-way valves to prevent backflow."
    elif sys_item["system"] == "Respiratory System":
        dist_ans = "Breathing (ventilation) is the mechanical inhalation and exhalation of air into and out of the lungs; Cellular respiration is the chemical oxidation of glucose inside mitochondria to release ATP energy."
    else:
        dist_ans = "Excretion is the removal of metabolic waste products created by cellular chemical reactions (e.g., urea, CO2); Egestion is the expulsion of undigested, unabsorbed food residue (faeces) from the digestive tract."

    answer_latex = (
        rf"\text{{1. Function: {sys_item['main_function']}.}}" "\n"
        rf"\text{{2. Organs: From [{sys_item['organs']}].}}" "\n"
        rf"\text{{3. Distinction: {dist_ans}}}" "\n"
        rf"\text{{4. Lifestyle: Balanced diet, regular cardiovascular exercise, adequate hydration, avoidance of smoking.}}"
    )
    sample = (
        f"1. Primary function: {sys_item['main_function']}.\n"
        f"2. Two organs: e.g. from {sys_item['organs']}.\n"
        f"3. Distinction: {dist_ans}\n"
        f"4. Lifestyle choice: Maintain regular exercise, drink sufficient water, follow a balanced diet, and avoid tobacco/alcohol abuse."
    )
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate primary function stated", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Two valid organs with accurate functional roles", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Clear and scientifically rigorous conceptual distinction", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Feasible preventative lifestyle recommendation", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Recall the exact difference between metabolic waste and undigested food, or mechanical ventilation vs chemical reaction.",
        "concept": "Organ systems collaborate: digestive absorbs nutrients, respiratory absorbs oxygen, circulatory transports both, excretory cleans wastes.",
        "breakdown": f"System: {sys_item['system']}. Focus on: {dist_ans[:80]}...",
    }
    return make_science_question(
        prefix="ns_human_sys",
        topic=TOPIC,
        subskill="human_organ_systems_and_physiology",
        learning_objective_id=f"{LO}_human_organ_systems",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["confusing_breathing_with_cellular_respiration", "confusing_excretion_with_egestion"],
        keywords=["digestion", "respiration", "circulation", "excretion", "homeostasis"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=6,
    )


# ============================================================================
# ARCHETYPE 4: THE BIOSPHERE & BIODIVERSITY (Grade 7)
# ============================================================================

SA_BIOMES = [
    {
        "name": "Fynbos Biome",
        "region": "Western Cape winter-rainfall belt",
        "climate": "Cool, wet winters and hot, dry summers",
        "vegetation": "Fine-leaved sclerophyllous shrubs (Proteas, Ericas, Restios)",
        "endemic_species": "King Protea (Protea cynaroides)",
        "adaptation": "Fire-adapted seeds (serotiny) and underground lignotubers to regenerate after bushfires",
        "biotic_interaction": "Cape sugarbirds pollinating tubular protea inflorescences",
    },
    {
        "name": "Succulent Karoo Biome",
        "region": "Arid west coast of the Northern and Western Cape",
        "climate": "Extremely low, reliable winter rainfall with arid, baking summer temperatures",
        "vegetation": "Dwarf succulent shrubs with fleshy water-storing leaves and stems",
        "endemic_species": "Quiver Tree (Aloidendron dichotomum)",
        "adaptation": "Thick fleshy leaves with waxy cuticles and CAM photosynthesis to conserve moisture",
        "biotic_interaction": "Specialised pollinating bees visiting seasonal carpet wildflowers",
    },
    {
        "name": "Savanna Biome (Bushveld)",
        "region": "Subtropical northern provinces (Limpopo, Mpumalanga, northern KZN)",
        "climate": "Warm, wet summers with lightning thunderstorms and dry, frost-free winters",
        "vegetation": "Continuous grass layer beneath an open canopy of drought-resistant acacia and marula trees",
        "endemic_species": "Marula tree (Sclerocarya birrea)",
        "adaptation": "Deep taproots reaching groundwater and thick fire-resistant cork bark",
        "biotic_interaction": "Browsing herbivores (giraffes, kudu) feeding on thorny acacia leaves",
    },
    {
        "name": "Grassland Biome",
        "region": "High inland plateau (Highveld of Gauteng, Free State, Mpumalanga)",
        "climate": "High summer rainfall with severe winter frosts and dry winter cold",
        "vegetation": "Dense, single-layered herbaceous grass cover with virtually no natural indigenous trees",
        "endemic_species": "Giant bullfrog (Pyxicephalus adspersus)",
        "adaptation": "Vigorous subterranean root networks that survive winter frost and resprout after fire",
        "biotic_interaction": "Grazing herds of blesbok and black wildebeest aerating topsoil",
    },
    {
        "name": "Albany Thicket Biome",
        "region": "Semi-arid river valleys of the Eastern Cape",
        "climate": "Semi-arid with variable precipitation distributed throughout all seasons",
        "vegetation": "Dense, impenetrable tangle of thorny shrubs, woody climbers, and succulent trees",
        "endemic_species": "Spekboom (Portulacaria afra)",
        "adaptation": "Exceptional carbon sequestration capacity and high tissue water storage",
        "biotic_interaction": "Elephants browsing dense thickets and dispersing seeds in nutrient-rich dung",
    },
    {
        "name": "Desert Biome",
        "region": "Hyper-arid Gariep and Richtersveld bioregions of the Northern Cape",
        "climate": "Extremely sparse rainfall (< 70 mm/yr) with extreme diurnal temperature fluctuations",
        "vegetation": "Dwarf stem-succulents, mobile sand dunes, and ephemeral desert annuals",
        "endemic_species": "Welwitschia / Halfmens (Pachypodium namaquanum)",
        "adaptation": "Water-storing swollen stems, spines reflecting intense solar radiation, and deep root systems",
        "biotic_interaction": "Nocturnal desert reptiles and tenebrionid beetles condensing fog moisture",
    },
    {
        "name": "Forest Biome (Afro-temperate)",
        "region": "Coastal platforms and south-facing mountain gorges of Knysna and Tsitsikamma",
        "climate": "High, non-seasonal year-round rainfall with mild temperate coastal humidity",
        "vegetation": "Multi-tiered closed-canopy evergreen trees with epiphytic lichens, mosses, and ferns",
        "endemic_species": "Outeniqua Yellowwood (Afrocarpus falcatus)",
        "adaptation": "Tall straight trunks competing for sunlight in dense canopy with buttress root stabilization",
        "biotic_interaction": "Knysna turacos (louries) feeding on fleshy fruits and dispersing seeds through forest interior",
    },
    {
        "name": "Nama Karoo Biome",
        "region": "Semi-arid central plateau of the Northern, Eastern and Western Cape interior",
        "climate": "Low summer-autumn rainfall with extreme continental summer heat and winter frosts",
        "vegetation": "Deciduous dwarf shrubs interspersed with annual grasses and geophytes",
        "endemic_species": "Karoo bush (Pentzia incana)",
        "adaptation": "Aromatic volatile oils in leaves reducing transpiration and deterring excessive grazing",
        "biotic_interaction": "Springbok herds migrating across plains following erratic summer thunderstorm flushes",
    },
]

BIOSPHERE_PROMPT_HOOKS = [
    "The biosphere represents the global ecological zone where all life exists on Earth.",
    "Planet Earth supports an extraordinary variety of interconnected ecosystems that comprise the biosphere.",
    "Ecological studies of the biosphere examine how living organisms interact with abiotic physical environments.",
    "The biosphere forms a self-regulating global network that sustains biological life across diverse terrestrial biomes.",
    "In South African biodiversity studies, natural biomes illustrate unique abiotic and biotic interactions within the biosphere.",
]


def _gen_biosphere_biodiversity_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    b = r.choice(SA_BIOMES)
    hook = r.choice(BIOSPHERE_PROMPT_HOOKS)
    
    prompt = (
        f"{hook}\n\n"
        f"1. Name the THREE abiotic physical spheres of Earth that interact to sustain life in the biosphere.\n"
        f"2. A field biologist conducted an ecological survey of the South African **{b['name']}** in the {b['region']}.\n"
        f"   - State the prevailing climatic conditions of this biome.\n"
        f"   - Name an iconic endemic species found here: **{b['endemic_species']}**.\n"
        f"   - Explain ONE structural adaptation that enables this species to survive in this specific biome.\n"
        f"3. Classify living organisms into the standard Five Kingdoms according to Whittaker's classification system.\n"
        f"4. Under binomial nomenclature rules, explain why scientific names (such as *{b['endemic_species']}*) consist of two words written in italics."
    )
    prompt_latex = (
        rf"\textbf{{The Biosphere and South African Biodiversity: {b['name']}}}" "\n\n"
        r"\text{1. Three abiotic physical spheres that interact to sustain the biosphere.}" "\n"
        rf"\text{{2. Ecology of {b['name']}: Climate, Endemic organism ({b['endemic_species']}), and adaptation.}}" "\n"
        r"\text{3. Five-Kingdom Classification Scheme (Whittaker).}" "\n"
        rf"\text{{4. Binomial nomenclature principles: Scientific naming conventions.}}"
    )
    answer_latex = (
        r"\text{1. Spheres: Atmosphere (air/gases), Lithosphere (crust/soil/rocks), Hydrosphere (all water).}" "\n"
        rf"\text{{2. Climate: {b['climate']}. Endemic: {b['endemic_species']}. Adaptation: {b['adaptation']}.}}" "\n"
        r"\text{3. Five Kingdoms: Animalia, Plantae, Fungi, Protista, Monera (Bacteria).}" "\n"
        r"\text{4. Binomial nomenclature: First word is Genus (capitalised); second word is species (lowercase); italicised to denote Latin origin.}"
    )
    sample = (
        "1. Three abiotic spheres: Atmosphere (gaseous envelope), Lithosphere (Earth's crust and soil), Hydrosphere (all water bodies).\n"
        f"2. {b['name']} Ecology:\n"
        f"   - Climate: {b['climate']}.\n"
        f"   - Endemic species: {b['endemic_species']}.\n"
        f"   - Adaptation: {b['adaptation']}.\n"
        "3. Five Kingdoms: Animalia, Plantae, Fungi, Protista, Monera (Bacteria).\n"
        f"4. Binomial nomenclature: The two-part scientific name specifies Genus (first word, capitalised) and species (second word, lowercase), universally recognised in Latin to prevent regional language confusion."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Atmosphere, Lithosphere, Hydrosphere correctly identified", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Accurate climate description and adaptation for {b['name']}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "All 5 Whittaker kingdoms correctly named", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Correct binomial nomenclature explanation (Genus + species)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Consider the three physical environments (rock, water, air) and the Latin Genus-species system.",
        "concept": "The biosphere integrates the atmosphere, hydrosphere, and lithosphere. Whittaker's 5 kingdoms are Monera, Protista, Fungi, Plantae, Animalia.",
        "breakdown": f"Biome: {b['name']}. Spheres: Lithosphere, Hydrosphere, Atmosphere. Endemic adaptation: {b['adaptation'][:60]}...",
    }
    return make_science_question(
        prefix="ns_bio_gr7",
        topic=TOPIC,
        subskill="biosphere_and_biodiversity_biomes",
        learning_objective_id=f"{LO}_biosphere_biodiversity",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["confusing_lithosphere_with_biosphere", "capitalising_species_epithet_in_binomial_name"],
        keywords=["biosphere", "lithosphere", "hydrosphere", "atmosphere", "fynbos", "biodiversity", "endemic"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 5: ANGIOSPERM REPRODUCTION & POLLINATION (Grade 7)
# ============================================================================

FLOWERING_SPECIES = [
    {
        "common": "Bird of Paradise",
        "scientific": "Strelitzia reginae",
        "pollinator": "Sunbirds (ornithophily)",
        "pollinator_adaptation": "Rigid boat-shaped spathe for birds to perch; bright orange sepals and arrow-like blue petals containing nectar",
    },
    {
        "common": "Wild Dagga / Lion's Ear",
        "scientific": "Leonotis leonurus",
        "pollinator": "Bees and sunbirds",
        "pollinator_adaptation": "Tubular orange velvety flowers arranged in rounded whorls, positioned for pollen transfer to animal foreheads",
    },
    {
        "common": "Cape Honeysuckle",
        "scientific": "Tecoma capensis",
        "pollinator": "Sunbirds",
        "pollinator_adaptation": "Long curved trumpet flowers with protruding stamens that brush pollen onto the pollinator's chest",
    },
    {
        "common": "Sweetcorn / Maize",
        "scientific": "Zea mays",
        "pollinator": "Wind (anemophily)",
        "pollinator_adaptation": "Lightweight airborne pollen produced in vast quantities from dangling tassels; feathery silk stigmas to catch passing grains",
    },
]

def _gen_angiosperm_reproduction_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    flower_parts = [
        {"part": "Anther", "role": "Produces pollen grains containing male gametes"},
        {"part": "Filament", "role": "Slender stalk that supports the anther in an exposed position"},
        {"part": "Stigma", "role": "Sticky surface that receives pollen grains during pollination"},
        {"part": "Style", "role": "Neck-like column down which the pollen tube grows toward the ovary"},
        {"part": "Ovary", "role": "Swollen basal structure containing ovules; develops into the fruit after fertilisation"},
        {"part": "Ovule", "role": "Contains female egg cell; develops into the seed following fertilisation"},
        {"part": "Petal (Corolla)", "role": "Brightly coloured, scented structure that attracts animal pollinators"},
        {"part": "Sepal (Calyx)", "role": "Green leaf-like structure that protects the flower bud before it opens"},
    ]
    sampled = r.sample(flower_parts, 3)
    p1, p2, p3 = sampled[0], sampled[1], sampled[2]
    specimen = r.choice(FLOWERING_SPECIES)
    
    prompt = (
        f"Flowering plants (angiosperms), such as the South African **{specimen['common']}** (*{specimen['scientific']}*), undergo sexual reproduction to propagate.\n\n"
        f"1. Distinguish between the botanical terms **pollination** and **fertilisation**.\n"
        f"2. Identify the role of the following floral structures in sexual reproduction:\n"
        f"   - **{p1['part']}**\n"
        f"   - **{p2['part']}**\n"
        f"   - **{p3['part']}**\n"
        f"3. {specimen['common']} is pollinated primarily by {specimen['pollinator']}. Describe how its floral morphology is adapted for this mode of pollination.\n"
        f"4. State what floral structures eventually develop into: (a) the seed, and (b) the fruit."
    )
    prompt_latex = (
        rf"\textbf{{Angiosperm Floral Morphology & Reproduction: {specimen['common']}}}" "\n\n"
        r"\text{1. Distinguish: Pollination vs. Fertilisation.}" "\n"
        rf"\text{{2. Functional roles of: {p1['part']}, {p2['part']}, {p3['part']}.}}" "\n"
        rf"\text{{3. Floral adaptations of {specimen['common']} for {specimen['pollinator']}.}}" "\n"
        r"\text{4. Post-fertilisation development of Ovule and Ovary.}"
    )
    answer_latex = (
        r"\text{1. Pollination: Transfer of pollen from anther to stigma. Fertilisation: Fusion of male gamete nucleus with female ovule nucleus.}" "\n"
        rf"\text{{2. {p1['part']}: {p1['role']}; {p2['part']}: {p2['role']}; {p3['part']}: {p3['role']}.}}" "\n"
        rf"\text{{3. Adaptation: {specimen['pollinator_adaptation']}.}}" "\n"
        r"\text{4. (a) Ovule } \to \text{ Seed; (b) Ovary } \to \text{ Fruit.}"
    )
    sample = (
        "1. Pollination is the physical transfer of pollen grains from the anther to the receptive stigma. "
        "Fertilisation is the subsequent fusion of the male gamete nucleus with the female egg nucleus inside the ovule.\n"
        f"2. Roles:\n"
        f"   - {p1['part']}: {p1['role']}.\n"
        f"   - {p2['part']}: {p2['role']}.\n"
        f"   - {p3['part']}: {p3['role']}.\n"
        f"3. Adaptations: {specimen['pollinator_adaptation']}.\n"
        "4. (a) The fertilised ovule develops into the seed. (b) The ovary wall develops into the fruit."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate distinction between pollination and fertilisation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Accurate roles for {p1['part']}, {p2['part']}, and {p3['part']}", "marks": 3, "editable": True},
            {"id": "mp3", "desc": f"Correct morphological adaptation for {specimen['pollinator']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Correct identification of ovule -> seed and ovary -> fruit", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Remember that pollen must first land on the stigma before the pollen tube can grow down to fuse with the egg.",
        "concept": "Pollination is pollen movement; fertilisation is gamete fusion. Ovules become seeds, ovaries become fruits.",
        "breakdown": f"Flower parts: {p1['part']} ({p1['role']}), {p2['part']} ({p2['role']}), {p3['part']} ({p3['role']}). Species: {specimen['common']}.",
    }
    return make_science_question(
        prefix="ns_angio",
        topic=TOPIC,
        subskill="angiosperm_reproduction_and_floral_anatomy",
        learning_objective_id=f"{LO}_angiosperm_reproduction",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["confusing_pollination_with_fertilisation", "confusing_ovary_with_ovule_destination"],
        keywords=["pollination", "fertilisation", "anther", "stigma", "ovary", "ovule", "pollen"],
        term=1,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# MAIN DISPATCH ENTRY POINT
# ============================================================================

def generate(seed: Optional[int] = None, grade: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Natural Sciences Life & Living question."""
    r = rng(seed)
    ARCHETYPES = ["photosynthesis", "cell_cytology", "human_systems", "biosphere", "angiosperm"]
    
    # If no archetype is explicitly passed, determine by seed rotation
    if archetype is None:
        if grade == 7:
            archetype = "biosphere" if (int(seed or 0) % 2 == 0) else "angiosperm"
        elif grade == 9:
            archetype = "cell_cytology" if (int(seed or 0) % 2 == 0) else "human_systems"
        elif grade == 8:
            # For general life and living, cycle across all 5 archetypes by seed
            archetype = ARCHETYPES[int(seed or 0) % len(ARCHETYPES)]
        else:
            archetype = ARCHETYPES[int(seed or 0) % len(ARCHETYPES)]

    if archetype == "photosynthesis":
        return _gen_photosynthesis_question(r, grade=grade or 8, mode=mode)
    elif archetype == "cell_cytology":
        return _gen_cell_cytology_question(r, mode=mode)
    elif archetype == "human_systems":
        return _gen_human_systems_question(r, mode=mode)
    elif archetype == "biosphere":
        return _gen_biosphere_biodiversity_question(r, mode=mode)
    elif archetype == "angiosperm":
        return _gen_angiosperm_reproduction_question(r, mode=mode)
    else:
        return _gen_photosynthesis_question(r, grade=grade or 8, mode=mode)

