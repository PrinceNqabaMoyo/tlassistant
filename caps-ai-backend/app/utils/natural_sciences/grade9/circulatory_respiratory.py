"""Natural Sciences Grade 9 Term 1: Circulatory and Respiratory Systems Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/04. Circulatory and respiratory systems.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. heart_structure_and_double_circulation: 4-chamber cardiac anatomy & double circulation (calls heart_generator).
2. breathing_mechanics: Ventilation mechanics: diaphragm, intercostal muscles, thoracic volume and air pressure gradients.
3. alveolus_gaseous_exchange: Gas diffusion across moist alveolar membrane (calls alveolus_builder).
4. blood_vessels_comparison: Structural and functional comparison of arteries, veins, and capillaries.
5. pulse_rate_exercise_investigation: Experimental investigation of pulse rate before/after exercise and cellular respiration link.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.heart_generator import generate_heart_question
from app.utils.life_sciences.organ_diagram_builders import build_alveolus_question

TOPIC_NAME = "Circulatory and respiratory systems"
ORDERED_SUBSKILLS = [
    "heart_structure_and_double_circulation",
    "breathing_mechanics",
    "alveolus_gaseous_exchange",
    "blood_vessels_comparison",
    "pulse_rate_exercise_investigation",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_crs"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "title" not in res or not res["title"]:
        res["title"] = "Human Heart & Circulatory Anatomy"
    if "question" not in res or not res["question"]:
        res["question"] = res.get("prompt") or res.get("question_text", "")
    if "prompt" not in res or not res["prompt"]:
        res["prompt"] = res.get("question") or res.get("question_text", "")
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    if "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["topic"] = TOPIC_NAME
    res["grade"] = "9"
    res["term"] = 1
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ("heart", "cardiac", "double_circulation"):
        return _normalize_res(generate_heart_question(subskill="heart_anatomy_identification", grade=9, mode=mode, seed=actual_seed))
    elif subskill in ("alveolus", "gas_exchange", "alveoli"):
        return _normalize_res(build_alveolus_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Heart Structure & Double Circulation (Role L / P)
    if chosen_subskill == "heart_structure_and_double_circulation":
        view = kwargs.get("view") or ("textbook" if (actual_seed % 2 == 0) else "flow")
        return _normalize_res(generate_heart_question(
            subskill="heart_anatomy_identification",
            grade=9,
            mode=mode,
            seed=actual_seed,
            view=view,
        ))

    # Subskill 2: Breathing Mechanics (Inhalation vs Exhalation)
    if chosen_subskill == "breathing_mechanics":
        phase = "inhalation" if (actual_seed % 2 == 0) else "exhalation"
        if phase == "inhalation":
            prompt = (
                "During the mechanical process of breathing (ventilation), pressure and volume changes in the thoracic cavity "
                "draw air into and force air out of the lungs.\n\n"
                "1. Describe the action and shape change of the **diaphragm muscle** during **inhalation**.\n"
                "2. State how the movement of the rib cage and diaphragm alters the **volume** and **internal air pressure** of the thoracic cavity.\n"
                "3. Name the two main tubes that branch off from the trachea to carry inhaled air into the left and right lungs."
            )
            sample = (
                "1. **Diaphragm Action:** Contracts and flattens (moves downwards);\n"
                "2. **Thoracic Changes:** Thoracic volume increases, causing internal thoracic air pressure to decrease below atmospheric pressure, which draws ambient air into the lungs;\n"
                "3. **Airway Tubes:** Bronchi (singular: bronchus)."
            )
            marking = (
                "• 1 mark: Diaphragm contracts and flattens / moves downwards [1]\n"
                "• 2 marks: Thoracic volume increases [1] and internal pressure decreases below atmospheric pressure [1]\n"
                "• 1 mark: Bronchi [1]\n"
                "**Total: 4 marks**"
            )
            hints = [
                "When you breathe in, your chest expands. What does the diaphragm do to make more room?",
                "An increase in container volume causes gas pressure to decrease.",
                "Diaphragm contracts and flattens; thoracic volume increases and pressure drops; bronchi branch into lungs.",
            ]
        else:
            prompt = (
                "During exhalation, air is expelled from the respiratory tract.\n\n"
                "1. Describe the action and shape change of the **diaphragm muscle** during **exhalation**.\n"
                "2. State how the movement of the rib cage and diaphragm alters the **volume** and **internal air pressure** of the thoracic cavity.\n"
                "3. Explain why exhaled air contains a higher percentage of carbon dioxide and lower percentage of oxygen than inhaled air."
            )
            sample = (
                "1. **Diaphragm Action:** Relaxes and curves upwards into a dome shape;\n"
                "2. **Thoracic Changes:** Thoracic volume decreases, which increases internal thoracic air pressure above atmospheric pressure, forcing air out of the lungs;\n"
                "3. **Gas Differences:** Cellular respiration in body tissues consumes oxygen and produces carbon dioxide as a metabolic byproduct, which diffuses into blood and is exhaled via the alveoli."
            )
            marking = (
                "• 1 mark: Diaphragm relaxes and arches upward into a dome shape [1]\n"
                "• 2 marks: Thoracic volume decreases [1] and pressure increases above atmospheric pressure [1]\n"
                "• 1 mark: Oxygen is consumed and CO2 produced by cellular respiration [1]\n"
                "**Total: 4 marks**"
            )
            hints = [
                "When you breathe out, your chest relaxes and shrinks.",
                "A decrease in container volume causes internal gas pressure to increase.",
                "Diaphragm relaxes into dome shape; thoracic volume decreases and pressure increases; respiration consumes O2 and makes CO2.",
            ]
        return {
            "title": f"Breathing Mechanics: {phase.capitalize()}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": prompt,
            "question": prompt,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": hints,
            "misconception_tags": ["inhalation_diaphragm_expansion_error", "breathing_respiration_conflation"],
            "learning_objective_id": "NS9.LL.04.02",
        }

    # Subskill 3: Alveolus Gaseous Exchange (Microscopic Diagram / Mechanism)
    if chosen_subskill == "alveolus_gaseous_exchange":
        if actual_seed % 2 == 0:
            return _normalize_res(build_alveolus_question(actual_seed, grade=9, mode=mode))
        question_text = (
            "Gaseous exchange occurs across the microscopic membranes of pulmonary alveoli.\n\n"
            "1. Name the physical process by which oxygen passes from the alveolar air into blood capillaries.\n"
            "2. State **three structural adaptations** of alveoli that maximize the rate of gaseous exchange.\n"
            "3. Identify the component of blood that binds with oxygen in the alveolar capillaries, and name the resulting compound."
        )
        sample = (
            "1. **Physical Process:** Diffusion (passive movement down a concentration gradient);\n"
            "2. **Structural Adaptations:**\n"
            "   • Extremely thin walls (one-cell-thick squamous epithelium) providing a short diffusion pathway;\n"
            "   • Huge cumulative surface area formed by millions of spherical alveoli;\n"
            "   • Moist inner surface dissolving gases for rapid diffusion;\n"
            "   • Dense network of surrounding capillaries maintaining a steep concentration gradient;\n"
            "3. **Blood Component:** Haemoglobin inside red blood cells; **Compound:** Oxyhaemoglobin."
        )
        marking = (
            "• 1 mark: Diffusion [1]\n"
            "• 3 marks: Three valid structural adaptations (thin walls, large surface area, moist surface, dense capillary network) [3]\n"
            "• 1 mark: Haemoglobin forming oxyhaemoglobin [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Alveolar Gas Exchange & Diffusion",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Gases move from high concentration to low concentration without using energy.",
                "Think about wall thickness, moisture, surface area, and blood supply.",
                "Process: Diffusion. Adaptations: thin 1-cell walls, huge surface area, moist lining. Haemoglobin forms oxyhaemoglobin.",
            ],
            "misconception_tags": ["active_transport_gas_exchange_error", "alveolar_structure_confusion"],
            "learning_objective_id": "NS9.LL.04.03",
        }

    # Subskill 4: Blood Vessels Comparison
    if chosen_subskill == "blood_vessels_comparison":
        question_text = (
            "The human circulatory system comprises three distinct types of blood vessels: arteries, veins, and capillaries.\n\n"
            "1. Tabulate **three structural differences** between **arteries** and **veins** regarding wall thickness, lumen size, and the presence of valves.\n"
            "2. Explain why arteries need thick, elastic muscular walls while veins do not.\n"
            "3. Describe the unique structural adaptation of **capillaries** that allows exchange of substances with surrounding tissues."
        )
        sample = (
            "1. **Structural Comparison Table:**\n\n"
            "| Feature | Artery | Vein |\n"
            "| :--- | :--- | :--- |\n"
            "| **Wall Thickness** | Thick, muscular, and highly elastic | Thinner, with less muscle and elastic tissue |\n"
            "| **Lumen Size** | Narrow / small relative to wall thickness | Large / wide lumen to offer low resistance to flow |\n"
            "| **Valves** | Absent (except semilunar valves at heart exits) | Present (valves prevent backflow of blood) |\n\n"
            "2. **Functional Rationale:** Arteries receive blood directly pumped from the ventricles under high, pulsating pressure; thick elastic walls withstand and dampen this pressure without rupturing. Veins carry blood under very low pressure back to the heart;\n"
            "3. **Capillary Adaptation:** Walls are only one cell thick (endothelium), allowing rapid diffusion of dissolved nutrients, gases, and metabolic wastes between blood plasma and tissue fluid."
        )
        marking = (
            "• 3 marks: Table comparing wall thickness [1], lumen diameter [1], and presence/absence of valves [1]\n"
            "• 1 mark: Arteries withstand high ventricular blood pressure [1]\n"
            "• 1 mark: Capillaries are one-cell-thick for rapid diffusion [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Blood Vessel Structure & Adaptation",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Arteries carry blood away from the heart under high pressure; veins carry blood back to the heart under low pressure.",
                "Veins need one-way valves to stop blood flowing backwards.",
                "Arteries: thick walls, narrow lumen, no valves. Veins: thin walls, wide lumen, valves. Capillaries: 1-cell thick.",
            ],
            "misconception_tags": ["arteries_always_oxygenated_myth", "vein_valve_function_misconception"],
            "learning_objective_id": "NS9.LL.04.04",
        }

    # Subskill 5: Pulse Rate & Exercise Investigation
    resting_bpm = r.choice([68, 72, 75, 80])
    post_exercise_bpm = resting_bpm + r.choice([40, 50, 60, 70])
    recovery_min = r.choice([3, 4, 5])
    diff_bpm = post_exercise_bpm - resting_bpm

    question_text = (
        "A Grade 9 class conducted a scientific investigation on the effect of physical exercise on human heart rate.\n"
        "Learner A measured a resting pulse rate of **" + str(resting_bpm) + " beats per minute (bpm)**.\n"
        "Immediately after running vigorously for 3 minutes, their pulse rate increased to **" + str(post_exercise_bpm) + " bpm**, "
        "returning to resting level after **" + str(recovery_min) + " minutes**.\n\n"
        "1. Identify the **independent variable** and the **dependent variable** in this investigation.\n"
        "2. Calculate the **percentage increase** in pulse rate caused by the exercise.\n"
        "3. Explain physiologically why the heart must beat faster and pump more blood during vigorous muscular activity."
    )
    pct_increase = (diff_bpm / resting_bpm) * 100
    sample = (
        "1. **Independent Variable:** Intensity / level of physical exercise (resting vs running);\n"
        "   **Dependent Variable:** Heart rate / pulse rate (in beats per minute);\n"
        f"2. **Percentage Increase Calculation:**\n"
        f"   $$\\text{{Percentage Increase}} = \\frac{{\\text{{Increase in bpm}}}}{{\\text{{Resting bpm}}}} \\times 100 = \\frac{{{diff_bpm}}}{{{resting_bpm}}} \\times 100 = {pct_increase:.1f}\\%$$\n"
        "3. **Physiological Explanation:** Working muscle cells contract rapidly and consume energy at an elevated rate via cellular respiration. "
        "The heart must beat faster to increase cardiac output, delivering more oxygen and glucose to muscle cells and rapidly removing excess carbon dioxide and heat."
    )
    marking = (
        "• 2 marks: Independent variable (exercise intensity) [1]; Dependent variable (heart rate / bpm) [1]\n"
        "• 2 marks: Percentage increase formula and accurate substitution [1], correct answer ({pct_increase:.1f}%) [1]\n"
        "• 1 mark: Explanation relating increased cardiac output to cellular respiration (O2 delivery / CO2 removal) [1]\n"
        "**Total: 5 marks**"
    )
    return {
        "title": "Pulse Rate & Cellular Respiration Investigation",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 1,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "The independent variable is what the investigator changes; the dependent variable is what is measured.",
            "Percentage increase = (Difference / Original value) * 100.",
            f"Independent: exercise. Dependent: pulse rate. Increase = {pct_increase:.1f}%. Reason: muscle cells need more O2 and glucose for respiration.",
        ],
        "misconceptions": ["independent_dependent_variable_inversion", "percentage_increase_denominator_error"],
        "learning_objective_id": "NS9.LL.04.05",
    }
