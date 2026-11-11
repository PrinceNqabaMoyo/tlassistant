"""Grade 9 Natural Sciences: Term 1 - Systems in the Human Body (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md.
Focus: Curated Campbell organ plates (Nephron, Endocrine, Digestive), organ systems overview, digestion, circulation, respiration, and skeleton.
"""
from __future__ import annotations

import json
import os
import random
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


NEPHRON_DATA = _load_anchors("human_nephron")
ENDOCRINE_DATA = _load_anchors("endocrine_system")
DIGESTIVE_DATA = _load_anchors("digestive_system")


def _make_organ_plate_question(
    rng: random.Random,
    master: str,
    target_key: str,
    subskill_id: str,
    system_label: str,
) -> Dict[str, Any]:
    if master == "human_nephron":
        anchor_data = NEPHRON_DATA
    elif master == "endocrine_system":
        anchor_data = ENDOCRINE_DATA
    else:
        anchor_data = DIGESTIVE_DATA

    anchors = anchor_data["anchors"]
    target = anchors[target_key]

    candidate_keys = [k for k in anchors.keys() if k != target_key]
    rng.shuffle(candidate_keys)
    selected_keys = [target_key] + candidate_keys[:3]
    rng.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = f"{rng.randint(100000, 999999)}_{k}"
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    diag_payload = {
        "diagram_role": "identify",
        "image_type": master,
        "master": master,
        "view": anchor_data.get("view", "anatomical_cross_section"),
        "viewBox": anchor_data.get("viewBox", "0 0 600 480"),
        "grade_mask": "g9",
        "pins": pins_payload,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    prompt = (
        f"Study the anatomical plate of the human **{system_label}**.\n\n"
        f"Which anatomical structure or organ is indicated by **Pin {target_pin}**?"
    )
    correct = target["name"]
    distractors = [anchors[k]["name"] for k in selected_keys if k != target_key]
    options = [correct] + distractors
    rng.shuffle(options)

    sol = (
        f"**Step 1:** Locate Pin {target_pin} on the {system_label} plate.\n"
        f"**Step 2:** Review anatomical position and physiological characteristics:\n"
        f"- {target['name']}: {target['description']}\n\n"
        f"**Step 3:** The structure indicated by Pin {target_pin} is **{correct}**."
    )

    return {
        "id": f"ns9_sys_{subskill_id[:2]}_{rng.randint(100000, 999999)}",
        "subskill": subskill_id,
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": diag_payload,
        "hints": {
            "tier_1": f"Observe where Pin {target_pin} is pointing on the {system_label} diagram.",
            "tier_2": f"This structure is known for: {target['description'][:60]}...",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": [f"organ_plate_identification_{target_key}_misconception"],
    }


# 01. Nephron glomerulus filtration plate identification (Campbell Plate)
def arch_01_nephron_glomerulus_filtration_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "human_nephron", "glomerulus", "01_nephron_glomerulus_filtration_plate_identification", "excretory nephron")


# 02. Nephron bowmans capsule ultrafiltration plate identification (Campbell Plate)
def arch_02_nephron_bowmans_capsule_ultrafiltration_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "human_nephron", "bowmans_capsule", "02_nephron_bowmans_capsule_ultrafiltration_plate_identification", "excretory nephron")


# 03. Nephron tubule reabsorption plate identification (Campbell Plate)
def arch_03_nephron_tubule_reabsorption_plate_identification(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["proximal_convoluted_tubule", "loop_of_henle"])
    return _make_organ_plate_question(rng, "human_nephron", target, "03_nephron_tubule_reabsorption_plate_identification", "excretory nephron")


# 04. Nephron collecting duct osmoregulation plate identification (Campbell Plate)
def arch_04_nephron_collecting_duct_osmoregulation_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "human_nephron", "collecting_duct", "04_nephron_collecting_duct_osmoregulation_plate_identification", "excretory nephron")


# 05. Endocrine pituitary master gland plate identification (Campbell Plate)
def arch_05_endocrine_pituitary_master_gland_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "endocrine_system", "pituitary_gland", "05_endocrine_pituitary_master_gland_plate_identification", "endocrine system")


