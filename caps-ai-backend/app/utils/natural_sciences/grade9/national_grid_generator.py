"""Natural Sciences Grade 9 Term 3: National Electricity Grid Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/05. Energy and the national electricity grid.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. power_station_energy_conversions: Thermal coal power station transformations (Chemical -> Thermal -> Kinetic -> Electrical).
2. step_up_and_step_down_transformers: Voltage transformations from generation (11-25 kV) to transmission (400 kV) to consumer (230 V).
3. transmission_heating_losses_and_high_voltage: Joule heating dissipation (P_loss = I^2*R) and why ultra-high voltage minimizes current loss.
4. south_african_power_mix_and_koeberg: Mpumalanga coal dominance, Koeberg Nuclear Power Station, uranium fission, Vaalputs waste.
5. environmental_impacts_and_renewable_alternatives: Coal emissions (CO2, SO2, fly ash) vs solar, wind, and pumped storage hydro (Ingula).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Energy and the national electricity grid"
ORDERED_SUBSKILLS = [
    "power_station_energy_conversions",
    "step_up_and_step_down_transformers",
    "transmission_heating_losses_and_high_voltage",
    "south_african_power_mix_and_koeberg",
    "environmental_impacts_and_renewable_alternatives",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_neg"
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

    # Subskill 1: Power Station Energy Conversions
    if chosen_subskill == "power_station_energy_conversions":
        question_text = (
            "Most of South Africa's electrical energy is generated in large baseload coal-fired thermal power stations.\n\n"
            "1. Outline the **complete sequence of energy transformations** that occur from raw pulverized coal to electrical output in the generator.\n"
            "2. Describe the physical role played by the **steam turbine** in the generation process.\n"
            "3. Explain the electromagnetic principle operating inside the **electrical generator** that produces electric current.\n"
            "4. What substance is emitted as large white billowing clouds from the hyperbola-shaped cooling towers of a power station?"
        )
        sample = (
            "1. **Energy Transformation Sequence:**\n"
            "   • **Chemical Potential Energy** stored in raw coal is combusted in the furnace boiler, releasing;\n"
            "   • **Thermal (Heat) Energy**, which boils purified water into superheated high-pressure steam, giving;\n"
            "   • **Kinetic Energy** of fast-moving steam that drives spinning blades of the turbine;\n"
            "   • **Electrical Energy** generated as the spinning turbine rotates heavy electromagnets inside stationary copper wire coils in the generator;\n"
            "2. **Turbine Function:** The steam turbine acts as a mechanical prime mover. High-pressure steam jets expand against its angled blades, converting thermal steam energy into rotational mechanical kinetic energy to spin the generator shaft at 3000 rpm;\n"
            "3. **Electromagnetic Generator Principle (Faraday's Law):** When a conducting coil moves through a magnetic field (or a massive rotor magnet rotates within stationary copper stator coils), "
            "the changing magnetic flux induces an alternating electromotive force (voltage) that drives electric current through the transmission cables;\n"
            "4. **Cooling Tower Emission:** Pure **water vapour / steam** (condensing into tiny water droplets as it cools upon contact with atmospheric air). It is completely non-toxic and is not smoke."
        )
        marking = (
            "• 2 marks: Complete transformation chain (Chemical → Thermal → Kinetic → Electrical) [2]\n"
            "• 1 mark: Turbine converts steam energy into rotational kinetic energy to turn shaft [1]\n"
            "• 2 marks: Generator rotates magnets inside copper coils [1], electromagnetic induction induces current [1]\n"
            "• 1 mark: Pure water vapour/condensed steam (not smoke) [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Coal Power Station: Stepwise Energy Transformations",
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
                "Energy flow: Chemical (coal) → Heat (steam) → Kinetic (turbine) → Electrical (generator).",
                "Turbines spin the generator shaft.",
                "Cooling towers release harmless water vapour, not toxic smoke.",
            ],
            "misconception_tags": ["cooling_towers_emit_toxic_smoke_myth", "generators_create_energy_from_nothing_myth"],
            "learning_objective_id": "NS9.EC.18.01",
        })

    # Subskill 2: Step-up and Step-down Transformers
    if chosen_subskill == "step_up_and_step_down_transformers":
        question_text = (
            "The national electricity grid relies on specialized electrical transformers to transmit electrical power across hundreds of kilometers.\n\n"
            "1. Differentiate between a **step-up transformer** and a **step-down transformer** in terms of voltage and current.\n"
            "2. Identify where in the national grid a **step-up transformer** is installed and state its typical operational voltage.\n"
            "3. Identify where **step-down transformers** are installed and state the standard voltage delivered to South African household wall sockets.\n"
            "4. Why could high-voltage electricity (e.g. 132 000 V) never be fed directly into residential suburban homes?"
        )
        sample = (
            "1. **Step-Up vs Step-Down Transformers:**\n"
            "   • **Step-Up Transformer:** Increases the electrical potential difference (voltage) while proportionally decreasing current (P = V·I);\n"
            "   • **Step-Down Transformer:** Decreases the voltage to a safe usable level while proportionally increasing available current;\n"
            "2. **Step-Up Placement:** Installed directly at the **power station site**; steps generated voltage (approx 20 kV) up to **400 000 V (400 kV) or 765 000 V (765 kV)** for long-distance cross-country transmission;\n"
            "3. **Step-Down Placement & Household Voltage:** Installed at municipal substations and local pole-mounted transformer cans; reduces voltage down to **230 V** for standard single-phase South African residential homes;\n"
            "4. **Danger of Direct High Voltage:** At 132 000 V, electricity would instantly arc across room air gaps, vaporize household appliance wiring, destroy insulation, cause catastrophic explosions, and deliver instant fatal electrocution to any occupant in the house."
        )
        marking = (
            "• 2 marks: Step-up increases voltage/lowers current [1], step-down decreases voltage/increases current [1]\n"
            "• 1 mark: Step-up at power station (up to 400 kV / 765 kV) [1]\n"
            "• 2 marks: Step-down at substations/local poles [1], delivered to homes at 230 V [1]\n"
            "• 1 mark: Severe arcing, explosions, insulation destruction, and fatal shock [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Grid Transformers: Step-Up Transmission to 230 V Domestic",
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
                "Step-up transformers increase voltage at the power station (up to 400 kV).",
                "Step-down transformers decrease voltage near towns and homes down to 230 V.",
                "High voltage must be stepped down before homes so appliances don't explode from arcing.",
            ],
            "misconception_tags": ["transformers_work_on_direct_current_dc_myth", "household_electricity_is_400_kv_myth"],
            "learning_objective_id": "NS9.EC.18.02",
        })

    # Subskill 3: Transmission Heating Losses and High Voltage
    if chosen_subskill == "transmission_heating_losses_and_high_voltage":
        question_text = (
            "Transmitting huge amounts of electrical energy through hundreds of kilometers of overland aluminium transmission cables encounters electrical resistance.\n\n"
            "1. State the formula for the **rate of electrical heat energy loss (Joule heating power)** dissipated in a conductor of resistance R carrying current I.\n"
            "2. Using the relationship P = V · I and P_loss = I²R, explain mathematically why transmitting power at **ultra-high voltage (e.g. 400 000 V)** drastically reduces transmission power loss.\n"
            "3. If electrical current is reduced by a factor of **10**, by what factor is the resistive heat loss in the transmission lines reduced?\n"
            "4. Why are overhead high-voltage transmission lines manufactured from **aluminium reinforced with a steel core** rather than copper?"
        )
        sample = (
            "1. **Heat Loss Formula:** **P_loss = I² · R**  (Power dissipated as heat is proportional to current squared);\n"
            "2. **High-Voltage Physics Explanation:**\n"
            "   • Electrical power transmitted is given by P = V · I. For a fixed required power P, increasing the transmission voltage V by a huge factor decreases the required electric current I proportionally (I = P / V);\n"
            "   • Because line heat losses depend on the square of current (P_loss = I²R), dropping the current drastically diminishes the resistive heating loss dissipated into the atmosphere;\n"
            "3. **Reduction Factor:** Heat loss is reduced by a factor of **100** (since 10² = 100); reducing current by 10 cuts heating losses to just 1% of its former value;\n"
            "4. **Aluminium with Steel Core Selection:**\n"
            "   • Aluminium is much lighter (lower density) and cheaper than copper, preventing massive mechanical sagging between distant pylons;\n"
            "   • The central high-tensile steel core provides mechanical tensile strength to span wide gorges and valleys without snapping under storm wind tension."
        )
        marking = (
            "• 1 mark: Formula P_loss = I²R [1]\n"
            "• 2 marks: P = VI means higher V reduces current I [1], I² relationship means lower I drastically slashes heat loss [1]\n"
            "• 1 mark: Reduced by a factor of 100 (10² = 100) [1]\n"
            "• 2 marks: Aluminium is lightweight/cheaper to prevent sagging [1], steel core provides tensile strength against snapping [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Joule Heating (I²R) & Physics of High-Voltage Transmission",
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
                "Power lost as heat is P = I²R.",
                "Higher voltage means lower current for the same transmitted power.",
                "Lower current means much less heat loss because losses depend on current SQUARED.",
            ],
            "misconception_tags": ["higher_voltage_causes_more_line_heating_myth", "cables_have_zero_resistance_myth"],
            "learning_objective_id": "NS9.EC.18.03",
        })

    # Subskill 4: South African Power Mix and Koeberg
    if chosen_subskill == "south_african_power_mix_and_koeberg":
        question_text = (
            "South Africa's national electricity grid has unique historical and geographical energy generation characteristics.\n\n"
            "1. State the dominant primary energy resource used to generate over 75% of South Africa's electricity, and name the province where most of these power stations are clustered.\n"
            "2. Identify the single **commercial nuclear power station** on the African continent, stating its location and cooling water source.\n"
            "3. Explain how a **nuclear reactor** produces electricity, contrasting its heat source with that of a coal power station.\n"
            "4. Name the remote disposal repository in the Northern Cape where South Africa stores low- and intermediate-level radioactive waste, and explain the safety requirement for storing high-level spent nuclear fuel."
        )
        sample = (
            "1. **Dominant Energy Resource & Region:** **Coal**; clustered primarily in **Mpumalanga Province** (on the Highveld coalfields near Witbank/eMalahleni, close to abundant open-cast coal mines);\n"
            "2. **Nuclear Station Identification:** **Koeberg Nuclear Power Station**; located at Duynefontein near Cape Town in the **Western Cape Province**; uses cold seawater pumped directly from the Atlantic Ocean for reactor cooling;\n"
            "3. **Nuclear vs Coal Heat Generation:**\n"
            "   • Instead of burning chemical bonds in fossil fuels, a nuclear reactor relies on **controlled nuclear fission of Uranium-235 atoms** inside fuel rods;\n"
            "   • Splitting heavy atomic nuclei releases colossal thermal energy, which heats pressurized water to create steam to drive identical steam turbines and generators, with **zero carbon dioxide (CO₂) emissions** during electricity generation;\n"
            "4. **Nuclear Waste Disposal (Vaalputs):**\n"
            "   • Low- and intermediate-level waste is sealed in reinforced concrete barrels and buried at the **Vaalputs National Radioactive Waste Disposal Facility** in the arid Northern Cape;\n"
            "   • High-level spent fuel rods are extremely radioactive and thermally hot; they must be kept submerged in deep on-site spent fuel cooling pools for decades, then transferred into hermetically sealed dry storage steel casks."
        )
        marking = (
            "• 2 marks: Coal [1], Mpumalanga province [1]\n"
            "• 2 marks: Koeberg Nuclear Power Station [1], Western Cape / Atlantic ocean cooling [1]\n"
            "• 2 marks: Controlled uranium fission heat [1], zero CO₂ emissions during generation [1]\n"
            "• 2 marks: Vaalputs repository in Northern Cape [1], submerged cooling pools / dry casks for spent fuel [1]\n"
            "**Total: 8 marks**"
        )
        return _normalize_res({
            "title": "South African Energy Mix: Mpumalanga Coal & Koeberg Nuclear",
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
                "Most South African electricity comes from coal power stations in Mpumalanga.",
                "Koeberg in the Western Cape is South Africa's only nuclear power station.",
                "Nuclear power splits uranium atoms (fission) to make steam without releasing CO₂.",
            ],
            "misconception_tags": ["nuclear_power_plants_explode_like_atomic_bombs_myth", "cooling_towers_at_koeberg_release_radiation_myth"],
            "learning_objective_id": "NS9.EC.18.04",
        })

    # Subskill 5: Environmental Impacts and Renewable Alternatives
    question_text = (
        "Transitioning from fossil fuels to sustainable renewable energy is a major national and global imperative.\n\n"
        "1. List **three severe environmental consequences** directly caused by the combustion of coal in large power stations.\n"
        "2. Contrast **Solar Photovoltaic (PV)** energy generation with coal generation in terms of carbon emissions and water consumption.\n"
        "3. Explain what a **pumped storage hydroelectric scheme** (such as Ingula or Drakensberg) is, and how it acts as a giant 'water battery' during peak national electricity demand.\n"
        "4. State **one major engineering limitation** of wind and solar renewable energy that requires grid energy storage."
    )
    sample = (
        "1. **Coal Environmental Consequences:**\n"
        "   • Release of massive volumes of **carbon dioxide (CO₂)**, driving global climate change and the enhanced greenhouse effect;\n"
        "   • Emission of **sulfur dioxide (SO₂) and nitrogen oxides (NOₓ)**, producing severe acidic rain that acidifies soils and water bodies;\n"
        "   • Generation of millions of tons of **fly ash and particulate pollution**, causing respiratory illness in local communities, and enormous fresh water consumption for cooling;\n"
        "2. **Solar PV vs Coal:** Solar PV produces electricity directly from sunlight using silicon semiconductor cells with **zero carbon emissions during operation** and consumes **zero water** for generating electricity;\n"
        "3. **Pumped Storage Hydro (Water Battery):**\n"
        "   • Consists of two large water dams: one on a high mountain and one in the valley below;\n"
        "   • **During peak demand (evenings):** Water rushes down through massive underground tunnels to spin hydro-turbines, delivering rapid electricity to the grid in under 3 minutes;\n"
        "   • **During off-peak periods (night):** Excess grid electricity is used to pump water back up to the top dam, storing gravitational potential energy for the next day;\n"
        "4. **Renewable Limitation (Intermittency):** Solar and wind are **intermittent and weather-dependent** (solar does not produce at night; wind does not blow continuously), meaning energy generation does not always coincide with peak consumer electricity demand."
    )
    marking = (
        "• 3 marks: Three valid coal impacts (CO₂ climate change [1], SO₂ acid rain [1], ash/water consumption [1])\n"
        "• 1 mark: Solar PV has zero operating CO₂ emissions and zero water use [1]\n"
        "• 2 marks: Upper/lower dam concept [1], releases water during peak and pumps back up off-peak (water battery) [1]\n"
        "• 1 mark: Intermittency (weather-dependent, doesn't match peak demand) [1]\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Coal Environmental Impact vs Renewables & Pumped Storage",
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
            "Coal burning causes carbon dioxide (greenhouse effect), sulfur dioxide (acid rain), and ash.",
            "Solar and wind are clean but intermittent (they only work when sunny or windy).",
            "Pumped storage hydro (like Ingula) pumps water uphill when electricity is cheap and drops it down to generate power during peak times.",
        ],
        "misconception_tags": ["solar_panels_work_at_night_myth", "hydroelectric_schemes_generate_endless_free_energy_myth"],
        "learning_objective_id": "NS9.EC.18.05",
    })
