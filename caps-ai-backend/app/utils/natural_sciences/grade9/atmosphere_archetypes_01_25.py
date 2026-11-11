"""Grade 9 Natural Sciences - The Atmosphere: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/04. The atmosphere.md
Focus:
Atmospheric composition (N2, O2, Ar, CO2), Gravity & barometric pressure gradient, High altitude hypoxia,
Five thermal layers (troposphere, stratosphere, mesosphere, thermosphere, exosphere), Troposphere lapse rate & weather,
Stratospheric ozone Chapman cycle, UV shielding (UV-B/C), CFC catalytic ozone destruction & Montreal Protocol,
Mesosphere coldest temperatures & meteor ablation, Thermosphere extreme kinetic temperatures & ionosphere radio skip,
Auroras & ISS orbit, Exosphere space boundary, Solar insolation & planetary albedo, Terrestrial longwave infrared radiation,
Natural greenhouse effect (+15 °C vs -18 °C) & molecular dipole infrared absorption.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_atmospheric_composition_major_gases_percentages(rng: random.Random) -> Dict[str, Any]:
    gas_info = rng.choice([
        ("Nitrogen (N2)", "78,08%", "most abundant gas, biologically fixed by soil bacteria to synthesize plant proteins and DNA"),
        ("Oxygen (O2)", "20,95%", "vital gas supporting aerobic cellular respiration in living organisms and combustion"),
        ("Argon (Ar)", "0,93%", "chemically unreactive noble gas produced by the radioactive decay of potassium-40 in rocks"),
        ("Carbon dioxide (CO2)", "~0,04%", "essential trace greenhouse gas absorbed by photosynthetic autotrophs to build carbohydrates")
    ])
    gas_name, pct, role = gas_info
    prompt = (
        "Dry air near Earth's surface is a uniform mixture of several distinct gases.\n\n"
        f"Which gas makes up approximately **{pct}** of dry atmospheric air by volume, and what is its primary biological or physical role?"
    )
    correct = f"**{gas_name}**; it is the {role}."
    options = [
        correct,
        f"**{gas_name}**; it is a flammable rocket fuel that explodes whenever heated by sunlight.",
        "**Hydrogen (H2)**; it makes up 90% of the air and causes clouds to float in the sky.",
        "**Helium (He)**; it makes up 50% of the air and turns rain into liquid neon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric gas volumetric composition:\n"
        "1. Nitrogen (N2) = 78,08%\n"
        "2. Oxygen (O2) = 20,95%\n"
        "3. Argon (Ar) = 0,93%\n"
        "4. Carbon dioxide (CO2) = ~0,04% (420 ppm)\n"
        f"Step 2: Analysis for {pct}:\n"
        f"{gas_name} accounts for {pct}; {role}."
    )
    return {
        "id": f"ns9_atm_01_{rng.randint(100000, 999999)}",
        "subskill": "01_atmospheric_composition_major_gases_percentages",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Which gas accounts for {pct} of the atmosphere?",
            "tier_2": f"It is {gas_name}, which {role[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmospheric_composition_percentages"]
    }


def arch_02_atmospheric_pressure_gravitational_density_gradient(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "At sea level, atmospheric pressure is approximately **101,3 kPa** (1 atmosphere), but pressure drops continuously as altitude increases.\n\n"
        "What fundamental force holds atmospheric gases to the Earth, and why does air density decrease with increasing altitude?"
    )
    correct = "Earth's gravitational attraction pulls gas molecules toward the planetary surface; air molecules near the surface are compressed by the weight of all the overlying air layers, creating maximum density and pressure at sea level that decreases exponentially upward."
    options = [
        correct,
        "Magnetic fields push air upward into outer space, creating a vacuum near the ground.",
        "Air density is completely uniform from the ground all the way to the Moon.",
        "The Sun's heat evaporates air at the top of the atmosphere, pulling all air molecules into space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Gravitational compression:\n"
        "Gravity holds Earth's gaseous envelope.\n"
        "Step 2: Hydrostatic equilibrium:\n"
        "Each atmospheric layer must support the weight of the air column above it: dP/dz = -ρg. Compression is greatest at the bottom (sea level ~1,2 kg/m³, 101,3 kPa) and decays exponentially with altitude."
    )
    return {
        "id": f"ns9_atm_02_{rng.randint(100000, 999999)}",
        "subskill": "02_atmospheric_pressure_gravitational_density_gradient",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What pulls air down and compresses it at sea level?",
            "tier_2": "Gravity pulls gas molecules downward; overlying air weight compresses lower air.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmospheric_pressure_gravity_gradient"]
    }


def arch_03_high_altitude_hypoxia_and_mountain_climber_physiology(rng: random.Random) -> Dict[str, Any]:
    mtn = rng.choice(["Thabana Ntlenyana (Drakensberg, 3 482 m)", "Mount Kilimanjaro (5 895 m)", "Mount Everest (8 848 m)"])
    prompt = (
        f"When mountaineers ascend high peaks like {mtn}, they experience 'thin air' and shortness of breath (altitude sickness / hypoxia).\n\n"
        "What physical and physiological factor causes high-altitude hypoxia?"
    )
    correct = "Although the percentage of oxygen in dry air remains 20,95%, lower atmospheric pressure at high altitude reduces the partial pressure of oxygen (pO2), resulting in a weaker diffusion pressure gradient to drive oxygen across alveolar membranes into the blood."
    options = [
        correct,
        "The percentage of oxygen drops to 0%, while pure nitrogen turns into liquid ice in the lungs.",
        "Mountain gravity is ten times stronger than sea level gravity, pulling blood out of climbers' ears.",
        "Plants on mountain peaks consume all atmospheric oxygen through nocturnal photosynthesis."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Dalton's Law of Partial Pressures:\n"
        "pO2 = 0,2095 × P_total. The fractional percentage of O2 does not change with altitude.\n"
        "Step 2: Alveolar diffusion physics:\n"
        "At high altitude, lower total barometric pressure (e.g. ~33 kPa on Everest vs 101 kPa at sea level) reduces pO2, diminishing the concentration gradient driving O2 diffusion across lung alveolar capillaries into hemoglobin."
    )
    return {
        "id": f"ns9_atm_03_{rng.randint(100000, 999999)}",
        "subskill": "03_high_altitude_hypoxia_and_mountain_climber_physiology",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does the percentage of oxygen change, or does the barometric pressure change?",
            "tier_2": "Oxygen stays 20,95%, but lower total pressure reduces oxygen partial pressure (pO2).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hypoxia_altitude_partial_pressure_oxygen"]
    }


def arch_04_five_thermal_layers_vertical_sequence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth's atmosphere is subdivided into distinct concentric vertical layers defined primarily by their temperature gradients.\n\n"
        "Which list correctly orders the **five atmospheric layers** from Earth's surface outward into space?"
    )
    correct = "Troposphere → Stratosphere → Mesosphere → Thermosphere → Exosphere"
    options = [
        correct,
        "Exosphere → Thermosphere → Mesosphere → Stratosphere → Troposphere",
        "Stratosphere → Troposphere → Exosphere → Thermosphere → Mesosphere",
        "Mesosphere → Stratosphere → Troposphere → Exosphere → Thermosphere"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric thermal vertical profile from surface to space:\n"
        "1. Troposphere (0 to ~12 km)\n"
        "2. Stratosphere (~12 to ~50 km)\n"
        "3. Mesosphere (~50 to ~85 km)\n"
        "4. Thermosphere (~85 to ~600 km)\n"
        "5. Exosphere (~600 to ~10 000 km)"
    )
    return {
        "id": f"ns9_atm_04_{rng.randint(100000, 999999)}",
        "subskill": "04_five_thermal_layers_vertical_sequence",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which layer touches the ground and which fades into space?",
            "tier_2": "Troposphere at surface, then Stratosphere, Mesosphere, Thermosphere, Exosphere.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmospheric_layers_vertical_ordering"]
    }


def arch_05_troposphere_thickness_environmental_lapse_rate(rng: random.Random) -> Dict[str, Any]:
    elev_m = rng.choice([1000, 2000, 3000])
    surface_temp = rng.choice([25, 28, 30])
    lapse_rate = 6.5  # °C per 1000 m
    temp_drop = (elev_m / 1000) * lapse_rate
    expected_temp = surface_temp - temp_drop
    prompt = (
        f"In the **troposphere**, air temperature decreases steadily with altitude at an average rate of **6,5 °C per 1 000 m** (the environmental lapse rate).\n\n"
        f"If the surface temperature at sea level is **{surface_temp} °C**, what is the expected temperature at an elevation of **{elev_m} m**?"
    )
    correct = f"{expected_temp:.1f} °C (temperature drops by {temp_drop:.1f} °C: {surface_temp} - {temp_drop:.1f} = {expected_temp:.1f} °C)."
    distractors = [
        f"{surface_temp + temp_drop:.1f} °C (temperature increases with altitude in the troposphere).",
        f"-50,0 °C (the troposphere immediately freezes at 500 m elevation).",
        f"100,0 °C (air boils into steam above sea level)."
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "Step 1: Environmental lapse rate formula:\n"
        f"ΔT = - (Lapse Rate × Height / 1000) = - (6,5 °C/km × {elev_m/1000} km) = -{temp_drop:.1f} °C.\n"
        "Step 2: Calculate temperature at elevation:\n"
        f"T = T_surface - ΔT = {surface_temp} °C - {temp_drop:.1f} °C = {expected_temp:.1f} °C."
    )
    return {
        "id": f"ns9_atm_05_{rng.randint(100000, 999999)}",
        "subskill": "05_troposphere_thickness_environmental_lapse_rate",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Subtract 6,5 °C for every 1 000 m of elevation.",
            "tier_2": f"Drop = {elev_m/1000} × 6,5 = {temp_drop:.1f} °C. Subtract from {surface_temp} °C.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["troposphere_lapse_rate_calculation"]
    }


def arch_06_troposphere_weather_engine_convection_and_clouds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Nearly all of Earth's weather phenomena (clouds, wind, rain, and thunderstorms) occur exclusively in the **troposphere**.\n\n"
        "What two factors make the troposphere the primary weather engine of the planet?"
    )
    correct = "It contains approximately 80% of total atmospheric mass and over 99% of all atmospheric water vapor, powered by vigorous thermal convection driven by solar heating of the Earth's surface from below."
    options = [
        correct,
        "It is the only layer where human aircraft fly and create clouds with their jet engines.",
        "It contains no air molecules and is filled with boiling steam from undersea volcanoes.",
        "It is heated exclusively by laser beams radiating from the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Water vapor concentration:\n"
        "Virtually all water vapor is confined to the warm lower troposphere (cold upper layers freeze out moisture).\n"
        "Step 2: Convective instability:\n"
        "Because the troposphere is heated from the ground up, warm buoyant air rises, expands adiabatically, cools, and condenses into clouds, generating storms and convective circulation."
    )
    return {
        "id": f"ns9_atm_06_{rng.randint(100000, 999999)}",
        "subskill": "06_troposphere_weather_engine_convection_and_clouds",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why is weather confined to the troposphere?",
            "tier_2": "It holds 99% of water vapor and 80% of mass, heated from below by Earth's surface.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["troposphere_weather_engine_convection"]
    }


def arch_07_stratosphere_temperature_inversion_and_stability(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Commercial jet airliners prefer cruising in the lower **stratosphere** (altitude ~11 to 14 km).\n\n"
        "What thermal profile characterizes the stratosphere, and why does it provide smooth, turbulence-free flying conditions?"
    )
    correct = "Temperature increases with altitude (a thermal inversion) due to ultraviolet absorption by ozone; warmer air sitting atop cooler air suppresses vertical convection currents, creating calm, stratified, non-turbulent air."
    options = [
        correct,
        "Temperature drops to absolute zero, which turns airplane wings into frictionless ice.",
        "The stratosphere has zero atmospheric pressure so airplanes float with engines switched off.",
        "Strong vertical tornadoes constantly blow airplanes forward at supersonic speeds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Temperature inversion in the stratosphere:\n"
        "From ~-56 °C at the tropopause up to ~0 °C at the stratopause.\n"
        "Step 2: Dynamic stability:\n"
        "In a temperature inversion, air displaced upward is colder and denser than surrounding air, causing it to sink back down. This negative buoyancy extinguishes vertical convection, preventing cumulus cloud formation and turbulence."
    )
    return {
        "id": f"ns9_atm_07_{rng.randint(100000, 999999)}",
        "subskill": "07_stratosphere_temperature_inversion_and_stability",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does temperature rise or fall in the stratosphere, and how does this affect turbulence?",
            "tier_2": "Temperature rises with altitude (inversion), suppressing vertical turbulence.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stratosphere_temperature_inversion_stability"]
    }


def arch_08_ozone_layer_formation_chapman_photochemical_cycle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **ozone layer** in the stratosphere continuously produces and breaks down ozone through the **Chapman photochemical cycle**.\n\n"
        "What chemical reaction sequence describes the natural formation of ozone (O3) in the stratosphere?"
    )
    correct = "High-energy solar UV-C breaks oxygen molecules into free oxygen atoms (O2 + UV → 2O); individual oxygen atoms then collide and bond with diatomic oxygen molecules to form ozone (O + O2 → O3)."
    options = [
        correct,
        "Nitrogen gas reacts with water vapor during lightning storms to form ozone (N2 + H2O → O3).",
        "Photosynthetic trees emit ozone directly through their leaf stomata into the upper atmosphere.",
        "Carbon dioxide reacts with helium under intense moonlight to form ozone molecules."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Photolysis of O2 (Chapman mechanism):\n"
        "Shortwave solar UV (λ < 240 nm) photodissociates O2: O2 + hν → O + O.\n"
        "Step 2: Ozone synthesis:\n"
        "Free oxygen radicals combine with ambient O2 in the presence of a third body chaperone molecule (M): O + O2 + M → O3 + M."
    )
    return {
        "id": f"ns9_atm_08_{rng.randint(100000, 999999)}",
        "subskill": "08_ozone_layer_formation_chapman_photochemical_cycle",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "How does solar UV turn O2 into O3?",
            "tier_2": "UV splits O2 into free O atoms; O atoms bond with O2 molecules to form O3.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ozone_formation_chapman_cycle"]
    }


def arch_09_ozone_shielding_uv_b_and_uv_c_radiation_protection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The stratospheric ozone layer functions as a vital planetary sunshield for all terrestrial life.\n\n"
        "What specific bands of solar ultraviolet radiation does stratospheric ozone absorb, and what biological damage does it prevent?"
    )
    correct = "It absorbs 100% of lethal UV-C (λ < 280 nm) and ~95% of damaging UV-B (280–315 nm), shielding living cells from DNA mutations, skin melanomas, corneal cataracts, and marine phytoplankton collapse."
    options = [
        correct,
        "It absorbs 100% of harmless visible light, plunging the Earth into permanent darkness.",
        "It absorbs radio waves broadcast by satellites to prevent cell phone reception.",
        "It absorbs infrared heat waves, keeping Earth's surface frozen solid."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: UV spectral bands:\n"
        "• UV-A (315–400 nm): Passes through ozone largely unattenuated.\n"
        "• UV-B (280–315 nm): Strongly absorbed by O3; causes cyclobutane pyrimidine dimers in DNA.\n"
        "• UV-C (100–280 nm): Completely screened out by O2 and O3.\n"
        "Step 2: Biospheric consequence:\n"
        "Without the stratospheric ozone shield, terrestrial colonization by complex life would have been biologically impossible due to nucleic acid destruction."
    )
    return {
        "id": f"ns9_atm_09_{rng.randint(100000, 999999)}",
        "subskill": "09_ozone_shielding_uv_b_and_uv_c_radiation_protection",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which UV wavelengths are blocked by ozone to prevent skin cancer and DNA damage?",
            "tier_2": "All UV-C and ~95% of UV-B are absorbed by ozone.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ozone_shielding_uvb_uvc_protection"]
    }


def arch_10_cfcs_chlorofluorocarbons_catalytic_ozone_depletion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the late 20th century, scientists discovered that synthetic **chlorofluorocarbons (CFCs)** were destroying stratospheric ozone.\n\n"
        "How does a single chlorine radical released from a CFC molecule destroy thousands of ozone molecules in a **catalytic chain reaction**?"
    )
    correct = "A chlorine atom reacts with ozone to form chlorine monoxide and oxygen (Cl + O3 → ClO + O2); then ClO reacts with free oxygen to regenerate the chlorine atom (ClO + O → Cl + O2), freeing the chlorine radical to attack another ozone molecule in a repeating cycle."
    options = [
        correct,
        "Chlorine atoms freeze into solid salt cubes that fall to the ground like hail.",
        "CFCs absorb all water vapor in the atmosphere until clouds dry up completely.",
        "Chlorine gas reacts with nitrogen to form permanent liquid bleach in the stratosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Photolysis of CFCs:\n"
        "CCl3F + hν → CCl2F + Cl•.\n"
        "Step 2: Catalytic destruction cycle:\n"
        "Reaction 1: Cl• + O3 → ClO• + O2\n"
        "Reaction 2: ClO• + O → Cl• + O2\n"
        "Net reaction: O3 + O → 2O2.\n"
        "Because Cl• is regenerated, a single chlorine atom can catalytically destroy up to 100 000 ozone molecules before being deactivated into stable reservoir species (HCl, ClONO2)."
    )
    return {
        "id": f"ns9_atm_10_{rng.randint(100000, 999999)}",
        "subskill": "10_cfcs_chlorofluorocarbons_catalytic_ozone_depletion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why is the destruction of ozone by chlorine called 'catalytic'?",
            "tier_2": "Chlorine is regenerated in the cycle: Cl + O3 → ClO + O2, then ClO + O → Cl + O2.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cfc_catalytic_ozone_depletion_cycle"]
    }


def arch_11_antarctic_ozone_hole_polar_stratospheric_clouds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Every Austral spring (September–October), a severe seasonal thinning of ozone known as the **Antarctic Ozone Hole** opens above the South Pole.\n\n"
        "What unique meteorological conditions above Antarctica trigger this massive seasonal ozone loss?"
    )
    correct = "The winter polar vortex traps isolated, ultra-cold air (< -78 °C) that forms Polar Stratospheric Clouds (PSCs); these ice crystals provide solid catalytic surfaces that convert inactive chlorine reservoirs into highly reactive Cl2 gas, which sunlight photodissociates into destructive Cl radicals in spring."
    options = [
        correct,
        "Migrating penguin flocks exhale toxic carbon monoxide that dissolves the ozone layer.",
        "Underground volcanic eruptions at Mount Erebus burn away all stratospheric gases.",
        "The magnetic South Pole repels ozone molecules across the equator into the northern hemisphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Isolation and polar cold:\n"
        "Circumpolar winds create the stable polar vortex. Temperatures drop below 195 K, nucleating Type I (nitric acid trihydrate) and Type II (water ice) Polar Stratospheric Clouds (PSCs).\n"
        "Step 2: Heterogeneous surface chemistry:\n"
        "Reservoirs react on PSC surfaces: HCl + ClONO2 → Cl2 + HNO3.\n"
        "When spring sunlight returns in September, photolysis breaks Cl2 into Cl radicals, unleashing rapid catalytic ozone destruction."
    )
    return {
        "id": f"ns9_atm_11_{rng.randint(100000, 999999)}",
        "subskill": "11_antarctic_ozone_hole_polar_stratospheric_clouds",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What icy clouds form in the cold Antarctic polar vortex to release chlorine?",
            "tier_2": "Polar Stratospheric Clouds (PSCs) convert reservoir chlorine into reactive chlorine gas.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["antarctic_ozone_hole_psc_mechanics"]
    }


def arch_12_montreal_protocol_international_treaty_and_recovery(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Adopted in 1987, the **Montreal Protocol on Substances that Deplete the Ozone Layer** is universally recognized as the most successful environmental treaty in history.\n\n"
        "What global regulatory action was enacted under the Montreal Protocol, and what has been the measurable atmospheric result?"
    )
    correct = "It legally mandated the worldwide phaseout of production and consumption of chlorofluorocarbons (CFCs) and halons, successfully halting ozone depletion and enabling the stratospheric ozone layer to begin measurable global recovery."
    options = [
        correct,
        "It banned all international commercial airline flights to keep the stratosphere empty.",
        "It required all countries to build giant chemical factories that pump artificial ozone into space.",
        "It placed a global tax on ordinary tap water to reduce ocean evaporation."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Montreal Protocol mandate (1987):\n"
        "Phased out production of CFCs, HCFCs, halons, and carbon tetrachloride.\n"
        "Step 2: Environmental verification:\n"
        "Atmospheric concentrations of chlorine and bromine peaked in the late 1990s and are declining. Climate-chemistry models project the Antarctic ozone hole will heal to pre-1980 levels by ~2060–2070."
    )
    return {
        "id": f"ns9_atm_12_{rng.randint(100000, 999999)}",
        "subskill": "12_montreal_protocol_international_treaty_and_recovery",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What synthetic chemicals were banned worldwide by the Montreal Protocol?",
            "tier_2": "Phased out CFCs and halons, allowing the ozone layer to recover.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["montreal_protocol_cfc_phaseout"]
    }


def arch_13_mesosphere_temperature_minimum_coldest_layer(rng: random.Random) -> Dict[str, Any]:
    temp_c = rng.choice([-90, -95, -100])
    prompt = (
        f"At the top of the **mesosphere** (the mesopause at ~85 km altitude), temperatures plummet to **{temp_c} °C**.\n\n"
        "Why is the mesosphere the coldest atmospheric layer in the entire Earth system?"
    )
    correct = "It has negligible ozone to absorb solar UV, very low concentrations of greenhouse gases to trap heat, and rarefied carbon dioxide molecules that radiate thermal energy away into space through infrared radiative cooling."
    options = [
        correct,
        "It is shielded from the Sun by thick sheets of frozen liquid nitrogen clouds.",
        "It is located in outer space where the Sun's light cannot reach.",
        "It contains giant icebergs that were launched into space by ocean geysers."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mesospheric energy balance:\n"
        "Above the stratopause, ozone concentration drops sharply, removing the primary solar UV absorption source.\n"
        "Step 2: Radiative cooling:\n"
        "CO2 molecules collisionally excited by ambient nitrogen radiate 15 µm infrared photons directly to space without reabsorption, cooling the mesopause down to ~130–140 K (-90 to -100 °C)."
    )
    return {
        "id": f"ns9_atm_13_{rng.randint(100000, 999999)}",
        "subskill": "13_mesosphere_temperature_minimum_coldest_layer",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why does temperature plunge to -90 °C in the mesosphere?",
            "tier_2": "No ozone UV absorption and strong radiative cooling to space.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mesosphere_coldest_layer_radiative_cooling"]
    }


def arch_14_meteor_ablation_frictional_heating_in_mesosphere(rng: random.Random) -> Dict[str, Any]:
    speed_kms = rng.choice([20, 30, 45, 60])
    prompt = (
        f"Incoming space meteoroids enter Earth's upper atmosphere at extreme orbital velocities of **{speed_kms} km/s** (tens of thousands of km/h).\n\n"
        "In which atmospheric layer do most meteors ('shooting stars') burn up, and what physical mechanism incinerates them?"
    )
    correct = "In the mesosphere (altitude 50 to 85 km); violent compression of air ahead of the hypersonic meteoroid (ram pressure) superheats the gas, transferring intense thermal energy that vaporizes and ablates the rock into a glowing streak of incandescent light."
    options = [
        correct,
        "In the troposphere, where rain clouds extinguish the burning rock.",
        "In the exosphere, where the vacuum of space freezes the meteor into ice cubes.",
        "In the core of the Earth, where molten iron dissolves the meteor upon entry."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric entry layer:\n"
        "Meteor ablation occurs primarily at 75–100 km (mesosphere).\n"
        "Step 2: Ram pressure heating:\n"
        "At hypersonic speeds (11–72 km/s), the meteoroid compresses air molecules faster than they can move out of the way. A shock wave develops in front of the body, heating air to thousands of degrees. Thermal radiation ablates (strips) rock material, producing the visible ionization trail."
    )
    return {
        "id": f"ns9_atm_14_{rng.randint(100000, 999999)}",
        "subskill": "14_meteor_ablation_frictional_heating_in_mesosphere",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "In which layer do meteors burn up due to ram pressure heating?",
            "tier_2": "The mesosphere (~50–85 km altitude).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["meteor_ablation_mesosphere_ram_pressure"]
    }


def arch_15_noctilucent_clouds_polar_mesospheric_ice_crystals(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During high-latitude summers, delicate electric-blue **noctilucent clouds** (night-shining clouds) are visible in the twilight sky long after sunset.\n\n"
        "At what extreme altitude do noctilucent clouds form, and what are they composed of?"
    )
    correct = "They form at ~80 to 85 km in the upper mesosphere (the highest clouds on Earth), composed of sub-micron water ice crystals nucleated around micrometeorite smoke dust at temperatures below -120 °C."
    options = [
        correct,
        "They form at 1 km in the troposphere, composed of chemical smoke from factory chimneys.",
        "They form on the surface of the Moon, reflecting light from street lamps.",
        "They form inside oceanic caves, composed of luminescent deep-sea jellyfish."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Polar Mesospheric Clouds (PMCs):\n"
        "Observed at ~83 km near the mesopause.\n"
        "Step 2: Illumination geometry:\n"
        "Because of their extreme altitude, they remain illuminated by sunlight from beneath the observer's horizon while the ground below is in darkness, shining with a distinctive electric blue hue due to methane-derived water vapor and meteoric smoke nuclei."
    )
    return {
        "id": f"ns9_atm_15_{rng.randint(100000, 999999)}",
        "subskill": "15_noctilucent_clouds_polar_mesospheric_ice_crystals",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What are the highest clouds in Earth's atmosphere called and where do they form?",
            "tier_2": "Noctilucent clouds formed of ice crystals in the mesosphere (~80–85 km).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["noctilucent_clouds_mesosphere_ice"]
    }


def arch_16_thermosphere_extreme_high_temperatures_solar_xrays(rng: random.Random) -> Dict[str, Any]:
    kinetic_t = rng.choice([1500, 1800, 2000])
    prompt = (
        f"In the **thermosphere** (altitude ~85 to 600 km), molecular kinetic temperatures soar to an incredible **{kinetic_t} °C**.\n\n"
        "What causes these blazing kinetic temperatures, and why would an astronaut's bare hand still feel freezing cold in this layer?"
    )
    correct = "High temperatures result from direct absorption of high-energy solar X-rays and extreme UV by oxygen and nitrogen; however, air density is so near-vacuum that too few molecules would collide with an astronaut's skin to transfer sensible heat."
    options = [
        correct,
        "The thermosphere is heated by magma boiling on the Moon, but the air is colored blue.",
        "The heat is caused by friction from passing asteroids, but space suits cancel gravity.",
        "The thermosphere is an optical illusion that exists only in computer simulation models."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Photo-absorption mechanism:\n"
        "Solar extreme ultraviolet (EUV) and X-ray photons ionize and dissociate N2, O2, and O, imparting high kinetic velocities (T_kinetic > 1500 °C).\n"
        "Step 2: Temperature vs Heat:\n"
        "Temperature measures average kinetic energy per particle. Heat measures total thermal energy transferred. At thermospheric pressures (<10⁻⁴ Pa), the mean free path exceeds kilometers; heat transfer via molecular conduction is virtually zero."
    )
    return {
        "id": f"ns9_atm_16_{rng.randint(100000, 999999)}",
        "subskill": "16_thermosphere_extreme_high_temperatures_solar_xrays",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why is the thermosphere 1500 °C yet feels cold to the touch?",
            "tier_2": "Gas particles move fast from solar EUV, but air is too rarefied to transfer heat.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["thermosphere_kinetic_temperature_rarefaction"]
    }


def arch_17_ionosphere_plasma_layer_and_am_radio_skip(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Embedded within the thermosphere and upper mesosphere is the **ionosphere**, an electrically charged layer of ions and free electrons.\n\n"
        "How does the ionosphere enable long-distance **shortwave and AM radio transmission** beyond the horizon?"
    )
    correct = "Electrically charged plasma layers (D, E, F layers) refract and reflect high-frequency radio waves back down toward Earth's surface (skywave propagation / 'skip'), allowing radio signals to bypass the Earth's geometric curvature."
    options = [
        correct,
        "The ionosphere absorbs radio waves and converts them into visible lightning bolts.",
        "The ionosphere uses fiber optic glass cables floating in the sky to transmit signals.",
        "Radio waves bounce off underground iron mines rather than the upper atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Ionospheric plasma formation:\n"
        "Solar radiation ionizes atmospheric atoms: O + hν → O⁺ + e⁻.\n"
        "Step 2: Skywave propagation:\n"
        "Radio waves entering the ionized plasma induce oscillations in free electrons, refracting the electromagnetic wave path back downward toward Earth. At night, the absorbing D layer recombines, allowing AM/shortwave signals to reflect from higher F layers across thousands of kilometers."
    )
    return {
        "id": f"ns9_atm_17_{rng.randint(100000, 999999)}",
        "subskill": "17_ionosphere_plasma_layer_and_am_radio_skip",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "How does the charged ionosphere help radio signals travel around the Earth?",
            "tier_2": "Free electrons and ions reflect radio waves back to Earth (skywave propagation).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ionosphere_radio_skywave_propagation"]
    }


def arch_18_auroras_borealis_and_australis_geomagnetic_excitation(rng: random.Random) -> Dict[str, Any]:
    aurora_type = rng.choice(["Aurora Australis (Southern Lights)", "Aurora Borealis (Northern Lights)"])
    prompt = (
        f"The breathtaking polar light displays known as **{aurora_type}** illuminate the night sky in polar regions.\n\n"
        "What physical interaction in the upper atmosphere produces these shimmering curtains of green and crimson light?"
    )
    correct = "Energetic charged particles (electrons and protons) from the solar wind are channeled along geomagnetic field lines into the polar thermosphere, colliding with oxygen and nitrogen atoms and exciting them to emit characteristic spectral photons (e.g. green 557,7 nm from atomic oxygen)."
    options = [
        correct,
        "Sunlight reflecting off polar snowdrifts into low-altitude rain clouds.",
        "Underground diamond mines turning on massive floodlights to celebrate the new year.",
        "Radioactive fallout from passing satellites burning in the lower troposphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geomagnetic funneling:\n"
        "Earth's magnetosphere redirects solar wind plasma into auroral ovals around geomagnetic poles.\n"
        "Step 2: Quantum emission:\n"
        "Injected electrons collide with atmospheric particles: e⁻ + O → e⁻ + O*.\n"
        "De-excitation releases photons: Atomic oxygen emits green (557,7 nm, ~100–150 km) or deep red (630,0 nm, >200 km); molecular nitrogen emits blue/violet."
    )
    return {
        "id": f"ns9_atm_18_{rng.randint(100000, 999999)}",
        "subskill": "18_auroras_borealis_and_australis_geomagnetic_excitation",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What solar particles collide with atmospheric oxygen and nitrogen to create auroras?",
            "tier_2": "Solar wind charged particles channeled by magnetic field excite gas atoms.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["auroras_solar_wind_excitation"]
    }


def arch_19_international_space_station_thermospheric_orbit(rng: random.Random) -> Dict[str, Any]:
    altitude_km = rng.choice([400, 410, 420])
    prompt = (
        f"The **International Space Station (ISS)** orbits Earth at an altitude of approximately **{altitude_km} km**, situated within the lower thermosphere.\n\n"
        "Even though the thermosphere is near-vacuum, why must ground control periodically fire rocket thrusters to **re-boost** the ISS's orbital altitude?"
    )
    correct = "Sparse atmospheric gas molecules collide with the massive station, generating continuous aerodynamic drag that bleeds orbital kinetic energy, causing the station to lose altitude (orbital decay) by ~100 meters per day."
    options = [
        correct,
        "Earth's gravity gets 50% stronger every night, pulling the station downward.",
        "The ISS runs out of oxygen and must sink to the surface to breathe.",
        "The Sun pushes the station toward Mars, requiring thrusters to hold it back."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Thermospheric density at 400 km:\n"
        "Residual gas density is ~10⁻¹¹ kg/m³ (microscopic, but non-zero across a 100-meter football-field-sized station).\n"
        "Step 2: Orbital decay physics:\n"
        "At orbital speeds (~7,66 km/s), residual drag F_D = 0,5 ρ v² C_D A dissipates orbital mechanical energy, requiring periodic propulsive re-boost maneuvers (using Progress or Cygnus thrusters) to maintain circular orbit."
    )
    return {
        "id": f"ns9_atm_19_{rng.randint(100000, 999999)}",
        "subskill": "19_international_space_station_thermospheric_orbit",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What slows down the ISS in its 400 km orbit?",
            "tier_2": "Aerodynamic drag from rarefied gas molecules causes orbital decay.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["iss_orbital_decay_thermospheric_drag"]
    }


def arch_20_exosphere_transition_to_interplanetary_vacuum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The outermost fringe of Earth's atmosphere is the **exosphere**, extending from ~600 km up to 10 000 km.\n\n"
        "What physical condition defines the exosphere, and what happens to light gas atoms (such as hydrogen and helium) in this region?"
    )
    correct = "The mean free path between molecular collisions exceeds the scale height of the atmosphere; gas particles travel along ballistic curved trajectories under gravity, and particles exceeding escape velocity (11,2 km/s) escape permanently into interplanetary space (Jeans escape)."
    options = [
        correct,
        "The exosphere is a solid titanium shell built to prevent atmosphere from leaking out.",
        "The exosphere contains liquid water oceans where interplanetary fish swim.",
        "The exosphere is pressurized at 5 atmospheres and filled with pure chlorine gas."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Exobase definition:\n"
        "At the exobase (~500–600 km), Knudsen number Kn > 1. Molecules rarely collide with each other.\n"
        "Step 2: Atmospheric escape (Jeans escape):\n"
        "Light atoms (H, He) have Maxwell-Boltzmann thermal velocity tails exceeding escape velocity (v_esc = √(2GM/R) ≈ 11,2 km/s), slowly bleeding Earth's primordial hydrogen into space."
    )
    return {
        "id": f"ns9_atm_20_{rng.randint(100000, 999999)}",
        "subskill": "20_exosphere_transition_to_interplanetary_vacuum",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Do molecules collide frequently in the exosphere, and can light gases escape?",
            "tier_2": "Collisions are extremely rare; particles follow ballistic trajectories and escape.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["exosphere_ballistic_trajectories_escape"]
    }


def arch_21_incoming_solar_radiation_insolation_spectrum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Incoming solar energy reaching the top of Earth's atmosphere (**insolation**) averages approximately **1 361 W/m²** (the solar constant).\n\n"
        "What electromagnetic wavelengths constitute the bulk of this incoming solar radiation?"
    )
    correct = "Shortwave radiation: predominantly visible light (~43%), near-infrared radiation (~49%), and a small fraction of ultraviolet radiation (~8%)."
    options = [
        correct,
        "Longwave radio waves (90%) and gamma rays (10%) with zero visible light.",
        "Sound waves that vibrate through outer space to heat ocean water.",
        "Pure microwave radiation emitted by household microwave ovens."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Solar blackbody radiation (Planck's Law):\n"
        "The Sun radiates as an approximate blackbody at ~5778 K.\n"
        "Step 2: Wien's Displacement Law:\n"
        "Peak emission λ_max = 2898 / 5778 ≈ 0,5 µm (visible green light). The bulk of insolation arrives as shortwave visible and near-infrared radiation."
    )
    return {
        "id": f"ns9_atm_21_{rng.randint(100000, 999999)}",
        "subskill": "21_incoming_solar_radiation_insolation_spectrum",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What wavelengths make up the bulk of sunlight reaching Earth?",
            "tier_2": "Shortwave radiation: visible light, near-infrared, and some ultraviolet.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["solar_insolation_shortwave_spectrum"]
    }


def arch_22_planetary_albedo_reflection_by_clouds_ice_and_surface(rng: random.Random) -> Dict[str, Any]:
    surface_type = rng.choice([
        ("Fresh polar snow and sea ice", "very high albedo (~0,80 to 0,90), reflecting 80% to 90% of incoming sunlight back into space"),
        ("Open ocean water", "very low albedo (~0,06 to 0,10), absorbing over 90% of incoming solar energy as heat")
    ])
    surf_name, albedo_desc = surface_type
    prompt = (
        "Earth has an average global **planetary albedo** of approximately **0,30** (reflecting 30% of incoming solar radiation).\n\n"
        f"What albedo characteristic defines **{surf_name}**?"
    )
    correct = f"It has {albedo_desc}."
    options = [
        correct,
        "It absorbs 100% of moonlight and emits radioactive gamma rays.",
        "It reflects sound waves while absorbing all atmospheric nitrogen.",
        "It has an albedo of exactly 10,0, multiplying sunlight ten times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of albedo:\n"
        "Albedo (α) = Reflected Solar Flux / Incident Solar Flux (dimensionless ratio from 0 to 1).\n"
        f"Step 2: Contrast for {surf_name}:\n"
        f"{surf_name} has {albedo_desc}."
    )
    return {
        "id": f"ns9_atm_22_{rng.randint(100000, 999999)}",
        "subskill": "22_planetary_albedo_reflection_by_clouds_ice_and_surface",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Does {surf_name} reflect a lot of light (high albedo) or absorb most light (low albedo)?",
            "tier_2": f"It has {albedo_desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["planetary_albedo_surface_reflection"]
    }


def arch_23_terrestrial_radiation_outgoing_longwave_infrared(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth absorbs shortwave solar radiation from the Sun and re-emits this energy back toward space as **terrestrial radiation**.\n\n"
        "Why is Earth's outgoing terrestrial radiation emitted as **longwave infrared**, and how does this differ from incoming solar radiation?"
    )
    correct = "Because Earth's surface is much cooler (~288 K / 15 °C) than the Sun (~5778 K), Wien's displacement law dictates that Earth emits at much longer electromagnetic wavelengths, peaking in the thermal infrared band (~10 micrometers)."
    options = [
        correct,
        "Earth emits high-energy X-rays and gamma rays because the core is radioactive.",
        "Earth emits green laser beams that keep satellites in orbit.",
        "Earth absorbs and re-emits identical visible yellow sunlight with zero wavelength change."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Wien's Displacement Law: λ_max = b / T.\n"
        "• Sun (T ≈ 5800 K) emits shortwave peak at λ ≈ 0,5 µm (visible light).\n"
        "• Earth (T ≈ 288 K) emits longwave peak at λ ≈ 10 µm (thermal infrared).\n"
        "Step 2: Critical significance:\n"
        "Atmospheric greenhouse gases are transparent to shortwave solar light but opaque to longwave terrestrial infrared."
    )
    return {
        "id": f"ns9_atm_23_{rng.randint(100000, 999999)}",
        "subskill": "23_terrestrial_radiation_outgoing_longwave_infrared",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why does a cooler planet emit longwave infrared radiation instead of visible light?",
            "tier_2": "Because cooler objects emit at longer wavelengths (Wien's law: λ_max = b / T).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["terrestrial_radiation_longwave_infrared"]
    }


def arch_24_natural_greenhouse_effect_life_sustaining_equilibrium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **natural greenhouse effect** is often confused with human-induced global warming, but it is an essential planetary feature.\n\n"
        "What would Earth's average global surface temperature be without the natural greenhouse effect, and how does it sustain life?"
    )
    correct = "Without the natural greenhouse effect, Earth's average temperature would be a frozen -18 °C; greenhouse gases warm the surface by 33 °C to a comfortable +15 °C, allowing liquid water oceans to exist and life to thrive."
    options = [
        correct,
        "Without the greenhouse effect, Earth would boil at +200 °C, incinerating all organisms.",
        "Without the greenhouse effect, Earth's temperature would remain completely unchanged at +15 °C.",
        "Without the greenhouse effect, Earth would float out of the Solar System into outer space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Radiative equilibrium calculation without greenhouse gases:\n"
        "T_effective = [(S0 (1 - α)) / (4 σ)]^(1/4) ≈ 255 K (-18 °C).\n"
        "Step 2: Natural greenhouse blanket:\n"
        "Water vapor, CO2, and other greenhouse gases absorb outgoing infrared and re-radiate it in all directions (including downward), warming the surface to ~288 K (+15 °C)—a +33 °C difference essential for liquid water."
    )
    return {
        "id": f"ns9_atm_24_{rng.randint(100000, 999999)}",
        "subskill": "24_natural_greenhouse_effect_life_sustaining_equilibrium",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What would Earth's temperature be without greenhouse gases (-18 °C or +15 °C)?",
            "tier_2": "It would be -18 °C instead of the comfortable +15 °C we enjoy today.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["natural_greenhouse_effect_33c_warming"]
    }


def arch_25_greenhouse_gases_infrared_absorption_molecular_vibrations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Why are triatomic molecules like **carbon dioxide (CO2)** and **water vapor (H2O)** greenhouse gases, while homonuclear diatomic gases like **nitrogen (N2)** and **oxygen (O2)** are NOT greenhouse gases?"
    )
    correct = "Polyatomic molecules (CO2, H2O) have flexible bonds that bend and stretch upon absorbing infrared photons, creating oscillating dipole moments that absorb and re-emit infrared radiation; symmetric diatomic molecules (N2, O2) have no changing dipole moment and cannot absorb infrared light."
    options = [
        correct,
        "CO2 and H2O are magnetic metals that attract heat like magnets, while N2 and O2 repel magnets.",
        "N2 and O2 are completely transparent to all radiation because they do not have any atoms.",
        "CO2 and H2O are radioactive elements that generate heat through nuclear fission in the air."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Molecular quantum mechanics of infrared absorption:\n"
        "Photons in the infrared spectrum match the vibrational energy levels of molecular bonds.\n"
        "Step 2: Dipole moment selection rule:\n"
        "A molecule can only absorb an infrared photon if the vibrational motion produces a changing electric dipole moment. Symmetrical N2 (N≡N) and O2 (O=O) have zero net dipole during vibration. Bending and asymmetric stretching modes in CO2 and H2O create temporary dipole changes, allowing strong IR absorption."
    )
    return {
        "id": f"ns9_atm_25_{rng.randint(100000, 999999)}",
        "subskill": "25_greenhouse_gases_infrared_absorption_molecular_vibrations",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why do CO2 and H2O absorb infrared while N2 and O2 cannot?",
            "tier_2": "Vibrating CO2 and H2O have changing dipole moments; symmetric N2 and O2 do not.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["greenhouse_gas_dipole_vibration_mechanism"]
    }


BUILDERS_01_25 = {
    "01_atmospheric_composition_major_gases_percentages": arch_01_atmospheric_composition_major_gases_percentages,
    "02_atmospheric_pressure_gravitational_density_gradient": arch_02_atmospheric_pressure_gravitational_density_gradient,
    "03_high_altitude_hypoxia_and_mountain_climber_physiology": arch_03_high_altitude_hypoxia_and_mountain_climber_physiology,
    "04_five_thermal_layers_vertical_sequence": arch_04_five_thermal_layers_vertical_sequence,
    "05_troposphere_thickness_environmental_lapse_rate": arch_05_troposphere_thickness_environmental_lapse_rate,
    "06_troposphere_weather_engine_convection_and_clouds": arch_06_troposphere_weather_engine_convection_and_clouds,
    "07_stratosphere_temperature_inversion_and_stability": arch_07_stratosphere_temperature_inversion_and_stability,
    "08_ozone_layer_formation_chapman_photochemical_cycle": arch_08_ozone_layer_formation_chapman_photochemical_cycle,
    "09_ozone_shielding_uv_b_and_uv_c_radiation_protection": arch_09_ozone_shielding_uv_b_and_uv_c_radiation_protection,
    "10_cfcs_chlorofluorocarbons_catalytic_ozone_depletion": arch_10_cfcs_chlorofluorocarbons_catalytic_ozone_depletion,
    "11_antarctic_ozone_hole_polar_stratospheric_clouds": arch_11_antarctic_ozone_hole_polar_stratospheric_clouds,
    "12_montreal_protocol_international_treaty_and_recovery": arch_12_montreal_protocol_international_treaty_and_recovery,
    "13_mesosphere_temperature_minimum_coldest_layer": arch_13_mesosphere_temperature_minimum_coldest_layer,
    "14_meteor_ablation_frictional_heating_in_mesosphere": arch_14_meteor_ablation_frictional_heating_in_mesosphere,
    "15_noctilucent_clouds_polar_mesospheric_ice_crystals": arch_15_noctilucent_clouds_polar_mesospheric_ice_crystals,
    "16_thermosphere_extreme_high_temperatures_solar_xrays": arch_16_thermosphere_extreme_high_temperatures_solar_xrays,
    "17_ionosphere_plasma_layer_and_am_radio_skip": arch_17_ionosphere_plasma_layer_and_am_radio_skip,
    "18_auroras_borealis_and_australis_geomagnetic_excitation": arch_18_auroras_borealis_and_australis_geomagnetic_excitation,
    "19_international_space_station_thermospheric_orbit": arch_19_international_space_station_thermospheric_orbit,
    "20_exosphere_transition_to_interplanetary_vacuum": arch_20_exosphere_transition_to_interplanetary_vacuum,
    "21_incoming_solar_radiation_insolation_spectrum": arch_21_incoming_solar_radiation_insolation_spectrum,
    "22_planetary_albedo_reflection_by_clouds_ice_and_surface": arch_22_planetary_albedo_reflection_by_clouds_ice_and_surface,
    "23_terrestrial_radiation_outgoing_longwave_infrared": arch_23_terrestrial_radiation_outgoing_longwave_infrared,
    "24_natural_greenhouse_effect_life_sustaining_equilibrium": arch_24_natural_greenhouse_effect_life_sustaining_equilibrium,
    "25_greenhouse_gases_infrared_absorption_molecular_vibrations": arch_25_greenhouse_gases_infrared_absorption_molecular_vibrations,
}
