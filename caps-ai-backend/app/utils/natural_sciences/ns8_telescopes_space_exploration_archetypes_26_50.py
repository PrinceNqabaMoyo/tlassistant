"""Grade 8 Natural Sciences - Looking into Space: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/03. Looking into space.md
Focus:
Radio astronomy (electromagnetic spectrum, radio waves, dish mechanics, 24/7 cloud penetration),
Interferometry and aperture synthesis, MeerKAT (64 dishes, Carnarvon Karoo, radio bubbles discovery),
Square Kilometre Array (SKA mega-project, SA-Mid and Aus-Low co-hosting, cosmic dawn science),
Atmospheric windows and turbulence (scintillation/seeing, adaptive optics),
Space telescopes (advantages, Hubble in LEO, JWST at L2, gold-coated beryllium mirrors, tennis-court sunshield,
Chandra/Fermi high-energy astronomy), Careers in astronomy (astrophysics, engineering, big data science),
SANSA (South African National Space Agency), Deep space probes vs telescopes, and Comprehensive Diagnostic Autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_electromagnetic_spectrum_beyond_visible_light(rng: random.Random) -> Dict[str, Any]:
    band, feature = rng.choice([
        ("Radio waves", "the longest wavelengths and lowest energy, penetrating through interstellar dust clouds"),
        ("Infrared radiation", "heat radiation that passes through cosmic dust to reveal newly forming protostars"),
        ("Ultraviolet radiation", "high-energy light emitted by massive hot young stars and active stellar coronae"),
        ("X-rays and Gamma rays", "extreme high-energy photons emitted by black hole accretion discs and supernova explosions")
    ])
    prompt = (
        "Human eyes only perceive a tiny sliver of the full electromagnetic spectrum called visible light.\n\n"
        f"Which statement correctly describes the astronomical significance of **{band}**?"
    )
    correct = f"It possesses {feature}."
    options = [
        correct,
        "It travels at half the speed of light compared to visible photons.",
        "It cannot travel through the vacuum of space and requires air to propagate.",
        "It is emitted exclusively by artificial radio antennas built on Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Electromagnetic spectrum breadth:\n"
        "Radio, Microwave, Infrared, Visible, Ultraviolet, X-ray, Gamma ray all travel at c = 300 000 km/s in vacuum.\n"
        f"Step 2: Role of {band}:\n"
        f"{band} possesses {feature}. Multi-wavelength astronomy provides a complete physical picture of the universe."
    )
    return {
        "id": f"ns8_tel_26_{rng.randint(100000, 999999)}",
        "subskill": "26_electromagnetic_spectrum_beyond_visible_light",
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
            "tier_1": f"What physical property characterizes {band}?",
            "tier_2": f"It possesses {feature[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["electromagnetic_spectrum_astronomy_bands"]
    }


def arch_27_radio_waves_properties_long_wavelength_penetration(rng: random.Random) -> Dict[str, Any]:
    wave_len = rng.choice(["millimeters to meters", "centimeters to several meters"])
    prompt = (
        f"Cosmic radio waves have wavelengths ranging from **{wave_len}**, compared to visible light whose wavelength is less than a millionth of a meter (~500 nm).\n\n"
        "What major physical advantage does this long wavelength give radio astronomy over optical astronomy?"
    )
    correct = "Radio waves easily diffract around and pass directly through dense interstellar dust lanes and Earth's overcast clouds without being scattered."
    options = [
        correct,
        "Radio waves can travel backward in time to before the Big Bang occurred.",
        "Radio waves can bounce off black holes without losing any energy.",
        "Radio waves make the astronomer's computers operate at infinite speed."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Rayleigh scattering and wavelength:\n"
        "Scattering intensity is inversely proportional to the fourth power of wavelength (I ∝ 1 / λ⁴).\n"
        "Step 2: Dust penetration:\n"
        "Because radio wavelengths (cm to m) are vastly larger than microscopic interstellar dust grains (~0,1 μm), radio waves pass straight through dust clouds that completely block visible starlight."
    )
    return {
        "id": f"ns8_tel_27_{rng.randint(100000, 999999)}",
        "subskill": "27_radio_waves_properties_long_wavelength_penetration",
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
            "tier_1": "Can long radio waves pass through dust and clouds?",
            "tier_2": "Yes, they penetrate through cosmic dust and overcast skies without scattering.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["radio_wave_dust_cloud_penetration"]
    }


def arch_28_radio_telescope_dish_antenna_and_feed_horn(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice(["parabolic dish reflector", "subreflector and feed horn"])
    prompt = (
        "A standard single-dish **radio telescope** uses metallic curved architecture to detect signals from space.\n\n"
        f"What is the optical and electrical role of the **{comp}** in a radio telescope?"
    )
    if comp == "parabolic dish reflector":
        correct = "To act as a curved metallic mirror that reflects and focuses incoming parallel radio waves toward the central receiver."
    else:
        correct = "To collect the focused radio energy from the dish and channel it into a cryogenic receiver to convert the electromagnetic waves into electrical voltages."
    options = [
        correct,
        "To broadcast loud music signals toward Mars to search for response echoes.",
        "To heat the air above the telescope so that rain clouds evaporate.",
        "To generate artificial gravity that holds the steel structure down."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Radio telescope anatomy:\n"
        "1. Parabolic Dish: curved metal surface (mesh or solid panels) acting as a primary concave reflector.\n"
        "2. Subreflector & Feed Horn: positioned at the focus; captures concentrated radio photons and couples them into waveguide circuits connected to low-noise amplifiers (LNAs) cooled by liquid helium."
    )
    return {
        "id": f"ns8_tel_28_{rng.randint(100000, 999999)}",
        "subskill": "28_radio_telescope_dish_antenna_and_feed_horn",
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
            "tier_1": f"What does the {comp} do to radio waves?",
            "tier_2": f"Review its function: {correct[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["radio_telescope_components_function"]
    }


def arch_29_radio_astronomy_24_hour_and_cloud_penetration_advantage(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Unlike optical observatories like SALT that can only observe on clear, cloudless nights, radio telescopes like MeerKAT can operate **24 hours a day, 365 days a year**.\n\n"
        "Why are radio observations unaffected by daytime sunlight and overcast cloud cover?"
    )
    correct = "Sunlight does not scatter radio waves in the atmosphere (no daytime 'radio skyglow'), and water droplets in rain clouds are too small to block long radio wavelengths."
    options = [
        correct,
        "Because radio telescopes use nuclear heaters that burn holes through clouds instantly.",
        "Because radio telescopes are placed underground inside deep gold mines.",
        "Because the Sun completely stops emitting any radiation during the day."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Lack of daytime skyglow:\n"
        "Rayleigh scattering of blue visible light illuminates our daytime sky, but radio waves have wavelengths millions of times longer and undergo zero atmospheric scattering.\n"
        "Step 2: Cloud transparency:\n"
        "Water droplets in clouds (~10 μm) are tiny compared to radio waves (cm to m), so radio signals pass through cloud cover unimpeded."
    )
    return {
        "id": f"ns8_tel_29_{rng.randint(100000, 999999)}",
        "subskill": "29_radio_astronomy_24_hour_and_cloud_penetration_advantage",
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
            "tier_1": "Do radio waves scatter in daytime air or bounce off rain clouds?",
            "tier_2": "No, they pass through unaffected, enabling 24/7 observation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["radio_astronomy_24_hour_weather_independence"]
    }


def arch_30_radio_interferometry_combining_signals_array_baseline(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Because radio waves have long wavelengths, a single radio dish has extraordinarily poor angular resolution unless it is made kilometers wide. Astronomers solve this using **radio interferometry**.\n\n"
        "How does radio interferometry link multiple independent radio dishes together?"
    )
    correct = "Signals from separate dishes are synchronized with nanosecond atomic clocks and transmitted via fiber optic cables to a central supercomputer (correlator) that combines the interference wave patterns."
    options = [
        correct,
        "All dishes are welded together with steel rods into a single solid physical dish.",
        "Each dish takes an ordinary photograph and astronomers glue the photos together with tape.",
        "Dishes use walkie-talkie audio signals to tell each other where to look."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The resolution problem of radio waves:\n"
        "Resolution θ ≈ λ / D. Because λ is large, D must be enormous to achieve sharp images.\n"
        "Step 2: Interferometry solution:\n"
        "Multiple antennas receive the same wavefront at slightly different times. An electronic correlator calculates cross-correlations, synthesizing interference fringes that reconstruct high-resolution celestial images."
    )
    return {
        "id": f"ns8_tel_30_{rng.randint(100000, 999999)}",
        "subskill": "30_radio_interferometry_combining_signals_array_baseline",
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
            "tier_1": "How are separate dishes combined in interferometry?",
            "tier_2": "Signals are synchronized with atomic clocks and processed by a correlator.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["radio_interferometry_correlation_concept"]
    }


def arch_31_virtual_telescope_effective_aperture_synthesis(rng: random.Random) -> Dict[str, Any]:
    baseline_km = rng.choice([8, 10, 20])
    prompt = (
        f"In an aperture synthesis radio array, individual antenna dishes are spread across the landscape with a maximum separation distance (baseline) of **{baseline_km} km**.\n\n"
        "What is the effective resolving diameter of the 'virtual telescope' created by this array?"
    )
    correct = f"It achieves the angular resolving power equivalent to a single giant telescope dish {baseline_km} km in diameter."
    options = [
        correct,
        f"It achieves the resolving power of a dish only {baseline_km} meters in diameter.",
        "It achieves zero resolving power because the space between dishes is completely wasted.",
        f"It achieves resolving power equal to {baseline_km} times the speed of light."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Aperture synthesis principle:\n"
        "The angular resolution of an interferometer depends on the maximum physical separation (baseline B) between the two most distant antennas (θ ≈ λ / B).\n"
        f"Step 2: Equivalent virtual aperture:\n"
        f"An array with an {baseline_km} km baseline resolves fine details identically to a hypothetical physical dish {baseline_km} km across!"
    )
    return {
        "id": f"ns8_tel_31_{rng.randint(100000, 999999)}",
        "subskill": "31_virtual_telescope_effective_aperture_synthesis",
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
            "tier_1": "What determines the resolving power of an interferometer array?",
            "tier_2": "The maximum baseline distance between the outermost dishes.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["aperture_synthesis_baseline_resolution"]
    }


def arch_32_meerkat_array_64_dishes_carnarvon_karoo(rng: random.Random) -> Dict[str, Any]:
    dish_count = 64
    diam_m = rng.choice(["13,5 meters", "13,5 m in diameter"])
    prompt = (
        f"South Africa's world-renowned **MeerKAT** radio telescope array consists of **{dish_count} dishes**, each {diam_m}, situated in the semi-desert near Carnarvon in the Northern Cape.\n\n"
        "Why is MeerKAT hailed globally as the most sensitive radio array in its frequency band?"
    )
    correct = "Its combination of 64 high-precision offset Gregorian dishes, ultra-low-noise cryogenic receivers, and radio-quiet Karoo location provides unprecedented sensitivity to faint cosmic radio emissions."
    options = [
        correct,
        "It uses optical lenses polished with diamonds to take high-resolution selfies of astronomers.",
        "It is built out of radioactive uranium that amplifies light waves automatically.",
        "It is suspended from helium balloons floating in the upper stratosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: MeerKAT specifications:\n"
        f"Inaugurated in 2018, MeerKAT comprises {dish_count} offset Gregorian dishes with a maximum baseline of 8 km.\n"
        "Step 2: World-leading performance:\n"
        "Its unblocked optical path (offset feed), cryogenically cooled digitizers, and strict protection under the Astronomy Geographic Advantage Act make it the most sensitive instrument on Earth at cm wavelengths."
    )
    return {
        "id": f"ns8_tel_32_{rng.randint(100000, 999999)}",
        "subskill": "32_meerkat_array_64_dishes_carnarvon_karoo",
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
            "tier_1": "How many dishes make up MeerKAT in the Karoo?",
            "tier_2": "64 dishes near Carnarvon.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["meerkat_specifications_and_sensitivity"]
    }


def arch_33_meerkat_breakthroughs_galactic_center_radio_bubbles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In 2019, MeerKAT made headlines worldwide by publishing an extraordinarily detailed radio mosaic of the centre of our Milky Way Galaxy.\n\n"
        "What colossal, previously unseen structures did MeerKAT reveal bursting outward from the galactic center?"
    )
    correct = "Enormous hourglass-shaped radio bubbles towering hundreds of light years above and below the galactic plane, energized by past explosive outbursts near the supermassive black hole."
    options = [
        correct,
        "A giant fleet of alien mother-ships parked around Neptune.",
        "A solid metal highway connecting Earth directly to the core of the galaxy.",
        "A field of blooming sunflowers growing on an asteroid."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: MeerKAT galactic center discovery:\n"
        "MeerKAT's clear mosaic penetrated the dense dust that blinds optical telescopes.\n"
        "Step 2: Radio bubbles phenomenon:\n"
        "It revealed two magnetized radio lobes spanning ~1 400 light years, likely produced by a cataclysmic energetic eruption from Sagittarius A* or a burst of star formation millions of years ago."
    )
    return {
        "id": f"ns8_tel_33_{rng.randint(100000, 999999)}",
        "subskill": "33_meerkat_breakthroughs_galactic_center_radio_bubbles",
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
            "tier_1": "What giant structures did MeerKAT discover at the center of the galaxy?",
            "tier_2": "Gigantic radio bubbles / lobes towering above and below the core.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["meerkat_galactic_center_bubbles_discovery"]
    }


def arch_34_square_kilometre_array_ska_global_mega_project(rng: random.Random) -> Dict[str, Any]:
    area_sq = "one square kilometer (1 000 000 m²)"
    prompt = (
        f"The **Square Kilometre Array (SKA)** is one of the largest scientific research facilities ever conceived by humanity. Its name originates from its planned total collecting area of **{area_sq}**.\n\n"
        "How will the completed SKA compare in scale and sensitivity to existing radio observatories?"
    )
    correct = "It will be roughly 50 times more sensitive and survey the sky 10 000 times faster than any previous radio instrument on Earth."
    options = [
        correct,
        "It will be smaller and slower than a handheld mobile smartphone.",
        "It will replace all existing hospitals and schools across Africa.",
        "It will have the exact same capabilities as Galileo's original 1609 telescope."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Scale of the SKA:\n"
        "An intergovernmental treaty organization (SKAO) comprising dozens of partner nations.\n"
        "Step 2: Performance leap:\n"
        "With one million square meters of collecting area spread across thousands of antennas over thousands of kilometers, the SKA represents an exponential quantum leap in cosmic discovery speed and sensitivity."
    )
    return {
        "id": f"ns8_tel_34_{rng.randint(100000, 999999)}",
        "subskill": "34_square_kilometre_array_ska_global_mega_project",
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
            "tier_1": "How much more sensitive will the SKA be compared to previous telescopes?",
            "tier_2": "Roughly 50 times more sensitive, mapping skies 10 000 times faster.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ska_scale_and_capabilities"]
    }


def arch_35_ska_co_hosting_south_africa_mid_australia_low(rng: random.Random) -> Dict[str, Any]:
    country, comp = rng.choice([
        ("South Africa (Karoo)", "SKA-Mid: mid-frequency dish antenna array (incorporating MeerKAT)"),
        ("Australia (Murchison)", "SKA-Low: low-frequency Christmas-tree-like dipole antenna array")
    ])
    prompt = (
        "The Square Kilometre Array (SKA) is co-hosted by two Southern Hemisphere nations.\n\n"
        f"What specific component of the SKA observatory is hosted by **{country}**?"
    )
    correct = comp
    options = [
        correct,
        "A single giant glass magnifying mirror suspended between two hot-air balloons.",
        "An underground submarine base searching for deep oceanic life.",
        "A nuclear rocket launch silo intended to deflect rogue comets."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Dual-site architecture:\n"
        "1. South Africa: SKA-Mid in the Karoo (350 MHz to 15 GHz), utilizing dish antennas (MeerKAT plus ~133 new SKA dishes).\n"
        "2. Australia: SKA-Low in Western Australia (50 to 350 MHz), utilizing ~131 072 stationary dipole antennas grouped in stations."
    )
    return {
        "id": f"ns8_tel_35_{rng.randint(100000, 999999)}",
        "subskill": "35_ska_co_hosting_south_africa_mid_australia_low",
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
            "tier_1": f"What type of SKA telescope does {country} host?",
            "tier_2": f"{country} hosts {comp[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ska_co_hosting_sa_mid_aus_low"]
    }


def arch_36_ska_scientific_goals_cosmic_dawn_and_gravity(rng: random.Random) -> Dict[str, Any]:
    goal, desc = rng.choice([
        ("Probing the Cosmic Dawn and Epoch of Reionization", "detecting the faint 21-cm hydrogen radio signal from the formation of the very first stars and galaxies"),
        ("Testing Einstein's General Relativity in extreme gravity", "timing cosmic clocks (pulsars) orbiting around supermassive black holes to detect gravitational waves"),
        ("Searching for Extraterrestrial Intelligence (SETI)", "detecting artificial, narrowband radio transmissions from technological civilizations on distant exoplanets")
    ])
    prompt = (
        f"The scientific agenda of the SKA is structured around fundamental questions in astrophysics.\n\n"
        f"How will the SKA accomplish its goal regarding **{goal}**?"
    )
    correct = f"By {desc}."
    options = [
        correct,
        "By drilling deep boreholes into Earth's mantle to measure magma pressure.",
        "By firing high-voltage lightning bolts into the clouds to alter the weather.",
        "By mining gold ore from passing near-Earth asteroids."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Core SKA science driver:\n"
        f"One of the key science goals is: {goal}.\n"
        f"Step 2: Technical execution:\n"
        f"The telescope achieves this by {desc}."
    )
    return {
        "id": f"ns8_tel_36_{rng.randint(100000, 999999)}",
        "subskill": "36_ska_scientific_goals_cosmic_dawn_and_gravity",
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
            "tier_1": f"How does the SKA investigate {goal[:25]}...?",
            "tier_2": f"It operates by {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ska_scientific_goals_cosmic_dawn"]
    }


def arch_37_atmospheric_windows_optical_and_radio_transmission(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth's atmosphere acts as a protective shield against cosmic radiation, creating only two major transparent **atmospheric windows** through which ground-based astronomy is possible.\n\n"
        "Which two regions of the electromagnetic spectrum easily penetrate Earth's atmosphere to reach ground observatories?"
    )
    correct = "The optical (visible light) window and the radio wave window."
    options = [
        correct,
        "The gamma-ray window and the X-ray window.",
        "The microwave oven window and the ultraviolet laser window.",
        "The nuclear fission window and the acoustic sound wave window."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric opacity:\n"
        "Ozone, oxygen, water vapor, and CO2 absorb gamma rays, X-rays, far UV, and most infrared wavelengths.\n"
        "Step 2: The two ground windows:\n"
        "1. Optical Window (~350 nm to 750 nm): visible light passes through.\n"
        "2. Radio Window (~1 cm to ~10–20 meters): radio waves pass through unimpeded. Telescopes for all other bands must be launched into space."
    )
    return {
        "id": f"ns8_tel_37_{rng.randint(100000, 999999)}",
        "subskill": "37_atmospheric_windows_optical_and_radio_transmission",
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
            "tier_1": "Which two bands reach the ground through the atmosphere?",
            "tier_2": "Visible (optical) and radio waves.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmospheric_windows_optical_and_radio"]
    }


def arch_38_atmospheric_turbulence_twinkling_seeing_degradation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When stargazers look at stars at night, stars appear to twinkle (scintillate), appearing through telescopes as blurred, dancing discs called 'seeing discs'.\n\n"
        "What atmospheric condition causes this rapid stellar twinkling and blurring?"
    )
    correct = "Pockets of warm and cold air with fluctuating temperatures and refractive indices constantly swirling through turbulent atmospheric layers, rapidly bending the incoming starlight."
    options = [
        correct,
        "The stars are physically turning their fusion fire on and off thirty times every second.",
        "Small meteors are continuously hitting the front of the telescope eyepiece.",
        "Light rays are being deflected by the gravitational pull of flying birds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cause of scintillation:\n"
        "Stars are point sources of light located many light years away.\n"
        "Step 2: Atmospheric turbulence:\n"
        "As the narrow column of starlight traverses Earth's turbulent atmosphere, convective eddies of different temperatures and densities refract the light randomly, causing rapid fluctuations in brightness (twinkling) and position (astronomical seeing)."
    )
    return {
        "id": f"ns8_tel_38_{rng.randint(100000, 999999)}",
        "subskill": "38_atmospheric_turbulence_twinkling_seeing_degradation",
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
            "tier_1": "What happens when light travels through turbulent pockets of warm and cold air?",
            "tier_2": "It refracts rapidly, causing twinkling and blurred images.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomical_seeing_atmospheric_turbulence"]
    }


def arch_39_adaptive_optics_laser_guide_stars_atmospheric_correction(rng: random.Random) -> Dict[str, Any]:
    freq_hz = rng.choice(["hundreds of times per second", "up to 1 000 times per second"])
    prompt = (
        f"Modern ground-based optical observatories use high-tech **adaptive optics** systems featuring deformable mirrors adjusted {freq_hz}.\n\n"
        "How does adaptive optics cancel out atmospheric blurring to achieve images as sharp as space telescopes?"
    )
    correct = "A wave-front sensor measures the atmospheric distortion (often using a laser guide star projected into the upper atmosphere), and computer-controlled actuators instantly warp the deformable mirror to apply the exact opposite shape."
    options = [
        correct,
        "A giant vacuum cleaner sucks all the air out of the atmosphere above the observatory.",
        "The telescope mirror rotates at supersonic speeds to slice through the air.",
        "The telescope shoots laser beams that vaporize all clouds within 500 kilometers."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Real-time wave-front sensing:\n"
        "Turbulent air distorts flat incoming starlight wavefronts. Adaptive optics uses a bright star or sodium laser guide star to detect the distortions in real time.\n"
        "Step 2: Dynamic correction:\n"
        "Micro-actuators flex a thin secondary mirror hundreds of times per second to cancel out the phase errors, restoring diffraction-limited sharpness."
    )
    return {
        "id": f"ns8_tel_39_{rng.randint(100000, 999999)}",
        "subskill": "39_adaptive_optics_laser_guide_stars_atmospheric_correction",
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
            "tier_1": "What does a deformable mirror do in adaptive optics?",
            "tier_2": "It flexes in real time to counteract atmospheric distortion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["adaptive_optics_atmospheric_correction"]
    }


def arch_40_space_telescope_advantages_zero_atmosphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Space agencies spend billions of dollars building and launching space observatories like Hubble and James Webb into outer space.\n\n"
        "What are the three decisive scientific advantages of placing telescopes in space rather than on high mountains on Earth?"
    )
    correct = "Zero atmospheric turbulence (no blurring/twinkling), access to all blocked wavelengths (UV, X-rays, far-infrared), and no interference from clouds, weather, or urban light pollution."
    options = [
        correct,
        "Telescopes in space are physically 90% closer to the Andromeda Galaxy than Earth telescopes.",
        "Space telescopes can land directly on stars to collect burning rock samples.",
        "Space telescopes can turn off the law of universal gravitation completely."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmosphere as an obstacle:\n"
        "Earth's atmosphere blurs images (seeing), blocks entire wavebands (opacity), and scatters city light (light pollution).\n"
        "Step 2: Space environment advantages:\n"
        "In the vacuum of space, telescopes operate 24/7 without weather, observe crystal-clear diffraction-limited images, and access UV, X-ray, gamma, and infrared radiation blocked by air."
    )
    return {
        "id": f"ns8_tel_40_{rng.randint(100000, 999999)}",
        "subskill": "40_space_telescope_advantages_zero_atmosphere",
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
            "tier_1": "What problems on Earth disappear when a telescope is in space?",
            "tier_2": "Atmospheric blurring, weather, light pollution, and blocked wavelengths.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["space_telescope_operational_advantages"]
    }


def arch_41_hubble_space_telescope_low_earth_orbit_achievements(rng: random.Random) -> Dict[str, Any]:
    alt_km = rng.choice(["approximately 540 km", "around 535 to 550 km in Low Earth Orbit"])
    prompt = (
        f"Launched in 1990 into Low Earth Orbit at an altitude of {alt_km}, the **Hubble Space Telescope (HST)** revolutionized astronomy.\n\n"
        "What landmark observation was achieved by the famous **Hubble Deep Field** image?"
    )
    correct = "Pointing at a tiny, seemingly empty patch of dark sky for 10 days revealed thousands of previously undiscovered distant galaxies stretching back into the early universe."
    options = [
        correct,
        "Photographing footprints left by dinosaurs on the surface of Mars.",
        "Discovering a solid wall of iron marking the outer boundary of the universe.",
        "Finding an ancient mechanical clock orbiting inside the core of the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hubble Deep Field (1995):\n"
        "Astronomers aimed Hubble at an empty speck of sky (the size of a pinhead held at arm's length) for 100 hours of cumulative exposure.\n"
        "Step 2: Scientific revelation:\n"
        "The image revealed nearly 3 000 galaxies in various stages of evolution, demonstrating that the observable universe is populated by hundreds of billions of galaxies."
    )
    return {
        "id": f"ns8_tel_41_{rng.randint(100000, 999999)}",
        "subskill": "41_hubble_space_telescope_low_earth_orbit_achievements",
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
            "tier_1": "What did the Hubble Deep Field reveal in an 'empty' patch of sky?",
            "tier_2": "Thousands of distant galaxies stretching back into early cosmic history.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hubble_deep_field_galaxy_abundance"]
    }


def arch_42_james_webb_space_telescope_lagrange_point_l2_location(rng: random.Random) -> Dict[str, Any]:
    dist_mkm = rng.choice(["1,5 million km", "approximately 1,5 million kilometers from Earth"])
    prompt = (
        f"Unlike Hubble which orbits Earth at 540 km, the **James Webb Space Telescope (JWST)** operates at the **Sun-Earth Lagrange Point 2 (L2)**, located {dist_mkm} away.\n\n"
        "What critical thermal advantage does the L2 orbit offer JWST?"
    )
    correct = "It keeps the Earth, Moon, and Sun permanently aligned on one side behind its giant sunshield, allowing the telescope to remain in perpetual cryogenic darkness without cycling in and out of Earth's shadow."
    options = [
        correct,
        "It places the telescope close enough for astronauts to walk to it every morning for repairs.",
        "It allows the telescope to use Earth's atmosphere as an extra magnifying glass.",
        "It protects the telescope from the vacuum of space by surrounding it with oxygen gas."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Orbital geometry of L2:\n"
        "Lagrange point 2 is a gravitational equilibrium point on the night side of Earth, 1,5 million km away.\n"
        "Step 2: Thermal stability:\n"
        "Because the Sun, Earth, and Moon stay in the exact same direction, a single sunshield permanently blocks all three heat sources, enabling ultra-cold cryogenic operation essential for infrared astronomy."
    )
    return {
        "id": f"ns8_tel_42_{rng.randint(100000, 999999)}",
        "subskill": "42_james_webb_space_telescope_lagrange_point_l2_location",
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
            "tier_1": "Why is L2 ideal for a sunshield?",
            "tier_2": "Sun, Earth, and Moon stay on one side, keeping the telescope permanently cold.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["jwst_lagrange_point_l2_thermal_advantage"]
    }


def arch_43_jwst_infrared_specialization_and_beryllium_gold_mirror(rng: random.Random) -> Dict[str, Any]:
    num_seg = 18
    diam_m = 6.5
    prompt = (
        f"JWST features a **{diam_m}-meter primary mirror** made of **{num_seg} hexagonal beryllium segments** coated in an ultra-thin microscopically pure layer of **gold**.\n\n"
        "Why is gold chosen as the mirror coating, and why is JWST optimized specifically for **infrared light**?"
    )
    correct = "Gold reflects infrared light with exceptional efficiency (>98%), and infrared light allows JWST to penetrate cosmic dust and capture highly redshifted light from the earliest galaxies in the universe."
    options = [
        correct,
        "Gold makes the telescope look expensive so international sponsors provide more funding.",
        "Gold is a magnetic metal that repels harmful asteroid impacts in deep space.",
        "Gold transforms visible starlight into cold liquid water to cool the cameras."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mirror material:\n"
        "Beryllium provides extreme stiffness-to-weight at cryogenic temperatures (-230 °C). The 18 segments are vapor-coated with ~100 nm of pure gold.\n"
        "Step 2: Infrared superiority:\n"
        "Gold has peak reflectivity in infrared. Infrared is required because cosmic expansion has redshifted the light from the first stars (born 13,5 billion years ago) from ultraviolet/visible into the near- and mid-infrared."
    )
    return {
        "id": f"ns8_tel_43_{rng.randint(100000, 999999)}",
        "subskill": "43_jwst_infrared_specialization_and_beryllium_gold_mirror",
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
            "tier_1": "What wavelength of light does gold reflect best?",
            "tier_2": "Infrared light (>98% reflectivity).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["jwst_gold_coating_infrared_specialization"]
    }


def arch_44_jwst_cryogenic_sunshield_tennis_court_scale(rng: random.Random) -> Dict[str, Any]:
    layers = 5
    temp_diff = rng.choice(["over 300 °C (from +85 °C on the hot side to -233 °C on the cold side)", "approximately 300 degrees Celsius across its layers"])
    prompt = (
        f"JWST deploys a five-layer Kapton sunshield roughly the size of a tennis court, establishing an extraordinary temperature gradient of {temp_diff}.\n\n"
        "Why must the telescope's scientific instruments be maintained at extreme cryogenic temperatures (below 50 Kelvin / -223 °C)?"
    )
    correct = "Because any warm object radiates its own infrared thermal glow; if the telescope were warm, its own heat radiation would completely blind its sensitive infrared detectors."
    options = [
        correct,
        "Because cold temperatures prevent the telescope's metal from expanding and cracking Earth's orbit.",
        "Because the telescope's digital cameras freeze light waves into solid photographic blocks.",
        "Because alien signals can only travel through ice sheets."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Infrared blackbody radiation:\n"
        "Any object with temperature above absolute zero emits thermal infrared radiation (Stefan-Boltzmann law).\n"
        "Step 2: Blinding effect:\n"
        "If JWST's mirrors and instruments were at room temperature, their own thermal glow would overwhelm faint photons from distant galaxies. The 5-layer sunshield passively cools the optics below 50 K (-223 °C)."
    )
    return {
        "id": f"ns8_tel_44_{rng.randint(100000, 999999)}",
        "subskill": "44_jwst_cryogenic_sunshield_tennis_court_scale",
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
            "tier_1": "What kind of radiation does a warm object emit?",
            "tier_2": "Infrared heat; if the telescope is warm, it blinds its own infrared sensors.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["jwst_sunshield_thermal_infrared_isolation"]
    }


def arch_45_xray_and_gamma_ray_space_telescopes_chandra_fermi(rng: random.Random) -> Dict[str, Any]:
    tel, band, source = rng.choice([
        ("Chandra X-ray Observatory", "X-rays", "superheated gas swirling at millions of degrees into black hole accretion discs"),
        ("Fermi Gamma-ray Space Telescope", "gamma rays", "relativistic plasma jets launched by blazars and colliding neutron stars (kilonovae)")
    ])
    prompt = (
        f"NASA's **{tel}** operates in outer space, specializing in high-energy **{band}**.\n\n"
        f"What violent astrophysical phenomenon does {tel} primarily investigate?"
    )
    correct = f"It observes {source}."
    options = [
        correct,
        "It tracks penguins walking on icebergs in Antarctica.",
        "It searches for ancient fossilized seashells on the floor of the Pacific Ocean.",
        "It measures the air pressure inside automobile tires on Earth."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: High-energy band:\n"
        f"{tel} detects {band} which are completely absorbed by Earth's upper atmosphere.\n"
        f"Step 2: Source physics:\n"
        f"{band} are produced by extreme high-energy thermal and relativistic processes, such as {source}."
    )
    return {
        "id": f"ns8_tel_45_{rng.randint(100000, 999999)}",
        "subskill": "45_xray_and_gamma_ray_space_telescopes_chandra_fermi",
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
            "tier_1": f"What violent events produce {band}?",
            "tier_2": f"It observes {source[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["high_energy_space_observatories"]
    }


def arch_46_careers_in_astronomy_astrophysicists_and_engineers(rng: random.Random) -> Dict[str, Any]:
    role, duties = rng.choice([
        ("Observational Astrophysicist", "analyzing spectral data and images from observatories to formulate mathematical models of stellar and galactic evolution"),
        ("Radio Frequency (RF) Engineer", "designing and calibrating high-frequency feed horns, waveguides, and low-noise receivers for telescopes like MeerKAT"),
        ("Cryogenics Technician", "operating liquid helium cooling equipment to maintain detector instruments at near-absolute zero temperatures"),
        ("Optical Engineer", "aligning, testing, and maintaining precision hexagonal mirror arrays and laser tracking systems at SALT")
    ])
    prompt = (
        "Modern astronomical mega-projects require diverse multi-disciplinary teams.\n\n"
        f"What is the primary professional responsibility of an **{role}** working at an astronomical facility?"
    )
    correct = f"They are responsible for {duties}."
    options = [
        correct,
        "They are responsible for manually steering the telescope by hand using physical ropes.",
        "They are responsible for forecasting personal horoscopes for daily newspapers.",
        "They are responsible for predicting lottery numbers using star patterns."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Specialized career role:\n"
        f"The profession of {role} is a critical component of mega-science.\n"
        f"Step 2: Key responsibilities:\n"
        f"Their work involves {duties}."
    )
    return {
        "id": f"ns8_tel_46_{rng.randint(100000, 999999)}",
        "subskill": "46_careers_in_astronomy_astrophysicists_and_engineers",
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
            "tier_1": f"What does an {role} do at an observatory?",
            "tier_2": f"They are responsible for {duties[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomy_stem_careers_roles"]
    }


def arch_47_data_science_and_big_data_in_modern_astronomy(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice(["terabytes to petabytes of raw data per day", "hundreds of terabytes of digitized signals every 24 hours"])
    prompt = (
        f"Next-generation radio observatories like MeerKAT and the SKA produce astronomical 'Big Data' generating {vol}.\n\n"
        "How do modern astronomers process and analyze this gargantuan flood of information?"
    )
    correct = "Using high-performance computing clusters, cloud supercomputing, automated machine learning algorithms, and distributed processing pipelines."
    options = [
        correct,
        "Printing out the data on paper sheets and reading through them line by line with magnifying glasses.",
        "Storing the data on magnetic floppy disks mailed to scientists via the post office.",
        "Engraving the numbers onto stone tablets stored inside mountain caves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Big data volume in astronomy:\n"
        "The SKA will produce data rates comparable to the entire global internet traffic.\n"
        "Step 2: Computational astronomy:\n"
        "Astronomy has evolved into a data science. Algorithms, artificial intelligence, and supercomputers (such as the Centre for High Performance Computing in Cape Town) automatically flag transient events, clean radio frequency interference, and generate celestial maps."
    )
    return {
        "id": f"ns8_tel_47_{rng.randint(100000, 999999)}",
        "subskill": "47_data_science_and_big_data_in_modern_astronomy",
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
            "tier_1": "How are petabytes of data analyzed today?",
            "tier_2": "Using supercomputing clusters and automated machine learning algorithms.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomy_big_data_supercomputing"]
    }


def arch_48_south_african_space_agency_sansa_earth_observation(rng: random.Random) -> Dict[str, Any]:
    facility = rng.choice(["Hermanus in the Western Cape (Space Science)", "Hartebeesthoek in Gauteng (Ground Operations)"])
    prompt = (
        f"Established in 2010, the **South African National Space Agency (SANSA)** operates key facilities, including at {facility}.\n\n"
        "What critical operational service does SANSA provide to protect modern technological infrastructure?"
    )
    correct = "Monitoring space weather (solar flares and coronal mass ejections) that induce geomagnetic storms that can disrupt electrical power grids, aviation communications, and GPS satellites."
    options = [
        correct,
        "Building nuclear missiles to shoot down passing meteors.",
        "Operating commercial passenger airlines flying between Cape Town and London.",
        "Manufacturing household microwave ovens for retail stores."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: SANSA's mandate:\n"
        "SANSA oversees South Africa's space research, Earth observation satellite data, and space operations.\n"
        "Step 2: Space weather monitoring (Hermanus):\n"
        "As the designated Regional Warning Centre for Africa, SANSA tracks solar activity 24/7 to issue geomagnetic storm warnings, safeguarding national power grids (Eskom) and aviation navigation."
    )
    return {
        "id": f"ns8_tel_48_{rng.randint(100000, 999999)}",
        "subskill": "48_south_african_space_agency_sansa_earth_observation",
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
            "tier_1": "What dangerous space phenomenon does SANSA monitor to protect GPS and power grids?",
            "tier_2": "Space weather (solar flares and geomagnetic storms).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sansa_space_weather_infrastructure_protection"]
    }


def arch_49_deep_space_probes_vs_telescopes_complementary_roles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In space exploration, scientists utilize both astronomical telescopes (ground and space-based) and robotic space probes (landers, orbiters, rovers).\n\n"
        "How do the scientific roles of telescopes and robotic space probes complement each other?"
    )
    correct = "Telescopes provide broad, long-term observational panoramas across billions of light years of the universe, whereas robotic probes conduct close-up, direct physical sampling of soils, atmospheres, and rocks within our solar system."
    options = [
        correct,
        "Telescopes can only observe objects smaller than one meter, while probes observe entire galaxies.",
        "Telescopes take black-and-white photos, while space probes can only listen to sound waves.",
        "Telescopes are used exclusively for military defence, while probes are used for weather forecasts."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Telescopes' domain:\n"
        "Electromagnetic observation across immense cosmic distances (galaxies, nebulae, exoplanets) without leaving the vicinity of Earth.\n"
        "Step 2: Probes' domain:\n"
        "In-situ ground truth: drilling Martian rock, tasting plumes on Enceladus, photographing close-up crater stratigraphy. Together, they create a comprehensive scientific understanding."
    )
    return {
        "id": f"ns8_tel_49_{rng.randint(100000, 999999)}",
        "subskill": "49_deep_space_probes_vs_telescopes_complementary_roles",
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
            "tier_1": "How do telescopes and robotic rovers differ in scope?",
            "tier_2": "Telescopes observe vast distances; probes perform close-up direct physical sampling.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["telescopes_vs_probes_complementary_roles"]
    }


def arch_50_looking_into_space_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    tech, trait, mechanism = rng.choice([
        ("Refracting telescopes", "chromatic aberration", "differential refraction of light wavelengths through glass objective lenses"),
        ("Reflecting telescopes", "absence of chromatic aberration", "reflection angles off curved mirrors are identical for all wavelengths"),
        ("Radio interferometers", "high angular resolution", "combining separated signals to synthesize a virtual aperture equal to the maximum baseline"),
        ("JWST", "cryogenic operation below 50 K", "tennis-court sunshield blocking infrared thermal heat from Sun and Earth")
    ])
    prompt = (
        f"**Comprehensive Optical and Astronomical Diagnostic:**\n"
        f"In assessing astronomical instrumentation, engineers note that **{tech}** uniquely display **{trait}**.\n\n"
        f"What underlying physical mechanism accounts for this operational feature in {tech}?"
    )
    correct = mechanism
    options = [
        correct,
        "artificial colored paint applied to the exterior metal tripod tubes",
        "continuous electric lightning bolts striking the observatory dome",
        "the gravitational pull of passing aircraft flying over the mountains"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Target technology and attribute:\n"
        f"{tech} exhibit {trait}.\n"
        f"Step 2: Underlying scientific cause:\n"
        f"The physical mechanism is: {mechanism}."
    )
    return {
        "id": f"ns8_tel_50_{rng.randint(100000, 999999)}",
        "subskill": "50_looking_into_space_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"What causes {trait} in {tech}?",
            "tier_2": f"The cause is {mechanism[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomical_instrumentation_diagnostic_autopsy"]
    }


BUILDERS_26_50 = {
    "26_electromagnetic_spectrum_beyond_visible_light": arch_26_electromagnetic_spectrum_beyond_visible_light,
    "27_radio_waves_properties_long_wavelength_penetration": arch_27_radio_waves_properties_long_wavelength_penetration,
    "28_radio_telescope_dish_antenna_and_feed_horn": arch_28_radio_telescope_dish_antenna_and_feed_horn,
    "29_radio_astronomy_24_hour_and_cloud_penetration_advantage": arch_29_radio_astronomy_24_hour_and_cloud_penetration_advantage,
    "30_radio_interferometry_combining_signals_array_baseline": arch_30_radio_interferometry_combining_signals_array_baseline,
    "31_virtual_telescope_effective_aperture_synthesis": arch_31_virtual_telescope_effective_aperture_synthesis,
    "32_meerkat_array_64_dishes_carnarvon_karoo": arch_32_meerkat_array_64_dishes_carnarvon_karoo,
    "33_meerkat_breakthroughs_galactic_center_radio_bubbles": arch_33_meerkat_breakthroughs_galactic_center_radio_bubbles,
    "34_square_kilometre_array_ska_global_mega_project": arch_34_square_kilometre_array_ska_global_mega_project,
    "35_ska_co_hosting_south_africa_mid_australia_low": arch_35_ska_co_hosting_south_africa_mid_australia_low,
    "36_ska_scientific_goals_cosmic_dawn_and_gravity": arch_36_ska_scientific_goals_cosmic_dawn_and_gravity,
    "37_atmospheric_windows_optical_and_radio_transmission": arch_37_atmospheric_windows_optical_and_radio_transmission,
    "38_atmospheric_turbulence_twinkling_seeing_degradation": arch_38_atmospheric_turbulence_twinkling_seeing_degradation,
    "39_adaptive_optics_laser_guide_stars_atmospheric_correction": arch_39_adaptive_optics_laser_guide_stars_atmospheric_correction,
    "40_space_telescope_advantages_zero_atmosphere": arch_40_space_telescope_advantages_zero_atmosphere,
    "41_hubble_space_telescope_low_earth_orbit_achievements": arch_41_hubble_space_telescope_low_earth_orbit_achievements,
    "42_james_webb_space_telescope_lagrange_point_l2_location": arch_42_james_webb_space_telescope_lagrange_point_l2_location,
    "43_jwst_infrared_specialization_and_beryllium_gold_mirror": arch_43_jwst_infrared_specialization_and_beryllium_gold_mirror,
    "44_jwst_cryogenic_sunshield_tennis_court_scale": arch_44_jwst_cryogenic_sunshield_tennis_court_scale,
    "45_xray_and_gamma_ray_space_telescopes_chandra_fermi": arch_45_xray_and_gamma_ray_space_telescopes_chandra_fermi,
    "46_careers_in_astronomy_astrophysicists_and_engineers": arch_46_careers_in_astronomy_astrophysicists_and_engineers,
    "47_data_science_and_big_data_in_modern_astronomy": arch_47_data_science_and_big_data_in_modern_astronomy,
    "48_south_african_space_agency_sansa_earth_observation": arch_48_south_african_space_agency_sansa_earth_observation,
    "49_deep_space_probes_vs_telescopes_complementary_roles": arch_49_deep_space_probes_vs_telescopes_complementary_roles,
    "50_looking_into_space_comprehensive_diagnostic_autopsy": arch_50_looking_into_space_comprehensive_diagnostic_autopsy,
}
