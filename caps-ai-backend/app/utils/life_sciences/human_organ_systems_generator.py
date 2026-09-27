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


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr9_organ_systems(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 9 Natural Sciences: Human digestive, circulatory, and respiratory anatomy."""
    system = r.choice(["digestive", "circulatory", "respiratory"])
    qid = _make_id("ns9_organ_system", seed, idx)

    if system == "digestive":
        prompt = (
            "The human digestive system processes food through mechanical and chemical digestion.\n\n"
            "1. Define the term 'chemical digestion' and name the biological catalysts responsible for this process.\n"
            "2. State the primary function of the stomach in the digestive process.\n"
            "3. State in which organ the absorption of digested nutrients into the bloodstream predominantly occurs."
        )
        ans_str = "1. Breakdown of large insoluble molecules into small soluble molecules using enzymes; 2. Churning food & protein digestion (pepsin/acid); 3. Small intestine"
        memo = (
            "1. Chemical digestion is the breakdown of large, complex, insoluble food molecules into small, simple, soluble molecules [1] catalyzed by digestive enzymes [1].\n"
            "2. Stomach churns food into chyme [1] and initiates protein digestion in an acidic environment (HCl and pepsin) [1].\n"
            "3. Absorption takes place mainly in the small intestine (jejunum and ileum) via villi [1]."
        )
        hints = {
            "tier_1": "Think about the role of enzymes and the structure of the small intestine.",
            "tier_2": "Chemical digestion uses enzymes to break chemical bonds. Most absorption occurs across the vast surface of the small intestine.",
            "tier_3": "1. Enzyme-catalyzed breakdown. 2. Protein digestion/churning. 3. Small intestine.",
        }
        marks = 5
    elif system == "circulatory":
        prompt = (
            "The human circulatory system is a double circulatory system consisting of systemic and pulmonary circuits.\n\n"
            "1. Differentiate between oxygenated blood and deoxygenated blood.\n"
            "2. Name the blood vessel that carries deoxygenated blood from the heart to the lungs.\n"
            "3. Name the heart chamber with the thickest muscular wall and explain why this thickness is necessary."
        )
        ans_str = "1. Oxygenated is rich in oxygen; deoxygenated is oxygen-poor; 2. Pulmonary artery; 3. Left ventricle, needs high pressure to pump to entire body."
        memo = (
            "1. Oxygenated blood carries a high concentration of oxygen (bound to hemoglobin); deoxygenated blood is low in oxygen and rich in CO2. [2]\n"
            "2. Pulmonary artery. [1]\n"
            "3. Left ventricle [1]. It must generate high pressure to pump blood through the systemic circulation to the entire body, unlike the right ventricle which only pumps to the nearby lungs [2]."
        )
        hints = {
            "tier_1": "Arteries carry blood away from the heart. The left side pumps to the body.",
            "tier_2": "Pulmonary artery carries blood to lungs. The left ventricle pumps against high systemic resistance.",
            "tier_3": "1. Oxygen-rich vs oxygen-poor. 2. Pulmonary artery. 3. Left ventricle (pumps to whole body).",
        }
        marks = 6
    else:
        prompt = (
            "The human respiratory system facilitates gas exchange between the atmosphere and the blood.\n\n"
            "1. State the pathway of inhaled air from the nasal cavity to the site of gas exchange in the lungs.\n"
            "2. Name the tiny air sacs where gas exchange takes place.\n"
            "3. Describe the mechanism of inhalation in terms of the diaphragm and rib cage movements."
        )
        ans_str = "1. Nasal cavity -> Pharynx -> Larynx -> Trachea -> Bronchi -> Bronchioles -> Alveoli; 2. Alveoli; 3. Diaphragm contracts/flattens, ribs move up/out, volume increases."
        memo = (
            "1. Nasal cavity -> Trachea -> Bronchi -> Bronchioles -> Alveoli [2]\n"
            "2. Alveoli (air sacs) [1]\n"
            "3. During inhalation: Diaphragm contracts and flattens downwards [1]; External intercostal muscles contract, pulling ribs upwards and outwards [1]; Thoracic cavity volume increases and pressure decreases below atmospheric pressure [1]."
        )
        hints = {
            "tier_1": "Air passes down through branching tubes into micro-sacs. Inhalation expands the chest.",
            "tier_2": "Trachea branches into bronchi, then bronchioles, ending in alveoli. Contracting muscles increase volume.",
            "tier_3": "1. Trachea -> Bronchi -> Alveoli. 2. Alveoli. 3. Diaphragm flattens, ribs up/out, volume increases.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
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


def _generate_gr11_nutrition_excretion(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Life Sciences: Animal Nutrition (enzymes, villi), Gaseous Exchange (alveoli), and Excretion (nephron)."""
    sub_topic = r.choice(["nutrition", "gaseous_exchange", "excretion"])
    qid = _make_id("ls11_organ_physiology", seed, idx)

    if mode == "elementary_enzyme_ph" or sub_topic == "nutrition":
        prompt = (
            "A test tube investigation is conducted on human digestive enzymes.\n"
            "Enzyme A (pepsin) and Enzyme B (pancreatic amylase) are incubated with their substrates at $37^\\circ\\text{C}$ "
            "across varying pH levels from 1 to 10.\n\n"
            "1. State the optimum pH for Enzyme A (pepsin) and name the digestive organ where it operates.\n"
            "2. Explain the structural adaptations of intestinal villi that facilitate efficient absorption of digested food."
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
    elif mode == "elementary_nephron_ultrafiltration" or sub_topic == "excretion":
        prompt = (
            "Excretion in humans is carried out primarily by the kidneys, containing millions of microscopic functional units called nephrons.\n\n"
            "1. Name the two components that make up the Malpighian body (renal corpuscle).\n"
            "2. Describe the process of ultrafiltration that occurs in the Malpighian body, explaining how high filtration pressure is generated.\n"
            "3. State which major blood components are normally prevented from passing into the glomerular filtrate."
        )
        ans_str = "1. Glomerulus and Bowman's capsule; 2. Afferent arteriole wider than efferent arteriole, high pressure forces water/solutes through podocyte slits; 3. Blood cells and plasma proteins."
        memo = (
            "1. Glomerulus (capillary network) and Bowman's capsule. [2]\n"
            "2. Ultrafiltration [3]: The afferent arteriole has a wider diameter than the efferent arteriole, creating high hydrostatic pressure in the glomerulus [1]. "
            "This pressure forces small molecules (water, glucose, amino acids, urea, mineral salts) through the endothelial pores and podocyte filtration slits into Bowman's capsule [2].\n"
            "3. Blood cells (erythrocytes, leukocytes) and large plasma proteins (e.g. albumin, fibrinogen) are too large to pass through the filtration slits [2]."
        )
        hints = {
            "tier_1": "Notice the difference in diameter between the incoming and outgoing arterioles.",
            "tier_2": "Afferent is wider than efferent, producing high pressure. Podocyte slits filter out large blood proteins and cells.",
            "tier_3": "1. Glomerulus & Bowman's capsule. 2. Afferent wider than efferent -> high pressure. 3. Blood cells & large proteins prevented.",
        }
        marks = 7
    else:
        # Gaseous exchange
        prompt = (
            "In human lungs, gaseous exchange occurs between the alveoli and pulmonary blood capillaries.\n\n"
            "1. State Fick's Law of diffusion and identify three structural features of human alveoli that satisfy this law.\n"
            "2. Explain how oxygen and carbon dioxide are transported in human blood."
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

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
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
    stimulus = r.choice(["high_glucose", "low_glucose", "dehydration", "cold_exposure"])
    qid = _make_id("ls12_homeostasis", seed, idx)

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
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
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
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if grade_num in ("7", "8", "9") or subskill in ("digestive", "circulatory", "respiratory"):
            q = _generate_gr9_organ_systems(sub_r, sub_seed, i, mode)
        elif grade_num == "12" or subskill in ("homeostasis", "endocrine", "glucose", "adh"):
            q = _generate_gr12_homeostasis_endocrine(sub_r, sub_seed, i, mode)
        else:
            # Grade 11 Life Sciences default: Nutrition, gaseous exchange, excretion
            q = _generate_gr11_nutrition_excretion(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
