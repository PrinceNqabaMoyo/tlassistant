"""Natural Sciences Grade 9 Term 3: Electric Cells as Energy Systems Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Electric cells as energy systems.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. chemical_to_electrical_conversion: Principles of cells converting chemical energy to electrical energy; cell vs battery.
2. electrochemical_half_cell_components: Zinc/copper electrode pairs, electrolytes, and external electron flow.
3. fruit_cell_investigation: Constructing citrus fruit cells (lemon/orange), measuring potential difference, internal resistance.
4. cells_in_series_voltage_sum: Series voltage summation law (V_total = V1 + V2 + ...), effect on current and bulb brightness.
5. rechargeable_vs_primary_cells: Primary single-use vs secondary rechargeable cells, reversible chemistry, heavy metal disposal.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Electric cells as energy systems"
ORDERED_SUBSKILLS = [
    "chemical_to_electrical_conversion",
    "electrochemical_half_cell_components",
    "fruit_cell_investigation",
    "cells_in_series_voltage_sum",
    "rechargeable_vs_primary_cells",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_ecel"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 3) -> Dict[str, Any]:
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

    # Subskill 1: Chemical to Electrical Conversion
    if chosen_subskill == "chemical_to_electrical_conversion":
        question_text = (
            "An electrochemical cell is an energy system that powers portable electrical devices.\n\n"
            "1. State the **fundamental energy conversion** that takes place inside an electric cell during operation.\n"
            "2. Distinguish clearly between an **electric cell** and a **battery** in physics terminology.\n"
            "3. Draw or describe the standard circuit diagram symbols used to represent a single cell versus a battery of three cells in series.\n"
            "4. What causes an electric cell to eventually run 'flat' or stop producing current?"
        )
        sample = (
            "1. **Energy Conversion:** Converts **chemical potential energy** into **electrical energy**;\n"
            "2. **Cell vs Battery:**\n"
            "   • **Cell:** A single electrochemical unit consisting of two electrodes and an electrolyte (usually producing 1.5 V);\n"
            "   • **Battery:** A collection of two or more interconnected cells coupled together in series or parallel to provide greater voltage or capacity;\n"
            "3. **Circuit Symbols:**\n"
            "   • **Single Cell:** One long thin line (positive terminal, +) and one shorter thicker line (negative terminal, -);\n"
            "   • **Three-Cell Battery:** Three alternating pairs of long thin and short thick lines connected in a continuous chain with dashed or solid connecting lines;\n"
            "4. **Reason for Running Flat:** The active chemical reactants (the zinc electrode and electrolyte ions) undergo irreversible oxidation/reduction until the available chemical reactants are completely exhausted and can no longer generate an electrical potential difference."
        )
        marking = (
            "• 1 mark: Chemical potential energy to electrical energy [1]\n"
            "• 2 marks: Clear distinction between single cell [1] and battery (two or more connected cells) [1]\n"
            "• 1 mark: Accurate description of circuit symbols (long thin positive, short thick negative) [1]\n"
            "• 1 mark: Exhaustion of chemical reactants inside cell [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Electrochemical Energy Conversion: Cell vs Battery",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Cells store chemical potential energy and convert it to electrical energy.",
                "A battery is two or more cells connected together.",
                "In circuit diagrams, the long line is positive (+) and the short thick line is negative (-).",
            ],
            "misconception_tags": ["batteries_store_raw_electricity_myth", "a_single_aa_is_a_battery_terminology_error"],
            "learning_objective_id": "NS9.EC.14.01",
        })

    # Subskill 2: Electrochemical Half-Cell Components
    if chosen_subskill == "electrochemical_half_cell_components":
        question_text = (
            "A simple electrochemical cell is assembled using a beaker containing dilute sulfuric acid (or copper sulfate solution), "
            "into which a strip of zinc and a strip of copper are immersed without touching. Connecting wires link the electrodes through a sensitive micro-ammeter.\n\n"
            "1. Identify the **three essential functional components** present in this electrochemical cell.\n"
            "2. Identify the **negative electrode (anode)** and the **positive electrode (cathode)** between zinc and copper.\n"
            "3. State the **direction of electron flow** through the external conducting wire connecting the two metal strips.\n"
            "4. Explain the function of the **electrolyte solution** in maintaining the circuit."
        )
        sample = (
            "1. **Three Essential Components:**\n"
            "   • Anode electrode (Zinc strip);\n"
            "   • Cathode electrode (Copper strip);\n"
            "   • Electrolyte liquid solution (dilute acid or ionic salt solution);\n"
            "2. **Electrode Identification:**\n"
            "   • Negative Electrode (Anode): **Zinc (Zn)** strip (more reactive, readily oxidizes/loses electrons);\n"
            "   • Positive Electrode (Cathode): **Copper (Cu)** strip (less reactive);\n"
            "3. **Electron Flow Direction:** Electrons flow from the **zinc electrode to the copper electrode** through the external metallic wire;\n"
            "4. **Electrolyte Function:** The electrolyte contains free-moving mobile ions that conduct charge through the liquid, completing the internal circuit and balancing ionic charges between the electrodes."
        )
        marking = (
            "• 2 marks: Three components named (two different metal electrodes [1], electrolyte liquid [1])\n"
            "• 1 mark: Zinc is negative (anode) and copper is positive (cathode) [1]\n"
            "• 1 mark: External electron flow from zinc to copper [1]\n"
            "• 1 mark: Electrolyte provides mobile ions to complete internal circuit [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Zinc-Copper Electrochemical Cell Architecture",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "An electrochemical cell needs two different metals and an electrolyte liquid.",
                "Zinc is more reactive than copper, so it loses electrons and acts as the negative terminal.",
                "Electrons travel from zinc to copper through the wire, while ions travel through the liquid.",
            ],
            "misconception_tags": ["electrons_flow_through_the_electrolyte_liquid_myth", "both_electrodes_can_be_same_metal_myth"],
            "learning_objective_id": "NS9.EC.14.02",
        })

    # Subskill 3: Fruit Cell Investigation
    if chosen_subskill == "fruit_cell_investigation":
        fruits = [
            ("Lemon", "citric acid", "0.9 V"),
            ("Grapefruit", "citric and ascorbic acid", "0.85 V"),
            ("Potato", "phosphoric acid and potassium salts", "0.75 V"),
        ]
        fr = fruits[actual_seed % len(fruits)]
        question_text = (
            f"A learner constructs a biological electric cell using a fresh **{fr[0]}**, a galvanized zinc nail, and a clean copper coin.\n\n"
            f"1. Explain what constituent in the {fr[0]} acts as the **electrolyte**, and why it is capable of conducting electricity ({fr[1]}).\n"
            f"2. When connected to a digital multimeter, the cell registers an open-circuit potential difference of approximately **{fr[2]}**.\n"
            "   Why is a single fruit cell unable to illuminate a standard 3.0 V flashlight light bulb?\n"
            "3. Describe how the learner can modify their apparatus to successfully light a 3.0 V red LED bulb.\n"
            "4. State the **independent variable** and the **dependent variable** if the learner investigates whether different fruits produce different voltages."
        )
        sample = (
            f"1. **Electrolyte Nature:** The **{fr[1]}** in the fruit juice acts as the electrolyte. It contains dissociated hydrogen ions and organic acid anions that move freely to conduct charge internally;\n"
            f"2. **Why It Cannot Light Bulb:** A single cell produces only {fr[2]}, which is far below the 3.0 V required threshold. Furthermore, the fruit cell has a high internal resistance, which restricts the delivered current to only microamperes;\n"
            "3. **Modification:** Connect **four or more fruit cells together in series** (connecting the copper coin of one fruit to the zinc nail of the next fruit in a continuous chain). This sums their individual voltages (e.g. 4 × 0.9 V = 3.6 V), providing sufficient potential difference to forward-bias and light the LED;\n"
            "4. **Investigation Variables:**\n"
            "   • **Independent Variable:** The type/variety of fruit used (e.g. lemon, orange, potato, tomato);\n"
            "   • **Dependent Variable:** The electrical potential difference (voltage, in Volts) measured across the terminals."
        )
        marking = (
            f"• 1 mark: Fruit juice/acid ({fr[1]}) contains mobile ions acting as electrolyte [1]\n"
            f"• 2 marks: Low voltage ({fr[2]} < 3.0 V) [1], high internal resistance restricts current [1]\n"
            "• 2 marks: Connect 4+ fruit cells in series (copper to zinc) to sum voltages [2]\n"
            "• 2 marks: Independent variable (fruit type) [1], Dependent variable (voltage measured) [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": f"Bio-Electrochemical Fruit Cell: {fr[0]} Investigation",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Fruit juice contains acid ions that act as an electrolyte.",
                "One fruit cell only gives under 1 V and very low current.",
                "To get 3 V, connect multiple fruit cells in series (copper of one to zinc of the next).",
            ],
            "misconception_tags": ["fruit_generates_electricity_without_metals_myth", "parallel_cells_multiply_voltage_myth"],
            "learning_objective_id": "NS9.EC.14.03",
        })

    # Subskill 4: Cells in Series Voltage Sum
    if chosen_subskill == "cells_in_series_voltage_sum":
        cell_counts = [2, 3, 4, 5]
        n_cells = cell_counts[actual_seed % len(cell_counts)]
        v_each = 1.5
        v_tot = round(n_cells * v_each, 1)

        question_text = (
            f"A learner constructs an electrical circuit containing **{n_cells} identical torch cells connected in series**.\n"
            f"Each individual cell has a nominal potential difference of **{v_each} V**.\n\n"
            "1. State the **mathematical formula** for the total potential difference (V_total) of n cells connected in series.\n"
            f"2. Calculate the **total voltage** supplied to the circuit by these {n_cells} cells.\n"
            "3. Contrast the **brightness of a miniature light bulb** connected to this battery of cells compared to when connected to only one cell.\n"
            "4. What would happen to the bulb if one of the cells was accidentally inserted backwards (reversed polarity)?"
        )
        sample = (
            "1. **Series Voltage Formula:**\n"
            "   V_total = V₁ + V₂ + V₃ + ... + V_n;\n"
            f"2. **Total Voltage Calculation:**\n"
            f"   V_total = {n_cells} × {v_each} V = **{v_tot} V**;\n"
            f"3. **Bulb Brightness Comparison:** The bulb glows **much brighter** with {n_cells} cells in series because the higher total voltage drives a significantly larger electric current through the filament resistance (I = V/R), dissipating greater power (P = V·I);\n"
            f"4. **Reversed Cell Effect:** The reversed cell opposes the other cells, subtracting its voltage ({v_each} V) from the total rather than adding to it. Total voltage drops by 2 × 1.5 V = 3.0 V compared to normal, making the bulb glow much dimmer or not at all."
        )
        marking = (
            "• 1 mark: Series voltage summation law: V_total = V1 + V2 + ... [1]\n"
            f"• 2 marks: Calculation showing formula and answer: {v_tot} V [2]\n"
            "• 2 marks: Bulb glows much brighter [1], higher voltage drives larger current / power [1]\n"
            "• 1 mark: Reversed cell opposes and subtracts voltage, drastically dimming bulb [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Cells in Series: Voltage Summation ({n_cells} Cells)",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Cells in series add their voltages: V_total = V1 + V2 + V3...",
                f"{n_cells} cells at 1.5 V each give {v_tot} V.",
                "Higher voltage pushes more current, making the bulb brighter. Reversing a cell subtracts voltage.",
            ],
            "misconception_tags": ["series_cells_keep_voltage_constant_myth", "cells_in_series_last_longer_than_parallel_myth"],
            "learning_objective_id": "NS9.EC.14.04",
        })

    # Subskill 5: Rechargeable vs Primary Cells
    question_text = (
        "Modern society relies on both disposable primary cells and secondary rechargeable batteries.\n\n"
        "1. Differentiate between a **primary cell** (e.g. zinc-carbon) and a **secondary cell** (e.g. lithium-ion in smartphones) in terms of chemical reversibility.\n"
        "2. Explain what happens chemically during the **recharging cycle** of a secondary battery.\n"
        "3. Name **two heavy metals** found in discarded batteries that present severe environmental hazards.\n"
        "4. Why is it illegal and ecologically hazardous to dispose of spent batteries in regular municipal landfill trash bins?"
    )
    sample = (
        "1. **Primary vs Secondary Cells:**\n"
        "   • **Primary Cell:** Undergoes an **irreversible chemical reaction**; once active chemicals are consumed, it cannot be recharged and must be discarded;\n"
        "   • **Secondary Cell:** Designed with a **reversible chemical reaction** that can be repeatedly reversed by passing an external electrical current in the opposite direction;\n"
        "2. **Recharging Process:** Connecting an external electric charger forces electrical current backwards through the cell, driving the redox reaction in reverse and restoring the original chemical reactants to their initial high-energy state;\n"
        "3. **Hazardous Heavy Metals:** **Cadmium (Cd)**, **Lead (Pb)**, **Mercury (Hg)**, or **Nickel (Ni)**;\n"
        "4. **Landfill Hazard:** In open municipal landfills, battery casings corrode and rupture over time. Toxic heavy metals and corrosive acidic/alkaline electrolytes leach through soil into underground water tables and nearby river ecosystems, poisoning drinking water and bioaccumulating up the food chain to cause human organ damage."
    )
    marking = (
        "• 2 marks: Primary is irreversible chemical reaction [1], secondary is reversible [1]\n"
        "• 1 mark: External current forces reaction in reverse restoring reactants [1]\n"
        "• 1 mark: Two valid heavy metals named (lead, cadmium, mercury, nickel) [1]\n"
        "• 2 marks: Battery casings corrode [1], heavy metals leach into groundwater causing toxic bioaccumulation [1]\n"
        "**Total: 6 marks**"
    )
    return _normalize_res({
        "title": "Primary vs Secondary Cells & Battery E-Waste Safety",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 3,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Primary cells cannot be recharged (one-time use).",
            "Secondary cells can be recharged by reversing the chemical reaction.",
            "Batteries contain toxic heavy metals like lead and cadmium that can leak into groundwater if thrown in normal bins.",
        ],
        "misconception_tags": ["all_batteries_can_be_recharged_if_plugged_in_myth", "batteries_leak_raw_electricity_into_ground_myth"],
        "learning_objective_id": "NS9.EC.14.05",
    })
