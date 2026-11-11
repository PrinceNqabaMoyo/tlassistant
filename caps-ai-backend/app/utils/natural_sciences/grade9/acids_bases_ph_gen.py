"""Natural Sciences Grade 9 Term 2: Acids, Bases and pH Value Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/04. Acids bases and the pH value.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. ph_scale_and_classification: pH scale 1 to 14, acidic (1-6), neutral (7), basic (8-14), strength variation.
2. universal_indicator_spectrum: Universal indicator color progression (red/orange/yellow -> green -> blue/purple).
3. acid_base_indicators_comparison: Litmus (red/blue), bromothymol blue, phenolphthalein, and natural indicators (red cabbage).
4. household_substances_ph_ranking: Ranking common household substances by acidity, neutrality, and basicity.
5. acid_safety_and_dilution_protocol: Safe dilution protocol (add acid to water), thermal safety, and laboratory precautions.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Acids, bases and pH value"
ORDERED_SUBSKILLS = [
    "ph_scale_and_classification",
    "universal_indicator_spectrum",
    "acid_base_indicators_comparison",
    "household_substances_ph_ranking",
    "acid_safety_and_dilution_protocol",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_abph"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 2) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    elif "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["grade"] = "9"
    res["term"] = term
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
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: pH Scale and Classification
    if chosen_subskill == "ph_scale_and_classification":
        samples = [
            ("Solution A (pH 1)", "strong acid", "high concentration of hydrogen ions", "battery acid / gastric juice"),
            ("Solution B (pH 5)", "weak acid", "low concentration of acidic ions", "black coffee / unpolluted rain"),
            ("Solution C (pH 7)", "neutral substance", "balanced hydrogen and hydroxide ions", "pure distilled water"),
            ("Solution D (pH 9)", "weak base", "low concentration of hydroxide ions", "baking soda solution"),
            ("Solution E (pH 14)", "strong base", "high concentration of hydroxide ions", "drain cleaner / sodium hydroxide"),
        ]
        chosen = samples[actual_seed % len(samples)]
        question_text = (
            "The pH scale is a continuous numerical scale used by scientists to measure the relative acidity or basicity of aqueous solutions.\n\n"
            "1. State the **complete numerical range** of the standard pH scale.\n"
            f"2. Classify **{chosen[0]}** as an acid, a neutral substance, or a base, stating whether it is strong or weak.\n"
            f"3. Explain what a pH value of **{chosen[0].split('(')[1].rstrip(')')}** indicates about the chemical nature of this solution.\n"
            "4. Contrast how the strength of an acid changes as its pH decreases from 6 towards 1."
        )
        sample = (
            "1. **pH Scale Range:** The standard pH scale extends from **1 to 14** (with 7 representing neutral);\n"
            f"2. **Classification:** {chosen[0]} is classified as a **{chosen[1]}**;\n"
            f"3. **Chemical Nature:** It indicates a {chosen[2]}, characteristic of substances such as {chosen[3]};\n"
            "4. **Acidity Trend:** As the pH value decreases towards 1, the acidity and concentration of active acidic ions **increase exponentially** (lower pH = stronger acid)."
        )
        marking = (
            "• 1 mark: Correct pH range (1 to 14) [1]\n"
            f"• 1 mark: Correct classification as {chosen[1]} [1]\n"
            f"• 1 mark: Explanation relating pH to chemical nature ({chosen[2]}) [1]\n"
            "• 1 mark: Clear understanding that decreasing pH denotes increasing acid strength [1]\n"
            "**Total: 4 marks**"
        )
        return _normalize_res({
            "title": "The pH Scale: Acidity and Basicity",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "The pH scale runs from 1 to 14, where 7 is pure neutral.",
                "Substances below 7 are acids (1 is strongest); substances above 7 are bases (14 is strongest).",
                f"{chosen[0]} is below 7 for acids or above 7 for bases. Decreasing pH means increasing acid strength.",
            ],
            "misconception_tags": ["higher_ph_equals_stronger_acid_myth", "ph_7_is_acidic_myth"],
            "learning_objective_id": "NS9.MM.10.01",
        })

    # Subskill 2: Universal Indicator Spectrum
    if chosen_subskill == "universal_indicator_spectrum":
        tests = [
            ("Lemon juice (pH 2)", "Red", "Strongly acidic"),
            ("Tomato juice (pH 4)", "Orange", "Moderately acidic"),
            ("Milk (pH 6)", "Yellow", "Weakly acidic"),
            ("Pure water (pH 7)", "Green", "Neutral"),
            ("Sea water (pH 8)", "Blue-green", "Weakly basic"),
            ("Baking soda solution (pH 9)", "Blue", "Moderately basic"),
            ("Bleach / Sodium hydroxide (pH 13)", "Purple / Violet", "Strongly basic"),
        ]
        t = tests[actual_seed % len(tests)]
        question_text = (
            "Universal indicator is a mixture of chemical dyes that changes through a continuous spectrum of colours across the pH scale.\n\n"
            f"1. A learner adds three drops of universal indicator to a test tube containing **{t[0]}**.\n"
            "   State the **predicted colour** observed in the test tube.\n"
            f"2. Deduce whether the solution is **strongly acidic, weakly acidic, neutral, weakly basic, or strongly basic**.\n"
            "3. State the characteristic colour of universal indicator in a **completely neutral solution (pH 7)**.\n"
            "4. Why is universal indicator superior to single-colour litmus paper when measuring unknown chemical solutions?"
        )
        sample = (
            f"1. **Predicted Colour:** **{t[1]}**;\n"
            f"2. **Deduction:** **{t[2]}**;\n"
            "3. **Neutral Colour:** Universal indicator turns **Green** in a neutral solution (pH 7);\n"
            "4. **Comparative Superiority:** Litmus paper only indicates whether a solution is an acid or base (binary test: red or blue), whereas universal indicator displays a full colour spectrum that reveals the **approximate quantitative pH value and relative strength** of the solution."
        )
        marking = (
            f"• 1 mark: Correct predicted colour ({t[1]}) [1]\n"
            f"• 1 mark: Correct acidity/basicity strength classification ({t[2]}) [1]\n"
            "• 1 mark: Correct identification of green as the neutral colour [1]\n"
            "• 1 mark: Valid explanation of universal indicator providing quantitative pH range vs binary litmus [1]\n"
            "**Total: 4 marks**"
        )
        return _normalize_res({
            "title": "Universal Indicator Colour Spectrum",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Universal indicator turns red/orange/yellow in acids, green in neutral, and blue/purple in bases.",
                "Green indicates exact neutrality (pH 7).",
                f"{t[0]} has a specific pH and turns {t[1]}. It allows measuring approximate pH strength, unlike simple litmus.",
            ],
            "misconception_tags": ["universal_indicator_is_always_green_myth", "blue_means_cold_not_base_myth"],
            "learning_objective_id": "NS9.MM.10.02",
        })

    # Subskill 3: Acid-Base Indicators Comparison
    if chosen_subskill == "acid_base_indicators_comparison":
        question_text = (
            "Chemical indicators change colour in response to the concentration of hydrogen ions in a solution.\n\n"
            "Complete the scientific indicator reference table by describing the expected colour in each condition:\n\n"
            "| Indicator | Colour in Acid (pH < 7) | Colour in Neutral (pH 7) | Colour in Base (pH > 7) |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Red Litmus Paper** | *(a)* | Red | *(b)* |\n"
            "| **Blue Litmus Paper** | *(c)* | Blue | *(d)* |\n"
            "| **Bromothymol Blue** | Yellow | *(e)* | Blue |\n"
            "| **Phenolphthalein** | Colourless | Colourless | *(f)* |\n\n"
            "State the correct observation for labels **(a)** through **(f)**."
        )
        sample = (
            "• **(a):** Remains **Red** (acids keep red litmus red);\n"
            "• **(b):** Turns **Blue** (bases turn red litmus blue);\n"
            "• **(c):** Turns **Red** (acids turn blue litmus red);\n"
            "• **(d):** Remains **Blue** (bases keep blue litmus blue);\n"
            "• **(e):** **Green** (bromothymol blue is green in neutral conditions);\n"
            "• **(f):** **Pink / Magenta** (phenolphthalein turns bright pink in alkaline/basic solutions)."
        )
        marking = (
            "• 1 mark: (a) Remains red [1]\n"
            "• 1 mark: (b) Turns blue [1]\n"
            "• 1 mark: (c) Turns red [1]\n"
            "• 1 mark: (d) Remains blue [1]\n"
            "• 1 mark: (e) Green [1]\n"
            "• 1 mark: (f) Pink / Magenta [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Laboratory Indicators: Litmus, Bromothymol Blue & Phenolphthalein",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Acids turn blue litmus red; bases turn red litmus blue.",
                "Bromothymol blue is yellow in acid, green in neutral, blue in base.",
                "Phenolphthalein is colourless in acid and neutral, but turns vibrant pink in base.",
            ],
            "misconception_tags": ["phenolphthalein_turns_blue_myth", "acids_turn_red_litmus_blue_confusion"],
            "learning_objective_id": "NS9.MM.10.03",
        })

    # Subskill 4: Household Substances pH Ranking
    if chosen_subskill == "household_substances_ph_ranking":
        domestic_sets = [
            [
                ("Gastric juice (stomach)", 1.5, "Strong acid"),
                ("Vinegar (ethanoic acid)", 3.0, "Acid"),
                ("Black coffee", 5.0, "Weak acid"),
                ("Pure distilled water", 7.0, "Neutral"),
                ("Baking soda solution", 8.5, "Weak base"),
                ("Household ammonia cleaner", 11.5, "Strong base"),
            ],
            [
                ("Lemon juice (citric acid)", 2.2, "Strong acid"),
                ("Sour milk / yogurt", 4.5, "Weak acid"),
                ("Table salt solution", 7.0, "Neutral"),
                ("Toothpaste", 8.0, "Weak base"),
                ("Soapy handwash water", 9.5, "Base"),
                ("Oven drain cleaner (caustic soda)", 13.5, "Strong base"),
            ],
        ]
        subset = domestic_sets[actual_seed % len(domestic_sets)]
        shuffled = list(subset)
        r.shuffle(shuffled)
        items_str = "\n".join([f"• {name}" for name, _, _ in shuffled])

        question_text = (
            "A group of Natural Sciences learners tested common domestic solutions using a calibrated electronic pH probe and recorded the following substances in random order:\n\n"
            f"{items_str}\n\n"
            "1. Arrange these six domestic substances in order of **increasing pH (from most acidic to most basic)**.\n"
            "2. Identify the substance that is **neutral** (pH ≈ 7).\n"
            "3. State **two physical properties** that distinguish acidic household liquids from basic household liquids (e.g., taste, feel)."
        )
        ordered_names = [name for name, _, _ in sorted(subset, key=lambda x: x[1])]
        sample = (
            "1. **Increasing pH Order (Most Acidic to Most Basic):**\n"
            f"   1. {ordered_names[0]} (pH ≈ {subset[0][1]})\n"
            f"   2. {ordered_names[1]} (pH ≈ {subset[1][1]})\n"
            f"   3. {ordered_names[2]} (pH ≈ {subset[2][1]})\n"
            f"   4. {ordered_names[3]} (pH ≈ {subset[3][1]})\n"
            f"   5. {ordered_names[4]} (pH ≈ {subset[4][1]})\n"
            f"   6. {ordered_names[5]} (pH ≈ {subset[5][1]});\n"
            f"2. **Neutral Substance:** **{subset[3][0]}** (pH = 7.0);\n"
            "3. **Physical Properties:**\n"
            "   • **Acids:** Taste sour (tart) and feel rough or squeaky between fingers;\n"
            "   • **Bases:** Taste bitter and feel slippery or soapy to the touch."
        )
        marking = (
            "• 2 marks: Correct ascending sequence from lowest to highest pH [2] (1 mark for partial order)\n"
            f"• 1 mark: Identification of {subset[3][0]} as neutral [1]\n"
            "• 2 marks: Two distinguishing physical properties (taste sour vs bitter [1], feel rough vs slippery/soapy [1])\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Domestic Substances: pH Hierarchy & Physical Properties",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Acids have the lowest pH values (stomach acid, citrus juice, vinegar).",
                "Pure water and neutral salts have a pH around 7.",
                "Cleaners, soap, and drain unblockers are alkaline with high pH above 7.",
            ],
            "misconception_tags": ["all_chemicals_in_homes_are_acids_myth", "soapy_water_is_acidic_myth"],
            "learning_objective_id": "NS9.MM.10.04",
        })

    # Subskill 5: Acid Safety and Dilution Protocol
    scenarios = [
        ("concentrated Hydrochloric acid (HCl)", "corrosive choking fumes and skin burns"),
        ("concentrated Sulfuric acid (H2SO4)", "severe dehydration of organic tissue and intense heat release"),
    ]
    sc = scenarios[actual_seed % len(scenarios)]
    question_text = (
        f"In school science laboratories, working with concentrated acids such as **{sc[0]}** requires strict safety adherence.\n\n"
        "1. State the **golden rule of laboratory acid dilution**: Should water be added to concentrated acid, or should acid be added to water?\n"
        "2. Explain the **thermodynamic hazard** that occurs if water is poured directly into concentrated acid.\n"
        "3. List **three essential Personal Protective Equipment (PPE)** items that learners must wear when handling acids in the laboratory.\n"
        "4. If a small droplet of dilute acid accidentally splashes onto a learner's forearm, state the **immediate first aid protocol** to follow."
    )
    sample = (
        "1. **Golden Rule of Dilution:** **Always add acid slowly to water** (never add water to acid);\n"
        "2. **Thermodynamic Hazard:** The dissolution of concentrated acid in water is extremely **exothermic** (releases large amounts of thermal energy). "
        "If water is added to acid, the high acid-to-water ratio causes the water to boil instantly, causing violent spitting and splashing of boiling concentrated acid onto hands and face;\n"
        "3. **Essential PPE:**\n"
        "   • Chemical splash safety goggles;\n"
        "   • Laboratory coat / chemical-resistant apron;\n"
        "   • Nitrile or chemical-resistant protective gloves;\n"
        "4. **First Aid Action:** Immediately flush the affected skin area under cold running tap water for at least 15 to 20 minutes to dilute and wash away the acid; notify the educator immediately."
    )
    marking = (
        "• 1 mark: Always add acid to water [1]\n"
        "• 2 marks: Exothermic reaction explanation [1], water boiling instantly causing violent splashing [1]\n"
        "• 1 mark: Three valid PPE items (goggles, lab coat, gloves) [1]\n"
        "• 1 mark: Immediate copious cold water flushing for 15-20 min [1]\n"
        "**Total: 5 marks**"
    )
    return _normalize_res({
        "title": "Laboratory Safety & Acid Dilution Protocol",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 2,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Remember the rule: 'Do as you oughta, add acid to water.'",
            "Adding water to acid causes boiling and splashing because the reaction is highly exothermic.",
            "Always wear goggles, coat, and gloves, and flush skin with plenty of water if exposed.",
        ],
        "misconception_tags": ["water_to_acid_is_safe_myth", "neutralize_acid_burns_with_strong_base_myth"],
        "learning_objective_id": "NS9.MM.10.05",
    })
