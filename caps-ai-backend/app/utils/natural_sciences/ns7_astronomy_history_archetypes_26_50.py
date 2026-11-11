"""Grade 7 Natural Sciences - Historical Development of Astronomy: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md
Focus: Sunspots, Saturn rings, Galileo and Church, Newton's universal gravitation, reflecting vs refracting telescopes,
radio astronomy (Jansky), South African astronomy (Sutherland Karoo, SALT, HartRAO, MeerKAT, SKA),
space telescopes (Hubble, JWST), multispectral astronomy, careers, and comprehensive diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_sunspots_observation_solar_rotation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When Galileo projected the Sun's image onto white paper using his telescope, "
        "he recorded dark, irregular blemishes drifting across the solar disc day after day.\n\n"
        "What are these **sunspots**, and what did their daily drift prove to astronomers?"
    )
    correct = "Sunspots are cooler regions on the Sun's surface caused by intense magnetic fields; their movement proved that the Sun rotates on its axis."
    options = [
        correct,
        "Sunspots are flocks of space birds nesting on the Sun's surface.",
        "Sunspots are dark planets orbiting inside Earth's atmosphere.",
        "Sunspots prove that the Sun is made of solid burning coal that burns unevenly."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Scientific nature of sunspots:\n"
        "Sunspots are areas where strong magnetic activity suppresses convection, making them cooler (~3 700 K) and darker than surrounding photosphere (~5 800 K).\n"
        "Step 2: Proving solar rotation:\n"
        "By tracking their transit across the solar disc over ~27 days, Galileo proved that the Sun itself spins on an axis."
    )
    return {
        "id": f"ns7_astro_26_{rng.randint(100000, 999999)}",
        "subskill": "26_sunspots_observation_solar_rotation",
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
            "tier_1": "What causes the spots to move across the Sun's face?",
            "tier_2": "The Sun rotates on its own axis.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["sunspot_nature_and_rotation_error"]
    }


def arch_27_saturns_rings_early_telescopic_puzzles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When Galileo observed Saturn with his low-magnification telescope in 1610, he noted that Saturn "
        "appeared to have 'ears' or two smaller companion spheres on either side, which later disappeared and reappeared.\n\n"
        "What spectacular planetary feature was Galileo actually observing with inadequate optical resolution?"
    )
    correct = "The rings of Saturn (later resolved by Christiaan Huygens in 1655 using a superior telescope)."
    options = [
        correct,
        "Giant space sails used by alien explorers.",
        "Two massive moons that collide with Saturn every decade.",
        "Smoke clouds drifting from active Saturnian volcanoes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Galileo's observation:\n"
        "Galileo described Saturn as 'triple-bodied' because his 20x telescope blurred the rings into side lobes ('ears').\n"
        "Step 2: Resolution:\n"
        "In 1655, Dutch astronomer Christiaan Huygens used a more powerful telescope to correctly identify the lobes as a flat, unattached ring system encircling Saturn."
    )
    return {
        "id": f"ns7_astro_27_{rng.randint(100000, 999999)}",
        "subskill": "27_saturns_rings_early_telescopic_puzzles",
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
            "tier_1": "Which planet is famous for its majestic system of rings?",
            "tier_2": "Saturn's rings appeared as 'ears' in early telescopes.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["saturn_rings_discovery_chronology"]
    }


def arch_28_galileos_conflict_with_inquisition_house_arrest(rng: random.Random) -> Dict[str, Any]:
    year = "1633"
    prompt = (
        f"In {year}, Galileo Galilei was summoned to Rome by the Roman Catholic Inquisition "
        "and put on trial after publishing his book *Dialogue Concerning the Two Chief World Systems*.\n\n"
        "What was the outcome of Galileo's trial regarding his support for the Copernican heliocentric theory?"
    )
    correct = "He was forced to recant his heliocentric views, his book was banned, and he spent the remainder of his life under house arrest near Florence."
    options = [
        correct,
        "He was awarded a gold medal and made head of the Vatican astronomical observatory.",
        "He was exiled to South Africa where he built the first Sutherland telescope.",
        "He immediately abandoned science to become a professional military general."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical context of the trial:\n"
        "The Church held that literal interpretations of Scripture supported a stationary Earth.\n"
        "Step 2: Inquisition verdict:\n"
        "Suspected of heresy, Galileo was forced to kneel and recite an abjuration in 1633. He remained confined to his villa in Arcetri under house arrest until his death in 1642."
    )
    return {
        "id": f"ns7_astro_28_{rng.randint(100000, 999999)}",
        "subskill": "28_galileos_conflict_with_inquisition_house_arrest",
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
            "tier_1": "Did religious authorities of the 1600s welcome heliocentrism?",
            "tier_2": "Galileo was forced to recant and placed under house arrest.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["galileo_trial_outcome_error"]
    }


def arch_29_isaac_newton_law_of_universal_gravitation(rng: random.Random) -> Dict[str, Any]:
    year = "1687"
    prompt = (
        f"In {year}, English physicist and mathematician **Sir Isaac Newton** published the monumental *Philosophiae Naturalis Principia Mathematica*.\n\n"
        "What revolutionary concept did Newton introduce with his **Law of Universal Gravitation**?"
    )
    correct = "The very same gravitational force that pulls an apple down to Earth also pulls the Moon into orbit around Earth and planets around the Sun."
    options = [
        correct,
        "Gravity only exists on Earth and has zero influence in outer space.",
        "Planets are pushed through space by invisible angels with giant wings.",
        "The Sun repels all planets using magnetic anti-gravity."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Concept of 'Universal' gravitation:\n"
        "Prior to Newton, people thought celestial physics was totally different from terrestrial physics.\n"
        "Step 2: Newton's unification:\n"
        "Newton showed that gravity is universal: every particle of matter attracts every other particle with a force proportional to mass and inversely proportional to the square of the distance (F = G*m1*m2/r²)."
    )
    return {
        "id": f"ns7_astro_29_{rng.randint(100000, 999999)}",
        "subskill": "29_isaac_newton_law_of_universal_gravitation",
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
            "tier_1": "Does the same gravity that drops an apple also hold the Moon in orbit?",
            "tier_2": "Universal gravitation unites terrestrial and celestial physics.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["universal_gravitation_unification_error"]
    }


def arch_30_newton_explaining_keplers_elliptical_orbits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "While Johannes Kepler discovered that planets move in elliptical orbits, he could not explain **why** they did so.\n\n"
        "How did Isaac Newton complete Kepler's work?"
    )
    correct = "Newton mathematically proved that Kepler's laws of elliptical orbits are the direct consequence of an inverse-square gravitational attraction from the Sun."
    options = [
        correct,
        "Newton showed that Kepler's data was completely fabricated and that orbits are square.",
        "Newton proved that magnetic compasses steer the planets across space.",
        "Newton demonstrated that solar wind pushes planets outward in straight lines."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Kepler vs Newton distinction:\n"
        "- Kepler described HOW planets move (empirical mathematical rules).\n"
        "- Newton explained WHY planets move (physical force: gravity).\n"
        "Step 2: Mathematical proof: Newton derived all three of Kepler's laws directly from his Universal Law of Gravitation and Laws of Motion."
    )
    return {
        "id": f"ns7_astro_30_{rng.randint(100000, 999999)}",
        "subskill": "30_newton_explaining_keplers_elliptical_orbits",
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
            "tier_1": "Kepler described the motion; Newton provided the physical gravitational cause.",
            "tier_2": "Gravity accounts for Kepler's elliptical orbits.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["kepler_vs_newton_scientific_contribution"]
    }


def arch_31_invention_of_reflecting_telescope_newton_mirrors(rng: random.Random) -> Dict[str, Any]:
    year = "1668"
    prompt = (
        f"In {year}, Isaac Newton designed and constructed a fundamentally new type of telescope: the **reflecting telescope**.\n\n"
        "Instead of using a glass objective lens to collect light, what optical component did Newton use?"
    )
    correct = "A curved (concave) primary mirror to gather light and reflect it to a focus."
    options = [
        correct,
        "A series of triangular prisms filled with olive oil.",
        "A flat piece of dark obsidian volcanic rock.",
        "A diamond laser beam projector."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify optical innovation:\n"
        "Newton replaced the glass objective lens with a curved metal speculum mirror.\n"
        "Step 2: Working principle:\n"
        "Light bounces off the primary concave mirror to a secondary flat diagonal mirror, which directs light into an eyepiece on the side of the tube."
    )
    stroke_c = rng.choice(["#38bdf8", "#0284c7", "#0284c7"])
    mir_w = rng.choice([3, 4, 5])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" width="100%" height="130"><rect x="30" y="30" width="240" height="70" fill="none" stroke="#475569" stroke-width="2"/><path d="M 270 30 Q 255 65 270 100" fill="none" stroke="{stroke_c}" stroke-width="{mir_w}"/><text x="270" y="120" text-anchor="middle" font-size="9" fill="#38bdf8">Primary Mirror</text><line x1="100" y1="55" x2="120" y2="75" stroke="#ef4444" stroke-width="3"/><text x="110" y="45" font-size="8" fill="#ef4444">Secondary</text><rect x="105" y="10" width="12" height="20" fill="#64748b"/><text x="111" y="8" text-anchor="middle" font-size="8">Eyepiece</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_astro_31_{rng.randint(100000, 999999)}",
        "subskill": "31_invention_of_reflecting_telescope_newton_mirrors",
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
            "tier_1": "What reflects light instead of refracting it?",
            "tier_2": "A curved mirror (reflecting telescope).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["reflecting_telescope_component_error"]
    }


def arch_32_refracting_telescopes_lenses_chromatic_aberration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Early astronomers using large refracting telescopes with glass lenses noticed distracting "
        "rainbow-colored fringes around bright stars and planets.\n\n"
        "What optical defect causes this **chromatic aberration** in refracting telescopes?"
    )
    correct = "Glass bends different wavelengths (colors) of light by slightly different amounts, so blue and red light focus at different focal points."
    options = [
        correct,
        "Dust particles from space stick to the outside of the telescope tube.",
        "Light travels faster in the dark, stretching stars into rainbow ribbons.",
        "The telescope tube bends under its own weight, squeezing the photons."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand refraction dispersion:\n"
        "When white light passes through a glass lens, shorter blue wavelengths refract more sharply than longer red wavelengths.\n"
        "Step 2: Consequence: Colors fail to converge to a single focal point, creating blurry color halos (chromatic aberration)."
    )
    return {
        "id": f"ns7_astro_32_{rng.randint(100000, 999999)}",
        "subskill": "32_refracting_telescopes_lenses_chromatic_aberration",
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
            "tier_1": "Why do prisms split light into rainbows? Different colors bend differently.",
            "tier_2": "Different colors focus at different points through lenses.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["chromatic_aberration_cause_confusion"]
    }


def arch_33_reflecting_telescopes_concave_mirrors_advantages(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Today, all giant professional research telescopes (such as SALT, Keck, and the James Webb Space Telescope) "
        "use mirrors rather than lenses.\n\n"
        "What major engineering and optical advantages do **reflecting telescopes** have over refracting telescopes?"
    )
    correct = "Mirrors have zero chromatic aberration, can be supported solidly from behind so they don't sag, and only one front surface needs polishing."
    options = [
        correct,
        "Mirrors are completely immune to any dust or dirt and never require electricity.",
        "Mirrors allow astronomers to see through solid planets to view their cores.",
        "Mirrors make light travel at ten times its normal cosmic speed."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Optical advantage:\n"
        "Law of reflection applies equally to all wavelengths: zero chromatic aberration.\n"
        "Step 2: Engineering advantage:\n"
        "Lenses must be supported only at the thin rim and sag under gravity if made larger than ~1 meter. Mirrors can be supported across their entire back structure."
    )
    return {
        "id": f"ns7_astro_33_{rng.randint(100000, 999999)}",
        "subskill": "33_reflecting_telescopes_concave_mirrors_advantages",
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
            "tier_1": "Can giant mirrors be supported from the back? Do they suffer from rainbow halos?",
            "tier_2": "Zero chromatic aberration and full structural support from behind.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mirror_vs_lens_telescope_advantages"]
    }


def arch_34_optical_vs_radio_telescopes_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Astronomers divide astronomical instruments into optical telescopes and radio telescopes.\n\n"
        "How do **radio telescopes** differ fundamentally in design and function from optical telescopes?"
    )
    correct = "Radio telescopes use large curved metallic dish antennas and electronic receivers to detect invisible long-wavelength radio waves emitted by cosmic sources."
    options = [
        correct,
        "Radio telescopes broadcast FM music stations directly into alien galaxies.",
        "Radio telescopes only work if an astronomer looks through a glass eyepiece.",
        "Radio telescopes can only operate during the daylight hours when clouds are thick."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Wavelength comparison:\n"
        "- Optical telescopes detect visible light (wavelengths 400-700 nanometres).\n"
        "- Radio telescopes detect radio waves (millimetres to metres in wavelength).\n"
        "Step 2: Construction:\n"
        "Radio telescopes use large parabolic metal dishes or dipole antennae connected to sensitive cryogenic radio receivers."
    )
    return {
        "id": f"ns7_astro_34_{rng.randint(100000, 999999)}",
        "subskill": "34_optical_vs_radio_telescopes_comparison",
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
            "tier_1": "Do radio telescopes look at visible light or listen to/detect radio waves?",
            "tier_2": "Metal dishes detecting invisible radio wavelengths.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["radio_telescope_audio_broadcast_fallacy"]
    }


def arch_35_radio_astronomy_history_karl_jansky(rng: random.Random) -> Dict[str, Any]:
    year = "1931"
    prompt = (
        f"In {year}, American engineer **Karl Jansky** at Bell Telephone Laboratories investigated background static hiss "
        "interfering with trans-Atlantic voice radio transmissions.\n\n"
        "What historic cosmic discovery did Jansky make that birthed the field of radio astronomy?"
    )
    correct = "The steady radio hiss was originating from the centre of our Milky Way galaxy in the constellation Sagittarius."
    options = [
        correct,
        "The static was coming from extraterrestrial radio broadcasts on Mars.",
        "The static proved that Earth's atmosphere was leaking into the Moon.",
        "The hiss was caused by radio signals bounced off the Antarctic ice sheet."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Jansky's experiment:\n"
        "Jansky built a rotating antenna array to locate sources of radio interference.\n"
        "Step 2: Cosmic origin:\n"
        "He found the static peaked every 23 hours and 56 minutes (a sidereal day), proving it tracked with the stars and originated from Sagittarius at the Milky Way's core."
    )
    return {
        "id": f"ns7_astro_35_{rng.randint(100000, 999999)}",
        "subskill": "35_radio_astronomy_history_karl_jansky",
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
            "tier_1": "Where did the mysterious radio hiss come from? Space.",
            "tier_2": "From the center of the Milky Way galaxy.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["birth_of_radio_astronomy_error"]
    }


def arch_36_radio_waves_penetrating_interstellar_dust(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Dense clouds of interstellar gas and cosmic dust completely block visible optical light "
        "from the centre of the Milky Way galaxy.\n\n"
        "Why are radio telescopes able to reveal galaxies, black holes, and star birth hidden behind these dense dust clouds?"
    )
    correct = "Radio waves have much longer wavelengths than visible light, allowing them to pass through interstellar dust particles without being scattered or absorbed."
    options = [
        correct,
        "Radio waves burn through dust clouds with high-powered atomic lasers.",
        "Radio waves are made of heavy iron atoms that push dust grains aside.",
        "Cosmic dust clouds only exist during nighttime and vanish by day."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Wavelength vs particle size relationship:\n"
        "Dust particles are roughly the same size as optical wavelengths (~0.5 micrometres), so they scatter visible light strongly (Rayleigh scattering).\n"
        "Step 2: Radio wave penetration:\n"
        "Radio waves have wavelengths of centimetres to metres—far larger than interstellar dust grains. They pass through unhindered, allowing astronomers to see through the cosmic dust."
    )
    return {
        "id": f"ns7_astro_36_{rng.randint(100000, 999999)}",
        "subskill": "36_radio_waves_penetrating_interstellar_dust",
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
            "tier_1": "Are radio wavelengths much longer than visible light?",
            "tier_2": "Long wavelengths pass easily through microscopic dust particles.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["radio_wave_dust_penetration_mechanism"]
    }


def arch_37_south_african_astronomy_heritage_royal_observatory(rng: random.Random) -> Dict[str, Any]:
    year = "1820"
    prompt = (
        f"In {year}, the **Royal Observatory, Cape of Good Hope** was established in Cape Town "
        "(now the headquarters of the South African Astronomical Observatory - SAAO).\n\n"
        "What was the original 19th-century scientific purpose of establishing this observatory in South Africa?"
    )
    correct = "Mapping the uncharted Southern Hemisphere stars to provide accurate navigational stellar charts and precise time signals for passing trading ships."
    options = [
        correct,
        "Building launch rockets to send satellites into orbit around Mars.",
        "Monitoring solar storms to protect city smartphone networks.",
        "Mining precious minerals discovered on fallen meteorites."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical context (1820):\n"
        "Maritime trade routes rounded the Cape of Good Hope.\n"
        "Step 2: Navigational mission:\n"
        "The Royal Observatory surveyed the southern sky, measured accurate star coordinates, and fired the Noon Gun to allow ships in Table Bay to calibrate their marine chronometers."
    )
    return {
        "id": f"ns7_astro_37_{rng.randint(100000, 999999)}",
        "subskill": "37_south_african_astronomy_heritage_royal_observatory",
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
            "tier_1": "What did sailing ships need in 1820 to navigate around the Cape?",
            "tier_2": "Accurate southern star charts and maritime time signals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sa_astronomy_heritage_purpose"]
    }


def arch_38_sutherland_karoo_ideal_astronomical_site(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the 1970s, major optical astronomical research was moved away from Cape Town to a remote plateau near **Sutherland in the Great Karoo**.\n\n"
        "Why is Sutherland considered one of the finest astronomical observatory locations on planet Earth?"
    )
    correct = "It has exceptionally dark skies with zero urban light pollution, dry semi-desert air (low humidity), high altitude, and over 300 cloudless nights per year."
    options = [
        correct,
        "It is located directly on the Equator where gravity is zero.",
        "It is surrounded by ocean water that cools the telescope mirrors with seawater.",
        "It is the only place on Earth where the Sun never shines."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric criteria for optical astronomy:\n"
        "- Dark skies: Minimum artificial light pollution.\n"
        "- Clear weather: High number of cloud-free nights.\n"
        "- Dry air: Low moisture reduces infrared absorption.\n"
        "- Stable air: Low atmospheric turbulence ('seeing').\n"
        "Step 2: Conclusion: The Karoo plateau near Sutherland satisfies all these conditions brilliantly."
    )
    return {
        "id": f"ns7_astro_38_{rng.randint(100000, 999999)}",
        "subskill": "38_sutherland_karoo_ideal_astronomical_site",
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
            "tier_1": "What ruins astronomical observations? City lights, clouds, and humidity.",
            "tier_2": "Sutherland has dark skies, high altitude, and dry clear weather.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["observatory_site_selection_criteria"]
    }


def arch_39_south_african_large_telescope_salt_specifications(rng: random.Random) -> Dict[str, Any]:
    diam = "11 metres"
    prompt = (
        f"The **Southern African Large Telescope (SALT)** at Sutherland is the single largest optical telescope in the entire Southern Hemisphere, "
        f"with a primary mirror array measuring approximately {diam} across.\n\n"
        "How much fainter can SALT detect celestial objects compared to the naked human eye?"
    )
    correct = "About a billion times fainter (capable of detecting a candle flame on the Moon)."
    options = [
        correct,
        "About two times fainter.",
        "SALT can only see objects that are brighter than the Full Moon.",
        "SALT cannot see faint objects because it only works with FM radio."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Light-gathering power:\n"
        "Light-gathering power is proportional to the area of the primary mirror (D²).\n"
        "Step 2: Magnitude of SALT:\n"
        "With an 11-metre aperture, SALT gathers enormous amounts of light, detecting distant stars and galaxies up to a billion times fainter than visible to the human eye."
    )
    return {
        "id": f"ns7_astro_39_{rng.randint(100000, 999999)}",
        "subskill": "39_south_african_large_telescope_salt_specifications",
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
            "tier_1": "An 11-metre mirror gathers vast amounts of light.",
            "tier_2": "Detects objects nearly a billion times fainter than the human eye.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["salt_light_gathering_power_error"]
    }


def arch_40_salt_hexagonal_primary_mirror_technology(rng: random.Random) -> Dict[str, Any]:
    n_mirrors = 91
    prompt = (
        f"Instead of casting a single colossal 11-metre glass mirror (which would be impossibly heavy and crack under thermal stress), "
        f"SALT's primary mirror is composed of **{n_mirrors} hexagonal mirror segments** fitted together like a honeycomb.\n\n"
        "How is this segmented mirror controlled so that all 91 segments act as one single optical surface?"
    )
    correct = "Computer-controlled robotic actuators and laser sensors continuously adjust each segment's position to within nanometres."
    options = [
        correct,
        "Astronomers physically climb under the mirror and tighten bolts by hand every five minutes.",
        "Strong magnets pull the glass segments until they melt into a single flat puddle.",
        "The mirrors float on sea water inside a large plastic swimming pool."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Segmented mirror technology:\n"
        "SALT uses 91 hexagonal segments, each 1 metre across.\n"
        "Step 2: Active optics alignment:\n"
        "Edge sensors and motorized computer actuators adjust the tip, tilt, and piston of each mirror segment every few seconds to maintain a perfect optical surface."
    )
    stroke_hex = rng.choice(["#38bdf8", "#0284c7", "#0ea5e9"])
    sw_hex = rng.choice([2, 2.5, 3])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 160" width="100%" height="130"><polygon points="120,20 160,40 160,90 120,110 80,90 80,40" fill="none" stroke="{stroke_hex}" stroke-width="{sw_hex}"/><polygon points="120,40 145,55 145,85 120,100 95,85 95,55" fill="#f8fafc" stroke="#64748b"/><text x="120" y="75" text-anchor="middle" font-size="9" fill="#0f172a">91 Segments</text><text x="120" y="140" text-anchor="middle" font-size="10" fill="#0284c7">Honeycomb Mirror Array (SALT)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_astro_40_{rng.randint(100000, 999999)}",
        "subskill": "40_salt_hexagonal_primary_mirror_technology",
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
            "tier_1": "Can humans turn bolts fast enough to keep 91 mirrors aligned?",
            "tier_2": "Computer-controlled robotic actuators and sensors.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["active_optics_actuator_misunderstanding"]
    }


def arch_41_hartraao_hartbeeshoek_radio_astronomy(rng: random.Random) -> Dict[str, Any]:
    dish_diam = "26 metres"
    prompt = (
        f"Located in Gauteng, the **Hartbeeshoek Radio Astronomy Observatory (HartRAO)** operates a {dish_diam} parabolic dish antenna.\n\n"
        "What major scientific contributions does HartRAO provide to international astronomy and geodesy?"
    )
    correct = "Tracking pulsars, measuring continental tectonic plate movements via VLBI (Very Long Baseline Interferometry), and monitoring satellite orbits."
    options = [
        correct,
        "Broadcasting television commercials to astronauts on the International Space Station.",
        "Generating hydroelectric electricity for Johannesburg.",
        "Refining radioactive uranium for medical hospitals."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: HartRAO's capabilities:\n"
        "Originally built as a NASA deep-space tracking station in 1961, it became a national radio astronomy facility in 1975.\n"
        "Step 2: Global network participation:\n"
        "Using Very Long Baseline Interferometry (VLBI), HartRAO links with global dishes to measure continental drift (centimetres per year) and study pulsating neutron stars (pulsars)."
    )
    return {
        "id": f"ns7_astro_41_{rng.randint(100000, 999999)}",
        "subskill": "41_hartraao_hartbeeshoek_radio_astronomy",
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
            "tier_1": "HartRAO does radio astronomy and geodesy (measuring Earth's plates).",
            "tier_2": "VLBI continental drift measurements and pulsar tracking.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hartraao_mission_profile_error"]
    }


def arch_42_meerkat_radio_telescope_karoo_precursor(rng: random.Random) -> Dict[str, Any]:
    n_dishes = 64
    diam = "13.5 metres"
    prompt = (
        f"In the Karoo astronomy reserve near Carnarvon, South Africa constructed **MeerKAT**, "
        f"an array of {n_dishes} interconnected dish antennas, each {diam} in diameter.\n\n"
        "How do 64 separate dish antennas work together to act as one single super-powerful telescope?"
    )
    correct = "Through interferometry: Supercomputers combine the radio signals from all 64 dishes using precise time delays to create ultra-high-resolution images."
    options = [
        correct,
        "All 64 dishes physically weld together into one giant metal bowl every midnight.",
        "The dishes bounce laser beams off each other to generate electricity.",
        "Each dish records one pixel and technicians assemble the composite data manually."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define interferometry:\n"
        "Interferometry combines signals from multiple separated antennas.\n"
        "Step 2: Virtual aperture:\n"
        "The 64 MeerKAT dishes synthesize the resolving power of a single giant dish spanning up to 8 kilometres in diameter, producing world-leading radio images of the galactic center."
    )
    return {
        "id": f"ns7_astro_42_{rng.randint(100000, 999999)}",
        "subskill": "42_meerkat_radio_telescope_karoo_precursor",
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
            "tier_1": "What process links multiple antennas together mathematically?",
            "tier_2": "Interferometry combining signals with supercomputers.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["interferometry_operation_misconception"]
    }


def arch_43_square_kilometre_array_ska_global_scientific_collaboration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Square Kilometre Array (SKA)** is the most ambitious mega-science project of the 21st century, "
        "co-hosted by South Africa (mid-frequency dishes) and Australia (low-frequency antennae).\n\n"
        "Why is this international project named the 'Square Kilometre Array'?"
    )
    correct = "When completed, the combined total collecting area of all its thousands of antennas will equal approximately one square kilometre (1 000 000 m²)."
    options = [
        correct,
        "The telescope is a single flat square concrete block measuring 1 km on each side.",
        "The telescope can only detect radio signals that travel exactly one kilometre.",
        "The project only costs one million rands to construct."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Origin of the name SKA:\n"
        "The total effective collecting surface area across all dishes and dipole antennas will total 1 square kilometre.\n"
        "Step 2: Sensitivity:\n"
        "This colossal collecting area makes SKA 50 times more sensitive than any previous radio telescope on Earth."
    )
    return {
        "id": f"ns7_astro_43_{rng.randint(100000, 999999)}",
        "subskill": "43_square_kilometre_array_ska_global_scientific_collaboration",
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
            "tier_1": "What does total collecting area add up to?",
            "tier_2": "One square kilometre of total collecting area.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ska_naming_origin_error"]
    }


def arch_44_ska_scientific_goals_cosmic_origins_dark_ages(rng: random.Random) -> Dict[str, Any]:
    goals = [
        ("probing the Cosmic Dawn", "detecting neutral hydrogen emission from the very first stars and galaxies formed after the Big Bang"),
        ("testing Einstein's General Relativity", "observing extreme gravitational physics around supermassive black holes and pulsars"),
        ("investigating cosmic magnetism", "mapping magnetic fields that shaped the evolution of galaxies across billions of years")
    ]
    goal_name, goal_desc = rng.choice(goals)
    prompt = (
        f"One of the primary transformational scientific goals of the SKA is {goal_name} ({goal_desc}).\n\n"
        "Why is South Africa's Karoo region uniquely suited to host this sensitive radio instrument?"
    )
    correct = "The South African Astronomy Geographic Advantage Act protects the Karoo as a radio-quiet reserve, banning cell phone towers and interference."
    options = [
        correct,
        "The Karoo has zero gravity, allowing radio waves to travel at infinite speed.",
        "The Karoo is underwater, which cools radio computer cables.",
        "The Karoo has an artificial glass dome covering the entire province."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The threat of Radio Frequency Interference (RFI):\n"
        "Modern devices (cellphones, Wi-Fi, microwaves, spark plugs) emit radio noise billions of times stronger than faint cosmic whispers.\n"
        "Step 2: Legal protection:\n"
        "South Africa established the Karoo Central Astronomy Advantage Area to legally restrict and eliminate terrestrial radio interference."
    )
    return {
        "id": f"ns7_astro_44_{rng.randint(100000, 999999)}",
        "subskill": "44_ska_scientific_goals_cosmic_origins_dark_ages",
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
            "tier_1": "What disrupts sensitive radio dishes? Radio noise from phones and towers.",
            "tier_2": "The Karoo is a legally protected radio-quiet zone.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["radio_quiet_zone_importance"]
    }


def arch_45_space_telescopes_hubble_avoiding_atmospheric_distortion(rng: random.Random) -> Dict[str, Any]:
    year = "1990"
    prompt = (
        f"In {year}, NASA and ESA launched the **Hubble Space Telescope (HST)** into low Earth orbit above the atmosphere.\n\n"
        "Why do space telescopes produce vastly sharper and clearer images than ground-based telescopes of similar size?"
    )
    correct = "They operate completely above Earth's atmosphere, avoiding atmospheric turbulence (which blurs starlight), air pollution, and weather clouds."
    options = [
        correct,
        "They are closer to distant galaxies by halfway across the universe.",
        "They use nuclear bombs to illuminate the constellations.",
        "They only take black-and-white photos which are always sharper."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric distortion ('seeing'):\n"
        "Earth's turbulent atmosphere causes starlight to flicker and blur ('twinkle').\n"
        "Step 2: Advantage of space telescopes:\n"
        "In space, there is no air turbulence, no cloud cover, and no light pollution, allowing diffraction-limited optical sharpness."
    )
    return {
        "id": f"ns7_astro_45_{rng.randint(100000, 999999)}",
        "subskill": "45_space_telescopes_hubble_avoiding_atmospheric_distortion",
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
            "tier_1": "What blurs starlight when viewing from Earth's ground?",
            "tier_2": "The atmosphere (air turbulence and clouds).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["space_telescope_proximity_fallacy"]
    }


def arch_46_james_webb_space_telescope_infrared_astronomy(rng: random.Random) -> Dict[str, Any]:
    year = "2021"
    prompt = (
        f"Launched on 25 December {year}, the **James Webb Space Telescope (JWST)** operates 1.5 million kilometres from Earth "
        "at the Second Lagrange Point (L2), equipped with a giant gold-coated 6.5-metre primary mirror and a tennis-court-sized sunshield.\n\n"
        "Why is JWST specifically optimized to observe the universe in **infrared light**?"
    )
    correct = "Cosmic expansion has stretched light from the earliest galaxies into the infrared spectrum (cosmological redshift), and infrared penetrates cosmic dust."
    options = [
        correct,
        "Infrared light is the only type of light that can travel through empty space vacuum.",
        "Visible light was permanently banned by international space treaties.",
        "Gold mirrors can only reflect green light and destroy all blue photons."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmological redshift:\n"
        "Because the universe is expanding, light from ancient galaxies emitted 13.5 billion years ago has been stretched from visible/UV wavelengths into infrared.\n"
        "Step 2: Penetrating dust:\n"
        "Infrared cuts through dense star-forming gas clouds, allowing JWST to view the birth of planetary systems."
    )
    return {
        "id": f"ns7_astro_46_{rng.randint(100000, 999999)}",
        "subskill": "46_james_webb_space_telescope_infrared_astronomy",
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
            "tier_1": "What happens to light from the distant universe as space expands? It shifts into infrared.",
            "tier_2": "Infrared reveals redshifted ancient galaxies and pierces dust.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["jwst_infrared_specialization_reason"]
    }


def arch_47_ground_vs_space_based_observatories_tradeoffs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Space telescopes offer crystal-clear views unhindered by the atmosphere, yet countries continue to invest "
        "hundreds of millions of rands building giant ground-based observatories like SALT and the SKA in the Karoo.\n\n"
        "What are the major advantages of ground-based observatories over space telescopes?"
    )
    correct = "Ground telescopes are vastly cheaper to construct, can be made much larger (e.g. 11m to 39m), and are easily upgraded and repaired throughout their operational lives."
    options = [
        correct,
        "Ground telescopes have zero building costs and require no human staff.",
        "Ground telescopes are closer to the stars than orbiting satellites.",
        "Ground telescopes operate completely underwater to avoid daylight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cost and size comparison:\n"
        "Launching a telescope into space costs billions (JWST was ~$10 billion) and limits mirror size to what fits in rocket fairings.\n"
        "Step 2: Maintenance advantage:\n"
        "Ground telescopes like SALT can have their instruments, cameras, and computers upgraded every year, lasting for decades at a fraction of the cost."
    )
    return {
        "id": f"ns7_astro_47_{rng.randint(100000, 999999)}",
        "subskill": "47_ground_vs_space_based_observatories_tradeoffs",
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
            "tier_1": "Can you easily fix a broken instrument on a space satellite?",
            "tier_2": "Ground telescopes are far cheaper, can be much larger, and are easy to upgrade.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ground_vs_space_observatory_economics"]
    }


def arch_48_multispectral_astronomy_visible_radio_xray(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Modern astronomers rarely study celestial objects using only visible light; they combine data across "
        "radio, infrared, optical, ultraviolet, and X-ray wavelengths (multispectral astronomy).\n\n"
        "Why is observing a supernova remnant or galaxy in multiple wavelengths essential for understanding its true nature?"
    )
    correct = "Different wavelengths reveal completely different physical processes (e.g., optical shows stars, radio shows cool gas, and X-rays show superheated shockwaves)."
    options = [
        correct,
        "Astronomers need to create colorful computer wallpapers to sell to television studios.",
        "Radio waves and X-rays cancel each other out to create ordinary white daylight.",
        "All celestial bodies emit exactly the same spectrum of light at all times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Temperature and emission physics:\n"
        "- Cold gas and neutral hydrogen emit radio waves.\n"
        "- Warm dust glows in infrared.\n"
        "- Stars shine in visible light.\n"
        "- Million-degree gas and black hole accretion discs radiate high-energy X-rays.\n"
        "Step 2: Conclusion: Combining all wavelengths gives a complete physical picture."
    )
    return {
        "id": f"ns7_astro_48_{rng.randint(100000, 999999)}",
        "subskill": "48_multispectral_astronomy_visible_radio_xray",
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
            "tier_1": "Do hot gases and cold dust emit the same type of light?",
            "tier_2": "Different wavelengths reveal different temperatures and physical structures.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["multispectral_astronomy_utility_error"]
    }


def arch_49_astronomy_careers_and_stem_skills_south_africa(rng: random.Random) -> Dict[str, Any]:
    careers = [
        ("Astrophysicists", "analyzing spectral data to model the birth of stars and cosmic evolution"),
        ("Radio Frequency (RF) Engineers", "designing cryogenic receivers and low-noise amplifiers for Karoo dish antennas"),
        ("Data Scientists and Software Engineers", "building supercomputing algorithms to process petabytes of streaming SKA data"),
        ("Optomechanical Engineers", "maintaining nanometre-precision robotic alignment of SALT mirror segments")
    ]
    prof, role = rng.choice(careers)
    prompt = (
        f"South Africa's leadership in world-class astronomy (SALT and SKA) has created high-tech careers for professionals such as **{prof}**, who specialize in {role}.\n\n"
        "What core school STEM subjects provide the vital foundation for entering these advanced astronomy and technology careers?"
    )
    correct = "Mathematics and Physical Sciences (incorporating physics, chemistry, and computer science)."
    options = [
        correct,
        "Consumer Studies and Drama exclusively.",
        "Tourism and Hospitality Management exclusively.",
        "Woodworking and Carpentry exclusively."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify foundational disciplines:\n"
        "Modern astronomy is an exact physical science requiring mathematical modeling, physical principles, and high-performance computing.\n"
        "Step 2: Career pathway:\n"
        "Mastery of Mathematics and Physical Sciences at the school level is the prerequisite gateway into university degrees in physics, engineering, and astronomy."
    )
    return {
        "id": f"ns7_astro_49_{rng.randint(100000, 999999)}",
        "subskill": "49_astronomy_careers_and_stem_skills_south_africa",
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
            "tier_1": "Which subjects are essential for science and engineering?",
            "tier_2": "Mathematics and Physical Sciences.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stem_subject_foundation_error"]
    }


def arch_50_astronomy_history_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    misconceptions = [
        ("Misconception: 'Galileo Galilei invented the optical telescope from scratch.'", "Correction: The telescope was invented in 1608 by Dutch spectacle-maker Hans Lippershey; Galileo improved the design and was the first to systematically observe and publish celestial discoveries in 1609-1610."),
        ("Misconception: 'African societies had no astronomical knowledge before Europeans arrived.'", "Correction: Indigenous African societies developed sophisticated astronomical calendar systems based on the Pleiades (Isilimela/Selemela), Venus, the Southern Cross, and constructed megalithic calendar stone circles like Adam's Calendar thousands of years ago."),
        ("Misconception: 'Radio telescopes listen to acoustic sound waves travelling through space.'", "Correction: Sound cannot travel through the vacuum of space; radio telescopes detect invisible electromagnetic radio waves, which are processed by computers into false-color images and spectra."),
        ("Misconception: 'Kepler discovered that planets travel around the Sun in perfect circles.'", "Correction: Kepler's First Law proved that planetary orbits are ellipses with the Sun at one focus, breaking away from the Greek dogma of perfect circles.")
    ]
    misc, corr = rng.choice(misconceptions)
    prompt = (
        f"A learner in a Grade 7 Natural Sciences examination writes the following answer:\n\n"
        f"**{misc}**\n\n"
        "Conduct a diagnostic autopsy of this answer. Which scientific correction accurately identifies and rectifies the historical or scientific error?"
    )
    correct = corr
    distractors = [c for m, c in misconceptions if c != corr]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Diagnostic Evaluation:\n"
        f"{misc}\n\n"
        f"Scientific & Historical Reality:\n"
        f"{corr}"
    )
    return {
        "id": f"ns7_astro_50_{rng.randint(100000, 999999)}",
        "subskill": "50_astronomy_history_comprehensive_diagnostic_autopsy",
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
            "tier_1": "Pinpoint the historical misconception in the student's statement.",
            "tier_2": "Contrast who invented vs who used, or sound vs electromagnetic waves.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["historical_astronomy_diagnostic_error"]
    }