# 06. Endocrine thyroid metabolism gland plate identification (Campbell Plate)
def arch_06_endocrine_thyroid_metabolism_gland_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "endocrine_system", "thyroid_gland", "06_endocrine_thyroid_metabolism_gland_plate_identification", "endocrine system")


# 07. Endocrine pancreas islets insulin plate identification (Campbell Plate)
def arch_07_endocrine_pancreas_islets_insulin_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "endocrine_system", "pancreas", "07_endocrine_pancreas_islets_insulin_plate_identification", "endocrine system")


# 08. Endocrine adrenal stress hormone plate identification (Campbell Plate)
def arch_08_endocrine_adrenal_stress_hormone_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "endocrine_system", "adrenal_glands", "08_endocrine_adrenal_stress_hormone_plate_identification", "endocrine system")


# 09. Digestive stomach acid churning plate identification (Campbell Plate)
def arch_09_digestive_stomach_acid_churning_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "digestive_system", "stomach", "09_digestive_stomach_acid_churning_plate_identification", "digestive system")


# 10. Digestive small intestine absorption plate identification (Campbell Plate)
def arch_10_digestive_small_intestine_absorption_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "digestive_system", "small_intestine", "10_digestive_small_intestine_absorption_plate_identification", "digestive system")


# 11. Digestive liver bile production plate identification (Campbell Plate)
def arch_11_digestive_liver_bile_production_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "digestive_system", "liver", "11_digestive_liver_bile_production_plate_identification", "digestive system")


# 12. Digestive esophagus peristalsis plate identification (Campbell Plate)
def arch_12_digestive_esophagus_peristalsis_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_organ_plate_question(rng, "digestive_system", "esophagus", "12_digestive_esophagus_peristalsis_plate_identification", "digestive system")


# 13. Human body systems overview and integration
def arch_13_human_body_systems_overview_and_integration(rng: random.Random) -> Dict[str, Any]:
    systems = [
        ("Nervous system", "detects internal and external stimuli, processes information, and coordinates electrical responses"),
        ("Endocrine system", "secretes chemical hormones directly into blood to regulate long-term growth, metabolism, and reproduction"),
        ("Excretory system", "filters nitrogenous metabolic wastes like urea from blood and regulates water and salt fluid balance"),
        ("Musculoskeletal system", "supports body weight, protects internal organs, and enables locomotion via antagonistic muscle pairs"),
    ]
    sys_name, sys_fn = rng.choice(systems)
    prompt = (
        f"The human body functions as a unified organism through multiple interdependent organ systems.\n\n"
        f"What is the primary physiological purpose of the **{sys_name}**?"
    )
    correct = f"It {sys_fn}."
    alt = [s[1] for s in systems if s[0] != sys_name]
    distractors = [f"It {fn}." for fn in alt]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review major body systems:\n"
        f"- For {sys_name}: {sys_fn}.\n\n"
        f"**Step 2:** The primary purpose is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_13_{rng.randint(100000, 999999)}",
        "subskill": "13_human_body_systems_overview_and_integration",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about what the {sys_name} accomplishes for the body.",
            "tier_2": f"Match {sys_name} to its defining physiological function.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["body_systems_purposes_overview_misconception"],
    }


# 14. Digestive system four core processes ingestion digestion absorption egestion
def arch_14_digestive_system_four_core_processes_ingestion_digestion_absorption_egestion(rng: random.Random) -> Dict[str, Any]:
    stages = [
        ("Ingestion", "Taking food and liquid into the body through the mouth"),
        ("Digestion", "Breaking down large, insoluble food molecules mechanically and chemically into small, soluble molecules"),
        ("Absorption", "Moving digested nutrient molecules across the intestinal epithelium into the bloodstream and lacteals"),
        ("Egestion", "Expelling undigested, unabsorbed food residues and dietary fibre from the anus as faeces"),
    ]
    target_stage, definition = rng.choice(stages)
    prompt = (
        f"Nutrition along the human alimentary canal occurs in four sequential physiological stages:\n"
        f"$$\\text{{Ingestion}} \\rightarrow \\text{{Digestion}} \\rightarrow \\text{{Absorption}} \\rightarrow \\text{{Egestion}}$$\n\n"
        f"What is the precise biological definition of **{target_stage}**?"
    )
    correct = definition
    alt = [s[1] for s in stages if s[0] != target_stage]
    options = [correct] + alt
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the four digestive processes:\n"
        f"- Ingestion = taking in food.\n"
        f"- Digestion = breaking down polymers into monomers.\n"
        f"- Absorption = nutrient uptake into blood.\n"
        f"- Egestion = removal of undigested waste (faeces).\n\n"
        f"**Step 2:** For {target_stage}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_14_{rng.randint(100000, 999999)}",
        "subskill": "14_digestive_system_four_core_processes_ingestion_digestion_absorption_egestion",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {target_stage} taking in food, breaking it down, absorbing it, or expelling faeces?",
            "tier_2": f"Match {target_stage} to its exact biological definition.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["digestion_vs_absorption_vs_egestion_misconception"],
    }


