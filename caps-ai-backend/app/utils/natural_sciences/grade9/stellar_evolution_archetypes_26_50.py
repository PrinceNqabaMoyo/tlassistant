"""Grade 9 Natural Sciences: Term 4 - Birth, Life and Death of a Star Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Birth life and the death of a star.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict


def arch_26_high_mass_star_evolutionary_pathway(rng: random.Random) -> Dict[str, Any]:
    threshold = rng.choice(["8 times the mass of our Sun", "8 to 10 solar masses", "greater than 8 solar masses"])
    prompt = (
        f"Stars with initial masses {threshold} follow a radically different and more violent evolutionary pathway than medium-mass stars like our Sun.\n\n"
        "What is the ultimate sequence of evolutionary stages experienced by such a massive star?"
    )
    correct = "Nebula → Protostar → Massive Main Sequence Star → Red Supergiant → Supernova Explosion → Neutron Star or Black Hole."
    options = [
        correct,
        "Nebula → Protostar → Yellow Dwarf → Red Giant → Planetary Nebula → White Dwarf.",
        "Protostar → White Dwarf → Red Giant → Black Dwarf → Asteroid Belt.",
        "Nebula → Gas Giant Planet → Comet → Meteor Shower → Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: High-mass threshold (>8 M_sun):\n"
        "Because of enormous gravitational pressure, massive stars burn violently hot and fast.\n"
        "Step 2: Sequence:\n"
        "After main sequence, they swell into Red Supergiants, fuse elements up to iron, suffer catastrophic core-collapse in a Supernova, leaving a Neutron Star or Black Hole."
    )
    return {
        "id": f"ns9_star_26_{rng.randint(100000, 999999)}",
        "subskill": "26_high_mass_star_evolutionary_pathway",
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
            "tier_1": "Do massive stars end gently with a planetary nebula or violently with a supernova?",
            "tier_2": "Massive stars end in a catastrophic supernova, leaving a neutron star or black hole.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["massive_star_lifecycle_stages"]
    }


def arch_27_red_supergiant_multishell_fusion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the advanced evolutionary stages of an evolved red supergiant star, the interior resembles the concentric layers of an onion.\n\n"
        "What nuclear reactions occur within these concentric shells surrounding the core?"
    )
    correct = "Multiple concentric burning shells fuse progressively heavier elements inward: hydrogen burning outer shell, followed by helium, carbon, neon, oxygen, and silicon burning shells."
    options = [
        correct,
        "All shells burn pure uranium fuel through nuclear fission.",
        "The shells freeze into solid rock layers of granite and basalt.",
        "The star stops fusing elements completely and fills up with liquid water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Onion-skin shell model:\n"
        "As each core fuel is exhausted, the core contracts, heats, and ignites the next heavier element, while the previous fuel continues burning in a surrounding shell.\n"
        "Step 2: Radial order (outer to inner):\n"
        "H → He → C → Ne → O → Si → inert Iron core."
    )
    return {
        "id": f"ns9_star_27_{rng.randint(100000, 999999)}",
        "subskill": "27_red_supergiant_multishell_fusion",
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
            "tier_1": "Think of an onion: what burns in the different layers?",
            "tier_2": "Concentric shells fuse progressively heavier elements inward, leading down to silicon and iron.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["onion_shell_nucleosynthesis_layers"]
    }


def arch_28_iron_core_nuclear_energy_sink(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Inside an advanced massive star, silicon fusion eventually synthesizes **Iron** (specifically Iron-56) in the central core.\n\n"
        "Why does the accumulation of iron in the core trigger the inevitable death of the star?"
    )
    correct = "Iron has the highest nuclear binding energy per nucleon; fusing iron requires absorbing energy rather than releasing energy, instantly cutting off the outward radiation pressure needed to support the star against gravity."
    options = [
        correct,
        "Iron is radioactive and dissolves all the other atoms into empty space.",
        "Iron turns into rust when exposed to cosmic solar wind.",
        "Iron is magnetic and pulls the star out of its galaxy."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Nuclear binding energy peak:\n"
        "Iron-56 (56Fe) sits at the peak of the binding energy curve.\n"
        "Step 2: Energy sink:\n"
        "For elements lighter than iron, fusion releases energy (exothermic). For iron and heavier elements, fusion is endothermic (absorbs energy). Therefore, fusing iron robs the core of heat and collapses radiation pressure immediately."
    )
    return {
        "id": f"ns9_star_28_{rng.randint(100000, 999999)}",
        "subskill": "28_iron_core_nuclear_energy_sink",
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
            "tier_1": "Does fusing iron release energy or absorb energy?",
            "tier_2": "Fusing iron consumes energy instead of releasing it, causing outward pressure to fail.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["iron_binding_energy_nuclear_sink"]
    }


def arch_29_core_collapse_catastrophic_gravitational_implosion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When the iron core of a massive star exceeds the Chandrasekhar mass limit (about 1.44 times the mass of the Sun), electron degeneracy pressure can no longer withstand the crush of gravity.\n\n"
        "What occurs during the catastrophic **core collapse** phase?"
    )
    correct = "The stellar core implodes inward at roughly a quarter the speed of light in a fraction of a second, crushing electrons and protons together into neutrons."
    options = [
        correct,
        "The core slowly expands over 500 million years into a giant cloud of steam.",
        "The core instantly transforms into a giant diamond that gently bounces into orbit.",
        "The core cools down smoothly into an ice cube without moving."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Sudden collapse timescale:\n"
        "In less than 1 second (a fraction of a second), an iron core with radius ~5 000 km collapses to a radius of ~10–20 km.\n"
        "Step 2: Electron capture:\n"
        "Under extreme pressure: p + e⁻ → n + ν_e. Protons and electrons merge into neutrons, releasing an enormous burst of neutrinos."
    )
    return {
        "id": f"ns9_star_29_{rng.randint(100000, 999999)}",
        "subskill": "29_core_collapse_catastrophic_gravitational_implosion",
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
            "tier_1": "How fast does the core collapse occur?",
            "tier_2": "In a fraction of a second at near light-speed, crushing electrons and protons into neutrons.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["core_collapse_speed_and_electron_capture"]
    }


def arch_30_supernova_type_ii_cosmic_explosion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "As the collapsing infalling outer layers slam into the newly formed incompressible neutron core, a violent shockwave rebounds outward.\n\n"
        "What is this colossal cosmic explosion called, and how bright can it become?"
    )
    correct = "A **Type II Supernova**; for days or weeks, it can shine with the combined luminosity of an entire galaxy containing hundreds of billions of normal stars."
    options = [
        correct,
        "A solar flare; it is slightly brighter than a candle flame on Earth.",
        "A lunar eclipse; it causes the Moon to turn dark red for two hours.",
        "A meteor shower; it produces tiny shooting stars in Earth's atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Rebound shockwave:\n"
        "Infalling gas rebounds off the stiff degenerate core, aided by neutrino energy deposition, creating an outward shockwave.\n"
        "Step 2: Supernova luminosity:\n"
        "The explosion releases ~10⁴⁴ Joules of energy, briefly outshining all stars in its host galaxy combined."
    )
    return {
        "id": f"ns9_star_30_{rng.randint(100000, 999999)}",
        "subskill": "30_supernova_type_ii_cosmic_explosion",
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
            "tier_1": "What is the massive stellar explosion that outshines a whole galaxy?",
            "tier_2": "A Type II Supernova.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["supernova_explosion_luminosity"]
    }


def arch_31_explosive_nucleosynthesis_heavy_elements(rng: random.Random) -> Dict[str, Any]:
    target_elements = rng.choice(["gold, silver, and uranium", "platinum, lead, and gold", "uranium, thorium, and silver"])
    prompt = (
        "Normal stellar core fusion inside living stars cannot produce elements heavier than iron because such reactions absorb energy.\n\n"
        f"Where in the universe were heavy elements like {target_elements} synthesized?"
    )
    correct = "During explosive supernova nucleosynthesis (rapid neutron capture / r-process) and extreme neutron star mergers."
    options = [
        correct,
        "In deep underground diamond mines on Earth through chemical crystallization.",
        "In Earth's oceans through the action of coral reefs and marine algae.",
        "Inside the core of our Sun during normal hydrogen-to-helium fusion."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Endothermic hurdle:\n"
        "Elements beyond iron (atomic number Z > 26) require intense neutron fluxes and surplus energy to form.\n"
        "Step 2: Explosive nucleosynthesis:\n"
        "The extreme energy and neutron density during supernovae and kilonovae (neutron star mergers) force rapid neutron capture (r-process), forging gold, platinum, and uranium."
    )
    return {
        "id": f"ns9_star_31_{rng.randint(100000, 999999)}",
        "subskill": "31_explosive_nucleosynthesis_heavy_elements",
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
            "tier_1": "Where do precious heavy metals like gold and uranium come from?",
            "tier_2": "Supernova explosions and neutron star collisions forge heavy elements.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["supernova_nucleosynthesis_heavy_elements"]
    }


def arch_32_chemical_enrichment_of_interstellar_medium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Renowned astronomer Carl Sagan famously declared that 'we are made of star-stuff' (stardust).\n\n"
        "What scientific process explains how stardust from dying stars led to the existence of rocky planets and human beings?"
    )
    correct = "Supernovae and planetary nebulae blast synthesized carbon, oxygen, nitrogen, calcium, and iron into interstellar gas clouds, which later condense to form new solar systems with rocky planets and living organisms."
    options = [
        correct,
        "Humans were beamed down to Earth by aliens living in the center of the Sun.",
        "Stardust fell directly from the sky as liquid raindrops to create living animals.",
        "Earth was formed by frozen comet ice that melted into rock over three weeks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmic chemical recycling:\n"
        "The primordial universe contained only H and He. All carbon, nitrogen, oxygen, calcium in our bones, and iron in our blood were forged inside ancient stars.\n"
        "Step 2: Enrichment of nebulae:\n"
        "Supernova shockwaves disperse these heavy elements into interstellar space, enriching molecular clouds that later collapse to form second- and third-generation star systems like our Solar System."
    )
    return {
        "id": f"ns9_star_32_{rng.randint(100000, 999999)}",
        "subskill": "32_chemical_enrichment_of_interstellar_medium",
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
            "tier_1": "How did carbon and iron get into our bodies and rocky Earth?",
            "tier_2": "Dying stars dispersed forged elements into space, which formed our solar system.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cosmic_chemical_recycling_stardust"]
    }


def arch_33_neutron_star_formation_and_extreme_density(rng: random.Random) -> Dict[str, Any]:
    diameter_km = rng.choice(["about 20 kilometers", "roughly 15 to 25 kilometers", "approximately 20 km (the size of a city)"])
    prompt = (
        f"If the collapsing core of a supernova has a mass between 1.4 and 3 solar masses, it stabilizes as a **neutron star**.\n\n"
        f"What is the physical size of this neutron star, and how dense is its matter?"
    )
    correct = f"It has a diameter of {diameter_km}, but packs more mass than our Sun; a single sugar-cube-sized volume of neutron star material would weigh approximately 1 billion tonnes on Earth."
    options = [
        correct,
        "It is larger than the Milky Way galaxy and has the density of clouds in the sky.",
        "It is the size of Earth and is completely hollow inside.",
        "It is a liquid ball of water floating in space with the density of milk."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Size:\n"
        f"A neutron star has a radius of only ~10–12 km ({diameter_km} diameter).\n"
        "Step 2: Nuclear density:\n"
        "Density is ~10¹⁴ to 10¹⁵ g/cm³ (comparable to the density of an atomic nucleus). Supported by neutron degeneracy pressure."
    )
    return {
        "id": f"ns9_star_33_{rng.randint(100000, 999999)}",
        "subskill": "33_neutron_star_formation_and_extreme_density",
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
            "tier_1": "Is a neutron star the size of a city or the size of a galaxy?",
            "tier_2": "City-sized (~20 km diameter) and extraordinarily dense (1 billion tonnes per sugar cube).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["neutron_star_size_and_density"]
    }


def arch_34_pulsar_rotating_magnetic_neutron_star(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In 1967, astronomer Jocelyn Bell Burnell discovered a celestial object emitting periodic, rapid radio pulses with clockwork precision.\n\n"
        "What is a **pulsar** in astrophysical reality, and why does it appear to 'pulse'?"
    )
    correct = "A rapidly rotating neutron star with a powerful magnetic field that channels beams of electromagnetic radiation from its magnetic poles; like a cosmic lighthouse, the beam flashes across Earth as the star rotates."
    options = [
        correct,
        "An alien spacecraft sending morse code radio signals to Earth.",
        "A distant planet with flashing lightning storms that cover its surface.",
        "A dying white dwarf that turns its light on and off using nuclear switches."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Nature of a pulsar:\n"
        "Pulsars are magnetized, rapidly spinning neutron stars (conserved angular momentum and magnetic flux).\n"
        "Step 2: Lighthouse mechanism:\n"
        "Radiation beams are emitted along the magnetic poles. Because magnetic and rotational axes are misaligned, the beam sweeps through space like a lighthouse beam, producing periodic pulses observed on Earth."
    )
    return {
        "id": f"ns9_star_34_{rng.randint(100000, 999999)}",
        "subskill": "34_pulsar_rotating_magnetic_neutron_star",
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
            "tier_1": "What spins super fast and acts like a lighthouse in space?",
            "tier_2": "A rapidly spinning magnetized neutron star beaming radiation toward Earth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["pulsar_lighthouse_model"]
    }


def arch_35_black_hole_formation_extreme_core_mass(rng: random.Random) -> Dict[str, Any]:
    core_limit = rng.choice(["about 3 solar masses", "greater than 3 times the mass of the Sun", "roughly 3 M_sun"])
    prompt = (
        f"If the remnant core remaining after a supernova has a mass {core_limit}, neutron degeneracy pressure is overwhelmed by gravity.\n\n"
        "What cosmic object is formed, and why is it termed 'black'?"
    )
    correct = "A **stellar-mass black hole**; its gravitational pull is so immense that the escape velocity exceeds the speed of light, preventing even light photons from escaping."
    options = [
        correct,
        "A black dwarf; it is black because it is coated in charcoal from burnt trees.",
        "A dark cloud of dust that absorbs moonlight over a city.",
        "A black hole; it is black because it has a painted wooden shell."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Tolman-Oppenheimer-Volkoff limit:\n"
        f"Beyond {core_limit}, no known degenerate particle pressure can counter gravitational collapse.\n"
        "Step 2: Definition of black hole:\n"
        "Gravity crushes the core into an infinitely dense singularity. Because escape velocity v_esc > c, no light or radiation can escape, rendering it completely black."
    )
    return {
        "id": f"ns9_star_35_{rng.randint(100000, 999999)}",
        "subskill": "35_black_hole_formation_extreme_core_mass",
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
            "tier_1": "What forms when core mass is too huge for even neutrons to support?",
            "tier_2": "A black hole, where gravity is so strong that even light cannot escape.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["black_hole_formation_escape_velocity"]
    }


def arch_36_event_horizon_and_schwarzschild_radius(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A black hole is bounded by an invisible spherical boundary known as the **event horizon**.\n\n"
        "What is the scientific significance of crossing a black hole's event horizon?"
    )
    correct = "It is the absolute boundary of no return; inside the event horizon, the escape velocity exceeds the speed of light, making escape impossible for any matter, radiation, or information."
    options = [
        correct,
        "It is a hard glass wall that bounces spaceships safely back into space.",
        "It is a portal that transports spaceships into another classroom instantly.",
        "It is a ring of fire that re-ignites the star into a yellow dwarf."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Event horizon definition:\n"
        "The Schwarzschild radius R_s = 2GM/c² defines the boundary where escape velocity equals c.\n"
        "Step 2: Physical implication:\n"
        "Any event or signal inside the horizon can never affect an outside observer; it is the ultimate point of no return in spacetime."
    )
    return {
        "id": f"ns9_star_36_{rng.randint(100000, 999999)}",
        "subskill": "36_event_horizon_and_schwarzschild_radius",
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
            "tier_1": "What is the point of no return around a black hole called?",
            "tier_2": "The event horizon: inside it, escape velocity exceeds light speed.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["event_horizon_point_of_no_return"]
    }


def arch_37_singularity_concept_infinite_density(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "At the mathematical center of a non-rotating black hole according to general relativity lies the **singularity**.\n\n"
        "What characterizes the physical conditions at the gravitational singularity?"
    )
    correct = "All the mass of the collapsed core is crushed into a point of zero volume, resulting in theoretically infinite density and infinite spacetime curvature where current laws of physics break down."
    options = [
        correct,
        "A giant sphere of soft cotton wool floating at zero temperature.",
        "A pool of liquid water where fish and plants can live comfortably.",
        "A hollow vacuum containing zero mass and zero gravity."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Singularity definition:\n"
        "A point in spacetime where gravitational forces compress matter to zero volume.\n"
        "Step 2: Physical breakdown:\n"
        "Density ρ = M / V approaches infinity as V → 0. General relativity predicts infinite curvature, indicating that a quantum theory of gravity is required to explain the true center."
    )
    return {
        "id": f"ns9_star_37_{rng.randint(100000, 999999)}",
        "subskill": "37_singularity_concept_infinite_density",
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
            "tier_1": "What is the point of zero volume and infinite density at the center called?",
            "tier_2": "A singularity, where matter is crushed to infinite density.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gravitational_singularity_properties"]
    }


def arch_38_hertzsprung_russell_diagram_axes_and_structure(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Hertzsprung-Russell (H-R) Diagram** is an indispensable tool used by astrophysicists to classify stars and trace stellar evolution.\n\n"
        "What two primary physical variables are plotted on the axes of an H-R diagram, and what is unusual about the horizontal axis?"
    )
    correct = "Vertical axis: Luminosity (or absolute brightness); Horizontal axis: Surface temperature (or spectral class), with temperature unusually plotted decreasing from left (hot) to right (cool)."
    options = [
        correct,
        "Vertical axis: Distance from Earth; Horizontal axis: Speed of the star.",
        "Vertical axis: Star mass in kilograms; Horizontal axis: Star age in years.",
        "Vertical axis: Number of orbiting planets; Horizontal axis: Number of sunspots."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Vertical axis:\n"
        "Luminosity (relative to the Sun, L/L_sun) or Absolute Magnitude, increasing upwards.\n"
        "Step 2: Horizontal axis:\n"
        "Effective surface temperature (Kelvin) or Spectral Class (O, B, A, F, G, K, M). Plotted inversely: hottest stars (30 000 K) on the left, coolest stars (3 000 K) on the right."
    )
    return {
        "id": f"ns9_star_38_{rng.randint(100000, 999999)}",
        "subskill": "38_hertzsprung_russell_diagram_axes_and_structure",
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
            "tier_1": "What two properties describe a star's brightness and heat?",
            "tier_2": "Luminosity on the vertical axis, and surface temperature decreasing left-to-right on the horizontal axis.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hr_diagram_axis_conventions"]
    }


def arch_39_hr_diagram_main_sequence_diagonal_band(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Across an H-R diagram, roughly 90% of all observed stars fall along a prominent diagonal band known as the **main sequence**.\n\n"
        "From where to where does this main sequence band run, and what does it tell us about stars situated along it?"
    )
    correct = "It extends diagonally from the top-left (hot, bright, massive blue giants) to the bottom-right (cool, dim, low-mass red dwarfs); all stars on it are stably fusing hydrogen into helium in their cores."
    options = [
        correct,
        "It runs horizontally along the bottom, representing dead stars made of frozen nitrogen.",
        "It forms a vertical ring in the exact center, representing stars that have exploded.",
        "It extends from top-right to bottom-left, representing stars that burn iron into uranium."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Diagonal orientation:\n"
        "Top-left: high temperature (~30 000 K), high luminosity (~10⁴–10⁵ L_sun) -> massive stars.\n"
        "Bottom-right: low temperature (~3 000 K), low luminosity (~10⁻³ L_sun) -> red dwarfs.\n"
        "Step 2: Physical meaning:\n"
        "Represents core hydrogen fusion in hydrostatic equilibrium."
    )
    return {
        "id": f"ns9_star_39_{rng.randint(100000, 999999)}",
        "subskill": "39_hr_diagram_main_sequence_diagonal_band",
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
            "tier_1": "Where are hot/bright stars and cool/dim stars located on the H-R diagram?",
            "tier_2": "Top-left (hot and bright) down to bottom-right (cool and dim).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hr_diagram_main_sequence_location"]
    }


def arch_40_hr_diagram_giant_and_supergiant_regions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On an H-R diagram, the upper right section contains stars that have relatively low surface temperatures (3 000 K to 4 000 K) yet possess enormous luminosities (thousands of times brighter than our Sun).\n\n"
        "Which classification of stars occupies this upper right region, and why are they so luminous despite having cool surfaces?"
    )
    correct = "Red Giants and Red Supergiants; they are extremely luminous because their physical surface area has expanded to colossal dimensions, radiating immense total power."
    options = [
        correct,
        "White dwarfs; they are luminous because they are tiny and packed with diamonds.",
        "Protostars; they are luminous because they have no gravity.",
        "Neutron stars; they are luminous because they spin at light speed."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stefan-Boltzmann radiation law:\n"
        "Total luminosity L = 4π R² σ T⁴.\n"
        "Step 2: Physical deduction:\n"
        "Even though surface temperature T is relatively low (red, ~3 500 K), their radiating radius R is hundreds of times larger than the Sun's, yielding astronomical total luminosities."
    )
    return {
        "id": f"ns9_star_40_{rng.randint(100000, 999999)}",
        "subskill": "40_hr_diagram_giant_and_supergiant_regions",
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
            "tier_1": "What cool, red stars are huge in size and located in the upper right?",
            "tier_2": "Red Giants and Supergiants: cool surface but huge size makes them luminous.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hr_diagram_giants_radius_luminosity"]
    }


def arch_41_hr_diagram_white_dwarf_region(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On an H-R diagram, the lower left section is occupied by stars that have exceptionally high surface temperatures (10 000 K to 25 000 K) but very low overall luminosities (less than 1% of the Sun).\n\n"
        "Which class of stars resides in this lower left region, and why is their luminosity so low despite their blazing heat?"
    )
    correct = "White dwarfs; their luminosity is very low because their physical surface area is tiny (roughly Earth-sized), so they emit very little total radiant energy."
    options = [
        correct,
        "Red supergiants; they are low luminosity because they are hidden behind dust.",
        "Main sequence blue giants; they are low luminosity because they have run out of gravity.",
        "Black holes; they are low luminosity because they are made of dark matter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Lower left quadrant properties:\n"
        "High temperature (bluish-white) + Low luminosity.\n"
        "Step 2: Stefan-Boltzmann explanation:\n"
        "L = 4π R² σ T⁴. High T is offset by tiny radius R (Earth-sized ~6 000 km), resulting in very low total luminosity."
    )
    return {
        "id": f"ns9_star_41_{rng.randint(100000, 999999)}",
        "subskill": "41_hr_diagram_white_dwarf_region",
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
            "tier_1": "What small, hot, dim remnants sit in the bottom left of the H-R diagram?",
            "tier_2": "White dwarfs: very hot surface, but tiny Earth-sized area means low total brightness.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hr_diagram_white_dwarfs_location"]
    }


def arch_42_sun_position_and_future_track_on_hr_diagram(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Where is our Sun currently situated in Hertzsprung-Russell stellar classifications, and how will its classification shift over the next 5 billion years as it evolves?"
    )
    correct = "The Sun is currently near the center of the Main Sequence (luminosity 1, temperature ~5 800 K); in 5 billion years it will move into the Red Giant region, before eventually settling into the White Dwarf cooling region."
    options = [
        correct,
        "The Sun is currently in the Black Hole region and will move into the Protostar region.",
        "The Sun is currently in the Red Supergiant region and will explode as a Type II Supernova.",
        "The Sun will never change its classification because its stellar properties are fixed permanently."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Current position:\n"
        "Main sequence: G2V yellow dwarf (L = 1 L_sun, T_eff ≈ 5 778 K).\n"
        "Step 2: Evolutionary track:\n"
        "Main Sequence → Red Giant Branch (moves up and right: brighter, cooler) → Horizontal Branch / AGB → Planetary Nebula ejection → White Dwarf (moves down and left: dim, hot) → cooling track."
    )
    return {
        "id": f"ns9_star_42_{rng.randint(100000, 999999)}",
        "subskill": "42_sun_position_and_future_track_on_hr_diagram",
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
            "tier_1": "Where does the Sun start, expand to, and end up as a remnant?",
            "tier_2": "Main sequence center → Red Giant (up-right) → White Dwarf (down-left).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sun_evolutionary_track_hr_diagram"]
    }


def arch_43_stellar_magnitude_apparent_vs_absolute(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When studying the night sky, astronomers distinguish between a star's **apparent magnitude** and its **absolute magnitude**.\n\n"
        "What is the fundamental scientific difference between these two measurements?"
    )
    correct = "Apparent magnitude measures how bright a star appears from Earth (affected by distance), while absolute magnitude measures the true, intrinsic brightness of a star if placed at a standard distance of 10 parsecs (approx. 32.6 light years)."
    options = [
        correct,
        "Apparent magnitude is measured in kilograms, while absolute magnitude is measured in meters.",
        "Apparent magnitude applies only to planets, while absolute magnitude applies only to moons.",
        "Both measurements are 100% identical and cannot be differentiated."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Apparent magnitude (m):\n"
        "Observed flux reaching Earth detectors. A nearby dim star can have a brighter apparent magnitude than a distant supergiant.\n"
        "Step 2: Absolute magnitude (M):\n"
        "Intrinsic luminosity calibrated to standard distance d = 10 parsecs (32.6 ly), removing distance bias via the inverse square law."
    )
    return {
        "id": f"ns9_star_43_{rng.randint(100000, 999999)}",
        "subskill": "43_stellar_magnitude_apparent_vs_absolute",
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
            "tier_1": "Which magnitude depends on how far away the star is from Earth?",
            "tier_2": "Apparent is how bright it looks from Earth; Absolute is intrinsic brightness at a standard distance.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["apparent_vs_absolute_magnitude"]
    }


def arch_44_spectral_classification_obafgkm_sequence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Astronomers classify stars into spectral classes using the canonical sequence: **O, B, A, F, G, K, M**.\n\n"
        "In what order are stars arranged along this sequence, and which spectral class corresponds to the hottest stars?"
    )
    correct = "The sequence is arranged in order of decreasing surface temperature from hottest (O stars, over 30 000 K) to coolest (M stars, under 3 500 K)."
    options = [
        correct,
        "The sequence is arranged alphabetically by distance from our Moon.",
        "M stars are the hottest (1 million K) and O stars are the coldest (0 K).",
        "The sequence represents the number of moons orbiting each star from 1 to 7."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical sequence:\n"
        "Harvard spectral classification: O B A F G K M (mnemonic: 'Oh Be A Fine Girl/Guy, Kiss Me').\n"
        "Step 2: Temperature correlation:\n"
        "Class O: >30 000 K (blue)\n"
        "Class B: 10 000–30 000 K (blue-white)\n"
        "Class A: 7 500–10 000 K (white)\n"
        "Class F: 6 000–7 500 K (yellow-white)\n"
        "Class G: 5 200–6 000 K (yellow, e.g. Sun G2V)\n"
        "Class K: 3 700–5 200 K (orange)\n"
        "Class M: 2 400–3 700 K (red)."
    )
    return {
        "id": f"ns9_star_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spectral_classification_obafgkm_sequence",
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
            "tier_1": "Which letter comes first: O or M, and is it the hottest or coolest?",
            "tier_2": "O is hottest (>30 000 K), decreasing down to M which is coolest (<3 500 K).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["obafgkm_spectral_sequence_order"]
    }


def arch_45_parallax_and_astronomical_distance_measurement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "To measure the distance to nearby stars, astronomers observe how a star appears to shift position relative to distant background stars over a six-month interval.\n\n"
        "What geometric method is being used, and what serves as the baseline for this measurement?"
    )
    correct = "Stellar parallax; the baseline is the diameter of Earth's orbit around the Sun (approx. 300 million km or 2 Astronomical Units)."
    options = [
        correct,
        "Radar echo reflection off the star's surface.",
        "Measuring the time it takes for a space probe to fly to the star.",
        "Counting the number of sunspots with a magnifying glass."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stellar parallax definition:\n"
        "The apparent angular shift of a nearby object when viewed from two different vantage points.\n"
        "Step 2: Baseline:\n"
        "Earth's orbit around the Sun provides a 2 AU baseline (~300 million km) when observations are taken 6 months apart. Parallax angle p yields distance: d = 1/p (in parsecs)."
    )
    return {
        "id": f"ns9_star_45_{rng.randint(100000, 999999)}",
        "subskill": "45_parallax_and_astronomical_distance_measurement",
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
            "tier_1": "What triangulation method uses Earth's orbit as a baseline?",
            "tier_2": "Stellar parallax, using Earth's 2 AU orbital baseline.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stellar_parallax_baseline"]
    }


def arch_46_nuclear_fusion_mass_deficit_einstein_relation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Inside a star, when four hydrogen protons fuse into one helium-4 nucleus, the mass of the resulting helium nucleus is approximately 0.7% less than the combined mass of the original four protons.\n\n"
        "What famous scientific equation governs how this missing mass is converted into the radiant energy that lights up the star?"
    )
    correct = "E = mc² (Energy equals mass deficit multiplied by the speed of light squared)."
    options = [
        correct,
        "F = ma (Force equals mass times acceleration).",
        "P = V · I (Power equals voltage times current).",
        "v = f · λ (Velocity equals frequency times wavelength)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mass-energy equivalence:\n"
        "Albert Einstein (1905) established that mass and energy are interconvertible.\n"
        "Step 2: Formula and magnitude:\n"
        "E = Δm · c². Because c² ≈ (3 × 10⁸ m/s)² = 9 × 10¹⁶ m²/s² is an astronomical number, converting even a microscopic mass deficit yields enormous energetic output."
    )
    return {
        "id": f"ns9_star_46_{rng.randint(100000, 999999)}",
        "subskill": "46_nuclear_fusion_mass_deficit_einstein_relation",
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
            "tier_1": "What is Einstein's most famous equation relating energy and mass?",
            "tier_2": "E = mc².",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["einstein_mass_energy_equivalence"]
    }


def arch_47_solar_radiation_pressure_and_coronal_mass_ejection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Active stars experience energetic phenomena in their outer atmospheres, including solar flares and **coronal mass ejections (CMEs)**.\n\n"
        "What are coronal mass ejections, and how can they impact technological infrastructure on Earth?"
    )
    correct = "Colossal bubbles of magnetized plasma ejected from the stellar corona; when striking Earth's magnetosphere, they induce geomagnetic storms that can disrupt electrical power grids, GPS satellite signals, and radio communications."
    options = [
        correct,
        "Streams of cool water droplets that wash clean solar panels on satellites.",
        "Frozen clouds of dry ice that cause the Earth's oceans to freeze solid.",
        "Radio signals sent by aliens to control traffic lights on highways."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: CME definition:\n"
        "Massive expulsions of magnetized plasma (billions of tonnes of protons and electrons) from the solar corona.\n"
        "Step 2: Terrestrial impacts:\n"
        "Interactions with Earth's geomagnetic field cause geomagnetic storms, auroras, induce geomagnetically induced currents (GIC) in power transformers, and disrupt satellite electronics."
    )
    return {
        "id": f"ns9_star_47_{rng.randint(100000, 999999)}",
        "subskill": "47_solar_radiation_pressure_and_coronal_mass_ejection",
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
            "tier_1": "What happens when magnetized plasma from the Sun hits Earth's magnetic field?",
            "tier_2": "It triggers geomagnetic storms that can disrupt satellites and power grids.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cme_space_weather_impacts"]
    }


def arch_48_salt_sutherland_astronomical_observatory(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Located on a plateau near Sutherland in the Karoo region of the Northern Cape, South Africa operates **SALT** (the Southern African Large Telescope).\n\n"
        "What makes SALT a world-class optical instrument for investigating stellar evolution, and why was Sutherland chosen as its location?"
    )
    correct = "SALT is the largest single optical telescope in the Southern Hemisphere (11-meter primary mirror); Sutherland was selected for its cloudless skies, high altitude, dry semi-desert climate, and absence of urban light pollution."
    options = [
        correct,
        "SALT is a submarine periscope used to track underwater whales in the Atlantic Ocean.",
        "Sutherland was chosen because it rains every day, keeping the telescope mirrors washed clean.",
        "SALT is an underground particle accelerator designed to detect coal seams."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Telescope specifications:\n"
        "SALT possesses an 11.1 × 9.8 meter hexagonal array composed of 91 segmented mirrors, making it the Southern Hemisphere's largest optical telescope.\n"
        "Step 2: Astronomical location advantages:\n"
        "Sutherland (Karoo plateau, 1 798 m altitude) features exceptionally dark skies (low light pollution), low atmospheric humidity, and high annual percentage of clear photometric nights."
    )
    return {
        "id": f"ns9_star_48_{rng.randint(100000, 999999)}",
        "subskill": "48_salt_sutherland_astronomical_observatory",
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
            "tier_1": "What kind of telescope is SALT in Sutherland and why is the Karoo ideal?",
            "tier_2": "The largest optical telescope in the Southern Hemisphere; Sutherland has dark, dry, clear skies.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["salt_optical_astronomy_sutherland"]
    }


def arch_49_meerkat_and_ska_radio_astronomy_in_karoo(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the semi-desert Karoo near Carnarvon, South Africa hosts the 64-dish **MeerKAT** radio telescope, a precursor to the global **Square Kilometre Array (SKA)**.\n\n"
        "How does radio astronomy differ from optical astronomy, and what stellar phenomena do radio telescopes excel at observing?"
    )
    correct = "Radio telescopes detect invisible long-wavelength electromagnetic radio waves rather than visible light; they can penetrate interstellar dust clouds to observe protostars, pulsar radio beams, and cold neutral hydrogen gas."
    options = [
        correct,
        "Radio telescopes broadcast commercial FM music to astronauts living on Mars.",
        "Radio telescopes use sound waves traveling through the air to hear star explosions.",
        "Radio telescopes only work during the daytime and shut down completely at night."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Wavelength spectrum:\n"
        "Radio waves have long wavelengths (millimeters to meters), enabling them to pass through dense interstellar dust lanes that block visible light.\n"
        "Step 2: Astronomical utility:\n"
        "MeerKAT and SKA map the 21-cm hydrogen line, discover rapidly spinning pulsars, study magnetic fields, and peer into active galactic nuclei."
    )
    return {
        "id": f"ns9_star_49_{rng.randint(100000, 999999)}",
        "subskill": "49_meerkat_and_ska_radio_astronomy_in_karoo",
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
            "tier_1": "What kind of waves do MeerKAT and SKA detect?",
            "tier_2": "Radio waves, which penetrate thick cosmic dust to reveal pulsars and star birth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["radio_astronomy_meerkat_ska_capabilities"]
    }


def arch_50_cosmic_recycling_and_stellar_generations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Over cosmic time, each generation of stars is born from nebulae enriched by the death products of previous generations.\n\n"
        "How does our Sun's chemical composition (as a Population I star) prove that it is at least a second- or third-generation star?"
    )
    correct = "Our Sun contains approximately 1.5% to 2% 'metals' (elements heavier than helium, such as carbon, iron, and silicon); since the early universe contained almost solely hydrogen and helium, these heavy elements could only have been manufactured by earlier generations of dying stars."
    options = [
        correct,
        "Our Sun is made entirely of pure uranium, which only forms in the Big Bang.",
        "Our Sun has zero heavy elements and is 100% pure primordial hydrogen.",
        "Our Sun has a ring of iron armor forged by extraterrestrial astronauts."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Primordial nucleosynthesis:\n"
        "The Big Bang produced only H (~75%), He (~25%), and trace Li. Zero carbon, oxygen, or iron existed.\n"
        "Step 2: Stellar generational enrichment:\n"
        "Population III (first stars, metal-free) → Population II (metal-poor) → Population I (metal-rich like the Sun, with ~2% heavy elements). This metallicity confirms our Sun condensed from an enriched nebula formed by previous supernovae."
    )
    return {
        "id": f"ns9_star_50_{rng.randint(100000, 999999)}",
        "subskill": "50_cosmic_recycling_and_stellar_generations",
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
            "tier_1": "Where did the heavy elements in our Sun come from?",
            "tier_2": "From previous generations of stars that exploded and enriched the birth cloud.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stellar_population_metallicity_recycling"]
    }


BUILDERS_26_50 = {
    "26_high_mass_star_evolutionary_pathway": arch_26_high_mass_star_evolutionary_pathway,
    "27_red_supergiant_multishell_fusion": arch_27_red_supergiant_multishell_fusion,
    "28_iron_core_nuclear_energy_sink": arch_28_iron_core_nuclear_energy_sink,
    "29_core_collapse_catastrophic_gravitational_implosion": arch_29_core_collapse_catastrophic_gravitational_implosion,
    "30_supernova_type_ii_cosmic_explosion": arch_30_supernova_type_ii_cosmic_explosion,
    "31_explosive_nucleosynthesis_heavy_elements": arch_31_explosive_nucleosynthesis_heavy_elements,
    "32_chemical_enrichment_of_interstellar_medium": arch_32_chemical_enrichment_of_interstellar_medium,
    "33_neutron_star_formation_and_extreme_density": arch_33_neutron_star_formation_and_extreme_density,
    "34_pulsar_rotating_magnetic_neutron_star": arch_34_pulsar_rotating_magnetic_neutron_star,
    "35_black_hole_formation_extreme_core_mass": arch_35_black_hole_formation_extreme_core_mass,
    "36_event_horizon_and_schwarzschild_radius": arch_36_event_horizon_and_schwarzschild_radius,
    "37_singularity_concept_infinite_density": arch_37_singularity_concept_infinite_density,
    "38_hertzsprung_russell_diagram_axes_and_structure": arch_38_hertzsprung_russell_diagram_axes_and_structure,
    "39_hr_diagram_main_sequence_diagonal_band": arch_39_hr_diagram_main_sequence_diagonal_band,
    "40_hr_diagram_giant_and_supergiant_regions": arch_40_hr_diagram_giant_and_supergiant_regions,
    "41_hr_diagram_white_dwarf_region": arch_41_hr_diagram_white_dwarf_region,
    "42_sun_position_and_future_track_on_hr_diagram": arch_42_sun_position_and_future_track_on_hr_diagram,
    "43_stellar_magnitude_apparent_vs_absolute": arch_43_stellar_magnitude_apparent_vs_absolute,
    "44_spectral_classification_obafgkm_sequence": arch_44_spectral_classification_obafgkm_sequence,
    "45_parallax_and_astronomical_distance_measurement": arch_45_parallax_and_astronomical_distance_measurement,
    "46_nuclear_fusion_mass_deficit_einstein_relation": arch_46_nuclear_fusion_mass_deficit_einstein_relation,
    "47_solar_radiation_pressure_and_coronal_mass_ejection": arch_47_solar_radiation_pressure_and_coronal_mass_ejection,
    "48_salt_sutherland_astronomical_observatory": arch_48_salt_sutherland_astronomical_observatory,
    "49_meerkat_and_ska_radio_astronomy_in_karoo": arch_49_meerkat_and_ska_radio_astronomy_in_karoo,
    "50_cosmic_recycling_and_stellar_generations": arch_50_cosmic_recycling_and_stellar_generations,
}
