"""Life Sciences & Senior Phase Natural Sciences — Human Organ Systems & Homeostasis.
Covers human digestion, circulation, gaseous exchange, kidney excretion, and endocrine negative feedback.
Strictly complies with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr9 NS, Gr11 LS, Gr12 LS)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.life_sciences.heart_generator import generate_heart_question
from app.utils.life_sciences.organ_diagram_builders import (
    build_digestive_question,
    build_villus_question,
    build_alveolus_question,
    build_nephron_question,
)
from app.utils.life_sciences.sensory_reproductive_builders import (
    build_eye_question,
    build_ear_question,
    build_endocrine_question,
    build_male_reproductive_question,
    build_female_reproductive_question,
)


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr9_organ_systems(r: random.Random, seed: Optional[int], idx: int, mode: str, subskill: str = "mixed") -> Dict[str, Any]:
    """Grade 9 Natural Sciences: Human digestive, circulatory, respiratory, excretory, sensory, reproductive, and musculoskeletal systems."""
    s_val = (int(seed or 0) + idx) if seed is not None else r.randint(100, 999999)
    sub_clean = (subskill or "mixed").lower()
    if sub_clean in ("digestive", "digestion"):
        system = "digestive"
    elif sub_clean in ("circulatory", "circulation", "heart"):
        system = "circulatory"
    elif sub_clean in ("respiratory", "respiration", "lungs"):
        system = "respiratory"
    elif sub_clean in ("excretory", "excretion", "kidney", "nephron"):
        system = "excretory"
    elif sub_clean in ("eye", "vision", "nervous", "sensory"):
        system = "sensory_eye"
    elif sub_clean in ("ear", "hearing"):
        system = "sensory_ear"
    elif sub_clean in ("reproductive", "reproduction"):
        system = "reproductive"
    elif sub_clean in ("musculoskeletal", "skeleton", "muscles"):
        system = "musculoskeletal"
    else:
        systems_pool = [
            "digestive",
            "circulatory",
            "respiratory",
            "excretory",
            "sensory_eye",
            "sensory_ear",
            "reproductive",
            "musculoskeletal",
        ]
        system = systems_pool[s_val % len(systems_pool)]

    if system == "digestive":
        return build_digestive_question(seed=s_val, grade=9, mode=mode)
    if system == "circulatory":
        return generate_heart_question(seed=s_val, grade=9, mode=mode, subskill=sub_clean)
    if system == "respiratory":
        return build_alveolus_question(seed=s_val, grade=9, mode=mode)
    if system == "excretory":
        return build_nephron_question(seed=s_val, grade=9, mode=mode)
    if system == "sensory_eye":
        return build_eye_question(seed=s_val, grade=9, mode=mode)
    if system == "sensory_ear":
        return build_ear_question(seed=s_val, grade=9, mode=mode)
    if system == "reproductive":
        return (
            build_male_reproductive_question(seed=s_val, grade=9, mode=mode)
            if (s_val // 8) % 2 == 0
            else build_female_reproductive_question(seed=s_val, grade=9, mode=mode)
        )

    qid = _make_id("ns9_organ_system", seed, idx)
    prompt = (
        "The human musculoskeletal system enables locomotion, structural support, and organ protection.\n\n"
        "1. Distinguish between the physiological roles of **ligaments** and **tendons** at a movable synovial joint.\n"
        "2. Explain why skeletal muscles must work in **antagonistic pairs** (such as the biceps and triceps) to move bones.\n"
        "3. Name TWO mineral deficiencies or disorders that affect the musculoskeletal system."
    )
    ans_str = (
        "1. Ligaments connect bone to bone to stabilise joints; tendons connect muscle to bone to transmit pulling force; "
        "2. Muscles can only contract (pull) and cannot actively push, so one flexes while the opposite extends; "
        "3. Rickets (vitamin D/calcium deficiency), osteoporosis (loss of bone mineral density), or arthritis (joint inflammation)."
    )
    memo = (
        "1. Ligaments vs Tendons [2]: Ligaments are tough, slightly elastic fibrous bands connecting bone to bone to stabilise joints [1]. "
        "Tendons are inelastic collagen cords connecting skeletal muscle to bone to transmit contraction forces [1].\n"
        "2. Antagonistic Muscle Pairs [2]: Skeletal muscle fibres can only exert force by contracting (pulling) and cannot push when relaxing [1]. "
        "Therefore, a flexor (e.g. biceps) contracts while its antagonist extensor (e.g. triceps) relaxes to bend the joint, and vice versa [1].\n"
        "3. Musculoskeletal Disorders [2]: Any two of Rickets, Osteoporosis, or Arthritis [2]."
    )
    hints = {
        "tier_1": "Think about what connects bone-to-bone versus muscle-to-bone, and whether a muscle can push.",
        "tier_2": "Ligaments = bone to bone. Tendons = muscle to bone. Muscles only pull when contracting, requiring antagonistic pairs.",
        "tier_3": "1. Ligaments (bone-bone), Tendons (muscle-bone). 2. Muscles only pull, so pairs alternate contraction/relaxation. 3. Rickets, osteoporosis, arthritis.",
    }
    marks = 6
    modality = "semantic"
    diagram_spec = None

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "modality": modality,
        "diagram_spec": diagram_spec,
        "solution_type": "marking_points",
        "question": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "expected_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["confused_artery_with_vein", "pulmonary_circulation_direction_inversion", "inhalation_pressure_misunderstanding"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition/pathway", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Specific organ/vessel identification", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Physiological explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


ORGAN_INQUIRY_HOOKS = [
    "During a clinical physiology investigation at a South African academic hospital,",
    "In a controlled laboratory experiment on human metabolic organ systems,",
    "A sports science research team analyzes physiological adaptations in endurance athletes,",
    "In a Life Sciences practical examination question on human organ physiology,",
    "An investigative medical diagnostic unit evaluates biochemical organ clearance,"
]


def _generate_gr11_nutrition_excretion(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Life Sciences: Animal Nutrition (enzymes, villi), Gaseous Exchange (alveoli), and Excretion (nephron)."""
    s_val = (int(seed or 0) + idx) if seed is not None else r.randint(0, 10000)
    hook = ORGAN_INQUIRY_HOOKS[s_val % len(ORGAN_INQUIRY_HOOKS)]
    sub_topics = ["nutrition", "gaseous_exchange", "excretion", "nutrition", "gaseous_exchange", "excretion"]
    sub_topic = sub_topics[s_val % len(sub_topics)]
    qid = _make_id("ls11_organ_physiology", seed, idx)
    modality = "semantic"
    diagram_spec = None

    if mode == "elementary_enzyme_ph" or sub_topic == "nutrition":
        temp = r.choice([36.5, 37.0, 37.5, 38.0])
        substrate = r.choice(["egg albumen (protein)", "dilute starch suspension", "gelatin sol", "casein protein"])
        prompt = (
            f"{hook} test tube investigations are conducted on human digestive enzymes using a {substrate} substrate.\n"
            f"Enzyme A (pepsin) and Enzyme B (pancreatic amylase) are incubated at {temp}°C "
            f"across varying pH levels from 1 to 10.\n\n"
            f"1. State the optimum pH for Enzyme A (pepsin) and name the digestive organ where it operates.\n"
            f"2. Explain the structural adaptations of intestinal villi that facilitate efficient absorption of digested food."
        )
        ans_str = "1. Optimum pH 1.5–2 (acidic), operates in the stomach; 2. Microvilli (large surface area), single cell epithelium (thin), lacteal, dense capillary network."
        memo = (
            "1. Enzyme A (pepsin) operates optimally at pH 1,5 to 2,0 [1] in the stomach [1].\n"
            "2. Adaptations of villi [4]:\n"
            "   - Microvilli on epithelial cells tremendously increase the surface area for absorption.\n"
            "   - Single-cell layer epithelium (thin surface) ensures rapid diffusion distance.\n"
            "   - Central lacteal absorbs digested fatty acids and glycerol.\n"
            "   - Dense blood capillary network transports glucose and amino acids away, maintaining a steep concentration gradient."
        )
        hints = {
            "tier_1": "Stomach hydrochloric acid creates an acidic environment for pepsin. Villi maximize surface area.",
            "tier_2": "Pepsin requires pH 1.5-2.0. Villi adaptations: microvilli (surface area), thin wall (diffusion), lacteal (fats), capillaries (blood).",
            "tier_3": "1. pH 1.5-2 in stomach. 2. Large surface area, thin 1-cell wall, lacteal for fats, capillaries for glucose/amino acids.",
        }
        marks = 6
        modality = "bio_diagram"
        diagram_spec = build_villus_question(seed=s_val, grade=11, mode=mode)["diagram_spec"]
    elif mode == "elementary_nephron_ultrafiltration" or sub_topic == "excretion":
        gfr = r.choice([120, 125, 130, 180])
        prompt = (
            f"{hook} renal excretion is evaluated in a patient with a glomerular filtration rate of {gfr} cm³·min⁻¹.\n"
            f"The functional microscopic filtration unit of the human kidney (nephron) is shown in schematic view.\n\n"
            f"1. Name the two structures indicated by Pin A and Pin B which together constitute the renal corpuscle.\n"
            f"2. Describe the process of ultrafiltration that occurs at Pin B, explaining how high filtration pressure is generated.\n"
            f"3. State which major blood components are normally prevented from passing into the glomerular filtrate inside Bowman's capsule (Pin A).\n"
            f"4. State the primary physiological process that occurs along the proximal tubule (Pin C) and Loop of Henle (Pin D)."
        )
        ans_str = "1. Bowman's capsule (A) and Glomerulus (B); 2. Afferent arteriole wider than efferent arteriole creates high hydrostatic pressure forcing small solutes through podocyte slits; 3. Blood cells and plasma proteins; 4. Tubular reabsorption (water and essential solutes)."
        memo = (
            "1. Pin A: Bowman's capsule; Pin B: Glomerulus (capillary network). Together they form the Malpighian body / renal corpuscle [2].\n"
            "2. Ultrafiltration [3]: The afferent arteriole has a wider diameter than the efferent arteriole, creating high hydrostatic pressure in the glomerulus [1]. "
            "This pressure forces small molecules (water, glucose, amino acids, urea, mineral salts) through the endothelial pores and podocyte filtration slits into Bowman's capsule [2].\n"
            "3. Blood cells (erythrocytes, leukocytes) and large plasma proteins (e.g. albumin, fibrinogen) are too large to pass through the filtration slits [2].\n"
            "4. Selective tubular reabsorption: Active reabsorption of glucose, amino acids, and passive reabsorption of water/salts back into the peritubular capillaries [1]."
        )
        hints = {
            "tier_1": "Pin A is the cup-shaped capsule; Pin B is the glomerulus knot. Look at the diameter difference in arterioles.",
            "tier_2": "Afferent arteriole is wider than efferent, producing high filtration pressure. Reabsorption recovers glucose and water.",
            "tier_3": "1. Bowman's capsule & Glomerulus. 2. Afferent wider than efferent -> high pressure. 3. Blood cells & large proteins. 4. Tubular reabsorption.",
        }
        marks = 8
        modality = "bio_diagram"
        diagram_spec = build_nephron_question(seed=s_val, grade=11, mode=mode)["diagram_spec"]
    else:
        # Gaseous exchange
        altitude = r.choice([1400, 1750, 2000, 2500])
        prompt = (
            f"{hook} pulmonary gaseous exchange is measured in athletes training at an altitude of {altitude} m above sea level.\n"
            f"In human lungs, gaseous exchange occurs between the alveoli and pulmonary blood capillaries.\n\n"
            f"1. State Fick's Law of diffusion and identify three structural features of human alveoli that satisfy this law.\n"
            f"2. Explain how oxygen and carbon dioxide are transported in human blood."
        )
        ans_str = "1. Rate of diffusion proportional to surface area and concentration gradient, inversely proportional to thickness; large surface area, 1-cell thin, moist lining; 2. Oxygen by oxyhemoglobin; CO2 mostly as bicarbonate ions."
        memo = (
            "1. Fick's Law: Diffusion rate is proportional to surface area and concentration gradient, and inversely proportional to membrane thickness [2].\n"
            "   Alveolar adaptations: Enormous collective surface area [1]; extremely thin wall (single layer of squamous epithelium) [1]; moist internal lining for gases to dissolve [1]; rich network of capillaries [1].\n"
            "2. Oxygen transport: 98.5% bound to hemoglobin in red blood cells forming oxyhemoglobin (HbO8); 1.5% dissolved in plasma [2].\n"
            "   Carbon dioxide transport: ~70% as bicarbonate ions (HCO3-) in plasma; ~23% bound to hemoglobin as carbaminohemoglobin; ~7% dissolved in plasma [2]."
        )
        hints = {
            "tier_1": "Think about Fick's equation: area, thickness, and moisture. Hemoglobin carries oxygen.",
            "tier_2": "Large surface area, thin squamous epithelium, and moisture facilitate diffusion. Oxygen binds to hemoglobin; CO2 travels mainly as bicarbonate.",
            "tier_3": "1. Large area, 1-cell thin, moist. 2. O2 = oxyhemoglobin. CO2 = bicarbonate ions in plasma.",
        }
        marks = 10
        modality = "bio_diagram"
        diagram_spec = build_alveolus_question(seed=s_val, grade=11, mode=mode)["diagram_spec"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "modality": modality,
        "diagram_spec": diagram_spec,
        "solution_type": "marking_points",
        "question": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "expected_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["nephron_reabsorption_misunderstanding", "excretion_egestion_confusion", "ficks_law_gradient_inversion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Anatomical structures", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Physiological process mechanism", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Transport/diffusion adaptations", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr12_homeostasis_endocrine(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 12 Life Sciences: Endocrine system and negative feedback mechanisms (glucose, ADH, thermoregulation)."""
    s_val = (int(seed or 0) + idx) if seed is not None else r.randint(100, 999999)
    stimulus = r.choice(["high_glucose", "low_glucose", "dehydration", "cold_exposure"])
    qid = _make_id("ls12_homeostasis", seed, idx)
    modality = "bio_diagram"
    diagram_spec = build_endocrine_question(seed=s_val, grade=12, mode=mode)["diagram_spec"]

    if stimulus in ("high_glucose", "low_glucose"):
        is_high = stimulus == "high_glucose"
        prompt = (
            f"A healthy human eats a meal high in carbohydrates, causing blood glucose levels to rise significantly above "
            f"the normal set point of $90\\text{{ mg/dL}}$."
            if is_high else
            f"A person has been fasting for 12 hours, causing blood glucose levels to drop below the normal set point of $90\\text{{ mg/dL}}$."
        ) + (
            "\n\n1. Define the term 'homeostasis' and explain the principle of a negative feedback mechanism.\n"
            f"2. Describe in detail the negative feedback response that restores blood glucose levels back to normal, identifying the specific endocrine gland, cell type, and hormone involved."
        )
        ans_str = (
            "1. Maintenance of a constant internal environment; negative feedback reverses deviation from set point; "
            "2. Pancreas beta cells secrete insulin; stimulates cells to absorb glucose and liver to store glucose as glycogen."
            if is_high else
            "1. Maintenance of a constant internal environment; negative feedback reverses deviation from set point; "
            "2. Pancreas alpha cells secrete glucagon; stimulates liver to break down glycogen into glucose, releasing it into blood."
        )
        memo = (
            "1. Homeostasis is the maintenance of a constant internal environment within narrow limits despite external fluctuations [2]. "
            "Negative feedback is a control mechanism where a deviation from the set point triggers a corrective physiological response that reverses the change back towards the set point [2].\n"
            "2. Feedback Loop [4]:\n"
            + (
                "   - High blood glucose is detected by beta cells in the islets of Langerhans of the pancreas [1].\n"
                "   - Beta cells secrete the hormone insulin into the bloodstream [1].\n"
                "   - Insulin stimulates body cells to take up more glucose and stimulates the liver and muscles to convert excess glucose into insoluble glycogen [1].\n"
                "   - Blood glucose levels decrease back to the normal set point [1]."
                if is_high else
                "   - Low blood glucose is detected by alpha cells in the islets of Langerhans of the pancreas [1].\n"
                "   - Alpha cells secrete the hormone glucagon into the bloodstream [1].\n"
                "   - Glucagon stimulates liver cells to convert stored glycogen into glucose [1].\n"
                "   - Glucose is released into the blood, increasing blood glucose back to the normal set point [1]."
            )
        )
        hints = {
            "tier_1": "Recall the two hormones produced by the islets of Langerhans: insulin and glucagon.",
            "tier_2": "Insulin lowers glucose by storing it as glycogen in the liver. Glucagon increases glucose by breaking down glycogen.",
            "tier_3": (
                "High glucose -> Beta cells secrete insulin -> Glucose converted to glycogen in liver -> Levels drop to normal."
                if is_high else
                "Low glucose -> Alpha cells secrete glucagon -> Glycogen converted to glucose in liver -> Levels rise to normal."
            ),
        }
        marks = 8
    else:
        # Osmoregulation via ADH
        prompt = (
            "On a hot summer afternoon, a person plays soccer for two hours without drinking water, leading to dehydration.\n\n"
            "1. Name the hormone responsible for maintaining water balance in the human body and state which gland secretes it.\n"
            "2. Describe the negative feedback mechanism that restores water balance in this dehydrated individual, detailing its effect on the nephron and urine output."
        )
        ans_str = "1. ADH (Antidiuretic Hormone) secreted by the pituitary gland; 2. Osmoreceptors detect low water, pituitary releases more ADH, collecting ducts become more permeable, water reabsorbed, concentrated small volume urine produced."
        memo = (
            "1. Antidiuretic Hormone (ADH) / Vasopressin [1], secreted by the posterior pituitary gland (hypophysis) [1].\n"
            "2. Negative Feedback Mechanism [4]:\n"
            "   - Dehydration causes blood osmolarity to rise (water potential drops), which is detected by osmoreceptors in the hypothalamus [1].\n"
            "   - The hypothalamus stimulates the pituitary gland to secrete more ADH into the blood [1].\n"
            "   - ADH increases the water permeability of the distal convoluted tubules and collecting ducts of the kidney nephrons [1].\n"
            "   - More water is reabsorbed by osmosis back into the blood capillaries, producing a small volume of dark, concentrated urine and restoring blood water potential to normal [1]."
        )
        hints = {
            "tier_1": "Think about ADH (Anti-Diuretic Hormone). 'Diuresis' means urine production; 'anti' means reducing water loss.",
            "tier_2": "Hypothalamus detects water loss and signals the pituitary to release ADH. ADH makes kidney collecting ducts more permeable to water.",
            "tier_3": "1. ADH from pituitary. 2. More ADH released -> collecting ducts reabsorb more water -> small volume concentrated urine -> blood water restored.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "modality": modality,
        "diagram_spec": diagram_spec,
        "solution_type": "marking_points",
        "question": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "expected_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["confused_insulin_with_glucagon", "adh_osmoregulation_mechanism_inverted", "hypophysis_hypothalamus_confusion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Homeostasis and feedback definitions", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Detection by receptor/gland", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Target organ physiological response", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr12_sensory_organs(r: random.Random, seed: Optional[int], idx: int, mode: str, organ: str = "mixed") -> Dict[str, Any]:
    """Grade 12 Life Sciences: Sensory reception - Longitudinal section of the human eye and ear."""
    eff_organ = "ear" if organ in ("ear", "hearing", "balance") else ("eye" if organ in ("eye", "vision", "accommodation") else (r.choice(["eye", "ear"])))
    if eff_organ == "ear":
        qid = _make_id("ls12_human_ear", seed, idx)
        prompt = (
            "The diagram shows a longitudinal cross-section of the human ear involved in hearing and balance.\n\n"
            "1. Identify the structures indicated by Pins C, D, and E.\n"
            "2. State the sensory function of the organ of Corti located within Pin F and explain how sound vibrations are transduced into nerve impulses.\n"
            "3. Explain the physiological role of the semicircular canals (Pin E) in maintaining dynamic equilibrium during rotational head movement.\n"
            "4. Describe the function of the Eustachian tube (Pin G) and explain why equal pressure across Pin C is necessary for normal hearing."
        )
        ans_str = (
            "1. Pin C: Tympanic membrane (eardrum); Pin D: Auditory ossicles (malleus, incus, stapes); Pin E: Semicircular canals; "
            "2. Converts mechanical vibrations of endolymph into action potentials via hair cells, transmitted by auditory nerve to cerebrum; "
            "3. Endolymph movement within ampullae bends crista ampullaris cupula hair cells, generating impulses for dynamic balance; "
            "4. Equalizes air pressure between middle ear and pharynx so tympanic membrane can vibrate freely."
        )
        memo = (
            "1. Identification [3]: Pin C: Tympanic membrane / Eardrum [1]; Pin D: Auditory ossicles (malleus, incus, stapes) [1]; Pin E: Semicircular canals [1].\n"
            "2. Organ of Corti Transduction [3]: Sound vibrations from oval window create fluid pressure waves in perilymph and endolymph of cochlea (Pin F) [1]. "
            "These waves bend microscopic hair cells on the basilar membrane against the tectorial membrane [1], depolarizing receptors and generating nerve impulses transmitted along the auditory nerve to the auditory cortex [1].\n"
            "3. Dynamic Equilibrium [2]: Semicircular canals are arranged in three mutually perpendicular planes [1]. Rotational acceleration causes endolymph fluid inertia to deflect gelatinous cupulae in the ampullae, bending sensory hair cells to signal dynamic balance to the cerebellum [1].\n"
            "4. Eustachian Tube Pressure Equalization [2]: Connects middle ear cavity to the nasopharynx to equalize air pressure on both sides of the tympanic membrane (Pin C) [1], allowing free resonant vibration without rupture or distortion [1]."
        )
        hints = {
            "tier_1": "Pin C is the eardrum. Pin D is the three middle ear bones. Pin E is the 3 loops for balance.",
            "tier_2": "The cochlea converts vibrations to nerve impulses. Semicircular canals detect rotation. Eustachian tube connects to throat to balance air pressure.",
            "tier_3": "1. Tympanic membrane, Ossicles, Semicircular canals. 2. Hair cells bend in cochlea. 3. Endolymph movement in ampullae for dynamic balance. 4. Equalizes pressure across eardrum.",
        }
        marks = 10
        s_val = (int(seed or 0) + idx) if seed is not None else r.randint(100, 999999)
        diagram_spec = build_ear_question(seed=s_val, grade=12, mode=mode)["diagram_spec"]
        return {
            "id": qid,
            "question_id": qid,
            "term": 2,
            "caps_weight_percent": 18,
            "suggested_duration_mins": 10,
            "mode": mode,
            "question_type": "short_answer",
            "modality": "bio_diagram",
            "diagram_spec": diagram_spec,
            "solution_type": "marking_points",
            "question": prompt,
            "prompt": prompt,
            "correct_answer": ans_str,
            "sample_answer": ans_str,
            "expected_answer": ans_str,
            "worked_solution": memo,
            "explanation": memo,
            "marks": marks,
            "hints": hints,
            "misconception_tags": [
                "middle_vs_inner_ear_confusion",
                "cochlea_semicircular_canal_function_inversion",
                "eustachian_tube_hearing_vs_pressure_confusion"
            ],
            "marking_schema": {
                "total_marks": marks,
                "marking_points": [
                    {"id": "mp_1", "desc": "Ear structures identification", "marks": 3, "editable": True},
                    {"id": "mp_2", "desc": "Organ of Corti transduction mechanism", "marks": 3, "editable": True},
                    {"id": "mp_3", "desc": "Semicircular canals dynamic balance", "marks": 2, "editable": True},
                    {"id": "mp_4", "desc": "Eustachian tube pressure equalization", "marks": 2, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
        }

    qid = _make_id("ls12_human_eye", seed, idx)
    action = r.choice(["accommodation_near", "accommodation_distant", "pupillary_bright", "pupillary_dim"])

    if "accommodation" in action:
        is_near = action == "accommodation_near"
        distance_str = "near object (less than 6 metres away)" if is_near else "distant object (further than 6 metres away)"
        prompt = (
            f"The diagram shows a longitudinal cross-section of the human eye.\n\n"
            f"1. Identify the parts indicated by Pins C, D, and E.\n"
            f"2. State the sensory function of the layer indicated by Pin F and name the two types of photoreceptor cells located within it.\n"
            f"3. A person shifts their gaze to focus clearly on a {distance_str}. Describe in sequence the changes that take place in the eye (accommodation) to produce a sharply focused image on Pin F.\n"
            f"4. Name the visual defect where the eyeball is too long or the lens is too convex, and state the type of lens used to correct it."
        )
        if is_near:
            mechanism = (
                "Accommodation for Near Vision (<6m) [4]:\n"
                "- Ciliary muscles contract [1].\n"
                "- Suspensory ligaments become slack / loosen [1].\n"
                "- Tension on the lens is reduced, allowing the biconvex lens (Pin D) to become more convex / rounded [1].\n"
                "- Refractive power of the lens increases, bending light rays more to focus precisely on the yellow spot / retina (Pin F) [1]."
            )
            ans_str = (
                "1. Pin C: Iris; Pin D: Biconvex Lens; Pin E: Ciliary body & suspensory ligaments; "
                "2. Pin F: Retina (photoreception via rods and cones); "
                "3. Ciliary muscles contract -> suspensory ligaments slacken -> lens becomes more convex -> refractive power increases -> clear image on retina; "
                "4. Myopia (short-sightedness), corrected with concave / diverging lens."
            )
        else:
            mechanism = (
                "Accommodation for Distant Vision (>6m) [4]:\n"
                "- Ciliary muscles relax [1].\n"
                "- Suspensory ligaments tauten / tighten [1].\n"
                "- Tension pulls on the biconvex lens (Pin D), causing it to become less convex / flatter [1].\n"
                "- Refractive power of the lens decreases, focusing light rays precisely on the yellow spot / retina (Pin F) [1]."
            )
            ans_str = (
                "1. Pin C: Iris; Pin D: Biconvex Lens; Pin E: Ciliary body & suspensory ligaments; "
                "2. Pin F: Retina (photoreception via rods and cones); "
                "3. Ciliary muscles relax -> suspensory ligaments tauten -> lens becomes less convex / flatter -> refractive power decreases -> clear image on retina; "
                "4. Hypermetropia (long-sightedness), corrected with convex / converging lens."
            )

        memo = (
            "1. Structure identification [3]: Pin C: Iris [1], Pin D: Biconvex Lens [1], Pin E: Ciliary body & suspensory ligaments [1].\n"
            "2. Sensory layer & photoreceptors [2]: Retina transduces light into nerve impulses [1] using rods (dim light) and cones (bright light/colour) [1].\n"
            f"3. Accommodation Sequence [4]:\n{mechanism}\n"
            "4. Visual Defect [2]: Myopia / Short-sightedness [1], corrected with concave / diverging lens [1]."
            if is_near else
            "1. Structure identification [3]: Pin C: Iris [1], Pin D: Biconvex Lens [1], Pin E: Ciliary body & suspensory ligaments [1].\n"
            "2. Sensory layer & photoreceptors [2]: Retina transduces light into nerve impulses [1] using rods (dim light) and cones (bright light/colour) [1].\n"
            f"3. Accommodation Sequence [4]:\n{mechanism}\n"
            "4. Visual Defect [2]: Hypermetropia / Long-sightedness [1], corrected with convex / converging lens [1]."
        )
        hints = {
            "tier_1": "Recall accommodation: ciliary muscle tension and suspensory ligaments control lens curvature.",
            "tier_2": "For near vision: ciliary muscles contract, ligaments slacken, lens rounds. For distant vision: ciliary muscles relax, ligaments tauten, lens flattens.",
            "tier_3": "Near: contract -> slacken -> more convex -> sharp focus. Distant: relax -> tauten -> less convex -> sharp focus.",
        }
        marks = 11
    else:
        is_bright = action == "pupillary_bright"
        light_cond = "bright sunlight" if is_bright else "a dimly lit room"
        prompt = (
            f"The diagram shows a longitudinal cross-section of the human eye.\n\n"
            f"1. Identify the structures indicated by Pins A, B, and G.\n"
            f"2. Explain why damage to Pin G results in complete blindness even if all other structures of the eye are undamaged.\n"
            f"3. Describe the pupillary reflex when a person suddenly walks into {light_cond}, detailing the antagonistic action of the iris muscles (Pin C) and the change in diameter of Pin B."
        )
        if is_bright:
            mechanism = (
                "Pupillary Reflex in Bright Light [4]:\n"
                "- Photoreceptors in retina detect high light intensity and send impulses along optic nerve [1].\n"
                "- Circular muscles of the iris (Pin C) contract [1].\n"
                "- Radial muscles of the iris relax [1].\n"
                "- The pupil (Pin B) constricts (narrows), reducing light entry to prevent photoreceptor damage [1]."
            )
            ans_str = (
                "1. Pin A: Cornea; Pin B: Pupil; Pin G: Optic nerve; "
                "2. Optic nerve carries sensory impulses to the visual cortex of the brain; if damaged, impulses cannot reach the cerebrum; "
                "3. Circular muscles contract, radial muscles relax, pupil constricts, reducing light entry."
            )
        else:
            mechanism = (
                "Pupillary Reflex in Dim Light [4]:\n"
                "- Photoreceptors in retina detect low light intensity and send impulses to brain [1].\n"
                "- Radial muscles of the iris (Pin C) contract [1].\n"
                "- Circular muscles of the iris relax [1].\n"
                "- The pupil (Pin B) dilates (widens), increasing light entry to stimulate rods [1]."
            )
            ans_str = (
                "1. Pin A: Cornea; Pin B: Pupil; Pin G: Optic nerve; "
                "2. Optic nerve carries sensory impulses to the visual cortex of the brain; if damaged, impulses cannot reach the cerebrum; "
                "3. Radial muscles contract, circular muscles relax, pupil dilates, allowing more light entry."
            )

        memo = (
            "1. Structure identification [3]: Pin A: Cornea [1], Pin B: Pupil [1], Pin G: Optic nerve [1].\n"
            "2. Sensory transmission [2]: Optic nerve conducts action potentials from retina to visual cortex (occipital lobe) of cerebrum [1]; without it, brain receives no sensory input [1].\n"
            f"3. Pupillary Reflex [4]:\n{mechanism}"
        )
        hints = {
            "tier_1": "Recall the two antagonistic muscle groups in the iris: circular and radial muscles.",
            "tier_2": "Bright light: circular muscles contract, pupil constricts. Dim light: radial muscles contract, pupil dilates.",
            "tier_3": "1. Cornea, Pupil, Optic nerve. 2. Impulses cannot reach brain. 3. Antagonistic iris muscles regulate pupil aperture.",
        }
        marks = 9

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "modality": "bio_diagram",
        "diagram_spec": build_eye_question(seed=(int(seed or 0) + idx) if seed is not None else r.randint(100, 999999), grade=12, mode=mode)["diagram_spec"],
        "solution_type": "marking_points",
        "question": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "expected_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "ciliary_muscle_suspensory_ligament_inversion",
            "circular_radial_muscle_confusion",
            "myopia_hypermetropia_lens_inversion"
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Eye anatomical structures identification", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Sensory function / transmission", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Physiological reflex / accommodation sequence", "marks": 4, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Human Organ Systems & Homeostasis."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "11"

    for i in range(count):
        sub_seed = (int(seed or 0) * 1000 + i) if seed is not None else random.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("circulatory", "heart", "cardiac_cycle", "valves") or (grade_num == "10" and subskill in ("transport", "heart", "cardiac_cycle")):
            q = generate_heart_question(seed=sub_seed, grade=int(grade_num) if grade_num in ("9", "10") else 10, mode=mode, subskill=subskill)
        elif grade_num in ("7", "8", "9") or subskill in ("digestive", "circulatory", "respiratory", "digestion", "heart", "lungs"):
            q = _generate_gr9_organ_systems(sub_r, sub_seed, i, mode, subskill)
        elif grade_num == "12" or subskill in ("homeostasis", "endocrine", "glucose", "adh", "eye", "ear", "senses", "vision", "hearing", "balance", "accommodation"):
            if subskill in ("eye", "ear", "senses", "vision", "hearing", "balance", "accommodation") or (sub_r.random() < 0.5 and subskill in ("mixed", "concepts")):
                organ = "ear" if subskill in ("ear", "hearing", "balance") else ("eye" if subskill in ("eye", "vision", "accommodation") else "mixed")
                q = _generate_gr12_sensory_organs(sub_r, sub_seed, i, mode, organ=organ)
            else:
                q = _generate_gr12_homeostasis_endocrine(sub_r, sub_seed, i, mode)
        else:
            # Grade 11 Life Sciences default: Nutrition, gaseous exchange, excretion
            q = _generate_gr11_nutrition_excretion(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions

# diagram_role specification helper
