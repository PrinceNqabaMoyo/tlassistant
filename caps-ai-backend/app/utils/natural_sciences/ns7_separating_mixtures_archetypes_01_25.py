"""
Grade 7 Natural Sciences - Term 2: Separating Mixtures (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/PDF - Separating mixtures.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Concepts & Types of Mixtures (01 - 09)
# ==============================================================================

def arch_01_mixture_definition_physical_combination(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("table salt dissolved in warm tap water", "salt and water", "no chemical reaction occurs; water can be evaporated to get salt back"),
        ("sand mixed with dry iron filings", "sand and iron", "particles sit side-by-side without chemical bonds; a magnet can separate iron"),
        ("peanuts and dried raisins in trail mix", "peanuts and raisins", "components retain their individual flavours and physical properties"),
    ]
    mix_desc, components, reason = rng.choice(examples)

    prompt = (
        f"Consider the substance combination: **{mix_desc}**.\n\n"
        f"1. Explain why this combination is classified as a **mixture** rather than a pure chemical compound.\n"
        f"2. State whether a chemical reaction is required to separate the components."
    )
    sol = (
        f"**Step 1:** It is a mixture because two or more substances ({components}) are physically combined without forming chemical bonds ({reason}) [1 Mark: Definition].\n\n"
        f"**Step 2:** **No chemical reaction** is required; the components can be separated purely by physical separation methods [1 Mark: Physical separation]."
    )
    return {
        "id": f"ns7_sep_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Physically combined without chemical bonds; no chemical reaction required (separated physically)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "01_mixture_definition_physical_combination",
        "misconception_tags": ["mixture_vs_compound"],
        "hints": {
            "tier_1": "Are the substances chemically bonded together or just mixed?",
            "tier_2": "In a mixture, substances keep their own properties and can be separated physically.",
            "tier_3": "Physically combined without chemical bonds; can be separated by physical methods."
        }
    }


def arch_02_types_of_mixtures_solid_solid(rng: random.Random) -> Dict[str, Any]:
    mixtures = [
        ("garden soil", ["sand grains", "clay particles", "decayed organic humus", "small pebbles"]),
        ("granite rock", ["quartz crystals", "feldspar", "biotite mica"]),
        ("beach sand and broken seashells", ["silica sand grains", "calcium carbonate shell fragments"]),
    ]
    name, parts = rng.choice(mixtures)

    prompt = (
        f"A sample of **{name}** consists of {', '.join(parts)}.\n\n"
        f"1. Identify the states of matter of the components in this mixture.\n"
        f"2. Explain why {name} is called a **heterogeneous** mixture."
    )
    sol = (
        f"**Step 1:** All components are in the **solid state** (it is a solid-solid mixture) [1 Mark: State of matter].\n\n"
        f"**Step 2:** It is heterogeneous because the different components are not uniformly distributed and individual particles/phases can be visibly distinguished [1 Mark: Heterogeneous definition]."
    )
    return {
        "id": f"ns7_sep_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Solid-solid mixture; components are not uniformly mixed and distinct parts can be seen",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "02_types_of_mixtures_solid_solid",
        "misconception_tags": ["heterogeneous_vs_homogeneous"],
        "hints": {
            "tier_1": "Are these components solids, liquids, or gases?",
            "tier_2": "All components are solids, and you can see the different parts.",
            "tier_3": "Solid-solid mixture; heterogeneous because components are visibly non-uniform."
        }
    }


def arch_03_suspension_definition_and_properties(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("powdered chalk stirred vigorously into a beaker of cold water", "chalk"),
        ("red clay powder stirred into a cylinder of water", "clay"),
        ("fine flour mixed with cold water", "flour"),
    ]
    desc, solid_name = rng.choice(examples)

    prompt = (
        f"A learner prepares a mixture by shaking {desc}.\n\n"
        f"1. Name this type of mixture (**solution** or **suspension**).\n"
        f"2. Describe the optical clarity of the mixture immediately after shaking (clear or opaque).\n"
        f"3. What will happen to the {solid_name} particles if the beaker is left standing undisturbed on a bench for 2 hours?"
    )
    sol = (
        f"**Step 1:** This mixture is a **suspension** [1 Mark: Classification].\n\n"
        f"**Step 2:** It is **opaque (cloudy)** because the suspended solid particles scatter light passing through the liquid [1 Mark: Optical property].\n\n"
        f"**Step 3:** Over time, gravity pulls the suspended {solid_name} particles down, causing them to **settle to the bottom as sediment** [1 Mark: Sedimentation]."
    )
    return {
        "id": f"ns7_sep_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Suspension; opaque / cloudy; particles settle to bottom as sediment",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_suspension_definition_and_properties",
        "misconception_tags": ["suspension_vs_solution"],
        "hints": {
            "tier_1": "Does chalk/clay dissolve in water?",
            "tier_2": "Insoluble particles make a cloudy suspension that settles over time.",
            "tier_3": "1. Suspension, 2. Opaque, 3. Particles settle to bottom."
        }
    }


def arch_04_solution_definition_solute_solvent(rng: random.Random) -> Dict[str, Any]:
    solutions = [
        ("copper sulfate crystals dissolved in distilled water", "copper sulfate crystals", "water", "blue transparent solution"),
        ("granulated white sugar stirred into hot tea", "sugar", "tea / water", "sweet transparent solution"),
        ("coarse sea salt dissolved in warm water", "salt (sodium chloride)", "water", "colourless clear solution"),
    ]
    scenario, solute, solvent, result = rng.choice(solutions)

    prompt = (
        f"Consider this mixture:\n"
        f"'{scenario}'.\n\n"
        f"1. Identify the **solute** in this mixture.\n"
        f"2. Identify the **solvent** in this mixture.\n"
        f"3. Explain why a true solution is described as **homogeneous**."
    )
    sol = (
        f"**Step 1:** Solute: **{solute}** (the substance that dissolves) [1 Mark: Solute].\n\n"
        f"**Step 2:** Solvent: **{solvent}** (the liquid in which the solute dissolves) [1 Mark: Solvent].\n\n"
        f"**Step 3:** It is **homogeneous** because the solute particles are broken down to molecular/ionic size and distributed evenly throughout the solvent, resulting in a single uniform phase that is clear/transparent [1 Mark: Homogeneous explanation]."
    )
    return {
        "id": f"ns7_sep_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Solute: {solute}; Solvent: {solvent}; evenly distributed throughout with uniform composition",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_solution_definition_solute_solvent",
        "misconception_tags": ["solute_vs_solvent"],
        "hints": {
            "tier_1": "Solute dissolves in the solvent.",
            "tier_2": f"{solute} dissolves in {solvent}.",
            "tier_3": f"Solute: {solute}; Solvent: {solvent}."
        }
    }


def arch_05_suspension_vs_solution_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two beakers each contain a solid mixed with water:\n"
        f"- Beaker A contains a solution of salt in water.\n"
        f"- Beaker B contains a suspension of clay in water.\n\n"
        f"Compare Beaker A and Beaker B by answering:\n"
        f"1. Which mixture is clear (transparent), and which is opaque (cloudy)?\n"
        f"2. What happens in each beaker when left standing on a lab bench for 24 hours?\n"
        f"3. Can the solid in Beaker A be separated by pouring the liquid through ordinary filter paper? Explain."
    )
    sol = (
        f"**Step 1:** Beaker A (solution) is **clear / transparent**, while Beaker B (suspension) is **opaque / cloudy** [1 Mark: Appearance].\n\n"
        f"**Step 2:** In Beaker A, nothing settles (remains completely dissolved); in Beaker B, the clay particles **settle to the bottom as sediment** [1 Mark: Stability].\n\n"
        f"**Step 3:** **No.** Dissolved salt particles are microscopic (individual ions) and pass directly through the microscopic pores of filter paper with the water [1 Mark: Filtration limit]."
    )
    return {
        "id": f"ns7_sep_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Beaker A clear, Beaker B opaque; clay settles while salt stays dissolved; No, dissolved ions pass through filter paper",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_suspension_vs_solution_comparison",
        "misconception_tags": ["filtering_dissolved_solutes_myth"],
        "hints": {
            "tier_1": "Solutions are clear and don't settle; suspensions are cloudy and settle.",
            "tier_2": "Can you filter dissolved salt? No, because the particles are too small.",
            "tier_3": "Beaker A clear, B cloudy; clay settles; dissolved salt cannot be filtered."
        }
    }


def arch_06_miscible_vs_immiscible_liquids(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("pure ethanol and tap water", True, "miscible", "form a single, completely uniform liquid solution without separate layers"),
        ("vegetable cooking oil and tap water", False, "immiscible", "do not mix and separate into two distinct layers"),
        ("vinegar (dilute ethanoic acid) and water", True, "miscible", "dissolve into each other completely in all proportions"),
        ("petrol and water", False, "immiscible", "repel each other and form distinct layers based on density differences"),
    ]
    liquids, mixes, term, behavior = rng.choice(pairs)

    prompt = (
        f"A laboratory technician pours 50 mL of each liquid into a beaker: **{liquids}**.\n\n"
        f"1. State whether this pair of liquids is **miscible** or **immiscible**.\n"
        f"2. Explain what this term means regarding their physical behaviour when shaken together."
    )
    sol = (
        f"**Step 1:** The liquids are **{term}** [1 Mark: Classification].\n\n"
        f"**Step 2:** {term.capitalize()} means that the two liquids {behavior} [1 Mark: Scientific explanation]."
    )
    return {
        "id": f"ns7_sep_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{term}; {behavior}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "06_miscible_vs_immiscible_liquids",
        "misconception_tags": ["miscibility_meaning"],
        "hints": {
            "tier_1": "Do these liquids mix into one phase or form layers?",
            "tier_2": f"Miscible means mixable; immiscible means they separate. This pair is {term}.",
            "tier_3": f"{term.capitalize()}."
        }
    }


def arch_07_emulsions_and_layer_separation(rng: random.Random) -> Dict[str, Any]:
    oil_density = rng.choice([0.88, 0.91, 0.92])
    water_density = 1.00

    prompt = (
        f"A mixture of sunflower cooking oil (density ${str(oil_density).replace('.', ',')}\\text{{ g/cm}}^3$) and water (density $1{{,}}00\\text{{ g/cm}}^3$) is shaken vigorously and poured into a measuring cylinder.\n\n"
        f"1. Name the temporary milky/cloudy mixture of tiny oil droplets dispersed in water.\n"
        f"2. When left to stand, which liquid forms the top layer, and which forms the bottom layer? Justify using density.\n"
        f"3. Name the specialized laboratory glassware equipped with a stopcock tap used to drain and separate these two layers."
    )
    sol = (
        f"**Step 1:** The temporary mixture is called an **emulsion** [1 Mark: Terminology].\n\n"
        f"**Step 2:** **Oil forms the top layer** and **water forms the bottom layer** because oil has a lower density (${str(oil_density).replace('.', ',')}\\text{{ g/cm}}^3$) than water ($1{{,}}00\\text{{ g/cm}}^3$) [1 Mark: Layer order and density].\n\n"
        f"**Step 3:** The glassware is a **separating funnel** (separatory funnel) [1 Mark: Apparatus]."
    )
    return {
        "id": f"ns7_sep_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Emulsion; Oil on top, water on bottom because oil is less dense; Separating funnel",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_emulsions_and_layer_separation",
        "misconception_tags": ["emulsion_and_separating_funnel"],
        "hints": {
            "tier_1": "Which liquid is less dense? Less dense liquid floats on top.",
            "tier_2": "Oil is less dense than water. The funnel with a tap is a separating funnel.",
            "tier_3": "Emulsion; oil top, water bottom; separating funnel."
        }
    }


def arch_08_gas_gas_mixtures_air_composition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Clean, dry atmospheric air is a gaseous mixture of different elements and compounds.\n\n"
        f"1. Name the most abundant gas in clean air, and state its approximate percentage by volume.\n"
        f"2. Name the second most abundant gas, essential for human respiration, and state its percentage.\n"
        f"3. Name ONE other gas present in air in small or trace amounts."
    )
    sol = (
        f"**Step 1:** The most abundant gas is **nitrogen ($N_2$)**, making up approximately **$78\\%$** of air [1 Mark: Nitrogen].\n\n"
        f"**Step 2:** The second gas is **oxygen ($O_2$)**, making up approximately **$21\\%$** [1 Mark: Oxygen].\n\n"
        f"**Step 3:** Trace gases (any one): **argon** (0.9%), **carbon dioxide ($CO_2$)** (0.04%), or water vapour [1 Mark: Trace gas]."
    )
    return {
        "id": f"ns7_sep_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Nitrogen (~78%); Oxygen (~21%); Argon / Carbon dioxide / Water vapour",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_gas_gas_mixtures_air_composition",
        "misconception_tags": ["air_is_mostly_oxygen_myth"],
        "hints": {
            "tier_1": "Air is mostly nitrogen, not oxygen.",
            "tier_2": "Nitrogen is ~78%, oxygen is ~21%.",
            "tier_3": "Nitrogen 78%, Oxygen 21%, Carbon dioxide / Argon."
        }
    }


def arch_09_solid_gas_liquid_gas_mixtures(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("black smoke rising from a wood campfire", "solid particles of unburnt carbon / soot suspended in hot air and gases", "solid-gas"),
        ("shaving foam or bubble bath foam", "gas (air) bubbles trapped in a thin liquid soap film", "liquid-gas"),
        ("dense morning fog / mist in a valley", "tiny liquid water droplets suspended in air", "liquid-gas"),
    ]
    phenomenon, description, mix_type = rng.choice(types)

    prompt = (
        f"Examine this everyday mixture: **{phenomenon}**.\n\n"
        f"1. Classify the states of matter forming this mixture (e.g. solid-gas, liquid-gas, or gas-gas).\n"
        f"2. Explain what components make up this mixture: {description}."
    )
    sol = (
        f"**Step 1:** It is classified as a **{mix_type}** mixture [1 Mark: Classification].\n\n"
        f"**Step 2:** Component explanation: {description.capitalize()} [1 Mark: Composition]."
    )
    return {
        "id": f"ns7_sep_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{mix_type}; {description}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "09_solid_gas_liquid_gas_mixtures",
        "misconception_tags": ["smoke_and_foam_states"],
        "hints": {
            "tier_1": "What states of matter are interacting in this mixture?",
            "tier_2": f"This is a {mix_type} mixture.",
            "tier_3": f"{mix_type}."
        }
    }


# ==============================================================================
# CLUSTER 2: Mechanical Separation & Filtration (10 - 19)
# ==============================================================================

def arch_10_hand_sorting_principles_and_uses(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("workers sorting dried red kidney beans from small pebbles and dried corn kernels at an agricultural co-operative", "differences in colour, size, and shape of beans vs stones"),
        ("informal waste reclaimers sorting clear PET plastic bottles from crushed aluminium cans in a collection sack", "differences in material texture, flexibility, and colour"),
        ("geologists sorting polished gemstone pebbles from river gravel on a sorting tray", "differences in colour, lustre, and crystalline appearance"),
    ]
    app, prop_diff = rng.choice(scenarios)

    prompt = (
        f"Hand sorting is the simplest physical separation method.\n"
        f"Application: '{app}'.\n\n"
        f"1. Identify the physical properties of the items that allow them to be separated by **hand sorting**.\n"
        f"2. State ONE major limitation of hand sorting when dealing with large industrial volumes of fine powders."
    )
    sol = (
        f"**Step 1:** Items are separated based on visible physical differences: **{prop_diff}** [1 Mark: Property differences].\n\n"
        f"**Step 2:** Limitation: Hand sorting is extremely **slow, labor-intensive**, and impossible for particles too small to be grasped individually with fingers or tweezers [1 Mark: Limitation]."
    )
    return {
        "id": f"ns7_sep_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Colour, size, shape, or texture; very slow, labor-intensive and impossible for fine powders",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "10_hand_sorting_principles_and_uses",
        "misconception_tags": ["hand_sorting_limits"],
        "hints": {
            "tier_1": "What can your eyes see and your fingers pick up?",
            "tier_2": "Size, colour, and shape allow hand sorting.",
            "tier_3": "Differences in size, colour, shape; limited by speed and particle size."
        }
    }


def arch_11_sieving_particle_size_separation(rng: random.Random) -> Dict[str, Any]:
    setups = [
        ("a builder sieving coarse river sand using a wire mesh screen with 2 mm openings", "fine plaster sand", "pebbles and coarse gravel", 2),
        ("a baker sifting wheat flour through a fine wire sieve with 0.5 mm mesh", "fine aerated flour", "large flour lumps and bran husks", 0.5),
        ("a gold prospector sieving crushed alluvial gravel through a 5 mm classifier screen", "fine sediment and gold dust", "large stones and tree roots", 5),
    ]
    scenario, passes_through, stays_behind, mesh_size = rng.choice(setups)

    prompt = (
        f"Consider this sieving operation:\n"
        f"'{scenario}'.\n\n"
        f"1. On which specific physical property does **sieving** depend to separate a mixture?\n"
        f"2. Which component ({passes_through} or {stays_behind}) passes through the mesh, and why?"
    )
    sol = (
        f"**Step 1:** Sieving depends on differences in **particle size** [1 Mark: Physical property].\n\n"
        f"**Step 2:** The **{passes_through}** passes through because its particles are smaller than the {mesh_size} mm mesh openings, while {stays_behind} particles are larger and remain trapped on top [1 Mark: Size explanation]."
    )
    return {
        "id": f"ns7_sep_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Difference in particle size; {passes_through} passes because particles are smaller than mesh openings",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "11_sieving_particle_size_separation",
        "misconception_tags": ["sieving_particle_size"],
        "hints": {
            "tier_1": "What allows smaller pieces to fall through the holes?",
            "tier_2": "Particle size.",
            "tier_3": f"Particle size; {passes_through} passes through."
        }
    }


def arch_12_magnetic_separation_iron_sand(rng: random.Random) -> Dict[str, Any]:
    non_magnetic = rng.choice(["yellow sulfur powder", "fine silica beach sand", "wood sawdust", "crushed plastic beads"])

    prompt = (
        f"A laboratory mixture consists of grey iron filings thoroughly blended with {non_magnetic}.\n\n"
        f"1. Describe how you would quickly and completely separate the iron filings from the {non_magnetic}.\n"
        f"2. Explain why wrapping the bar magnet in a clean plastic sheet or clingwrap before inserting it into the mixture is good laboratory technique."
    )
    sol = (
        f"**Step 1:** Move a strong **bar magnet** through or just above the mixture; the magnetic iron filings will be attracted and cling to the magnet, leaving {non_magnetic} behind [1 Mark: Method].\n\n"
        f"**Step 2:** Wrapping the magnet prevents sharp iron filings from sticking directly into the metal poles of the magnet; peeling off the plastic over a clean container easily releases all the filings without scratching the magnet [1 Mark: Practical lab technique]."
    )
    return {
        "id": f"ns7_sep_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Use a bar magnet to attract iron filings; wrapping allows easy removal of filings without scratching magnet",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "12_magnetic_separation_iron_sand",
        "misconception_tags": ["magnetic_separation_practicalities"],
        "hints": {
            "tier_1": "Iron is attracted to magnets; sand/sulfur is not.",
            "tier_2": "Use a magnet. Plastic wrap makes cleaning iron filings off the magnet easy.",
            "tier_3": "Pass a magnet over the mixture; plastic allows easy release of filings."
        }
    }


def arch_13_magnetic_separation_industrial_scrap(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a scrap-metal recycling plant, tons of mixed municipal rubbish and crushed car parts arrive on a fast-moving conveyor belt.\n"
        f"A huge overhead crane with a powerful electromagnet hangs above the belt.\n\n"
        f"1. What types of metals will the electromagnet lift off the conveyor belt?\n"
        f"2. Name TWO common metals on the conveyor belt that will NOT be attracted by the electromagnet.\n"
        f"3. How does the crane operator release the lifted metals into the storage hopper?"
    )
    sol = (
        f"**Step 1:** The electromagnet lifts **ferrous metals** containing iron and steel [1 Mark: Ferrous metals].\n\n"
        f"**Step 2:** Non-magnetic metals (any two): **aluminium**, **copper**, **lead**, **brass**, or **zinc** [1 Mark: Non-ferrous metals].\n\n"
        f"**Step 3:** The operator turns off the electric current flowing to the electromagnet, which switches off the magnetic field and drops the scrap metal [1 Mark: Electromagnet operation]."
    )
    return {
        "id": f"ns7_sep_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Iron and steel (ferrous); aluminium and copper; switch off electric current to turn off magnet",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_magnetic_separation_industrial_scrap",
        "misconception_tags": ["electromagnet_switching"],
        "hints": {
            "tier_1": "Electromagnets only attract iron/steel, and can be switched off with electric current.",
            "tier_2": "Aluminium and copper are non-magnetic.",
            "tier_3": "Ferrous metals; aluminium/copper; turn off electric current."
        }
    }


def arch_14_filtration_residue_and_filtrate(rng: random.Random) -> Dict[str, Any]:
    mixtures = [
        ("chalk powder mixed with tap water", "white chalk powder", "clear water", "#f8fafc", "#38bdf8"),
        ("sand mixed with copper sulfate solution", "brown sand grains", "clear blue copper sulfate solution", "#d97706", "#2563eb"),
        ("crushed charcoal mixed with salt water", "black charcoal powder", "clear salt water", "#1e293b", "#38bdf8"),
    ]
    mix_name, solid_part, liquid_part, res_color, fil_color = rng.choice(mixtures)

    svg = (
        f'<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<line x1="80" y1="20" x2="80" y2="200" stroke="#334155" stroke-width="4"/>'
        f'<rect x="40" y="195" width="80" height="15" fill="#334155" rx="2"/>'
        f'<line x1="80" y1="80" x2="150" y2="80" stroke="#64748b" stroke-width="3"/>'
        f'<polygon points="150,70 230,70 195,120 185,120" fill="none" stroke="#0284c7" stroke-width="2"/>'
        f'<polygon points="155,72 225,72 193,115 187,115" fill="#f1f5f9" stroke="#94a3b8"/>'
        f'<ellipse cx="190" cy="85" rx="15" ry="8" fill="{res_color}"/>'
        f'<line x1="190" y1="120" x2="190" y2="145" stroke="#0284c7" stroke-width="2"/>'
        f'<path d="M 160,200 L 170,140 L 210,140 L 220,200 Z" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M 162,198 L 168,160 L 212,160 L 218,198 Z" fill="{fil_color}" opacity="0.6"/>'
        f'<text x="250" y="85" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Residue (Part A)</text>'
        f'<line x1="245" y1="85" x2="205" y2="85" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="250" y="175" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Filtrate (Part B)</text>'
        f'<line x1="245" y1="175" x2="215" y2="175" stroke="#0f172a" stroke-width="1.5"/>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Filtration apparatus separating {mix_name}",
        "diagram_role": "context"
    }

    prompt = (
        f"A learner pours a mixture of **{mix_name}** through a filter funnel lined with filter paper into a conical flask.\n\n"
        f"1. Name the material trapped on the filter paper (**Part A**).\n"
        f"2. Name the clear liquid collected in the flask below (**Part B**).\n"
        f"3. Specifically identify which component of the mixture is in Part A and which is in Part B."
    )
    sol = (
        f"**Step 1:** Part A is called the **residue** [1 Mark: Terminology].\n\n"
        f"**Step 2:** Part B is called the **filtrate** [1 Mark: Terminology].\n\n"
        f"**Step 3:** The residue is the insoluble **{solid_part}**; the filtrate is the **{liquid_part}** [1 Mark: Identification]."
    )
    return {
        "id": f"ns7_sep_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Part A = Residue ({solid_part}); Part B = Filtrate ({liquid_part})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "14_filtration_residue_and_filtrate",
        "misconception_tags": ["residue_vs_filtrate"],
        "hints": {
            "tier_1": "The solid left in the paper is residue; the liquid that passes through is filtrate.",
            "tier_2": f"Residue is {solid_part}; filtrate is {liquid_part}.",
            "tier_3": f"Part A = Residue ({solid_part}); Part B = Filtrate ({liquid_part})."
        }
    }


def arch_15_filtration_insoluble_solid_liquid(rng: random.Random) -> Dict[str, Any]:
    solids = [
        ("coarse sand", "cannot dissolve in water (insoluble)", True),
        ("table salt (sodium chloride)", "dissolves into individual separated ions in water (soluble)", False),
        ("crushed blackboard chalk", "does not dissolve in water (insoluble)", True),
        ("granulated white sugar", "dissolves into individual molecules in water (soluble)", False),
    ]
    rng.shuffle(solids)
    s1, s2 = solids[0], solids[1]

    prompt = (
        f"A learner has two test mixtures in water:\n"
        f"- Mixture 1: {s1[0]} in water\n"
        f"- Mixture 2: {s2[0]} in water\n\n"
        f"1. State which mixture CAN be separated using filter paper and funnel.\n"
        f"2. Explain why filtration succeeds for that mixture but completely fails for the other."
    )
    filterable = s1[0] if s1[2] else (s2[0] if s2[2] else "Neither")
    unfilterable = s2[0] if s1[2] else (s1[0] if s2[2] else "Both")

    sol = (
        f"**Step 1:** **{filterable} in water** can be separated by filtration [1 Mark: Selection].\n\n"
        f"**Step 2:** Filtration only separates **insoluble solids** whose particles are larger than the filter paper pores. Soluble substances like {unfilterable} dissolve completely into molecular/ionic particles that pass freely through the pores with water [1 Mark: Scientific explanation]."
    )
    return {
        "id": f"ns7_sep_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{filterable} in water; filtration only separates insoluble solids whose particles are larger than filter pores",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "15_filtration_insoluble_solid_liquid",
        "misconception_tags": ["filtration_requires_insoluble_solid"],
        "hints": {
            "tier_1": "Can you filter something that is dissolved?",
            "tier_2": "Only insoluble solids are trapped by filter paper.",
            "tier_3": f"{filterable} can be filtered because it is insoluble."
        }
    }


def arch_16_filtration_apparatus_setup(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When setting up a filtration apparatus in a laboratory:\n\n"
        f"1. List THREE key pieces of laboratory equipment required (excluding the beaker holding the dirty mixture).\n"
        f"2. Describe how a flat circular disc of filter paper is folded to fit snugly inside a conical funnel.\n"
        f"3. Explain why the folded paper is moistened with a few drops of pure water before pouring the mixture."
    )
    sol = (
        f"**Step 1:** Three pieces: **filter funnel**, **conical flask (or receiving beaker)**, and **retort stand with clamp (or ring)** [1 Mark: Equipment].\n\n"
        f"**Step 2:** Fold the circular filter paper in half to make a semicircle, then in half again to form a quadrant; open one pocket out to create a cone [1 Mark: Folding technique].\n\n"
        f"**Step 3:** Wetting the paper with water seals it against the glass funnel wall, preventing unfiltered liquid from bypassing around the edges [1 Mark: Wetting purpose]."
    )
    return {
        "id": f"ns7_sep_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Filter funnel, conical flask, filter paper; fold in half then quarters to form cone; seals paper against glass",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_filtration_apparatus_setup",
        "misconception_tags": ["filter_paper_folding_technique"],
        "hints": {
            "tier_1": "You need funnel, flask, and paper.",
            "tier_2": "Fold in half, fold in half again, open into cone.",
            "tier_3": "Funnel, flask, filter paper; fold in quarters; wetting seals paper against glass."
        }
    }


def arch_17_sedimentation_and_settling_principle(rng: random.Random) -> Dict[str, Any]:
    min_time = rng.choice([15, 30, 45])
    settling_items = [
        ("muddy flood river water containing silt and clay", "denser silt grains settle to the bottom under gravity, leaving clearer water on top"),
        ("crushed gold ore slurry in a cyanide settling vat", "dense gold-bearing rock pulp sinks to the bottom of the vat"),
        ("fresh unpasteurised milk standing in a vat", "less dense cream / fat globules float to the top"),
    ]
    context, mechanism = rng.choice(settling_items)

    prompt = (
        f"In civil engineering and mining, settling tanks are widely used.\n"
        f"Consider: '{context}'.\n\n"
        f"1. Define the physical process of **sedimentation**.\n"
        f"2. Explain which natural physical force drives sedimentation.\n"
        f"3. State how particle size affects the speed at which particles settle."
    )
    sol = (
        f"**Step 1:** Sedimentation is the process where heavier suspended solid particles settle out of a liquid mixture to form a layer of sediment at the bottom [1 Mark: Definition].\n\n"
        f"**Step 2:** The process is driven by the force of **gravity** pulling on the denser particles [1 Mark: Force].\n\n"
        f"**Step 3:** **Larger, denser particles settle much faster** than fine colloidal particles [1 Mark: Particle size effect]."
    )
    return {
        "id": f"ns7_sep_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Heavier particles settle to bottom; driven by gravity; larger particles settle faster",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_sedimentation_and_settling_principle",
        "misconception_tags": ["sedimentation_gravity_driving_force"],
        "hints": {
            "tier_1": "What pulls heavy particles down to the bottom?",
            "tier_2": "Gravity causes sedimentation; bigger particles sink faster.",
            "tier_3": "Particles settle to bottom under gravity; larger particles settle faster."
        }
    }


def arch_18_decanting_technique_and_limits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"After allowing muddy water to settle in a beaker, a learner performs **decanting**.\n\n"
        f"1. Describe the physical action involved in decanting a settled mixture.\n"
        f"2. Why is a clean glass stirring rod often held across the lip of the beaker during decanting?\n"
        f"3. State ONE major disadvantage of decanting compared to filtration."
    )
    sol = (
        f"**Step 1:** Decanting is carefully pouring off the clear liquid (supernatant) from the top while leaving the solid sediment undisturbed at the bottom [1 Mark: Description].\n\n"
        f"**Step 2:** The glass rod guides the liquid stream smoothly without splashing or disturbing the delicate sediment bed [1 Mark: Technique].\n\n"
        f"**Step 3:** Decanting is **less complete / less pure** than filtration, as some fine suspended particles inevitably pour over, and some liquid is left behind in the sediment [1 Mark: Limitation]."
    )
    return {
        "id": f"ns7_sep_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Carefully pouring off liquid leaving sediment; glass rod guides flow smoothly; less pure than filtration (some solid pours over)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_decanting_technique_and_limits",
        "misconception_tags": ["decanting_vs_filtration_purity"],
        "hints": {
            "tier_1": "Decanting means pouring off the top liquid.",
            "tier_2": "A glass rod directs the flow; decanting is not 100% clean compared to filtration.",
            "tier_3": "Pour off liquid leaving sediment; rod prevents splashing; decanting leaves impurities."
        }
    }


def arch_19_centrifuging_speed_separation(rng: random.Random) -> Dict[str, Any]:
    rpm = rng.choice([3000, 4000, 5000])
    cases = [
        ("whole blood sample in a medical clinic pathology laboratory", "dense red blood cells settle to the bottom, clear yellowish blood plasma stays on top"),
        ("fresh whole milk in a dairy processing plant", "dense skim milk is driven outwards while lighter fat/cream collects at the centre"),
    ]
    sample_desc, outcome = rng.choice(cases)

    prompt = (
        f"A medical technician places a test tube containing {sample_desc} into a **centrifuge** spinning at {rpm} revolutions per minute (rpm).\n\n"
        f"1. Explain how a centrifuge speeds up the separation of suspended components compared to ordinary gravity settling.\n"
        f"2. Describe the separated layers produced: {outcome}."
    )
    sol = (
        f"**Step 1:** Rapid spinning generates a powerful centrifugal force (many times greater than gravity), forcing denser particles to the outer bottom of the tube in minutes rather than waiting hours [1 Mark: Centrifugal mechanism].\n\n"
        f"**Step 2:** {outcome.capitalize()} [1 Mark: Separation outcome]."
    )
    return {
        "id": f"ns7_sep_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"High-speed spinning creates strong centrifugal force separating dense particles rapidly; {outcome}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "19_centrifuging_speed_separation",
        "misconception_tags": ["centrifuge_operation"],
        "hints": {
            "tier_1": "Spinning rapidly creates a force much stronger than gravity.",
            "tier_2": f"Denser components are forced to the bottom; {outcome}.",
            "tier_3": "Centrifugal force accelerates sedimentation."
        }
    }


# ==============================================================================
# CLUSTER 3: Evaporation, Distillation & Thermal Separation (20 - 25)
# ==============================================================================

def arch_20_evaporation_recovering_solute(rng: random.Random) -> Dict[str, Any]:
    salts = [
        ("salt water (sodium chloride solution)", "white crystalline salt", "water vapour", 100),
        ("copper sulfate solution", "blue copper sulfate crystals", "water vapour", 100),
        ("alum solution (potassium aluminium sulfate)", "clear alum crystals", "water vapour", 100),
    ]
    solution_name, crystal_name, vapour_name, bp = rng.choice(salts)

    prompt = (
        f"A learner pours $50\\text{{ mL}}$ of **{solution_name}** into a porcelain evaporating dish mounted on a tripod and wire gauze over a Bunsen flame.\n\n"
        f"1. Describe what happens to the liquid solvent as heating continues.\n"
        f"2. What remains in the evaporating dish after all the liquid has vanished?\n"
        f"3. State ONE major disadvantage of using evaporation if your goal is to recover the pure liquid."
    )
    sol = (
        f"**Step 1:** The solvent (water) boils and evaporates away as **{vapour_name}** escaping into the atmosphere [1 Mark: Solvent fate].\n\n"
        f"**Step 2:** Solid **{crystal_name}** remains behind in the dish [1 Mark: Residue].\n\n"
        f"**Step 3:** The evaporated solvent escapes into the air and is **lost / cannot be collected** [1 Mark: Evaporation limitation]."
    )
    return {
        "id": f"ns7_sep_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Solvent boils and evaporates into air; {crystal_name} remains; the solvent liquid is lost to atmosphere",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_evaporation_recovering_solute",
        "misconception_tags": ["solvent_lost_in_evaporation"],
        "hints": {
            "tier_1": "Where does the steam go? Can you catch it with a dish?",
            "tier_2": "The water evaporates into the air and is lost; solid crystals stay behind.",
            "tier_3": f"Solvent evaporates away; {crystal_name} remains; solvent is lost."
        }
    }


def arch_21_rate_of_evaporation_factors(rng: random.Random) -> Dict[str, Any]:
    factors = [
        ("Temperature", "high temperature increases the kinetic energy of liquid particles, allowing them to escape faster from the surface"),
        ("Surface area", "a wider container exposes more liquid molecules at the surface, increasing the rate of evaporation"),
        ("Air movement / wind", "moving air removes vapour molecules immediately above the surface, preventing local saturation"),
    ]
    f1, f2 = rng.sample(factors, 2)

    prompt = (
        f"Commercial sea-salt works in Port Elizabeth and Walvis Bay use vast, shallow open-air pans to evaporate seawater.\n\n"
        f"1. Explain why salt works use wide, shallow pans rather than deep vertical tanks (relate to **{f1[0]}**).\n"
        f"2. Explain how **{f2[0]}** affects the time taken for all water to evaporate."
    )
    sol = (
        f"**Step 1:** {f1[1].capitalize()} [1 Mark: First factor].\n\n"
        f"**Step 2:** {f2[1].capitalize()} [1 Mark: Second factor]."
    )
    return {
        "id": f"ns7_sep_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{f1[0]}: {f1[1]}; {f2[0]}: {f2[1]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "21_rate_of_evaporation_factors",
        "misconception_tags": ["evaporation_factors_surface_area"],
        "hints": {
            "tier_1": "Think of spreading wet washing: why does it dry faster when unfolded and in the sun?",
            "tier_2": "Large surface area and warm breezy conditions speed up evaporation.",
            "tier_3": f"{f1[0]} and {f2[0]} increase rate of evaporation."
        }
    }


def arch_22_crystallisation_from_solution(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("Copper sulfate", "bright blue diamond-shaped crystals"),
        ("Alum (potassium aluminium sulfate)", "clear octahedral crystals"),
        ("Sodium chloride (table salt)", "cubic crystals"),
    ]
    sub, shape = rng.choice(substances)

    prompt = (
        f"To obtain large, pure crystals of **{sub}**:\n"
        f"A hot saturated solution is prepared and then allowed to cool down very slowly on a shelf undisturbed for several days.\n\n"
        f"1. Explain why crystals form as a hot saturated solution cools down.\n"
        f"2. Why does slow cooling produce much larger, better-formed crystals than plunging the beaker into an ice bath?"
    )
    sol = (
        f"**Step 1:** Most solid solutes are less soluble at lower temperatures; as the solvent cools, it can hold less dissolved solute, so excess solute precipitates out as solid crystals [1 Mark: Solubility temperature curve].\n\n"
        f"**Step 2:** Slow cooling allows solute particles ample time to arrange themselves into orderly, symmetrical crystalline lattice structures ({shape}), whereas rapid cooling forms tiny, irregular crystal grains [1 Mark: Crystal growth rate]."
    )
    return {
        "id": f"ns7_sep_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Solubility decreases with cooling so excess solute crystallises; slow cooling gives particles time to form large regular crystals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "22_crystallisation_from_solution",
        "misconception_tags": ["cooling_rate_crystal_size"],
        "hints": {
            "tier_1": "Does cold water hold more or less dissolved salt than hot water?",
            "tier_2": "Solubility drops as water cools. Slow cooling gives time to grow big crystals.",
            "tier_3": "Solubility decreases as temp drops; slow cooling forms large regular lattices."
        }
    }


def arch_23_simple_distillation_apparatus_parts(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([100, 78, 95])
    substance = "Water" if temp == 100 else ("Ethanol" if temp == 78 else "Liquid mixture")

    svg = (
        f'<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<circle cx="80" cy="140" r="30" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 60,150 Q 80,165 100,150 Z" fill="#93c5fd"/>'
        f'<rect x="74" y="60" width="12" height="60" fill="#ffffff" stroke="#334155" stroke-width="2"/>'
        f'<line x1="80" y1="30" x2="80" y2="90" stroke="#ef4444" stroke-width="2"/>'
        f'<circle cx="80" cy="90" r="3" fill="#ef4444"/>'
        f'<text x="60" y="45" font-family="sans-serif" font-size="9" fill="#ef4444">T: {temp}°C</text>'
        f'<line x1="86" y1="80" x2="250" y2="160" stroke="#334155" stroke-width="3"/>'
        f'<rect x="120" y="85" width="100" height="24" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" transform="rotate(27 170 97)"/>'
        f'<line x1="140" y1="120" x2="140" y2="145" stroke="#0284c7" stroke-width="2"/>'
        f'<line x1="210" y1="80" x2="210" y2="55" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="140" y="160" font-family="sans-serif" font-size="8" fill="#0284c7" text-anchor="middle">Water in</text>'
        f'<text x="210" y="48" font-family="sans-serif" font-size="8" fill="#0284c7" text-anchor="middle">Water out</text>'
        f'<path d="M 260,200 L 270,165 L 290,165 L 300,200 Z" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 262,198 L 268,180 L 292,180 L 298,198 Z" fill="#38bdf8"/>'
        f'<text x="80" y="195" font-family="sans-serif" font-size="10" fill="#334155" text-anchor="middle">Boiling Flask</text>'
        f'<text x="175" y="145" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0284c7">Liebig Condenser</text>'
        f'<text x="280" y="215" font-family="sans-serif" font-size="10" fill="#334155" text-anchor="middle">Distillate</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Simple distillation apparatus for separating {substance} showing Liebig condenser",
        "diagram_role": "context"
    }

    prompt = (
        f"In a laboratory distillation setup purifying {substance}:\n\n"
        f"1. Name the glass tube apparatus that cools and condenses vapour into liquid.\n"
        f"2. Where exactly should the bulb of the thermometer be positioned, and why?\n"
        f"3. Name the two consecutive phase changes that occur during distillation."
    )
    sol = (
        f"**Step 1:** The apparatus is a **Liebig condenser** [1 Mark: Apparatus].\n\n"
        f"**Step 2:** The bulb must be placed **level with the side-arm opening** leading into the condenser to measure the exact boiling temperature of the vapour entering the condenser [1 Mark: Thermometer position].\n\n"
        f"**Step 3:** The two phase changes are **evaporation (boiling)** in the flask followed by **condensation** in the condenser [1 Mark: Phase changes]."
    )
    return {
        "id": f"ns7_sep_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Liebig condenser; level with condenser side-arm entrance; boiling/evaporation followed by condensation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "23_simple_distillation_apparatus_parts",
        "misconception_tags": ["distillation_phase_changes"],
        "hints": {
            "tier_1": "Liquid boils to vapour, then vapour cools to liquid.",
            "tier_2": "The cooler is a Liebig condenser. Thermometer bulb sits at the side-arm.",
            "tier_3": "Liebig condenser; side-arm level; evaporation and condensation."
        }
    }


def arch_24_simple_distillation_water_flow_direction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a Liebig condenser, cold tap water circulates through an outer jacket surrounding the inner vapour tube.\n\n"
        f"1. Should cold cooling water enter at the **bottom** or the **top** of the condenser jacket?\n"
        f"2. Explain TWO scientific reasons why this direction of water flow is essential."
    )
    sol = (
        f"**Step 1:** Cold water must enter at the **bottom** and leave at the **top** [1 Mark: Direction].\n\n"
        f"**Step 2:**\n"
        f"- Reason 1: Entering at the bottom ensures the entire outer jacket fills completely with water without trapping insulating air pockets [1 Mark: Complete filling].\n"
        f"- Reason 2: It creates a **counter-current cooling** gradient where the coldest water meets the coolest liquid at the exit, maximizing heat transfer and preventing vapour from escaping [1 Mark: Efficient heat transfer]."
    )
    return {
        "id": f"ns7_sep_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Enters at bottom, exits at top; completely fills jacket without air bubbles and provides counter-current cooling",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_simple_distillation_water_flow_direction",
        "misconception_tags": ["condenser_water_flow_direction"],
        "hints": {
            "tier_1": "Water in at bottom, water out at top.",
            "tier_2": "Water entering at top would trickle down and leave the top half full of air.",
            "tier_3": "Bottom in, top out; fills jacket completely and ensures maximum cooling."
        }
    }


def arch_25_simple_distillation_pure_water_recovery(rng: random.Random) -> Dict[str, Any]:
    volumes = [100, 150, 200]
    initial_vol = rng.choice(volumes)
    salt_mass = rng.choice([5, 8, 10])

    prompt = (
        f"A learner distills {initial_vol} mL of seawater containing {salt_mass} g of dissolved salt in a simple distillation kit.\n\n"
        f"1. Name the liquid collected in the receiving conical flask.\n"
        f"2. What physical substance remains inside the round-bottom flask after all liquid distills over?\n"
        f"3. Explain why distillation can recover pure water from saltwater whereas simple boiling in an open dish cannot."
    )
    sol = (
        f"**Step 1:** The liquid collected is **pure distilled water** (the distillate) [1 Mark: Distillate].\n\n"
        f"**Step 2:** Solid **salt crystals ({salt_mass} g)** remain behind in the boiling flask [1 Mark: Residue].\n\n"
        f"**Step 3:** Distillation channels the evaporated water vapour into a closed condenser that cools and captures it as liquid, whereas an open dish lets the vapour escape into the open air [1 Mark: Closed recovery system]."
    )
    return {
        "id": f"ns7_sep_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Pure distilled water; {salt_mass} g salt crystals; condenser captures and condenses steam into liquid",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_simple_distillation_pure_water_recovery",
        "misconception_tags": ["distillation_vs_evaporation_purpose"],
        "hints": {
            "tier_1": "Distillation collects the liquid that boiled away.",
            "tier_2": "Pure water is collected as distillate; salt stays behind.",
            "tier_3": "Pure distilled water; salt remains; condenser captures the steam."
        }
    }
