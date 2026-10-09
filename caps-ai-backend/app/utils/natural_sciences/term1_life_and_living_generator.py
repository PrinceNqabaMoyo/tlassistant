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
]


def _gen_photosynthesis_question(r: random.Random, grade: int = 8, mode: str = "compound") -> Dict[str, Any]:
    scen = r.choice(PHOTOSYNTHESIS_SCENARIOS)
    
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

    # Compound organelle function and structure
    prompt = (
        f"A Grade 9 learner viewed various eukaryotic cells under a compound light microscope.\n\n"
        f"1. Identify the organelle described as '{o1['structure']}'. State its primary cellular function.\n"
        f"2. Organelle '{o2['name']}' is found in {o2['found_in']}. Explain one structural adaptation of this organelle that maximizes its efficiency.\n"
        f"3. What metabolic crisis would a cell experience if all of its {o3['name']}s were enzymatically deactivated?\n"
        f"4. Calculate the actual width of a plant cell in micrometres (µm) if its magnified image measures 45 mm under a magnification of 400x."
    )
    prompt_latex = (
        rf"\textbf{{Cell Cytology Analysis}}" "\n\n"
        rf"\text{{1. Organelle 1 Description: {o1['structure']}. Name and function?}}" "\n"
        rf"\text{{2. Organelle 2 ({o2['name']}): Structural adaptation for efficiency?}}" "\n"
        rf"\text{{3. Consequence of deactivated {o3['name']}?}}" "\n"
        rf"\text{{4. Magnification Calculation: }}" "\n"
        r"\text{Actual size } = \frac{\text{Image size}}{\text{Magnification}} \quad [\text{Image} = 45\text{ mm}, \text{ Mag} = 400\times]"
    )
    actual_um = (45 * 1000) / 400
    actual_str = fmt_sa(actual_um, 2)
    answer_latex = (
        rf"\text{{1. Organelle: {o1['name']}. Function: {o1['function']}.}}" "\n"
        rf"\text{{2. Adaptation: {o2['adaptation']}.}}" "\n"
        rf"\text{{3. Impact: Loss of {o3['name']} impairs: {o3['function']}.}}" "\n"
        rf"\text{{4. Actual size}} = \frac{{45\text{{ mm}} \times 1\,000}}{{400}} = \frac{{45\,000}}{{400}} = {actual_str}\text{{ }}\mu\text{{m}}"
    )
    sample = (
        f"1. Name: {o1['name']}. Function: {o1['function']}.\n"
        f"2. Adaptation: {o2['adaptation']}.\n"
        f"3. Deactivating {o3['name']} stops its vital role: {o3['function']}.\n"
        f"4. Formula: Actual size = Image size / Magnification.\n"
        f"   Convert 45 mm to micrometres: 45 mm x 1000 = 45 000 µm.\n"
        f"   Actual size = 45 000 µm / 400 = {actual_str} µm."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": f"Correctly identify {o1['name']} and function", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct structural adaptation for {o2['name']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate biological deduction for deactivated {o3['name']}", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Correct conversion (mm to µm) and division by 400x", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Remember that 1 millimetre contains 1 000 micrometres (µm).",
        "concept": "Magnification formula: Actual size (A) = Image size (I) / Magnification (M). Ensure units match before dividing.",
        "breakdown": f"45 mm = 45 000 µm. 45 000 / 400 = {actual_str} µm. Organelle 1 is {o1['name']}.",
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
    
    prompt = (
        f"The human body relies on coordinated organ systems to maintain internal homeostasis.\n\n"
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
# ARCHETYPE 4: ANGIOSPERM REPRODUCTION & BIODIVERSITY (Grade 7)
# ============================================================================

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
    
    prompt = (
        f"Flowering plants (angiosperms) undergo sexual reproduction to produce seeds for the next generation.\n\n"
        f"1. Distinguish between the botanical terms **pollination** and **fertilisation**.\n"
        f"2. Identify the role of the following floral structures in sexual reproduction:\n"
        f"   - **{p1['part']}**\n"
        f"   - **{p2['part']}**\n"
        f"   - **{p3['part']}**\n"
        f"3. Differentiate between flowers adapted for insect pollination versus wind pollination in terms of pollen appearance and petal structure.\n"
        f"4. State what floral structures eventually develop into: (a) the seed, and (b) the fruit."
    )
    prompt_latex = (
        r"\textbf{Angiosperm Floral Morphology & Sexual Reproduction}" "\n\n"
        r"\text{1. Distinguish: Pollination vs. Fertilisation.}" "\n"
        rf"\text{{2. Functional roles of: {p1['part']}, {p2['part']}, {p3['part']}.}}" "\n"
        r"\text{3. Adaptations: Insect-pollinated vs. Wind-pollinated floral anatomy.}" "\n"
        r"\text{4. Post-fertilisation development of Ovule and Ovary.}"
    )
    answer_latex = (
        r"\text{1. Pollination: Transfer of pollen from anther to stigma. Fertilisation: Fusion of male gamete nucleus with female ovule nucleus.}" "\n"
        rf"\text{{2. {p1['part']}: {p1['role']}; {p2['part']}: {p2['role']}; {p3['part']}: {p3['role']}.}}" "\n"
        r"\text{3. Insect: Bright large petals, sticky pollen. Wind: Small green/reduced petals, light abundant airborne pollen.}" "\n"
        r"\text{4. (a) Ovule } \to \text{ Seed; (b) Ovary } \to \text{ Fruit.}"
    )
    sample = (
        "1. Pollination is the physical transfer of pollen grains from the anther to the receptive stigma. "
        "Fertilisation is the subsequent fusion of the male gamete nucleus with the female egg nucleus inside the ovule.\n"
        f"2. Roles:\n"
        f"   - {p1['part']}: {p1['role']}.\n"
        f"   - {p2['part']}: {p2['role']}.\n"
        f"   - {p3['part']}: {p3['role']}.\n"
        "3. Insect-pollinated flowers have large, brightly coloured petals, nectar, and sticky rough pollen grains. "
        "Wind-pollinated flowers have small, dull/green petals, long dangling stamens, feathery stigmas, and smooth, light, airborne pollen.\n"
        "4. (a) The fertilised ovule develops into the seed. (b) The ovary wall develops into the fruit."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate distinction between pollination and fertilisation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Accurate roles for {p1['part']}, {p2['part']}, and {p3['part']}", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Correct contrast between insect and wind pollination traits", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Correct identification of ovule -> seed and ovary -> fruit", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Remember that pollen must first land on the stigma before the pollen tube can grow down to fuse with the egg.",
        "concept": "Pollination is pollen movement; fertilisation is gamete fusion. Ovules become seeds, ovaries become fruits.",
        "breakdown": f"Flower parts: {p1['part']} ({p1['role']}), {p2['part']} ({p2['role']}), {p3['part']} ({p3['role']}).",
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

def generate(seed: Optional[int] = None, grade: int = 8, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Natural Sciences Life & Living question."""
    r = rng(seed)
    
    if archetype == "photosynthesis" or (archetype is None and grade == 8):
        return _gen_photosynthesis_question(r, grade=grade, mode=mode)
    elif archetype == "cell_cytology" or (archetype is None and grade == 9 and r.random() < 0.5):
        return _gen_cell_cytology_question(r, mode=mode)
    elif archetype == "human_systems" or (archetype is None and grade == 9):
        return _gen_human_systems_question(r, mode=mode)
    elif archetype == "angiosperm" or (archetype is None and grade == 7):
        return _gen_angiosperm_reproduction_question(r, mode=mode)
    else:
        # Default distribution across archetypes
        choice = r.choice(["photosynthesis", "cell_cytology", "human_systems", "angiosperm"])
        if choice == "photosynthesis":
            return _gen_photosynthesis_question(r, grade=grade, mode=mode)
        elif choice == "cell_cytology":
            return _gen_cell_cytology_question(r, mode=mode)
        elif choice == "human_systems":
            return _gen_human_systems_question(r, mode=mode)
        else:
            return _gen_angiosperm_reproduction_question(r, mode=mode)
