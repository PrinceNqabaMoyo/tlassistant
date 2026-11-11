"""Natural Sciences Grade 9 Term 3: Cost of Electrical Energy Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/06. Cost of electrical energy.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. power_rating_and_watt_unit_conversion: Power definition (1 W = 1 J/s), conversion from Watts to Kilowatts (kW = W / 1000).
2. electrical_energy_kwh_formula: Energy consumption formula (E = P * t in kWh), understanding the Kilowatt-hour (3.6 MJ).
3. cost_calculation_with_tariffs: Cost calculation (Cost = kWh * Tariff), prepaid meter electricity credit consumption.
4. appliance_consumption_ranking: Sequencing high-demand heating vs low-demand domestic appliances.
5. energy_efficiency_and_conservation_strategies: Efficiency comparison (Incandescent vs LED), geyser blankets, solar water heaters.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Cost of electrical energy"
ORDERED_SUBSKILLS = [
    "power_rating_and_watt_unit_conversion",
    "electrical_energy_kwh_formula",
    "cost_calculation_with_tariffs",
    "appliance_consumption_ranking",
    "energy_efficiency_and_conservation_strategies",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_cee"
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

    # Subskill 1: Power Rating and Watt Unit Conversion
    if chosen_subskill == "power_rating_and_watt_unit_conversion":
        appliances_watts = [
            ("Microwave oven", 1200),
            ("Electric kettle", 2200),
            ("Hair dryer", 1800),
            ("LED smart television", 150),
            ("Electric frying pan", 1500),
            ("Desktop computer", 350),
        ]
        chosen = appliances_watts[actual_seed % len(appliances_watts)]
        kw_val = chosen[1] / 1000

        question_text = (
            "Every domestic electrical appliance features an official manufacturer's technical rating plate.\n\n"
            "1. Define the physical quantity **electrical power (P)** and state its SI unit and symbol.\n"
            "2. State what 1 Watt (1 W) represents in terms of basic energy transfer per unit time (Joules and seconds).\n"
            f"3. A technical label on an **{chosen[0]}** states: `230 V ~ 50 Hz, {chosen[1]} W`.\n"
            f"   Convert this power rating into **kilowatts (kW)**.\n"
            f"4. Explain what a power rating of **{chosen[1]} W** means about the rate of electrical energy consumption of this appliance."
        )
        sample = (
            "1. **Electrical Power Definition:** The rate at which electrical energy is transferred, converted, or consumed by an electrical appliance per unit time. "
            "Its SI unit is the **Watt (W)**;\n"
            "2. **1 Watt Equivalence:** **1 W = 1 Joule per second (1 J/s)**;\n"
            f"3. **Conversion to Kilowatts:**\n"
            f"   Power (kW) = Power (W) / 1000 = {chosen[1]} W / 1000 = **{kw_val} kW**;\n"
            f"4. **Physical Meaning:** A rating of {chosen[1]} W means that the {chosen[0]} consumes and converts **{chosen[1]} Joules of electrical energy every single second** into thermal or mechanical energy."
        )
        marking = (
            "• 1 mark: Rate of energy transfer/consumption [1]\n"
            "• 1 mark: 1 W = 1 Joule per second (1 J/s) [1]\n"
            f"• 2 marks: Conversion formula / 1000 [1], {kw_val} kW [1]\n"
            f"• 1 mark: Converts {chosen[1]} Joules of energy per second [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": f"Power Rating & Watt to Kilowatt Conversion: {chosen[0]}",
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
                "Power is measured in Watts: 1 Watt = 1 Joule per second.",
                f"To convert Watts to Kilowatts, divide by 1000: {chosen[1]} / 1000 = {kw_val} kW.",
                f"A {chosen[1]} W device uses {chosen[1]} Joules of energy every second it runs.",
            ],
            "misconception_tags": ["power_and_energy_are_the_same_thing_myth", "multiply_by_1000_for_kilowatts_error"],
            "learning_objective_id": "NS9.EC.19.01",
        })

    # Subskill 2: Electrical Energy kWh Formula
    if chosen_subskill == "electrical_energy_kwh_formula":
        devices = [
            ("Electric room heater", 2000, 2.0, 5, 10.0),
            ("Swimming pool pump", 750, 0.75, 8, 6.0),
            ("Air conditioner unit", 1500, 1.5, 6, 9.0),
            ("Washing machine", 1000, 1.0, 3, 3.0),
        ]
        d = devices[actual_seed % len(devices)]

        question_text = (
            f"An **{d[0]}** rated at **{d[1]} W** is switched on and operated continuously for **{d[3]} hours**.\n\n"
            "1. State the **mathematical formula** used to calculate electrical energy consumed (E) in kilowatt-hours (kWh).\n"
            f"2. Convert the power rating of the {d[0]} from Watts into **kilowatts (kW)**.\n"
            f"3. Calculate the **total electrical energy consumed (E)** in **kilowatt-hours (kWh)** during the {d[3]}-hour operation.\n"
            "4. Why do electricity supply utilities (like Eskom and municipalities) bill consumers in kilowatt-hours (kWh) rather than standard SI Joules (J)?"
        )
        sample = (
            "1. **Energy Formula:**\n"
            "   E = P · t  (where E is in kWh, P is power in kW, and t is time in hours);\n"
            f"2. **Power in kW:**\n"
            f"   P = {d[1]} W / 1000 = **{d[2]} kW**;\n"
            f"3. **Energy Calculation:**\n"
            f"   E = P × t = {d[2]} kW × {d[3]} hours = **{d[4]} kWh**;\n"
            "4. **Reason for Using kWh:** The standard SI unit, the Joule, is extremely tiny (1 kWh = 3 600 000 Joules). "
            "Billing in Joules would require unwieldy, multi-million or billion-digit numbers on electricity bills (e.g. 10 kWh = 36 000 000 J). "
            "The kilowatt-hour is a much more practical, human-readable commercial unit."
        )
        marking = (
            "• 1 mark: Formula: E = P × t [1]\n"
            f"• 1 mark: P = {d[2]} kW [1]\n"
            f"• 2 marks: Substitution [1], {d[4]} kWh [1]\n"
            "• 1 mark: Joules are too small, leading to multi-million digit numbers; kWh is practical [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": f"Energy Consumption Calculation: {d[0]} (kWh)",
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
                "Formula: Energy (kWh) = Power (kW) × Time (hours).",
                f"First divide {d[1]} W by 1000 to get {d[2]} kW.",
                f"Then multiply by {d[3]} hours to get {d[4]} kWh.",
            ],
            "misconception_tags": ["kwh_means_kilowatts_per_hour_error", "forgetting_to_convert_watts_to_kw_error"],
            "learning_objective_id": "NS9.EC.19.02",
        })

    # Subskill 3: Cost Calculation with Tariffs
    if chosen_subskill == "cost_calculation_with_tariffs":
        scenarios = [
            ("Geyser (water heater)", 3000, 3.0, 4, 12.0, 2.50, 30.00, 900.00),
            ("Tumble dryer", 2500, 2.5, 2, 5.0, 2.80, 14.00, 420.00),
            ("Oil heater", 1800, 1.8, 8, 14.4, 2.60, 37.44, 1123.20),
        ]
        sc = scenarios[actual_seed % len(scenarios)]

        question_text = (
            f"A household operates a **{sc[0]}** with a power rating of **{sc[1]} W** for **{sc[3]} hours per day**.\n"
            f"The municipal electricity tariff is **R {sc[5]:.2f} per kWh**.\n\n"
            "1. State the formula used to calculate the **financial cost of electricity consumed**.\n"
            f"2. Calculate the daily energy consumption in **kilowatt-hours (kWh)**.\n"
            f"3. Calculate the **daily cost** (in Rands) to run this appliance.\n"
            f"4. Calculate the **total monthly cost** (for a 30-day month) of operating this appliance.\n"
            "5. If a prepaid electricity meter has a credit balance of R 150,00 remaining, calculate how many whole days this appliance could run on that credit."
        )
        days_rem = int(150.00 // sc[6])
        sample = (
            "1. **Cost Formula:**\n"
            "   Cost = Energy Consumed (kWh) × Electricity Tariff (R/kWh);\n"
            f"2. **Daily Energy Consumption:**\n"
            f"   P = {sc[1]} W / 1000 = {sc[2]} kW\n"
            f"   E = P × t = {sc[2]} kW × {sc[3]} h = **{sc[4]} kWh per day**;\n"
            f"3. **Daily Cost:**\n"
            f"   Cost = {sc[4]} kWh × R {sc[5]:.2f}/kWh = **R {sc[6]:.2f} per day**;\n"
            f"4. **Monthly Cost (30 Days):**\n"
            f"   Monthly Cost = R {sc[6]:.2f} × 30 days = **R {sc[7]:.2f}**;\n"
            f"5. **Prepaid Days Remaining:**\n"
            f"   Days = R 150,00 / R {sc[6]:.2f} per day = {150.00 / sc[6]:.2f} days ==> **{days_rem} full days**."
        )
        marking = (
            "• 1 mark: Cost formula: Cost = kWh × Tariff [1]\n"
            f"• 1 mark: Daily kWh: {sc[4]} kWh [1]\n"
            f"• 2 marks: Daily cost calculation: R {sc[6]:.2f} [2]\n"
            f"• 2 marks: Monthly cost (30 days): R {sc[7]:.2f} [2]\n"
            f"• 1 mark: Prepaid days: {days_rem} full days [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": f"Electricity Tariff & Cost Analysis: {sc[0]}",
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
                f"Daily energy = {sc[2]} kW × {sc[3]} h = {sc[4]} kWh.",
                f"Daily cost = {sc[4]} kWh × R {sc[5]:.2f} = R {sc[6]:.2f}.",
                f"Multiply by 30 for the monthly cost: R {sc[7]:.2f}.",
            ],
            "misconception_tags": ["multiplying_watts_instead_of_kw_by_tariff_error", "forgetting_to_multiply_by_30_for_monthly_error"],
            "learning_objective_id": "NS9.EC.19.03",
        })

    # Subskill 4: Appliance Consumption Ranking
    appliance_suite = [
        ("Electric Stove & Oven", 3500, "High demand (Thermal heating element)"),
        ("Electric Geyser", 2500, "High demand (Continuous thermal water heating)"),
        ("Electric Kettle", 2000, "High demand (Rapid liquid heating, short duration)"),
        ("Steam Clothing Iron", 1600, "High demand (Thermal soleplate heating)"),
        ("Microwave Oven", 1200, "Moderate demand (Electromagnetic heating)"),
        ("Refrigerator (compressor)", 150, "Low-to-moderate demand (Intermittent cycling motor)"),
        ("LED Smart Television", 80, "Low demand (Solid-state electronic display)"),
        ("Laptop Computer", 60, "Low demand (Microprocessor logic)"),
        ("LED Light Bulb", 9, "Very low demand (Efficient electroluminescent diode)"),
    ]
    shuffled_app = list(appliance_suite)
    r.shuffle(shuffled_app)
    subset_apps = shuffled_app[:5]
    names_str = "\n".join([f"• {name} (rating: {w} W)" for name, w, _ in subset_apps])

    question_text = (
        "A family wants to audit their home electricity bill and lists five appliances with manufacturer power ratings in random order:\n\n"
        f"{names_str}\n\n"
        "1. Arrange these five appliances in order of **decreasing power demand (from highest power to lowest power consumption)**.\n"
        "2. Identify the common physical mechanism present in all the top high-power consumption domestic appliances.\n"
        "3. Explain why an electric kettle (2000 W) often costs less to operate over a month than an electric geyser (2500 W), despite both having high power ratings."
    )
    sorted_apps = sorted(subset_apps, key=lambda x: x[1], reverse=True)
    order_str = "\n".join([f"   {i+1}. {name} ({w} W - {cat})" for i, (name, w, cat) in enumerate(sorted_apps)])

    sample = (
        "1. **Decreasing Power Order (Highest to Lowest):**\n"
        f"{order_str};\n"
        "2. **Common High-Power Mechanism:** All high-demand appliances contain **resistive thermal heating elements** (such as coiled nichrome wire) engineered to convert massive amounts of electrical energy directly into heat;\n"
        "3. **Kettle vs Geyser Operational Cost:** Total electrical energy consumed depends on both **Power AND Time (E = P · t)**. "
        "A kettle runs for only 3 to 4 minutes per boil (accumulating perhaps 15 minutes a day), whereas a geyser switches on automatically for 4 to 6 hours each day to reheat a 150 L reservoir of hot water. "
        "Because time t is vastly greater for the geyser, its monthly kWh consumption and financial cost are far higher."
    )
    marking = (
        "• 2 marks: Correct descending sequence from highest to lowest power [2] (1 mark for partial order)\n"
        "• 1 mark: Resistive thermal heating elements (converting electricity to heat) [1]\n"
        "• 2 marks: Cost depends on Energy = Power × Time [1], kettle runs for minutes while geyser runs for hours daily [1]\n"
        "**Total: 5 marks**"
    )
    return _normalize_res({
        "title": "Domestic Appliance Power Hierarchy & Operating Time",
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
            "Thermal heating appliances (stove, geyser, kettle) use thousands of Watts.",
            "Electronics and LED lights use very few Watts.",
            "Energy consumed is Power × Time: a kettle has high power but runs for only minutes.",
        ],
        "misconception_tags": ["appliances_with_higher_wattage_always_cost_more_monthly_myth", "fridges_use_more_power_than_geysers_myth"],
        "learning_objective_id": "NS9.EC.19.04",
    })

    # Subskill 5: Energy Efficiency and Conservation Strategies
    question_text = (
        "Implementing energy efficiency strategies saves households money and reduces strain on the national grid.\n\n"
        "1. Compare a traditional **60 W incandescent light bulb** with a modern **9 W LED bulb** producing identical light luminosity (800 lumens):\n"
        "   • (a) Explain why the incandescent bulb requires 60 W while the LED bulb only requires 9 W.\n"
        "   • (b) Calculate the **percentage electrical energy saved** by switching from the incandescent bulb to the LED bulb.\n"
        "2. Explain how installing a **geyser thermal insulation blanket** and pipe lagging saves household electrical energy.\n"
        "3. Explain what **standby power consumption ('vampire power')** is, and how home dwellers can eliminate it."
    )
    pct_saved = round(((60 - 9) / 60) * 100, 1)
    sample = (
        "1. **Incandescent vs LED Comparison:**\n"
        "   • (a) **Efficiency Difference:** The incandescent bulb works by heating a thin tungsten filament until it glows white-hot; **over 90% of its electrical energy is wasted as heat**, with less than 10% emitted as light. "
        "The LED bulb uses semiconductor electroluminescence that converts electricity directly into photons of light with minimal waste heat, requiring only 9 W;\n"
        f"   • (b) **Percentage Energy Saved:**\n"
        f"     Energy Saved = ((60 W - 9 W) / 60 W) × 100% = (51 / 60) × 100% = **{pct_saved}% energy saved**;\n"
        "2. **Geyser Blanket Function:** A geyser blanket is made of thick fiberglass or reflective insulating foil wrapped tightly around the water cylinder. "
        "It acts as a thermal barrier that drastically slows conduction and radiation heat loss into cold ceiling cavities, allowing the water to stay hot for hours and preventing the geyser thermostat from repeatedly switching on the 3000 W element;\n"
        "3. **Standby Power ('Vampire Draw'):** Many electronic devices (TVs, decoders, microwave digital clocks, phone chargers left plugged in) continue to draw a small background electrical current (3 to 15 W) when turned off with remote controls. "
        "Over an entire year, this standby power accumulates significantly on electricity bills. Dwellers can eliminate it by **switching off the appliance at the physical wall plug switch**."
    )
    marking = (
        "• 2 marks: Incandescent wastes 90% as heat [1], LED converts directly to light without heat waste [1]\n"
        f"• 2 marks: Percentage saved formula [1], {pct_saved}% [1]\n"
        "• 1 mark: Geyser blanket slows thermal heat loss, reducing element reheating cycles [1]\n"
        "• 1 mark: Standby draw defined and eliminated by switching off wall socket [1]\n"
        "**Total: 6 marks**"
    )
    return _normalize_res({
        "title": "Energy Efficiency: LED Lighting & Geyser Conservation",
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
            "Incandescent bulbs waste 90% of power as heat. LEDs are cold and super efficient.",
            "Energy saved = ((60 - 9) / 60) × 100% = 85%.",
            "Geyser blankets trap heat so the element turns on less often. Switch off wall plugs to kill standby power.",
        ],
        "misconception_tags": ["appliances_draw_zero_power_on_standby_myth", "led_bulbs_produce_high_heat_myth"],
        "learning_objective_id": "NS9.EC.19.05",
    })