# 15. Mechanical vs chemical digestion peristalsis and enzymes
def arch_15_mechanical_vs_chemical_digestion_peristalsis_and_enzymes(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Mechanical digestion",
            "Physical breakdown of large food pieces into smaller chunks (by chewing with teeth, muscular churning in stomach, and bile emulsification) without altering chemical bonds, increasing surface area for enzymes",
        ),
        (
            "Chemical digestion",
            "Enzymatic hydrolysis that breaks chemical covalent bonds within large, insoluble macromolecules (converting starch into glucose, proteins into amino acids, and lipids into fatty acids and glycerol)",
        ),
    ]
    target_t, desc = rng.choice(types)
    prompt = (
        f"Digestion involves both mechanical and chemical processes.\n\n"
        f"Which statement scientifically distinguishes **{target_t}**?"
    )
    correct = desc
    other_t = [t[1] for t in types if t[0] != target_t][0]
    options = [
        correct,
        other_t,
        "It uses gamma radiation to convert food into pure gold atoms inside the esophagus.",
        "It freezes all food into solid nitrogen blocks to stop microbial digestion.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish mechanical vs chemical digestion:\n"
        f"- Mechanical = physical breaking (teeth, churning, bile); increases surface area; no chemical bond breakage.\n"
        f"- Chemical = enzymatic hydrolysis; breaks chemical bonds to yield monomers.\n\n"
        f"**Step 2:** For {target_t}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_15_{rng.randint(100000, 999999)}",
        "subskill": "15_mechanical_vs_chemical_digestion_peristalsis_and_enzymes",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does mechanical digestion break chemical bonds or only physical size?",
            "tier_2": "Mechanical digestion physically breaks food to increase surface area; chemical digestion breaks bonds using enzymes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mechanical_vs_chemical_digestion_misconception"],
    }


# 16. Digestive enzymes carbohydrases proteases and lipases
def arch_16_digestive_enzymes_carbohydrases_proteases_and_lipases(rng: random.Random) -> Dict[str, Any]:
    enzymes = [
        ("Salivary and pancreatic amylase (carbohydrases)", "starch (complex polysaccharide)", "maltose and glucose simple sugars"),
        ("Pepsin and trypsin (proteases)", "proteins (polypeptide chains)", "soluble amino acids"),
        ("Pancreatic lipase", "lipids (dietary fats and oils)", "fatty acids and glycerol"),
    ]
    target_enz, substrate, end_products = rng.choice(enzymes)
    prompt = (
        f"Digestive enzymes act as biological catalysts with high substrate specificity.\n\n"
        f"What substrate does **{target_enz}** break down, and what are the resulting absorbable end products?"
    )
    correct = f"Substrate: {substrate};\nEnd products: {end_products}."
    alt = [e for e in enzymes if e[0] != target_enz]
    distractors = [f"Substrate: {e[1]};\nEnd products: {e[2]}." for e in alt]
    distractors.append("Substrate: Metallic iron;\nEnd products: Helium gas.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review digestive enzyme specificity:\n"
        f"- Amylase hydrolyses starch -> maltose/glucose.\n"
        f"- Proteases hydrolyse proteins -> amino acids.\n"
        f"- Lipase hydrolyses lipids -> fatty acids and glycerol.\n\n"
        f"**Step 2:** For {target_enz}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_16_{rng.randint(100000, 999999)}",
        "subskill": "16_digestive_enzymes_carbohydrases_proteases_and_lipases",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {target_enz.split()[0]} a carbohydrase, protease, or lipase?",
            "tier_2": f"Match {target_enz} to its specific food substrate and monomer products.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["digestive_enzymes_substrate_products_misconception"],
    }


