"""
Grade 8 Natural Sciences - Term 2: Particle Model of Matter (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/02. Particle model of matter.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Core Principles & States of Matter (01 - 09)
# ==============================================================================

def arch_01_particle_model_four_core_principles(rng: random.Random) -> Dict[str, Any]:
    principles = [
        ("Principle 1: All matter is made up of particles", "atoms, molecules, or ions form all physical substances"),
        ("Principle 2: Particles are in continuous, ceaseless motion", "particles possess kinetic energy at all temperatures above absolute zero"),
        ("Principle 3: There are empty spaces between particles", "the space between particles contains absolutely nothing, not even air"),
        ("Principle 4: Particles exert forces of attraction on one another", "intermolecular forces pull particles together, with strength varying by state"),
    ]
    target_p, detail = rng.choice(principles)

    prompt = (
        f"The **particle model of matter** is a cornerstone scientific theory that explains the physical behavior of materials.\n\n"
        f"1. State the core concept described by: **{target_p.split(':')[0]}** ({detail}).\n"
        f"2. Name any two other fundamental principles of the particle model of matter.\n"
        f"3. What is located in the spaces between particles in a pure substance?"
    )
    sol = (
        f"**Step 1:** {target_p} [1 Mark: Target principle].\n\n"
        f"**Step 2:** Any two other principles: (1) All matter is made of particles; (2) Particles are in continuous motion; (3) There are empty spaces between particles; (4) Particles exert forces of attraction on one another [1 Mark: Other principles].\n\n"
        f"**Step 3:** There is **empty space (a vacuum / nothing at all)** between the particles; there is no air or other matter between them [1 Mark: Empty space]."
    )
    return {
        "id": f"ns8_pmm_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_p}; Any two other principles; Empty space (vacuum) with nothing between particles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "01_particle_model_four_core_principles",
        "misconception_tags": ["particle_model_principles"],
        "hints": {
            "tier_1": "Recall the four rules: particles, moving, spaces, forces.",
            "tier_2": "The space between particles is completely empty (vacuum).",
            "tier_3": f"{target_p}; two other principles; empty space."
        }
    }


def arch_02_solids_particle_arrangement_and_vibration(rng: random.Random) -> Dict[str, Any]:
    solids = [
        ("Copper metal bar", "atoms arranged in a tightly packed face-centered cubic lattice"),
        ("Ice crystal (solid water)", "water molecules locked into an open hexagonal crystalline framework"),
        ("Table salt crystal ($NaCl$)", "sodium and chloride ions alternating in a rigid 3D cubic lattice"),
    ]
    name, struct = rng.choice(solids)

    prompt = (
        f"Consider a solid substance: **{name}** ({struct}).\n\n"
        f"1. Describe the arrangement of particles in a solid (order, spacing, and pattern).\n"
        f"2. How do particles move inside a solid? Can they move freely from place to place?\n"
        f"3. Explain why solids have a fixed shape and cannot easily be squashed (incompressible)."
    )
    sol = (
        f"**Step 1:** Particles in a solid are **closely packed together in a regular, orderly repeating pattern (crystal lattice)** with minimal empty space between them [1 Mark: Arrangement].\n\n"
        f"**Step 2:** Particles **vibrate back and forth about fixed positions**; they cannot move freely or slide past each other because strong attractive forces hold them in place [1 Mark: Movement].\n\n"
        f"**Step 3:** Solids maintain a fixed shape because **strong forces prevent particles from moving away from their fixed positions**, and they are incompressible because **particles are already packed as closely as possible** [1 Mark: Fixed shape and incompressibility]."
    )
    return {
        "id": f"ns8_pmm_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Closely packed in regular orderly pattern; vibrate about fixed positions; strong forces maintain fixed shape and close packing prevents compression",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_solids_particle_arrangement_and_vibration",
        "misconception_tags": ["solids_particle_model"],
        "hints": {
            "tier_1": "In solids, particles are locked in place like soldiers in ranks.",
            "tier_2": "They only vibrate; they cannot swap places.",
            "tier_3": "Closely packed regular pattern; vibrate in fixed positions; strong forces."
        }
    }


def arch_03_liquids_particle_arrangement_and_slip(rng: random.Random) -> Dict[str, Any]:
    liquids = [
        ("liquid water", "poured from a tall measuring cylinder into a flat petri dish"),
        ("vegetable cooking oil", "poured from a bottle into a frying pan"),
        ("liquid mercury", "transferred between different laboratory beakers"),
    ]
    name, action = rng.choice(liquids)

    prompt = (
        f"When **{name}** is {action}, it changes its shape to match the container, but its volume remains exactly the same.\n\n"
        f"1. Describe the arrangement of particles in a liquid (spacing and order).\n"
        f"2. How do particles move in a liquid, and how does this explain why liquids can flow?\n"
        f"3. Why is a liquid virtually incompressible even though it can flow?"
    )
    sol = (
        f"**Step 1:** Particles in a liquid are **closely packed but in a disordered, random arrangement** with small spaces between them [1 Mark: Arrangement].\n\n"
        f"**Step 2:** Particles have enough kinetic energy to overcome fixed positions, allowing them to **slide and roll past one another continuously**; this sliding motion allows liquids to flow and take the shape of their container [1 Mark: Flow mechanism].\n\n"
        f"**Step 3:** Liquids are incompressible because **particles are still touching/in very close contact**, so there is very little empty space to compress [1 Mark: Incompressibility]."
    )
    return {
        "id": f"ns8_pmm_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Closely packed in disordered arrangement; particles slide past each other allowing flow; incompressible because particles are in close contact",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_liquids_particle_arrangement_and_slip",
        "misconception_tags": ["liquids_particle_model"],
        "hints": {
            "tier_1": "Liquids flow because particles slide past each other.",
            "tier_2": "Particles are still touching, so you cannot compress them.",
            "tier_3": "Disordered close packing; slide past each other; touching particles prevent compression."
        }
    }


def arch_04_gases_particle_arrangement_and_rapid_motion(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("helium gas inside a party balloon", "filling every corner of the elastic rubber volume"),
        ("compressed air inside a scuba diving tank", "compressed under 200 bar of pressure into a steel cylinder"),
        ("steam escaping from a boiling kettle", "rapidly spreading throughout the entire kitchen"),
    ]
    name, context = rng.choice(gases)

    prompt = (
        f"Consider **{name}** ({context}).\n\n"
        f"1. Describe the spacing and arrangement of particles in a gas compared to solids and liquids.\n"
        f"2. How do gas particles move (speed and direction)?\n"
        f"3. Why does a gas expand to fill the entire volume of any container it is placed into?"
    )
    sol = (
        f"**Step 1:** Gas particles are **separated by very large empty spaces** (tens to hundreds of particle diameters apart) in a completely **random, disordered arrangement** [1 Mark: Spacing].\n\n"
        f"**Step 2:** Gas particles move **rapidly in all directions in straight lines**, continually colliding with each other and the container walls [1 Mark: Motion].\n\n"
        f"**Step 3:** Intermolecular forces of attraction between gas particles are **extremely weak (virtually negligible)**, so particles fly apart freely to occupy all available space [1 Mark: Expansion explanation]."
    )
    return {
        "id": f"ns8_pmm_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Very large empty spaces in random arrangement; rapid straight-line motion in all directions; very weak forces allow particles to fill container",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_gases_particle_arrangement_and_rapid_motion",
        "misconception_tags": ["gases_particle_model"],
        "hints": {
            "tier_1": "Gases have huge empty spaces between particles.",
            "tier_2": "They zoom in straight lines at high speed with almost zero attraction.",
            "tier_3": "Large spaces, random arrangement; rapid motion in all directions; negligible forces."
        }
    }


def arch_05_particle_spacing_and_intermolecular_forces(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Solid vs Gas", "Solids have particles touching with very strong forces; gases have particles far apart with negligible forces"),
        ("Liquid vs Gas", "Liquids have particles touching with moderate forces; gases have particles far apart with negligible forces"),
        ("Solid vs Liquid", "Solids have rigid regular packing with strong forces; liquids have close disordered packing with moderate forces"),
    ]
    comparison, summary = rng.choice(pairs)

    prompt = (
        f"Compare the microscopic properties of matter across states: **{comparison}**.\n\n"
        f"1. Contrast the **size of the empty spaces** between particles in these two states.\n"
        f"2. Contrast the **strength of the intermolecular forces of attraction** holding the particles together.\n"
        f"3. What relationship exists between the distance separating particles and the strength of the attractive forces between them?"
    )
    sol = (
        f"**Step 1:** Particle spacing contrast: {summary.split(';')[0]} [1 Mark: Spacing].\n\n"
        f"**Step 2:** Force strength contrast: {summary.split(';')[1]} [1 Mark: Forces].\n\n"
        f"**Step 3:** As the distance between particles **increases**, the strength of the attractive forces **decreases rapidly** (inverse relationship) [1 Mark: Distance vs Force relationship]."
    )
    return {
        "id": f"ns8_pmm_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{summary}; As distance increases, attractive force decreases rapidly",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_particle_spacing_and_intermolecular_forces",
        "misconception_tags": ["spacing_vs_forces_relationship"],
        "hints": {
            "tier_1": "Close particles feel strong attraction; far apart particles feel almost none.",
            "tier_2": "Solids are closest (strongest forces); gases are furthest (weakest forces).",
            "tier_3": f"{summary}; force decreases as distance increases."
        }
    }


def arch_06_compressibility_in_gases_vs_solids_liquids(rng: random.Random) -> Dict[str, Any]:
    syringe_experiment = rng.choice([
        ("Syringe A contains air; Syringe B contains liquid water", "Air can be compressed to less than half its volume, while water cannot be compressed at all"),
        ("Syringe A contains air; Syringe B contains solid sand/wood", "Air plunger moves easily under thumb pressure, whereas the sand plunger does not budge"),
    ])
    setup, observation = rng.choice([syringe_experiment])

    prompt = (
        f"In a classroom experiment, two plastic syringes have their tips sealed with rubber caps:\n"
        f"**{setup}**.\n\n"
        f"When a student pushes down hard on both plungers:\n"
        f"1. Describe what is observed ({observation}).\n"
        f"2. Use the particle model of matter to explain why gases are easily compressed.\n"
        f"3. Use the particle model to explain why liquids and solids cannot be noticeably compressed."
    )
    sol = (
        f"**Step 1:** The plunger in Syringe A (air) pushes inward significantly, while the plunger in Syringe B cannot be pushed inward at all [1 Mark: Observation].\n\n"
        f"**Step 2:** In gases, there are **vast empty spaces between particles**, so applying pressure easily pushes the particles closer together [1 Mark: Gas compression].\n\n"
        f"**Step 3:** In liquids and solids, particles are **already in direct contact (touching)** with negligible empty space between them, so they cannot be forced any closer [1 Mark: Incompressible explanation]."
    )
    return {
        "id": f"ns8_pmm_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{observation}; Gases have large empty spaces pushed together; Liquids/solids are already touching with no spaces to close",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "06_compressibility_in_gases_vs_solids_liquids",
        "misconception_tags": ["compressibility_particle_explanation"],
        "hints": {
            "tier_1": "Air has lots of empty space to squeeze; water/solids are already touching.",
            "tier_2": "Gases compress because particles get closer; solids/liquids cannot compress.",
            "tier_3": "Air plunger compresses, water/sand does not; empty spaces vs touching particles."
        }
    }


def arch_07_shape_and_volume_fixed_vs_variable(rng: random.Random) -> Dict[str, Any]:
    states = [
        ("Solid", "Fixed shape and fixed volume", "strong attractive forces lock particles into fixed positions so they cannot change shape or volume"),
        ("Liquid", "Variable shape (takes container shape) and fixed volume", "particles slide past each other taking the container shape, but remain touching so volume is constant"),
        ("Gas", "Variable shape and variable volume (fills entire container)", "particles move independently in all directions with negligible attractive forces, expanding to fill any space"),
    ]
    target_state, prop, explanation = rng.choice(states)

    prompt = (
        f"Matter exhibits distinct macro-level properties regarding shape and volume.\n\n"
        f"Consider a **{target_state}**:\n"
        f"1. State whether its **shape** is fixed or variable.\n"
        f"2. State whether its **volume** is fixed or variable.\n"
        f"3. Explain these properties using the particle model of matter ({explanation})."
    )
    sol = (
        f"**Step 1:** Shape: **{prop.split(' and ')[0]}** [1 Mark: Shape].\n\n"
        f"**Step 2:** Volume: **{prop.split(' and ')[1]}** [1 Mark: Volume].\n\n"
        f"**Step 3:** Particle explanation: {explanation} [1 Mark: Scientific explanation]."
    )
    return {
        "id": f"ns8_pmm_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{prop}; {explanation}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_shape_and_volume_fixed_vs_variable",
        "misconception_tags": ["shape_and_volume_properties"],
        "hints": {
            "tier_1": f"Think about {target_state}: does it change shape or size when moved?",
            "tier_2": f"{target_state} has {prop}.",
            "tier_3": f"{prop}; {explanation}."
        }
    }


def arch_08_particle_model_diagram_identification(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["Solid", "Liquid", "Gas"])
    r_val = rng.choice([7, 8, 9])

    # Dynamic SVG showing 3 boxes for Solid, Liquid, Gas
    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        # Box A: Solid (ordered grid)
        f'<rect x="15" y="20" width="100" height="100" rx="4" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="65" y="140" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Box A</text>'
        # Box B: Liquid (disordered, touching at bottom)
        f'<rect x="130" y="20" width="100" height="100" rx="4" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="180" y="140" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Box B</text>'
        # Box C: Gas (scattered with arrows)
        f'<rect x="245" y="20" width="100" height="100" rx="4" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="295" y="140" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Box C</text>'
    )
    # Draw solid particles in Box A (3x3 grid)
    for row in range(3):
        for col in range(3):
            svg += f'<circle cx="{40 + col*25}" cy="{45 + row*25}" r="{r_val}" fill="#2563eb" stroke="#1e3a8a"/>'
    # Draw liquid particles in Box B (clustered disordered at bottom)
    l_coords = [(150, 80), (170, 75), (195, 80), (210, 75), (160, 100), (185, 102), (205, 98), (145, 103), (175, 90)]
    for lx, ly in l_coords:
        svg += f'<circle cx="{lx}" cy="{ly}" r="{r_val}" fill="#0ea5e9" stroke="#0369a1"/>'
    # Draw gas particles in Box C (4 particles far apart)
    g_coords = [(265, 45), (320, 55), (275, 105), (315, 95)]
    for gx, gy in g_coords:
        svg += f'<circle cx="{gx}" cy="{gy}" r="{r_val}" fill="#f59e0b" stroke="#b45309"/>'
    svg += '</svg>'

    box_map = {"Solid": "Box A", "Liquid": "Box B", "Gas": "Box C"}
    target_box = box_map[target]

    prompt = (
        f"Examine the particle model diagrams for three states of matter (Box A, Box B, Box C).\n\n"
        f"1. Which box represents a **{target}**? Identify each box from A to C.\n"
        f"2. Give two visual reasons supporting your identification of Box A (Solid).\n"
        f"3. Give two visual reasons supporting your identification of Box C (Gas)."
    )
    sol = (
        f"**Step 1:** **{target} is {target_box}** (Box A = Solid, Box B = Liquid, Box C = Gas) [1 Mark: State identification].\n\n"
        f"**Step 2:** Box A is a solid because particles are arranged in a **regular orderly grid/lattice** and are **tightly touching** [1 Mark: Solid reasons].\n\n"
        f"**Step 3:** Box C is a gas because particles are **far apart with large empty spaces** and are **randomly scattered** throughout the box [1 Mark: Gas reasons]."
    )
    return {
        "id": f"ns8_pmm_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target} = {target_box}; Box A = Solid (regular grid, touching); Box B = Liquid; Box C = Gas (far apart, scattered)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_particle_model_diagram_identification",
        "misconception_tags": ["particle_diagram_state_identification"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Grid = Solid. Touching at bottom = Liquid. Few and spread out = Gas.",
            "tier_2": f"Box A is Solid, Box B is Liquid, Box C is Gas. Target is {target_box}.",
            "tier_3": f"{target} is {target_box}; Box A=Solid, Box B=Liquid, Box C=Gas."
        }
    }


def arch_09_brownian_motion_experimental_evidence(rng: random.Random) -> Dict[str, Any]:
    experiments = [
        ("pollen grains suspended in water viewed under a light microscope", "Robert Brown in 1827", "water molecules"),
        ("tiny smoke specks in a lighted glass cell viewed through a microscope", "Albert Einstein's explanation in 1905", "air molecules"),
    ]
    exp, pioneer, invisible_particle = rng.choice(experiments)

    prompt = (
        f"In a classic scientific investigation, **{exp}** were observed by {pioneer}.\n\n"
        f"The microscopic specks were seen dancing and jiggling continuously in random, erratic zigzag paths.\n\n"
        f"1. What is this phenomenon called?\n"
        f"2. Explain why the visible specks jiggle erratically even though nothing visible is touching them.\n"
        f"3. How did this experiment provide crucial historical evidence for the particle model of matter?"
    )
    sol = (
        f"**Step 1:** This phenomenon is called **Brownian motion** [1 Mark: Term].\n\n"
        f"**Step 2:** Invisible, rapidly moving **{invisible_particle}** collide unevenly with the larger visible specks from all sides, knocking them in random directions [1 Mark: Collision mechanism].\n\n"
        f"**Step 3:** It provided direct experimental proof that **matter is made of tiny, invisible particles that are in continuous ceaseless motion** [1 Mark: Particle model proof]."
    )
    return {
        "id": f"ns8_pmm_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Brownian motion; Invisible {invisible_particle} collide unevenly with specks; Proves matter is made of particles in continuous motion",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_brownian_motion_experimental_evidence",
        "misconception_tags": ["brownian_motion"],
        "hints": {
            "tier_1": "Named after botanist Robert Brown: Brownian motion.",
            "tier_2": f"Invisible {invisible_particle} bump into the specks randomly.",
            "tier_3": "Brownian motion; invisible moving molecules collide; proves continuous particle motion."
        }
    }


# ==============================================================================
# CLUSTER 2: Diffusion in Gases and Liquids (10 - 17)
# ==============================================================================

def arch_10_diffusion_definition_and_concentration_gradient(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Diffusion is a fundamental physical process explained by the particle model of matter.\n\n"
        f"1. Define the process of **diffusion** in scientific terms.\n"
        f"2. What is meant by a **concentration gradient**?\n"
        f"3. When does net diffusion stop occurring in a closed system?"
    )
    sol = (
        f"**Step 1:** Diffusion is the spontaneous **net movement of particles from an area of high concentration to an area of lower concentration** until evenly distributed [1 Mark: Definition].\n\n"
        f"**Step 2:** A concentration gradient is the **difference in the concentration (number of particles per unit volume)** between two regions [1 Mark: Gradient definition].\n\n"
        f"**Step 3:** Net diffusion stops when **dynamic equilibrium** is reached (particles are evenly distributed throughout the space, though individual particles continue to move randomly) [1 Mark: Equilibrium]."
    )
    return {
        "id": f"ns8_pmm_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Movement from high to low concentration until evenly distributed; difference in concentration between two regions; stops at dynamic equilibrium",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_diffusion_definition_and_concentration_gradient",
        "misconception_tags": ["diffusion_definition_equilibrium"],
        "hints": {
            "tier_1": "High concentration to low concentration.",
            "tier_2": "Particles spread out until evenly mixed (equilibrium).",
            "tier_3": "High to low concentration; concentration difference; dynamic equilibrium."
        }
    }


def arch_11_diffusion_in_gases_perfume_and_ammonia(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("a bottle of perfume is opened in the front corner of a quiet classroom", "perfume vapour molecules", "students at the back can smell the perfume after a short time"),
        ("a piece of burning incense is lit on a table", "scented smoke and aroma molecules", "the floral scent quickly spreads through the entire room"),
        ("an onion is sliced open on a kitchen counter", "volatile sulfur gas compounds", "people across the kitchen begin to smell it and tear up"),
    ]
    action, vapor, effect = rng.choice(scenarios)

    prompt = (
        f"When {action}, {effect} without any breeze or fan blowing.\n\n"
        f"1. Name the scientific process responsible for spreading these scent particles.\n"
        f"2. Explain using the particle model how {vapor} travel across the room through the air.\n"
        f"3. Why does diffusion happen much faster in gases than in liquids?"
    )
    sol = (
        f"**Step 1:** The process is **diffusion** [1 Mark: Process].\n\n"
        f"**Step 2:** Scent particles move **rapidly in all directions in random straight lines**, colliding with air particles and bouncing into the large empty spaces between them, spreading outward from high to low concentration [1 Mark: Particle model explanation].\n\n"
        f"**Step 3:** Gas diffusion is much faster because gas particles move at **much higher speeds** and have **vast empty spaces** to move through with negligible attractive forces [1 Mark: Gas vs Liquid speed]."
    )
    return {
        "id": f"ns8_pmm_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Diffusion; Scent particles move rapidly in random directions into empty spaces; Gas particles move faster with larger empty spaces",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_diffusion_in_gases_perfume_and_ammonia",
        "misconception_tags": ["gas_diffusion_mechanisms"],
        "hints": {
            "tier_1": "The scent spreads by diffusion.",
            "tier_2": "Gas particles fly fast through huge empty spaces.",
            "tier_3": "Diffusion; rapid random motion into empty spaces; gases have higher speed and larger spaces."
        }
    }


def arch_12_diffusion_in_liquids_potassium_permanganate(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("a purple crystal of potassium permanganate ($KMnO_4$) dropped into still water", "purple color spreads slowly throughout the liquid over several hours"),
        ("a single drop of concentrated blue food coloring placed in a beaker of still water", "blue color gradually swirls and spreads until the water is uniformly blue"),
        ("a tea bag submerged in a cup of room-temperature water", "brown tea compounds diffuse outward forming swirling clouds of color"),
    ]
    setup, observation = rng.choice(examples)

    prompt = (
        f"In a laboratory observation: **{setup}** ({observation}) without stirring.\n\n"
        f"1. Explain how the solute particles spread through the liquid using the particle model.\n"
        f"2. Why does the color eventually spread throughout the whole beaker even without stirring?\n"
        f"3. Why does diffusion take several hours in still water, whereas gas diffusion takes only seconds/minutes?"
    )
    sol = (
        f"**Step 1:** Solute particles dissolve and **water particles constantly collide with them**, jostling them into the spaces between moving water molecules [1 Mark: Liquid diffusion].\n\n"
        f"**Step 2:** Because liquid particles are in **continuous, random motion**, particles keep colliding and dispersing until they are uniformly distributed [1 Mark: Continuous motion].\n\n"
        f"**Step 3:** In liquids, particles are **closely packed with small spaces** and stronger attractive forces, meaning diffusing particles constantly bump into tightly packed liquid molecules, slowing their progress [1 Mark: Why liquids diffuse slower]."
    )
    return {
        "id": f"ns8_pmm_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Collisions push solute particles into spaces between water molecules; Continuous random motion ensures even distribution; Slower because particles are closely packed with small spaces",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_diffusion_in_liquids_potassium_permanganate",
        "misconception_tags": ["liquid_diffusion"],
        "hints": {
            "tier_1": "Moving water molecules bump the colored particles around.",
            "tier_2": "It's slower in liquids because water molecules are packed closely together.",
            "tier_3": "Water collisions spread particles; continuous motion; closely packed molecules slow diffusion."
        }
    }


def arch_13_why_diffusion_does_not_occur_in_solids(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"If a copper coin is placed on top of a silver coin on a shelf for 10 years, the two metals do not mix or diffuse into each other.\n\n"
        f"1. Does diffusion occur in solid materials under standard room conditions? (Yes or No)\n"
        f"2. Explain this observation using the particle model of matter (particle arrangement, movement, and attractive forces).\n"
        f"3. Contrast particle mobility in solids with that in liquids and gases."
    )
    sol = (
        f"**Step 1:** **No**, observable diffusion does not occur in solids under normal room conditions [1 Mark: Yes/No].\n\n"
        f"**Step 2:** Particles in solids are held by **very strong attractive forces in fixed positions (crystal lattice)** and can only vibrate; they cannot slide past each other or break free to mix with other particles [1 Mark: Solid restriction].\n\n"
        f"**Step 3:** Unlike liquids (where particles can slide past each other) and gases (where particles fly freely), solid particles **lack translational mobility** [1 Mark: Mobility contrast]."
    )
    return {
        "id": f"ns8_pmm_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No; Strong attractive forces lock particles in fixed positions so they cannot move past one another; Solids lack translational mobility",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_why_diffusion_does_not_occur_in_solids",
        "misconception_tags": ["no_diffusion_in_solids"],
        "hints": {
            "tier_1": "Can solid atoms walk away from their neighbors?",
            "tier_2": "No, they only vibrate in fixed spots.",
            "tier_3": "No; strong forces lock particles in fixed positions; no translational movement."
        }
    }


def arch_14_effect_of_temperature_on_diffusion_rate(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A tea bag placed in hot boiling water ($90^\\circ\\text{{C}}$) vs ice-cold water ($10^\\circ\\text{{C}}$)", "hot water turns dark brown within seconds, while cold water takes many minutes"),
        ("A drop of food dye placed in warm water ($60^\\circ\\text{{C}}$) vs cold water ($15^\\circ\\text{{C}}$)", "dye disperses much more rapidly in the warm water beaker"),
    ]
    setup, obs = rng.choice(scenarios)

    prompt = (
        f"A learner investigates diffusion at different temperatures:\n"
        f"**{setup}** ({obs}).\n\n"
        f"1. How does temperature affect the rate of diffusion?\n"
        f"2. Explain this effect using the concepts of **heat, kinetic energy, and particle speed**.\n"
        f"3. Identify the independent and dependent variables in this investigation."
    )
    sol = (
        f"**Step 1:** As temperature increases, the **rate of diffusion increases** (faster diffusion) [1 Mark: Temperature effect].\n\n"
        f"**Step 2:** Heating supplies thermal energy which converts into **higher kinetic energy**, making particles **move and vibrate much faster**; faster particles collide more frequently and spread out more rapidly [1 Mark: Kinetic energy explanation].\n\n"
        f"**Step 3:** Independent variable = **Temperature of the water**; Dependent variable = **Rate of diffusion (time taken to spread)** [1 Mark: Variables]."
    )
    return {
        "id": f"ns8_pmm_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Higher temperature increases diffusion rate; Higher temperature gives particles more kinetic energy to move faster; IV = Water temperature, DV = Diffusion rate",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_effect_of_temperature_on_diffusion_rate",
        "misconception_tags": ["temperature_and_diffusion_rate"],
        "hints": {
            "tier_1": "Hot water has fast moving particles.",
            "tier_2": "Higher temperature = higher kinetic energy = faster spreading.",
            "tier_3": "Higher temp = faster diffusion; more kinetic energy/speed; IV = temperature, DV = diffusion rate."
        }
    }


def arch_15_diffusion_rate_and_particle_mass_grahams_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a classic glass tube demonstration, cotton wool soaked in concentrated ammonia solution ($NH_3$, molar mass $17\\text{{ g/mol}}$) is placed at one end, and cotton wool soaked in concentrated hydrochloric acid ($HCl$, molar mass $36,5\\text{{ g/mol}}$) is placed at the other end.\n\n"
        f"When the gases diffuse toward each other, a white ring of ammonium chloride ($NH_4Cl$) solid forms inside the tube.\n\n"
        f"1. Is the white ring formed closer to the $NH_3$ end or closer to the $HCl$ end?\n"
        f"2. Explain why using the relationship between **particle mass and diffusion velocity**.\n"
        f"3. Write the word equation for the chemical reaction that forms the white ring."
    )
    sol = (
        f"**Step 1:** The white ring forms **closer to the $HCl$ end** [1 Mark: Ring location].\n\n"
        f"**Step 2:** Ammonia ($NH_3$) molecules are **lighter (smaller mass: $17\\text{{ g/mol}}$)** than hydrochloric acid ($HCl$) molecules ($36,5\\text{{ g/mol}}$); at the same temperature, lighter particles move with **higher average velocity** and therefore diffuse further in the same time [1 Mark: Mass vs velocity explanation].\n\n"
        f"**Step 3:** Word equation: **Ammonia + Hydrogen chloride $\\rightarrow$ Ammonium chloride** [1 Mark: Word equation]."
    )
    return {
        "id": f"ns8_pmm_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Closer to the HCl end; Lighter NH3 molecules travel faster than heavier HCl molecules; Ammonia + Hydrogen chloride -> Ammonium chloride",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_diffusion_rate_and_particle_mass_grahams_concept",
        "misconception_tags": ["particle_mass_diffusion_rate"],
        "hints": {
            "tier_1": "Lighter particles move faster than heavier particles.",
            "tier_2": "NH3 is lighter (17) than HCl (36.5), so it travels further down the tube.",
            "tier_3": "Closer to HCl end; lighter NH3 travels faster; Ammonia + Hydrogen chloride -> Ammonium chloride."
        }
    }


def arch_16_everyday_diffusion_phenomena(rng: random.Random) -> Dict[str, Any]:
    phenomena = [
        ("Oxygen diffusing from the lungs (alveoli) into the blood capillaries", "high oxygen concentration in inhaled air moves across thin membranes into lower oxygen blood"),
        ("Carbon dioxide diffusing into leaf stomata during photosynthesis", "ambient atmospheric CO2 moves from higher concentration outside into lower concentration inside leaf mesophyll"),
        ("A drop of milk swirling through a cup of black coffee without stirring", "milk fat and protein droplets diffuse slowly throughout the coffee water"),
    ]
    p_name, bio_mech = rng.choice(phenomena)

    prompt = (
        f"Diffusion is vital not just in chemistry labs, but in everyday life and living organisms.\n\n"
        f"Consider: **{p_name}** ({bio_mech}).\n\n"
        f"1. Explain how diffusion makes this life process or everyday event possible.\n"
        f"2. Why does diffusion require **no external energy (no cellular energy/ATP)** to occur?\n"
        f"3. Name one other vital biological or domestic example of diffusion."
    )
    sol = (
        f"**Step 1:** It relies on the natural movement of particles down their **concentration gradient** from high concentration to low concentration [1 Mark: Diffusion role].\n\n"
        f"**Step 2:** Diffusion is a **passive physical process** driven purely by the intrinsic kinetic energy of the moving particles; it requires no pump or energy input [1 Mark: Passive process].\n\n"
        f"**Step 3:** Other examples: gaseous exchange in animal tissues, nutrient absorption in small intestines, or aroma spreading from cooking food [1 Mark: Other example]."
    )
    return {
        "id": f"ns8_pmm_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Particles move down concentration gradient from high to low; Passive process driven by particle kinetic energy; e.g. gas exchange in lungs or aroma from food",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_everyday_diffusion_phenomena",
        "misconception_tags": ["everyday_diffusion_applications"],
        "hints": {
            "tier_1": "Diffusion is passive—it happens naturally without energy.",
            "tier_2": "Particles spread from high to low concentration automatically.",
            "tier_3": "Down concentration gradient; passive process powered by kinetic energy; e.g. breathing/smells."
        }
    }


def arch_17_investigating_diffusion_variables_fair_test(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner plans an experiment to test the hypothesis: *'Potassium permanganate crystals diffuse faster in warm water than in cold water.'*\n\n"
        f"1. Identify the **independent variable** in this investigation.\n"
        f"2. Identify the **dependent variable** and how it could be accurately measured.\n"
        f"3. State **two control variables** that must be kept strictly constant to ensure a fair test."
    )
    sol = (
        f"**Step 1:** Independent variable: **Temperature of the water** [1 Mark: Independent variable].\n\n"
        f"**Step 2:** Dependent variable: **Rate of diffusion** (measured by timing in seconds how long it takes for the color to reach the top of the beaker or spread uniformly) [1 Mark: Dependent variable].\n\n"
        f"**Step 3:** Control variables (any two): (1) Volume of water in each beaker; (2) Size/mass of potassium permanganate crystal; (3) Beaker shape and size; (4) Ensuring neither beaker is stirred or disturbed [1 Mark: Control variables]."
    )
    return {
        "id": f"ns8_pmm_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "IV: Water temperature; DV: Rate of diffusion (time to spread); Controls: Volume of water, crystal size, no stirring",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_investigating_diffusion_variables_fair_test",
        "misconception_tags": ["fair_test_variables_diffusion"],
        "hints": {
            "tier_1": "IV = what you change (temperature). DV = what you measure (time).",
            "tier_2": "Keep water volume and crystal size the same.",
            "tier_3": "IV = temperature; DV = time taken/rate; Controls = volume, crystal size, no stirring."
        }
    }


# ==============================================================================
# CLUSTER 3: Phase Changes & Thermal Curves (18 - 25)
# ==============================================================================

def arch_18_melting_and_freezing_microscopic_explanation(rng: random.Random) -> Dict[str, Any]:
    phase = rng.choice(["melting", "freezing"])
    if phase == "melting":
        p_name = "Melting (solid to liquid)"
        desc = "adding heat energy increases particle vibrations until forces holding particles in fixed positions are overcome"
        rev = "Freezing / solidifying"
    else:
        p_name = "Freezing (liquid to solid)"
        desc = "removing heat energy slows particle motion until attractive forces pull them back into fixed lattice positions"
        rev = "Melting"

    prompt = (
        f"Changes of state involve changes in the energy and arrangement of particles without changing the chemical identity of the substance.\n\n"
        f"Consider the process of **{p_name}**.\n\n"
        f"1. Explain what happens to the energy, movement, and arrangement of particles during {phase}.\n"
        f"2. Name the reverse phase change ({rev}).\n"
        f"3. Does the temperature of the substance change while it is actively {phase}? Explain."
    )
    sol = (
        f"**Step 1:** During {phase}: {desc} [1 Mark: Particle explanation].\n\n"
        f"**Step 2:** The reverse change is **{rev}** [1 Mark: Reverse name].\n\n"
        f"**Step 3:** **No**, the temperature remains **constant** during a phase change because thermal energy is used to overcome/form intermolecular bonds rather than changing particle kinetic energy [1 Mark: Constant temperature explanation]."
    )
    return {
        "id": f"ns8_pmm_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{desc}; Reverse is {rev}; Temperature stays constant during phase change",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_melting_and_freezing_microscopic_explanation",
        "misconception_tags": ["melting_freezing_particle_level"],
        "hints": {
            "tier_1": f"Think about heat: does {phase} add or remove energy?",
            "tier_2": "Temperature never changes during a state change.",
            "tier_3": f"{desc}; {rev}; temperature stays constant."
        }
    }


def arch_19_evaporation_vs_boiling_distinction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Both evaporation and boiling involve a liquid changing into a gas (vaporisation), but they differ fundamentally.\n\n"
        f"1. State two differences between **evaporation** and **boiling** (consider temperature and location within the liquid).\n"
        f"2. Use the particle model to explain why energetic particles at the liquid surface can evaporate below the boiling point.\n"
        f"3. Why does evaporation cause a cooling effect on your skin when you sweat?"
    )
    sol = (
        f"**Step 1:** Differences: (1) Evaporation occurs at **any temperature** below boiling, while boiling occurs only at a **fixed boiling point**; (2) Evaporation occurs **only at the liquid surface**, while boiling occurs **throughout the entire liquid (forming bubbles)** [1 Mark: Differences].\n\n"
        f"**Step 2:** Particles in a liquid have a range of kinetic energies; the **fastest, most energetic surface particles** can overcome attractive forces and escape into the gas phase [1 Mark: Surface particle escape].\n\n"
        f"**Step 3:** When the most energetic particles escape, the **average kinetic energy of the remaining liquid decreases**, causing the temperature of the skin to drop (evaporative cooling) [1 Mark: Cooling effect]."
    )
    return {
        "id": f"ns8_pmm_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Evaporation at any temp only at surface; Boiling at boiling point throughout liquid; Fast surface particles escape, lowering average kinetic energy (cooling skin)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_evaporation_vs_boiling_distinction",
        "misconception_tags": ["evaporation_vs_boiling"],
        "hints": {
            "tier_1": "Evaporation happens only at the top; boiling makes bubbles everywhere.",
            "tier_2": "Sweat cools you because the fastest hot molecules fly away.",
            "tier_3": "Surface vs throughout liquid; energetic particles escape; lowers average KE (cooling)."
        }
    }


def arch_20_condensation_and_cooling_effect(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("droplets of water forming on the outside of a cold soda can taken from the fridge", "invisible water vapour in the warm room air contacts the cold metal surface"),
        ("bathroom mirror fogging up after a hot shower", "hot steam and water vapour in the air contact the cooler glass surface"),
        ("dew forming on morning grass blades", "ground surface cools overnight causing atmospheric water vapour to condense"),
    ]
    setup, cause = rng.choice(examples)

    prompt = (
        f"A common physical observation is: **{setup}** ({cause}).\n\n"
        f"1. Name the phase change responsible for this observation.\n"
        f"2. Explain what happens to the energy and movement of the gas particles when they hit the cold surface.\n"
        f"3. How do intermolecular forces of attraction change during this transition?"
    )
    sol = (
        f"**Step 1:** The process is **condensation (gas $\\rightarrow$ liquid)** [1 Mark: Name].\n\n"
        f"**Step 2:** Gas particles lose thermal/kinetic energy to the cold surface, causing them to **slow down significantly** [1 Mark: Energy loss].\n\n"
        f"**Step 3:** As particles slow down, **intermolecular forces of attraction pull them together** into touching liquid droplets [1 Mark: Attractive forces]."
    )
    return {
        "id": f"ns8_pmm_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Condensation; Gas particles lose kinetic energy and slow down; Attractive forces pull them together into liquid droplets",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_condensation_and_cooling_effect",
        "misconception_tags": ["condensation_particle_level"],
        "hints": {
            "tier_1": "Gas turning into liquid droplets is condensation.",
            "tier_2": "Gas particles cool down, slow down, and stick together.",
            "tier_3": "Condensation; particles lose kinetic energy/slow down; forces pull them together."
        }
    }


def arch_21_sublimation_and_deposition_dry_ice_iodine(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("Dry ice (solid carbon dioxide, $CO_2$)", "solid turns directly into white foggy gas at room temperature without forming any liquid puddle"),
        ("Iodine crystals", "dark purple solid crystals turn directly into a dense purple gas when gently warmed in a beaker"),
        ("Naphthalene (mothballs)", "solid white balls slowly shrink away into vapor without melting"),
    ]
    name, obs = rng.choice(substances)

    prompt = (
        f"Some unique substances bypass the liquid state altogether:\n"
        f"**{name}** ({obs}).\n\n"
        f"1. What is the name of the phase change when a solid turns **directly into a gas** without melting?\n"
        f"2. What is the reverse process called (gas turning **directly into a solid**)?\n"
        f"3. Explain in terms of the particle model why dry ice does not leave a wet puddle on a desk."
    )
    sol = (
        f"**Step 1:** The transition from solid directly to gas is called **sublimation** [1 Mark: Sublimation].\n\n"
        f"**Step 2:** The reverse transition from gas directly to solid is called **deposition** (or desublimation) [1 Mark: Deposition].\n\n"
        f"**Step 3:** The particles gain enough energy to break completely free from the solid lattice directly into independent gas particles; atmospheric pressure is too low for liquid $CO_2$ to exist stably at room temperature, so no liquid forms [1 Mark: No liquid explanation]."
    )
    return {
        "id": f"ns8_pmm_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sublimation; Deposition; Particles break completely free from solid directly into gas with no liquid phase",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_sublimation_and_deposition_dry_ice_iodine",
        "misconception_tags": ["sublimation_and_deposition"],
        "hints": {
            "tier_1": "Solid straight to gas = sublimation. Gas straight to solid = deposition.",
            "tier_2": "Dry ice never melts into liquid, so it's dry!",
            "tier_3": "Sublimation; Deposition; breaks directly into gas phase."
        }
    }


def arch_22_heating_curve_temperature_plateaus(rng: random.Random) -> Dict[str, Any]:
    mp = rng.choice([0, 55, 80])
    bp = mp + rng.choice([100, 120])
    sub_name = "Water" if mp == 0 else f"Substance X (mp {mp}°C, bp {bp}°C)"

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<line x1="40" y1="170" x2="340" y2="170" stroke="#334155" stroke-width="2"/>'
        f'<line x1="40" y1="170" x2="40" y2="20" stroke="#334155" stroke-width="2"/>'
        f'<text x="190" y="190" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">Time / Heat Added</text>'
        f'<text x="15" y="90" font-family="sans-serif" font-size="10" fill="#475569" transform="rotate(-90 15 90)" text-anchor="middle">Temperature (°C)</text>'
        # Curve
        f'<path d="M 40,160 L 80,120 L 140,120 L 200,60 L 280,60 L 330,30" fill="none" stroke="#2563eb" stroke-width="3"/>'
        # Labels
        f'<text x="110" y="112" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Melting ({mp}°C)</text>'
        f'<text x="240" y="52" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Boiling ({bp}°C)</text>'
        f'<text x="60" y="150" font-family="sans-serif" font-size="9" fill="#1e293b">Solid</text>'
        f'<text x="170" y="100" font-family="sans-serif" font-size="9" fill="#1e293b">Liquid</text>'
        f'<text x="305" y="40" font-family="sans-serif" font-size="9" fill="#1e293b">Gas</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the heating curve for **{sub_name}**.\n\n"
        f"1. What is happening to the state of matter during the two flat horizontal plateaus ({mp}°C and {bp}°C)?\n"
        f"2. Why does the temperature remain constant during these plateaus even though heat is continually being supplied?\n"
        f"3. In which region(s) of the curve is the average kinetic energy of the particles actually increasing?"
    )
    sol = (
        f"**Step 1:** Phase changes are occurring: at {mp}°C the solid is **melting into liquid**, and at {bp}°C the liquid is **boiling into gas** [1 Mark: Phase changes].\n\n"
        f"**Step 2:** The heat energy supplied is used as **latent heat to overcome (break) intermolecular forces of attraction** holding particles together, rather than increasing particle speed/kinetic energy [1 Mark: Latent heat explanation].\n\n"
        f"**Step 3:** Kinetic energy increases during the **slanted (rising) sections** where only a single phase is present (solid heating up, liquid heating up, gas heating up) [1 Mark: Rising sections]."
    )
    return {
        "id": f"ns8_pmm_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Melting and boiling; Energy is used to break intermolecular forces rather than increase temperature; Slanted rising sections",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_heating_curve_temperature_plateaus",
        "misconception_tags": ["heating_curve_plateaus_latent_heat"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Flat lines mean state changes: melting and boiling.",
            "tier_2": "Heat is breaking bonds, not raising temperature.",
            "tier_3": "Melting/boiling plateaus; heat breaks intermolecular forces; rising lines increase kinetic energy."
        }
    }


def arch_23_cooling_curve_solidification_plateau(rng: random.Random) -> Dict[str, Any]:
    sub = rng.choice([("Stearic acid", 69), ("Salol (phenyl salicylate)", 43), ("Water", 0)])
    name, fp = sub

    prompt = (
        f"When hot liquid **{name}** is allowed to cool down to room temperature, its cooling curve shows a distinct plateau at **{fp}^\\circ\\text{{C}}**.\n\n"
        f"1. What phase change is taking place at {fp}°C?\n"
        f"2. Explain why the temperature stays constant at {fp}°C during freezing, even though the test tube is losing heat to the cooler room.\n"
        f"3. What happens to the kinetic energy and potential energy of the particles as liquid freezes into solid?"
    )
    sol = (
        f"**Step 1:** The liquid is **freezing (solidifying)** into a solid [1 Mark: Phase change].\n\n"
        f"**Step 2:** As particles form new attractive bonds to lock into the solid lattice, they **release latent heat energy** to the surroundings at the exact rate heat is being lost, keeping temperature steady [1 Mark: Heat release during bond formation].\n\n"
        f"**Step 3:** The average **kinetic energy remains constant** (constant temperature), while **potential energy decreases** as particles settle into lower-energy bonded lattice states [1 Mark: KE vs PE]."
    )
    return {
        "id": f"ns8_pmm_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Freezing (solidifying); Forming attractive bonds releases latent heat; Kinetic energy is constant while potential energy decreases",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "23_cooling_curve_solidification_plateau",
        "misconception_tags": ["cooling_curve_latent_heat"],
        "hints": {
            "tier_1": "Plateau on cooling curve = freezing.",
            "tier_2": "Bonding releases energy, keeping temperature flat.",
            "tier_3": "Freezing; bond formation releases latent heat; KE constant, PE decreases."
        }
    }


def arch_24_kinetic_energy_vs_temperature_relationship(rng: random.Random) -> Dict[str, Any]:
    temps = [(20, 80), (0, 100), (25, 300)]
    t1, t2 = rng.choice(temps)

    prompt = (
        f"In physics and chemistry, temperature has a precise microscopic definition.\n\n"
        f"1. Define **temperature** in terms of particle motion and kinetic energy.\n"
        f"2. Compare the average speed of water molecules at **${t1}^\\circ\\text{{C}}$** with those at **${t2}^\\circ\\text{{C}}$**.\n"
        f"3. What is **absolute zero** ($-273^\\circ\\text{{C}}$ or $0\\text{{ K}}$) in terms of particle motion?"
    )
    sol = (
        f"**Step 1:** Temperature is a measure of the **average kinetic energy** of the particles in a substance [1 Mark: Temperature definition].\n\n"
        f"**Step 2:** Water molecules at ${t2}^\\circ\\text{{C}}$ have **significantly higher kinetic energy and move much faster** than molecules at ${t1}^\\circ\\text{{C}}$ [1 Mark: Comparison].\n\n"
        f"**Step 3:** Absolute zero is the theoretical temperature at which **all particle motion ceases completely** (zero kinetic energy) [1 Mark: Absolute zero]."
    )
    return {
        "id": f"ns8_pmm_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Measure of average kinetic energy; Molecules at higher temp move faster; Absolute zero is where all particle motion stops",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_kinetic_energy_vs_temperature_relationship",
        "misconception_tags": ["temperature_as_average_kinetic_energy"],
        "hints": {
            "tier_1": "Temperature measures how fast particles are moving on average.",
            "tier_2": f"Molecules at {t2}°C move faster than at {t1}°C.",
            "tier_3": "Average kinetic energy; faster at higher temp; absolute zero = all motion stops."
        }
    }


def arch_25_conservation_of_mass_during_phase_change(rng: random.Random) -> Dict[str, Any]:
    m_val = rng.choice([50, 120, 250, 350])
    scenarios = [
        (f"A block of ice with mass ${m_val}\\text{{ g}}$ melts completely inside a sealed ziplock bag", f"mass of resulting liquid water is exactly {m_val} g"),
        (f"Liquid water with mass ${m_val}\\text{{ g}}$ boils and turns completely into steam inside a sealed pressure flask", f"mass of steam remains exactly {m_val} g"),
    ]
    setup, outcome = rng.choice(scenarios)

    prompt = (
        f"Consider the closed system experiment:\n"
        f"**{setup}**.\n\n"
        f"1. Predict the mass of the substance after the phase change is complete ({outcome}).\n"
        f"2. Explain why mass is conserved during physical changes using the particle model of matter.\n"
        f"3. Why might an unsealed open beaker appear to lose mass when water boils?"
    )
    sol = (
        f"**Step 1:** The mass is **exactly {m_val} g** [1 Mark: Mass prediction].\n\n"
        f"**Step 2:** No particles are created or destroyed during a phase change; the **total number and mass of particles remain strictly identical**, only their spacing and arrangement change [1 Mark: Particle conservation].\n\n"
        f"**Step 3:** In an open beaker, steam particles **escape into the surrounding room air**, so fewer particles remain in the beaker, causing a measured loss of mass [1 Mark: Open system explanation]."
    )
    return {
        "id": f"ns8_pmm_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Exactly {m_val} g; Total number of particles is conserved; In open container, gas particles escape into room air",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_conservation_of_mass_during_phase_change",
        "misconception_tags": ["conservation_of_mass_phase_change"],
        "hints": {
            "tier_1": "Melting never destroys atoms! Mass stays the same.",
            "tier_2": f"If you started with {m_val} g, you end with {m_val} g.",
            "tier_3": f"Exactly {m_val} g; number of particles does not change; steam escapes in open container."
        }
    }
