"""
Grade 8 Natural Sciences - Term 2: Atoms (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/01. Atoms.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Historical Models & Atomic Postulates (01 - 06)
# ==============================================================================

def arch_01_democritus_atomos_concept(rng: random.Random) -> Dict[str, Any]:
    analogies = [
        ("a brick wall built of individual bricks", "matter is composed of discrete, tiny indivisible units rather than continuous substance"),
        ("a sand dune made of tiny individual grains of sand", "materials appear continuous from a distance but are made of distinct indivisible particles"),
        ("a mosaic artwork made of individual tiny ceramic tiles", "complex matter is assembled from basic, indivisible building blocks"),
    ]
    analogy, explanation = rng.choice(analogies)

    prompt = (
        f"Around 400 BC, the ancient Greek philosopher Democritus used the idea of {analogy} to propose a revolutionary theory about matter.\n\n"
        f"1. What Greek term did Democritus coin to describe these basic units, and what did this word literally mean?\n"
        f"2. Why did it take more than 2 000 years for the scientific community to accept Democritus's idea?"
    )
    sol = (
        f"**Step 1:** Democritus coined the term **atomos**, which literally means **'indivisible'** (or 'uncuttable / that which cannot be split') [1 Mark: Term & Meaning].\n\n"
        f"**Step 2:** Early philosophers and scientists could not observe atoms because they are far too small to be seen with the naked eye or early tools, and Democritus had no experimental evidence or scientific equipment to prove their existence [1 Mark: Reason for delay]."
    )
    return {
        "id": f"ns8_atom_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Atomos (meaning indivisible / uncuttable); lacked experimental evidence and atoms were too small to see",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "01_democritus_atomos_concept",
        "misconception_tags": ["democritus_atomos"],
        "hints": {
            "tier_1": "The word atom comes from the Greek word 'atomos'.",
            "tier_2": "Atomos means indivisible. It lacked experimental proof for 2 000 years.",
            "tier_3": "Atomos (indivisible); no experimental proof because atoms are unimaginably small."
        }
    }


def arch_02_daltons_atomic_postulates(rng: random.Random) -> Dict[str, Any]:
    postulates = [
        ("Postulate 1", "All matter consists of minute, indivisible particles called atoms.", "atoms cannot be subdivided, created, or destroyed in chemical reactions"),
        ("Postulate 2", "All atoms of a given chemical element are identical in mass and properties.", "atoms of the same element have the same number of protons and chemical characteristics"),
        ("Postulate 3", "Atoms of different elements have different masses and chemical properties.", "each element has its own distinct atomic mass and structure"),
    ]
    target_post, statement, modern_context = rng.choice(postulates)

    prompt = (
        f"In 1803, the English chemist John Dalton proposed the first scientific atomic theory based on experimental evidence.\n\n"
        f"1. State Dalton's postulate concerning: **{target_post}**.\n"
        f"2. In modern atomic theory, why do we now know that atoms CAN be broken down further?"
    )
    sol = (
        f"**Step 1:** Dalton stated: **{statement}** [1 Mark: Postulate].\n\n"
        f"**Step 2:** Modern science discovered that atoms are composed of smaller **subatomic particles** (protons, neutrons, and electrons) and can be split during nuclear reactions [1 Mark: Subatomic breakdown]."
    )
    return {
        "id": f"ns8_atom_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{statement}; modern atoms contain subatomic particles (protons, neutrons, electrons)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "02_daltons_atomic_postulates",
        "misconception_tags": ["dalton_atomic_theory"],
        "hints": {
            "tier_1": f"Recall Dalton's rules about elements and atoms for {target_post}.",
            "tier_2": "Dalton thought atoms were solid spheres that could not be split.",
            "tier_3": f"{statement}; atoms have subatomic particles."
        }
    }


def arch_03_scientific_models_evolution(rng: random.Random) -> Dict[str, Any]:
    models = [
        ("Dalton's billiard ball model (1803)", "Thomson's plum pudding model (1897)", "discovery of the negatively charged electron"),
        ("Thomson's plum pudding model (1897)", "Rutherford's nuclear model (1911)", "gold foil alpha particle scattering experiment discovering the dense nucleus"),
        ("Rutherford's nuclear model (1911)", "Bohr's planetary shell model (1913)", "discovery that electrons occupy fixed, quantized energy shells/orbits"),
    ]
    m1, m2, evidence = rng.choice(models)

    prompt = (
        f"The scientific model of the atom has undergone significant evolution:\n"
        f"**{m1}** $\\rightarrow$ **{m2}**.\n\n"
        f"1. What is a **scientific model** and why do scientists use models to represent atoms?\n"
        f"2. What new experimental evidence caused the transition from {m1.split(' ')[0]}'s model to {m2.split(' ')[0]}'s model?"
    )
    sol = (
        f"**Step 1:** A scientific model is a **mental or visual representation** used to explain phenomena or systems that cannot be seen directly (like unimaginably small atoms) [1 Mark: Scientific model definition].\n\n"
        f"**Step 2:** The model changed due to the **{evidence}** [1 Mark: Experimental evidence]."
    )
    return {
        "id": f"ns8_atom_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"A model visualises things too small to see directly; transition was driven by {evidence}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "03_scientific_models_evolution",
        "misconception_tags": ["nature_of_scientific_models"],
        "hints": {
            "tier_1": "Models help us picture things we cannot see directly.",
            "tier_2": f"New experimental data ({evidence}) forced scientists to revise the model.",
            "tier_3": f"Visual representation of unseen systems; {evidence}."
        }
    }


def arch_04_thomson_plum_pudding_model(rng: random.Random) -> Dict[str, Any]:
    food_analogies = [
        ("plum pudding", "raisins embedded in a sponge pudding cake"),
        ("chocolate chip muffin", "chocolate chips scattered inside the baked dough"),
        ("watermelon", "black seeds embedded inside the red sweet flesh"),
    ]
    food, desc = rng.choice(food_analogies)

    prompt = (
        f"In 1897, J.J. Thomson discovered the electron and proposed the '{food}' model of the atom ({desc}).\n\n"
        f"1. In Thomson's model, what represented the positively charged part of the atom?\n"
        f"2. What represented the negatively charged electrons?\n"
        f"3. Why was the overall atom considered electrically neutral in Thomson's model?"
    )
    sol = (
        f"**Step 1:** The positive charge was represented by a **diffuse, solid sphere of positive fluid/matter** (the pudding/dough/flesh) [1 Mark: Positive sphere].\n\n"
        f"**Step 2:** The electrons were represented by **tiny negative particles embedded/scattered throughout the sphere** (the raisins/chips/seeds) [1 Mark: Negative electrons].\n\n"
        f"**Step 3:** The total amount of negative charge embedded in the atom **exactly balanced** the total positive charge of the sphere, resulting in zero net charge [1 Mark: Electrical balance]."
    )
    return {
        "id": f"ns8_atom_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Positive fluid sphere with embedded negative electrons; total positive equals total negative charge",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_thomson_plum_pudding_model",
        "misconception_tags": ["thomson_atomic_model"],
        "hints": {
            "tier_1": "Think about the dough and the raisins.",
            "tier_2": "The dough is positive, raisins are negative electrons. They balance out.",
            "tier_3": "Positive sphere with embedded negative electrons; balanced charges make it neutral."
        }
    }


def arch_05_rutherford_gold_foil_scattering(rng: random.Random) -> Dict[str, Any]:
    observations = [
        (
            "Over 99% of the positively charged alpha particles passed straight through the gold foil with no deflection",
            "the atom consists mostly of empty space",
            "Volume"
        ),
        (
            "A small fraction of alpha particles were deflected through large angles, and a few bounced straight back",
            "the positive charge and most of the atom's mass are concentrated in a tiny, dense central nucleus",
            "Nucleus"
        ),
    ]
    obs, deduction, focus = rng.choice(observations)

    prompt = (
        f"In 1911, Ernest Rutherford and his team fired positively charged alpha particles at an ultra-thin gold foil.\n\n"
        f"Consider this key observation: *'{obs}'*.\n\n"
        f"1. What revolutionary scientific conclusion did Rutherford deduce from this specific observation?\n"
        f"2. Where does Rutherford's model place the negatively charged electrons?"
    )
    sol = (
        f"**Step 1:** Rutherford deduced that **{deduction}** [1 Mark: Scientific deduction].\n\n"
        f"**Step 2:** Electrons are placed **orbiting in the vast empty space around the central nucleus** [1 Mark: Electron placement]."
    )
    return {
        "id": f"ns8_atom_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deduction}; electrons orbit the tiny central nucleus in empty space",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "05_rutherford_gold_foil_scattering",
        "misconception_tags": ["rutherford_scattering_experiment"],
        "hints": {
            "tier_1": "If particles pass straight through, what does that say about space inside an atom?",
            "tier_2": "Most of the atom is empty space; the centre is a dense, positive nucleus.",
            "tier_3": f"{deduction}; electrons orbit outside the nucleus."
        }
    }


def arch_06_bohr_planetary_atomic_model(rng: random.Random) -> Dict[str, Any]:
    analogies = [
        ("planets orbiting the Sun in our Solar System", "electrons orbit the central nucleus in specific circular orbits or energy shells"),
        ("rungs on a ladder", "electrons can only occupy specific fixed energy levels, not the spaces between them"),
        ("steps in a staircase", "electrons jump between fixed energy levels by absorbing or emitting discrete packets of energy"),
    ]
    analogy, explanation = rng.choice(analogies)

    prompt = (
        f"In 1913, Danish physicist Niels Bohr refined Rutherford's nuclear model by comparing electron paths to {analogy}.\n\n"
        f"1. In the Bohr model, how are electrons arranged around the central nucleus?\n"
        f"2. What prevents negatively charged electrons from collapsing into the positively charged nucleus?"
    )
    sol = (
        f"**Step 1:** Electrons move around the nucleus in **fixed circular paths called electron shells (or discrete energy levels)** [1 Mark: Fixed shells].\n\n"
        f"**Step 2:** Electrons in a given shell possess a **fixed, quantized amount of kinetic energy**, preventing them from spiraling inward into the nucleus [1 Mark: Fixed energy levels]."
    )
    return {
        "id": f"ns8_atom_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Electrons orbit in fixed energy shells; electrons possess fixed energy preventing collapse into nucleus",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "06_bohr_planetary_atomic_model",
        "misconception_tags": ["bohr_atomic_model"],
        "hints": {
            "tier_1": "Bohr introduced fixed orbits or energy levels called shells.",
            "tier_2": "Electrons have fixed energy in each shell and cannot just fall into the center.",
            "tier_3": "Fixed energy shells; fixed energy prevents collapse."
        }
    }


# ==============================================================================
# CLUSTER 2: Subatomic Particles & Atomic Structure (07 - 15)
# ==============================================================================

def arch_07_subatomic_particles_charges(rng: random.Random) -> Dict[str, Any]:
    particles = [
        ("Proton", "+1 (positive)", "p^+"),
        ("Neutron", "0 (neutral / zero charge)", "n^0"),
        ("Electron", "-1 (negative)", "e^-"),
    ]
    p_name, p_charge, p_sym = rng.choice(particles)

    prompt = (
        f"An atom is composed of three fundamental subatomic particles: protons, neutrons, and electrons.\n\n"
        f"1. What is the electrical charge of a **{p_name}**?\n"
        f"2. State the electrical charges of the other two subatomic particles.\n"
        f"3. Which two particles are responsible for the overall zero electrical charge of an uncharged atom?"
    )
    sol = (
        f"**Step 1:** A {p_name} has a charge of **{p_charge}** [1 Mark: Target charge].\n\n"
        f"**Step 2:** The other particles are: Protons (+1), Neutrons (0), Electrons (-1) [1 Mark: Other charges].\n\n"
        f"**Step 3:** The **protons (+1)** and **electrons (-1)** cancel each other out because they have equal and opposite charges [1 Mark: Charge cancellation]."
    )
    return {
        "id": f"ns8_atom_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{p_name}: {p_charge}; Proton (+1), Neutron (0), Electron (-1); Protons and electrons balance each other",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_subatomic_particles_charges",
        "misconception_tags": ["subatomic_particle_charges"],
        "hints": {
            "tier_1": "Protons are positive, neutrons are neutral, electrons are negative.",
            "tier_2": "Positive protons cancel negative electrons.",
            "tier_3": f"{p_name} is {p_charge}; protons (+1) and electrons (-1) balance."
        }
    }


def arch_08_subatomic_particles_locations(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["nucleus", "electron_cloud", "both"])
    prompt = (
        f"An atom consists of two main anatomical regions: the central core and the surrounding space.\n\n"
        f"1. Name the dense central core of the atom and identify which two subatomic particles are located inside it.\n"
        f"2. Where are electrons located in relation to this central core, and how do they move?"
    )
    sol = (
        f"**Step 1:** The dense central core is the **nucleus**, which contains **protons** and **neutrons** (collectively called nucleons) [2 Marks: Nucleus and contents].\n\n"
        f"**Step 2:** Electrons are located outside the nucleus in **electron shells / energy levels**, moving rapidly around the nucleus in empty space [1 Mark: Electron location]."
    )
    return {
        "id": f"ns8_atom_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Nucleus contains protons and neutrons; electrons orbit outside in electron shells",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_subatomic_particles_locations",
        "misconception_tags": ["atomic_anatomy_locations"],
        "hints": {
            "tier_1": "The centre is called the nucleus. What is inside it?",
            "tier_2": "Protons and neutrons are in the nucleus; electrons are in shells outside.",
            "tier_3": "Nucleus contains protons and neutrons; electrons are in shells orbiting outside."
        }
    }


def arch_09_subatomic_particles_relative_masses(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The three subatomic particles differ drastically in mass.\n\n"
        f"1. Compare the relative masses of a **proton** and a **neutron** in atomic mass units (amu).\n"
        f"2. How does the mass of an **electron** compare to the mass of a proton (state its approximate fraction)?\n"
        f"3. In which region of the atom is practically all ($> 99,9\\%$) of the atom's mass concentrated?"
    )
    sol = (
        f"**Step 1:** A proton and a neutron have approximately the **same mass: 1 atomic mass unit (amu)** each [1 Mark: Proton vs Neutron mass].\n\n"
        f"**Step 2:** An electron is extremely tiny, with a mass of approximately **$\\frac{{1}}{{1836}}$ (or $\\frac{{1}}{{2000}}$)** of a proton's mass (negligible mass) [1 Mark: Electron mass fraction].\n\n"
        f"**Step 3:** Almost all of the atom's mass is concentrated in the **central nucleus** [1 Mark: Mass location]."
    )
    return {
        "id": f"ns8_atom_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Proton = 1 amu, Neutron = 1 amu; Electron = 1/1836 amu; Mass is concentrated in the nucleus",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_subatomic_particles_relative_masses",
        "misconception_tags": ["subatomic_relative_masses"],
        "hints": {
            "tier_1": "Protons and neutrons are heavy (1 amu); electrons are super light.",
            "tier_2": "An electron has about 1/1836 the mass of a proton.",
            "tier_3": "Proton = 1 amu, Neutron = 1 amu, Electron = 1/1836 amu; nucleus holds the mass."
        }
    }


def arch_10_atomic_number_protons_element_identity(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Carbon", 6, "every atom with 6 protons is carbon, regardless of neutrons or electrons"),
        ("Nitrogen", 7, "every atom with 7 protons is nitrogen"),
        ("Oxygen", 8, "every atom with 8 protons is oxygen"),
        ("Sodium", 11, "every atom with 11 protons is sodium"),
        ("Gold", 79, "every atom with 79 protons is gold"),
    ]
    name, z, reason = rng.choice(elements)

    prompt = (
        f"Consider the element **{name}**, which has an atomic number of **{z}**.\n\n"
        f"1. Define the **atomic number ($Z$)** of an atom.\n"
        f"2. How many protons are present in the nucleus of any {name} atom?\n"
        f"3. Can two different elements ever have the same atomic number? Explain why or why not."
    )
    sol = (
        f"**Step 1:** The atomic number is the **number of protons** found in the nucleus of an atom [1 Mark: Definition].\n\n"
        f"**Step 2:** A {name} atom has **{z} protons** [1 Mark: Proton count].\n\n"
        f"**Step 3:** **No**, two different elements can never have the same atomic number because the number of protons uniquely identifies the element [1 Mark: Element uniqueness]."
    )
    return {
        "id": f"ns8_atom_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Number of protons in nucleus; {z} protons; No, atomic number uniquely defines the element",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_atomic_number_protons_element_identity",
        "misconception_tags": ["atomic_number_proton_identity"],
        "hints": {
            "tier_1": "Atomic number = number of protons.",
            "tier_2": f"If atomic number is {z}, it has {z} protons.",
            "tier_3": "Atomic number = protons; each element has a unique number of protons."
        }
    }


def arch_11_atomic_mass_protons_plus_neutrons(rng: random.Random) -> Dict[str, Any]:
    atoms = [
        ("Lithium (Li)", 3, 7),
        ("Beryllium (Be)", 4, 9),
        ("Carbon (C)", 6, 12),
        ("Nitrogen (N)", 7, 14),
        ("Sodium (Na)", 11, 23),
        ("Aluminium (Al)", 13, 27),
        ("Phosphorus (P)", 15, 31),
    ]
    elem, z, a = rng.choice(atoms)
    neutrons = a - z

    prompt = (
        f"An atom of **{elem}** has an atomic number ($Z$) of **{z}** and an atomic mass number ($A$) of **{a}**.\n\n"
        f"1. What two subatomic particles are counted in the atomic mass number ($A$)?\n"
        f"2. Calculate the number of neutrons present in this {elem.split(' ')[0]} atom.\n"
        f"3. Why are electrons omitted when calculating the atomic mass number?"
    )
    sol = (
        f"**Step 1:** The atomic mass number counts the **protons and neutrons** in the nucleus [1 Mark: Particles in mass number].\n\n"
        f"**Step 2:** Number of neutrons = $\\text{{Atomic mass }} (A) - \\text{{Atomic number }} (Z) = {a} - {z} = \\mathbf{{{neutrons}}}$ neutrons [1 Mark: Neutron calculation].\n\n"
        f"**Step 3:** Electrons have **negligible mass** (approx. $\\frac{{1}}{{1836}}$ of a proton), so their mass is too small to affect the rounded mass number [1 Mark: Negligible electron mass]."
    )
    return {
        "id": f"ns8_atom_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Protons and neutrons; {neutrons} neutrons; Electrons have negligible mass",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_atomic_mass_protons_plus_neutrons",
        "misconception_tags": ["atomic_mass_and_neutrons"],
        "hints": {
            "tier_1": "Neutrons = Mass number - Atomic number.",
            "tier_2": f"Neutrons = {a} - {z} = {neutrons}.",
            "tier_3": f"Protons + neutrons; {neutrons} neutrons; electron mass is negligible."
        }
    }


def arch_12_electrical_neutrality_of_atoms(rng: random.Random) -> Dict[str, Any]:
    atoms = [
        ("Helium (He)", 2),
        ("Oxygen (O)", 8),
        ("Magnesium (Mg)", 12),
        ("Chlorine (Cl)", 17),
        ("Calcium (Ca)", 20),
    ]
    elem, z = rng.choice(atoms)

    prompt = (
        f"All neutral, unbonded atoms have an overall electrical charge of **zero**.\n\n"
        f"1. Consider a neutral atom of **{elem}** (atomic number {z}). How many electrons does it have?\n"
        f"2. Explain using charges why this {elem.split(' ')[0]} atom is electrically neutral.\n"
        f"3. What would happen to the atom's charge if it lost one electron?"
    )
    sol = (
        f"**Step 1:** In a neutral atom, electrons equal protons, so it has **{z} electrons** [1 Mark: Electron count].\n\n"
        f"**Step 2:** It contains {z} positive protons (+{z}) and {z} negative electrons (-{z}). The sum of charges is $(+{z}) + (-{z}) = 0$, making it neutral [1 Mark: Charge cancellation].\n\n"
        f"**Step 3:** If it loses one negative electron, it will have more protons than electrons, giving it a **positive charge (+1)** (forming a positive cation) [1 Mark: Ion formation]."
    )
    return {
        "id": f"ns8_atom_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{z} electrons; {z} positive protons balance {z} negative electrons; becomes positively charged (+1)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_electrical_neutrality_of_atoms",
        "misconception_tags": ["electrical_neutrality_atoms"],
        "hints": {
            "tier_1": "Neutral means positive protons equal negative electrons.",
            "tier_2": f"Protons = {z}, so electrons = {z}.",
            "tier_3": f"{z} electrons; charges cancel (+{z} - {z} = 0); losing an electron gives +1 charge."
        }
    }


def arch_13_deducing_p_n_e_counts_from_nuclide_symbol(rng: random.Random) -> Dict[str, Any]:
    nuclides = [
        ("^{12}_{6}\\text{C}", "Carbon", 6, 12),
        ("^{16}_{8}\\text{O}", "Oxygen", 8, 16),
        ("^{19}_{9}\\text{F}", "Fluorine", 9, 19),
        ("^{23}_{11}\\text{Na}", "Sodium", 11, 23),
        ("^{24}_{12}\\text{Mg}", "Magnesium", 12, 24),
        ("^{32}_{16}\\text{S}", "Sulfur", 16, 32),
        ("^{35}_{17}\\text{Cl}", "Chlorine", 17, 35),
        ("^{40}_{20}\\text{Ca}", "Calcium", 20, 40),
    ]
    sym_code, name, z, a = rng.choice(nuclides)
    neutrons = a - z

    prompt = (
        f"Examine the standard nuclide notation for a neutral atom of {name}: **${sym_code}$**.\n\n"
        f"1. How many **protons** does this atom contain?\n"
        f"2. How many **neutrons** does this atom contain?\n"
        f"3. How many **electrons** are orbiting the nucleus?"
    )
    sol = (
        f"**Step 1:** The subscript ($Z$) represents the atomic number: **{z} protons** [1 Mark: Protons].\n\n"
        f"**Step 2:** Neutrons = Superscript ($A$) - Subscript ($Z$) = ${a} - {z} = \\mathbf{{{neutrons}}}$ **neutrons** [1 Mark: Neutrons].\n\n"
        f"**Step 3:** For a neutral atom, electrons equal protons: **{z} electrons** [1 Mark: Electrons]."
    )
    return {
        "id": f"ns8_atom_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Protons: {z}, Neutrons: {neutrons}, Electrons: {z}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_deducing_p_n_e_counts_from_nuclide_symbol",
        "misconception_tags": ["nuclide_notation_subatomic_counts"],
        "hints": {
            "tier_1": "Bottom number is protons (and electrons). Top minus bottom is neutrons.",
            "tier_2": f"Protons = {z}, Neutrons = {a} - {z} = {neutrons}, Electrons = {z}.",
            "tier_3": f"Protons = {z}, Neutrons = {neutrons}, Electrons = {z}."
        }
    }


def arch_14_electron_energy_levels_capacity_2_8_8(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Lithium (Z = 3)", 3, [2, 1]),
        ("Carbon (Z = 6)", 6, [2, 4]),
        ("Neon (Z = 10)", 10, [2, 8]),
        ("Sodium (Z = 11)", 11, [2, 8, 1]),
        ("Silicon (Z = 14)", 14, [2, 8, 4]),
        ("Argon (Z = 18)", 18, [2, 8, 8]),
        ("Potassium (Z = 19)", 19, [2, 8, 8, 1]),
        ("Calcium (Z = 20)", 20, [2, 8, 8, 2]),
    ]
    elem, z, cfg = rng.choice(elements)
    cfg_str = ", ".join(map(str, cfg))

    prompt = (
        f"Electrons orbit the atomic nucleus in fixed energy shells following the **2, 8, 8 rule** for the first 20 elements.\n\n"
        f"1. What is the maximum electron capacity of Shell 1 (innermost) and Shell 2?\n"
        f"2. Write down the electron arrangement (configuration) for **{elem}**.\n"
        f"3. How many electrons are present in the outermost shell (valence shell) of this atom?"
    )
    sol = (
        f"**Step 1:** Shell 1 can hold a maximum of **2 electrons**; Shell 2 can hold a maximum of **8 electrons** [1 Mark: Shell capacities].\n\n"
        f"**Step 2:** The electron arrangement for {elem} is **{cfg_str}** [1 Mark: Arrangement].\n\n"
        f"**Step 3:** The outermost shell contains **{cfg[-1]} electron(s)** [1 Mark: Valence electrons]."
    )
    return {
        "id": f"ns8_atom_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Shell 1: max 2, Shell 2: max 8; Configuration: {cfg_str}; Valence electrons: {cfg[-1]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_electron_energy_levels_capacity_2_8_8",
        "misconception_tags": ["electron_shells_2_8_8_rule"],
        "hints": {
            "tier_1": "First shell holds up to 2, second holds up to 8.",
            "tier_2": f"Distribute {z} electrons into 2, 8, ...",
            "tier_3": f"Max 2 and 8; {cfg_str}; outer shell has {cfg[-1]}."
        }
    }


def arch_15_drawing_bohr_rutherford_diagram(rng: random.Random) -> Dict[str, Any]:
    atoms = [
        ("Helium", "He", 2, 4, [2], "#38bdf8"),
        ("Carbon", "C", 6, 12, [2, 4], "#34d399"),
        ("Oxygen", "O", 8, 16, [2, 6], "#f87171"),
        ("Neon", "Ne", 10, 20, [2, 8], "#fbbf24"),
    ]
    name, sym, z, a, shells, color = rng.choice(atoms)
    neutrons = a - z

    # Generate dynamic Bohr model SVG
    cx, cy = 180, 130
    svg_shells = ""
    r_list = [40, 75]
    for s_idx, count in enumerate(shells):
        r = r_list[s_idx]
        svg_shells += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        for e_i in range(count):
            angle = (360 / count) * e_i
            import math
            rad = math.radians(angle)
            ex = cx + r * math.cos(rad)
            ey = cy + r * math.sin(rad)
            svg_shells += f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4.5" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>'

    svg = (
        f'<svg viewBox="0 0 360 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="240" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="30" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Bohr-Rutherford Model: {name} ({sym})</text>'
        f'<circle cx="{cx}" cy="{cy}" r="26" fill="{color}" stroke="#334155" stroke-width="2"/>'
        f'<text x="{cx}" y="{cy - 5}" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{z}p</text>'
        f'<text x="{cx}" y="{cy + 10}" font-family="sans-serif" font-size="10" fill="#334155" text-anchor="middle">{neutrons}n</text>'
        f'{svg_shells}'
        f'<text x="180" y="240" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Shell 1: {shells[0]}e⁻{" | Shell 2: " + str(shells[1]) + "e⁻" if len(shells) > 1 else ""}</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the Bohr-Rutherford atomic model for **{name} ({sym})**.\n\n"
        f"1. How many protons and neutrons are shown inside the central nucleus?\n"
        f"2. How many electron shells does this atom possess, and how many total electrons are orbiting in these shells?\n"
        f"3. Explain why the inner shell only holds {shells[0]} electrons before electrons begin occupying the outer shell."
    )
    sol = (
        f"**Step 1:** The nucleus contains **{z} protons** and **{neutrons} neutrons** [1 Mark: Nucleus counts].\n\n"
        f"**Step 2:** It has **{len(shells)} electron shell(s)** with a total of **{z} electrons** [1 Mark: Shells and total electrons].\n\n"
        f"**Step 3:** The innermost shell (Shell 1) has a **maximum energy capacity of 2 electrons**; once filled, additional electrons must occupy the next higher energy level (Shell 2) [1 Mark: Shell capacity explanation]."
    )
    return {
        "id": f"ns8_atom_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{z} protons and {neutrons} neutrons; {len(shells)} shell(s) with {z} electrons; Shell 1 has maximum capacity of 2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_drawing_bohr_rutherford_diagram",
        "misconception_tags": ["bohr_rutherford_diagram_reading"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Look at the nucleus in the center for p and n counts.",
            "tier_2": f"Count the rings: {len(shells)} ring(s). Count the blue dots: {z} electrons.",
            "tier_3": f"{z} protons, {neutrons} neutrons; {len(shells)} shell(s); Shell 1 max capacity is 2."
        }
    }


# ==============================================================================
# CLUSTER 3: First 20 Elements & Periodic Table Grounding (16 - 25)
# ==============================================================================

def arch_16_first_twenty_elements_z1_to_z5(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (1, "Hydrogen", "H", "gas", "lightest element in the universe"),
        (2, "Helium", "He", "gas", "noble gas with 2 electrons filling its only shell"),
        (3, "Lithium", "Li", "solid", "lightest alkali metal, floats on oil"),
        (4, "Beryllium", "Be", "solid", "alkaline earth metal with 4 protons"),
        (5, "Boron", "B", "solid", "semi-metal with 5 protons"),
    ]
    z, name, sym, state, fact = rng.choice(elements)

    prompt = (
        f"Consider Element number **{z}** from the first 20 elements on the Periodic Table.\n\n"
        f"1. State the full chemical name and the standard chemical symbol for element {z}.\n"
        f"2. How many protons are in its nucleus, and what is its normal state of matter at room temperature ($25^\\circ\\text{{C}}$)?"
    )
    sol = (
        f"**Step 1:** Name: **{name}**; Symbol: **{sym}** [1 Mark: Name & Symbol].\n\n"
        f"**Step 2:** It has **{z} protons** and is a **{state}** at room temperature [1 Mark: Protons & State]."
    )
    return {
        "id": f"ns8_atom_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name} ({sym}); {z} protons; {state}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "16_first_twenty_elements_z1_to_z5",
        "misconception_tags": ["first_five_elements"],
        "hints": {
            "tier_1": f"Think of element {z} on the Periodic Table (H, He, Li, Be, B).",
            "tier_2": f"Z = {z} is {name} ({sym}).",
            "tier_3": f"{name} ({sym}); {z} protons; {state}."
        }
    }


def arch_17_first_twenty_elements_z6_to_z10(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (6, "Carbon", "C", "solid non-metal", "basis of all organic molecules and living tissue"),
        (7, "Nitrogen", "N", "gas", "makes up ~78% of Earth's atmosphere as N2"),
        (8, "Oxygen", "O", "gas", "essential for aerobic respiration and combustion as O2"),
        (9, "Fluorine", "F", "gas", "the most reactive halogen non-metal"),
        (10, "Neon", "Ne", "gas", "inert noble gas with a full valence octet of 8 electrons"),
    ]
    z, name, sym, desc, role = rng.choice(elements)

    prompt = (
        f"From the second period of the Periodic Table (atomic numbers 6 to 10):\n\n"
        f"1. Identify the element with atomic number **{z}** ({role}). State its name and symbol.\n"
        f"2. How many electrons are in a neutral atom of this element, and what is its classification ({desc.split(' ')[0]})?"
    )
    sol = (
        f"**Step 1:** Element {z} is **{name}** (chemical symbol: **{sym}**) [1 Mark: Name & Symbol].\n\n"
        f"**Step 2:** It has **{z} electrons** in a neutral atom and is classified as a **{desc}** [1 Mark: Electrons & Classification]."
    )
    return {
        "id": f"ns8_atom_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name} ({sym}); {z} electrons; {desc}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "17_first_twenty_elements_z6_to_z10",
        "misconception_tags": ["elements_6_to_10"],
        "hints": {
            "tier_1": "Elements 6 to 10: C, N, O, F, Ne.",
            "tier_2": f"Element {z} is {name} ({sym}).",
            "tier_3": f"{name} ({sym}); {z} electrons; {desc}."
        }
    }


def arch_18_first_twenty_elements_z11_to_z15(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (11, "Sodium", "Na", "alkali metal", "stored under oil, reacts violently with water"),
        (12, "Magnesium", "Mg", "alkaline earth metal", "burns with brilliant white light in air"),
        (13, "Aluminium", "Al", "metal", "lightweight, corrosion-resistant metal used in aircraft"),
        (14, "Silicon", "Si", "semi-metal (metalloid)", "semiconductor used in microchips"),
        (15, "Phosphorus", "P", "non-metal", "reactive non-metal used in matches and fertilizers"),
    ]
    z, name, sym, grp, use = rng.choice(elements)

    prompt = (
        f"Consider the elements from atomic numbers 11 to 15 (Period 3):\n\n"
        f"1. Name the element with atomic number **{z}** and give its chemical symbol.\n"
        f"2. Classify it as a metal, non-metal, or semi-metal ({grp}).\n"
        f"3. State one notable property or application ({use})."
    )
    sol = (
        f"**Step 1:** Name: **{name}**; Symbol: **{sym}** [1 Mark: Name & Symbol].\n\n"
        f"**Step 2:** It is classified as a **{grp}** [1 Mark: Classification].\n\n"
        f"**Step 3:** Property/Application: {use} [1 Mark: Fact]."
    )
    return {
        "id": f"ns8_atom_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name} ({sym}); {grp}; {use}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_first_twenty_elements_z11_to_z15",
        "misconception_tags": ["elements_11_to_15"],
        "hints": {
            "tier_1": "Elements 11 to 15: Na, Mg, Al, Si, P.",
            "tier_2": f"Atomic number {z} is {name} ({sym}).",
            "tier_3": f"{name} ({sym}); {grp}; {use}."
        }
    }


def arch_19_first_twenty_elements_z16_to_z20(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (16, "Sulfur", "S", "yellow solid non-metal", "used in sulfuric acid and vulcanising rubber"),
        (17, "Chlorine", "Cl", "yellow-green toxic gas", "halogen used to disinfect swimming pools"),
        (18, "Argon", "Ar", "inert noble gas", "used in incandescent light bulbs"),
        (19, "Potassium", "K", "soft alkali metal", "essential plant nutrient and highly reactive metal"),
        (20, "Calcium", "Ca", "alkaline earth metal", "essential for strong bones, teeth, and cement"),
    ]
    z, name, sym, desc, use = rng.choice(elements)

    prompt = (
        f"Focusing on elements with atomic numbers 16 to 20:\n\n"
        f"1. Identify the element with atomic number **{z}**: state its name and chemical symbol.\n"
        f"2. How many protons are inside its nucleus?\n"
        f"3. Briefly state its everyday significance ({use})."
    )
    sol = (
        f"**Step 1:** Name: **{name}**; Symbol: **{sym}** [1 Mark: Name & Symbol].\n\n"
        f"**Step 2:** It has **{z} protons** [1 Mark: Protons].\n\n"
        f"**Step 3:** Significance: {use} [1 Mark: Everyday use]."
    )
    return {
        "id": f"ns8_atom_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name} ({sym}); {z} protons; {use}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_first_twenty_elements_z16_to_z20",
        "misconception_tags": ["elements_16_to_20"],
        "hints": {
            "tier_1": "Elements 16 to 20: S, Cl, Ar, K, Ca.",
            "tier_2": f"Atomic number {z} is {name} ({sym}).",
            "tier_3": f"{name} ({sym}); {z} protons; {use}."
        }
    }


def arch_20_chemical_symbols_rules_and_origins(rng: random.Random) -> Dict[str, Any]:
    latin_pairs = [
        ("Sodium", "Na", "Natrium"),
        ("Potassium", "K", "Kalium"),
        ("Iron", "Fe", "Ferrum"),
        ("Copper", "Cu", "Cuprum"),
        ("Gold", "Au", "Aurum"),
        ("Lead", "Pb", "Plumbum"),
    ]
    name, sym, latin = rng.choice(latin_pairs)

    prompt = (
        f"Chemical symbols follow strict international IUPAC conventions.\n\n"
        f"1. State the capitalization rule for writing a two-letter chemical symbol.\n"
        f"2. Why is the symbol for **{name}** written as **{sym}** instead of starting with the letter '{name[0]}' (mention '{latin}')?\n"
        f"3. What is the danger if a student incorrectly writes 'CO' (carbon monoxide) instead of 'Co' (cobalt)?"
    )
    sol = (
        f"**Step 1:** The **first letter is always CAPITALIZED**, and the **second letter is always LOWERCASE** [1 Mark: Capitalization rule].\n\n"
        f"**Step 2:** The symbol {sym} derives from its **Latin root word '{latin}'** [1 Mark: Latin origin].\n\n"
        f"**Step 3:** 'CO' represents a compound of carbon and oxygen (toxic carbon monoxide gas), whereas 'Co' represents the single element cobalt metal; case errors completely change the chemical meaning [1 Mark: Chemical ambiguity]."
    )
    return {
        "id": f"ns8_atom_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"First letter capitalized, second lowercase; symbol {sym} comes from Latin '{latin}'; CO is carbon monoxide compound, Co is cobalt element",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_chemical_symbols_rules_and_origins",
        "misconception_tags": ["chemical_symbol_conventions"],
        "hints": {
            "tier_1": "First letter capital, second lowercase. Some symbols come from Latin.",
            "tier_2": f"{name} comes from Latin '{latin}'. CO is two elements, Co is one element.",
            "tier_3": f"First letter capital, second lowercase; Latin '{latin}'; CO vs Co distinction."
        }
    }


def arch_21_periodic_table_periods_and_groups_gr8(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["periods", "groups", "both"])
    prompt = (
        f"The Periodic Table is arranged systematically in horizontal rows and vertical columns.\n\n"
        f"1. What are the horizontal rows called, and what does the row number tell us about an atom's electron shells?\n"
        f"2. What are the vertical columns called, and why do elements in the same column exhibit similar chemical properties?"
    )
    sol = (
        f"**Step 1:** The horizontal rows are called **periods** [1 Mark]. The period number indicates the **number of electron shells (energy levels)** occupied by electrons [1 Mark: Shell count].\n\n"
        f"**Step 2:** The vertical columns are called **groups** [1 Mark]. Elements in the same group have the **same number of valence electrons** in their outermost shell, giving them similar chemical reactivity [1 Mark: Chemical behavior]."
    )
    return {
        "id": f"ns8_atom_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Horizontal rows = periods (number of electron shells); Vertical columns = groups (same number of valence electrons, similar chemical properties)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "21_periodic_table_periods_and_groups_gr8",
        "misconception_tags": ["periods_and_groups_periodic_table"],
        "hints": {
            "tier_1": "Rows are periods; columns are groups.",
            "tier_2": "Period number = number of shells. Group elements have the same valence electrons.",
            "tier_3": "Periods = rows (electron shells); Groups = columns (valence electrons, similar reactivity)."
        }
    }


def arch_22_periodic_table_metals_vs_non_metals_gr8(rng: random.Random) -> Dict[str, Any]:
    trios = [
        ("Magnesium (Mg)", "Metal", "Left side (Group 2)", "shiny, malleable electrical conductor"),
        ("Sulfur (S)", "Non-metal", "Upper right side (Group 16)", "dull, brittle electrical insulator"),
        ("Silicon (Si)", "Semi-metal", "Along the zigzag border line (Group 14)", "intermediate semiconductor"),
    ]
    elem, cat, loc, prop = rng.choice(trios)

    prompt = (
        f"The Periodic Table clearly divides elements into metals, non-metals, and semi-metals.\n\n"
        f"Consider **{elem}**:\n"
        f"1. In which region of the table is {elem.split(' ')[0]} located ({loc.split(' (')[0]})?\n"
        f"2. Classify {elem.split(' ')[0]} as a metal, non-metal, or semi-metal.\n"
        f"3. State one key physical property that reflects this classification ({prop})."
    )
    sol = (
        f"**Step 1:** Location: **{loc}** [1 Mark: Location].\n\n"
        f"**Step 2:** Classification: **{cat}** [1 Mark: Classification].\n\n"
        f"**Step 3:** Property: {prop} [1 Mark: Physical property]."
    )
    return {
        "id": f"ns8_atom_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{loc}; {cat}; {prop}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_periodic_table_metals_vs_non_metals_gr8",
        "misconception_tags": ["metals_nonmetals_semimetals_locations"],
        "hints": {
            "tier_1": "Left = metals, right = non-metals, zigzag = semi-metals.",
            "tier_2": f"{elem} is a {cat}.",
            "tier_3": f"{loc}; {cat}; {prop}."
        }
    }


def arch_23_atomic_size_trends_concept(rng: random.Random) -> Dict[str, Any]:
    groups = [
        ("Group 1 (Alkali metals)", "Lithium (Period 2) vs Sodium (Period 3) vs Potassium (Period 4)", "Potassium is largest because it has 4 electron shells compared to Lithium's 2 shells"),
        ("Group 18 (Noble gases)", "Helium (Period 1) vs Neon (Period 2) vs Argon (Period 3)", "Argon is largest because it has 3 electron shells compared to Helium's 1 shell"),
        ("Group 17 (Halogens)", "Fluorine (Period 2) vs Chlorine (Period 3) vs Bromine (Period 4)", "Bromine is largest because more filled electron energy levels are added"),
    ]
    grp, comparison, explanation = rng.choice(groups)

    prompt = (
        f"Atomic size (atomic radius) changes predictably across the Periodic Table.\n\n"
        f"Consider the downward sequence in **{grp}**: **{comparison}**.\n\n"
        f"1. How does the size of an atom change as you move **down** any group from top to bottom?\n"
        f"2. Explain this trend in terms of atomic structure (electron shells)."
    )
    sol = (
        f"**Step 1:** Atomic size **increases** as you move down a group [1 Mark: Trend].\n\n"
        f"**Step 2:** Each period down adds an **additional electron shell (energy level)**, placing outer electrons further from the nucleus and increasing the atom's volume [1 Mark: Shell addition]."
    )
    return {
        "id": f"ns8_atom_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Atomic size increases down a group; each step down adds an extra electron shell",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "23_atomic_size_trends_concept",
        "misconception_tags": ["atomic_size_group_trend"],
        "hints": {
            "tier_1": "Do atoms get bigger or smaller as you go down?",
            "tier_2": "Each row adds a new ring of electrons, making the atom bigger.",
            "tier_3": "Increases down a group; adding extra electron shells makes atoms larger."
        }
    }


def arch_24_isotopes_concept_introductory(rng: random.Random) -> Dict[str, Any]:
    isotope_examples = [
        ("Carbon-12 and Carbon-14", 6, 12, 14, "dating ancient fossils and archaeological artifacts"),
        ("Chlorine-35 and Chlorine-37", 17, 35, 37, "explaining why chlorine's relative atomic mass on the periodic table is approximately 35,5"),
        ("Hydrogen-1 (protium) and Hydrogen-2 (deuterium)", 1, 1, 2, "forming heavy water used in nuclear reactor cooling systems"),
    ]
    pair, z, a1, a2, application = rng.choice(isotope_examples)
    n1 = a1 - z
    n2 = a2 - z

    prompt = (
        f"Not all atoms of a particular element have the identical mass. Consider **{pair}**.\n\n"
        f"1. Define the term **isotope** in chemistry.\n"
        f"2. Compare the number of protons and neutrons in these two isotopes (atomic number Z = {z}).\n"
        f"3. Explain why both isotopes behave identically in chemical reactions."
    )
    sol = (
        f"**Step 1:** Isotopes are atoms of the **same element** that have the **same atomic number (same protons)** but **different atomic mass numbers (different neutrons)** [1 Mark: Definition].\n\n"
        f"**Step 2:** Both isotopes have **{z} protons**; the first has **{n1} neutrons** (${a1} - {z}$) and the second has **{n2} neutrons** (${a2} - {z}$) [1 Mark: Particle comparison].\n\n"
        f"**Step 3:** Chemical reactions are determined by the **number and arrangement of electrons**, which are identical in both neutral isotopes [1 Mark: Chemical identity]."
    )
    return {
        "id": f"ns8_atom_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Same protons, different neutrons; Both have {z} protons, but {n1} vs {n2} neutrons; Identical electron arrangements dictate chemical behavior",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_isotopes_concept_introductory",
        "misconception_tags": ["isotopes_definition_properties"],
        "hints": {
            "tier_1": "Isotopes are identical twins with slightly different weights (neutrons).",
            "tier_2": f"Same protons ({z}), different neutrons ({n1} vs {n2}). Same electrons = same chemistry.",
            "tier_3": "Same protons, different neutrons; identical electrons mean identical chemical reactions."
        }
    }


def arch_25_evaluating_atomic_data_cards_gr8(rng: random.Random) -> Dict[str, Any]:
    cards = [
        ("Nitrogen", "N", 7, 14.007, "#3b82f6", "Gas", [2, 5]),
        ("Magnesium", "Mg", 12, 24.305, "#10b981", "Metal", [2, 8, 2]),
        ("Phosphorus", "P", 15, 30.974, "#f59e0b", "Non-metal", [2, 8, 5]),
        ("Calcium", "Ca", 20, 40.078, "#8b5cf6", "Metal", [2, 8, 8, 2]),
        ("Boron", "B", 5, 10.81, "#ec4899", "Semi-metal", [2, 3]),
    ]
    name, sym, z, mass, color, category, cfg = rng.choice(cards)
    rounded_mass = round(mass)
    neutrons = rounded_mass - z

    svg = (
        f'<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border-radius:10px;border:2px solid {color};">'
        f'<rect x="10" y="10" width="300" height="200" rx="8" fill="#f8fafc" stroke="{color}" stroke-width="1.5"/>'
        f'<rect x="25" y="25" width="270" height="35" rx="4" fill="{color}"/>'
        f'<text x="160" y="48" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Periodic Table Data Tile</text>'
        f'<text x="45" y="90" font-family="sans-serif" font-size="16" font-weight="bold" fill="#334155">{z}</text>'
        f'<text x="160" y="125" font-family="sans-serif" font-size="38" font-weight="bold" fill="{color}" text-anchor="middle">{sym}</text>'
        f'<text x="160" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{name}</text>'
        f'<text x="160" y="180" font-family="sans-serif" font-size="12" fill="#64748b" text-anchor="middle">Atomic Mass: {mass}</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the chemical data tile for **{name}**.\n\n"
        f"1. State the atomic number ($Z$) and chemical symbol of this element.\n"
        f"2. Calculate the number of neutrons in a typical atom of {name} (round atomic mass to {rounded_mass}).\n"
        f"3. State how many electrons orbit in a neutral atom of {name}, and write its electron arrangement (configuration)."
    )
    sol = (
        f"**Step 1:** Atomic number ($Z$) = **{z}**; Chemical symbol = **{sym}** [1 Mark: Z and Symbol].\n\n"
        f"**Step 2:** Neutrons = Rounded mass - Atomic number = ${rounded_mass} - {z} = \\mathbf{{{neutrons}}}$ **neutrons** [1 Mark: Neutrons].\n\n"
        f"**Step 3:** A neutral atom has **{z} electrons** arranged as **{', '.join(map(str, cfg))}** [1 Mark: Electrons and configuration]."
    )
    return {
        "id": f"ns8_atom_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Z = {z}, Symbol = {sym}; {neutrons} neutrons; {z} electrons with arrangement {', '.join(map(str, cfg))}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_evaluating_atomic_data_cards_gr8",
        "misconception_tags": ["periodic_table_tile_interpretation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": f"Z is the top number ({z}). Rounded mass is {rounded_mass}.",
            "tier_2": f"Neutrons = {rounded_mass} - {z} = {neutrons}. Electrons = {z}.",
            "tier_3": f"Z = {z}, Symbol = {sym}; {neutrons} neutrons; {z} electrons ({', '.join(map(str, cfg))})."
        }
    }