# 17. Circulatory system closed double circulation pulmonary and systemic
def arch_17_circulatory_system_closed_double_circulation_pulmonary_and_systemic(rng: random.Random) -> Dict[str, Any]:
    circuits = [
        (
            "Pulmonary circulation",
            "Right ventricle -> Pulmonary artery -> Lungs (capillary gas exchange oxygenating blood) -> Pulmonary veins -> Left atrium",
            "deoxygenated blood is pumped to the lungs to offload CO2 and pick up O2",
        ),
        (
            "Systemic circulation",
            "Left ventricle -> Aorta -> Systemic arteries & body tissues -> Vena cava -> Right atrium",
            "oxygenated blood at high pressure is delivered to all body cells for cellular respiration",
        ),
    ]
    target_c, pathway, purpose = rng.choice(circuits)
    prompt = (
        f"Mammals possess a **closed double circulatory system** consisting of two separate vascular circuits.\n\n"
        f"Which pathway and physiological purpose correctly defines the **{target_c}**?"
    )
    correct = f"Pathway: {pathway}.\nPurpose: {purpose}."
    other_c = [c for c in circuits if c[0] != target_c][0]
    options = [
        correct,
        f"Pathway: {other_c[1]}.\nPurpose: {other_c[2]}.",
        "Pathway: Stomach -> Brain -> Ears -> Feet.\nPurpose: To cool the skull.",
        "Pathway: Hair follicles -> Fingernails -> Teeth.\nPurpose: To grow hard keratin.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze double circulation:\n"
        f"- Double circulation means blood passes through the heart twice for each complete circuit.\n"
        f"- Pulmonary: right heart -> lungs -> left heart (oxygenation).\n"
        f"- Systemic: left heart -> body tissues -> right heart (nutrient/oxygen delivery).\n\n"
        f"**Step 2:** For {target_c}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_17_{rng.randint(100000, 999999)}",
        "subskill": "17_circulatory_system_closed_double_circulation_pulmonary_and_systemic",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Does {target_c} travel to the lungs or to the rest of the body?",
            "tier_2": "Pulmonary goes to lungs for oxygenation; systemic goes to body organs at higher pressure.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pulmonary_vs_systemic_circulation_misconception"],
    }


# 18. Blood vessels structural comparison arteries veins capillaries
def arch_18_blood_vessels_structural_comparison_arteries_veins_capillaries(rng: random.Random) -> Dict[str, Any]:
    vessels = [
        (
            "Artery",
            "Thick muscular and elastic tunica media, narrow central lumen, withstands high pulsating systolic pressure, carries blood away from heart, no valves (except semilunars at base)",
        ),
        (
            "Vein",
            "Thin muscular wall, wide central lumen, low blood pressure, contains pocket semilunar valves to prevent backflow of blood against gravity, carries blood toward heart",
        ),
        (
            "Capillary",
            "Microscopic vessel with a wall only a single endothelial cell layer thick, highly branched network, allows rapid diffusion of oxygen, glucose, and wastes between blood and tissues",
        ),
    ]
    target_v, structural_desc = rng.choice(vessels)
    prompt = (
        f"Blood travels through three distinct types of blood vessels: arteries, veins, and capillaries.\n\n"
        f"Which structural profile scientifically describes an **{target_v}**?"
    )
    correct = structural_desc
    other_v = [v[1] for v in vessels if v[0] != target_v]
    options = [correct] + other_v
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare vessel histology:\n"
        f"- Arteries: thick, elastic walls to handle high pressure from ventricular systole.\n"
        f"- Veins: wide lumen, thin walls, valves to prevent backflow under low pressure.\n"
        f"- Capillaries: single-cell endothelium for rapid diffusion.\n\n"
        f"**Step 2:** For {target_v}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_18_{rng.randint(100000, 999999)}",
        "subskill": "18_blood_vessels_structural_comparison_arteries_veins_capillaries",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about wall thickness, lumen width, and valves for an {target_v.lower()}.",
            "tier_2": f"Arteries have thick elastic walls; veins have valves and wide lumens; capillaries are 1 cell thick.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["artery_vein_capillary_structural_differences_misconception"],
    }


