"""Grade 9 Natural Sciences: Term 1 - Circulatory and Respiratory Systems (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/04. Circulatory and respiratory systems.md.
Focus: Curated Campbell organ plates (Heart & Alveolus Gas Exchange), double circulation, cardiac cycle, blood vessels, breathing mechanics, and gas diffusion.
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


HEART_DATA = _load_anchors("heart")
ALVEOLUS_DATA = _load_anchors("alveolus_gas_exchange")


def _make_plate_question(
    rng: random.Random,
    master: str,
    target_key: str,
    subskill_id: str,
    system_label: str,
) -> Dict[str, Any]:
    anchor_data = HEART_DATA if master == "heart" else ALVEOLUS_DATA
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
        "view": anchor_data.get("view", "coronal_section"),
        "viewBox": anchor_data.get("viewBox", "0 0 600 480"),
        "grade_mask": "g9",
        "pins": pins_payload,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    prompt = (
        f"Study the anatomical plate of the human **{system_label}**.\n\n"
        f"Which anatomical structure is indicated by **Pin {target_pin}**?"
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
        "id": f"ns9_crs_{subskill_id[:2]}_{rng.randint(100000, 999999)}",
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
            "tier_1": f"Observe the position of Pin {target_pin} on the {system_label} diagram.",
            "tier_2": f"This structure is known for: {target['description'][:60]}...",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": [f"circulatory_respiratory_anatomy_{target_key}_misconception"],
    }


# 01. Heart anatomy superior vena cava plate identification
def arch_01_heart_anatomy_superior_vena_cava_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "superior_vena_cava", "01_heart_anatomy_superior_vena_cava_plate_identification", "human heart")


# 02. Heart anatomy inferior vena cava plate identification
def arch_02_heart_anatomy_inferior_vena_cava_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "inferior_vena_cava", "02_heart_anatomy_inferior_vena_cava_plate_identification", "human heart")


# 03. Heart anatomy right atrium plate identification
def arch_03_heart_anatomy_right_atrium_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "right_atrium", "03_heart_anatomy_right_atrium_plate_identification", "human heart")


# 04. Heart anatomy right ventricle plate identification
def arch_04_heart_anatomy_right_ventricle_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "right_ventricle", "04_heart_anatomy_right_ventricle_plate_identification", "human heart")


# 05. Heart anatomy pulmonary artery plate identification
def arch_05_heart_anatomy_pulmonary_artery_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "pulmonary_artery", "05_heart_anatomy_pulmonary_artery_plate_identification", "human heart")


# 06. Heart anatomy pulmonary veins plate identification
def arch_06_heart_anatomy_pulmonary_veins_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "pulmonary_veins", "06_heart_anatomy_pulmonary_veins_plate_identification", "human heart")


# 07. Heart anatomy left atrium plate identification
def arch_07_heart_anatomy_left_atrium_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "left_atrium", "07_heart_anatomy_left_atrium_plate_identification", "human heart")


# 08. Heart anatomy left ventricle plate identification
def arch_08_heart_anatomy_left_ventricle_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "left_ventricle", "08_heart_anatomy_left_ventricle_plate_identification", "human heart")


# 09. Heart anatomy aorta plate identification
def arch_09_heart_anatomy_aorta_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "aorta", "09_heart_anatomy_aorta_plate_identification", "human heart")


# 10. Heart anatomy interventricular septum plate identification
def arch_10_heart_anatomy_interventricular_septum_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "heart", "interventricular_septum", "10_heart_anatomy_interventricular_septum_plate_identification", "human heart")


# 11. Alveolus anatomy lumen air space plate identification
def arch_11_alveolus_anatomy_lumen_air_space_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "alveolus_gas_exchange", "alveolar_lumen", "11_alveolus_anatomy_lumen_air_space_plate_identification", "alveolus gas exchange microstructure")


# 12. Alveolus anatomy squamous epithelium plate identification
def arch_12_alveolus_anatomy_squamous_epithelium_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "alveolus_gas_exchange", "alveolar_epithelium", "12_alveolus_anatomy_squamous_epithelium_plate_identification", "alveolus gas exchange microstructure")


# 13. Alveolus anatomy capillary endothelium plate identification
def arch_13_alveolus_anatomy_capillary_endothelium_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "alveolus_gas_exchange", "capillary_endothelium", "13_alveolus_anatomy_capillary_endothelium_plate_identification", "alveolus gas exchange microstructure")


# 14. Alveolus anatomy red blood cell erythrocyte plate identification
def arch_14_alveolus_anatomy_red_blood_cell_erythrocyte_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_plate_question(rng, "alveolus_gas_exchange", "red_blood_cell", "14_alveolus_anatomy_red_blood_cell_erythrocyte_plate_identification", "alveolus gas exchange microstructure")


# 15. Circulatory system double circulation pulmonary vs systemic circuit
def arch_15_circulatory_system_double_circulation_pulmonary_vs_systemic_circuit(rng: random.Random) -> Dict[str, Any]:
    circuits = [
        (
            "Pulmonary Circulation",
            "Right ventricle -> Pulmonary artery -> Alveolar capillaries of lungs (oxygenation/decarboxylation) -> Pulmonary veins -> Left atrium",
            "Pumps deoxygenated blood under lower pressure to delicate lung tissues for gas exchange",
        ),
        (
            "Systemic Circulation",
            "Left ventricle -> Aorta -> Systemic arteries, arterioles, and capillaries -> Venae cavae -> Right atrium",
            "Pumps oxygen-rich blood under high hydrostatic pressure throughout the entire body to supply all metabolic tissues",
        ),
    ]
    name, pathway, purpose = rng.choice(circuits)
    prompt = (
        f"Humans possess a closed, double circulatory system in which blood passes through the heart twice during each complete circuit.\n\n"
        f"Which anatomical pathway and physiological purpose defines the **{name}**?"
    )
    correct = f"Pathway: {pathway}.\nFunction: {purpose}."
    alt = [c for c in circuits if c[0] != name][0]
    options = [
        correct,
        f"Pathway: {alt[1]}.\nFunction: {alt[2]}.",
        "Pathway: Stomach -> Kidneys -> Brain -> Feet -> Lungs.\nFunction: Removes solid food waste from blood.",
        "Pathway: Spleen -> Pancreas -> Gallbladder -> Heart.\nFunction: Synthesizes bile inside heart chambers.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze closed double circulation pathways.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct pathway and function is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_15_{rng.randint(100000, 999999)}",
        "subskill": "15_circulatory_system_double_circulation_pulmonary_vs_systemic_circuit",
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
            "tier_1": f"Does {name} go to the lungs (pulmonary) or to the rest of the body (systemic)?",
            "tier_2": "Pulmonary: Right ventricle -> lungs -> Left atrium. Systemic: Left ventricle -> body -> Right atrium.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["double_circulation_pulmonary_vs_systemic_misconception"],
    }


# 16. Cardiac cycle atrial systole ventricular systole general diastole
def arch_16_cardiac_cycle_atrial_systole_ventricular_systole_general_diastole(rng: random.Random) -> Dict[str, Any]:
    phases = [
        (
            "Atrial Systole (~0.1 seconds)",
            "Both atria contract simultaneously; tricuspid and bicuspid (AV) valves are pushed wide open; remaining 20-30% of blood is forced into relaxed ventricles; semi-lunar valves remain closed",
        ),
        (
            "Ventricular Systole (~0.3 seconds)",
            "Both ventricles contract forcefully; high intraventricular pressure snaps AV valves shut ('lubb' first heart sound); semi-lunar valves open as blood surges into aorta and pulmonary artery",
        ),
        (
            "General Diastole (~0.4 seconds)",
            "Entire myocardium (atria and ventricles) relaxes; semi-lunar valves snap shut ('dubb' second heart sound) to prevent arterial backflow; blood passively flows from venae cavae and pulmonary veins into atria",
        ),
    ]
    phase_name, mechanics = rng.choice(phases)
    prompt = (
        f"The human cardiac cycle lasts approximately 0.8 seconds at a resting heart rate of ~75 beats per minute.\n\n"
        f"Which mechanical and valve events occur during **{phase_name}**?"
    )
    correct = mechanics
    distractors = [p[1] for p in phases if p[0] != phase_name]
    distractors.append("All four heart chambers contract together, squeezing all blood out through the skull.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze cardiac cycle phase events: {phase_name}.\n"
        f"**Step 2:** Note chamber states and valve actions:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate description is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_16_{rng.randint(100000, 999999)}",
        "subskill": "16_cardiac_cycle_atrial_systole_ventricular_systole_general_diastole",
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
            "tier_1": f"What happens to atria, ventricles, and valves during {phase_name.split()[0]}?",
            "tier_2": "Atrial systole: atria contract, AV open; Ventricular systole: ventricles contract, AV close (lubb), semilunar open; Diastole: whole heart relaxes, semilunar close (dubb).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cardiac_cycle_systole_diastole_valve_timing_misconception"],
    }


# 17. Heart valves tricuspid bicuspid semilunar preventing backflow
def arch_17_heart_valves_tricuspid_bicuspid_semilunar_preventing_backflow(rng: random.Random) -> Dict[str, Any]:
    valves = [
        (
            "Tricuspid valve (Right Atrioventricular valve)",
            "Located between right atrium and right ventricle",
            "Prevents backflow of deoxygenated blood from right ventricle into right atrium during ventricular systole",
        ),
        (
            "Bicuspid / Mitral valve (Left Atrioventricular valve)",
            "Located between left atrium and left ventricle",
            "Prevents backflow of oxygenated blood from left ventricle into left atrium under extreme systolic pressure",
        ),
        (
            "Aortic semi-lunar valve",
            "Located at the base of the aorta where it exits the left ventricle",
            "Prevents backflow of oxygenated blood from aorta back into left ventricle during diastole",
        ),
        (
            "Pulmonary semi-lunar valve",
            "Located at the base of the pulmonary artery where it exits the right ventricle",
            "Prevents backflow of deoxygenated blood from pulmonary trunk back into right ventricle during diastole",
        ),
    ]
    v_name, location, function = rng.choice(valves)
    prompt = (
        f"Heart valves ensure strictly unidirectional flow of blood through cardiac chambers and great vessels.\n\n"
        f"What is the anatomical location and physiological function of the **{v_name}**?"
    )
    correct = f"Location: {location}.\nFunction: {function}."
    alt = [v for v in valves if v[0] != v_name][0]
    options = [
        correct,
        f"Location: {alt[1]}.\nFunction: {alt[2]}.",
        "Location: Inside the femoral vein.\nFunction: Mixes arterial and venous blood to regulate body warmth.",
        "Location: Directly beneath the tongue.\nFunction: Filters saliva before entering the heart.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify heart valve: {v_name}.\n"
        f"**Step 2:** Relate to location and backflow prevention:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_17_{rng.randint(100000, 999999)}",
        "subskill": "17_heart_valves_tricuspid_bicuspid_semilunar_preventing_backflow",
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
            "tier_1": f"Where is the {v_name} situated in the heart?",
            "tier_2": "Tricuspid = right AV; Bicuspid = left AV; Semilunar = bases of pulmonary artery and aorta.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["heart_valves_anatomical_position_and_function_misconception"],
    }


# 18. Blood vessels structural comparison artery vein capillary wall thickness
def arch_18_blood_vessels_structural_comparison_artery_vein_capillary_wall_thickness(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Arteries",
            "Thick, muscular, and elastic tunica media containing elastin fibers; narrow lumen; withstands and dampens high systolic hydrostatic pressure waves from ventricular contractions",
        ),
        (
            "Veins",
            "Thin muscular wall with little elastic tissue; wide lumen offering low resistance to blood flow; contains semilunar pocket valves to prevent retrograde flow under low pressure",
        ),
        (
            "Capillaries",
            "Microscopic wall consisting of a single layer of flattened squamous endothelial cells with no muscle or elastic fibers; narrow lumen (~8 um) allowing red blood cells to pass single file for rapid diffusion",
        ),
    ]
    name, histology = rng.choice(types)
    prompt = (
        f"The vascular network comprises three distinct vessel types structurally adapted for their mechanical roles.\n\n"
        f"Which histological structure and mechanical adaptation characterizes **{name}**?"
    )
    correct = histology
    distractors = [t[1] for t in types if t[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare histology of blood vessels.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct histological adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_18_{rng.randint(100000, 999999)}",
        "subskill": "18_blood_vessels_structural_comparison_artery_vein_capillary_wall_thickness",
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
            "tier_1": f"Think about wall thickness, lumen size, and pressure in {name}.",
            "tier_2": "Arteries: thick elastic walls, narrow lumen, high pressure; Veins: thin walls, wide lumen, valves; Capillaries: 1 cell thick.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["blood_vessel_histological_comparison_misconception"],
    }


# 19. Blood vessel mechanics blood pressure pulse and valves in veins
def arch_19_blood_vessel_mechanics_blood_pressure_pulse_and_valves_in_veins(rng: random.Random) -> Dict[str, Any]:
    mechanics = [
        (
            "Blood pressure gradient",
            "Highest in systemic arteries (aorta ~120/80 mmHg), drops significantly across arterioles and capillary beds, and reaches near zero in great systemic veins (venae cavae)",
        ),
        (
            "The arterial pulse",
            "The rhythmic shockwave of expansion and elastic recoil of arterial walls transmitted along arteries with each left ventricular ejection of blood",
        ),
        (
            "Skeletal muscle pump and venous return",
            "Contraction of surrounding skeletal muscles compresses deep veins, forcing blood upward through open one-way pocket valves while backward flow is blocked by closing valves",
        ),
    ]
    concept, explanation = rng.choice(mechanics)
    prompt = (
        f"Hemodynamic principles govern blood movement through high-pressure arterial and low-pressure venous circuits.\n\n"
        f"Which statement accurately explains **{concept}**?"
    )
    correct = explanation
    distractors = [m[1] for m in mechanics if m[0] != concept]
    distractors.append("Venous blood flows strictly by anti-gravitational magnetic attraction toward the skull.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze hemodynamic principles.\n"
        f"**Step 2:** Relate to {concept}:\n"
        f"- {concept}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_19_{rng.randint(100000, 999999)}",
        "subskill": "19_blood_vessel_mechanics_blood_pressure_pulse_and_valves_in_veins",
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
            "tier_1": f"Consider how blood pressure, pulse, or venous return works: {concept}.",
            "tier_2": "Pressure drops from aorta to veins; pulse is arterial elastic recoil; skeletal muscle pump drives venous return past valves.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hemodynamic_pressure_gradient_and_venous_return_misconception"],
    }


# 20. Blood components plasma erythrocytes leukocytes platelets
def arch_20_blood_components_plasma_erythrocytes_leukocytes_platelets(rng: random.Random) -> Dict[str, Any]:
    fractions = [
        (
            "Plasma (~55% of blood volume)",
            "Straw-colored liquid matrix (90% water) transporting dissolved nutrients (glucose, amino acids), metabolic wastes (urea, CO2 as HCO3-), hormones, and plasma proteins (albumin, fibrinogen)",
        ),
        (
            "Erythrocytes (Red Blood Cells)",
            "Biconcave, anucleated cells packed with iron-containing hemoglobin molecules; specialized for carrying oxygen from lungs to systemic tissues",
        ),
        (
            "Leukocytes (White Blood Cells)",
            "Nucleated immune cells (phagocytes and lymphocytes) that defend the body against infectious microorganisms by engulfing pathogens or producing antibodies",
        ),
        (
            "Thrombocytes (Platelets)",
            "Small cell fragments derived from bone marrow megakaryocytes; initiate blood clotting (hemostasis) by clumping at vascular tears and triggering fibrin formation",
        ),
    ]
    name, role = rng.choice(fractions)
    prompt = (
        f"Human blood is a specialized fluid connective tissue consisting of cellular elements suspended in a liquid extracellular matrix.\n\n"
        f"What is the primary composition and physiological function of **{name}**?"
    )
    correct = role
    distractors = [f[1] for f in fractions if f[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze blood tissue components.\n"
        f"**Step 2:** Relate {name} to functional role:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct functional profile is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_20_{rng.randint(100000, 999999)}",
        "subskill": "20_blood_components_plasma_erythrocytes_leukocytes_platelets",
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
            "tier_1": f"Recall the role of {name}: transport, oxygen delivery, pathogen defense, or clotting?",
            "tier_2": "Plasma = transport fluid; RBCs = oxygen; WBCs = immunity; Platelets = blood clotting.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["blood_components_cellular_fractions_and_plasma_misconception"],
    }


# 21. Respiratory system tract nasal cavity pharynx larynx trachea bronchi
def arch_21_respiratory_system_tract_nasal_cavity_pharynx_larynx_trachea_bronchi(rng: random.Random) -> Dict[str, Any]:
    structures = [
        (
            "Nasal Cavity",
            "Lined with vascular mucous membrane and hairs that warm, moisten, and filter inhaled air before it enters lower respiratory passages",
        ),
        (
            "Epiglottis and Larynx",
            "Cartilaginous flap that snaps down over the glottis during swallowing to prevent food/liquid from entering the airway, housing vocal cords for phonation",
        ),
        (
            "Trachea (Windpipe)",
            "Flexible tube reinforced with C-shaped rings of hyaline cartilage that prevent airway collapse during pressure drops of inhalation while allowing esophageal expansion",
        ),
        (
            "Bronchi and Bronchioles",
            "Branching airway tree conducting air into lobes of both lungs, terminating in clusters of microscopic alveoli",
        ),
    ]
    name, role = rng.choice(structures)
    prompt = (
        f"Inhaled atmospheric air travels through a sequence of conducting respiratory structures before reaching the respiratory zone.\n\n"
        f"Which anatomical adaptation and protective function defines the **{name}**?"
    )
    correct = role
    distractors = [s[1] for s in structures if s[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review anatomical pathway of inhaled air.\n"
        f"**Step 2:** Relate {name} to structural features:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct functional adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_21_{rng.randint(100000, 999999)}",
        "subskill": "21_respiratory_system_tract_nasal_cavity_pharynx_larynx_trachea_bronchi",
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
            "tier_1": f"Recall the structural adaptation of the {name}.",
            "tier_2": "Nasal cavity warms/filters; epiglottis covers trachea when swallowing; C-shaped cartilage keeps trachea open.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiratory_tract_conducting_zone_anatomy_misconception"],
    }


# 22. Ciliated epithelial mucociliary escalator and goblet cells
def arch_22_ciliated_epithelial_mucociliary_escalator_and_goblet_cells(rng: random.Random) -> Dict[str, Any]:
    cells = [
        (
            "Goblet cells",
            "Specialized epithelial gland cells that secrete sticky mucus to trap inhaled airborne dust particles, pollen, soot, and pathogens",
        ),
        (
            "Ciliated epithelial cells",
            "Possess thousands of apical hair-like cilia beating rhythmically upward (mucociliary escalator) to sweep mucus toward the pharynx to be swallowed or expectorated",
        ),
        (
            "Impact of cigarette smoke and airborne pollutants",
            "Chemical irritants paralyze and destroy cilia, leading to mucus accumulation, chronic cough ('smoker's cough'), and recurrent bacterial respiratory infections",
        ),
    ]
    name, mechanism = rng.choice(cells)
    prompt = (
        f"The respiratory conducting passages are lined with pseudostratified ciliated columnar epithelium.\n\n"
        f"What is the specialized physiological role of **{name}** in airway defense?"
    )
    correct = mechanism
    distractors = [c[1] for c in cells if c[0] != name]
    distractors.append("Produces hydrochloric acid to digest food boluses inside the lungs.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze airway epithelial cleaning mechanisms.\n"
        f"**Step 2:** Relate {name} to mucociliary escalator defense:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_22_{rng.randint(100000, 999999)}",
        "subskill": "22_ciliated_epithelial_mucociliary_escalator_and_goblet_cells",
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
            "tier_1": f"Think about how mucus and cilia work together: {name}.",
            "tier_2": "Goblet cells trap dirt in mucus; cilia sweep mucus up and out of the lungs; smoking paralyzes cilia.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mucociliary_escalator_goblet_cells_cilia_action_misconception"],
    }


# 23. Ventilation mechanics inhalation diaphragm intercostals thoracic volume
def arch_23_ventilation_mechanics_inhalation_diaphragm_intercostals_thoracic_volume(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During active inhalation (inspiration), muscular actions alter the volume and internal pressure of the thoracic cavity.\n\n"
        f"Which sequence of physiological events accurately describes the mechanical process of **inhalation**?"
    )
    correct = (
        "Diaphragm contracts and flattens downwards; external intercostal muscles contract pulling ribs upwards and outwards; "
        "thoracic cavity volume increases; intra-pulmonary pressure drops below atmospheric pressure; air rushes into lungs along the pressure gradient."
    )
    wrong1 = (
        "Diaphragm relaxes and domes upwards; intercostal muscles relax pulling ribs downwards; "
        "thoracic cavity volume decreases; internal pressure increases; air is forced out of lungs."
    )
    wrong2 = (
        "Lungs actively expand their muscular walls using peristalsis to pump air through the ribs without any muscle movements."
    )
    wrong3 = (
        "Diaphragm turns sideways while ribs clamp tightly together, compressing the lungs so that atmospheric air is vacuumed through the skin."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the mechanics of inhalation (Boyle's law: Volume increases -> Pressure decreases):\n"
        f"1. Diaphragm contracts -> moves down (flattens).\n"
        f"2. External intercostals contract -> ribs move up and out.\n"
        f"3. Thoracic volume increases -> internal lung pressure decreases below atmospheric pressure.\n"
        f"4. Air rushes in from high atmospheric pressure to low intra-pulmonary pressure.\n\n"
        f"**Step 2:** The correct sequence is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_23_{rng.randint(100000, 999999)}",
        "subskill": "23_ventilation_mechanics_inhalation_diaphragm_intercostals_thoracic_volume",
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
            "tier_1": "Does the diaphragm contract (flatten) or relax (dome up) during inhalation?",
            "tier_2": "Inhalation: diaphragm contracts and flattens, ribs move up/out, volume increases, pressure drops, air enters.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["inhalation_ventilation_mechanics_pressure_volume_misconception"],
    }


# 24. Ventilation mechanics exhalation elastic recoil and pressure gradients
def arch_24_ventilation_mechanics_exhalation_elastic_recoil_and_pressure_gradients(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During quiet, resting exhalation (expiration), the muscles of ventilation relax.\n\n"
        f"Which sequence of physiological events accurately describes the mechanical process of **resting exhalation**?"
    )
    correct = (
        "Diaphragm relaxes and curves upwards into a dome shape; external intercostal muscles relax allowing ribs to move downwards and inwards; "
        "thoracic cavity volume decreases; elastic lung tissue recoils; intra-pulmonary pressure rises above atmospheric pressure; air is pushed out of lungs."
    )
    wrong1 = (
        "Diaphragm contracts violently and flattens downwards; intercostal muscles pull ribs outwards; "
        "thoracic volume increases; pressure drops; air enters the lungs."
    )
    wrong2 = (
        "Internal organs contract to squeeze the stomach into the trachea, physically expelling digestive gases through the nose."
    )
    wrong3 = (
        "The ribs detach from the sternum to let air escape directly through the chest wall into the atmosphere."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze resting exhalation mechanics (Passive process):\n"
        f"1. Diaphragm relaxes -> arches up into a dome.\n"
        f"2. External intercostals relax -> ribs move down and in.\n"
        f"3. Thoracic cavity volume decreases -> internal pressure increases above atmospheric pressure.\n"
        f"4. Air is driven out down the pressure gradient.\n\n"
        f"**Step 2:** The correct sequence is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_24_{rng.randint(100000, 999999)}",
        "subskill": "24_ventilation_mechanics_exhalation_elastic_recoil_and_pressure_gradients",
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
            "tier_1": "Recall: Exhalation is passive at rest. Muscles relax and lung volume decreases.",
            "tier_2": "Diaphragm relaxes (domes up), ribs move down/in, volume decreases, pressure rises, air exits.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["exhalation_ventilation_mechanics_pressure_volume_misconception"],
    }


# 25. Alveolar gas exchange partial pressures oxygen carbon dioxide diffusion
def arch_25_alveolar_gas_exchange_partial_pressures_oxygen_carbon_dioxide_diffusion(rng: random.Random) -> Dict[str, Any]:
    gases = [
        (
            "Oxygen (O2) diffusion gradient",
            "Inhaled alveolar air has high pO2 (~104 mmHg) while deoxygenated blood entering pulmonary capillaries has low pO2 (~40 mmHg); O2 dissolves in moisture and diffuses down its concentration gradient into blood, binding to hemoglobin",
        ),
        (
            "Carbon dioxide (CO2) diffusion gradient",
            "Deoxygenated capillary blood has high pCO2 (~45 mmHg) while alveolar air has low pCO2 (~40 mmHg); CO2 diffuses down its partial pressure gradient across endothelial and epithelial layers into alveolar lumen to be exhaled",
        ),
        (
            "Fick's law of diffusion adaptations",
            "Gas exchange is maximized by an enormous collective alveolar surface area (~70-100 m²), an ultra-thin barrier (<1 um), and continuous capillary blood flow maintaining steep concentration gradients",
        ),
    ]
    name, mechanism = rng.choice(gases)
    prompt = (
        f"Gas exchange across the respiratory membrane in the alveoli occurs strictly via passive diffusion.\n\n"
        f"Which statement accurately explains the biophysical mechanism of: **{name}**?"
    )
    correct = mechanism
    distractors = [g[1] for g in gases if g[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze alveolar gas exchange dynamics.\n"
        f"**Step 2:** Relate {name} to diffusion physics:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_25_{rng.randint(100000, 999999)}",
        "subskill": "25_alveolar_gas_exchange_partial_pressures_oxygen_carbon_dioxide_diffusion",
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
            "tier_1": f"Which direction does {name.split()[0]} move between alveolar air and capillary blood?",
            "tier_2": "O2 moves from high alveolar air into low capillary blood; CO2 moves from high blood into alveolar air to be exhaled.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["alveolar_gas_exchange_partial_pressure_diffusion_gradients_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_heart_anatomy_superior_vena_cava_plate_identification": arch_01_heart_anatomy_superior_vena_cava_plate_identification,
    "02_heart_anatomy_inferior_vena_cava_plate_identification": arch_02_heart_anatomy_inferior_vena_cava_plate_identification,
    "03_heart_anatomy_right_atrium_plate_identification": arch_03_heart_anatomy_right_atrium_plate_identification,
    "04_heart_anatomy_right_ventricle_plate_identification": arch_04_heart_anatomy_right_ventricle_plate_identification,
    "05_heart_anatomy_pulmonary_artery_plate_identification": arch_05_heart_anatomy_pulmonary_artery_plate_identification,
    "06_heart_anatomy_pulmonary_veins_plate_identification": arch_06_heart_anatomy_pulmonary_veins_plate_identification,
    "07_heart_anatomy_left_atrium_plate_identification": arch_07_heart_anatomy_left_atrium_plate_identification,
    "08_heart_anatomy_left_ventricle_plate_identification": arch_08_heart_anatomy_left_ventricle_plate_identification,
    "09_heart_anatomy_aorta_plate_identification": arch_09_heart_anatomy_aorta_plate_identification,
    "10_heart_anatomy_interventricular_septum_plate_identification": arch_10_heart_anatomy_interventricular_septum_plate_identification,
    "11_alveolus_anatomy_lumen_air_space_plate_identification": arch_11_alveolus_anatomy_lumen_air_space_plate_identification,
    "12_alveolus_anatomy_squamous_epithelium_plate_identification": arch_12_alveolus_anatomy_squamous_epithelium_plate_identification,
    "13_alveolus_anatomy_capillary_endothelium_plate_identification": arch_13_alveolus_anatomy_capillary_endothelium_plate_identification,
    "14_alveolus_anatomy_red_blood_cell_erythrocyte_plate_identification": arch_14_alveolus_anatomy_red_blood_cell_erythrocyte_plate_identification,
    "15_circulatory_system_double_circulation_pulmonary_vs_systemic_circuit": arch_15_circulatory_system_double_circulation_pulmonary_vs_systemic_circuit,
    "16_cardiac_cycle_atrial_systole_ventricular_systole_general_diastole": arch_16_cardiac_cycle_atrial_systole_ventricular_systole_general_diastole,
    "17_heart_valves_tricuspid_bicuspid_semilunar_preventing_backflow": arch_17_heart_valves_tricuspid_bicuspid_semilunar_preventing_backflow,
    "18_blood_vessels_structural_comparison_artery_vein_capillary_wall_thickness": arch_18_blood_vessels_structural_comparison_artery_vein_capillary_wall_thickness,
    "19_blood_vessel_mechanics_blood_pressure_pulse_and_valves_in_veins": arch_19_blood_vessel_mechanics_blood_pressure_pulse_and_valves_in_veins,
    "20_blood_components_plasma_erythrocytes_leukocytes_platelets": arch_20_blood_components_plasma_erythrocytes_leukocytes_platelets,
    "21_respiratory_system_tract_nasal_cavity_pharynx_larynx_trachea_bronchi": arch_21_respiratory_system_tract_nasal_cavity_pharynx_larynx_trachea_bronchi,
    "22_ciliated_epithelial_mucociliary_escalator_and_goblet_cells": arch_22_ciliated_epithelial_mucociliary_escalator_and_goblet_cells,
    "23_ventilation_mechanics_inhalation_diaphragm_intercostals_thoracic_volume": arch_23_ventilation_mechanics_inhalation_diaphragm_intercostals_thoracic_volume,
    "24_ventilation_mechanics_exhalation_elastic_recoil_and_pressure_gradients": arch_24_ventilation_mechanics_exhalation_elastic_recoil_and_pressure_gradients,
    "25_alveolar_gas_exchange_partial_pressures_oxygen_carbon_dioxide_diffusion": arch_25_alveolar_gas_exchange_partial_pressures_oxygen_carbon_dioxide_diffusion,
}
