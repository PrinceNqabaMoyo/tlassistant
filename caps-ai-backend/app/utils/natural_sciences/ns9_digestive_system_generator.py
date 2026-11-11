"""Natural Sciences Grade 9 Term 1: Digestive System Topic Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Digestive system.md
- curriculum_docs/NaturalSciences_Gr9/Term 1/Digestive_system.md

Subskills:
1. alimentary_canal_anatomy: Sequential structures and macroscopic organs (diagram questions).
2. mechanical_vs_chemical: Mastication and peristalsis vs enzymatic breakdown.
3. enzymes_and_secretions: Salivary amylase, gastric pepsin, pancreatic lipase, bile emulsification.
4. absorption_and_egestion: Small intestine assimilation and large intestine water absorption.
5. health_and_diet: Malnutrition, balanced diets, ulcers, and dental decay.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import build_digestive_question


SUBSKILLS = [
    "alimentary_canal_anatomy",
    "mechanical_vs_chemical",
    "enzymes_and_secretions",
    "absorption_and_egestion",
    "health_and_diet",
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

    if chosen_subskill in ("alimentary_canal_anatomy", "diagram", "diagram_label", "anatomy"):
        return build_digestive_question(actual_seed, grade=9, mode=mode, subskill=chosen_subskill)

    # Conceptual & Procedural Subskills
    subskills_pool = [
        "mechanical_vs_chemical",
        "enzymes_and_secretions",
        "absorption_and_egestion",
        "health_and_diet",
    ]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "mechanical_vs_chemical":
        scenarios = [
            (
                "Which process represents **mechanical digestion** rather than chemical digestion?",
                "Churning of food in the stomach into liquid chyme",
                [
                    "Hydrolysis of starch into maltose by salivary amylase",
                    "Breakdown of polypeptides into peptides by gastric pepsin",
                    "Cleavage of triglycerides into fatty acids and glycerol by lipase",
                ],
                "Mechanical digestion physically breaks food into smaller pieces to increase surface area without breaking chemical bonds.",
            ),
            (
                "What is the biological purpose of rhythmic contractions of smooth circular and longitudinal muscles in the esophagus?",
                "Peristalsis to propel the food bolus towards the stomach",
                [
                    "Mastication to grind insoluble dietary fiber",
                    "Emulsification of hydrophobic lipid droplets",
                    "Ultrafiltration of soluble vitamins into blood capillaries",
                ],
                "Peristalsis consists of involuntary waves of muscular contraction that push food along the alimentary canal.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ns9_digestive_mechanical_chemical",
            q[0],
            q[1],
            q[2],
            q[3],
            "mechanical_vs_chemical_confusion",
        )

    elif chosen_subskill == "enzymes_and_secretions":
        scenarios = [
            (
                "Where is **bile** produced, and what is its primary mechanical function in digestion?",
                "Produced in the liver; emulsifies large fat droplets into micro-droplets",
                [
                    "Produced in the gall bladder; chemically digests proteins into amino acids",
                    "Produced in the stomach; neutralizes acidic chyme in the mouth",
                    "Produced in the pancreas; hydrolyzes complex starch into glucose",
                ],
                "Bile is synthesized by hepatocytes in the liver (stored in gallbladder) and emulsifies fats, multiplying surface area for lipase.",
            ),
            (
                "Gastric juice in the stomach contains hydrochloric acid (HCl). What is its primary enzymatic role?",
                "Provides an acidic pH of ~2 to activate pepsinogen into active pepsin",
                [
                    "Neutralizes alkaline saliva to protect tooth enamel",
                    "Synthesizes vitamin D from dietary calcium ions",
                    "Breaks down dietary cellulose into soluble sucrose",
                ],
                "HCl creates the optimal acidic pH (~1,5 - 2,0) required for pepsin to break down proteins into polypeptides.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ns9_digestive_enzymes_secretions",
            q[0],
            q[1],
            q[2],
            q[3],
            "bile_origin_function_misconception",
        )

    elif chosen_subskill == "absorption_and_egestion":
        scenarios = [
            (
                "Most chemical digestion and nutrient absorption takes place in the small intestine. Why is its inner wall folded into thousands of microscopic villi?",
                "To dramatically increase the surface area for rapid absorption of nutrients",
                [
                    "To generate peristaltic friction against indigestible fiber",
                    "To produce bile salts that coagulate gastric acid",
                    "To store glycogen for emergency cellular respiration",
                ],
                "Villi and microvilli create a massive surface area to maximize the passive and active absorption of glucose, amino acids, and fatty acids.",
            ),
            (
                "What is the primary physiological consequence if the colon (large intestine) is irritated or infected, leading to rapid transit of waste?",
                "Diarrhea due to reduced water reabsorption, risking dehydration",
                [
                    "Constipation due to excessive water extraction into blood",
                    "Kwashiorkor due to acute protein deficiency",
                    "Scurvy due to lack of ascorbic acid",
                ],
                "The large intestine's primary role is reabsorbing water from indigestible waste; failed reabsorption results in watery diarrhea.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ns9_digestive_absorption_egestion",
            q[0],
            q[1],
            q[2],
            q[3],
            "colon_water_reabsorption_failure",
        )

    else:  # health_and_diet
        scenarios = [
            (
                "A child consuming a diet composed almost exclusively of refined maize meal (carbohydrates) develops a swollen abdomen (edema) and muscle wasting. Which nutritional condition is indicated?",
                "Kwashiorkor (severe protein deficiency)",
                [
                    "Marasmus (total calorie starvation)",
                    "Scurvy (vitamin C deficiency)",
                    "Rickets (vitamin D / calcium deficiency)",
                ],
                "Kwashiorkor is caused by severe protein deficiency, leading to reduced plasma proteins, osmotic imbalance, and fluid retention in tissues (edema).",
            ),
            (
                "Why is dietary roughage (insoluble fiber/cellulose) essential in the human diet even though humans lack cellulase enzymes to digest it?",
                "It adds bulk to the feces, stimulating peristaltic muscle contractions and preventing constipation",
                [
                    "It is converted into essential amino acids by stomach acid",
                    "It binds with hemoglobin to accelerate oxygen transport",
                    "It dissolves cholesterol plaque inside coronary arteries",
                ],
                "Insoluble fiber provides physical bulk that triggers stretch receptors in the intestinal wall, stimulating peristalsis.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ns9_digestive_health_diet",
            q[0],
            q[1],
            q[2],
            q[3],
            "kwashiorkor_vs_marasmus_confusion",
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
        "term": 1,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 2,
        "learning_objective_id": lo_id,
        "misconception_tags": [misconception],
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "hints": [
            "Review the specific physiological roles of digestive organs and secretions.",
            f"Key concept: {explanation[:80]}...",
            f"The correct biological answer is: {correct}.",
        ],
        "worked_solution": f"Correct Answer: {correct}. Explanation: {explanation}",
    }