# 19. Components of blood plasma erythrocytes leukocytes platelets
def arch_19_components_of_blood_plasma_erythrocytes_leukocytes_platelets(rng: random.Random) -> Dict[str, Any]:
    components = [
        ("Blood plasma (55% of volume)", "pale yellow liquid transport medium consisting of 90% water, carrying dissolved glucose, amino acids, mineral ions, hormones, urea, and plasma proteins"),
        ("Red blood cells / Erythrocytes", "biconcave anucleate discs containing iron-rich hemoglobin to transport oxygen from lungs to respiring cells"),
        ("White blood cells / Leukocytes", "nucleated immune cells (phagocytes and lymphocytes) that defend the body against infectious pathogens"),
        ("Platelets / Thrombocytes", "small cellular fragments without nuclei that initiate blood clotting (coagulation) to prevent blood loss and pathogen entry at wound sites"),
    ]
    target_comp, function = rng.choice(components)
    prompt = (
        f"Whole human blood is a specialized fluid connective tissue.\n\n"
        f"What is the composition and physiological function of **{target_comp}**?"
    )
    correct = function
    other_c = [c[1] for c in components if c[0] != target_comp]
    options = [correct] + other_c[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review blood components:\n"
        f"- Plasma = liquid matrix.\n"
        f"- Erythrocytes = oxygen transport via hemoglobin.\n"
        f"- Leukocytes = immunity.\n"
        f"- Platelets = clotting / coagulation.\n\n"
        f"**Step 2:** For {target_comp}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_19_{rng.randint(100000, 999999)}",
        "subskill": "19_components_of_blood_plasma_erythrocytes_leukocytes_platelets",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {target_comp.split()[0]} liquid plasma, oxygen-carrying, immune defense, or clotting?",
            "tier_2": f"Match {target_comp} to its specific physiological role in blood.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["blood_components_and_functions_misconception"],
    }


# 20. Respiratory system tract anatomy trachea bronchi alveoli
def arch_20_respiratory_system_tract_anatomy_trachea_bronchi_alveoli(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("C-shaped cartilage rings in the trachea and bronchi", "prevent the airway tubes from collapsing or kinking during the negative pressure of inhalation"),
        ("Ciliated mucous epithelium in the trachea", "traps inhaled dust and pathogens in mucus and beats cilia upward to clear the respiratory tract"),
        ("Microscopic alveoli clusters", "provide an enormous surface area (~70 m^2) enveloped by dense capillaries for gas exchange"),
    ]
    target_s, func = rng.choice(structures)
    prompt = (
        f"The human respiratory tract channels inhaled air from the nasal cavity into the lungs.\n\n"
        f"What is the biological importance of **{target_s}**?"
    )
    correct = f"It {func}."
    alt = [s[1] for s in structures if s[0] != target_s]
    distractors = [f"It {f}." for f in alt]
    distractors.append("It produces strong digestive acid to dissolve inhaled food.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review respiratory tract anatomy:\n"
        f"- For {target_s}: {func}.\n\n"
        f"**Step 2:** The accurate anatomical importance is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_20_{rng.randint(100000, 999999)}",
        "subskill": "20_respiratory_system_tract_anatomy_trachea_bronchi_alveoli",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Why does the body need {target_s.split()[0]} in the respiratory tract?",
            "tier_2": "Cartilage keeps airways open; cilia sweep mucus; alveoli provide surface area for gas diffusion.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiratory_anatomy_cartilage_alveoli_misconception"],
    }


