"""Grade 9 Natural Sciences: Term 1 - Digestive System (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md & digestive curriculum requirements.
Focus: Curated Campbell organ plates (Digestive System & Intestinal Villus), core digestive processes, mechanical vs chemical digestion, enzymes, gastric/pancreatic secretions, and absorption.
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


DIGESTIVE_DATA = _load_anchors("digestive_system")
VILLUS_DATA = _load_anchors("intestinal_villus")


def _make_digestive_plate_question(
    rng: random.Random,
    master: str,
    target_key: str,
    subskill_id: str,
    system_label: str,
) -> Dict[str, Any]:
    anchor_data = DIGESTIVE_DATA if master == "digestive_system" else VILLUS_DATA
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
        "view": anchor_data.get("view", "coronal_alimentary_canal"),
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
        "id": f"ns9_dig_{subskill_id[:2]}_{rng.randint(100000, 999999)}",
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
        "misconception_tags": [f"digestive_anatomy_plate_{target_key}_misconception"],
    }


# 01. Digestive mouth oral cavity plate identification
def arch_01_digestive_mouth_oral_cavity_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "mouth", "01_digestive_mouth_oral_cavity_plate_identification", "human digestive tract")


# 02. Digestive esophagus peristalsis plate identification
def arch_02_digestive_esophagus_peristalsis_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "esophagus", "02_digestive_esophagus_peristalsis_plate_identification", "human digestive tract")


# 03. Digestive stomach gastric juice plate identification
def arch_03_digestive_stomach_gastric_juice_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "stomach", "03_digestive_stomach_gastric_juice_plate_identification", "human digestive tract")


# 04. Digestive liver bile secretion plate identification
def arch_04_digestive_liver_bile_secretion_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "liver", "04_digestive_liver_bile_secretion_plate_identification", "human digestive tract")


# 05. Digestive pancreas pancreatic juice plate identification
def arch_05_digestive_pancreas_pancreatic_juice_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "pancreas", "05_digestive_pancreas_pancreatic_juice_plate_identification", "human digestive tract")


# 06. Digestive small intestine duodenum ileum plate identification
def arch_06_digestive_small_intestine_duodenum_ileum_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "small_intestine", "06_digestive_small_intestine_duodenum_ileum_plate_identification", "human digestive tract")


# 07. Digestive large intestine colon water reabsorption plate identification
def arch_07_digestive_large_intestine_colon_water_reabsorption_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "large_intestine", "07_digestive_large_intestine_colon_water_reabsorption_plate_identification", "human digestive tract")


# 08. Digestive rectum anus egestion plate identification
def arch_08_digestive_rectum_anus_egestion_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "digestive_system", "rectum", "08_digestive_rectum_anus_egestion_plate_identification", "human digestive tract")


# 09. Villus microvilli brush border plate identification
def arch_09_villus_microvilli_brush_border_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "intestinal_villus", "microvilli", "09_villus_microvilli_brush_border_plate_identification", "intestinal villus histology")


# 10. Villus columnar epithelium thin barrier plate identification
def arch_10_villus_columnar_epithelium_thin_barrier_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "intestinal_villus", "columnar_epithelium", "10_villus_columnar_epithelium_thin_barrier_plate_identification", "intestinal villus histology")


# 11. Villus goblet cell mucus protection plate identification
def arch_11_villus_goblet_cell_mucus_protection_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "intestinal_villus", "goblet_cell", "11_villus_goblet_cell_mucus_protection_plate_identification", "intestinal villus histology")


# 12. Villus central lacteal lipid absorption plate identification
def arch_12_villus_central_lacteal_lipid_absorption_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "intestinal_villus", "lacteal", "12_villus_central_lacteal_lipid_absorption_plate_identification", "intestinal villus histology")


# 13. Villus capillary network glucose amino acid transport plate identification
def arch_13_villus_capillary_network_glucose_amino_acid_transport_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_digestive_plate_question(rng, "intestinal_villus", "capillary_network", "13_villus_capillary_network_glucose_amino_acid_transport_plate_identification", "intestinal villus histology")


# 14. Four digestive processes ingestion digestion absorption egestion
def arch_14_four_digestive_processes_ingestion_digestion_absorption_egestion(rng: random.Random) -> Dict[str, Any]:
    processes = [
        ("Ingestion", "The physiological intake of solid food or liquids into the mouth and alimentary canal"),
        ("Digestion", "The breakdown of large, complex, insoluble food polymers into small, simple, soluble monomers via mechanical and chemical actions"),
        ("Absorption", "The passage of digested soluble nutrient molecules across the epithelial lining of the small intestine into blood capillaries and lacteals"),
        ("Egestion (Defecation)", "The elimination of undigested and unabsorbed food residues and dietary fiber from the body as feces through the anus"),
    ]
    name, definition = rng.choice(processes)
    prompt = (
        f"The human digestive tract performs four fundamental, sequential physiological functions.\n\n"
        f"Which definition accurately describes the biological process of **{name}**?"
    )
    correct = definition
    distractors = [p[1] for p in processes if p[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review four stages of food processing: Ingestion -> Digestion -> Absorption -> Egestion.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct definition is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_14_{rng.randint(100000, 999999)}",
        "subskill": "14_four_digestive_processes_ingestion_digestion_absorption_egestion",
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
            "tier_1": f"Think about where and what occurs during {name}.",
            "tier_2": "Ingestion = intake; Digestion = breakdown; Absorption = uptake into blood; Egestion = removal of undigested waste.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["four_digestive_processes_sequence_and_definitions_misconception"],
    }


# 15. Mechanical digestion mastication teeth churning peristalsis
def arch_15_mechanical_digestion_mastication_teeth_churning_peristalsis(rng: random.Random) -> Dict[str, Any]:
    mechanisms = [
        (
            "Mastication (Chewing)",
            "Teeth cut, tear, and grind food into smaller particles while the tongue mixes it with saliva to form a moist bolus, vastly multiplying surface area for enzyme action",
        ),
        (
            "Peristalsis",
            "Involuntary, rhythmic waves of contraction of circular muscles behind the bolus and longitudinal muscles ahead, propelling food along the alimentary canal",
        ),
        (
            "Gastric Churning",
            "Vigorous contractions of three smooth muscle layers in the stomach wall that physically smash and liquefy food boluses with gastric juice into semi-liquid chyme",
        ),
        (
            "Bile Emulsification",
            "Physical dispersal of large dietary fat globules into microscopic droplets (micelles), providing an enormous surface area for water-soluble lipase enzymes",
        ),
    ]
    name, role = rng.choice(mechanisms)
    prompt = (
        f"Mechanical digestion physically breaks down food without cleaving covalent chemical bonds.\n\n"
        f"What is the mechanical mechanism and physiological purpose of **{name}**?"
    )
    correct = role
    distractors = [m[1] for m in mechanisms if m[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze mechanical digestion modes.\n"
        f"**Step 2:** Relate {name} to physical breakdown:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_15_{rng.randint(100000, 999999)}",
        "subskill": "15_mechanical_digestion_mastication_teeth_churning_peristalsis",
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
            "tier_1": f"How does {name} physically break down food or increase surface area?",
            "tier_2": "Mechanical digestion crushes, churns, emulsifies, or moves food without breaking chemical bonds.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mechanical_digestion_surface_area_peristalsis_misconception"],
    }


# 16. Chemical digestion enzymatic hydrolysis lock and key hypothesis
def arch_16_chemical_digestion_enzymatic_hydrolysis_lock_and_key_hypothesis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Chemical digestion relies on hydrolytic biological catalysts (enzymes) operating under the 'lock and key' model.\n\n"
        f"Which statement accurately explains how enzymes facilitate chemical digestion according to this model?"
    )
    correct = (
        "Each digestive enzyme has a specifically shaped active site ('lock') complementary only to a specific substrate molecule ('key'); "
        "binding forms an enzyme-substrate complex that lowers activation energy to catalyze hydrolysis into simpler soluble monomers without altering the enzyme."
    )
    wrong1 = (
        "Enzymes are living micro-organisms that eat substrate molecules and turn into blood cells inside the stomach."
    )
    wrong2 = (
        "A single universal enzyme breaks down all proteins, carbohydrates, and fats simultaneously regardless of molecular shape."
    )
    wrong3 = (
        "Enzymes are permanently destroyed and consumed with each single molecule of food they break down."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze enzyme action and substrate specificity:\n"
        f"- Active site (lock) is geometrically complementary to the substrate (key).\n"
        f"- Enzymes lower activation energy for hydrolysis reactions.\n"
        f"- Enzymes are reusable biological catalysts that remain unchanged after reaction.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_16_{rng.randint(100000, 999999)}",
        "subskill": "16_chemical_digestion_enzymatic_hydrolysis_lock_and_key_hypothesis",
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
            "tier_1": "Recall the lock-and-key model of enzyme specificity.",
            "tier_2": "The active site fits the substrate like a lock and key, lowering activation energy without being consumed.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["enzyme_lock_and_key_substrate_specificity_misconception"],
    }


# 17. Digestive enzymes carbohydrases salivary amylase maltase
def arch_17_digestive_enzymes_carbohydrases_salivary_amylase_maltase(rng: random.Random) -> Dict[str, Any]:
    carbohydrases = [
        (
            "Salivary Amylase (Ptyalin)",
            "Salivary glands into mouth (pH ~6.8 - 7.0)",
            "Starch (complex polysaccharide)",
            "Maltose (disaccharide)",
        ),
        (
            "Pancreatic Amylase",
            "Pancreas into duodenum (pH ~7.5 - 8.0)",
            "Undigested starch",
            "Maltose disaccharides",
        ),
        (
            "Maltase",
            "Small intestine brush border lining",
            "Maltose",
            "Glucose monomers (simple monosaccharides)",
        ),
    ]
    name, site, substrate, product = rng.choice(carbohydrases)
    prompt = (
        f"Carbohydrates provide the primary metabolic energy substrate for cellular respiration in humans.\n\n"
        f"What is the secretory origin, operating site, substrate, and end-product of **{name}**?"
    )
    correct = f"Site of action: {site}.\nSubstrate: {substrate} -> End-product: {product}."
    alt = [c for c in carbohydrases if c[0] != name][0]
    options = [
        correct,
        f"Site of action: {alt[1]}.\nSubstrate: {alt[2]} -> End-product: {alt[3]}.",
        "Site of action: Gallbladder.\nSubstrate: Nucleic acids -> End-product: Pure sulfuric acid.",
        "Site of action: Rectum.\nSubstrate: Carbon dioxide -> End-product: Liquid calcium.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze carbohydrate breakdown pathway:\n"
        f"- Starch -> Maltose (by salivary/pancreatic amylase).\n"
        f"- Maltose -> Glucose (by maltase on brush border).\n\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_17_{rng.randint(100000, 999999)}",
        "subskill": "17_digestive_enzymes_carbohydrases_salivary_amylase_maltase",
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
            "tier_1": f"Where does {name} act, and does it turn starch into maltose or maltose into glucose?",
            "tier_2": "Amylase converts starch to maltose; maltase converts maltose to glucose.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["carbohydrase_amylase_maltase_substrate_product_misconception"],
    }


# 18. Digestive enzymes proteases pepsin trypsin amino acids
def arch_18_digestive_enzymes_proteases_pepsin_trypsin_amino_acids(rng: random.Random) -> Dict[str, Any]:
    proteases = [
        (
            "Pepsin",
            "Gastric glands in stomach wall; activated by hydrochloric acid (pH 1.5 - 2.0)",
            "Proteins (polypeptides)",
            "Shorter peptide chains and peptones",
        ),
        (
            "Trypsin",
            "Exocrine pancreas into duodenum (neutral/alkaline pH 7.5 - 8.0)",
            "Peptides and remaining proteins",
            "Shorter oligopeptides and dipeptides",
        ),
        (
            "Peptidases (Erepsin)",
            "Small intestine epithelial brush border",
            "Dipeptides and tripeptides",
            "Individual amino acid monomers",
        ),
    ]
    name, site, substrate, product = rng.choice(proteases)
    prompt = (
        f"Proteins are essential for tissue growth, repair, and synthesis of enzymes and hormones.\n\n"
        f"What is the operational environment, substrate, and end-product of **{name}**?"
    )
    correct = f"Site & environment: {site}.\nSubstrate: {substrate} -> End-product: {product}."
    alt = [p for p in proteases if p[0] != name][0]
    options = [
        correct,
        f"Site & environment: {alt[1]}.\nSubstrate: {alt[2]} -> End-product: {alt[3]}.",
        "Site & environment: Inside the heart at pH 12.\nSubstrate: Glycogen -> End-product: Pure water.",
        "Site & environment: Salivary glands at pH 3.\nSubstrate: Saturated fats -> End-product: Bile salts.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace protein digestion hierarchy:\n"
        f"- Proteins -> Peptides (Pepsin in acidic stomach).\n"
        f"- Peptides -> Dipeptides (Trypsin in alkaline duodenum).\n"
        f"- Dipeptides -> Amino acids (Peptidases on small intestine border).\n\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct profile is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_18_{rng.randint(100000, 999999)}",
        "subskill": "18_digestive_enzymes_proteases_pepsin_trypsin_amino_acids",
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
            "tier_1": f"Where does {name} operate: stomach (acidic) or duodenum (alkaline)?",
            "tier_2": "Pepsin operates in acidic stomach; trypsin operates in alkaline duodenum; final monomers are amino acids.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["protease_pepsin_trypsin_ph_amino_acids_misconception"],
    }


# 19. Digestive enzymes lipases bile salts emulsification lipids
def arch_19_digestive_enzymes_lipases_bile_salts_emulsification_lipids(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Lipids (fats and oils) are hydrophobic water-insoluble molecules that require coordinated processing by the liver and pancreas.\n\n"
        f"How do **bile salts** and **pancreatic lipase** cooperate to achieve lipid digestion?"
    )
    correct = (
        "Bile salts mechanically emulsify large lipid droplets into microscopic micelles (multiplying available surface area without chemical digestion); "
        "pancreatic lipase then chemically hydrolyzes each triglyceride molecule into one glycerol molecule and three fatty acids."
    )
    wrong1 = (
        "Bile salts chemically digest fats into glucose, while lipase acts as a detergent that washes fats out of the blood."
    )
    wrong2 = (
        "Lipase freezes fat into solid wax, while bile salts melt the wax into stomach acid."
    )
    wrong3 = (
        "Lipids cannot be digested in humans and are absorbed as intact solid butter chunks directly into brain cells."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze lipid digestion sequence:\n"
        f"- Bile salts (from liver/gallbladder): Mechanical emulsification -> increases surface area.\n"
        f"- Pancreatic lipase: Chemical hydrolysis -> 1 Glycerol + 3 Fatty Acids.\n\n"
        f"**Step 2:** The correct cooperative mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_19_{rng.randint(100000, 999999)}",
        "subskill": "19_digestive_enzymes_lipases_bile_salts_emulsification_lipids",
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
            "tier_1": "Does bile digest chemically or emulsify mechanically? What does lipase break fats into?",
            "tier_2": "Bile emulsifies fats mechanically; lipase breaks triglycerides into glycerol and fatty acids.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lipid_digestion_bile_emulsification_lipase_glycerol_misconception"],
    }


# 20. Gastric juice hydrochloric acid pepsinogen mucus barrier
def arch_20_gastric_juice_hydrochloric_acid_pepsinogen_mucus_barrier(rng: random.Random) -> Dict[str, Any]:
    components = [
        (
            "Hydrochloric Acid (HCl)",
            "Parietal cells",
            "Creates a strongly acidic pH (~1.5 - 2.0) that destroys ingested pathogens, denatures dietary proteins, and activates inactive pepsinogen into active pepsin",
        ),
        (
            "Pepsinogen (inactive zymogen)",
            "Chief (zymogenic) cells",
            "Secreted as an inactive precursor to prevent self-digestion of gastric cellular proteins; converted into active pepsin upon contact with HCl in the stomach lumen",
        ),
        (
            "Gastric Mucus barrier",
            "Mucous neck cells",
            "Forms an alkaline bicarbonate-rich protective barrier lining the gastric mucosa, shielding stomach epithelial cells from corrosive acid and pepsin auto-digestion",
        ),
    ]
    name, source, role = rng.choice(components)
    prompt = (
        f"Gastric juice secreted by specialized cells in the gastric glands is highly specialized and chemically potent.\n\n"
        f"What is the secretory cell source and physiological function of **{name}**?"
    )
    correct = f"Source: {source}.\nFunction: {role}."
    alt = [c for c in components if c[0] != name][0]
    options = [
        correct,
        f"Source: {alt[1]}.\nFunction: {alt[2]}.",
        "Source: Red blood cells.\nFunction: Dissolves calcium from teeth during swallowing.",
        "Source: Hypothalamus.\nFunction: Pumps pure oxygen directly into the duodenum.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze gastric gland cytology:\n"
        f"- Parietal cells: produce HCl.\n"
        f"- Chief cells: produce pepsinogen.\n"
        f"- Mucous cells: produce protective alkaline mucus.\n\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_20_{rng.randint(100000, 999999)}",
        "subskill": "20_gastric_juice_hydrochloric_acid_pepsinogen_mucus_barrier",
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
            "tier_1": f"Why does the stomach produce {name}?",
            "tier_2": "HCl kills germs and activates pepsinogen; pepsinogen breaks down proteins; mucus protects stomach wall from acid.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gastric_juice_hcl_pepsinogen_mucus_function_misconception"],
    }


# 21. Pancreatic juice bicarbonate neutralization and enzymes
def arch_21_pancreatic_juice_bicarbonate_neutralization_and_enzymes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Acidic chyme leaving the stomach enters the duodenum where it is met by secretions from the exocrine pancreas.\n\n"
        f"What is the dual physiological purpose of **pancreatic juice** in the duodenum?"
    )
    correct = (
        "1. Sodium bicarbonate (NaHCO3) neutralizes acidic gastric chyme, raising pH to ~7.5-8.0 to protect duodenal mucosa and optimize enzyme action;\n"
        "2. Delivers a comprehensive enzyme suite: pancreatic amylase (starch), trypsin (proteins), and pancreatic lipase (lipids)."
    )
    wrong1 = (
        "1. Adds extra hydrochloric acid to burn through food bones;\n"
        "2. Produces insulin directly into the gut lumen to digest table sugar."
    )
    wrong2 = (
        "1. Absorbs all liquid water, turning chyme into solid dry powder;\n"
        "2. Destroys all intestinal villi to prevent nutrient absorption."
    )
    wrong3 = (
        "1. Synthesizes red blood cells to carry bile;\n"
        "2. Neutralizes glucose into dietary fiber."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze pancreatic juice components:\n"
        f"- Bicarbonate (NaHCO3): Neutralizes acid chyme (creates optimal pH 7.5-8.0).\n"
        f"- Enzymes: Amylase, Trypsin, Lipase.\n\n"
        f"**Step 2:** The correct dual purpose is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_21_{rng.randint(100000, 999999)}",
        "subskill": "21_pancreatic_juice_bicarbonate_neutralization_and_enzymes",
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
            "tier_1": "Why must stomach acid be neutralized in the duodenum, and what enzymes does the pancreas supply?",
            "tier_2": "Bicarbonate neutralizes stomach acid; pancreatic juice supplies amylase, trypsin, and lipase.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pancreatic_juice_bicarbonate_neutralization_enzymes_misconception"],
    }


# 22. Bile synthesis gallbladder storage emulsification mechanism
def arch_22_bile_synthesis_gallbladder_storage_emulsification_mechanism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Bile is an alkaline yellowish-green fluid that plays a critical role in digestion.\n\n"
        f"Where is bile synthesized, where is it stored and concentrated, and does it contain digestive enzymes?"
    )
    correct = (
        "Synthesized by hepatocytes in the liver; stored and concentrated in the gallbladder; "
        "released via the common bile duct into the duodenum; contains bile salts and pigments (bilirubin) but contains zero digestive enzymes."
    )
    wrong1 = (
        "Synthesized in the gallbladder; stored in the stomach; contains high concentrations of pepsin enzymes."
    )
    wrong2 = (
        "Synthesized in the pancreas; stored in the spleen; contains pure hydrochloric acid."
    )
    wrong3 = (
        "Synthesized in salivary glands; stored in the appendix; digests complex dietary fiber into vitamins."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Note origins and storage of bile:\n"
        f"- Site of synthesis: Liver.\n"
        f"- Site of storage/concentration: Gallbladder.\n"
        f"- Enzymatic content: ZERO digestive enzymes (acts purely mechanically via emulsification).\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_22_{rng.randint(100000, 999999)}",
        "subskill": "22_bile_synthesis_gallbladder_storage_emulsification_mechanism",
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
            "tier_1": "Which organ MAKES bile, which organ STORES it, and are there enzymes in bile?",
            "tier_2": "Liver synthesizes bile; gallbladder stores it; bile contains NO digestive enzymes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bile_synthesis_liver_vs_gallbladder_storage_no_enzymes_misconception"],
    }


# 23. Small intestine structural adaptations for absorption
def arch_23_small_intestine_structural_adaptations_for_absorption(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The human small intestine (approximately 6 meters in length) is supremely adapted for efficient nutrient absorption.\n\n"
        f"Which structural features provide a massive absorptive surface area and rapid transport of nutrients?"
    )
    correct = (
        "1. Circular folds (plicae circulares) that slow chyme transit;\n"
        "2. Millions of finger-like villi projecting into the lumen;\n"
        "3. Dense brush border of microscopic microvilli on enterocytes (total surface area ~250-300 m²);\n"
        "4. Extremely thin, single-cell epithelial lining and rich capillary and lacteal networks in each villus."
    )
    wrong1 = (
        "Thick, smooth bone lining with zero folds to allow food to slide through in less than 5 seconds without touching blood."
    )
    wrong2 = (
        "A completely closed muscular tube with zero blood vessels that stores food for 3 weeks."
    )
    wrong3 = (
        "Large external gills that exchange gases directly with the room atmosphere through the abdominal wall."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze small intestine surface area amplification:\n"
        f"- Plicae circulares (folds) x3.\n"
        f"- Villi x10.\n"
        f"- Microvilli (brush border) x20.\n"
        f"- Combined surface area: ~250-300 m² (size of a tennis court).\n"
        f"- Thin 1-cell epithelium + dense capillary/lacteal networks for fast diffusion.\n\n"
        f"**Step 2:** The correct suite of structural adaptations is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_23_{rng.randint(100000, 999999)}",
        "subskill": "23_small_intestine_structural_adaptations_for_absorption",
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
            "tier_1": "Recall the 3 levels of surface folding in the small intestine: folds, villi, and microvilli.",
            "tier_2": "Circular folds, villi, microvilli, single-layer epithelium, and capillary/lacteal networks maximize absorption.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["small_intestine_absorptive_adaptations_surface_area_misconception"],
    }


# 24. Hepatic portal system liver processing glycogen deamination
def arch_24_hepatic_portal_system_liver_processing_glycogen_deamination(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Capillaries of the small intestine absorb water-soluble nutrients (glucose, amino acids, vitamins, minerals).\n\n"
        f"Through which specialized vascular vessel are these nutrients transported directly to the liver, and what vital metabolic processing occurs there?"
    )
    correct = (
        "Hepatic Portal Vein; the liver converts excess glucose into glycogen for storage (under insulin stimulation), "
        "deaminates excess amino acids into urea (excreted by kidneys) and keto-acids (used for respiration), and detoxifies harmful chemicals and drugs."
    )
    wrong1 = (
        "Pulmonary Vein; the liver pumps food directly into the left lung for immediate evaporation."
    )
    wrong2 = (
        "Femoral Artery; the liver converts all glucose into solid muscle fibers inside the feet."
    )
    wrong3 = (
        "Renal Artery; the liver instantly excretes 100% of absorbed glucose into urine."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify vascular link between gut and liver: Hepatic Portal Vein.\n"
        f"**Step 2:** Note hepatic metabolic functions:\n"
        f"- Glycogenesis: Glucose -> Glycogen storage.\n"
        f"- Deamination: Excess amino acids -> Ammonia -> Urea.\n"
        f"- Detoxification of alcohol and pharmacological agents.\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_24_{rng.randint(100000, 999999)}",
        "subskill": "24_hepatic_portal_system_liver_processing_glycogen_deamination",
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
            "tier_1": "Which vein carries blood from small intestine directly to the liver?",
            "tier_2": "Hepatic portal vein; the liver stores glucose as glycogen and deaminates excess amino acids into urea.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hepatic_portal_system_liver_metabolism_deamination_misconception"],
    }


# 25. Large intestine water mineral reabsorption and feces formation
def arch_25_large_intestine_water_mineral_reabsorption_and_feces_formation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Indigestible food residues pass from the ileum through the ileocecal sphincter into the large intestine (colon).\n\n"
        f"What are the primary physiological functions of the **colon**?"
    )
    correct = (
        "1. Active and osmotic reabsorption of water, mineral salts, and electrolytes, consolidating liquid residue into semi-solid feces;\n"
        "2. Hosting mutualistic gut microbiome bacteria that ferment indigestible cellulose and synthesize vitamins (Vitamin K and B-complex);\n"
        "3. Storing feces in the rectum before controlled defecation (egestion)."
    )
    wrong1 = (
        "1. Primary site of protein and starch digestion using salivary enzymes;\n"
        "2. Pumping oxygen directly into the systemic circulation."
    )
    wrong2 = (
        "1. Producing hydrochloric acid to digest kidney stones;\n"
        "2. Turning solid food into bile."
    )
    wrong3 = (
        "1. Filtering all red blood cells out of the human body;\n"
        "2. Storing inhaled air before exhalation."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze large intestine / colon functions:\n"
        f"- Reabsorption of ~90% of remaining water and salts.\n"
        f"- Harboring beneficial gut microbiota (vitamin K synthesis).\n"
        f"- Compacting waste into feces stored in rectum prior to egestion.\n\n"
        f"**Step 2:** The correct functional summary is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_25_{rng.randint(100000, 999999)}",
        "subskill": "25_large_intestine_water_mineral_reabsorption_and_feces_formation",
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
            "tier_1": "What is reabsorbed in the large intestine, and what do gut bacteria make?",
            "tier_2": "The colon reabsorbs water and salts, compacts feces, and gut bacteria produce Vitamin K.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["large_intestine_colon_water_reabsorption_feces_formation_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_digestive_mouth_oral_cavity_plate_identification": arch_01_digestive_mouth_oral_cavity_plate_identification,
    "02_digestive_esophagus_peristalsis_plate_identification": arch_02_digestive_esophagus_peristalsis_plate_identification,
    "03_digestive_stomach_gastric_juice_plate_identification": arch_03_digestive_stomach_gastric_juice_plate_identification,
    "04_digestive_liver_bile_secretion_plate_identification": arch_04_digestive_liver_bile_secretion_plate_identification,
    "05_digestive_pancreas_pancreatic_juice_plate_identification": arch_05_digestive_pancreas_pancreatic_juice_plate_identification,
    "06_digestive_small_intestine_duodenum_ileum_plate_identification": arch_06_digestive_small_intestine_duodenum_ileum_plate_identification,
    "07_digestive_large_intestine_colon_water_reabsorption_plate_identification": arch_07_digestive_large_intestine_colon_water_reabsorption_plate_identification,
    "08_digestive_rectum_anus_egestion_plate_identification": arch_08_digestive_rectum_anus_egestion_plate_identification,
    "09_villus_microvilli_brush_border_plate_identification": arch_09_villus_microvilli_brush_border_plate_identification,
    "10_villus_columnar_epithelium_thin_barrier_plate_identification": arch_10_villus_columnar_epithelium_thin_barrier_plate_identification,
    "11_villus_goblet_cell_mucus_protection_plate_identification": arch_11_villus_goblet_cell_mucus_protection_plate_identification,
    "12_villus_central_lacteal_lipid_absorption_plate_identification": arch_12_villus_central_lacteal_lipid_absorption_plate_identification,
    "13_villus_capillary_network_glucose_amino_acid_transport_plate_identification": arch_13_villus_capillary_network_glucose_amino_acid_transport_plate_identification,
    "14_four_digestive_processes_ingestion_digestion_absorption_egestion": arch_14_four_digestive_processes_ingestion_digestion_absorption_egestion,
    "15_mechanical_digestion_mastication_teeth_churning_peristalsis": arch_15_mechanical_digestion_mastication_teeth_churning_peristalsis,
    "16_chemical_digestion_enzymatic_hydrolysis_lock_and_key_hypothesis": arch_16_chemical_digestion_enzymatic_hydrolysis_lock_and_key_hypothesis,
    "17_digestive_enzymes_carbohydrases_salivary_amylase_maltase": arch_17_digestive_enzymes_carbohydrases_salivary_amylase_maltase,
    "18_digestive_enzymes_proteases_pepsin_trypsin_amino_acids": arch_18_digestive_enzymes_proteases_pepsin_trypsin_amino_acids,
    "19_digestive_enzymes_lipases_bile_salts_emulsification_lipids": arch_19_digestive_enzymes_lipases_bile_salts_emulsification_lipids,
    "20_gastric_juice_hydrochloric_acid_pepsinogen_mucus_barrier": arch_20_gastric_juice_hydrochloric_acid_pepsinogen_mucus_barrier,
    "21_pancreatic_juice_bicarbonate_neutralization_and_enzymes": arch_21_pancreatic_juice_bicarbonate_neutralization_and_enzymes,
    "22_bile_synthesis_gallbladder_storage_emulsification_mechanism": arch_22_bile_synthesis_gallbladder_storage_emulsification_mechanism,
    "23_small_intestine_structural_adaptations_for_absorption": arch_23_small_intestine_structural_adaptations_for_absorption,
    "24_hepatic_portal_system_liver_processing_glycogen_deamination": arch_24_hepatic_portal_system_liver_processing_glycogen_deamination,
    "25_large_intestine_water_mineral_reabsorption_and_feces_formation": arch_25_large_intestine_water_mineral_reabsorption_and_feces_formation,
}
