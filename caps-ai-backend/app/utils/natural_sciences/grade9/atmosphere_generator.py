"""Natural Sciences Grade 9 Term 4: The Atmosphere Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 4/04. Atmosphere.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. atmospheric_gas_composition: Volumetric gas proportions (78% N2, 21% O2, <1% CO2, argon, water vapour).
2. four_atmospheric_layers_altitude_profile: Troposphere, Stratosphere, Mesosphere, Thermosphere vertical structure and characteristics.
3. troposphere_lapse_rate_calculations: Temperature lapse rate calculations (1 °C per 100 m) on mountain elevations.
4. ozone_layer_and_uv_protection: Stratospheric ozone (O3), UV-B/C absorption, melanoma prevention, CFC depletion.
5. greenhouse_effect_vs_global_warming: Natural greenhouse blanket (+15 °C vs -18 °C) vs enhanced global warming from fossil fuel CO2.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "The atmosphere"
ORDERED_SUBSKILLS = [
    "atmospheric_gas_composition",
    "four_atmospheric_layers_altitude_profile",
    "troposphere_lapse_rate_calculations",
    "ozone_layer_and_uv_protection",
    "greenhouse_effect_vs_global_warming",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_atm"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 4) -> Dict[str, Any]:
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

    # Subskill 1: Atmospheric Gas Composition
    if chosen_subskill == "atmospheric_gas_composition":
        question_text = (
            "Earth's atmosphere is a mixture of gases held bound around the planet by gravitational attraction.\n\n"
            "1. State the exact standard **percentage volumetric proportions** of the two main gases that make up 99% of dry atmospheric air:\n"
            "   • (a) **Nitrogen gas (N₂)**\n"
            "   • (b) **Oxygen gas (O₂)**\n"
            "2. State the percentage of **Carbon dioxide (CO₂)** and **Argon (Ar)** present in unpolluted air.\n"
            "3. Explain the biological importance of **Nitrogen** and **Oxygen** to living organisms in the Biosphere.\n"
            "4. Why does atmospheric air pressure decrease continuously as an aircraft climbs higher into the atmosphere?"
        )
        sample = (
            "1. **Primary Atmospheric Gases:**\n"
            "   • (a) **Nitrogen (N₂):** Approximately **78%** by volume;\n"
            "   • (b) **Oxygen (O₂):** Approximately **21%** by volume;\n"
            "2. **Trace Gases:**\n"
            "   • **Argon (Ar):** Approximately **0.93%**;\n"
            "   • **Carbon Dioxide (CO₂):** Approximately **0.04%** (less than 1%);\n"
            "3. **Biological Importance:**\n"
            "   • **Oxygen:** Essential for cellular respiration in aerobic organisms, oxidizing glucose to release cellular energy (ATP);\n"
            "   • **Nitrogen:** Essential building block for amino acids, proteins, and nucleic acids (DNA/RNA). Nitrogen-fixing bacteria convert atmospheric N₂ into nitrates for plant uptake;\n"
            "4. **Pressure vs Altitude Mechanism:** Air pressure is caused by the weight of air molecules pressing down due to gravity. "
            "At higher altitudes, there are fewer air molecules stacked above, and gas molecules are spaced further apart, meaning the density and gravitational weight of overlying air decrease."
        )
        marking = (
            "• 2 marks: Nitrogen 78% [1], Oxygen 21% [1]\n"
            "• 1 mark: Argon ~0.93%, Carbon dioxide ~0.04% (<1%) [1]\n"
            "• 2 marks: Oxygen for cellular respiration [1], Nitrogen for proteins/DNA [1]\n"
            "• 1 mark: Fewer gas molecules above, lower density and weight of air at higher altitude [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Atmospheric Composition & Atmospheric Pressure Gradient",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Air is 78% Nitrogen and 21% Oxygen.",
                "CO₂ is only about 0.04% (less than 1%).",
                "Pressure drops as you climb because there is less air pressing down on you.",
            ],
            "misconception_tags": ["air_is_mostly_oxygen_myth", "carbon_dioxide_makes_up_10_percent_of_air_myth"],
            "learning_objective_id": "NS9.PE.23.01",
        })

    # Subskill 2: Four Atmospheric Layers Altitude Profile
    if chosen_subskill == "four_atmospheric_layers_altitude_profile":
        question_text = (
            "Earth's atmosphere is structured vertically into four concentric thermal layers based on temperature trends.\n\n"
            "Complete the scientific atmospheric layer reference summary:\n\n"
            "1. **Troposphere (0 to 10–12 km):** State the percentage of total atmospheric mass it contains and name **two weather phenomena** exclusive to this layer.\n"
            "2. **Stratosphere (10 to 50 km):** Name the critical gas layer housed within it and explain why commercial airliners prefer to cruise in the lower stratosphere.\n"
            "3. **Mesosphere (50 to 80 km):** State why this is the coldest layer (-90 °C) and describe what happens to space meteoroids passing through it.\n"
            "4. **Thermosphere (80 to 600 km):** Name the human spacecraft orbiting within this layer (at approx 370 km) and explain what solar radiation it absorbs."
        )
        sample = (
            "1. **Troposphere:**\n"
            "   • Contains **over 70% to 75%** of the entire mass of the atmosphere (and almost all atmospheric water vapour);\n"
            "   • Exclusive weather phenomena: Rain clouds, lightning/thunderstorms, tornadoes, hail, and snow;\n"
            "2. **Stratosphere:**\n"
            "   • Houses the **Ozone Layer (O₃)**;\n"
            "   • Commercial jet aircraft fly in the lower stratosphere because it is dry, stable, and completely free of turbulent weather storms and cloud turbulence, maximizing fuel efficiency;\n"
            "3. **Mesosphere:**\n"
            "   • Characterized by extremely thin air and no ozone to absorb UV, reaching temperatures below -90 °C;\n"
            "   • Infalling space debris and **meteoroids burn up** due to extreme atmospheric friction and compression, producing 'shooting stars';\n"
            "4. **Thermosphere:**\n"
            "   • The **International Space Station (ISS)** orbits within the thermosphere at approximately 370–400 km altitude;\n"
            "   • Directly absorbs high-energy, dangerous **solar X-rays and extreme ultraviolet (EUV) radiation**, causing temperatures to soar above 1000 °C."
        )
        marking = (
            "• 2 marks: Troposphere: >70% mass [1], clouds/storms/rain [1]\n"
            "• 2 marks: Stratosphere: Ozone layer [1], stable non-turbulent flight [1]\n"
            "• 2 marks: Mesosphere: coldest layer [1], burns meteoroids via friction [1]\n"
            "• 2 marks: Thermosphere: International Space Station (ISS) [1], absorbs solar X-rays/EUV [1]\n"
            "**Total: 8 marks**"
        )
        return _normalize_res({
            "title": "Atmospheric Layers: Vertical Architecture (0 to 600 km)",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Troposphere (0-10 km): weather and life, >70% of air.",
                "Stratosphere (10-50 km): ozone layer and airplanes.",
                "Mesosphere (50-80 km): coldest layer, burns meteors. Thermosphere (>80 km): ISS orbits here.",
            ],
            "misconception_tags": ["clouds_exist_in_the_stratosphere_myth", "space_begins_at_10_km_myth"],
            "learning_objective_id": "NS9.PE.23.02",
        })

    # Subskill 3: Troposphere Lapse Rate Calculations
    if chosen_subskill == "troposphere_lapse_rate_calculations":
        mountain_cases = [
            ("Drakensberg Mafadi Peak", 3450, 25.0, 1.0, 100),
            ("Table Mountain", 1086, 22.0, 1.0, 100),
            ("Mount Kilimanjaro", 5895, 30.0, 1.0, 100),
        ]
        m_name, m_alt, sea_temp, rate, unit_m = mountain_cases[actual_seed % len(mountain_cases)]
        temp_drop = round((m_alt / unit_m) * rate, 1)
        summit_temp = round(sea_temp - temp_drop, 1)

        question_text = (
            "Within the troposphere, air temperature drops steadily as altitude increases, governed by the environmental lapse rate.\n"
            "The standard national curriculum lapse rate in the troposphere is **1 °C per 100 metres of elevation**.\n\n"
            f"A scientific expedition measures a sea-level baseline temperature of **{sea_temp} °C** at the coast.\n"
            f"The team ascends to the summit of **{m_name}**, at an altitude of **{m_alt} metres above sea level**.\n\n"
            "1. State the formula for the temperature drop (ΔT) with altitude.\n"
            f"2. Calculate the expected **temperature drop (ΔT)** when ascending from sea level to the summit of {m_name}.\n"
            f"3. Calculate the predicted **temperature at the summit** of {m_name}.\n"
            "4. Explain the physical reason why air cools as it ascends in the troposphere."
        )
        sample = (
            "1. **Lapse Rate Formula:**\n"
            "   ΔT = (Altitude in metres / 100 m) × 1.0 °C;\n"
            f"2. **Temperature Drop Calculation:**\n"
            f"   ΔT = ({m_alt} m / 100 m) × 1.0 °C = **{temp_drop} °C drop**;\n"
            f"3. **Summit Temperature Calculation:**\n"
            f"   T_summit = T_sealevel - ΔT = {sea_temp} °C - {temp_drop} °C = **{summit_temp} °C**;\n"
            "4. **Physical Mechanism of Cooling:** The troposphere is heated from below: sunlight passes through transparent air and heats the ground surface, "
            "which radiates heat upwards. As rising air parcels ascend into lower atmospheric pressure, they expand adiabatically. "
            "Expanding air pushes against surrounding air, performing work at the expense of its internal thermal kinetic energy, causing its temperature to drop."
        )
        marking = (
            "• 1 mark: Correct lapse rate formula [1]\n"
            f"• 2 marks: Calculation of temperature drop ({temp_drop} °C) [2]\n"
            f"• 2 marks: Final summit temperature calculation ({summit_temp} °C) [2]\n"
            "• 1 mark: Heating from ground upwards and adiabatic expansion cooling at lower pressure [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Troposphere Lapse Rate: {m_name} ({m_alt} m)",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "For every 100 metres you climb, temperature drops by 1 °C.",
                f"Drop = {m_alt} / 100 = {temp_drop} °C.",
                f"Summit temp = {sea_temp} - {temp_drop} = {summit_temp} °C.",
            ],
            "misconception_tags": ["higher_altitudes_are_hotter_because_closer_to_the_sun_myth", "forgetting_to_subtract_temperature_drop_error"],
            "learning_objective_id": "NS9.PE.23.03",
        })

    # Subskill 4: Ozone Layer and UV Protection
    if chosen_subskill == "ozone_layer_and_uv_protection":
        question_text = (
            "The stratospheric ozone layer is Earth's natural sunscreen shielding planetary life from lethal solar radiation.\n\n"
            "1. State the **chemical formula** of an ozone molecule and identify the atmospheric layer where it is concentrated (15–35 km).\n"
            "2. Describe the vital shielding function of ozone: What specific solar radiation does it absorb?\n"
            "3. State **three severe medical or ecological consequences** to life on Earth if the ozone layer were depleted.\n"
            "4. Name the industrial chemical class (used in old refrigerators and aerosol cans) that caused the Antarctic 'ozone hole', and name the historic international treaty that banned them."
        )
        sample = (
            "1. **Ozone Formula & Location:** **O₃** (triatomic oxygen); concentrated in the **Stratosphere**;\n"
            "2. **Shielding Function:** Ozone molecules absorb 98% of high-energy, harmful **ultraviolet radiation (specifically UV-B and UV-C)** emitted by the Sun, "
            "converting photon energy into heat and preventing mutagenic radiation from reaching Earth's surface;\n"
            "3. **Consequences of Ozone Depletion:**\n"
            "   • **Human Health:** Drastic increase in malignant skin cancers (melanoma) and eye cataracts;\n"
            "   • **Marine Ecosystems:** Destruction of surface marine **phytoplankton**, collapsing the foundation of global oceanic food webs;\n"
            "   • **Terrestrial Flora:** Severe damage to photosynthetic mechanisms and cellular DNA in agricultural crop plants;\n"
            "4. **Ozone-Depleting Chemicals & Treaty:**\n"
            "   • **Chemical Class:** **Chlorofluorocarbons (CFCs)**;\n"
            "   • **Global Treaty:** The **Montreal Protocol (1987)**, which legally phased out global CFC production."
        )
        marking = (
            "• 1 mark: Formula O₃ in Stratosphere [1]\n"
            "• 1 mark: Absorbs harmful solar UV-B and UV-C radiation [1]\n"
            "• 3 marks: Three consequences (skin cancer/cataracts [1], phytoplankton destruction [1], crop damage [1])\n"
            "• 2 marks: Chlorofluorocarbons (CFCs) [1], Montreal Protocol [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Stratospheric Ozone Layer (O₃) & UV Shielding",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Ozone is O₃ and lives in the Stratosphere.",
                "It absorbs dangerous Ultraviolet (UV) radiation.",
                "CFC chemicals damaged ozone, which was saved by the Montreal Protocol.",
            ],
            "misconception_tags": ["ozone_hole_causes_global_warming_confusion", "ozone_is_o2_myth"],
            "learning_objective_id": "NS9.PE.23.04",
        })

    # Subskill 5: Greenhouse Effect vs Global Warming
    question_text = (
        "Learners frequently confuse the natural greenhouse effect with anthropogenic global warming.\n\n"
        "1. Differentiate clearly between the **Natural Greenhouse Effect** and the **Enhanced Greenhouse Effect (Global Warming)**.\n"
        "2. Name the **three most significant greenhouse gases** present in Earth's atmosphere.\n"
        "3. Explain what Earth's average planetary surface temperature would be **without** the natural greenhouse effect (approx -18 °C vs +15 °C).\n"
        "4. Describe step-by-step how excess greenhouse gases trap heat energy:\n"
        "   • What wavelength of light passes through the atmosphere from the Sun?\n"
        "   • What wavelength of energy is re-radiated by Earth's surface and trapped by greenhouse gas molecules?"
    )
    sample = (
        "1. **Natural vs Enhanced Greenhouse Effect:**\n"
        "   • **Natural Greenhouse Effect:** A natural, life-sustaining atmospheric process where greenhouse gases trap outgoing terrestrial heat, keeping Earth warm enough for liquid water and life;\n"
        "   • **Enhanced Greenhouse Effect (Global Warming):** Anthropogenic elevation of greenhouse gases from burning fossil fuels and deforestation, trapping excessive heat and unnaturally accelerating global climate instability;\n"
        "2. **Three Key Greenhouse Gases:** **Water vapour (H₂O)**, **Carbon dioxide (CO₂)**, and **Methane (CH₄)** (also Nitrous oxide, N₂O);\n"
        "3. **Temperature Without Greenhouse Effect:** Without greenhouse gases, Earth's average surface temperature would plummet to approximately **-18 °C** (a frozen, lifeless ice planet), rather than our comfortable habitable average of **+15 °C** (a 33 °C warming benefit);\n"
        "4. **Thermal Trapping Mechanism:**\n"
        "   • Incoming solar energy enters as **short-wavelength visible and ultraviolet light**, which passes transparently through atmospheric gases to heat Earth's surface;\n"
        "   • The warm Earth re-radiates this energy upwards as **long-wavelength infrared (thermal heat) radiation**;\n"
        "   • Greenhouse gas molecules absorb this outgoing infrared radiation, vibrating and re-emitting thermal energy in all directions, including back towards the Earth's surface."
    )
    marking = (
        "• 2 marks: Natural (life-sustaining) [1] vs Enhanced (anthropogenic warming from fossil fuels) [1]\n"
        "• 1 mark: Three gases named (Water vapour, CO₂, Methane) [1]\n"
        "• 1 mark: Plummets to -18 °C without it, vs +15 °C with it [1]\n"
        "• 2 marks: Shortwave solar light penetrates [1], outgoing longwave infrared trapped by greenhouse gases [1]\n"
        "**Total: 6 marks**"
    )
    return _normalize_res({
        "title": "Greenhouse Effect: Natural Blanket vs Global Warming",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 4,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "The natural greenhouse effect is good: it keeps Earth at +15 °C instead of a frozen -18 °C.",
            "Shortwave visible light comes from the Sun; Earth radiates longwave infrared heat.",
            "Greenhouse gases (CO₂, methane, water vapour) trap outgoing infrared heat.",
        ],
        "misconception_tags": ["greenhouse_effect_is_purely_bad_and_unnatural_myth", "greenhouse_gases_trap_sunlight_directly_myth"],
        "learning_objective_id": "NS9.PE.23.05",
    })