# 21. Breathing ventilation mechanics inhalation vs exhalation
def arch_21_breathing_ventilation_mechanics_inhalation_vs_exhalation(rng: random.Random) -> Dict[str, Any]:
    phases = [
        (
            "Inhalation (Inspiration)",
            "Diaphragm contracts and flattens downward; external intercostal muscles contract, pulling ribs upward and outward; thoracic volume increases; thoracic air pressure falls below atmospheric pressure; air rushes in down the pressure gradient.",
        ),
        (
            "Exhalation (Expiration at rest)",
            "Diaphragm relaxes and domes upward; external intercostals relax, allowing ribs to move downward and inward; thoracic volume decreases; thoracic air pressure rises above atmospheric pressure; air is forced out.",
        ),
    ]
    target_p, mechanics = rng.choice(phases)
    prompt = (
        f"Ventilation (breathing) relies on volume and pressure changes inside the thoracic cavity.\n\n"
        f"Which sequence of muscular actions and pressure changes describes **{target_p}**?"
    )
    correct = mechanics
    other_p = [p[1] for p in phases if p[0] != target_p][0]
    options = [
        correct,
        other_p,
        "The stomach contracts, turning the lungs into solid rock which squeezes oxygen into the brain.",
        "The heart expands to push air directly through the skin pores into the atmosphere.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ventilation mechanics:\n"
        f"- Inhalation: active contraction of diaphragm (flattens) + intercostals (ribs up/out) -> volume increases -> pressure drops -> air enters.\n"
        f"- Exhalation: passive relaxation of diaphragm (domes) + intercostals (ribs down/in) -> volume decreases -> pressure rises -> air leaves.\n\n"
        f"**Step 2:** For {target_p}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_21_{rng.randint(100000, 999999)}",
        "subskill": "21_breathing_ventilation_mechanics_inhalation_vs_exhalation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"During {target_p}, does the diaphragm contract or relax, and does thoracic volume increase or decrease?",
            "tier_2": "Inhalation increases thoracic volume causing lower pressure; exhalation decreases volume causing higher pressure.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["breathing_mechanics_diaphragm_pressure_misconception"],
    }


# 22. Alveolar gas exchange diffusion gradients oxygen and carbon dioxide
def arch_22_alveolar_gas_exchange_diffusion_gradients_oxygen_and_carbon_dioxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Gas exchange between alveolar air spaces and pulmonary blood capillaries occurs across the respiratory membrane.\n\n"
        f"What physical and biological conditions maximize the rate of diffusion of oxygen into blood and carbon dioxide into alveoli?"
    )
    correct = (
        "A steep concentration gradient maintained by continuous ventilation and blood flow, "
        "an extremely short diffusion distance across single-cell-thick alveolar and capillary walls, "
        "a moist inner surface dissolving gases, and an enormous collective surface area."
    )
    options = [
        correct,
        "A thick wall of dry limestone rock that prevents any liquid water from contacting air.",
        "Zero concentration difference between air and blood so gases remain completely stationary.",
        "A cold vacuum chamber that freezes all gas molecules into solid carbon crystals.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply Fick's Law of diffusion to alveoli:\n"
        f"- High surface area (~70 m^2).\n"
        f"- Very thin barrier (0.5 um, single-cell layers).\n"
        f"- Moisture layer for gas solution.\n"
        f"- Steep partial pressure gradients ($pO_2$ in alveoli > capillary; $pCO_2$ in capillary > alveoli).\n\n"
        f"**Step 2:** The conditions are: **{correct}**."
    )
    return {
        "id": f"ns9_sys_22_{rng.randint(100000, 999999)}",
        "subskill": "22_alveolar_gas_exchange_diffusion_gradients_oxygen_and_carbon_dioxide",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What features make an efficient gas exchange surface?",
            "tier_2": "Large surface area, thin membrane (1 cell thick), moist surface, and steep concentration gradients.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["alveolar_gas_exchange_adaptations_misconception"],
    }


