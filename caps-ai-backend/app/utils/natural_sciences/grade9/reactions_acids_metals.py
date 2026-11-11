"""Natural Sciences Grade 9 Term 2: Reactions of Acids with Metals Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Reactions of acids with a metal.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. general_acid_metal_reaction_rule: General word and chemical rule (Acid + Metal -> Salt + Hydrogen gas).
2. hydrochloric_acid_with_metals: Reactions of dilute HCl with Mg, Zn, and Fe forming chloride salts.
3. sulfuric_acid_with_metals: Reactions of dilute H2SO4 with Mg, Zn, and Fe forming sulfate salts.
4. hydrogen_gas_test_and_safety: Confirmatory burning splint 'squeaky pop' test, gas collection, and thermal safety.
5. metal_reactivity_series_and_unreactivity: Reactivity order (Mg > Zn > Fe > Cu), copper unreactivity in dilute acid.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Reactions of acids with metals"
ORDERED_SUBSKILLS = [
    "general_acid_metal_reaction_rule",
    "hydrochloric_acid_with_metals",
    "sulfuric_acid_with_metals",
    "hydrogen_gas_test_and_safety",
    "metal_reactivity_series_and_unreactivity",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_roam"
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

    # Subskill 1: General Acid-Metal Reaction Rule
    if chosen_subskill == "general_acid_metal_reaction_rule":
        metals = [
            ("Magnesium", "Hydrochloric acid", "Magnesium chloride", "Hydrogen"),
            ("Zinc", "Sulfuric acid", "Zinc sulfate", "Hydrogen"),
            ("Iron", "Hydrochloric acid", "Iron(II) chloride", "Hydrogen"),
        ]
        m, a, s, g = metals[actual_seed % len(metals)]
        question_text = (
            "When reactive metals are added to dilute acids, a single displacement chemical reaction takes place.\n\n"
            "1. State the **general word equation** representing the reaction between an acid and a reactive metal.\n"
            f"2. Write the **specific word equation** for the reaction between **{m}** and **{a}**.\n"
            "3. State **two observable macroscopic signs** indicating that an acid-metal reaction is actively occurring in a test tube.\n"
            "4. Contrast the gas produced in an acid-metal reaction with the gas produced in an acid-carbonate reaction."
        )
        sample = (
            "1. **General Word Equation:** Acid + Metal → Salt + Hydrogen Gas;\n"
            f"2. **Specific Word Equation:** {a} + {m} → {s} + {g} gas;\n"
            "3. **Observable Signs:**\n"
            "   • Vigorous effervescence / rapid stream of gas bubbles escaping from the metal surface;\n"
            "   • The metal strip gradually diminishes in size (dissolves);\n"
            "   • Exothermic temperature rise (the test tube feels warm or hot to the touch);\n"
            "4. **Gas Comparison:** An acid-metal reaction produces **Hydrogen gas (H₂)**, which is flammable; whereas an acid-carbonate reaction produces **Carbon dioxide gas (CO₂)**, which extinguishes flames."
        )
        marking = (
            "• 1 mark: General equation (Acid + Metal → Salt + Hydrogen) [1]\n"
            f"• 1 mark: Specific word equation ({a} + {m} → {s} + {g}) [1]\n"
            "• 1 mark: Two valid macroscopic observations (bubbles/effervescence, metal dissolving, heat) [1]\n"
            "• 1 mark: Clear contrast between Hydrogen (H₂) vs Carbon dioxide (CO₂) [1]\n"
            "**Total: 4 marks**"
        )
        return _normalize_res({
            "title": "Acid-Metal Reactions: General Rule & Principles",
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
                "Acid + Metal always gives a Salt and Hydrogen gas (H₂).",
                "Effervescence and heat are clear signs of this reaction.",
                "Acid + metal makes hydrogen (pop test), whereas acid + carbonate makes carbon dioxide (limewater test).",
            ],
            "misconception_tags": ["acid_metal_makes_oxygen_myth", "acid_metal_makes_water_myth"],
            "learning_objective_id": "NS9.MM.12.01",
        })

    # Subskill 2: Hydrochloric Acid with Metals
    if chosen_subskill == "hydrochloric_acid_with_metals":
        hcl_rx = [
            ("Magnesium ribbon", "Mg", "MgCl2", "Mg + 2HCl → MgCl₂ + H₂", "Magnesium chloride"),
            ("Zinc granules", "Zn", "ZnCl2", "Zn + 2HCl → ZnCl₂ + H₂", "Zinc chloride"),
            ("Iron filings / nail", "Fe", "FeCl2", "Fe + 2HCl → FeCl₂ + H₂", "Iron(II) chloride"),
        ]
        m_name, m_sym, s_f, balanced, salt_name = hcl_rx[actual_seed % len(hcl_rx)]
        question_text = (
            f"A learner adds a clean piece of **{m_name}** into a test tube containing dilute hydrochloric acid (HCl).\n\n"
            f"1. Name the chemical salt formed in this reaction: **{salt_name}**.\n"
            f"2. Write the **balanced chemical equation** for the reaction between {m_name.split(' ')[0]} and hydrochloric acid.\n"
            "3. State how many moles/molecules of HCl are required to react completely with one atom of the metal.\n"
            "4. Describe what happens to the atoms of the metal as they transform into salt in aqueous solution."
        )
        sample = (
            f"1. **Salt Formed:** **{salt_name}** ({s_f});\n"
            f"2. **Balanced Chemical Equation:** **{balanced}**;\n"
            "3. **Stoichiometric Ratio:** **2 molecules of HCl** react with each metal atom;\n"
            "4. **Atomic Transformation:** The neutral solid metal atoms lose electrons to form dissolved metal cations that enter the aqueous solution alongside chloride ions to form the dissolved salt."
        )
        marking = (
            f"• 1 mark: Salt name ({salt_name}) [1]\n"
            f"• 2 marks: Correct balanced equation ({balanced}) [2]\n"
            "• 1 mark: Correct ratio (2 HCl per metal atom) [1]\n"
            "• 1 mark: Solid metal atoms dissolve as cations into salt solution [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Hydrochloric Acid with Reactive Metals",
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
                "Hydrochloric acid reacts with metals to form chloride salts and hydrogen gas.",
                "Magnesium, zinc, and iron each displace hydrogen from 2 HCl molecules.",
                "Metal + 2HCl → MetalCl₂ + H₂.",
            ],
            "misconception_tags": ["chlorine_gas_is_produced_myth", "equation_balances_with_1_hcl_myth"],
            "learning_objective_id": "NS9.MM.12.02",
        })

    # Subskill 3: Sulfuric Acid with Metals
    if chosen_subskill == "sulfuric_acid_with_metals":
        h2so4_rx = [
            ("Magnesium ribbon", "Mg", "MgSO4", "Mg + H₂SO₄ → MgSO₄ + H₂", "Magnesium sulfate"),
            ("Zinc granules", "Zn", "ZnSO4", "Zn + H₂SO₄ → ZnSO₄ + H₂", "Zinc sulfate"),
            ("Iron filings", "Fe", "FeSO4", "Fe + H₂SO₄ → FeSO₄ + H₂", "Iron(II) sulfate"),
        ]
        m_name, m_sym, s_f, balanced, salt_name = h2so4_rx[actual_seed % len(h2so4_rx)]
        question_text = (
            f"A laboratory investigation reacts **{m_name}** with dilute sulfuric acid (H2SO4).\n\n"
            f"1. Name the chemical salt produced: **{salt_name}**.\n"
            f"2. Write the **balanced chemical equation** for the reaction between {m_name.split(' ')[0]} and sulfuric acid.\n"
            "3. State the formula of the sulfate polyatomic group present in the acid and the salt.\n"
            "4. Why does this reaction not require a coefficient of 2 in front of H2SO4, unlike the reaction with HCl?"
        )
        sample = (
            f"1. **Salt Name:** **{salt_name}** ({s_f});\n"
            f"2. **Balanced Chemical Equation:** **{balanced}**;\n"
            "3. **Sulfate Radical Formula:** **SO₄²⁻** (sulfate ion);\n"
            "4. **Reason for 1:1 Ratio:** Sulfuric acid (H₂SO₄) is a diprotic acid already containing two hydrogen atoms per molecule, which directly provides the two hydrogen atoms needed to form one diatomic hydrogen molecule (H₂)."
        )
        marking = (
            f"• 1 mark: Salt name ({salt_name}) [1]\n"
            f"• 2 marks: Correct balanced equation ({balanced}) [2]\n"
            "• 1 mark: Sulfate ion formula (SO₄²⁻ / SO₄) [1]\n"
            "• 1 mark: H₂SO₄ already carries two hydrogen atoms for H₂ release [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Sulfuric Acid with Reactive Metals: Sulfate Salts",
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
                "Sulfuric acid produces sulfate salts (ending in -sulfate).",
                "H₂SO₄ already contains two hydrogen atoms, so metal + H₂SO₄ → metalSO₄ + H₂ balances with 1:1 ratio.",
                "Magnesium, zinc, and iron each form divalent cations (2+ charge).",
            ],
            "misconception_tags": ["sulfuric_acid_makes_sulfide_myth", "hydrogen_is_monatomic_h_myth"],
            "learning_objective_id": "NS9.MM.12.03",
        })

    # Subskill 4: Hydrogen Gas Test and Safety
    if chosen_subskill == "hydrogen_gas_test_and_safety":
        question_text = (
            "During an experiment reacting zinc with hydrochloric acid, a colourless, odourless gas fills an inverted test tube.\n\n"
            "1. Name the standard laboratory test used to confirm the presence of **hydrogen gas**.\n"
            "2. Describe the **exact step-by-step procedure and positive observation** for this test.\n"
            "3. Write the balanced chemical equation for the combustion reaction that causes the characteristic sound heard during the test.\n"
            "4. State **two laboratory safety precautions** necessary when collecting and testing hydrogen gas in a classroom."
        )
        sample = (
            "1. **Confirmatory Test:** The **Burning Wooden Splint ('Squeaky Pop') Test**;\n"
            "2. **Procedure & Observation:**\n"
            "   • Collect the gas in an inverted test tube (hydrogen is less dense than air);\n"
            "   • Bring a lit / flaming wooden splint close to the mouth of the test tube;\n"
            "   • A positive result is confirmed by a sharp, characteristic **'squeaky pop' sound** as the hydrogen combusts rapidly with atmospheric oxygen;\n"
            "3. **Combustion Equation:** **2H₂ + O₂ → 2H₂O**;\n"
            "4. **Safety Precautions:**\n"
            "   • Wear safety goggles to protect eyes from potential test tube shattering or acid splashes;\n"
            "   • Keep the gas generation apparatus away from open flames until ready to test, as hydrogen-air mixtures are explosive in larger quantities."
        )
        marking = (
            "• 1 mark: Burning splint test identified [1]\n"
            "• 2 marks: Procedure (bring burning splint to mouth [1], characteristic squeaky pop sound [1])\n"
            "• 1 mark: Balanced equation for combustion: 2H₂ + O₂ → 2H₂O [1]\n"
            "• 1 mark: Two safety rules (eye protection, flame management) [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Hydrogen Confirmatory Test & Combustion Safety",
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
                "Hydrogen gas is identified with a burning wooden splint that produces a squeaky pop sound.",
                "The pop sound is caused by miniature explosive combustion: 2H₂ + O₂ → 2H₂O.",
                "Hydrogen is lighter than air, so test tubes are held inverted.",
            ],
            "misconception_tags": ["glowing_splint_relights_for_hydrogen_myth", "hydrogen_smells_like_rotten_eggs_myth"],
            "learning_objective_id": "NS9.MM.12.04",
        })

    # Subskill 5: Metal Reactivity Series and Unreactivity
    metals_order = [
        ("Magnesium (Mg)", "Extremely vigorous effervescence; rapid temperature spike; ribbon dissolves in under 30 seconds"),
        ("Zinc (Zn)", "Moderate continuous stream of bubbles; steady temperature increase; granules dissolve over several minutes"),
        ("Iron (Fe)", "Slow, sluggish bubbling; slight temperature rise; filings dissolve slowly over a long period"),
        ("Copper (Cu)", "Zero effervescence; no bubbles; no temperature change; metal strip remains completely unreacted"),
    ]
    question_text = (
        "A learner places equal masses of four different metal strips into four separate test tubes, each containing 10 mL of 1 M hydrochloric acid at 20 °C:\n\n"
        "• Test tube 1: Magnesium (Mg)\n"
        "• Test tube 2: Zinc (Zn)\n"
        "• Test tube 3: Iron (Fe)\n"
        "• Test tube 4: Copper (Cu)\n\n"
        "1. Rank these four metals in order of **decreasing reactivity with dilute acid (from most reactive to least reactive)**.\n"
        f"2. Describe the specific observation in **Test tube 1 (Magnesium)**: *{metals_order[0][1]}*.\n"
        "3. Explain why **no reaction** occurs in **Test tube 4 (Copper)**.\n"
        "4. Why is copper frequently chosen for domestic water plumbing pipes rather than iron or zinc?"
    )
    sample = (
        "1. **Reactivity Order (Decreasing):**\n"
        "   **Magnesium (Mg) > Zinc (Zn) > Iron (Fe) > Copper (Cu)**;\n"
        f"2. **Observation for Magnesium:** {metals_order[0][1]};\n"
        "3. **Explanation for Copper Unreactivity:** Copper is located **below hydrogen** in the reactivity series. "
        "It has a lower chemical tendency to lose electrons than hydrogen, and therefore cannot displace hydrogen ions from dilute acid solutions;\n"
        "4. **Domestic Plumbing Selection:** Copper does not react with water or dilute acidic solutions, and forms a protective patina rather than rusting like iron, ensuring water pipes do not corrode or contaminate drinking water."
    )
    marking = (
        "• 1 mark: Correct reactivity order (Mg > Zn > Fe > Cu) [1]\n"
        "• 1 mark: Vigorous bubbling and heat observation for Magnesium [1]\n"
        "• 2 marks: Copper is below hydrogen in reactivity series [1], cannot displace hydrogen from dilute acid [1]\n"
        "• 1 mark: Copper does not corrode/react with water, making it safe and durable for plumbing [1]\n"
        "**Total: 5 marks**"
    )
    return _normalize_res({
        "title": "Reactivity Series of Metals & Acid Displacement",
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
            "Reactivity order: Magnesium is most reactive, followed by zinc, then iron, then copper.",
            "Copper is below hydrogen in the reactivity series and does not displace hydrogen from dilute acid.",
            "Copper's unreactivity is why it is used for durable water pipes.",
        ],
        "misconception_tags": ["all_metals_react_with_acid_myth", "copper_dissolves_in_dilute_hcl_myth"],
        "learning_objective_id": "NS9.MM.12.05",
    })
