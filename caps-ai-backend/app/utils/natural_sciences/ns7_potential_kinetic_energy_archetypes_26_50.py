"""Grade 7 Natural Sciences: Term 3 - Potential and Kinetic Energy (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/02. Potential and kinetic energy.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _clean_options(correct: str, distractors: List[str], rng: random.Random) -> List[str]:
    opts = [correct] + [d for d in distractors if d != correct][:3]
    rng.shuffle(opts)
    return opts


# 26. Bow and arrow energy transformation
def arch_26_bow_and_arrow_energy_transformation(rng: random.Random) -> Dict[str, Any]:
    archery_types = [
        ("traditional African wooden hunting bow", "the bent wooden limbs and taut cord"),
        ("modern sports recurve archery bow", "the flexed carbon-fiber bow limbs"),
    ]
    bow_name, parts = rng.choice(archery_types)
    prompt = (
        f"An archer draws an arrow in a **{bow_name}**, bending **{parts}**, and then releases the arrow toward a target.\n\n"
        f"What is the sequence of energy transformations from drawing the string to releasing the flying arrow?"
    )
    correct = (
        "Chemical potential energy in archer's muscles -> Mechanical work bending the bow storing **elastic potential energy** -> "
        "**Kinetic energy** of the rapidly accelerating arrow."
    )
    distractors = [
        "Gravitational energy in the arrow -> Nuclear energy in the target -> Electrical energy in the bow.",
        "Thermal heat in the string -> Light energy in the air -> Chemical energy in the feathers.",
        "Sound energy in the woods -> Magnetic energy in the cord -> Gravitational potential energy in the quiver.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Bow and Arrow Energy Mechanics:**\n"
        f"1. **Draw:** Chemical potential energy in the archer's muscles does mechanical work to bend {parts}.\n"
        f"2. **Hold:** Energy is stored as **elastic potential energy** in the bent limbs of the bow.\n"
        f"3. **Release:** The limbs spring back to their rest position, transferring stored energy into the **kinetic energy** of the arrow."
    )
    return {
        "id": f"ns7_pk_26_{rng.randint(100000, 999999)}",
        "subskill": "26_bow_and_arrow_energy_transformation",
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
        "learning_objective_id": "ns7_pk_26",
        "hints": {
            "tier_1": "What energy is in the bent bow limbs before release?",
            "tier_2": "Bending the bow stores elastic potential energy; releasing it makes the arrow move (kinetic).",
            "tier_3": "Chemical energy in muscles -> Elastic potential energy in bow -> Kinetic energy of arrow.",
        },
        "misconception_tags": ["arrow_stores_energy_before_release", "bow_string_creates_chemical_energy"],
    }


# 27. Catapult mechanism elastic to kinetic
def arch_27_catapult_mechanism_elastic_to_kinetic(rng: random.Random) -> Dict[str, Any]:
    weights = [(50, "a 50 g ball of clay"), (100, "a 100 g wooden block")]
    mass_g, projectile = rng.choice(weights)
    prompt = (
        f"Learners construct a wooden catapult using strong elastic rubber bands to launch {projectile} ({mass_g} grams).\n\n"
        f"If the learners pull the catapult arm further back before release, what will happen to the projectile, and why?"
    )
    correct = (
        "It will launch with greater kinetic energy and travel further, because stretching the rubber bands further "
        "stores more elastic potential energy."
    )
    distractors = [
        "It will launch slower because stretching rubber bands destroys mechanical energy.",
        "It will not move at all because elastic bands only store energy when compressed into ice.",
        "It will fly backward into the ground because gravity reverses when rubber is stretched.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Catapult Elastic Potential Principles:**\n"
        f"- Work done stretching the elastic bands is directly related to displacement: greater stretch -> **greater elastic potential energy**.\n"
        f"- Upon release, this larger reservoir of stored energy converts into greater **kinetic energy** (\\(E_k = \\frac{{1}}{{2}}mv^2\\)), yielding higher launch speed and greater distance."
    )
    return {
        "id": f"ns7_pk_27_{rng.randint(100000, 999999)}",
        "subskill": "27_catapult_mechanism_elastic_to_kinetic",
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
        "learning_objective_id": "ns7_pk_27",
        "hints": {
            "tier_1": "Does pulling an elastic band further back store more or less energy?",
            "tier_2": "More stretch = more elastic potential energy = higher launch speed (kinetic energy).",
            "tier_3": "It will launch with greater kinetic energy and travel further.",
        },
        "misconception_tags": ["stretch_amount_does_not_affect_speed", "catapult_creates_energy"],
    }


# 28. Trampoline elastic potential rebound
def arch_28_trampoline_elastic_potential_rebound(rng: random.Random) -> Dict[str, Any]:
    gymnasts = [("an athlete bouncing on a competition trampoline", "the woven bed and steel perimeter springs"),
                 ("a child jumping on a backyard trampoline", "the tension springs and flexible mat")]
    context, parts = rng.choice(gymnasts)
    prompt = (
        f"Consider **{context}**.\n\n"
        f"At the lowest point of the bounce where **{parts}** are stretched downwards to their maximum limit, "
        f"what is the primary form of energy stored in the system?"
    )
    correct = "Elastic potential energy stored in the stretched trampoline springs and depressed mat."
    distractors = [
        "Gravitational potential energy at its highest maximum value.",
        "Kinetic energy of maximum downward speed.",
        "Chemical potential energy in the steel metal frame.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Trampoline Bounce Energy Stages:**\n"
        f"1. **Peak of jump:** Maximum gravitational potential energy (\\(E_p\\)), zero kinetic (\\(E_k = 0\\)).\n"
        f"2. **Descent:** \\(E_p\\) converts to kinetic energy \\(E_k\\) (fastest right before touching bed).\n"
        f"3. **Bottom of bounce:** Jumper decelerates to a momentary stop; kinetic energy is converted into **elastic potential energy** stored in {parts}.\n"
        f"4. **Rebound:** Springs contract, launching jumper upward."
    )
    return {
        "id": f"ns7_pk_28_{rng.randint(100000, 999999)}",
        "subskill": "28_trampoline_elastic_potential_rebound",
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
        "learning_objective_id": "ns7_pk_28",
        "hints": {
            "tier_1": "What is stretched to the maximum at the lowest point of the jump?",
            "tier_2": "The stretched springs store elastic potential energy.",
            "tier_3": "Elastic potential energy stored in the stretched springs and mat.",
        },
        "misconception_tags": ["kinetic_energy_is_maximum_at_lowest_point", "trampolines_absorb_energy_permanently"],
    }


# 29. Windup mechanical clockwork toy
def arch_29_windup_mechanical_clockwork_toy(rng: random.Random) -> Dict[str, Any]:
    toys = [
        ("a clockwork wind-up toy car with a metal spiral mainspring", "driving the axle gears and wheels forward across the carpet"),
        ("a mechanical wind-up music box with a coiled spring", "spinning a pinned metal cylinder against musical comb teeth"),
    ]
    toy_name, purpose = rng.choice(toys)
    prompt = (
        f"A child turns the winding key of **{toy_name}**, then sets it down on a table.\n\n"
        f"Which statement describes the energy changes that occur during winding and running?"
    )
    correct = (
        f"Winding does work to tightly coil the internal spring storing **elastic potential energy**; "
        f"as the spring slowly uncoils, it converts stored energy into **kinetic energy** ({purpose})."
    )
    distractors = [
        "Winding pumps electrical battery acid into the wheels to create electromagnetic waves.",
        "Winding heats up the air inside the toy to boil water into steam power.",
        "Winding creates nuclear fusion inside the steel casing that emits light.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Clockwork Mechanism Energy Sequence:**\n"
        f"1. **Input:** Muscular work turns key -> coils spiral spring tightly -> stores **elastic potential energy**.\n"
        f"2. **Release:** Escapement mechanism allows spring to unwind gradually, transferring energy to gears as **kinetic energy** ({purpose}).\n"
        f"3. Dissipation: Small amounts of sound (clicking) and thermal heat (friction) escape to surroundings."
    )
    return {
        "id": f"ns7_pk_29_{rng.randint(100000, 999999)}",
        "subskill": "29_windup_mechanical_clockwork_toy",
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
        "learning_objective_id": "ns7_pk_29",
        "hints": {
            "tier_1": "What type of energy does a tightly coiled spiral spring store?",
            "tier_2": "Coiling a spring stores elastic potential energy; unwinding turns into kinetic motion.",
            "tier_3": f"Stores elastic potential energy; uncoiling converts it into kinetic energy ({purpose}).",
        },
        "misconception_tags": ["clockwork_toys_use_batteries", "springs_generate_heat_only"],
    }


# 30. Hydroelectric dam water potential to kinetic
def arch_30_hydroelectric_dam_water_potential_to_kinetic(rng: random.Random) -> Dict[str, Any]:
    head_heights = [(60, "Gariep Dam"), (120, "Vanderkloof Dam")]
    height_m, dam_name = rng.choice(head_heights)
    prompt = (
        f"At **{dam_name}**, billions of liters of water are held in the reservoir at a height of **{height_m} meters** above the turbine hall.\n\n"
        f"When control sluice gates open and water rushes down the penstock pipes, what transformation occurs before the water hits the turbine blades?"
    )
    correct = "The **gravitational potential energy** of elevated water converts directly into the **kinetic energy** of fast-moving water."
    distractors = [
        "The water's kinetic energy converts into chemical potential energy inside hydrogen atoms.",
        "The water loses all mass and becomes electromagnetic light waves.",
        "The water freezes into ice due to the destruction of gravitational potential energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Hydroelectric Penstock Energy Transfer:**\n"
        f"- Water in the high reservoir possesses **gravitational potential energy** (\\(E_p = mgh\\)).\n"
        f"- As water plunges {height_m} meters down the penstocks, gravity accelerates it to high velocity.\n"
        f"- Thus, \\(E_p\\) converts into **kinetic energy** of the rushing water, which then strikes and rotates the turbine runner."
    )
    return {
        "id": f"ns7_pk_30_{rng.randint(100000, 999999)}",
        "subskill": "30_hydroelectric_dam_water_potential_to_kinetic",
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
        "learning_objective_id": "ns7_pk_30",
        "hints": {
            "tier_1": "What happens when elevated water rushes downhill through pipes?",
            "tier_2": "Height (gravitational potential) converts into rushing motion (kinetic).",
            "tier_3": "Gravitational potential energy converts directly into kinetic energy of rushing water.",
        },
        "misconception_tags": ["water_has_chemical_combustion", "hydro_creates_energy_out_of_nothing"],
    }


# 31. Falling meteor or skydiver terminal velocity
def arch_31_falling_meteor_or_skydiver_terminal_velocity(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A skydiver in a belly-to-earth freefall reaching terminal velocity (~200 km/h) in the atmosphere",
         "gravitational potential energy is converted into kinetic energy and then dissipated into thermal energy via atmospheric friction (air drag)"),
        ("A meteoroid descending through Earth's upper atmosphere at high speed",
         "its massive gravitational and kinetic energy is converted into intense thermal energy and light via severe atmospheric compression and friction"),
    ]
    event, mechanism = rng.choice(scenarios)
    prompt = (
        f"Consider the physics of **{event}**.\n\n"
        f"Once an object reaches a constant **terminal velocity**, why does it stop accelerating even though gravity is still pulling it downward?"
    )
    correct = (
        "Upward air resistance (drag) equals the downward force of gravity, so net force is zero; "
        "further loss of gravitational potential energy is converted entirely into thermal heat in the surrounding air."
    )
    distractors = [
        "Gravity stops acting on the object once it enters the troposphere.",
        "The object loses 100% of its physical mass and floats weightlessly in the air.",
        "The object creates an antigravity magnetic field that propels it upward.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Terminal Velocity and Energy Balance:**\n"
        f"1. **Forces:** When downward gravity (\\(F_g = mg\\)) equals upward aerodynamic drag (\\(F_\\text{{drag}}\\)), net force = 0, so acceleration ceases.\n"
        f"2. **Energy:** As the object continues descending at constant speed (constant kinetic energy), {mechanism}."
    )
    return {
        "id": f"ns7_pk_31_{rng.randint(100000, 999999)}",
        "subskill": "31_falling_meteor_or_skydiver_terminal_velocity",
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
        "learning_objective_id": "ns7_pk_31",
        "hints": {
            "tier_1": "What happens when air resistance pushes up with the same force as gravity pulls down?",
            "tier_2": "Forces balance, so velocity becomes constant (terminal velocity).",
            "tier_3": "Upward air resistance equals downward gravity; potential energy loss becomes heat in air.",
        },
        "misconception_tags": ["gravity_disappears_at_terminal_velocity", "terminal_velocity_means_stopping"],
    }


# 32. Law of conservation of energy statement
def arch_32_law_of_conservation_of_energy_statement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Law of Conservation of Energy** is one of the most fundamental principles in all of science.\n\n"
        "Which statement correctly states this universal law?"
    )
    correct = "Energy cannot be created or destroyed; it can only be transferred from one system to another or transformed from one form to another."
    distractors = [
        "Energy is naturally destroyed whenever an object comes to a stop due to friction.",
        "New energy is created whenever an electric lamp or candle is ignited.",
        "Energy can only exist in living organisms and disappears in non-living machines.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Law of Conservation of Energy:**\n"
        f"- **Universal Invariant:** Energy cannot be created out of nothing, nor can it be permanently destroyed into nothing.\n"
        f"- It only **transforms** (e.g. chemical -> electrical -> light + heat) or **transfers** between systems.\n"
        f"- Total energy in a closed/isolated universe remains strictly **constant**."
    )
    return {
        "id": f"ns7_pk_32_{rng.randint(100000, 999999)}",
        "subskill": "32_law_of_conservation_of_energy_statement",
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
        "learning_objective_id": "ns7_pk_32",
        "hints": {
            "tier_1": "Can energy be made from nothing or destroyed into nothing?",
            "tier_2": "Energy cannot be created or destroyed, only transformed.",
            "tier_3": "Energy cannot be created or destroyed; it can only be transferred or transformed.",
        },
        "misconception_tags": ["energy_is_consumed_and_disappears", "friction_destroys_energy"],
    }


# 33. Conservation of energy pendulum system
def arch_33_conservation_of_energy_pendulum_system(rng: random.Random) -> Dict[str, Any]:
    energies = [(10, 0, 10), (25, 0, 25), (50, 0, 50)]
    ep_top, ek_top, total = rng.choice(energies)
    half_ep = total / 2
    prompt = (
        f"A simple pendulum swings in an idealized frictionless system.\n"
        f"At its highest point A, its gravitational potential energy is **{ep_top} J** and its kinetic energy is **{ek_top} J** "
        f"(total mechanical energy = **{total} J**).\n\n"
        f"What will be its kinetic energy when it swings halfway down, where its potential energy has dropped to **{half_ep:g} J**?"
    )
    correct = f"**{half_ep:g} J**, because total mechanical energy (\\(E_p + E_k\\)) must remain constant at {total} J."
    distractors = [
        f"**0 J**, because a pendulum only possesses energy at its endpoints.",
        f"**{total * 2} J**, because gravity adds new energy during the downward swing.",
        f"**{total} J**, because kinetic energy is always equal to total energy at all points.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Conservation of Mechanical Energy Calculation:**\n"
        f"$$\\text{{Total Mechanical Energy}} = E_p + E_k$$\n"
        f"At top: \\(\\text{{Total}} = {ep_top}\\text{{ J}} + {ek_top}\\text{{ J}} = {total}\\text{{ J}}\\).\n"
        f"Halfway down: \\(E_p = {half_ep:g}\\text{{ J}}\\).\n"
        f"$$E_k = \\text{{Total}} - E_p = {total}\\text{{ J}} - {half_ep:g}\\text{{ J}} = \\mathbf{{{half_ep:g}\\text{{ J}}}}$."
    )
    return {
        "id": f"ns7_pk_33_{rng.randint(100000, 999999)}",
        "subskill": "33_conservation_of_energy_pendulum_system",
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
        "learning_objective_id": "ns7_pk_33",
        "hints": {
            "tier_1": "Total energy stays constant at all points: \\(E_p + E_k = \\text{Total}\\).",
            "tier_2": f"Subtract {half_ep:g} J from total {total} J.",
            "tier_3": f"{half_ep:g} J, because total energy must remain {total} J.",
        },
        "misconception_tags": ["energy_is_lost_at_midpoints", "kinetic_energy_does_not_depend_on_potential"],
    }


# 34. Energy dissipation friction and sound
def arch_34_energy_dissipation_friction_and_sound(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A child riding a wooden cart down a gentle slope gradually slowing down and stopping on level ground",
         "mechanical kinetic energy is transformed into thermal energy (heat in wheel axles and ground) and sound"),
        ("A swinging playground pendulum gradually losing height with each swing until coming to rest",
         "mechanical energy is dissipated into thermal energy via air resistance and pivot friction"),
    ]
    event, mechanism = rng.choice(scenarios)
    prompt = (
        f"Consider this observation:\n*{event}*\n\n"
        f"According to the Law of Conservation of Energy, why does the object eventually stop moving?"
    )
    correct = f"Its mechanical energy is not destroyed, but is **dissipated** (spread out) into the surroundings as {mechanism}."
    distractors = [
        "Its kinetic energy is destroyed permanently into nothingness by friction.",
        "Gravity stops pulling on the object once it has traveled more than 10 meters.",
        "The object creates cold dark matter that freezes its atoms solid.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Concept of Energy Dissipation:**\n"
        f"- When mechanical systems operate in the real world, friction and air resistance oppose motion.\n"
        f"- Work done against friction transforms useful kinetic energy into **wasted thermal energy** (heat) and **sound waves**.\n"
        f"- This energy dissipates (spreads out) into the surrounding environment and becomes less useful, but the total energy of the universe is unchanged."
    )
    return {
        "id": f"ns7_pk_34_{rng.randint(100000, 999999)}",
        "subskill": "34_energy_dissipation_friction_and_sound",
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
        "learning_objective_id": "ns7_pk_34",
        "hints": {
            "tier_1": "Does friction destroy energy or convert it to heat and sound?",
            "tier_2": "Friction converts kinetic motion into thermal heat that warms surroundings.",
            "tier_3": "Mechanical energy is dissipated into the surroundings as thermal energy and sound.",
        },
        "misconception_tags": ["friction_destroys_energy_completely", "stopping_proves_conservation_is_false"],
    }


# 35. Sankey diagram energy balance concept
def arch_35_sankey_diagram_energy_balance_concept(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an incandescent filament light bulb", 100, 10, 90, "Light energy", "Thermal heat wasted to air"),
        ("an electric blender", 200, 140, 60, "Kinetic energy of blades", "Heat and sound wasted to surroundings"),
        ("a car petrol engine", 500, 150, 350, "Mechanical motion of car", "Thermal heat in radiator and exhaust"),
    ]
    app, input_j, useful_j, wasted_j, useful_label, wasted_label = rng.choice(appliances)
    prompt = (
        f"In an energy balance analysis for **{app}**:\n"
        f"- **Input energy:** {input_j} J (electrical/fuel)\n"
        f"- **Useful output energy:** {useful_j} J ({useful_label})\n"
        f"- **Wasted output energy:** {wasted_j} J ({wasted_label})\n\n"
        f"How does this energy balance demonstrate the Law of Conservation of Energy?"
    )
    correct = f"Total Input ({input_j} J) = Useful Output ({useful_j} J) + Wasted Output ({wasted_j} J); no energy is lost or created."
    distractors = [
        f"The system created {wasted_j} J of brand new energy from nothing.",
        f"The {wasted_j} J was destroyed and ceased to exist in the universe.",
        "Conservation of energy failed because useful output is less than input.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Sankey Energy Accounting:**\n"
        f"$$\\text{{Total Input Energy}} = \\text{{Useful Output Energy}} + \\text{{Wasted Dissipated Energy}}$$\n"
        f"$${input_j}\\text{{ J}} = {useful_j}\\text{{ J}} + {wasted_j}\\text{{ J}}$$\n"
        f"Even though only {useful_j} J performed the intended task, every single Joule is accounted for in the system balance."
    )
    return {
        "id": f"ns7_pk_35_{rng.randint(100000, 999999)}",
        "subskill": "35_sankey_diagram_energy_balance_concept",
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
        "learning_objective_id": "ns7_pk_35",
        "hints": {
            "tier_1": "Check the math: does useful + wasted equal the total input?",
            "tier_2": f"{useful_j} + {wasted_j} = {input_j}.",
            "tier_3": f"Total Input ({input_j} J) = Useful Output ({useful_j} J) + Wasted Output ({wasted_j} J).",
        },
        "misconception_tags": ["efficiency_below_100_violates_conservation", "wasted_energy_disappears"],
    }


# 36. Calculating proportional potential energy height
def arch_36_calculating_proportional_potential_energy_height(rng: random.Random) -> Dict[str, Any]:
    heights = [(2, 4, 30, 60), (1.5, 4.5, 20, 60), (3, 6, 45, 90)]
    h1, h2, ep1, ep2 = rng.choice(heights)
    ratio = int(h2 / h1)
    prompt = (
        f"A 2 kg brick held at a height of **{h1} meters** stores **{ep1} J** of gravitational potential energy.\n\n"
        f"If the same brick is lifted to a height of **{h2} meters** ({ratio} times higher), "
        f"how much gravitational potential energy does it now store?"
    )
    correct = f"**{ep2} J**, because gravitational potential energy is directly proportional to height (\\(E_p \\propto h\\))."
    distractors = [
        f"**{ep1} J**, because the mass of the brick did not change.",
        f"**{ep1 + 5} J**, because energy only increases by 5 J for every meter.",
        f"**{ep2 * 4} J**, because potential energy depends on the square of the height.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Proportional Reasoning for \\(E_p = mgh\\):**\n"
        f"- Since mass \\(m\\) and gravity \\(g\\) are constant, \\(E_p \\propto h\\).\n"
        f"- Height ratio: \\(\\frac{{{h2}}}{{{h1}}} = {ratio}\\).\n"
        f"- New potential energy: \\({ep1}\\text{{ J}} \\times {ratio} = \\mathbf{{{ep2}\\text{{ J}}}}\\)."
    )
    return {
        "id": f"ns7_pk_36_{rng.randint(100000, 999999)}",
        "subskill": "36_calculating_proportional_potential_energy_height",
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
        "learning_objective_id": "ns7_pk_36",
        "hints": {
            "tier_1": f"The height increased by a factor of {ratio}.",
            "tier_2": f"Multiply the initial energy ({ep1} J) by {ratio}.",
            "tier_3": f"{ep2} J, because potential energy is directly proportional to height.",
        },
        "misconception_tags": ["height_has_quadratic_relationship", "mass_is_the_only_factor"],
    }


# 37. Calculating proportional potential energy mass
def arch_37_calculating_proportional_potential_energy_mass(rng: random.Random) -> Dict[str, Any]:
    masses = [(1, 3, 25, 75), (2, 4, 40, 80), (1.5, 3.0, 30, 60)]
    m1, m2, ep1, ep2 = rng.choice(masses)
    ratio = int(m2 / m1)
    prompt = (
        f"A **{m1} kg** box placed on a laboratory shelf stores **{ep1} J** of gravitational potential energy.\n\n"
        f"A heavier **{m2} kg** box is placed on the exact same shelf at the same height.\n"
        f"How much gravitational potential energy does the {m2} kg box store?"
    )
    correct = f"**{ep2} J**, because gravitational potential energy is directly proportional to mass (\\(E_p \\propto m\\))."
    distractors = [
        f"**{ep1} J**, because both boxes are resting at the same height.",
        f"**{ep2 * 3} J**, because mass increases energy exponentially.",
        f"**0 J**, because heavier boxes sink into the shelf.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Proportional Reasoning for Mass:**\n"
        f"- At the same height and gravity, \\(E_p = mgh \\propto m\\).\n"
        f"- Mass ratio: \\(\\frac{{{m2}}}{{{m1}}} = {ratio}\\).\n"
        f"- New potential energy: \\({ep1}\\text{{ J}} \\times {ratio} = \\mathbf{{{ep2}\\text{{ J}}}}\\)."
    )
    return {
        "id": f"ns7_pk_37_{rng.randint(100000, 999999)}",
        "subskill": "37_calculating_proportional_potential_energy_mass",
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
        "learning_objective_id": "ns7_pk_37",
        "hints": {
            "tier_1": f"The mass increased by a factor of {ratio}.",
            "tier_2": f"Multiply the initial energy ({ep1} J) by {ratio}.",
            "tier_3": f"{ep2} J, because potential energy is directly proportional to mass.",
        },
        "misconception_tags": ["all_objects_at_same_height_have_same_energy", "mass_does_not_scale_linearly"],
    }


# 38. Qualitative kinetic energy comparison
def arch_38_qualitative_kinetic_energy_comparison(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("A heavy railway freight train moving at 30 km/h vs a cyclist moving at 30 km/h", "the freight train", "its mass is thousands of times greater than the cyclist, resulting in vastly higher kinetic energy"),
        ("A fast-pitch cricket ball thrown at 140 km/h vs a gently tossed cricket ball at 30 km/h", "the fast-pitch cricket ball", "its speed is much higher, and kinetic energy scales with speed squared"),
    ]
    comparison, winner, reason = rng.choice(cases)
    prompt = (
        f"Consider this comparison:\n*{comparison}*\n\n"
        f"Which object possesses significantly greater **kinetic energy**, and what is the scientific justification?"
    )
    correct = f"**{winner.capitalize()}**, because {reason}."
    distractors = [
        "Both have identical kinetic energy because both exist in the same town.",
        "Neither has kinetic energy because they are not powered by rocket fuel.",
        "The other object has greater kinetic energy because small objects travel through time.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Kinetic Energy Comparison (\\(E_k = \\frac{{1}}{{2}}mv^2\\)):**\n"
        f"- Depends directly on mass (\\(m\\)) and the square of velocity (\\(v^2\\)).\n"
        f"- In this comparison: **{winner.capitalize()}** has vastly greater kinetic energy because {reason}."
    )
    return {
        "id": f"ns7_pk_38_{rng.randint(100000, 999999)}",
        "subskill": "38_qualitative_kinetic_energy_comparison",
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
        "learning_objective_id": "ns7_pk_38",
        "hints": {
            "tier_1": "Check whether mass is vastly different or speed is vastly different.",
            "tier_2": "Recall \\(E_k = \\frac{1}{2}mv^2\\).",
            "tier_3": f"{winner.capitalize()}, because {reason}.",
        },
        "misconception_tags": ["equal_speeds_always_mean_equal_energy", "lighter_objects_always_have_more_energy"],
    }


# 39. Skateboarder halfpipe energy exchange
def arch_39_skateboarder_halfpipe_energy_exchange(rng: random.Random) -> Dict[str, Any]:
    heights = [(3, "a 3-meter U-shaped skate ramp"), (4, "a 4-meter professional halfpipe")]
    h, ramp_name = rng.choice(heights)
    prompt = (
        f"A skateboarder drops into **{ramp_name}** from the top coping edge.\n\n"
        f"Where along the halfpipe does the skateboarder experience **maximum speed (maximum kinetic energy)**, "
        f"and where is the **gravitational potential energy greatest**?"
    )
    correct = "Maximum kinetic energy (fastest speed) is at the flat bottom of the curve; maximum potential energy is at the highest points on the left and right coping rims."
    distractors = [
        "Maximum kinetic energy is at the top rim; maximum potential energy is at the bottom.",
        "Kinetic energy is identical at all points; potential energy is zero everywhere.",
        "Maximum speed occurs only while airborne outside the skate park.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Halfpipe Energy Exchange:**\n"
        f"1. **Top Coping Rim (Maximum Height \\(h\\)):** Maximum gravitational potential energy (\\(E_p\\)), minimum kinetic energy.\n"
        f"2. **Descent:** \\(E_p\\) converts into \\(E_k\\) as gravity accelerates the skateboarder.\n"
        f"3. **Flat Bottom (Lowest point \\(h = 0\\)):** Maximum kinetic energy (\\(E_k\\)) and maximum speed.\n"
        f"4. **Ascent:** \\(E_k\\) converts back into \\(E_p\\) as the skater rises up the opposite wall."
    )
    return {
        "id": f"ns7_pk_39_{rng.randint(100000, 999999)}",
        "subskill": "39_skateboarder_halfpipe_energy_exchange",
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
        "learning_objective_id": "ns7_pk_39",
        "hints": {
            "tier_1": "Where are you lowest and fastest? Where are you highest and momentarily stationary?",
            "tier_2": "Fastest at the bottom (max kinetic); highest at the rims (max potential).",
            "tier_3": "Max kinetic at the bottom; max potential at highest coping rims.",
        },
        "misconception_tags": ["fastest_at_the_highest_point", "skaters_accelerate_when_going_up"],
    }


# 40. Swing playground energy transfer
def arch_40_swing_playground_energy_transfer(rng: random.Random) -> Dict[str, Any]:
    riders = [("a learner on a playground swing", "pumps legs at the bottom of the swing arc"),
              ("a child swinging on a park swing", "leans back and kicks legs forward periodically")]
    who, pumping_action = rng.choice(riders)
    prompt = (
        f"When **{who}** ({pumping_action}), the swing goes higher and higher.\n\n"
        f"From an energy perspective, why does pumping legs increase the height of the swing?"
    )
    correct = "Muscular chemical potential energy does work to add mechanical energy to the system, overcoming friction and raising total mechanical energy."
    distractors = [
        "Pumping legs eliminates the force of gravity completely from the playground.",
        "Kicking legs creates cold nuclear fission inside the metal chains.",
        "Swinging creates negative mass that makes the child lighter than air.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Pumping a Swing:**\n"
        f"- Without input, friction (air resistance and pivot friction) dissipates energy, causing swings to decrease in amplitude.\n"
        f"- By {pumping_action}, the rider does mechanical work, converting **chemical potential energy** from food/muscles into added mechanical energy.\n"
        f"- This increases the total energy of the swing system, allowing higher maximum potential energy at the crests."
    )
    return {
        "id": f"ns7_pk_40_{rng.randint(100000, 999999)}",
        "subskill": "40_swing_playground_energy_transfer",
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
        "learning_objective_id": "ns7_pk_40",
        "hints": {
            "tier_1": "Where does the extra energy come from when you pump your legs?",
            "tier_2": "Your muscles do work, adding energy to the swinging system.",
            "tier_3": "Muscular chemical potential energy does work to add mechanical energy.",
        },
        "misconception_tags": ["swings_go_higher_automatically", "kicking_destroys_gravity"],
    }


# 41. Compressed air pneumatic system
def arch_41_compressed_air_pneumatic_system(rng: random.Random) -> Dict[str, Any]:
    devices = [
        ("a manual bicycle tire pump with the nozzle blocked by a thumb", "the trapped air is compressed into a smaller volume"),
        ("a pneumatic paintball marker or air rifle reservoir", "pressurized gas is packed under high pressure behind a valve"),
    ]
    device, state = rng.choice(devices)
    prompt = (
        f"Consider **{device}**.\n\n"
        f"When {state}, what type of energy is stored in the compressed gas, and what happens when the pressure is released?"
    )
    correct = "It stores **elastic potential energy (pressure potential)**; upon release, the gas expands rapidly, converting stored energy into kinetic motion."
    distractors = [
        "It stores gravitational energy that makes the pump fall upward.",
        "It stores nuclear radiation that dissolves the pump cylinder.",
        "It stores zero energy because gases cannot interact with mechanical forces.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Pneumatic Energy Storage:**\n"
        f"- Work is done compressing gas particles closer together against internal pressure.\n"
        f"- This stores **elastic potential energy** (pneumatic / pressure potential).\n"
        f"- When the valve or nozzle is opened, the gas expands forcefully, converting potential energy into **kinetic energy** (motion of gas and projectiles)."
    )
    return {
        "id": f"ns7_pk_41_{rng.randint(100000, 999999)}",
        "subskill": "41_compressed_air_pneumatic_system",
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
        "learning_objective_id": "ns7_pk_41",
        "hints": {
            "tier_1": "Think of compressed gas acting like a compressed spring.",
            "tier_2": "Compressed gas stores elastic potential energy that expands into kinetic motion.",
            "tier_3": "Stores elastic potential energy; expanding gas converts it into kinetic motion.",
        },
        "misconception_tags": ["air_has_no_energy", "gases_cannot_store_potential_energy"],
    }


# 42. Chemical to mechanical car engine
def arch_42_chemical_to_mechanical_car_engine(rng: random.Random) -> Dict[str, Any]:
    engines = [("an internal combustion petrol car engine", "spark plug ignites atomized fuel"),
               ("a heavy-duty diesel transport truck engine", "compression ignition of diesel fuel")]
    engine_name, ignition = rng.choice(engines)
    prompt = (
        f"Inside **{engine_name}**, {ignition} inside the combustion chamber.\n\n"
        f"Which chain accurately represents the transformation of energy from fuel to vehicle movement?"
    )
    correct = (
        "Chemical potential energy in fuel -> Thermal energy (expanding hot combustion gases) -> "
        "Kinetic energy (moving pistons and spinning driveshaft) -> Kinetic energy of vehicle moving forward."
    )
    distractors = [
        "Electrical energy -> Gravitational potential -> Nuclear fission -> Light energy.",
        "Sound energy -> Chemical potential energy -> Gravity -> Heat energy.",
        "Kinetic energy in exhaust -> Chemical bonds in tires -> Sound in headlights.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Engine Energy Transformation Sequence:**\n"
        f"1. **Fuel Tank:** Chemical potential energy stored in hydrocarbon bonds.\n"
        f"2. **Combustion:** Rapid reaction with oxygen releases **thermal energy**, raising gas temperature and pressure.\n"
        f"3. **Mechanical Stroke:** Expanding hot gas pushes pistons down -> **Kinetic energy** of engine parts.\n"
        f"4. **Drivetrain:** Rotates wheels -> **Kinetic energy** of the moving vehicle (with thermal heat and sound dissipated as waste)."
    )
    return {
        "id": f"ns7_pk_42_{rng.randint(100000, 999999)}",
        "subskill": "42_chemical_to_mechanical_car_engine",
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
        "learning_objective_id": "ns7_pk_42",
        "hints": {
            "tier_1": "Start with fuel bonds and end with the moving car.",
            "tier_2": "Chemical energy burns (heat) -> pushes pistons (kinetic) -> moves car.",
            "tier_3": "Chemical potential -> Thermal energy -> Kinetic energy of pistons -> Kinetic energy of vehicle.",
        },
        "misconception_tags": ["petrol_contains_pure_electricity", "engines_have_100_percent_efficiency"],
    }


# 43. Electric kettle energy transformation
def arch_43_electric_kettle_energy_transformation(rng: random.Random) -> Dict[str, Any]:
    kettles = [("a 2 000 W domestic electric kettle plugged into a 230 V wall socket", "1.5 liters of cold tap water")]
    item, water_vol = rng.choice(kettles)
    prompt = (
        f"A learner switches on **{item}** to boil {water_vol}.\n\n"
        f"What is the intended useful energy transformation inside the kettle element?"
    )
    correct = "Electrical energy from the wall socket is converted into thermal (heat) energy in the heating element and water."
    distractors = [
        "Gravitational energy is converted into nuclear fission inside water molecules.",
        "Sound energy is converted into chemical potential energy inside copper pipes.",
        "Light energy is converted into magnetic potential energy to freeze water.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Kettle Energy Conversion:**\n"
        f"1. **Input:** Electrical current flows through a high-resistance heating element (e.g. nichrome wire).\n"
        f"2. **Useful Output:** Resistance heats the element, transferring **thermal energy** to water molecules by conduction and convection.\n"
        f"3. **Wasted Output:** Sound (bubbling/hissing) and heat escaping through kettle walls."
    )
    return {
        "id": f"ns7_pk_43_{rng.randint(100000, 999999)}",
        "subskill": "43_electric_kettle_energy_transformation",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "ns7_pk_43",
        "hints": {
            "tier_1": "What enters through the plug, and what happens to the water?",
            "tier_2": "Electricity enters; thermal heat warms the water.",
            "tier_3": "Electrical energy is converted into thermal (heat) energy.",
        },
        "misconception_tags": ["kettles_use_chemical_combustion", "water_boils_from_light"],
    }


# 44. Battery powered flashlight circuit
def arch_44_battery_powered_flashlight_circuit(rng: random.Random) -> Dict[str, Any]:
    torches = [("a portable LED flashlight", "chemical cells (batteries), a slide switch, and a light-emitting diode")]
    torch, parts = rng.choice(torches)
    prompt = (
        f"Consider **{torch}** composed of **{parts}**.\n\n"
        f"Which sequence accurately outlines the multi-stage energy transfers that occur from switching it on to projecting a beam of light?"
    )
    correct = (
        "Chemical potential energy in battery -> Electrical energy (kinetic electron flow in circuit) -> "
        "Radiant light energy (useful output) + Thermal heat energy (wasted dissipation)."
    )
    distractors = [
        "Nuclear energy in switch -> Gravitational potential in wires -> Magnetic sound waves.",
        "Sound energy in casing -> Chemical energy in LED -> Kinetic motion of batteries.",
        "Thermal heat in room -> Electrical energy -> Chemical storage in flashlight glass.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Flashlight System Energy Flow:**\n"
        f"1. **Battery:** Chemical potential energy stored in reactants.\n"
        f"2. **Circuit:** Converts to **electrical energy** when switch closes.\n"
        f"3. **LED:** Converts electrical energy primarily into **radiant light energy** (useful) and some **thermal heat** (wasted)."
    )
    return {
        "id": f"ns7_pk_44_{rng.randint(100000, 999999)}",
        "subskill": "44_battery_powered_flashlight_circuit",
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
        "learning_objective_id": "ns7_pk_44",
        "hints": {
            "tier_1": "Battery (chemical) -> Circuit (electrical) -> Lamp (light + heat).",
            "tier_2": "Trace energy step-by-step from chemicals to the light beam.",
            "tier_3": "Chemical potential -> Electrical energy -> Radiant light + Thermal heat.",
        },
        "misconception_tags": ["batteries_store_pure_light", "leds_have_zero_energy_transformations"],
    }


# 45. Misconception energy gets used up disappears
def arch_45_misconception_energy_gets_used_up_disappears(rng: random.Random) -> Dict[str, Any]:
    claims = [
        ("When a car runs out of petrol, people say 'all the energy was used up and disappeared into nothing'.",
         "The chemical potential energy was not destroyed; it transformed into kinetic motion of the car, and was ultimately dissipated as heat in the road, brakes, and air, plus sound waves."),
        ("When a swinging pendulum stops swinging, a student claims 'its energy died and vanished from the universe'.",
         "The mechanical energy was not obliterated; friction at the pivot and drag against air particles transformed it into thermal heat that dispersed into the surrounding room."),
    ]
    statement, correction = rng.choice(claims)
    prompt = (
        f"In everyday language, people often say energy has been 'used up'.\n\n"
        f"Consider this scenario:\n*{statement}*\n\n"
        f"Why is the claim that energy 'disappeared or was destroyed' scientifically incorrect?"
    )
    correct = correction
    distractors = [
        "Because energy never changes form under any physical circumstances.",
        "Because the object secretly stores the energy inside parallel dimensions.",
        "Because petrol engines actually generate fresh coal underground while driving.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Scientific Misconception Clarification:**\n"
        f"- Everyday phrase 'energy is used up' means energy has been converted from a **useful concentrated form** (e.g. petrol, motion) into a **less useful dispersed form** (ambient heat).\n"
        f"- {correction}\n"
        f"- Conservation of energy holds universally: \\(\\Delta E_{{\\text{{universe}}}} = 0\\)."
    )
    return {
        "id": f"ns7_pk_45_{rng.randint(100000, 999999)}",
        "subskill": "45_misconception_energy_gets_used_up_disappears",
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
        "learning_objective_id": "ns7_pk_45",
        "hints": {
            "tier_1": "Can energy be destroyed?",
            "tier_2": "Energy cannot be destroyed; it dissipates as heat and sound into surroundings.",
            "tier_3": f"{correction}",
        },
        "misconception_tags": ["energy_is_destroyed_by_use", "used_up_means_vanished"],
    }


# 46. Misconception stationary objects have no energy
def arch_46_misconception_stationary_objects_have_no_energy(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A heavy boulder perched precariously at the top of a steep mountain cliff", "gravitational potential energy"),
        ("A stick of dynamite resting quietly inside a locked storage crate", "chemical potential energy"),
        ("A compressed industrial coil spring clamped in a vise", "elastic potential energy"),
    ]
    obj, energy_form = rng.choice(examples)
    prompt = (
        f"A common misconception is that if an object is completely stationary and unmoving, it contains zero energy.\n\n"
        f"Why is this misconception refuted by **{obj}**?"
    )
    correct = f"Although its kinetic energy is zero because it is not in motion, it stores immense **{energy_form}** that can do substantial work when released."
    distractors = [
        "Because stationary objects are actually moving faster than light in secret.",
        "Because all stationary objects generate electrical lightning continuously.",
        "Because potential energy only exists when an object is falling at terminal speed.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Refuting the Stationary Energy Myth:**\n"
        f"- Kinetic energy requires velocity: \\(v = 0 \\implies E_k = 0\\).\n"
        f"- However, **potential energy** does not require motion; it depends on position, configuration, or chemical bonds.\n"
        f"- {obj} stores substantial **{energy_form}** waiting to be released."
    )
    return {
        "id": f"ns7_pk_46_{rng.randint(100000, 999999)}",
        "subskill": "46_misconception_stationary_objects_have_no_energy",
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
        "learning_objective_id": "ns7_pk_46",
        "hints": {
            "tier_1": "Does a boulder at the top of a mountain have energy even before it falls?",
            "tier_2": "It has potential energy stored due to its position.",
            "tier_3": f"Kinetic energy is zero, but it stores immense {energy_form}.",
        },
        "misconception_tags": ["stationary_objects_have_zero_energy", "energy_only_exists_in_motion"],
    }


# 47. Misconception heavier objects fall with more energy
def arch_47_misconception_heavier_objects_fall_with_more_energy(rng: random.Random) -> Dict[str, Any]:
    pairs = [("a 5 kg cannonball and a 0.5 kg wooden ball dropped simultaneously from the same height of 10 meters in a vacuum",
              "both fall with identical acceleration (g) and reach the ground with identical speed, but the 5 kg ball has 10 times more kinetic energy because of its greater mass")]
    pair, reality = rng.choice(pairs)
    prompt = (
        f"Consider **{pair}**.\n\n"
        f"Which statement correctly clarifies the relationship between mass, acceleration, falling speed, and energy?"
    )
    correct = f"In a vacuum, {reality}."
    distractors = [
        "The heavier ball falls 10 times faster because gravity pulls heavy objects with greater acceleration.",
        "Both balls have identical kinetic energy because gravity exerts equal force on all masses.",
        "The lighter ball falls faster because air pushes it downward with greater pressure.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Galilean Principle vs Energy Dynamics:**\n"
        f"1. **Kinematics:** Acceleration due to gravity (\\(g\\)) is independent of mass: \\(a = g \\approx 9.8\\text{{ m/s}}^2\\). Both hit the ground at identical speed (\\(v = \\sqrt{{2gh}}\\)).\n"
        f"2. **Energy:** Kinetic energy is \\(E_k = \\frac{{1}}{{2}}mv^2\\). Because the heavier ball has 10x mass, its kinetic energy is 10x greater."
    )
    return {
        "id": f"ns7_pk_47_{rng.randint(100000, 999999)}",
        "subskill": "47_misconception_heavier_objects_fall_with_more_energy",
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
        "learning_objective_id": "ns7_pk_47",
        "hints": {
            "tier_1": "Do all objects fall with the same acceleration in a vacuum?",
            "tier_2": "They fall at the same speed, but the heavier one has more kinetic energy because \\(E_k = \\frac{1}{2}mv^2\\).",
            "tier_3": f"{reality}.",
        },
        "misconception_tags": ["heavier_objects_fall_faster_in_vacuum", "mass_does_not_affect_impact_energy"],
    }


# 48. Misconception potential only means gravity
def arch_48_misconception_potential_only_means_gravity(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Chemical potential energy in glucose molecules powering cellular respiration", "bonds between carbon, hydrogen, and oxygen atoms"),
        ("Elastic potential energy in an archery bow stretched before release", "mechanical deformation of flexible polymer/wood fibers"),
    ]
    example, sub_source = rng.choice(types)
    prompt = (
        f"A learner states: *\"Potential energy only exists when something is lifted high off the ground.\"*\n\n"
        f"How does **{example}** ({sub_source}) prove this statement false?"
    )
    correct = "It shows that potential energy also exists as chemical potential in molecular bonds and elastic potential in deformed materials, completely independent of height above the ground."
    distractors = [
        "It proves that glucose molecules only exist on mountain tops.",
        "It shows that all potential energy turns into solid diamond crystals.",
        "It confirms that potential energy cannot exist on Earth.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Diversity of Potential Energy:**\n"
        f"Gravitational potential is only one form of stored energy.\n"
        f"- **Chemical Potential:** Stored in atomic bonds (food, fuels, batteries).\n"
        f"- **Elastic Potential:** Stored in mechanical deformation (springs, rubber, bent bows).\n"
        f"- Both exist even when flat on the ground at zero elevation."
    )
    return {
        "id": f"ns7_pk_48_{rng.randint(100000, 999999)}",
        "subskill": "48_misconception_potential_only_means_gravity",
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
        "learning_objective_id": "ns7_pk_48",
        "hints": {
            "tier_1": "Can food or a compressed spring store energy on the ground?",
            "tier_2": "Chemical and elastic energies are potential energies that do not need height.",
            "tier_3": "Potential energy also exists as chemical in molecular bonds and elastic in deformed materials.",
        },
        "misconception_tags": ["potential_energy_only_equals_gravity", "chemical_energy_is_kinetic"],
    }


# 49. Energy transformations in daily appliances
def arch_49_energy_transformations_in_daily_appliances(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("a microwave oven", "Electrical energy -> Radiant microwave energy -> Thermal kinetic energy of vibrating water molecules in food"),
        ("a hair dryer", "Electrical energy -> Thermal energy (heating coils) + Mechanical kinetic energy (spinning fan) + Sound energy"),
        ("an electric washing machine", "Electrical energy -> Mechanical kinetic energy (spinning drum) + Thermal energy (water heater) + Sound"),
    ]
    app, flow = rng.choice(appliances)
    prompt = (
        f"Domestic household appliances are systems designed to convert electrical input into specific useful outputs.\n\n"
        f"For **{app}**, which sequence correctly describes its energy transformation pathway?"
    )
    correct = flow
    distractors = [
        "Nuclear energy -> Gravitational potential energy -> Magnetic light.",
        "Chemical potential energy in wall -> Sound waves -> Zero energy.",
        "Light energy -> Cold radiation -> Chemical bonds in plastic casing.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Path in {app}:**\n"
        f"- **Input:** Electrical current.\n"
        f"- **Transformations:** **{flow}**.\n"
        f"- Useful vs Wasted: Useful output fulfills the appliance's function; wasted outputs (excess sound and heat) disperse into surroundings."
    )
    return {
        "id": f"ns7_pk_49_{rng.randint(100000, 999999)}",
        "subskill": "49_energy_transformations_in_daily_appliances",
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
        "learning_objective_id": "ns7_pk_49",
        "hints": {
            "tier_1": f"Think about what goes in and what comes out of {app}.",
            "tier_2": "Look for the sequence that matches electrical input to the active functions.",
            "tier_3": f"{flow}",
        },
        "misconception_tags": ["appliances_create_energy", "electricity_is_pure_heat"],
    }


# 50. Potential and kinetic energy comprehensive diagnostic
def arch_50_potential_and_kinetic_energy_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A downhill mountain biker pedals to the summit (chemical -> gravitational potential), coasts down a rugged mountain track at high speed (potential -> kinetic), and applies disc brakes to stop at the finish line (kinetic -> thermal heat in brake rotors and sound)",
         "Chemical potential -> Gravitational potential -> Kinetic energy -> Thermal heat and sound dissipation",
         "Total energy remains constant throughout; energy was transferred between systems and forms, with no energy created or destroyed"),
        ("A hydroelectric pumped-storage facility pumps water uphill at night using grid power (electrical -> gravitational potential), and releases it during daytime peak demand to drive turbines (potential -> kinetic -> electrical)",
         "Electrical energy -> Gravitational potential energy -> Kinetic water energy -> Electrical energy output",
         "The system acts as a mechanical energy store, strictly conserving total energy minus frictional dissipation losses"),
    ]
    story, sequence, law_application = rng.choice(scenarios)
    prompt = (
        f"**Comprehensive Systems Energy Diagnostic:**\n\n"
        f"Examine the physical scenario:\n*{story}*\n\n"
        f"Which analysis correctly identifies the full sequence of energy transformations and its alignment with the Law of Conservation of Energy?"
    )
    correct = f"Transformation Sequence: **{sequence}**.\nLaw Application: **{law_application}**."
    distractors = [
        f"Transformation Sequence: Nuclear -> Static electricity -> Cold void.\nLaw Application: Energy was permanently destroyed at the finish line.",
        f"Transformation Sequence: {sequence}.\nLaw Application: Energy increased tenfold because gravity creates free energy out of nothing.",
        f"Transformation Sequence: Light -> Chemical -> Sound only.\nLaw Application: Conservation laws do not apply to moving humans or water.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Comprehensive Diagnostic Solution:**\n"
        f"1. **Energy Transformations:** {sequence}.\n"
        f"2. **Conservation Law:** {law_application}.\n"
        f"This synthesis unifies stored potential forms, dynamic kinetic motion, dissipative mechanisms, and universal conservation."
    )
    return {
        "id": f"ns7_pk_50_{rng.randint(100000, 999999)}",
        "subskill": "50_potential_and_kinetic_energy_comprehensive_diagnostic",
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
        "learning_objective_id": "ns7_pk_50",
        "hints": {
            "tier_1": "Trace the energy from the very start to the very end.",
            "tier_2": "Remember that energy is never destroyed, only converted to heat and sound.",
            "tier_3": f"Sequence: {sequence}. Application: {law_application}.",
        },
        "misconception_tags": ["brakes_destroy_energy", "complex_systems_violate_conservation"],
    }