# 23. Musculoskeletal system bone tissue cartilage and marrow
def arch_23_musculoskeletal_system_bone_tissue_cartilage_and_marrow(rng: random.Random) -> Dict[str, Any]:
    tissues = [
        ("Compact bone tissue", "hard outer calcified matrix of calcium phosphate and collagen fibres providing rigid compressive strength"),
        ("Spongy bone tissue (cancellous bone)", "honeycomb lattice of trabeculae containing red bone marrow where hematopoiesis (blood cell production) occurs"),
        ("Articular cartilage", "smooth, glassy hyaline tissue covering bone ends in synovial joints to reduce friction and absorb mechanical shock"),
    ]
    target_t, role = rng.choice(tissues)
    prompt = (
        f"The human skeleton consists of 206 bones made of living osseous tissue and cartilage.\n\n"
        f"What is the structural characteristic and biological function of **{target_t}**?"
    )
    correct = role
    alt = [t[1] for t in tissues if t[0] != target_t]
    distractors = alt + ["dead metallic outer coating that conducts electric current across the skull"]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review skeletal tissue anatomy:\n"
        f"- Compact bone = dense, hard outer shell.\n"
        f"- Spongy bone = porous lattice with red marrow making blood cells.\n"
        f"- Cartilage = smooth shock-absorbing joint surface.\n\n"
        f"**Step 2:** For {target_t}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_23_{rng.randint(100000, 999999)}",
        "subskill": "23_musculoskeletal_system_bone_tissue_cartilage_and_marrow",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {target_t.split()[0]} dense, spongy with marrow, or smooth joint cartilage?",
            "tier_2": f"Match {target_t} to its specific histological structure and role.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bone_histology_cartilage_marrow_misconception"],
    }


# 24. Joints classification ball and socket hinge and pivot
def arch_24_joints_classification_ball_and_socket_hinge_and_pivot(rng: random.Random) -> Dict[str, Any]:
    joints = [
        ("Ball-and-socket joint (e.g. shoulder and hip joints)", "multiaxial rotational movement in all planes plus circumduction (360-degree range)"),
        ("Hinge joint (e.g. elbow and knee joints)", "uniaxial movement in a single plane only (flexion and extension, like a door hinge)"),
        ("Pivot joint (e.g. atlas-axis neck joint / radioulnar joint)", "rotational movement around a single central axis (allowing head shaking 'no')"),
    ]
    target_j, motion = rng.choice(joints)
    prompt = (
        f"Synovial joints allow different degrees of articulation between adjacent bones.\n\n"
        f"What range and type of mechanical movement is permitted by a **{target_j}**?"
    )
    correct = motion
    alt = [j[1] for j in joints if j[0] != target_j]
    options = [correct] + alt + ["zero movement because bones are permanently fused together with solid steel pins"]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Classify synovial joint kinematics:\n"
        f"- Ball-and-socket: multiaxial rotation (shoulder/hip).\n"
        f"- Hinge: uniaxial flexion/extension (elbow/knee).\n"
        f"- Pivot: rotation around an axis (neck atlas-axis).\n\n"
        f"**Step 2:** For {target_j}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_24_{rng.randint(100000, 999999)}",
        "subskill": "24_joints_classification_ball_and_socket_hinge_and_pivot",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about how the shoulder/hip, elbow/knee, or neck pivots.",
            "tier_2": "Ball-and-socket allows all-plane rotation; hinge allows single-plane movement; pivot allows rotation on an axis.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["synovial_joints_movement_planes_misconception"],
    }


