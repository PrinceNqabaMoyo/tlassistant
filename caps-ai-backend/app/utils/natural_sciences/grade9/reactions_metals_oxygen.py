"""Natural Sciences Grade 9 Term 2: Reactions of Metals with Oxygen Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/02. Reactions of metals with oxygen.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. general_metal_oxidation_rule: General word and symbolic equations (metal + oxygen -> metal oxide).
2. magnesium_combustion: Observations (blinding white flame, white ash MgO) and balanced equation (2Mg + O2 -> 2MgO).
3. iron_combustion_and_rusting: Rapid burning of steel wool vs slow corrosion/rusting (4Fe + 3O2 -> 2Fe2O3).
4. copper_oxidation: Surface reaction of copper forming black copper(II) oxide (2Cu + O2 -> 2CuO).
5. rust_prevention_strategies: Barrier methods (painting/greasing) and sacrificial protection (galvanising with zinc).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Reactions of metals with oxygen"
ORDERED_SUBSKILLS = [
    "general_metal_oxidation_rule",
    "magnesium_combustion",
    "iron_combustion_and_rusting",
    "copper_oxidation",
    "rust_prevention_strategies",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_rmo"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


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

    # Subskill 1: General Metal Oxidation Rule
    if chosen_subskill == "general_metal_oxidation_rule":
        metal_examples = [
            ("Zinc", "Zinc oxide", "Zn", "ZnO", "2Zn + O₂ → 2ZnO"),
            ("Calcium", "Calcium oxide", "Ca", "CaO", "2Ca + O₂ → 2CaO"),
            ("Lithium", "Lithium oxide", "Li", "Li₂O", "4Li + O₂ → 2Li₂O"),
            ("Potassium", "Potassium oxide", "K", "K₂O", "4K + O₂ → 2K₂O"),
        ]
        ex = metal_examples[actual_seed % len(metal_examples)]
        question_text = (
            "When metals react with oxygen during heating or combustion, they undergo oxidation.\n\n"
            "1. State the **general word equation** for the reaction between a metal and oxygen.\n"
            f"2. Write the **word equation** for the reaction when **{ex[0]}** reacts with oxygen.\n"
            f"3. Write the **balanced chemical equation** for the oxidation of {ex[0]}.\n"
            "4. Predict whether the resulting metal oxide will form an acidic or basic solution when dissolved in water."
        )
        sample = (
            "1. **General Equation:** Metal + Oxygen → Metal Oxide;\n"
            f"2. **Word Equation:** {ex[0]} + Oxygen → {ex[1]};\n"
            f"3. **Balanced Chemical Equation:**\n"
            f"   $$\\text{{{ex[4]}}}$$\n"
            "4. **Acid/Base Nature:** Metal oxides are basic. When dissolved in water, they form alkaline solutions containing hydroxide ions (OH⁻) that turn red litmus paper blue."
        )
        marking = (
            "• 1 mark: Metal + Oxygen → Metal Oxide [1]\n"
            f"• 1 mark: {ex[0]} + Oxygen → {ex[1]} [1]\n"
            f"• 2 marks: Balanced chemical equation ({ex[4]}) [2]\n"
            "• 1 mark: Basic metal oxide (turns red litmus blue) [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": f"General Metal Oxidation: {ex[0]}",
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
                "The general rule is: Metal + Oxygen → Metal Oxide.",
                "Metal oxides are bases (alkaline), turning red litmus paper blue.",
                f"Rule: Metal + Oxygen → Metal Oxide. For {ex[0]}: {ex[4]}. Metal oxides are basic.",
            ],
            "misconception_tags": ["metal_oxide_is_acidic_myth", "oxidation_general_equation_error"],
            "learning_objective_id": "NS9.MM.08.01",
        }

    # Subskill 2: Magnesium Combustion
    if chosen_subskill == "magnesium_combustion":
        question_text = (
            "A teacher demonstrates the combustion of a strip of magnesium ribbon using tongs and a Bunsen burner flame.\n\n"
            "1. State **two observable macroscopic changes** that occur when magnesium burns in air.\n"
            "2. State **one crucial safety precaution** the learners must follow during this demonstration.\n"
            "3. Write the **balanced chemical equation** for this reaction.\n"
            "4. The white powdery product is collected, dissolved in water, and tested with Universal Indicator. "
            "Predict the color of the indicator and explain your answer."
        )
        sample = (
            "1. **Observations:** Magnesium burns with an intensely brilliant, blinding white flame and leaves behind a white powdery ash (magnesium oxide);\n"
            "2. **Safety Precaution:** Learners must **never look directly at the bright flame**, as intense ultraviolet light can cause temporary blindness or retinal eye damage (use dark safety goggles or look away);\n"
            "3. **Balanced Chemical Equation:**\n"
            "   $$\\text{2Mg + O₂ → 2MgO}$$\n"
            "4. **Indicator Result:** The indicator turns **blue or purple (pH ~ 9–10)** because magnesium oxide reacts with water to form magnesium hydroxide, a basic/alkaline solution."
        )
        marking = (
            "• 2 marks: Two observations (blinding white flame [1], white powder/ash formed [1])\n"
            "• 1 mark: Safety: do not look directly at flame / wear dark goggles to prevent eye damage [1]\n"
            "• 1 mark: 2Mg + O₂ → 2MgO [1]\n"
            "• 1 mark: Blue/purple indicator color because MgO is basic [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Combustion of Magnesium Ribbon",
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
                "Magnesium burns with a very bright white light that requires eye protection.",
                "The product is white magnesium oxide powder, which forms a basic solution in water.",
                "Observations: blinding white light, white powder. Equation: 2Mg + O₂ → 2MgO. Blue/purple in indicator (basic).",
            ],
            "misconception_tags": ["magnesium_combustion_safety_omission", "metal_oxide_neutral_myth"],
            "learning_objective_id": "NS9.MM.08.02",
        }

    # Subskill 3: Iron Combustion and Rusting
    if chosen_subskill == "iron_combustion_and_rusting":
        question_text = (
            "Iron can react with oxygen rapidly during heating, or slowly at room temperature.\n\n"
            "1. Contrast the **rapid combustion of steel wool** in a flame with the **slow rusting of an iron nail** in terms of reaction speed and conditions.\n"
            "2. Name the **two environmental substances** that MUST both be present for iron to rust.\n"
            "3. Write the **balanced chemical equation** for the formation of iron(III) oxide (rust).\n"
            "4. In an investigation, an iron nail was placed in boiled distilled water sealed with an oil layer on top. "
            "Explain whether the nail will rust after two weeks."
        )
        sample = (
            "1. **Rapid vs Slow:** Combustion of steel wool is an extremely fast, high-temperature reaction producing heat, bright orange sparks, and iron oxide in seconds; rusting is a slow, gradual surface corrosion occurring at ambient room temperature over days or weeks;\n"
            "2. **Necessary Substances:** Both **Oxygen (from air)** AND **Water (moisture)** must be present simultaneously;\n"
            "3. **Balanced Chemical Equation:**\n"
            "   $$\\text{4Fe + 3O₂ → 2Fe₂O₃}$$\n"
            "4. **Investigation Prediction:** The nail **will NOT rust**. Boiling the water expels all dissolved oxygen, and the oil layer forms an impermeable barrier preventing atmospheric oxygen from dissolving back in."
        )
        marking = (
            "• 1 mark: Contrast rapid combustion (heat/sparks) with slow rusting (gradual corrosion) [1]\n"
            "• 2 marks: Oxygen [1] AND Water/moisture [1]\n"
            "• 1 mark: 4Fe + 3O₂ → 2Fe₂O₃ [1]\n"
            "• 1 mark: Will not rust because boiled water + oil excludes oxygen [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Iron Oxidation & Rusting Conditions",
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
                "Does iron rust in dry air alone? Does it rust in water without oxygen? Both are needed!",
                "Boiling water drives out dissolved air. Oil blocks oxygen from entering.",
                "Speed: combustion is fast; rusting is slow. Needs BOTH oxygen and water. Equation: 4Fe + 3O₂ → 2Fe₂O₃. No rust with oil seal.",
            ],
            "misconception_tags": ["water_alone_causes_rust_myth", "rusting_is_physical_change_myth"],
            "learning_objective_id": "NS9.MM.08.03",
        }

    # Subskill 4: Copper Oxidation
    if chosen_subskill == "copper_oxidation":
        question_text = (
            "A piece of shiny reddish-brown copper metal is held in a Bunsen burner flame for several minutes.\n\n"
            "1. Describe the observable color change that occurs on the surface of the copper metal.\n"
            "2. State the **chemical name** and **chemical formula** of the black compound formed.\n"
            "3. Write the **balanced chemical equation** for the oxidation of copper.\n"
            "4. Explain why copper does not burn with a vigorous flame like magnesium."
        )
        sample = (
            "1. **Observation:** The shiny reddish-brown surface of the copper turns dull and becomes coated with a black layer;\n"
            "2. **Product:** Chemical Name: **Copper(II) oxide**; Chemical Formula: **CuO**;\n"
            "3. **Balanced Chemical Equation:**\n"
            "   $$\\text{2Cu + O₂ → 2CuO}$$\n"
            "4. **Reactivity:** Copper is much lower in the reactivity series than magnesium. It reacts sluggishly with oxygen at high temperatures to form a surface oxide coat, but does not release enough heat to sustain combustion."
        )
        marking = (
            "• 1 mark: Shiny reddish-brown turns black [1]\n"
            "• 1 mark: Copper(II) oxide / CuO [1]\n"
            "• 2 marks: 2Cu + O₂ → 2CuO [2]\n"
            "• 1 mark: Copper is low in the reactivity series / does not burn vigorously [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Oxidation of Copper Metal",
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
                "Copper turns from shiny reddish-brown to black when heated in air.",
                "The black layer is copper(II) oxide, CuO.",
                "Color: turns black. Name: Copper(II) oxide (CuO). Equation: 2Cu + O₂ → 2CuO. Copper is less reactive than magnesium.",
            ],
            "misconception_tags": ["copper_turns_green_in_flame_myth", "copper_oxide_formula_error"],
            "learning_objective_id": "NS9.MM.08.04",
        }

    # Subskill 5: Rust Prevention Strategies
    methods = [
        (
            "Painting and Plastic Coating",
            "Creates an impermeable physical barrier over the iron surface, preventing atmospheric oxygen and water moisture from contacting the iron atoms.",
            "Car bodies, outdoor gates, bridges, garden furniture",
            "barrier_protection_concept",
        ),
        (
            "Galvanizing (Zinc Coating)",
            "Coating iron with a thin layer of zinc metal. Zinc acts as a physical barrier and, if scratched, acts as a sacrificial metal because zinc is more reactive than iron and oxidizes preferentially (sacrificial protection).",
            "Corrugated roofing sheets, chain-link fences, nails, buckets",
            "galvanizing_sacrificial_protection_error",
        ),
        (
            "Oiling and Greasing",
            "A hydrophobic oil/grease layer repels water moisture and excludes air from moving metal surfaces.",
            "Bicycle chains, machine engine gears, mechanical tools",
            "lubrication_rust_prevention_confusion",
        ),
        (
            "Electroplating with Chromium",
            "Electrolytically depositing a hard, unreactive, corrosion-resistant chromium layer on iron to exclude oxygen and water while providing an attractive shiny finish.",
            "Bathroom water taps, motor car bumpers, bicycle handlebars",
            "electroplating_barrier_error",
        ),
    ]
    target_method = methods[actual_seed % len(methods)]
    question_text = (
        "Corrosion and rusting of iron cost economies billions of Rands annually in structural damage.\n\n"
        f"1. Explain how **{target_method[0]}** prevents iron from rusting.\n"
        f"2. Give **two practical real-world examples** where {target_method[0]} is utilized.\n"
        "3. Explain why galvanizing with zinc continues to protect iron even if the protective outer layer is scratched."
    )
    sample = (
        f"1. **Mechanism:** {target_method[1]}\n"
        f"2. **Examples:** {target_method[2]};\n"
        "3. **Sacrificial Protection:** Zinc is more reactive than iron in the reactivity series. If the coating is scratched, zinc corrodes preferentially by losing electrons to oxygen, sacrificing itself while keeping the iron underneath protected from oxidation."
    )
    marking = (
        f"• 2 marks: Clear explanation of rust prevention mechanism ({target_method[1]}) [2]\n"
        f"• 1 mark: Two valid everyday applications ({target_method[2]}) [1]\n"
        "• 1 mark: Zinc is more reactive than iron / oxidizes preferentially (sacrificial protection) [1]\n"
        "**Total: 4 marks**"
    )
    return {
        "title": f"Rust Prevention: {target_method[0]}",
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
            "Rusting needs both oxygen and water. How does this method stop them touching the iron?",
            "Zinc is higher on the reactivity series, so it sacrifices itself before iron can rust.",
            f"Mechanism: {target_method[1]}. Examples: {target_method[2]}. Zinc sacrifices itself because it is more reactive.",
        ],
        "misconception_tags": [target_method[3], "sacrificial_metal_reactivity_inversion"],
        "learning_objective_id": "NS9.MM.08.05",
    }
