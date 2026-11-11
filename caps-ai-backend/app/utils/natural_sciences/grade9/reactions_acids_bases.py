"""Natural Sciences Grade 9 Term 2: Reactions of Acids with Bases Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/04. Reactions of Acids and bases.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. neutralisation_concept_and_word_equations: Neutralisation principle (Acid + Base -> Salt + Water), pH shift to 7.
2. acids_with_metal_hydroxides: Reactions with metal hydroxides (NaOH, KOH, Ca(OH)2), salt naming and crystallisation.
3. acids_with_metal_oxides: Reactions with metal oxides (MgO, CuO), dissolution of black CuO to form blue CuSO4 solution.
4. acids_with_metal_carbonates: Reactions with metal carbonates (CaCO3, Na2CO3) forming Salt + CO2 + H2O, limewater test.
5. practical_applications_and_neutralisation: Antacid medication, agricultural soil liming, and insect sting neutralisation.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Reactions of acids with bases"
ORDERED_SUBSKILLS = [
    "neutralisation_concept_and_word_equations",
    "acids_with_metal_hydroxides",
    "acids_with_metal_oxides",
    "acids_with_metal_carbonates",
    "practical_applications_and_neutralisation",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_roab"
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

    # Subskill 1: Neutralisation Concept and Word Equations
    if chosen_subskill == "neutralisation_concept_and_word_equations":
        pairs = [
            ("Hydrochloric acid", "Sodium hydroxide", "Sodium chloride", "Water"),
            ("Nitric acid", "Potassium hydroxide", "Potassium nitrate", "Water"),
            ("Sulfuric acid", "Sodium hydroxide", "Sodium sulfate", "Water"),
        ]
        acid, base, salt, water = pairs[actual_seed % len(pairs)]
        question_text = (
            "When an acid reacts chemically with a base, a neutralisation reaction occurs.\n\n"
            "1. Define the term **neutralisation** in terms of chemical reactants and pH change.\n"
            "2. State the **general word equation** representing the reaction between an acid and a base.\n"
            f"3. Write the **specific word equation** for the reaction between **{acid}** and **{base}**.\n"
            "4. Predict the colour change observed if universal indicator was initially added to the acidic solution and base was added until the neutral point is reached."
        )
        sample = (
            "1. **Definition:** Neutralisation is a chemical reaction in which an acid reacts with a base to form a salt and water, causing the acidic and basic properties to cancel each other out and the pH to shift towards neutral (pH 7);\n"
            "2. **General Word Equation:** Acid + Base → Salt + Water;\n"
            f"3. **Specific Word Equation:** {acid} + {base} → {salt} + {water};\n"
            "4. **Indicator Colour Change:** The universal indicator changes from **red/orange (acidic)** through yellow to **green (neutral, pH 7)**."
        )
        marking = (
            "• 1 mark: Valid definition of neutralisation and pH shift towards 7 [1]\n"
            "• 1 mark: General equation (Acid + Base → Salt + Water) [1]\n"
            f"• 1 mark: Correct specific word equation ({acid} + {base} → {salt} + water) [1]\n"
            "• 1 mark: Red/orange changing to green [1]\n"
            "**Total: 4 marks**"
        )
        return _normalize_res({
            "title": "Neutralisation Principle & Word Equations",
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
                "Acid + Base always produces a Salt and Water.",
                "Hydrochloric acid makes chloride salts; Sulfuric acid makes sulfate salts; Nitric acid makes nitrate salts.",
                "Universal indicator turns green when exact neutralisation is reached.",
            ],
            "misconception_tags": ["neutralisation_destroys_all_atoms_myth", "salts_are_always_table_salt_myth"],
            "learning_objective_id": "NS9.MM.11.01",
        })

    # Subskill 2: Acids with Metal Hydroxides
    if chosen_subskill == "acids_with_metal_hydroxides":
        rx_list = [
            ("Hydrochloric acid", "Sodium hydroxide", "HCl", "NaOH", "NaCl", "H2O", "HCl + NaOH → NaCl + H₂O", "Sodium chloride"),
            ("Sulfuric acid", "Sodium hydroxide", "H2SO4", "NaOH", "Na2SO4", "H2O", "H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O", "Sodium sulfate"),
            ("Hydrochloric acid", "Potassium hydroxide", "HCl", "KOH", "KCl", "H2O", "HCl + KOH → KCl + H₂O", "Potassium chloride"),
            ("Nitric acid", "Sodium hydroxide", "HNO3", "NaOH", "NaNO3", "H2O", "HNO₃ + NaOH → NaNO₃ + H₂O", "Sodium nitrate"),
        ]
        acid_n, base_n, ac_f, bs_f, s_f, w_f, balanced, salt_name = rx_list[actual_seed % len(rx_list)]
        question_text = (
            f"A learner titrates dilute **{acid_n} ({ac_f})** against dilute **{base_n} ({bs_f})**.\n\n"
            f"1. Name the chemical salt produced in this reaction: **{salt_name}**.\n"
            f"2. Write the **balanced chemical equation** for the complete neutralisation of {acid_n} with {base_n}.\n"
            "3. Outline the laboratory procedure the learner must use to recover pure solid salt crystals from the resulting neutral solution."
        )
        sample = (
            f"1. **Salt Name:** **{salt_name}** ({s_f});\n"
            f"2. **Balanced Chemical Equation:** **{balanced}**;\n"
            "3. **Crystallisation Procedure:**\n"
            "   • Pour the neutralised solution into an evaporating dish;\n"
            "   • Gently heat the dish over a Bunsen burner or water bath to evaporate most of the water until saturation point;\n"
            "   • Allow the concentrated solution to cool slowly at room temperature, permitting pure crystals to form, then pat dry with filter paper."
        )
        marking = (
            f"• 1 mark: Salt name ({salt_name}) [1]\n"
            f"• 2 marks: Correct balanced equation ({balanced}) [2] (1 mark if formulas correct but coefficients missing)\n"
            "• 2 marks: Laboratory crystallisation steps (evaporation of water [1], slow cooling to form crystals [1])\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Neutralisation: Acids with Soluble Metal Hydroxides",
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
                "Metal hydroxides react with acids to produce a metal salt and water.",
                "Balance the hydrogen and oxygen atoms carefully on both sides.",
                "To get dry crystals from a solution, heat to evaporate water and cool slowly.",
            ],
            "misconception_tags": ["hydroxide_disappears_without_forming_water_myth", "heating_burns_the_salt_myth"],
            "learning_objective_id": "NS9.MM.11.02",
        })

    # Subskill 3: Acids with Metal Oxides
    if chosen_subskill == "acids_with_metal_oxides":
        oxide_rx = [
            ("Copper(II) oxide (black powder)", "Sulfuric acid", "CuO", "H2SO4", "CuSO4", "H2O", "CuO + H₂SO₄ → CuSO₄ + H₂O", "Copper(II) sulfate", "turns from colourless to vibrant clear blue"),
            ("Magnesium oxide (white powder)", "Hydrochloric acid", "MgO", "HCl", "MgCl2", "H2O", "MgO + 2HCl → MgCl₂ + H₂O", "Magnesium chloride", "white powder dissolves to give a clear colourless solution"),
            ("Iron(II) oxide (black powder)", "Hydrochloric acid", "FeO", "HCl", "FeCl2", "H2O", "FeO + 2HCl → FeCl₂ + H₂O", "Iron(II) chloride", "black powder dissolves to give a pale greenish solution"),
        ]
        ox_name, ac_name, ox_f, ac_f, salt_f, w_f, balanced, s_name, visual = oxide_rx[actual_seed % len(oxide_rx)]
        question_text = (
            f"Metal oxides act as basic compounds that neutralise acids.\n\n"
            f"A learner adds a spatula of **{ox_name}** to a beaker containing warm **{ac_name}**.\n\n"
            "1. State the **general equation** for the reaction between an acid and a metal oxide.\n"
            f"2. Write the **balanced chemical equation** for the reaction between {ox_name.split(' (')[0]} and {ac_name}.\n"
            f"3. Describe the **key visual observation** in the beaker as the reaction proceeds ({visual}).\n"
            "4. Why must the reaction mixture be gently warmed to ensure complete reaction of the insoluble metal oxide?"
        )
        sample = (
            "1. **General Equation:** Acid + Metal Oxide → Salt + Water;\n"
            f"2. **Balanced Chemical Equation:** **{balanced}**;\n"
            f"3. **Visual Observation:** The insoluble powder gradually dissolves, and the liquid **{visual}**;\n"
            "4. **Reason for Heating:** Metal oxides are insoluble solids; gentle warming provides thermal kinetic energy to increase collision frequency between acid particles and the solid oxide lattice, accelerating the reaction rate."
        )
        marking = (
            "• 1 mark: General equation (Acid + Metal Oxide → Salt + Water) [1]\n"
            f"• 2 marks: Correct balanced equation ({balanced}) [2]\n"
            f"• 1 mark: Correct visual observation ({visual}) [1]\n"
            "• 1 mark: Explanation of heat accelerating dissolution/reaction rate of insoluble oxide [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Reactions with Metal Oxides: Insoluble Bases",
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
                "Metal oxides are bases: Acid + Metal Oxide → Salt + Water.",
                "Copper oxide (CuO) is black; copper sulfate (CuSO₄) solution is blue.",
                "Warming increases particle collisions and speeds up the reaction.",
            ],
            "misconception_tags": ["metal_oxides_are_acidic_myth", "insoluble_means_unreactive_myth"],
            "learning_objective_id": "NS9.MM.11.03",
        })

    # Subskill 4: Acids with Metal Carbonates
    if chosen_subskill == "acids_with_metal_carbonates":
        carb_rx = [
            ("Calcium carbonate (marble chips / chalk)", "Hydrochloric acid", "CaCO3", "HCl", "CaCl2", "2HCl + CaCO₃ → CaCl₂ + CO₂ + H₂O", "Calcium chloride"),
            ("Sodium carbonate (washing soda)", "Hydrochloric acid", "Na2CO3", "HCl", "NaCl", "2HCl + Na₂CO₃ → 2NaCl + CO₂ + H₂O", "Sodium chloride"),
            ("Calcium carbonate", "Sulfuric acid", "CaCO3", "H2SO4", "CaSO4", "H₂SO₄ + CaCO₃ → CaSO₄ + CO₂ + H₂O", "Calcium sulfate"),
        ]
        c_name, a_name, c_f, a_f, s_f, balanced, salt_name = carb_rx[actual_seed % len(carb_rx)]
        question_text = (
            f"When an acid reacts with a metal carbonate, effervescence (fizzing) is observed.\n\n"
            f"A test tube contains **{c_name}** to which dilute **{a_name}** is added.\n\n"
            "1. State the **general word equation** for the reaction between an acid and a metal carbonate.\n"
            f"2. Write the **balanced chemical equation** for the reaction between {a_name} and {c_name.split(' (')[0]}.\n"
            "3. Name the gas released that causes the observed effervescence.\n"
            "4. Describe the standard **laboratory confirmatory test** for this gas, including the reagent used and the positive observation."
        )
        sample = (
            "1. **General Word Equation:** Acid + Metal Carbonate → Salt + Carbon Dioxide + Water;\n"
            f"2. **Balanced Chemical Equation:** **{balanced}**;\n"
            "3. **Gas Released:** **Carbon dioxide (CO₂)** gas;\n"
            "4. **Confirmatory Limewater Test:** Bubble the released gas through clear, colourless **limewater (calcium hydroxide solution, Ca(OH)₂)**. "
            "A positive result is confirmed when the limewater turns **milky / cloudy** due to the precipitation of insoluble calcium carbonate."
        )
        marking = (
            "• 1 mark: General equation (Acid + Metal Carbonate → Salt + CO₂ + Water) [1]\n"
            f"• 2 marks: Correct balanced equation ({balanced}) [2]\n"
            "• 1 mark: Carbon dioxide (CO₂) identified [1]\n"
            "• 2 marks: Bubble through limewater [1], turns milky/cloudy [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Effervescence & Carbon Dioxide: Acids with Metal Carbonates",
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
                "Carbonates always produce carbon dioxide gas (CO₂) alongside salt and water.",
                "Effervescence means rapid bubbling or fizzing as gas escapes.",
                "The test for CO₂ is bubbling through clear limewater, which turns milky/turbid.",
            ],
            "misconception_tags": ["carbonate_reaction_produces_hydrogen_myth", "limewater_turns_blue_myth"],
            "learning_objective_id": "NS9.MM.11.04",
        })

    # Subskill 5: Practical Applications and Neutralisation
    applications = [
        ("Heartburn / Stomach Indigestion", "Excess stomach acid (Hydrochloric acid, HCl)", "Antacid tablets containing Magnesium hydroxide (Mg(OH)₂) or Calcium carbonate (CaCO₃)", "Neutralises excess stomach acid, raising pH back to comfortable levels"),
        ("Agricultural Soil Acidification", "Soil pH below 5.5 due to acid rain and fertilizers", "Agricultural Lime (Calcium carbonate, CaCO₃ / Calcium oxide, CaO)", "Neutralises soil acidity, restoring optimal nutrient uptake for crop roots"),
        ("Insect Stings Treatment", "Acidic bee sting (formic acid / mellitin)", "Bicarbonate of soda paste (mild base)", "Neutralises the acidic venom in skin tissue, reducing burning sensation and swelling"),
    ]
    app = applications[actual_seed % len(applications)]
    question_text = (
        f"Neutralisation chemistry plays a vital role in everyday medical, agricultural, and domestic contexts.\n\n"
        f"Consider the practical scenario: **{app[0]}**.\n\n"
        f"1. Identify the **chemical cause / acidic condition** in this scenario: *{app[1]}*.\n"
        f"2. Name the **basic substance applied** to treat the condition and explain its mode of action.\n"
        "3. Write a word equation illustrating the chemical neutralisation occurring in this application.\n"
        "4. A wasp sting is chemically alkaline (basic). Explain why applying vinegar (ethanoic acid) relieves a wasp sting, whereas applying baking soda would not."
    )
    sample = (
        f"1. **Underlying Cause:** {app[1]};\n"
        f"2. **Treatment & Mode of Action:** **{app[2]}** is applied. It is a base that reacts chemically with the excess acid, neutralising it to form harmless salts and water, thereby relieving irritation or damage;\n"
        f"3. **Word Equation:** Acid + Base → Salt + Water (e.g., Stomach Acid (HCl) + Antacid Base → Salt + Water);\n"
        "4. **Wasp vs Bee Sting Chemistry:** A wasp sting is alkaline; applying vinegar (a mild acid) neutralises the base. "
        "Applying baking soda (which is also basic) would add more alkaline substance, failing to neutralise and potentially worsening tissue irritation."
    )
    marking = (
        f"• 1 mark: Correct identification of acidic cause ({app[1]}) [1]\n"
        f"• 1 mark: Treatment identified and mechanism explained ({app[2]}) [1]\n"
        "• 1 mark: Valid neutralisation word equation [1]\n"
        "• 2 marks: Wasp venom is alkaline so acid (vinegar) neutralises it [1], baking soda is also basic and would not neutralise [1]\n"
        "**Total: 5 marks**"
    )
    return _normalize_res({
        "title": "Practical Neutralisation: Health, Agriculture & Stings",
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
            "Excess acid is treated with a mild base (antacids, lime).",
            "Bee stings are acidic (neutralised by baking soda).",
            "Wasp stings are alkaline (neutralised by mild acid like vinegar).",
        ],
        "misconception_tags": ["all_insect_stings_are_acidic_myth", "strong_acids_can_be_safely_neutralized_on_skin_with_caustic_soda_myth"],
        "learning_objective_id": "NS9.MM.11.05",
    })