# 25. Tendons vs ligaments connective tissue function
def arch_25_tendons_vs_ligaments_connective_tissue_function(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (
            "Tendon",
            "Tough, non-elastic fibrous connective tissue that attaches skeletal muscle to bone, transmitting contractile pulling force to move the skeleton",
        ),
        (
            "Ligament",
            "Strong, slightly elastic fibrous connective tissue that connects bone to bone across a joint, stabilizing the joint and preventing dislocation",
        ),
    ]
    target_t, role = rng.choice(pairs)
    prompt = (
        f"The musculoskeletal system relies on specialized fibrous connective tissues to link muscles, bones, and joints.\n\n"
        f"What is the precise anatomical definition and mechanical function of a **{target_t}**?"
    )
    correct = role
    other_t = [p[1] for p in pairs if p[0] != target_t][0]
    options = [
        correct,
        other_t,
        "A nerve fibre that conducts electrical action potentials from the stomach to the kidney",
        "A layer of adipose fat that cools the elbow during summer",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish tendons and ligaments:\n"
        f"- **Tendon**: connects muscle to bone (transmits pull; inelastic).\n"
        f"- **Ligament**: connects bone to bone (stabilizes joint; slightly elastic).\n\n"
        f"**Step 2:** For {target_t}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_25_{rng.randint(100000, 999999)}",
        "subskill": "25_tendons_vs_ligaments_connective_tissue_function",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does it connect muscle-to-bone or bone-to-bone?",
            "tier_2": "Tendons connect muscle to bone; ligaments connect bone to bone at joints.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tendon_vs_ligament_confusion_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_nephron_glomerulus_filtration_plate_identification": arch_01_nephron_glomerulus_filtration_plate_identification,
    "02_nephron_bowmans_capsule_ultrafiltration_plate_identification": arch_02_nephron_bowmans_capsule_ultrafiltration_plate_identification,
    "03_nephron_tubule_reabsorption_plate_identification": arch_03_nephron_tubule_reabsorption_plate_identification,
    "04_nephron_collecting_duct_osmoregulation_plate_identification": arch_04_nephron_collecting_duct_osmoregulation_plate_identification,
    "05_endocrine_pituitary_master_gland_plate_identification": arch_05_endocrine_pituitary_master_gland_plate_identification,
    "06_endocrine_thyroid_metabolism_gland_plate_identification": arch_06_endocrine_thyroid_metabolism_gland_plate_identification,
    "07_endocrine_pancreas_islets_insulin_plate_identification": arch_07_endocrine_pancreas_islets_insulin_plate_identification,
    "08_endocrine_adrenal_stress_hormone_plate_identification": arch_08_endocrine_adrenal_stress_hormone_plate_identification,
    "09_digestive_stomach_acid_churning_plate_identification": arch_09_digestive_stomach_acid_churning_plate_identification,
    "10_digestive_small_intestine_absorption_plate_identification": arch_10_digestive_small_intestine_absorption_plate_identification,
    "11_digestive_liver_bile_production_plate_identification": arch_11_digestive_liver_bile_production_plate_identification,
    "12_digestive_esophagus_peristalsis_plate_identification": arch_12_digestive_esophagus_peristalsis_plate_identification,
    "13_human_body_systems_overview_and_integration": arch_13_human_body_systems_overview_and_integration,
    "14_digestive_system_four_core_processes_ingestion_digestion_absorption_egestion": arch_14_digestive_system_four_core_processes_ingestion_digestion_absorption_egestion,
    "15_mechanical_vs_chemical_digestion_peristalsis_and_enzymes": arch_15_mechanical_vs_chemical_digestion_peristalsis_and_enzymes,
    "16_digestive_enzymes_carbohydrases_proteases_and_lipases": arch_16_digestive_enzymes_carbohydrases_proteases_and_lipases,
    "17_circulatory_system_closed_double_circulation_pulmonary_and_systemic": arch_17_circulatory_system_closed_double_circulation_pulmonary_and_systemic,
    "18_blood_vessels_structural_comparison_arteries_veins_capillaries": arch_18_blood_vessels_structural_comparison_arteries_veins_capillaries,
    "19_components_of_blood_plasma_erythrocytes_leukocytes_platelets": arch_19_components_of_blood_plasma_erythrocytes_leukocytes_platelets,
    "20_respiratory_system_tract_anatomy_trachea_bronchi_alveoli": arch_20_respiratory_system_tract_anatomy_trachea_bronchi_alveoli,
    "21_breathing_ventilation_mechanics_inhalation_vs_exhalation": arch_21_breathing_ventilation_mechanics_inhalation_vs_exhalation,
    "22_alveolar_gas_exchange_diffusion_gradients_oxygen_and_carbon_dioxide": arch_22_alveolar_gas_exchange_diffusion_gradients_oxygen_and_carbon_dioxide,
    "23_musculoskeletal_system_bone_tissue_cartilage_and_marrow": arch_23_musculoskeletal_system_bone_tissue_cartilage_and_marrow,
    "24_joints_classification_ball_and_socket_hinge_and_pivot": arch_24_joints_classification_ball_and_socket_hinge_and_pivot,
    "25_tendons_vs_ligaments_connective_tissue_function": arch_25_tendons_vs_ligaments_connective_tissue_function,
}
