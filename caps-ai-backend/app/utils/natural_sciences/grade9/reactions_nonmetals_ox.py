"""Natural Sciences Grade 9 Term 2: Reactions of Non-Metals with Oxygen Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Reactions of non metals with oxygen.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. general_nonmetal_oxidation_rule: General word and balanced chemical equations (non-metal + oxygen -> non-metal oxide).
2. carbon_combustion_and_limewater_test: Carbon burning to form CO2 and the calcium hydroxide limewater precipitation test.
3. sulfur_combustion_and_safety: Sulfur burning with blue flame to form SO2 gas and asthma safety hazards.
4. nonmetal_oxides_acidity: Acidic nature of dissolved non-metal oxides (H2CO3, H2SO3) turning blue litmus red.
5. acid_rain_environmental_impact: Tracing fossil fuel SO2/CO2 combustion to sulfuric acid rain and environmental damage.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Reactions of non metals with oxygen"
ORDERED_SUBSKILLS = [
    "general_nonmetal_oxidation_rule",
    "carbon_combustion_and_limewater_test",
    "sulfur_combustion_and_safety",
    "nonmetal_oxides_acidity",
    "acid_rain_environmental_impact",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_rnmo"
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

    # Subskill 1: General Non-Metal Oxidation Rule
    if chosen_subskill == "general_nonmetal_oxidation_rule":
        nonmetals = [
            ("Carbon", "Carbon dioxide", "C", "CO₂", "C + O₂ → CO₂", "Carbonic acid (H₂CO₃)"),
            ("Sulfur", "Sulfur dioxide", "S", "SO₂", "S + O₂ → SO₂", "Sulfurous acid (H₂SO₃)"),
            ("Phosphorus", "Phosphorus pentoxide", "P₄", "P₄O₁₀", "P₄ + 5O₂ → P₄O₁₀", "Phosphoric acid (H₃PO₄)"),
            ("Hydrogen", "Water (Dihydrogen monoxide)", "H₂", "H₂O", "2H₂ + O₂ → 2H₂O", "Neutral water (pH 7)"),
        ]
        nm = nonmetals[actual_seed % len(nonmetals)]
        question_text = (
            "When non-metals burn in air or oxygen, they react to form non-metal oxides.\n\n"
            "1. State the **general word equation** for the combustion of a non-metal with oxygen.\n"
            f"2. Write the **word equation** for the combustion of **{nm[0]}** in oxygen.\n"
            f"3. Write the **balanced chemical equation** for this reaction.\n"
            "4. Contrast the general pH nature of non-metal oxides with metal oxides when dissolved in water."
        )
        sample = (
            "1. **General Equation:** Non-metal + Oxygen → Non-metal Oxide;\n"
            f"2. **Word Equation:** {nm[0]} + Oxygen → {nm[1]};\n"
            f"3. **Balanced Chemical Equation:**\n"
            f"   $$\\text{{{nm[4]}}}$$\n"
            "4. **pH Contrast:** Non-metal oxides are generally acidic (lowering pH below 7 and turning blue litmus paper red when dissolved in water), whereas metal oxides are basic/alkaline (raising pH above 7 and turning red litmus paper blue)."
        )
        marking = (
            "• 1 mark: Non-metal + Oxygen → Non-metal Oxide [1]\n"
            f"• 1 mark: {nm[0]} + Oxygen → {nm[1]} [1]\n"
            f"• 2 marks: Balanced chemical equation ({nm[4]}) [2]\n"
            "• 1 mark: Non-metal oxides are acidic (turn blue litmus red); metal oxides are basic [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": f"General Non-Metal Oxidation: {nm[0]}",
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
                "Non-metal + Oxygen → Non-metal Oxide.",
                "Non-metal oxides dissolve in water to produce acidic solutions (pH < 7).",
                f"Rule: Non-metal + Oxygen → Non-metal Oxide. Equation: {nm[4]}. Non-metal oxides are acidic.",
            ],
            "misconception_tags": ["nonmetal_oxide_is_basic_myth", "combustion_product_formula_error"],
            "learning_objective_id": "NS9.MM.09.01",
        }

    # Subskill 2: Carbon Combustion & Limewater Test
    if chosen_subskill == "carbon_combustion_and_limewater_test":
        question_text = (
            "A piece of charcoal (carbon) is heated in a deflagrating spoon until it glows red, then lowered into a gas jar of oxygen.\n\n"
            "1. State the observable macroscopic appearance of carbon burning in pure oxygen.\n"
            "2. Write the **balanced chemical equation** for the combustion of carbon.\n"
            "3. Clear limewater (calcium hydroxide solution, Ca(OH)₂) is poured into the gas jar and swirled.\n"
            "   (a) State the diagnostic visual observation.\n"
            "   (b) Name the insoluble chemical precipitate responsible for this observation."
        )
        sample = (
            "1. **Observation:** Carbon burns vigorously with an orange/yellow glow, producing a colorless, odorless gas (carbon dioxide);\n"
            "2. **Balanced Chemical Equation:**\n"
            "   $$\\text{C + O₂ → CO₂}$$\n"
            "3. **Limewater Test:**\n"
            "   (a) The clear, colorless limewater turns **milky / cloudy white**;\n"
            "   (b) The precipitate formed is insoluble **Calcium carbonate (CaCO₃)**:\n"
            "       $$\\text{CO₂ + Ca(OH)₂ → CaCO₃ (solid precipitate) + H₂O}$$"
        )
        marking = (
            "• 1 mark: Carbon glows red/orange, produces colorless gas [1]\n"
            "• 1 mark: C + O₂ → CO₂ [1]\n"
            "• 1 mark: Clear limewater turns milky / cloudy white [1]\n"
            "• 1 mark: Calcium carbonate (CaCO₃) precipitate [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": "Combustion of Carbon & Limewater Test",
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
                "Carbon burns in oxygen to make carbon dioxide gas.",
                "Carbon dioxide turns clear limewater milky by forming calcium carbonate precipitate.",
                "Equation: C + O₂ → CO₂. Limewater turns milky/cloudy due to insoluble calcium carbonate (CaCO₃).",
            ],
            "misconception_tags": ["limewater_confused_with_lemon_juice_myth", "carbon_monoxide_limewater_myth"],
            "learning_objective_id": "NS9.MM.09.02",
        }

    # Subskill 3: Sulfur Combustion & Safety Hazards
    if chosen_subskill == "sulfur_combustion_and_safety":
        question_text = (
            "A small sample of yellow powdered sulfur is heated in a deflagrating spoon in a fume cupboard.\n\n"
            "1. State the **color of the flame** observed when sulfur burns in air or oxygen.\n"
            "2. Name the toxic gaseous product formed, and state its **chemical formula**.\n"
            "3. Write the **balanced chemical equation** for the combustion of sulfur.\n"
            "4. Explain why this experiment must be performed strictly inside a fume cupboard or well-ventilated laboratory, "
            "highlighting the danger to individuals with asthma."
        )
        sample = (
            "1. **Flame Color:** Sulfur burns with a characteristic vivid, bright **blue flame**;\n"
            "2. **Product:** Chemical Name: **Sulfur dioxide**; Chemical Formula: **SO₂**;\n"
            "3. **Balanced Chemical Equation:**\n"
            "   $$\\text{S + O₂ → SO₂}$$\n"
            "4. **Safety Rationale:** Sulfur dioxide is a poisonous, suffocating gas with a sharp, choking, pungent odor. When inhaled, it reacts with moisture in the respiratory tract to form sulfurous acid, triggering severe airway constriction, coughing spasms, and acute bronchial attacks in asthmatics."
        )
        marking = (
            "• 1 mark: Bright blue flame [1]\n"
            "• 1 mark: Sulfur dioxide / SO₂ [1]\n"
            "• 1 mark: S + O₂ → SO₂ [1]\n"
            "• 2 marks: Fume cupboard safety rationale: toxic suffocating gas [1] that triggers acute bronchospasm/asthma attacks [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Combustion of Sulfur & Laboratory Safety",
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
                "Sulfur burns with a vivid blue flame.",
                "The product is sulfur dioxide (SO₂), a choking gas harmful to breathing.",
                "Flame: vivid blue. Product: Sulfur dioxide (SO₂). Equation: S + O₂ → SO₂. Danger: poisonous gas, asthma hazard.",
            ],
            "misconception_tags": ["sulfur_dioxide_odorless_myth", "fume_hood_safety_omission"],
            "learning_objective_id": "NS9.MM.09.03",
        }

    # Subskill 4: Non-Metal Oxides Acidity
    if chosen_subskill == "nonmetal_oxides_acidity":
        question_text = (
            "After burning sulfur in a gas jar of oxygen, a small amount of distilled water is added and shaken. "
            "The resulting liquid is tested with both blue and red litmus paper.\n\n"
            "1. State the resulting color of:\n"
            "   (a) Blue litmus paper\n"
            "   (b) Red litmus paper\n"
            "2. Name the acid formed when sulfur dioxide (SO₂) dissolves in water, and write its chemical formula.\n"
            "3. Estimate the approximate pH of this solution (pH < 7, pH = 7, or pH > 7).\n"
            "4. Contrast this result with the solution formed when calcium oxide (CaO, a metal oxide) dissolves in water."
        )
        sample = (
            "1. **Litmus Observations:**\n"
            "   (a) Blue litmus paper turns **red**;\n"
            "   (b) Red litmus paper **remains red**;\n"
            "2. **Acid Formed:** **Sulfurous acid**; Formula: **H₂SO₃** (SO₂ + H₂O → H₂SO₃);\n"
            "3. **Estimated pH:** **pH < 7** (typically pH ~ 2–3, indicating an acidic solution);\n"
            "4. Calcium oxide (CaO) is a basic metal oxide that reacts with water to form calcium hydroxide (limewater), an alkaline solution with pH > 7 that turns red litmus blue."
        )
        marking = (
            "• 2 marks: Blue litmus turns red [1]; Red litmus remains red [1]\n"
            "• 1 mark: Sulfurous acid / H₂SO₃ [1]\n"
            "• 1 mark: pH < 7 [1]\n"
            "• 1 mark: CaO forms basic calcium hydroxide with pH > 7 (turns red litmus blue) [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Acidic Nature of Non-Metal Oxides",
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
                "Acids turn blue litmus paper red.",
                "Non-metal oxides dissolve in water to make acids (pH less than 7).",
                "Blue litmus turns red; red litmus stays red. Forms sulfurous acid (H₂SO₃), pH < 7. Metal oxides are basic (pH > 7).",
            ],
            "misconception_tags": ["litmus_color_inversion", "nonmetal_oxide_neutral_myth"],
            "learning_objective_id": "NS9.MM.09.04",
        }

    # Subskill 5: Acid Rain Environmental Impact
    sources = [
        ("Coal-fired power stations", "Sulfur dioxide (SO₂)", "Sulfuric acid (H₂SO₄)"),
        ("Internal combustion motor vehicle exhausts", "Nitrogen dioxide (NO₂)", "Nitric acid (HNO₃)"),
    ]
    src = sources[actual_seed % len(sources)]
    question_text = (
        "Industrial emissions of non-metal oxides have major environmental consequences.\n\n"
        f"1. Explain how emissions of **{src[1]}** from **{src[0]}** lead to the formation of **acid rain**.\n"
        "2. State **three severe environmental or structural consequences** of acid rain.\n"
        "3. Name the chemical compound commonly spread onto agricultural soil or lakes to neutralize acid rain damage, and explain why it works."
    )
    sample = (
        f"1. **Formation Mechanism:** When fossil fuels are burned in {src[0]}, {src[1]} gas is released into the atmosphere. "
        f"It rises and dissolves in atmospheric water droplets and clouds, oxidizing to form dilute acid precipitation (such as {src[2]});\n"
        "2. **Environmental Consequences:**\n"
        "   • Leaches vital plant nutrients (calcium, magnesium) from soil and releases toxic aluminium ions, damaging forest trees and crops;\n"
        "   • Acidifies freshwater lakes and rivers, lowering pH and killing aquatic fish and amphibians;\n"
        "   • Accelerates the chemical corrosion of metal infrastructure (bridges) and dissolves calcium carbonate in limestone and marble buildings/monuments;\n"
        "3. **Remediation:** **Agricultural Lime (Calcium carbonate, CaCO₃)** is spread on soils and lakes. It is a basic metal carbonate that neutralizes acidity: Acid + Base → Salt + Water + CO₂."
    )
    marking = (
        "• 1 mark: Non-metal oxide emissions dissolve in atmospheric moisture forming acid precipitation [1]\n"
        "• 3 marks: Three valid impacts (forest/soil damage [1], lake acidification/aquatic death [1], corrosion of buildings/limestone [1])\n"
        "• 1 mark: Calcium carbonate (lime) neutralizes acidic soil/water [1]\n"
        "**Total: 5 marks**"
    )
    return {
        "title": "Acid Rain: Chemistry & Environmental Impact",
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
            "Non-metal oxides dissolve in clouds to form dilute acid rain.",
            "Acid rain damages trees, kills fish in lakes, and erodes limestone buildings.",
            f"Emissions dissolve in rain forming {src[2]}. Causes forest damage, lake acidification, building erosion. Lime (CaCO₃) neutralizes.",
        ],
        "misconception_tags": ["acid_rain_eats_skin_immediately_myth", "lime_is_an_acid_myth"],
        "learning_objective_id": "NS9.MM.09.05",
    }
