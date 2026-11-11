"""Grade 7 Natural Sciences - Relationship of the Sun to the Earth: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md
Focus: Polar night/midnight sun, opposite hemispheres, photosynthesis, water cycle, wind, ocean currents,
radiation spectrum, atmosphere insulation, ozone, magnetic field, auroras, sundials, solar power, diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_polar_day_and_night_midnight_sun(rng: random.Random) -> Dict[str, Any]:
    pole_zones = [
        ("the Arctic Circle (66.5° N) in June", "the Sun never sets below the horizon for 24 continuous hours ('Midnight Sun')"),
        ("the Antarctic Circle (66.5° S) in June", "the Sun never rises above the horizon, resulting in 24 hours of polar night"),
        ("the Antarctic Circle (66.5° S) in December", "the Sun remains above the horizon for 24 hours a day during polar summer")
    ]
    zone, effect = rng.choice(pole_zones)
    prompt = (
        f"At {zone}, {effect}.\n\n"
        "What causes these extreme 24-hour day and 24-hour night phenomena in the polar circles?"
    )
    correct = "Earth's 23.5° axial tilt keeps polar regions pointed entirely into or out of sunlight as the planet rotates."
    options = [
        correct,
        "Earth stops rotating completely whenever it enters the Arctic and Antarctic regions.",
        "The Sun moves into a polar orbit around the North Pole every summer.",
        "Ice reflects all cosmic rays, creating artificial perpetual daylight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand polar circle geometry:\n"
        "Because of Earth's 23.5° tilt, latitudes beyond 66.5° (90° - 23.5°) fall entirely inside or outside the daylight circle (terminator) during solstices.\n"
        "Step 2: Effect: Continuous daylight (Midnight Sun) or continuous darkness (Polar Night)."
    )
    return {
        "id": f"ns7_sun_26_{rng.randint(100000, 999999)}",
        "subskill": "26_polar_day_and_night_midnight_sun",
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
            "tier_1": "Think about how Earth's tilt affects regions near the poles.",
            "tier_2": "The 23.5 degree tilt keeps the polar circle in continuous light or darkness.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["midnight_sun_rotation_halt_fallacy"]
    }


def arch_27_opposite_seasons_northern_vs_southern_hemisphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When families in South Africa are celebrating Christmas in hot summer sunshine during December, "
        "families in Canada or the UK are experiencing freezing winter snowstorms.\n\n"
        "Why do the Northern and Southern Hemispheres always experience opposite seasons simultaneously?"
    )
    correct = "Because Earth's axis is tilted in a fixed direction, when one hemisphere tilts towards the Sun, the opposite hemisphere is naturally tilted away."
    options = [
        correct,
        "The Sun only emits heat towards the southern half of space in December.",
        "The equator has a solid thermal wall that reflects cold air north and hot air south.",
        "The Northern Hemisphere is ten times farther away from the Sun than the Southern Hemisphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall axial tilt orientation:\n"
        "Earth is divided into two hemispheres by the equator.\n"
        "Step 2: Opposite tilt exposure:\n"
        "When the South Pole tilts towards the Sun (December), the North Pole points away. Hence, summer in the south always coincides with winter in the north."
    )
    r_earth = rng.choice([38, 40, 42])
    col_sun = rng.choice(["#f59e0b", "#fbbf24", "#d97706"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" width="100%" height="140"><circle cx="50" cy="80" r="30" fill="{col_sun}"/><text x="50" y="85" text-anchor="middle" fill="#ffffff" font-size="11">Sun</text><circle cx="230" cy="80" r="{r_earth}" fill="#3b82f6"/><line x1="210" y1="30" x2="250" y2="130" stroke="#ef4444" stroke-width="2"/><text x="260" y="55" fill="#f87171" font-size="10">North (Tilted Away)</text><text x="260" y="115" fill="#38bdf8" font-size="10">South (Tilted Toward)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_sun_27_{rng.randint(100000, 999999)}",
        "subskill": "27_opposite_seasons_northern_vs_southern_hemisphere",
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
        "diagram_spec": spec,
        "hints": {
            "tier_1": "When one end of a pencil tilts forward, what happens to the other end?",
            "tier_2": "Tilting toward the Sun means the opposite side tilts away.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["hemispheric_season_inversion_error"]
    }


def arch_28_seasonal_lag_thermal_inertia_oceans(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The summer solstice (longest daylight) occurs around 21 December in South Africa. "
        "However, the hottest summer temperatures typically occur a month or two later in January or February.\n\n"
        "What physical property of Earth's oceans and land masses causes this **seasonal lag**?"
    )
    correct = "Thermal inertia: Oceans have a high heat capacity and take several weeks to absorb and warm up to maximum temperature."
    options = [
        correct,
        "Earth's orbital speed doubles in January, creating sudden friction with space dust.",
        "The Sun moves closer to Earth during February than in December.",
        "Volcanoes erupt worldwide on 1 January, adding artificial heat."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand heat capacity:\n"
        "Water has a very high specific heat capacity, meaning it absorbs vast amounts of heat before its temperature rises.\n"
        "Step 2: Thermal lag:\n"
        "Even after peak solar radiation (solstice), heat continues to accumulate faster than it is radiated away, peaking in January/February."
    )
    return {
        "id": f"ns7_sun_28_{rng.randint(100000, 999999)}",
        "subskill": "28_seasonal_lag_thermal_inertia_oceans",
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
            "tier_1": "Think about boiling a large pot of water: does it heat up instantly?",
            "tier_2": "Oceans take time to warm up (thermal inertia).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["seasonal_lag_concept_confusion"]
    }


def arch_29_solar_energy_sustaining_photosynthesis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Green plants, algae, and cyanobacteria form the foundation of almost all ecological food chains on Earth.\n\n"
        "What biochemical process converts radiant solar energy into chemical energy stored in food molecules?"
    )
    correct = "Photosynthesis: Chlorophyll absorbs sunlight to synthesize glucose and oxygen from carbon dioxide and water."
    options = [
        correct,
        "Cellular respiration: Cells burn sugar to produce heat and carbon dioxide.",
        "Transpiration: Water evaporates through stomata into the air.",
        "Fermentation: Microorganisms digest sugars without using oxygen."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify energy conversion:\n"
        "Radiant light energy -> Stored chemical potential energy.\n"
        "Step 2: Formula and process:\n"
        "6CO₂ + 6H₂O + Sunlight -> C₆H₁₂O₆ (glucose) + 6O₂ (photosynthesis)."
    )
    return {
        "id": f"ns7_sun_29_{rng.randint(100000, 999999)}",
        "subskill": "29_solar_energy_sustaining_photosynthesis",
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
            "tier_1": "What process uses chlorophyll and sunlight to make plant food?",
            "tier_2": "Photosynthesis produces glucose and oxygen.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["photosynthesis_energy_conversion_error"]
    }


def arch_30_solar_energy_driving_the_water_cycle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The water cycle continuously redistributes fresh water across continents through evaporation, condensation, and precipitation.\n\n"
        "What is the primary driving energy source that powers this global hydrologic cycle?"
    )
    correct = "Solar heat energy, which warms ocean and land water, causing it to evaporate into water vapour."
    options = [
        correct,
        "Geothermal energy from deep underground oil drills.",
        "Nuclear energy emitted by radioactive decay of granite rocks.",
        "Frictional energy generated by ships sailing across the Atlantic."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify the main engine of the water cycle:\n"
        "Evaporation requires thermal energy to break hydrogen bonds in liquid water.\n"
        "Step 2: Source of energy:\n"
        "The Sun provides thermal radiant energy that evaporates surface water, powering cloud formation and precipitation."
    )
    return {
        "id": f"ns7_sun_30_{rng.randint(100000, 999999)}",
        "subskill": "30_solar_energy_driving_the_water_cycle",
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
            "tier_1": "What heats the water in puddles, dams, and oceans so it evaporates?",
            "tier_2": "The Sun's heat energy drives evaporation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_cycle_driving_force_confusion"]
    }


def arch_31_solar_heating_driving_global_winds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Wind is the horizontal movement of air across Earth's surface. How does the Sun cause wind to blow?"
    )
    correct = "Unequal solar heating creates temperature differences; warm air expands and rises (low pressure), and cooler dense air rushes in to replace it."
    options = [
        correct,
        "The Sun's gravity pushes air clouds around Earth like a giant vacuum cleaner.",
        "Trees waving their branches in the wind generate all atmospheric air currents.",
        "The rotation of the Moon creates giant air waves that crash against mountains."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mechanism of wind:\n"
        "1. Sun heats equatorial regions more than poles.\n"
        "2. Warm air becomes less dense and rises (low pressure).\n"
        "3. Cool, high-pressure air moves toward low-pressure areas, creating wind."
    )
    return {
        "id": f"ns7_sun_31_{rng.randint(100000, 999999)}",
        "subskill": "31_solar_heating_driving_global_winds",
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
            "tier_1": "Warm air rises; cool air rushes in.",
            "tier_2": "Unequal heating causes pressure differences, driving wind.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["wind_origin_misconception"]
    }


def arch_32_solar_energy_ocean_currents_convection(rng: random.Random) -> Dict[str, Any]:
    currents = [
        ("the warm Agulhas Current", "carrying warm tropical water southwards along South Africa's east coast"),
        ("the cold Benguela Current", "carrying cold sub-Antarctic water northwards along South Africa's west coast")
    ]
    c_name, c_desc = rng.choice(currents)
    prompt = (
        f"Off South Africa's coastline, {c_name} flows, {c_desc}.\n\n"
        "How does solar heating contribute to the massive convection currents circulating in the world's oceans?"
    )
    correct = "Solar radiation intensely warms equatorial surface water, creating density and temperature differences that drive deep and surface convection loops."
    options = [
        correct,
        "The Sun boils seawater at the equator, turning it into hot steam bubbles that push the water.",
        "The Sun's magnetic field pulls salt ions directly through ocean trenches.",
        "Ocean currents are caused solely by schools of migrating tuna swimming together."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Convection in oceans:\n"
        "Water at the equator absorbs intense solar heat, expands, and becomes less dense.\n"
        "Step 2: Circulation:\n"
        "Warm equatorial water flows toward the poles, while cold dense polar water sinks and flows toward the equator, creating thermohaline conveyor currents."
    )
    return {
        "id": f"ns7_sun_32_{rng.randint(100000, 999999)}",
        "subskill": "32_solar_energy_ocean_currents_convection",
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
            "tier_1": "Warm water rises and moves; cold water sinks.",
            "tier_2": "Solar heating at the equator drives ocean convection.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ocean_current_density_convection_error"]
    }


def arch_33_solar_radiation_spectrum_visible_uv_infrared(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Sun emits a broad electromagnetic spectrum. What are the three primary types of solar radiation reaching Earth's upper atmosphere?"
    )
    correct = "Visible light (illuminates our world), Infrared radiation (felt as heat), and Ultraviolet (UV) radiation (invisible, can cause sunburn)."
    options = [
        correct,
        "Alpha particles, Beta particles, and Gamma rays exclusively.",
        "Radio waves, Microwaves, and Sound waves exclusively.",
        "Liquid nitrogen, Oxygen gas, and Carbon dioxide rays."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Break down the solar spectrum:\n"
        "- Visible light (~44%): Light visible to the human eye.\n"
        "- Infrared (~48%): Thermal radiation felt as heat.\n"
        "- Ultraviolet (~7%): Higher energy waves that can trigger vitamin D synthesis or sunburns."
    )
    return {
        "id": f"ns7_sun_33_{rng.randint(100000, 999999)}",
        "subskill": "33_solar_radiation_spectrum_visible_uv_infrared",
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
            "tier_1": "Think about what light we see, what we feel as heat, and what burns skin.",
            "tier_2": "Visible light, infrared (heat), and ultraviolet (UV).",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["electromagnetic_spectrum_components_error"]
    }


def arch_34_earths_atmosphere_insulation_greenhouse_effect(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Without its natural atmosphere, Earth's average surface temperature would be a frozen -18 °C instead of the comfortable +15 °C we enjoy today.\n\n"
        "How does the natural **greenhouse effect** in Earth's atmosphere maintain this habitable temperature?"
    )
    correct = "Greenhouse gases (water vapour, CO₂, methane) absorb re-radiated infrared heat from the surface and trap it, slowing heat loss into space."
    options = [
        correct,
        "The atmosphere creates a solid glass roof over the continents that reflects all rain back.",
        "Oxygen molecules burn constantly in the upper sky to keep the air warm.",
        "The atmosphere absorbs nuclear radiation and releases hot steam into the clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Incoming vs outgoing radiation:\n"
        "Solar shortwave radiation passes through the atmosphere and warms the ground.\n"
        "Step 2: Trapping longwave heat:\n"
        "The ground radiates longwave infrared heat upward. Greenhouse gases absorb and re-emit this heat, keeping the planet warm like a blanket."
    )
    return {
        "id": f"ns7_sun_34_{rng.randint(100000, 999999)}",
        "subskill": "34_earths_atmosphere_insulation_greenhouse_effect",
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
            "tier_1": "What acts like a blanket to keep Earth warm at night?",
            "tier_2": "Greenhouse gases trap outgoing infrared heat.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["greenhouse_effect_pure_evil_fallacy"]
    }


def arch_35_ozone_layer_uv_protection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The ozone layer (O₃) is concentrated in the stratosphere between 15 km and 35 km above Earth's surface.\n\n"
        "What critical role does the ozone layer play in protecting life on Earth from the Sun?"
    )
    correct = "It absorbs the majority of dangerous ultraviolet (UV-B and UV-C) radiation, preventing skin cancer and DNA damage in living organisms."
    options = [
        correct,
        "It traps nitrogen gas so that humans do not float into space.",
        "It blocks 100% of visible light so that night can exist.",
        "It generates rainwater during thunderstorms."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify ozone function:\n"
        "Ozone molecules (O₃) absorb high-energy ultraviolet radiation from the Sun.\n"
        "Step 2: Biological protection:\n"
        "By filtering out harmful UV rays, the ozone layer protects terrestrial life from mutations, cataracts, and skin cancer."
    )
    return {
        "id": f"ns7_sun_35_{rng.randint(100000, 999999)}",
        "subskill": "35_ozone_layer_uv_protection",
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
            "tier_1": "Which type of solar ray causes sunburn and skin damage?",
            "tier_2": "Ozone filters harmful ultraviolet (UV) radiation.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["ozone_depletion_vs_global_warming_confusion"]
    }


def arch_36_earths_magnetic_field_solar_wind_deflection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Sun constantly blows a stream of high-energy charged particles (electrons and protons) known as the **solar wind** across space.\n\n"
        "What protects Earth's atmosphere from being stripped away by this harmful solar wind?"
    )
    correct = "Earth's magnetosphere (magnetic field), generated by molten iron convection in its outer core, deflects charged solar particles around the planet."
    options = [
        correct,
        "A thick wall of ocean fog that freezes incoming particles into raindrops.",
        "Earth's gravitational force, which repels all electrons into deep space.",
        "The Moon, which absorbs 100% of the solar wind on its far side."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify planetary shield:\n"
        "Earth's rotating molten iron outer core generates a geomagnetic dipole field.\n"
        "Step 2: Deflection mechanism:\n"
        "The magnetosphere acts as a protective magnetic bubble, forcing charged solar wind particles to flow harmlessly around Earth."
    )
    return {
        "id": f"ns7_sun_36_{rng.randint(100000, 999999)}",
        "subskill": "36_earths_magnetic_field_solar_wind_deflection",
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
            "tier_1": "What invisible field deflects charged particles like electrons?",
            "tier_2": "Earth's magnetic field (magnetosphere).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magnetic_field_shielding_error"]
    }


def arch_37_aurora_australis_southern_lights_phenomenon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Near Earth's magnetic poles, observers sometimes see glowing curtains of green and violet light in the night sky "
        "(Aurora Borealis in the north, and Aurora Australis in the south).\n\n"
        "What causes these stunning auroral light displays?"
    )
    correct = "Charged particles from the solar wind are channeled by Earth's magnetic field into polar regions, colliding with oxygen and nitrogen atoms in the upper atmosphere."
    options = [
        correct,
        "Sunlight reflecting off massive icebergs in Antarctica like a giant mirror.",
        "Spontaneous chemical combustion of toxic polar pollutants in the air.",
        "Electric flashes from high-voltage undersea telegraph cables."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand particle excitation:\n"
        "Solar wind particles funnel along magnetic field lines into the upper polar atmosphere.\n"
        "Step 2: Light emission:\n"
        "They excite atmospheric gas atoms (oxygen emits green/red; nitrogen emits blue/purple), producing auroras."
    )
    return {
        "id": f"ns7_sun_37_{rng.randint(100000, 999999)}",
        "subskill": "37_aurora_australis_southern_lights_phenomenon",
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
            "tier_1": "What happens when solar particles collide with atmospheric gas near the magnetic poles?",
            "tier_2": "Collisions excite atmospheric atoms to emit glowing auroral light.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["aurora_light_origin_fallacy"]
    }


def arch_38_solar_flares_and_space_weather_impact(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Occasionally, the Sun releases intense bursts of electromagnetic radiation and coronal mass ejections (solar flares).\n\n"
        "What technological disruptions can major solar storms cause on Earth?"
    )
    correct = "They induce geomagnetically induced currents that can trip electrical power grids, disrupt satellite navigation (GPS), and interfere with radio communication."
    options = [
        correct,
        "They cause smartphone screens to physically shatter into glass fragments.",
        "They reverse the gravitational attraction of Earth, causing cars to float.",
        "They turn drinking water into diesel fuel inside underground pipes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand space weather:\n"
        "Solar flares and coronal mass ejections bombard Earth's magnetosphere with electromagnetic disturbances.\n"
        "Step 2: Societal impact:\n"
        "These disturbances induce erratic electrical currents in power grids, degrade high-frequency radio waves, and damage satellite electronics."
    )
    return {
        "id": f"ns7_sun_38_{rng.randint(100000, 999999)}",
        "subskill": "38_solar_flares_and_space_weather_impact",
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
            "tier_1": "Think about electrical grids, satellites, and radio signals.",
            "tier_2": "Solar flares disrupt modern communication and power systems.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["space_weather_impact_error"]
    }


def arch_39_sundials_and_gnomon_timekeeping(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Before modern mechanical and quartz clocks were invented, ancient civilizations used **sundials** with a central pointer (gnomon) to tell time.\n\n"
        "On what fundamental astronomical principle does a sundial operate?"
    )
    correct = "As Earth rotates, the Sun's changing position in the sky causes the gnomon's shadow to rotate across a calibrated dial plate."
    options = [
        correct,
        "The Sun sends Morse code optical signals directly into the gnomon pointer.",
        "Heat from the Sun causes the dial's stone base to shrink and expand once per minute.",
        "Sundials measure the Moon's gravitational pull on a lead pendulum."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify sundial mechanism:\n"
        "A sundial uses a vertical or tilted pointer called a gnomon.\n"
        "Step 2: Connecting to Earth's motion:\n"
        "Because Earth rotates at a steady rate of 15° per hour, the shadow cast by the gnomon tracks consistently across the hour markings."
    )
    return {
        "id": f"ns7_sun_39_{rng.randint(100000, 999999)}",
        "subskill": "39_sundials_and_gnomon_timekeeping",
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
            "tier_1": "What moves across the face of a sundial during the day?",
            "tier_2": "The shadow cast by the gnomon moves as Earth rotates.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["sundial_operation_misconception"]
    }


def arch_40_seasonal_agricultural_cycles_south_africa(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("maize farming in the Free State", "planting seeds in spring/early summer (October/November) to utilize summer rain and sunshine"),
        ("wheat farming in the Western Cape", "planting in late autumn (April/May) to take advantage of winter rainfall and harvesting in summer"),
        ("deciduous fruit orchards in the Ceres valley", "pruning trees in winter dormancy and harvesting sweet fruit in late summer")
    ]
    crop, cycle = rng.choice(crops)
    prompt = (
        f"In South African agriculture, {crop} relies heavily on {cycle}.\n\n"
        "Why is agricultural food production fundamentally tied to the Sun-Earth relationship?"
    )
    correct = "Seasonal changes in sunlight duration, temperature, and solar-driven rainfall dictate plant germination, growth, and harvest cycles."
    options = [
        correct,
        "Farming is independent of the Sun because all plants prefer growing in pitch dark caves.",
        "Tractors can only drive when the Sun is at an exact 45° angle in the sky.",
        "Seeds only germinate when the Moon passes in front of Mars."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Connect astronomy to biology and agriculture:\n"
        "Crop species evolved to respond to seasonal photoperiods (day length) and thermal cycles driven by Earth's tilt and orbit.\n"
        "Step 2: Practical farming:\n"
        "Farmers must align sowing and harvesting with seasonal rainfall and frost-free periods."
    )
    return {
        "id": f"ns7_sun_40_{rng.randint(100000, 999999)}",
        "subskill": "40_seasonal_agricultural_cycles_south_africa",
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
            "tier_1": "How do crops rely on sunlight, temperature, and rain across seasons?",
            "tier_2": "Seasonal day length and temperatures govern planting and harvest.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["agricultural_seasonality_confusion"]
    }


def arch_41_solar_power_photovoltaic_renewable_energy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Solar photovoltaic (PV) panels installed across solar farms in the Northern Cape generate clean electrical power.\n\n"
        "What direct energy conversion occurs inside a solar photovoltaic cell?"
    )
    correct = "Light energy (photons from sunlight) is converted directly into electrical energy via the photoelectric effect in semiconductor silicon."
    options = [
        correct,
        "Sound energy from sunlight is converted into mechanical kinetic energy.",
        "Chemical energy from battery acid is converted into visible laser beams.",
        "Nuclear energy from radioactive panels is converted into diesel fuel."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify energy input and output:\n"
        "Input: Radiant light energy from the Sun.\n"
        "Output: Direct current (DC) electrical energy.\n"
        "Step 2: Physics principle: The photovoltaic effect in silicon semiconductor cells."
    )
    return {
        "id": f"ns7_sun_41_{rng.randint(100000, 999999)}",
        "subskill": "41_solar_power_photovoltaic_renewable_energy",
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
            "tier_1": "What goes in (light) and what comes out (electricity)?",
            "tier_2": "Light energy to electrical energy.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["solar_pv_energy_conversion_error"]
    }


def arch_42_solar_thermal_water_heating_principles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A solar water geyser on a residential roof in Polokwane features a black absorber plate and glass cover.\n\n"
        "Why is the solar thermal collector plate painted matte black?"
    )
    correct = "Black surfaces are excellent absorbers of radiant solar heat, while light or shiny surfaces reflect heat away."
    options = [
        correct,
        "Black paint is a magical superconductor that creates electrical sparks.",
        "Black paint keeps birds from perching on the roof.",
        "Black paint makes water inside the pipes turn into sweet drinking juice."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Color absorption physics:\n"
        "Dark, matte black surfaces absorb almost all incident visible and infrared radiation.\n"
        "Step 2: Water heating application:\n"
        "The absorbed heat conducts efficiently into copper pipes, warming water for domestic use."
    )
    return {
        "id": f"ns7_sun_42_{rng.randint(100000, 999999)}",
        "subskill": "42_solar_thermal_water_heating_principles",
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
            "tier_1": "Which absorbs more heat in the Sun: a black T-shirt or a white T-shirt?",
            "tier_2": "Black surfaces absorb heat best.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["black_body_heat_absorption_misconception"]
    }


def arch_43_passive_solar_building_design_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In South Africa (Southern Hemisphere), sustainable architects design houses with large windows facing **north**.\n\n"
        "Why do north-facing windows provide optimal passive solar heating and lighting in South Africa?"
    )
    correct = "In the Southern Hemisphere, the midday Sun is always situated in the northern sky, providing abundant natural winter warmth and year-round daylight."
    options = [
        correct,
        "North-facing windows protect houses from solar radiation because the Sun rises in the south.",
        "Cold Antarctic blizzards always blow exclusively through south-facing windows.",
        "North-facing glass generates free electricity automatically without any wires."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Determine Sun's path in Southern Hemisphere:\n"
        "South of the Tropic of Capricorn (e.g. all of South Africa), the Sun arcs through the northern half of the sky.\n"
        "Step 2: Passive solar benefit:\n"
        "North-facing windows capture low winter northern Sun rays for natural heating, reducing electricity consumption."
    )
    return {
        "id": f"ns7_sun_43_{rng.randint(100000, 999999)}",
        "subskill": "43_passive_solar_building_design_insulation",
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
            "tier_1": "Which direction do you look at noon to see the Sun in South Africa?",
            "tier_2": "Look north; hence north-facing windows capture maximum sunlight.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["passive_solar_orientation_error"]
    }


def arch_44_albedo_effect_surface_reflectivity_ice_land(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Fresh polar snow and sea ice reflect up to 85% of incoming sunlight back into space, "
        "while dark ocean water absorbs over 90% of sunlight.\n\n"
        "What is the term for a surface's ability to reflect solar radiation, and what happens when sea ice melts?"
    )
    correct = "Albedo; melting ice exposes dark ocean water, which absorbs more solar heat and accelerates planetary warming."
    options = [
        correct,
        "Salinity; melting ice causes oceans to turn into solid salt crystals.",
        "Viscosity; melting ice makes ocean water as thick as motor oil.",
        "Turbidity; melting ice causes the Sun to extinguish its nuclear fuel."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define albedo:\n"
        "Albedo is the fraction of solar radiation reflected by a surface.\n"
        "Step 2: Ice-albedo positive feedback:\n"
        "High albedo (ice) reflects heat. When ice melts to expose dark ocean (low albedo), more heat is absorbed, accelerating warming."
    )
    return {
        "id": f"ns7_sun_44_{rng.randint(100000, 999999)}",
        "subskill": "44_albedo_effect_surface_reflectivity_ice_land",
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
            "tier_1": "What is surface reflectivity called?",
            "tier_2": "Albedo describes how much light a surface reflects.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["albedo_feedback_misconception"]
    }


def arch_45_diffuse_vs_direct_solar_radiation_cloud_cover(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On an overcast day in KwaZulu-Natal, thick clouds cover the sky so the Sun is not directly visible. "
        "Yet outdoors, there is still plenty of daylight to read a book.\n\n"
        "What type of solar radiation illuminates the ground on a cloudy day?"
    )
    correct = "Diffuse solar radiation: Sunlight scattered in all directions by water droplets and aerosols in the cloud layer."
    options = [
        correct,
        "Bioluminescent radiation generated by cloud-dwelling bacteria.",
        "Thermal radiation emitted by underground molten magma.",
        "Fluorescent lighting beamed down from commercial satellites."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Distinguish direct vs diffuse radiation:\n"
        "- Direct radiation travels in a straight beam from the Sun without scattering.\n"
        "- Diffuse radiation is scattered in all directions by clouds and atmospheric particles.\n"
        "Step 2: Conclusion: Clouds scatter sunlight into diffuse ambient daylight."
    )
    return {
        "id": f"ns7_sun_45_{rng.randint(100000, 999999)}",
        "subskill": "45_diffuse_vs_direct_solar_radiation_cloud_cover",
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
            "tier_1": "Is scattered light direct or diffuse?",
            "tier_2": "Diffuse radiation is scattered light.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["diffuse_radiation_concept_error"]
    }


def arch_46_equatorial_vs_polar_climate_solar_distribution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Regions near Earth's Equator (like the Congo basin) are warm and tropical year-round, "
        "while regions near the Poles (like Antarctica) remain permanently frozen in ice.\n\n"
        "What is the fundamental astronomical reason for this global climate difference?"
    )
    correct = "Because Earth is curved, equatorial regions receive steep, direct solar rays year-round, while polar regions receive shallow, oblique rays spread over large areas."
    options = [
        correct,
        "The Equator is five million kilometres closer to the Sun than the South Pole.",
        "The Sun only circles the Equator and never shines on polar latitudes.",
        "Antarctica has no atmosphere, while the Equator has a double atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Earth's spherical geometry:\n"
        "Incoming parallel solar rays strike the curved surface of Earth.\n"
        "Step 2: Solar intensity distribution:\n"
        "At the equator, rays strike at nearly 90° (maximum energy concentration). Near the poles, rays strike at grazing angles, spreading energy thinly over large areas."
    )
    return {
        "id": f"ns7_sun_46_{rng.randint(100000, 999999)}",
        "subskill": "46_equatorial_vs_polar_climate_solar_distribution",
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
            "tier_1": "How does Earth's curved spherical shape affect incoming light?",
            "tier_2": "Curvature makes equatorial rays direct and polar rays shallow.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["equator_polar_climate_cause_fallacy"]
    }


def arch_47_zenith_angle_and_atmospheric_path_length(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When the Sun is low near the horizon at sunrise or sunset, sunlight feels much gentler and looks golden or reddish, "
        "compared to the harsh burning white light of solar noon.\n\n"
        "How does the **atmospheric path length** explain this difference?"
    )
    correct = "Low-angle sunlight travels through a much thicker layer of atmosphere, which scatters and absorbs more solar energy before reaching the ground."
    options = [
        correct,
        "The Sun burns cooler fuel at sunrise and hotter fuel at midday.",
        "Earth's atmosphere physically shrinks to zero thickness at solar noon.",
        "Clouds automatically disappear every day at exactly 12:00."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geometric path length:\n"
        "At solar noon (overhead), rays pass through minimum atmospheric thickness (1 air mass).\n"
        "Step 2: Low horizon angle:\n"
        "At sunrise/sunset, rays travel obliquely through up to 10-30 times more atmosphere, causing heavy scattering and attenuation of energy."
    )
    return {
        "id": f"ns7_sun_47_{rng.randint(100000, 999999)}",
        "subskill": "47_zenith_angle_and_atmospheric_path_length",
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
            "tier_1": "Does light pass through more air when it enters at an angle?",
            "tier_2": "Thicker air path scatters and absorbs more energy.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["atmospheric_path_length_error"]
    }


def arch_48_seasonal_animal_behaviour_hibernation_migration(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("the Barn Swallow", "migrating thousands of kilometres from Europe to spend summer in sunny South Africa"),
        ("African bats and small rodents in the Drakensberg", "entering torpor or winter dormancy to conserve metabolic energy"),
        ("wildebeest and zebras in East/Southern Africa", "migrating across savannahs following seasonal solar-driven rains")
    ]
    beast, action = rng.choice(animals)
    prompt = (
        f"In wildlife biology, {beast} responds to seasonal solar variations by {action}.\n\n"
        "What astronomical environmental cues trigger these seasonal animal survival behaviours?"
    )
    correct = "Changing photoperiod (daylight hours) and ambient temperatures caused by Earth's axial tilt and revolution."
    options = [
        correct,
        "Radio signals broadcast from cellular telecommunication towers.",
        "Sudden fluctuations in Earth's gravitational acceleration at high tide.",
        "Changes in the chemical salt content of fresh drinking rivers."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Environmental cues:\n"
        "Animals perceive changing day length (photoperiod) through photoreceptors and hormonal triggers.\n"
        "Step 2: Biological adaptation:\n"
        "Shortening days and cooling temperatures signal approaching winter, triggering migration, food caching, or hibernation."
    )
    return {
        "id": f"ns7_sun_48_{rng.randint(100000, 999999)}",
        "subskill": "48_seasonal_animal_behaviour_hibernation_migration",
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
            "tier_1": "How do animals sense winter is coming?",
            "tier_2": "Shortening daylight hours and cooler temperatures.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["animal_seasonal_cues_confusion"]
    }


def arch_49_seasonal_plant_adaptations_deciduous_dormancy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During autumn in South Africa (April/May), deciduous trees change leaf colors to yellow, orange, and red, "
        "and subsequently shed their leaves before winter.\n\n"
        "What is the evolutionary benefit of shedding leaves during the winter season?"
    )
    correct = "It prevents excessive water loss through transpiration when soil is dry or frozen, and protects trees from frost and branch-breaking winter winds."
    options = [
        correct,
        "It allows trees to absorb moonlight directly through their tree trunks.",
        "Trees shed leaves because leaves become radioactive during winter.",
        "Trees shed leaves to feed earthworms so that soil becomes lighter in weight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand deciduous adaptation:\n"
        "Leaves lose water rapidly via transpiration through stomata.\n"
        "Step 2: Winter survival:\n"
        "With low winter sunlight and dry cold soil, trees reabsorb nutrients, break down green chlorophyll, and drop leaves to enter winter dormancy."
    )
    return {
        "id": f"ns7_sun_49_{rng.randint(100000, 999999)}",
        "subskill": "49_seasonal_plant_adaptations_deciduous_dormancy",
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
            "tier_1": "Why do trees drop leaves when it gets cold and dry?",
            "tier_2": "To conserve water and survive winter dormancy.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["deciduous_leaf_loss_misconception"]
    }


def arch_50_sun_earth_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    misconceptions = [
        ("Misconception: 'The Earth is closer to the Sun in summer and farther in winter.'", "Correction: Seasons are caused by Earth's 23.5° axial tilt, not orbital distance. In fact, Earth is closest to the Sun in January (Southern Hemisphere summer)."),
        ("Misconception: 'The Sun physically rises and sets by moving across a stationary Earth.'", "Correction: The Sun's daily motion is an apparent motion caused by Earth rotating from west to east on its axis once every 24 hours."),
        ("Misconception: 'Summer days are warmer solely because the Sun emits more nuclear fire.'", "Correction: The Sun's energy output is nearly constant; summer is warmer because steeper incoming rays deliver more concentrated heat and daylight lasts longer."),
        ("Misconception: 'Day and night are caused by Earth revolving in an orbit around the Sun.'", "Correction: Day and night are caused by Earth's 24-hour rotation on its own internal axis; revolution causes the 365.25-day year.")
    ]
    misc, corr = rng.choice(misconceptions)
    prompt = (
        f"A learner in a Grade 7 Natural Sciences examination submits the following answer:\n\n"
        f"**{misc}**\n\n"
        "Conduct a diagnostic autopsy of this answer. Which scientific correction accurately rectifies the error?"
    )
    correct = corr
    distractors = [c for m, c in misconceptions if c != corr]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Diagnostic Evaluation:\n"
        f"{misc}\n\n"
        f"Scientific Reality:\n"
        f"{corr}"
    )
    return {
        "id": f"ns7_sun_50_{rng.randint(100000, 999999)}",
        "subskill": "50_sun_earth_comprehensive_diagnostic_autopsy",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "hints": {
            "tier_1": "Carefully identify the conceptual error in the student's assertion.",
            "tier_2": "Contrast rotation vs revolution and tilt vs distance.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["comprehensive_solar_earth_diagnostic_error"]
    }
