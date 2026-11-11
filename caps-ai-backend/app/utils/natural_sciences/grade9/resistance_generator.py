"""Natural Sciences Grade 9 Term 3: Resistance Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Resistance.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. concept_of_electrical_resistance: Definition of electrical resistance, Ohms (Omega), electron collision mechanics, energy dissipation.
2. factors_affecting_resistance_length_thickness: Geometric relationships: length (R proportional to L) and cross-sectional thickness (R proportional to 1/A).
3. factors_affecting_resistance_material_temperature: Material resistivity (copper vs nichrome) and thermal lattice vibration effect.
4. resistors_as_control_and_heating_elements: Nichrome heating elements (kettles, toasters, geysers) and rheostats for current regulation.
5. resistor_investigation_and_graphing: Ohm's law relationship (R = V/I), quantitative data tables, and circuit analysis.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Resistance"
ORDERED_SUBSKILLS = [
    "concept_of_electrical_resistance",
    "factors_affecting_resistance_length_thickness",
    "factors_affecting_resistance_material_temperature",
    "resistors_as_control_and_heating_elements",
    "resistor_investigation_and_graphing",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_res"
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

    # Subskill 1: Concept of Electrical Resistance
    if chosen_subskill == "concept_of_electrical_resistance":
        question_text = (
            "Electrical resistance is a fundamental property of conductors in an electric circuit.\n\n"
            "1. Define the term **electrical resistance** and state its standard SI unit and symbol.\n"
            "2. Explain the **microscopic mechanism** of electrical resistance in terms of electrons and metal ions.\n"
            "3. State the **energy conversion** that occurs when electric current forces its way through a high-resistance conductor.\n"
            "4. Contrast a **good electrical conductor** (such as copper) with a **resistor** in terms of current flow opposition."
        )
        sample = (
            "1. **Definition & SI Unit:** Electrical resistance is the opposition or obstruction that a material offers to the flow of electric charge (current). "
            "Its SI unit is the **Ohm**, denoted by the Greek capital letter **Omega (Ω)**;\n"
            "2. **Microscopic Mechanism:** As free conduction electrons drift through the conductor driven by the electric field, they constantly collide with the vibrating positive metal lattice ions. "
            "These collisions obstruct the forward motion of electrons, resulting in electrical resistance;\n"
            "3. **Energy Conversion:** The mechanical energy lost during these microscopic electron-ion collisions converts **electrical potential energy into thermal energy (heat)** and sometimes light (as in incandescent filaments);\n"
            "4. **Conductor vs Resistor:**\n"
            "   • **Good Conductor:** Offers negligible, extremely low resistance, allowing electrons to flow effortlessly with minimal energy loss;\n"
            "   • **Resistor:** Specifically engineered to provide a known, controlled opposition to current, reducing current flow or dissipating energy as heat."
        )
        marking = (
            "• 2 marks: Definition (opposition to electric current flow) [1], SI unit Ohm (Ω) [1]\n"
            "• 2 marks: Collisions between drifting electrons and vibrating metal lattice ions [2]\n"
            "• 1 mark: Electrical energy converted to thermal energy (heat) [1]\n"
            "• 1 mark: Conductor has very low resistance; resistor deliberately opposes current [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Concept of Resistance & Microscopic Electron Collisions",
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
                "Resistance is measured in Ohms (Ω).",
                "It happens when moving electrons bump into vibrating metal atoms.",
                "Collisions convert electrical energy into heat.",
            ],
            "misconception_tags": ["electrons_travel_at_the_speed_of_light_myth", "resistors_destroy_charge_myth"],
            "learning_objective_id": "NS9.EC.15.01",
        })

    # Subskill 2: Factors Affecting Resistance: Length and Thickness
    if chosen_subskill == "factors_affecting_resistance_length_thickness":
        wire_cases = [
            ("Wire A (length 1.0 m, diameter 0.5 mm)", "Wire B (length 2.0 m, diameter 0.5 mm)", "Wire B has double the resistance of Wire A because resistance is directly proportional to conductor length (R ∝ L)"),
            ("Wire C (length 1.0 m, diameter 0.2 mm)", "Wire D (length 1.0 m, diameter 0.8 mm)", "Wire C has much higher resistance than Wire D because resistance is inversely proportional to cross-sectional area (R ∝ 1/A); thinner wires restrict electron flow"),
        ]
        chosen_c = wire_cases[actual_seed % len(wire_cases)]
        question_text = (
            "The physical dimensions of a conductor directly dictate its electrical resistance.\n\n"
            "1. State the relationship between the **length (L)** of a conducting wire and its electrical resistance.\n"
            "2. State the relationship between the **thickness (cross-sectional area, A)** of a conducting wire and its resistance.\n"
            f"3. Consider two nichrome wires: **{chosen_c[0]}** and **{chosen_c[1]}**.\n"
            f"   Predict which wire has greater electrical resistance and explain why: *{chosen_c[2]}*.\n"
            "4. Use the analogy of water flowing through a garden hose to explain why a thick wire carries electric current more easily than a thin wire."
        )
        sample = (
            "1. **Length Relationship:** Resistance is **directly proportional** to length (R ∝ L). Doubling the length of a wire doubles the number of collisions electrons encounter, doubling its resistance;\n"
            "2. **Thickness Relationship:** Resistance is **inversely proportional** to cross-sectional area (R ∝ 1/A). A thicker wire has lower resistance, while a thinner wire has higher resistance;\n"
            f"3. **Wire Comparison:** {chosen_c[2]};\n"
            "4. **Garden Hose Analogy:** Water flows freely through a wide fire hose with little resistance, whereas forcing the same water through a narrow drinking straw requires high pressure and restricts flow. "
            "Similarly, a thick conductor provides a broader cross-sectional channel with vastly more parallel pathways for electrons to drift without crowding."
        )
        marking = (
            "• 1 mark: Directly proportional to length (R ∝ L) [1]\n"
            "• 1 mark: Inversely proportional to cross-sectional area (R ∝ 1/A) [1]\n"
            f"• 2 marks: Correct wire identified with proportional justification [2]\n"
            "• 1 mark: Clear garden hose / pipe analogy explaining wider channel for electrons [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": "Conductor Geometry: Length & Thickness Effects",
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
                "Longer wire = higher resistance (R ∝ L).",
                "Thicker wire = lower resistance (R ∝ 1/A).",
                "Think of a wide hallway versus a narrow doorway for crowds of people.",
            ],
            "misconception_tags": ["thicker_wires_have_higher_resistance_myth", "wire_length_does_not_matter_myth"],
            "learning_objective_id": "NS9.EC.15.02",
        })

    # Subskill 3: Factors Affecting Resistance: Material and Temperature
    if chosen_subskill == "factors_affecting_resistance_material_temperature":
        question_text = (
            "Apart from physical dimensions, the internal material structure and thermal state of a conductor govern its resistance.\n\n"
            "1. Contrast the electrical properties of **copper** and **nichrome alloy** (an alloy of nickel and chromium), explaining why copper is chosen for household wiring while nichrome is chosen for heating elements.\n"
            "2. Describe how the **temperature** of a metal conductor affects its electrical resistance.\n"
            "3. Explain the microscopic reason why heating a metal wire causes its resistance to change.\n"
            "4. What is a **superconductor**, and under what extreme thermal condition does it occur?"
        )
        sample = (
            "1. **Copper vs Nichrome:**\n"
            "   • **Copper:** Has extremely low resistivity (superb conductor); transmits electrical current with negligible energy dissipation and zero overheating in domestic walls;\n"
            "   • **Nichrome:** An alloy engineered with high resistivity and high melting point; efficiently dissipates electrical energy into intense heat without oxidizing or melting;\n"
            "2. **Temperature Effect:** As the temperature of a metallic conductor increases, its electrical resistance **increases**;\n"
            "3. **Microscopic Thermal Explanation:** Increasing temperature delivers thermal kinetic energy to the positive metal ions in the crystal lattice, causing them to vibrate more vigorously and with larger amplitudes. "
            "These violently oscillating ions occupy more effective cross-sectional space, greatly increasing the collision frequency with passing electrons and obstructing current flow;\n"
            "4. **Superconductivity:** A superconductor is a material that exhibits **zero electrical resistance** when cooled below a critical cryogenic temperature (near absolute zero), permitting electric current to flow indefinitely without energy loss."
        )
        marking = (
            "• 2 marks: Copper has low resistance (wiring) [1], nichrome has high resistance (heating) [1]\n"
            "• 1 mark: Resistance increases with temperature in metals [1]\n"
            "• 2 marks: Lattice ions vibrate more violently with heat [1], increasing electron collisions and obstruction [1]\n"
            "• 1 mark: Superconductor has zero resistance at very low cryogenic temperatures [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Material Properties, Temperature & Superconductivity",
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
                "Copper has very low resistance; nichrome has high resistance.",
                "Heating a metal makes its resistance go UP because metal atoms vibrate faster.",
                "Superconductors have zero resistance near absolute zero.",
            ],
            "misconception_tags": ["hot_metals_conduct_better_myth", "all_metals_have_identical_resistance_myth"],
            "learning_objective_id": "NS9.EC.15.03",
        })

    # Subskill 4: Resistors as Control and Heating Elements
    appliances = [
        ("Electric kettle", "wound nichrome spiral element submerged in water", "boils water rapidly by dissipating 2000 W of heat"),
        ("Domestic toaster", "flat ribbon nichrome wire wound on mica sheets", "glows red-hot emitting radiant infrared heat to toast bread"),
        ("Electric geyser (water heater)", "heavy-duty copper-sheathed nichrome heating element", "maintains household hot water at 60 °C"),
        ("Hair dryer", "coiled nichrome wire behind a motorized fan", "heats air blown across the glowing coils"),
    ]
    app = appliances[actual_seed % len(appliances)]
    question_text = (
        f"Resistors are utilized both for energy dissipation and for sensitive electronic control.\n\n"
        f"Consider the domestic appliance: **{app[0]}**.\n\n"
        f"1. Name the **alloy material** commonly used for the heating element inside this appliance: *{app[1]}*.\n"
        "2. State **two vital physical properties** this alloy possesses that make it uniquely suited for heating elements.\n"
        "3. In electronic circuit boards, miniature ceramic resistors are used. Explain why resistors are essential to protect sensitive components like LEDs.\n"
        "4. What is a **rheostat (variable resistor)**, and give one common household application of a variable resistor."
    )
    sample = (
        f"1. **Alloy Material:** **Nichrome** (nickel-chromium alloy);\n"
        "2. **Physical Properties:**\n"
        "   • **High electrical resistivity** (converts significant electrical energy into thermal energy);\n"
        "   • **High melting point** (approx 1400 °C) and does not oxidize or burn when glowing red-hot in air;\n"
        "3. **Circuit Protection (LEDs):** Light-emitting diodes (LEDs) have very low internal resistance and can easily be destroyed by excessive current. "
        "A series resistor limits the current to a safe operating value (e.g. 20 mA), preventing burnout;\n"
        "4. **Variable Resistor (Rheostat):** A resistor whose resistance value can be manually adjusted (e.g. by sliding a contact or turning a dial). "
        "Application: **Volume control knob** on an audio amplifier or **dimmer switch** on a ceiling light."
    )
    marking = (
        "• 1 mark: Nichrome alloy identified [1]\n"
        "• 2 marks: Two properties (high resistivity [1], high melting point / oxidation resistant [1])\n"
        "• 1 mark: Resistors limit current to protect delicate components (LEDs) [1]\n"
        "• 2 marks: Variable resistor defined (adjustable resistance) [1], valid example (dimmer switch / volume dial) [1]\n"
        "**Total: 6 marks**"
    )
    return _normalize_res({
        "title": f"Resistors in Practice: Heating Elements & Circuit Control",
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
            "Heating elements use Nichrome because it has high resistance and won't melt easily.",
            "Resistors in circuits limit current to protect delicate parts like LEDs from burning out.",
            "A variable resistor (rheostat) lets you change resistance, like a light dimmer knob.",
        ],
        "misconception_tags": ["heating_elements_use_copper_myth", "resistors_are_only_useless_energy_wasters_myth"],
        "learning_objective_id": "NS9.EC.15.04",
    })

    # Subskill 5: Resistor Investigation and Graphing
    v_vals = [2.0, 4.0, 6.0, 8.0, 10.0]
    r_val = [4, 5, 8, 10][actual_seed % 4]
    i_vals = [round(v / r_val, 2) for v in v_vals]

    question_text = (
        "A learner conducted a laboratory investigation to determine the resistance of an unknown resistor by measuring potential difference (V) and current (I).\n"
        "The following experimental data was recorded:\n\n"
        f"| Potential Difference V (Volts) | Current I (Amperes) |\n"
        f"| :--- | :--- |\n"
        f"| {v_vals[0]} | {i_vals[0]} |\n"
        f"| {v_vals[1]} | {i_vals[1]} |\n"
        f"| {v_vals[2]} | {i_vals[2]} |\n"
        f"| {v_vals[3]} | {i_vals[3]} |\n"
        f"| {v_vals[4]} | {i_vals[4]} |\n\n"
        "1. State **Ohm's Law relationship** relating Potential Difference (V), Current (I), and Resistance (R).\n"
        f"2. Using the data in the table, calculate the **resistance (R)** of the component.\n"
        "3. Describe the shape of the graph obtained when plotting Potential Difference (V) on the y-axis against Current (I) on the x-axis for an **ohmic resistor**.\n"
        "4. What does the **gradient (slope)** of this V vs I graph represent?"
    )
    sample = (
        "1. **Ohm's Law Formula:**\n"
        "   V = I · R  (or  R = V / I  or  I = V / R);\n"
        f"2. **Resistance Calculation:**\n"
        f"   For any data pair (e.g. V = {v_vals[2]} V, I = {i_vals[2]} A):\n"
        f"   R = V / I = {v_vals[2]} V / {i_vals[2]} A = **{r_val} Ω**;\n"
        "3. **Graph Shape:** A **straight line passing through the origin (0,0)**, indicating that current is directly proportional to potential difference (I ∝ V);\n"
        "4. **Gradient Meaning:** The gradient of the V vs I line (ΔV / ΔI) represents the **constant resistance (R)** of the conductor in Ohms (Ω)."
    )
    marking = (
        "• 1 mark: Ohm's law formula: R = V / I [1]\n"
        f"• 2 marks: Substitution [1] and correct value ({r_val} Ω) [1]\n"
        "• 1 mark: Straight line passing through the origin [1]\n"
        "• 1 mark: Gradient represents the resistance R [1]\n"
        "**Total: 5 marks**"
    )
    return _normalize_res({
        "title": "Ohm's Law Investigation: Quantitative V/I Analysis",
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
            "Use R = V / I with any pair of numbers from the table.",
            f"For example: {v_vals[0]} / {i_vals[0]} = {r_val} Ω.",
            "For an ohmic resistor, the V vs I graph is a straight line through the origin, and its slope is the resistance.",
        ],
        "misconception_tags": ["resistance_equals_i_divided_by_v_error", "curved_graph_for_ohmic_resistors_myth"],
        "learning_objective_id": "NS9.EC.15.05",
    })
