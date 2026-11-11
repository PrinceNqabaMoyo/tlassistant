"""Life Sciences Grade 11 Term 3: Gaseous Exchange Topic Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr11/Term 3/01. Gaseous exchange.md
- curriculum_docs/LifeSciences_Gr11/Term 3/Gaseous_exchange.md

Subskills:
1. alveolus_gas_exchange_anatomy: Microscopic pulmonary alveolus and capillary diffusion (diagram questions).
2. exchange_surface_requirements: Fick's Law, surface area, thinness, moisture, transport vascularization.
3. breathing_ventilation_mechanics: Inhalation vs exhalation, diaphragm, intercostal muscles, pressure changes.
4. gas_transport_mechanisms: Oxyhemoglobin, carbaminohemoglobin, bicarbonate ions (HCO3-).
5. homeostatic_co2_control: Medulla oblongata, carotid body chemoreceptors, negative feedback.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import build_alveolus_question


SUBSKILLS = [
    "alveolus_gas_exchange_anatomy",
    "exchange_surface_requirements",
    "breathing_ventilation_mechanics",
    "gas_transport_mechanisms",
    "homeostatic_co2_control",
]


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = SUBSKILLS[actual_seed % len(SUBSKILLS)]
    else:
        chosen_subskill = subskill

    if chosen_subskill in ("alveolus_gas_exchange_anatomy", "alveolus_gas_exchange", "diagram", "alveolus", "anatomy"):
        return build_alveolus_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)

    subskills_pool = [
        "exchange_surface_requirements",
        "breathing_ventilation_mechanics",
        "gas_transport_mechanisms",
        "homeostatic_co2_control",
    ]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "exchange_surface_requirements":
        scenarios = [
            (
                "According to Fick's Law of Diffusion, which combination of structural adaptations maximizes the rate of gaseous exchange across human alveoli?",
                "Large total surface area, single-cell thin diffusion barrier, moist lining, and extensive capillary perfusion",
                [
                    "Thick keratinized stratified epithelium, dry surface, and sparse capillary loops",
                    "Narrow surface area, thick cartilage rings, and high hydrostatic blood pressure",
                    "Ciliated columnar cells, dry mucous plugs, and muscular sphincters",
                ],
                "Efficient gas exchange surfaces require a large surface area (millions of alveoli), extremely thin barrier (squamous cells), moisture to dissolve gases, and high concentration gradients maintained by blood flow.",
            ),
            (
                "Why must the internal surface of the alveoli be lined with a microscopic film of **pulmonary surfactant** (phospholipids)?",
                "It reduces surface tension in alveolar fluid, preventing alveoli from collapsing during exhalation",
                [
                    "It oxidizes carbon dioxide into solid carbonate crystals",
                    "It acts as a digestive enzyme hydrolyzing airborne pathogens",
                    "It actively pumps oxygen against its partial pressure gradient",
                ],
                "Pulmonary surfactant synthesized by Type II alveolar cells lowers surface tension to prevent alveolar atelectasis (collapse) during expiration.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_gas_exchange_requirements",
            q[0],
            q[1],
            q[2],
            q[3],
            "surfactant_function_misconception",
        )

    elif chosen_subskill == "breathing_ventilation_mechanics":
        scenarios = [
            (
                "During active **inhalation (inspiration)** in humans, what sequence of muscular actions and pressure changes occurs?",
                "Diaphragm contracts and flattens; external intercostal muscles contract lifting ribs up and out; thoracic volume increases; intrathoracic pressure drops below atmospheric pressure, drawing air in",
                [
                    "Diaphragm relaxes into dome shape; internal intercostals contract; thoracic volume decreases; pressure rises, forcing air out",
                    "Abdominal muscles contract; ribs move down and in; thoracic pressure equalizes with blood pressure",
                    "Lungs actively expand via intrinsic muscular fibers; diaphragm remains completely static",
                ],
                "Inhalation is an active process: muscular contraction increases thoracic volume, which reduces internal air pressure below atmospheric pressure, causing air to rush in (Boyle's law).",
            ),
            (
                "During quiet, resting **exhalation (expiration)**, why is the process considered primarily **passive**?",
                "The diaphragm and external intercostal muscles relax, allowing the elastic recoil of the lungs and thoracic cage to compress air out",
                [
                    "Active ATP hydrolysis is required to compress the pleural cavity",
                    "Smooth muscles lining bronchioles contract violently to eject air",
                    "Atmospheric air pressure actively forces its way down the trachea",
                ],
                "Quiet expiration requires no active muscular contraction; elastic recoil of stretched alveolar tissues naturally decreases thoracic volume, elevating pressure.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_gas_exchange_ventilation",
            q[0],
            q[1],
            q[2],
            q[3],
            "inhalation_exhalation_pressure_inversion",
        )

    elif chosen_subskill == "gas_transport_mechanisms":
        scenarios = [
            (
                "In what primary form is the majority (~70%) of **carbon dioxide** transported in human blood from respiring tissues to the lungs?",
                "As soluble bicarbonate ions (HCO3-) dissolved in blood plasma",
                [
                    "As gaseous bubbles of CO2 dissolved under pressure in arterial blood",
                    "Bound irreversibly to the heme iron of hemoglobin as carboxyhemoglobin",
                    "As solid urea granules inside white blood cells",
                ],
                "CO2 enters RBCs, where carbonic anhydrase catalyzes its conversion into carbonic acid, which dissociates into H+ and bicarbonate ions (HCO3-) that diffuse into plasma via the chloride shift.",
            ),
            (
                "How is **oxygen** transported in human blood from alveolar capillary beds to systemic tissue cells?",
                "~98,5% reversibly bound to the iron (Fe2+) atoms in hemoglobin molecules as oxyhemoglobin (HbO8)",
                [
                    "~98,5% dissolved as free gas bubbles directly in blood plasma",
                    "Bound to albumin proteins in the lymphatic fluid",
                    "Chemically converted into water by catalase enzymes in platelets",
                ],
                "Oxygen has very low solubility in water; almost all oxygen is transported bound to the four iron-containing heme groups of each hemoglobin molecule.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_gas_exchange_transport",
            q[0],
            q[1],
            q[2],
            q[3],
            "co2_bicarbonate_vs_carbaminohemoglobin_confusion",
        )

    else:  # homeostatic_co2_control
        scenarios = [
            (
                "During intense exercise, cellular respiration in muscle cells produces large quantities of CO2. How does the body sense and correct this hypercapnia?",
                "Elevated blood CO2 lowers blood pH; chemoreceptors in the carotid artery and aorta send nerve impulses to the medulla oblongata, which stimulates faster, deeper breathing to exhale CO2",
                [
                    "Elevated CO2 stimulates the pancreas to secrete glucagon, neutralizing blood acid",
                    "Stretch receptors in the bronchioles immediately shut off blood flow to muscles",
                    "The kidneys instantly excrete gaseous CO2 directly into the urinary bladder",
                ],
                "Carbon dioxide is the primary chemical driver of breathing rate; decreased pH (acidosis) is detected by central and peripheral chemoreceptors, triggering medullary respiratory acceleration.",
            ),
            (
                "What dangerous physiological condition occurs if high blood CO2 levels cause blood pH to drop significantly below the normal homeostatic range (7,35 - 7,45)?",
                "Acidosis, which risks denaturing vital metabolic enzymes and impairing neural transmission",
                [
                    "Alkalosis, which causes excess glycogen crystallization in liver cells",
                    "Hypothermia, due to rapid cooling of pulmonary capillaries",
                    "Anemia, caused by spontaneous rupture of erythrocyte membranes",
                ],
                "Respiratory acidosis occurs when inadequate ventilation causes CO2 accumulation, forming excess carbonic acid (H2CO3) and lowering systemic blood pH.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_gas_exchange_co2_homeostasis",
            q[0],
            q[1],
            q[2],
            q[3],
            "co2_primary_breathing_driver_misconception",
        )


def _format_mcq(
    seed: int,
    lo_id: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    explanation: str,
    misconception: str,
) -> Dict[str, Any]:
    options = [correct] + distractors
    random.Random(seed).shuffle(options)
    return {
        "id": f"{lo_id}_{seed}",
        "term": 3,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 3,
        "learning_objective_id": lo_id,
        "misconception_tags": [misconception],
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "hints": [
            "Consider the physiological principles governing human Gaseous Exchange and ventilation.",
            f"Key concept: {explanation[:80]}...",
            f"The correct biological answer is: {correct}.",
        ],
        "worked_solution": f"Correct Answer: {correct}. Explanation: {explanation}",
    }
