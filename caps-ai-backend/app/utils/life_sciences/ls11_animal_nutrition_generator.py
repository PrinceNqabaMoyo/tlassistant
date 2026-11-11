"""Life Sciences Grade 11 Term 2: Animal Nutrition Topic Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr11/Term 2/04. Animal nutrition.md
- curriculum_docs/LifeSciences_Gr11/Term 2/Animal_nutrition.md

Subskills:
1. villus_and_macroscopic_anatomy: Microscopic villus and macroscopic alimentary canal (diagram questions).
2. dentition_dietary_adaptations: Dentition differences in herbivores, carnivores, omnivores.
3. chemical_digestion_enzymes: Digestive enzymes, substrates, end-products, pH optima.
4. villus_absorption_mechanisms: Lacteal vs capillary absorption, hepatic portal system.
5. homeostatic_glucose_control: Islets of Langerhans, insulin, glucagon negative feedback.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import (
    build_digestive_question,
    build_villus_question,
)


SUBSKILLS = [
    "villus",
    "digestive",
    "dentition_dietary_adaptations",
    "chemical_digestion_enzymes",
    "villus_absorption_mechanisms",
    "homeostatic_glucose_control",
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

    if chosen_subskill in ("villus_and_macroscopic_anatomy", "diagram", "villus", "digestive", "human_digestive_system", "digestive_system", "intestinal_villus"):
        if chosen_subskill in ("digestive", "human_digestive_system", "digestive_system"):
            return build_digestive_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)
        elif chosen_subskill in ("villus", "intestinal_villus"):
            return build_villus_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)
        elif actual_seed % 2 == 0:
            return build_villus_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)
        else:
            return build_digestive_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)

    subskills_pool = [
        "dentition_dietary_adaptations",
        "chemical_digestion_enzymes",
        "villus_absorption_mechanisms",
        "homeostatic_glucose_control",
    ]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "dentition_dietary_adaptations":
        scenarios = [
            (
                "How does the skull and dentition of an obligate **herbivore** (e.g. sheep or cow) differ from a carnivore?",
                "Presence of a diastema (gap) between incisors and premolars to manipulate plant food, with broad flat molars for grinding",
                [
                    "Presence of large pointed carnassial teeth adapted for shearing bone and muscle tissue",
                    "A fused dental plate with sharp hooked fangs for venom injection",
                    "Complete absence of molars with rows of continuous replacement incisors",
                ],
                "Herbivores have a horny pad, incisors biting against it, a diastema to manipulate grass boluses, and ridged molars for grinding cellulose.",
            ),
            (
                "What is the specialized function of the modified **carnassial teeth** (last upper premolar and first lower molar) in carnivores?",
                "Act like scissors with sharp scissor-action edges to shear meat and crack bone",
                [
                    "Grind fibrous cellulolytic plant matter into fine pulp",
                    "Filter plankton and aquatic microorganisms from water",
                    "Store calcium carbonate crystals for eggshell synthesis",
                ],
                "Carnassial teeth are specialized shearing teeth in mammalian carnivores that slide past each other like scissor blades.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_nutrition_dentition",
            q[0],
            q[1],
            q[2],
            q[3],
            "herbivore_carnivore_dentition_confusion",
        )

    elif chosen_subskill == "chemical_digestion_enzymes":
        scenarios = [
            (
                "Why does chemical digestion of carbohydrates by salivary amylase **cease** immediately once the food bolus enters the stomach?",
                "The highly acidic gastric juice (pH ~1,5 - 2,0) denatures salivary amylase, which has an optimum neutral pH of ~6,8 - 7,0",
                [
                    "Salivary amylase is consumed by the chemical synthesis of bile pigments",
                    "Stomach peristalsis mechanically destroys all protein bonds in enzymes",
                    "Hydrochloric acid converts amylase into pepsinogen",
                ],
                "Enzymes are globular proteins with specific 3D active sites; the extreme acidity of HCl denatures amylase, inactivating it.",
            ),
            (
                "Which enzyme secreted in pancreatic juice hydrolyzes emulsified triglyceride droplets into absorbable **fatty acids and glycerol**?",
                "Pancreatic lipase",
                [
                    "Pancreatic amylase",
                    "Trypsin",
                    "Maltase",
                ],
                "Pancreatic lipase works in the alkaline duodenum (pH ~8) to hydrolyze fats into fatty acids and glycerol.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_nutrition_enzymes",
            q[0],
            q[1],
            q[2],
            q[3],
            "enzyme_ph_denaturation_misconception",
        )

    elif chosen_subskill == "villus_absorption_mechanisms":
        scenarios = [
            (
                "Following absorption across the microvillar columnar epithelium of the villi, into which circulatory structure are **fatty acids and glycerol** initially absorbed?",
                "Central lacteal (lymphatic vessel)",
                [
                    "Blood capillary network connecting to the hepatic portal vein",
                    "Renal interlobular arteriole",
                    "Inferior vena cava directly",
                ],
                "Lipid breakdown products recombine into chylomicrons and enter the central lacteal, traveling through the thoracic duct into the lymphatic system.",
            ),
            (
                "What is the vital physiological role of the **hepatic portal vein** in human animal nutrition?",
                "Transports blood carrying absorbed water-soluble nutrients (glucose, amino acids) directly from the intestines to the liver for processing",
                [
                    "Transports oxygenated arterial blood from the aorta to the stomach wall",
                    "Transports bile from the gall bladder into the pancreatic duct",
                    "Transports deoxygenated blood from the kidneys to the heart",
                ],
                "The hepatic portal system ensures that all absorbed monosaccharides, amino acids, and toxins pass directly through the liver for glycogen synthesis, deamination, and detoxification.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_nutrition_villus_absorption",
            q[0],
            q[1],
            q[2],
            q[3],
            "lacteal_vs_blood_capillary_confusion",
        )

    else:  # homeostatic_glucose_control
        scenarios = [
            (
                "After a carbohydrate-rich meal, blood glucose levels rise above the set point (approx. 5 mmol/L). Describe the **negative feedback** response:",
                "Beta cells in the Islets of Langerhans secrete insulin, stimulating liver and muscle cells to absorb glucose and convert it into glycogen",
                [
                    "Alpha cells in the Islets of Langerhans secrete glucagon, converting glycogen in the liver into free glucose",
                    "Adrenal medulla secretes aldosterone to reabsorb glucose across the renal collecting ducts",
                    "Thyroid gland secretes thyroxine to slow down cellular respiration in mitochondria",
                ],
                "Insulin lowers blood glucose by accelerating cellular uptake, increasing glycogenesis (glucose -> glycogen), and stimulating fat synthesis.",
            ),
            (
                "During prolonged fasting or rigorous physical exercise, blood glucose drops below the normal homeostatic threshold. What hormonal correction occurs?",
                "Alpha cells in the pancreas secrete glucagon, stimulating liver cells to break down stored glycogen into glucose (glycogenolysis)",
                [
                    "Beta cells secrete insulin, causing excess glucose to be excreted in urine",
                    "Pituitary gland secretes ADH, increasing the volume of blood plasma",
                    "Parathyroid gland secretes calcitonin, stimulating glucose release from bones",
                ],
                "Glucagon elevates blood glucose back to normal levels by promoting hepatic glycogenolysis and gluconeogenesis.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_nutrition_glucose_homeostasis",
            q[0],
            q[1],
            q[2],
            q[3],
            "insulin_glucagon_inversion",
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
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "learning_objective_id": lo_id,
        "misconception_tags": [misconception],
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "hints": [
            "Consider the physiological adaptations and regulatory mechanisms in Animal Nutrition.",
            f"Key biological principle: {explanation[:80]}...",
            f"The correct biological answer is: {correct}.",
        ],
        "worked_solution": f"Correct Answer: {correct}. Explanation: {explanation}",
    }
