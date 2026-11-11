"""Natural Sciences Grade 9 Term 1: Digestive System Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Digestive system.md (realigned from Term 4 to Term 1)
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. alimentary_canal_anatomy: Macroscopic digestive organs (calls build_digestive_question).
2. mechanical_vs_chemical_digestion: Mastication and peristalsis vs enzymatic/acid hydrolysis.
3. villus_histology_and_absorption: Microscopic small intestine villus structure (calls build_villus_question).
4. laboratory_food_tests: Practical testing for starch (Iodine), glucose (Benedict's), protein (Biuret), fats (Ethanol).
5. dietary_health_and_disorders: Balanced nutrition, eating disorders, ulcers, cirrhosis, and malnutrition.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import (
    build_digestive_question,
    build_villus_question,
)

TOPIC_NAME = "Digestive system"
ORDERED_SUBSKILLS = [
    "alimentary_canal_anatomy",
    "mechanical_vs_chemical_digestion",
    "villus_histology_and_absorption",
    "laboratory_food_tests",
    "dietary_health_and_disorders",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_dig"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "title" not in res or not res["title"]:
        res["title"] = "Human Digestive System Anatomy & Absorption"
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
    elif subskill in ("alimentary_canal_anatomy", "digestive_anatomy", "diagram"):
        return _normalize_res(build_digestive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))
    elif subskill in ("villus", "villi", "absorption_villus"):
        return _normalize_res(build_villus_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Alimentary Canal Anatomy (Macro Plate)
    if chosen_subskill == "alimentary_canal_anatomy":
        return _normalize_res(build_digestive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))

    # Subskill 2: Mechanical vs Chemical Digestion
    if chosen_subskill == "mechanical_vs_chemical_digestion":
        question_text = (
            "Digestion in humans comprises both mechanical and chemical processes.\n\n"
            "1. Define the difference between **mechanical digestion** and **chemical digestion**.\n"
            "2. Name and describe the wave-like muscular contraction that moves food down the oesophagus.\n"
            "3. State the two essential chemical substances present in **gastric juice** in the stomach, and give the function of each."
        )
        sample = (
            "1. **Mechanical Digestion:** Physical breakdown, crushing, and mashing of food into smaller pieces to increase surface area without breaking chemical bonds (e.g. chewing, churning, emulsification);\n"
            "   **Chemical Digestion:** Breakdown of large, insoluble food molecules into small, soluble molecules by chemical action and digestive enzymes (hydrolysis);\n"
            "2. **Peristalsis:** Involuntary, rhythmic waves of circular and longitudinal muscle contraction and relaxation along the digestive tract that push the food bolus forward;\n"
            "3. **Gastric Juices:**\n"
            "   • **Hydrochloric Acid (HCl):** Provides an acidic pH (~2) to kill ingested bacteria and activates pepsinogen into active pepsin;\n"
            "   • **Pepsin (Protease enzyme):** Chemically breaks down complex proteins into shorter polypeptide chains."
        )
        marking = (
            "• 2 marks: Accurate distinction between mechanical (physical breakdown / surface area) [1] and chemical (enzymatic breakdown into soluble molecules) [1]\n"
            "• 1 mark: Peristalsis with rhythmic muscular contraction description [1]\n"
            "• 2 marks: Hydrochloric acid (kills bacteria / acidic pH) [1] and Pepsin (protein digestion) [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Mechanical vs Chemical Digestion & Peristalsis",
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
                "Mechanical digestion changes the physical size of food; chemical digestion uses enzymes to break chemical bonds.",
                "The muscular squeeze down the oesophagus is called peristalsis.",
                "Mechanical: physical breakdown. Chemical: enzyme hydrolysis. Peristalsis: rhythmic muscular wave. Gastric juice: HCl + pepsin.",
            ],
            "misconception_tags": ["peristalsis_gravity_fallacy", "bile_is_enzyme_misconception"],
            "learning_objective_id": "NS9.LL.05.02",
        }

    # Subskill 3: Villus Histology & Absorption (Microscopic Plate)
    if chosen_subskill == "villus_histology_and_absorption":
        if actual_seed % 2 == 0:
            return _normalize_res(build_villus_question(actual_seed, grade=9, mode=mode))
        question_text = (
            "The small intestine (ileum) is highly adapted for the absorption of digested nutrients into the bloodstream.\n\n"
            "1. Name the microscopic finger-like projections lining the wall of the small intestine.\n"
            "2. State **three structural adaptations** of these finger-like projections that enhance absorption efficiency.\n"
            "3. Name the central vessel inside each projection that absorbs fatty acids and glycerol, and state the fluid it carries."
        )
        sample = (
            "1. **Projections:** Villi (singular: villus);\n"
            "2. **Structural Adaptations:**\n"
            "   • Large cumulative surface area (millions of villi and microscopic microvilli brush border);\n"
            "   • Extremely thin surface layer (single-cell-thick epithelium) for short diffusion distance;\n"
            "   • Dense capillary network in close contact with epithelium to rapidly transport amino acids and glucose away, maintaining steep concentration gradient;\n"
            "   • Rich supply of central lacteals for lipid absorption;\n"
            "3. **Central Vessel:** Lacteal (lymph capillary); **Fluid:** Lymph (chyle)."
        )
        marking = (
            "• 1 mark: Villi [1]\n"
            "• 3 marks: Three structural adaptations (large surface area, 1-cell epithelium, dense capillaries, lacteal) [3]\n"
            "• 1 mark: Lacteal carrying lymph [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Small Intestine Villus Structure & Absorption",
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
                "The finger-like projections in the small intestine are villi.",
                "They have very thin 1-cell walls, huge surface area, and a rich blood supply.",
                "Finger projections: Villi. Adaptations: thin epithelium, high surface area, capillaries. Central vessel: lacteal.",
            ],
            "misconception_tags": ["villus_absorption_misconception", "lacteal_blood_vessel_error"],
            "learning_objective_id": "NS9.LL.05.03",
        }

    # Subskill 4: Laboratory Food Tests (Practical Investigation)
    if chosen_subskill == "laboratory_food_tests":
        food_tests = [
            (
                "Starch (Complex Carbohydrate)",
                "Iodine Solution",
                "Yellow-brown / amber",
                "Blue-black",
                "starch_iodine_test_error",
            ),
            (
                "Glucose (Reducing Sugar)",
                "Benedict's Solution (heated in water bath)",
                "Clear blue",
                "Green → Yellow → Orange → Brick-red precipitate",
                "benedict_heat_omission_error",
            ),
            (
                "Protein",
                "Biuret Reagent (Sodium Hydroxide + dilute Copper Sulfate)",
                "Pale blue",
                "Violet / Purple / Mauve",
                "biuret_color_confusion",
            ),
            (
                "Fats & Oils (Lipids)",
                "Ethanol Emulsion Test (or Translucent Grease Spot on paper)",
                "Clear colorless ethanol",
                "Milky white cloudy emulsion (or permanent translucent spot)",
                "lipid_emulsion_misconception",
            ),
        ]
        target_test = food_tests[actual_seed % len(food_tests)]
        question_text = (
            "Grade 9 learners investigated the nutritional components of food samples in a science laboratory.\n\n"
            f"1. Name the chemical reagent used to test for the presence of **{target_test[0]}**.\n"
            "2. State the initial color of this reagent before adding the food sample.\n"
            f"3. State the **positive diagnostic color change** observed if {target_test[0]} is present.\n"
            "4. If heating is required during this procedure, explain why a water bath is used instead of heating directly over an open flame."
        )
        sample = (
            f"1. **Reagent:** {target_test[1]};\n"
            f"2. **Initial Color:** {target_test[2]};\n"
            f"3. **Positive Result:** {target_test[3]};\n"
            "4. A water bath provides gentle, even heating and prevents flammable reagents (such as ethanol) from catching fire or boiling liquids violently spurting out of the test tube."
        )
        marking = (
            f"• 1 mark: Correct reagent ({target_test[1]}) [1]\n"
            f"• 1 mark: Initial reagent color ({target_test[2]}) [1]\n"
            f"• 1 mark: Diagnostic positive color change ({target_test[3]}) [1]\n"
            "• 1 mark: Water bath safety rationale (even temperature / prevents ignition of flammable reagents) [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"Food Test: {target_test[0]}",
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
                f"Recall which standard laboratory reagent tests for {target_test[0]}.",
                f"What color does {target_test[1].split('(')[0].strip()} turn when it detects {target_test[0]}?",
                f"Reagent: {target_test[1]}. Initial: {target_test[2]}. Positive: {target_test[3]}. Water bath for safety.",
            ],
            "misconception_tags": [target_test[4], "food_test_reagent_conflation"],
            "learning_objective_id": "NS9.LL.05.04",
        }

    # Subskill 5: Dietary Health and Disorders
    disorders = [
        (
            "Stomach Ulcers",
            "Sores or lesions developing in the mucus lining of the stomach",
            "Acidic gastric juice (HCl) and pepsin eroding unprotected stomach wall, often exacerbated by Helicobacter pylori bacterial infection, stress, or NSAID drugs",
            "Antacid medications to neutralize stomach acid, antibiotics for bacterial infection, avoiding highly acidic foods",
            "ulcer_etiology_confusion",
        ),
        (
            "Anorexia Nervosa",
            "A serious psychological eating disorder characterized by extreme voluntary self-starvation and intense fear of weight gain",
            "Severe nutrient deprivation, muscle wasting, bone density loss, extreme weakness, and immune suppression",
            "Psychological counseling, monitored clinical refeeding, nutritional therapy",
            "anorexia_dietary_conflation",
        ),
        (
            "Kwashiorkor",
            "Severe protein deficiency malnutrition occurring in young children",
            "Distended swollen abdomen (oedema/ascites), stunted growth, reddish-orange thinned hair, and weakened immunity",
            "Providing a diet rich in complete protein sources (milk, eggs, legumes, soya, fish)",
            "kwashiorkor_marasmus_confusion",
        ),
        (
            "Liver Cirrhosis",
            "Chronic degenerative scarring and fibrosis of liver tissue replacing functional hepatocytes",
            "Prolonged heavy alcohol abuse or chronic viral hepatitis leading to loss of bile production, toxin accumulation, and liver failure",
            "Abstaining completely from alcohol, balanced low-sodium diet, medical antiviral therapy",
            "cirrhosis_mechanism_error",
        ),
    ]
    dis = disorders[actual_seed % len(disorders)]
    question_text = (
        f"Inappropriate eating plans and substance abuse cause severe digestive and systemic health disorders.\n\n"
        f"1. Describe the biological nature of **{dis[0]}**.\n"
        f"2. Explain the **underlying physiological cause** of this condition.\n"
        f"3. State **two medical or dietary interventions** used to treat or manage this disorder."
    )
    sample = (
        f"1. **Nature of Disorder:** {dis[1]};\n"
        f"2. **Physiological Cause:** {dis[2]};\n"
        f"3. **Treatment / Interventions:** {dis[3]}."
    )
    marking = (
        f"• 1 mark: Clear description of condition ({dis[1]}) [1]\n"
        f"• 2 marks: Accurate physiological cause ({dis[2]}) [2]\n"
        f"• 1 mark: Valid treatment / dietary intervention ({dis[3]}) [1]\n"
        "**Total: 4 marks**"
    )
    return {
        "title": f"Digestive Health: {dis[0]}",
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
            f"Think about what goes wrong in the digestive tract during {dis[0]}.",
            f"What dietary deficiency or chemical erosion causes {dis[0]}?",
            f"Condition: {dis[1]}. Cause: {dis[2]}. Interventions: {dis[3]}.",
        ],
        "misconception_tags": [dis[4], "digestive_disorder_etiology_error"],
        "learning_objective_id": "NS9.LL.05.05",
    }
