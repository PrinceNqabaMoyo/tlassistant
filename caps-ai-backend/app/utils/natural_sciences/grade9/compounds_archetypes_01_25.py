"""Grade 9 Natural Sciences - Compounds: Archetypes 01 to 25.
Grounded strictly in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Compounds.md.

Covers:
- Elements, compounds, mixtures, and chemical bonding principles
- Diatomic molecules (H2, N2, O2, F2, Cl2, Br2, I2)
- Molecular clusters vs crystal lattice networks (e.g. NaCl, MgO)
- Law of constant composition & fixed combining ratios
- Periodic Table organization: Groups (1 to 18), Periods (1 to 7)
- Metals, non-metals, and semi-metals (metalloids)
- Physical & chemical properties of Group 1 (Alkali metals) & storage in oil
- Atomic notation, atomic number Z, mass number A, subatomic particles, valence electrons
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Elements, Molecules & Pure Substances vs Mixtures (01 - 09)
# ==============================================================================

def arch_01_compound_definition_and_chemical_bonding(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("water", "H2O", "two hydrogen atoms chemically bonded to one oxygen atom", "hydrogen and oxygen"),
        ("table salt (sodium chloride)", "NaCl", "sodium and chlorine ions bonded in a repeating crystal lattice in a 1:1 ratio", "sodium and chlorine"),
        ("carbon dioxide", "CO2", "one carbon atom chemically bonded to two oxygen atoms", "carbon and oxygen"),
        ("methane", "CH4", "one carbon atom chemically bonded to four hydrogen atoms", "carbon and hydrogen"),
    ]
    name, formula, desc, elements = rng.choice(examples)

    prompt = (
        f"In chemistry, matter can exist as elements, compounds, or mixtures.\n\n"
        f"1. Define what a **chemical compound** is in terms of elements and chemical bonds.\n"
        f"2. Using {name} (${formula}$) as an example, explain why it is classified as a compound rather than a mixture of {elements}.\n"
        f"3. Can the constituent elements in {name} be separated using simple physical methods like filtration or boiling? Explain."
    )
    sol = (
        f"**Step 1:** A **compound** is a pure substance formed when two or more different chemical elements are chemically bonded together in a fixed ratio [1 Mark: Definition].\n\n"
        f"**Step 2:** {name.capitalize()} (${formula}$) is a compound because {desc}; the atoms are chemically joined by strong chemical bonds and lose their individual elemental properties [1 Mark: Chemical bonding & fixed ratio].\n\n"
        f"**Step 3:** **No**; chemical bonds cannot be broken by physical separation techniques (like filtration or distillation). They can only be separated into elements through chemical reactions or electrolysis [1 Mark: Physical separation impossible]."
    )
    return {
        "id": f"ns9_comp_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Compound = 2+ different elements chemically bonded in fixed ratio; {name} has chemically bonded atoms ({desc}); Cannot be separated physically, only chemically",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "01_compound_definition_and_chemical_bonding",
        "misconception_tags": ["compound_definition_vs_mixture"],
        "hints": {
            "tier_1": "A compound must have different elements bonded in a fixed ratio.",
            "tier_2": "Chemical bonds require chemical methods to break, not physical ones.",
            "tier_3": f"Compound definition; chemically bonded {desc}; physical separation not possible."
        }
    }


def arch_02_element_vs_compound_fundamental_distinction(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Oxygen gas ($O_2$)", "element", "made up of only one kind of atom (oxygen)", "Water ($H_2O$)", "compound", "made up of two different elements (hydrogen and oxygen) chemically bonded"),
        ("Iron filings ($Fe$)", "element", "consists of only iron atoms", "Iron(II) sulfide ($FeS$)", "compound", "formed when iron and sulfur chemically bond together in a 1:1 ratio"),
        ("Carbon graphite ($C$)", "element", "composed entirely of carbon atoms", "Carbon dioxide ($CO_2$)", "compound", "composed of carbon and oxygen atoms chemically bonded"),
    ]
    e_name, e_type, e_reason, c_name, c_type, c_reason = rng.choice(pairs)

    prompt = (
        f"Consider the two pure chemical substances: **{e_name}** and **{c_name}**.\n\n"
        f"1. Classify each substance as either an **element** or a **compound**.\n"
        f"2. Provide the scientific microscopic reason for your classification of {e_name}.\n"
        f"3. Provide the scientific microscopic reason for your classification of {c_name}."
    )
    sol = (
        f"**Step 1:** {e_name} is an **{e_type}**; {c_name} is a **{c_type}** [1 Mark: Classifications].\n\n"
        f"**Step 2:** {e_name} is an {e_type} because it is **{e_reason}** (atoms all have the same atomic number) [1 Mark: Element microscopic reason].\n\n"
        f"**Step 3:** {c_name} is a {c_type} because it is **{c_reason}** [1 Mark: Compound microscopic reason]."
    )
    return {
        "id": f"ns9_comp_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{e_name} is an {e_type} ({e_reason}); {c_name} is a {c_type} ({c_reason})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_element_vs_compound_fundamental_distinction",
        "misconception_tags": ["element_vs_compound_distinction"],
        "hints": {
            "tier_1": "Elements have only one type of atom. Compounds have two or more different types bonded.",
            "tier_2": f"{e_name} has one atom type; {c_name} has different atoms bonded.",
            "tier_3": f"{e_type} ({e_reason}); {c_type} ({c_reason})."
        }
    }


def arch_03_pure_substance_vs_mixture_particulate_model(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A sealed container containing helium gas ($He$)", "Pure substance (element)", "consists of only one type of atom with a constant, uniform composition throughout"),
        ("A beaker containing pure distilled water ($H_2O$)", "Pure substance (compound)", "consists of only one type of particle (water molecules) in a fixed 2:1 ratio"),
        ("A glass of seawater containing dissolved sodium chloride, water, and minerals", "Mixture", "contains different independent substances physically mingled without chemical bonding in variable proportions"),
        ("Clean dry atmospheric air (nitrogen, oxygen, argon, and carbon dioxide)", "Mixture", "contains different gases physically blended together in variable ratios without chemical bonds between them"),
    ]
    subst, classification, microscopic_reason = rng.choice(scenarios)

    prompt = (
        f"In chemistry, matter is categorized into **pure substances** (elements and compounds) and **mixtures**.\n\n"
        f"Consider: **{subst}**.\n\n"
        f"1. Classify this sample as either a **pure substance** or a **mixture**.\n"
        f"2. Explain your choice at the microscopic/particle level.\n"
        f"3. Does this sample possess fixed physical properties (such as a sharp, constant boiling point)? Explain."
    )
    is_pure = "Pure" in classification
    props = "Yes; pure substances have fixed, constant boiling and melting points" if is_pure else "No; mixtures boil and melt over a range of temperatures depending on their composition"

    sol = (
        f"**Step 1:** Classification: **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Particle reason: It {microscopic_reason} [1 Mark: Microscopic explanation].\n\n"
        f"**Step 3:** Physical properties: **{props}** [1 Mark: Physical properties]."
    )
    return {
        "id": f"ns9_comp_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{classification}; {microscopic_reason}; {props}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_pure_substance_vs_mixture_particulate_model",
        "misconception_tags": ["pure_substance_vs_mixture"],
        "hints": {
            "tier_1": "Pure substances have identical particles throughout. Mixtures contain different particles unbonded.",
            "tier_2": f"{subst} is a {classification.split(' ')[0]}.",
            "tier_3": f"{classification}; {microscopic_reason}; {props}."
        }
    }


def arch_04_diatomic_elements_seven_homonuclear_molecules(rng: random.Random) -> Dict[str, Any]:
    diatomics = [
        ("Hydrogen", "H2", "gas", "Group 1"),
        ("Nitrogen", "N2", "gas", "Group 15"),
        ("Oxygen", "O2", "gas", "Group 16"),
        ("Fluorine", "F2", "gas", "Group 17"),
        ("Chlorine", "Cl2", "gas", "Group 17"),
        ("Bromine", "Br2", "liquid", "Group 17"),
        ("Iodine", "I2", "solid", "Group 17"),
    ]
    elem, form, state, grp = rng.choice(diatomics)

    prompt = (
        f"Certain non-metal elements exist naturally as **diatomic molecules** at standard temperature and pressure.\n\n"
        f"1. What is the meaning of the scientific term **diatomic**?\n"
        f"2. Write the correct chemical formula for pure **{elem.lower()}** in its natural state.\n"
        f"3. Explain why {elem} is classified as an **element** and NOT as a compound, even though it exists as molecules."
    )
    sol = (
        f"**Step 1:** **Diatomic** means consisting of **two atoms** chemically bonded together ($di = 2$, $atomic = atoms$) [1 Mark: Definition].\n\n"
        f"**Step 2:** Chemical formula: **${form}$** [1 Mark: Formula].\n\n"
        f"**Step 3:** {elem} (${form}$) is an element because the two bonded atoms are of the **exact same kind/element** (identical atomic number); a compound requires two or more *different* elements chemically bonded [1 Mark: Element justification]."
    )
    return {
        "id": f"ns9_comp_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Diatomic = two atoms bonded together; {form}; Element because both bonded atoms are identical (same element)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_diatomic_elements_seven_homonuclear_molecules",
        "misconception_tags": ["diatomic_element_not_compound"],
        "hints": {
            "tier_1": "Di means two. H2, N2, O2, F2, Cl2, Br2, I2 are diatomic elements.",
            "tier_2": f"Formula for {elem} is {form}.",
            "tier_3": f"Two atoms bonded; {form}; identical atoms means it is still an element."
        }
    }


def arch_05_molecular_compounds_discrete_particle_clusters(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("water", "H2O", "two hydrogen atoms and one oxygen atom", 3, "covalent molecular"),
        ("ammonia", "NH3", "one nitrogen atom and three hydrogen atoms", 4, "covalent molecular"),
        ("methane", "CH4", "one carbon atom and four hydrogen atoms", 5, "covalent molecular"),
        ("carbon dioxide", "CO2", "one carbon atom and two oxygen atoms", 3, "covalent molecular"),
    ]
    name, formula, composition, n_atoms, struct_type = rng.choice(compounds)

    prompt = (
        f"The chemical compound **{name}** has the chemical formula **${formula}$**.\n\n"
        f"1. Describe the microscopic composition of a single molecule of {name}.\n"
        f"2. How many total atoms make up one discrete molecule of {name}?\n"
        f"3. Does {name} exist as individual discrete molecules or as an infinite ionic crystal lattice at room temperature?"
    )
    sol = (
        f"**Step 1:** A single molecule of {name} consists of **{composition}** held together by chemical bonds [1 Mark: Composition].\n\n"
        f"**Step 2:** Total atoms per molecule: **{n_atoms} atoms** [1 Mark: Atom count].\n\n"
        f"**Step 3:** It exists as **individual discrete molecules** (covalent molecular structure) [1 Mark: Discrete molecules]."
    )
    return {
        "id": f"ns9_comp_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{composition}; {n_atoms} total atoms; Discrete molecules",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_molecular_compounds_discrete_particle_clusters",
        "misconception_tags": ["discrete_molecules_structure"],
        "hints": {
            "tier_1": "Count each atom in the formula subscripts.",
            "tier_2": f"{name} is made of separate small molecules.",
            "tier_3": f"{composition}; {n_atoms} atoms; individual discrete molecules."
        }
    }


def arch_06_crystal_lattice_structures_ionic_repeating_networks(rng: random.Random) -> Dict[str, Any]:
    lattices = [
        ("Sodium chloride (table salt)", "NaCl", "sodium ions ($Na^+$) and chloride ions ($Cl^-$)", "1 : 1", "face-centered cubic crystalline lattice"),
        ("Magnesium oxide", "MgO", "magnesium ions ($Mg^{2+}$) and oxide ions ($O^{2-}$)", "1 : 1", "cubic ionic crystal lattice"),
        ("Calcium chloride", "CaCl2", "calcium ions ($Ca^{2+}$) and chloride ions ($Cl^-$)", "1 : 2", "crystalline ionic network"),
    ]
    name, formula, ions, ratio, shape = rng.choice(lattices)

    prompt = (
        f"Solid **{name}** (${formula}$) forms a solid crystalline material.\n\n"
        f"1. Explain what a **crystal lattice** is in solid-state chemistry.\n"
        f"2. Does {name} consist of small separate independent molecules? Explain your answer.\n"
        f"3. What does the chemical formula **${formula}$** represent in this crystal lattice structure?"
    )
    sol = (
        f"**Step 1:** A **crystal lattice** is a regular, repeating three-dimensional symmetrical arrangement of atoms or ions throughout a crystalline solid [1 Mark: Crystal lattice definition].\n\n"
        f"**Step 2:** **No**; it does not consist of small independent molecules, but rather an extended giant three-dimensional network of millions of {ions} held by strong electrostatic bonds [1 Mark: Giant network not molecules].\n\n"
        f"**Step 3:** The formula represents the simplest **formula unit** showing the simplest fixed ratio of ions ({ratio}) in the lattice [1 Mark: Formula unit ratio]."
    )
    return {
        "id": f"ns9_comp_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Crystal lattice = regular repeating 3D arrangement of ions; No, it is a giant network (not separate molecules); Formula represents the simplest formula unit ratio ({ratio})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "06_crystal_lattice_structures_ionic_repeating_networks",
        "misconception_tags": ["ionic_lattice_vs_molecules"],
        "hints": {
            "tier_1": "Salts do not have separate molecules; they form giant 3D lattices.",
            "tier_2": "NaCl is a formula unit representing a 1:1 ratio.",
            "tier_3": "Regular 3D repeating structure; giant network not separate molecules; simplest ratio/formula unit."
        }
    }


def arch_07_fixed_ratio_of_atoms_law_of_constant_composition(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("water", "H2O", "hydrogen", 2, "oxygen", 1, "2 : 1", "If the ratio changes to 2:2, a completely different compound forms: hydrogen peroxide ($H_2O_2$)"),
        ("carbon dioxide", "CO2", "carbon", 1, "oxygen", 2, "1 : 2", "If the ratio changes to 1:1, a completely different toxic compound forms: carbon monoxide ($CO$)"),
        ("methane", "CH4", "carbon", 1, "hydrogen", 4, "1 : 4", "If the ratio changes to 2:6, a completely different hydrocarbon forms: ethane ($C_2H_6$)"),
    ]
    c_name, form, el1, n1, el2, n2, ratio, alter = rng.choice(cases)

    prompt = (
        f"A fundamental law of chemistry states that elements in a given chemical compound always combine in a **fixed, definite ratio**.\n\n"
        f"Consider the compound **{c_name}** (${form}$).\n\n"
        f"1. State the precise atomic ratio of {el1} atoms to {el2} atoms in every sample of pure {c_name}.\n"
        f"2. Can a chemist create a sample of {c_name} with an atomic ratio of {el1} to {el2} other than {ratio}? Explain.\n"
        f"3. What happens if the atomic combining ratio is altered ({alter})?"
    )
    sol = (
        f"**Step 1:** The atomic ratio of {el1} to {el2} is **{ratio}** ($n({el1}) : n({el2}) = {n1} : {n2}$) [1 Mark: Fixed ratio].\n\n"
        f"**Step 2:** **No**; according to the Law of Constant Composition, a specific compound always has the exact same ratio of elements anywhere in the universe [1 Mark: Law of Constant Composition].\n\n"
        f"**Step 3:** If the ratio changes, **a completely different substance with different chemical properties is produced** [1 Mark: Different compound formed]."
    )
    return {
        "id": f"ns9_comp_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Ratio is {ratio}; No, because compounds have fixed constant composition; Changing the ratio creates a completely different compound",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_fixed_ratio_of_atoms_law_of_constant_composition",
        "misconception_tags": ["fixed_ratio_constant_composition"],
        "hints": {
            "tier_1": f"Look at the subscripts in {form}: {ratio}.",
            "tier_2": "Compounds cannot have variable ratios; that would be a mixture or a different chemical.",
            "tier_3": f"{ratio}; No (fixed composition); creates a different compound."
        }
    }


def arch_08_physical_mixture_vs_chemical_compound_separation(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Iron filings and sulfur powder mixed together in a petri dish at room temperature",
            "A magnet can easily pull out the black iron filings, leaving the yellow sulfur powder behind",
            "Physical mixture",
            "Physical method (magnetism) works because the iron and sulfur atoms are NOT chemically bonded together"
        ),
        (
            "Iron(II) sulfide ($FeS$) formed after heating iron filings and sulfur powder until they glow",
            "A magnet brought near the black crushed product fails to attract the iron",
            "Chemical compound",
            "Physical method fails because iron and sulfur atoms are chemically bonded; it requires a chemical reaction to separate them"
        ),
        (
            "Sodium chloride dissolved in water",
            "Heating the solution allows water to evaporate, leaving solid sodium chloride salt crystals behind",
            "Physical mixture (solution)",
            "The salt and water are physically mingled; water can be removed by physical phase change (evaporation)"
        ),
    ]
    mixture_desc, test_obs, classification, explanation = rng.choice(scenarios)

    prompt = (
        f"A science class investigates the behavior of materials during laboratory experiments:\n"
        f"- **Sample:** {mixture_desc}.\n"
        f"- **Test Observation:** {test_obs}.\n\n"
        f"1. Classify the sample under test as a **physical mixture** or a **chemical compound**.\n"
        f"2. Explain why the separation test succeeded or failed based on chemical bonding.\n"
        f"3. In general, what type of process (physical or chemical) is required to break down a chemical compound into its elements?"
    )
    sol = (
        f"**Step 1:** Classification: **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Explanation: {explanation} [1 Mark: Bonding explanation].\n\n"
        f"**Step 3:** A **chemical process** (such as thermal decomposition or electrolysis) is required to break chemical bonds [1 Mark: Chemical process required]."
    )
    return {
        "id": f"ns9_comp_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{classification}; {explanation}; Chemical process (e.g. electrolysis/heating)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_physical_mixture_vs_chemical_compound_separation",
        "misconception_tags": ["mixture_separation_vs_compound_decomposition"],
        "hints": {
            "tier_1": "Magnets only separate iron if it is not chemically bonded in a compound.",
            "tier_2": f"This sample is a {classification}.",
            "tier_3": f"{classification}; {explanation}; Chemical process."
        }
    }


def arch_09_particle_diagram_classifying_element_compound_mixture(rng: random.Random) -> Dict[str, Any]:
    box_id = rng.choice(["A", "B", "C"])
    c_blue = rng.choice(["#2563eb", "#1d4ed8", "#3b82f6"])
    c_red = rng.choice(["#ef4444", "#dc2626", "#e11d48"])
    c_gold = rng.choice(["#f59e0b", "#d97706", "#b45309"])
    uid = f"FIG-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 380 150" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="360" height="130" rx="6" fill="#f8fafc"/>'
        f'<text x="190" y="24" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Particle Models of Matter</text>'
        f'<text x="360" y="24" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Box A: Diatomic Element
        f'<rect x="20" y="36" width="100" height="85" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="70" y="50" font-family="sans-serif" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">Box A</text>'
        f'<circle cx="50" cy="70" r="9" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="65" cy="70" r="9" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="75" cy="100" r="9" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="90" cy="100" r="9" fill="{c_blue}" stroke="#0f172a"/>'
        # Box B: Pure Compound
        f'<rect x="140" y="36" width="100" height="85" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="190" y="50" font-family="sans-serif" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">Box B</text>'
        f'<circle cx="180" cy="75" r="10" fill="{c_red}" stroke="#0f172a"/>'
        f'<circle cx="168" cy="85" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="192" cy="85" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="210" cy="100" r="10" fill="{c_red}" stroke="#0f172a"/>'
        f'<circle cx="198" cy="110" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="222" cy="110" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        # Box C: Mixture of Element and Compound
        f'<rect x="260" y="36" width="100" height="85" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="310" y="50" font-family="sans-serif" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">Box C</text>'
        f'<circle cx="280" cy="75" r="8" fill="{c_gold}" stroke="#0f172a"/>'
        f'<circle cx="330" cy="75" r="10" fill="{c_red}" stroke="#0f172a"/>'
        f'<circle cx="318" cy="85" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="342" cy="85" r="6" fill="{c_blue}" stroke="#0f172a"/>'
        f'<circle cx="295" cy="105" r="8" fill="{c_gold}" stroke="#0f172a"/>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle models depicted in Box A, Box B, and Box C.\n\n"
        f"1. Classify the substance shown in **Box A** and explain your reasoning.\n"
        f"2. Classify the substance shown in **Box B** and explain your reasoning.\n"
        f"3. Classify the substance shown in **Box C** and explain your reasoning."
    )
    sol = (
        f"**Step 1:** **Box A is an element (diatomic element)**; it consists of identical diatomic molecules composed of the same type of atom (blue circles only) [1 Mark: Box A].\n\n"
        f"**Step 2:** **Box B is a pure compound**; all particles in the box are identical molecules consisting of two different kinds of atoms chemically bonded in a fixed 2:1 ratio (red and blue circles) [1 Mark: Box B].\n\n"
        f"**Step 3:** **Box C is a mixture of an element and a compound**; it contains separate, independent single atoms (gold) mingled alongside compound molecules (red and blue) without chemical bonds between them [1 Mark: Box C]."
    )
    return {
        "id": f"ns9_comp_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Box A = Diatomic element (identical atoms); Box B = Pure compound (identical molecules of 2 different bonded atoms); Box C = Mixture of element and compound",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_particle_diagram_classifying_element_compound_mixture",
        "misconception_tags": ["particle_diagram_classification"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Box A has only one atom color. Box B has identical bonded clusters. Box C has different unbonded particles.",
            "tier_2": "A = diatomic element; B = compound; C = mixture.",
            "tier_3": "A = Diatomic element; B = Pure compound; C = Mixture of element and compound."
        }
    }


# ==============================================================================
# CLUSTER 2: Periodic Table Structure & Trends (10 - 18)
# ==============================================================================

def arch_10_periodic_table_groups_and_periods_definitions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Periodic Table of Elements organizes all known chemical elements systematically.\n\n"
        f"1. What are the vertical columns of the Periodic Table called, and how many are there?\n"
        f"2. What are the horizontal rows of the Periodic Table called, and how many are there?\n"
        f"3. In general, what do elements belonging to the same vertical column share in common?"
    )
    sol = (
        f"**Step 1:** The vertical columns are called **Groups**; there are **18 groups** in total [1 Mark: Groups].\n\n"
        f"**Step 2:** The horizontal rows are called **Periods**; there are **7 periods** in total [1 Mark: Periods].\n\n"
        f"**Step 3:** Elements in the same group have the **same number of valence electrons** in their outermost energy level, giving them **similar chemical properties and reactivity** [1 Mark: Chemical similarity]."
    )
    return {
        "id": f"ns9_comp_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Vertical columns = Groups (18 groups); Horizontal rows = Periods (7 periods); Elements in same group share similar chemical properties / same valence electrons",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_periodic_table_groups_and_periods_definitions",
        "misconception_tags": ["groups_vs_periods_definitions"],
        "hints": {
            "tier_1": "Columns = Groups (18), Rows = Periods (7).",
            "tier_2": "Groups have elements with similar properties.",
            "tier_3": "Groups (18); Periods (7); similar chemical properties/valence electrons."
        }
    }


def arch_11_group_number_and_similar_chemical_properties(rng: random.Random) -> Dict[str, Any]:
    groups = [
        ("Group 1 (Alkali metals)", ["Lithium ($Li$)", "Sodium ($Na$)", "Potassium ($K$)"], 1, "soft, highly reactive metals that react violently with water releasing hydrogen gas"),
        ("Group 2 (Alkaline earth metals)", ["Beryllium ($Be$)", "Magnesium ($Mg$)", "Calcium ($Ca$)"], 2, "reactive metals that burn with bright flames in oxygen to form basic metal oxides"),
        ("Group 17 (Halogens)", ["Fluorine ($F$)", "Chlorine ($Cl$)", "Bromine ($Br$)", "Iodine ($I$)"], 7, "reactive non-metals that readily accept 1 electron to form salts (-ide) with metals"),
        ("Group 18 (Noble gases)", ["Helium ($He$)", "Neon ($Ne$)", "Argon ($Ar$)"], 8, "completely unreactive, inert non-metal gases with full outer valence electron shells"),
    ]
    grp_name, members, val_e, behavior = rng.choice(groups)

    prompt = (
        f"Consider the elements belonging to **{grp_name}**:\n"
        f"Examples: {', '.join(members)}.\n\n"
        f"1. How many valence electrons do neutral atoms of these elements have in their outermost shell ({val_e})?\n"
        f"2. Describe the characteristic chemical behavior shared by these elements ({behavior.split(' that')[0]}).\n"
        f"3. Explain why chemical similarity occurs among elements placed in the same group."
    )
    sol = (
        f"**Step 1:** Atoms in this group have **{val_e} valence electron{'s' if val_e > 1 else ''}** (helium has 2) in their outermost energy level [1 Mark: Valence electrons].\n\n"
        f"**Step 2:** Chemical behavior: They are {behavior} [1 Mark: Chemical behavior].\n\n"
        f"**Step 3:** Chemical similarity occurs because **valence electrons determine chemical bonding and reactions**; since elements in the same group have the same valence electron configuration, they react in the same way [1 Mark: Reason for similarity]."
    )
    return {
        "id": f"ns9_comp_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{val_e} valence electron(s); {behavior}; Same valence electron count dictates identical bonding behavior",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_group_number_and_similar_chemical_properties",
        "misconception_tags": ["periodic_group_similarity"],
        "hints": {
            "tier_1": f"Check the valence electrons for {grp_name}: {val_e}.",
            "tier_2": "Valence electrons determine how elements bond.",
            "tier_3": f"{val_e}; {behavior}; same valence electrons govern bonding."
        }
    }


def arch_12_metals_nonmetals_and_semimetals_locations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Periodic Table is broadly divided into three main classes of elements: **metals**, **non-metals**, and **semi-metals (metalloids)**.\n\n"
        f"1. Where on the Periodic Table are the **metals** predominantly located?\n"
        f"2. Where on the Periodic Table are the **non-metals** located?\n"
        f"3. Where are the **semi-metals (metalloids)** found, and what visual feature separates metals from non-metals?"
    )
    sol = (
        f"**Step 1:** **Metals** are located on the **left side and center** (spanning Groups 1 to 12 and lower parts of Groups 13 to 16) [1 Mark: Metals location].\n\n"
        f"**Step 2:** **Non-metals** are located on the **far right side** of the table (plus hydrogen on the top left) [1 Mark: Non-metals location].\n\n"
        f"**Step 3:** **Semi-metals (metalloids)** lie along the **diagonal zig-zag dividing line** between metals and non-metals (e.g., boron, silicon, germanium) [1 Mark: Semi-metals & zig-zag line]."
    )
    return {
        "id": f"ns9_comp_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Metals = left and center; Non-metals = far right (plus Hydrogen top left); Semi-metals = along the diagonal zig-zag dividing line",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_metals_nonmetals_and_semimetals_locations",
        "misconception_tags": ["periodic_table_classification_zones"],
        "hints": {
            "tier_1": "Metals make up the left and middle; non-metals are on the right.",
            "tier_2": "The zig-zag staircase line separates them.",
            "tier_3": "Left/center = metals; right = non-metals; zig-zag line = semi-metals."
        }
    }


def arch_13_properties_of_metals_electrical_thermal_malleability(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Copper ($Cu$)", "electrical wiring and cooking pot bases", "high electrical and thermal conductivity, ductile"),
        ("Iron ($Fe$)", "building beams and bridge structures", "high tensile strength, malleable, high melting point"),
        ("Gold ($Au$)", "jewelry and high-reliability electronic contacts", "extremely malleable, ductile, shiny luster, does not corrode"),
        ("Aluminum ($Al$)", "airplane frames and beverage cans", "low density, malleable, good conductor, resistant to corrosion"),
    ]
    elem, app, props = rng.choice(metals)

    prompt = (
        f"Metals display distinctive physical and mechanical properties that make them vital for human industry.\n"
        f"Example: **{elem}**, used for {app}.\n\n"
        f"1. State three characteristic physical properties common to almost all metallic elements.\n"
        f"2. Explain what the terms **malleable** and **ductile** mean.\n"
        f"3. In what state of matter do almost all metals exist at room temperature, and which metal is the only liquid exception?"
    )
    sol = (
        f"**Step 1:** Common physical properties of metals: **shiny metallic luster, high electrical conductivity, high thermal conductivity, high density, and high melting points** [1 Mark: Any three properties].\n\n"
        f"**Step 2:** **Malleable** means can be hammered or rolled into thin sheets without shattering; **Ductile** means can be drawn or stretched into thin wires [1 Mark: Malleable and ductile definitions].\n\n"
        f"**Step 3:** Almost all metals are **solids** at room temperature; the only liquid metal is **mercury ($Hg$)** [1 Mark: Solid state & mercury exception]."
    )
    return {
        "id": f"ns9_comp_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Shiny luster, good electrical/thermal conductor, high melting point; Malleable = hammered into sheets, Ductile = drawn into wires; Solids, liquid exception is mercury (Hg)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_properties_of_metals_electrical_thermal_malleability",
        "misconception_tags": ["metal_physical_properties"],
        "hints": {
            "tier_1": "Malleable = sheets; Ductile = wires.",
            "tier_2": "The only liquid metal at room temperature is mercury.",
            "tier_3": "Shiny/conductive/malleable; Malleable=sheets, Ductile=wires; Solids, mercury is liquid."
        }
    }


def arch_14_properties_of_nonmetals_and_semimetals_silicon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Non-metals and semi-metals (metalloids) have properties that contrast sharply with metals.\n\n"
        f"1. List three typical physical properties of solid **non-metals** (such as sulfur or carbon).\n"
        f"2. What is a **semi-metal (metalloid)** in terms of its physical and electrical properties?\n"
        f"3. Name the most technologically famous semi-metal (Atomic Number 14) and describe its application in microchips."
    )
    sol = (
        f"**Step 1:** Solid non-metals are **dull (lack luster), brittle (break or crumble when struck), and electrical/thermal insulators** (poor conductors) [1 Mark: Non-metal properties].\n\n"
        f"**Step 2:** A **semi-metal** has intermediate properties between metals and non-metals; it looks like a metal (shiny) but conducts electricity weakly, acting as a **semiconductor** [1 Mark: Semi-metal definition].\n\n"
        f"**Step 3:** The element is **Silicon ($Si$)**; it is used as a **semiconductor in computer microchips, processors, and solar photovoltaic cells** because its electrical conductivity can be controlled [1 Mark: Silicon & microchips]."
    )
    return {
        "id": f"ns9_comp_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Dull, brittle, poor electrical/thermal conductors (insulators); Semi-metal = intermediate properties / semiconductor; Silicon (Si), used in microchips and computer electronics",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_properties_of_nonmetals_and_semimetals_silicon",
        "misconception_tags": ["nonmetal_and_semimetal_properties"],
        "hints": {
            "tier_1": "Non-metals are brittle and insulators. Silicon is the semiconductor in microchips.",
            "tier_2": "Element 14 is Silicon (Si).",
            "tier_3": "Dull/brittle/insulators; intermediate properties (semiconductor); Silicon (Si) for microchips."
        }
    }


def arch_15_first_20_elements_symbols_and_names(rng: random.Random) -> Dict[str, Any]:
    first_20 = [
        (1, "Hydrogen", "H", "non-metal"),
        (2, "Helium", "He", "noble gas non-metal"),
        (3, "Lithium", "Li", "alkali metal"),
        (4, "Beryllium", "Be", "alkaline earth metal"),
        (5, "Boron", "B", "semi-metal"),
        (6, "Carbon", "C", "non-metal"),
        (7, "Nitrogen", "N", "non-metal"),
        (8, "Oxygen", "O", "non-metal"),
        (9, "Fluorine", "F", "halogen non-metal"),
        (10, "Neon", "Ne", "noble gas non-metal"),
        (11, "Sodium", "Na", "alkali metal"),
        (12, "Magnesium", "Mg", "alkaline earth metal"),
        (13, "Aluminum", "Al", "metal"),
        (14, "Silicon", "Si", "semi-metal"),
        (15, "Phosphorus", "P", "non-metal"),
        (16, "Sulfur", "S", "non-metal"),
        (17, "Chlorine", "Cl", "halogen non-metal"),
        (18, "Argon", "Ar", "noble gas non-metal"),
        (19, "Potassium", "K", "alkali metal"),
        (20, "Calcium", "Ca", "alkaline earth metal"),
    ]
    z, name, sym, cat = rng.choice(first_20)

    prompt = (
        f"In Grade 9 Natural Sciences, students must know the first 20 elements of the Periodic Table.\n\n"
        f"Consider the element with **Atomic Number {z}**:\n\n"
        f"1. What is the full English name of this element ({name})?\n"
        f"2. Write its official chemical symbol ({sym}). (Ensure correct uppercase/lowercase convention).\n"
        f"3. Classify it broadly as a **metal**, **non-metal**, or **semi-metal**."
    )
    sol = (
        f"**Step 1:** Name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Chemical symbol: **{sym}** (first letter uppercase, second lowercase if present) [1 Mark: Symbol].\n\n"
        f"**Step 3:** Classification: **{cat}** [1 Mark: Classification]."
    )
    return {
        "id": f"ns9_comp_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{name}; {sym}; {cat}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_first_20_elements_symbols_and_names",
        "misconception_tags": ["first_20_elements_identification"],
        "hints": {
            "tier_1": f"Atomic number {z} corresponds to {name}.",
            "tier_2": f"Symbol is {sym}.",
            "tier_3": f"{name}; {sym}; {cat}."
        }
    }


def arch_16_latin_origin_chemical_symbols_iron_copper_sodium(rng: random.Random) -> Dict[str, Any]:
    latin_elements = [
        ("Sodium", "Na", "Natrium", 11, "Group 1 alkali metal"),
        ("Potassium", "K", "Kalium", 19, "Group 1 alkali metal"),
        ("Iron", "Fe", "Ferrum", 26, "Transition metal"),
        ("Copper", "Cu", "Cuprum", 29, "Transition metal"),
        ("Lead", "Pb", "Plumbum", 82, "Post-transition metal"),
        ("Gold", "Au", "Aurum", 79, "Transition precious metal"),
        ("Silver", "Ag", "Argentum", 47, "Transition precious metal"),
    ]
    name, sym, latin, z, cat = rng.choice(latin_elements)

    prompt = (
        f"Several chemical symbols do not match their modern English names because they originate from ancient Latin names.\n\n"
        f"Consider the element **{name}**:\n\n"
        f"1. What is the official chemical symbol for {name}?\n"
        f"2. State the ancient Latin name from which the symbol '{sym}' is derived ({latin}).\n"
        f"3. Why must the second letter of a two-letter chemical symbol always be written in lowercase (e.g. Co vs CO)?"
    )
    sol = (
        f"**Step 1:** Chemical symbol: **{sym}** [1 Mark: Symbol].\n\n"
        f"**Step 2:** Ancient Latin name: **{latin}** [1 Mark: Latin root].\n\n"
        f"**Step 3:** The second letter must be lowercase to **distinguish a single two-letter element from a compound of two different elements**; for instance, $Co$ is the element cobalt, while $CO$ is the compound carbon monoxide [1 Mark: Uppercase/lowercase rule]."
    )
    return {
        "id": f"ns9_comp_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{sym}; {latin}; To avoid confusion between a single element (e.g. Co = cobalt) and a compound (e.g. CO = carbon monoxide)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_latin_origin_chemical_symbols_iron_copper_sodium",
        "misconception_tags": ["chemical_symbols_latin_origin"],
        "hints": {
            "tier_1": f"Symbol for {name} is {sym}.",
            "tier_2": f"Latin name is {latin}.",
            "tier_3": f"{sym}; {latin}; distinguish element from compound (e.g. Co vs CO)."
        }
    }


def arch_17_alkali_metals_group_1_properties_and_oil_storage(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Lithium", "Li", 3, "least vigorous of Group 1, fizzes smoothly"),
        ("Sodium", "Na", 11, "melts into a shiny silver ball and darts rapidly across water surface with yellow flame"),
        ("Potassium", "K", 19, "ignites instantly on contact with water, burning with a distinctive lilac/purple flame"),
    ]
    name, sym, z, reaction_desc = rng.choice(metals)

    prompt = (
        f"The elements of **Group 1** (the Alkali metals), such as **{name}** (${sym}$), display exceptional properties:\n\n"
        f"1. How can alkali metals be mechanically cut in the laboratory, and what is observed on the freshly cut surface?\n"
        f"2. Why must alkali metals always be stored submerged in liquid paraffin oil or mineral oil?\n"
        f"3. What happens to the shiny metallic luster of a freshly cut piece of {name} if it is left exposed to air for a few seconds?"
    )
    sol = (
        f"**Step 1:** Alkali metals are **extremely soft and can easily be cut with a scalpel or butter knife**, revealing a bright, shiny silvery metallic surface [1 Mark: Softness and cut].\n\n"
        f"**Step 2:** They must be stored in oil because they are **extremely reactive with atmospheric oxygen and water vapor**; oil acts as a barrier preventing contact with air and moisture [1 Mark: Storage in oil].\n\n"
        f"**Step 3:** The shiny surface **rapidly tarnishes and turns dull grey/white** as it reacts with oxygen to form a surface layer of metal oxide [1 Mark: Tarnishing/oxidation]."
    )
    return {
        "id": f"ns9_comp_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Cut with a knife (very soft), reveals shiny surface; Stored in paraffin oil to prevent reaction with atmospheric oxygen and water vapor; Rapidly tarnishes/turns dull due to oxidation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_alkali_metals_group_1_properties_and_oil_storage",
        "misconception_tags": ["alkali_metals_softness_oil_storage"],
        "hints": {
            "tier_1": "Alkali metals are soft enough to cut with a butter knife.",
            "tier_2": "Oil prevents contact with air and moisture.",
            "tier_3": "Cut with a knife; stored in oil to prevent oxidation with air/water; tarnishes rapidly."
        }
    }


def arch_18_alkali_metals_reaction_with_water_and_reactivity_trend(rng: random.Random) -> Dict[str, Any]:
    alkalis = [
        ("Lithium ($Li$)", "Lithium hydroxide", "LiOH", "slow bubbling and effervescence, releases hydrogen"),
        ("Sodium ($Na$)", "Sodium hydroxide", "NaOH", "melts into a sphere, vigorous fizzing, skates on water"),
        ("Potassium ($K$)", "Potassium hydroxide", "KOH", "violent ignition, bursts into lilac flame"),
    ]
    metal, hydrox, h_form, obs = rng.choice(alkalis)

    prompt = (
        f"When a small piece of **{metal}** is placed into a trough of cold water containing a few drops of universal indicator or phenolphthalein:\n\n"
        f"1. Write the **word equation** for the chemical reaction between {metal.split(' ')[0]} and water.\n"
        f"2. Name the flammable gas released, and describe the laboratory test that confirms its presence.\n"
        f"3. What color change occurs in the solution, and what does this prove about the product formed?\n"
        f"4. State the trend in reactivity of the alkali metals as one moves **down Group 1** from Lithium to Potassium to Cesium."
    )
    sol = (
        f"**Step 1:** Word equation: **{metal.split(' ')[0]} + Water $\\rightarrow$ {hydrox} + Hydrogen** [1 Mark: Word equation].\n\n"
        f"**Step 2:** Gas: **Hydrogen gas ($H_2$)**; Test: A burning wooden splint placed at the mouth of the test tube makes a distinctive **'pop' sound** [1 Mark: Gas and test].\n\n"
        f"**Step 3:** Indicator turns **blue/purple (universal indicator) or pink (phenolphthalein)**, proving the solution is **strongly basic/alkaline** ({hydrox}) [1 Mark: Indicator change].\n\n"
        f"**Step 4:** Reactivity **increases down Group 1** (Potassium is more reactive than Sodium, which is more reactive than Lithium) [1 Mark: Reactivity trend]."
    )
    return {
        "id": f"ns9_comp_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{metal.split(' ')[0]} + Water -> {hydrox} + Hydrogen; Hydrogen gas (burning splint 'pop' test); Turns blue/purple or pink (strongly basic/alkaline solution); Reactivity increases down the group",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "18_alkali_metals_reaction_with_water_and_reactivity_trend",
        "misconception_tags": ["alkali_metal_water_reactivity_trend"],
        "hints": {
            "tier_1": "Metal + Water -> Metal Hydroxide + Hydrogen.",
            "tier_2": "Hydrogen pops with a burning splint. Solution is alkaline (turns purple).",
            "tier_3": f"{metal.split(' ')[0]} + Water -> {hydrox} + Hydrogen; Hydrogen ('pop'); alkaline/basic; reactivity increases down."
        }
    }


# ==============================================================================
# CLUSTER 3: Subatomic Particles & Atomic Notation (19 - 25)
# ==============================================================================

def arch_19_atomic_number_z_protons_and_electrons_identity(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Carbon", "C", 6, 12),
        ("Nitrogen", "N", 7, 14),
        ("Oxygen", "O", 8, 16),
        ("Fluorine", "F", 9, 19),
        ("Sodium", "Na", 11, 23),
        ("Magnesium", "Mg", 12, 24),
        ("Aluminum", "Al", 13, 27),
        ("Chlorine", "Cl", 17, 35),
    ]
    name, sym, z, a = rng.choice(elements)

    prompt = (
        f"Consider a neutral atom of **{name}** (${sym}$), which has an **Atomic Number ($Z$) of {z}**.\n\n"
        f"1. What subatomic particle specifically defines the **Atomic Number ($Z$)** of an atom?\n"
        f"2. How many protons and how many electrons are present in this neutral atom of {name}?\n"
        f"3. Explain why a neutral atom has zero net electrical charge."
    )
    sol = (
        f"**Step 1:** The **Atomic Number ($Z$)** is defined by the **number of protons** in the atomic nucleus [1 Mark: Definition].\n\n"
        f"**Step 2:** In a neutral atom: **{z} protons** and **{z} electrons** [1 Mark: Proton and electron counts].\n\n"
        f"**Step 3:** The atom is electrically neutral because the positive charge of the protons ($+{z}$) is **exactly balanced** by the equal negative charge of the electrons ($-{z}$), resulting in a net charge of zero ($+{z} - {z} = 0$) [1 Mark: Electrical neutrality]."
    )
    return {
        "id": f"ns9_comp_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Atomic Number = number of protons; {z} protons and {z} electrons; Zero net charge because positive protons equal negative electrons (+{z} - {z} = 0)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_atomic_number_z_protons_and_electrons_identity",
        "misconception_tags": ["atomic_number_proton_definition"],
        "hints": {
            "tier_1": "Atomic number Z = number of protons.",
            "tier_2": "In neutral atoms, protons = electrons.",
            "tier_3": f"Protons; {z} protons, {z} electrons; positive balances negative."
        }
    }


def arch_20_mass_number_a_protons_plus_neutrons(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Lithium", "Li", 3, 7, 4),
        ("Beryllium", "Be", 4, 9, 5),
        ("Boron", "B", 5, 11, 6),
        ("Phosphorus", "P", 15, 31, 16),
        ("Potassium", "K", 19, 39, 20),
        ("Calcium", "Ca", 20, 40, 20),
    ]
    name, sym, z, a, n = rng.choice(elements)

    prompt = (
        f"An atom of **{name}** (${sym}$) has an Atomic Number $Z = {z}$ and a **Mass Number $A = {a}$**.\n\n"
        f"1. Define what the **Mass Number ($A$)** of an atom represents.\n"
        f"2. Where in the atom is virtually all of its mass concentrated?\n"
        f"3. Why are electrons practically ignored when calculating the mass number of an atom?"
    )
    sol = (
        f"**Step 1:** The **Mass Number ($A$)** is the **total number of protons and neutrons (nucleons)** in the atomic nucleus ($A = Z + N$) [1 Mark: Mass number definition].\n\n"
        f"**Step 2:** Virtually all of the mass is concentrated in the dense **atomic nucleus** [1 Mark: Nucleus location].\n\n"
        f"**Step 3:** Electrons have an extremely tiny, negligible mass (approx. $\\frac{{1}}{{1840}}$ the mass of a proton or neutron); their contribution to total atomic mass is negligible [1 Mark: Negligible electron mass]."
    )
    return {
        "id": f"ns9_comp_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Mass Number = total protons + neutrons in nucleus; Concentrated in the nucleus; Electrons have negligible mass (~1/1840 of a nucleon)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_mass_number_a_protons_plus_neutrons",
        "misconception_tags": ["mass_number_nucleons_definition"],
        "hints": {
            "tier_1": "Mass number = protons + neutrons.",
            "tier_2": "Electrons are too light to affect the rounded mass number.",
            "tier_3": "Protons + neutrons; nucleus; electrons have negligible mass."
        }
    }


def arch_21_calculating_neutron_count_from_a_minus_z(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Sodium", "Na", 11, 23),
        ("Magnesium", "Mg", 12, 24),
        ("Aluminum", "Al", 13, 27),
        ("Silicon", "Si", 14, 28),
        ("Phosphorus", "P", 15, 31),
        ("Sulfur", "S", 16, 32),
        ("Chlorine", "Cl", 17, 35),
        ("Argon", "Ar", 18, 40),
        ("Potassium", "K", 19, 39),
        ("Calcium", "Ca", 20, 40),
    ]
    name, sym, z, a = rng.choice(elements)
    neutrons = a - z

    prompt = (
        f"An element tile on the Periodic Table displays the following data for **{name}** (${sym}$):\n"
        f"- **Atomic Number ($Z$):** {z}\n"
        f"- **Mass Number ($A$):** {a}\n\n"
        f"1. State the formula used to calculate the number of **neutrons ($N$)** in an atom.\n"
        f"2. Calculate the exact number of neutrons in this atom of {name}.\n"
        f"3. State the electrical charge of a neutron."
    )
    sol = (
        f"**Step 1:** Formula: $$\\mathbf{{N = A - Z}}$$ (Number of Neutrons = Mass Number $-$ Atomic Number) [1 Mark: Formula].\n\n"
        f"**Step 2:** Calculation: $$N = {a} - {z} = \\mathbf{{{neutrons}\\text{{ neutrons}}}}$$ [1 Mark: Calculation].\n\n"
        f"**Step 3:** A neutron is **neutral** (has an electrical charge of **zero**) [1 Mark: Neutral charge]."
    )
    return {
        "id": f"ns9_comp_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"N = A - Z; {neutrons} neutrons ({a} - {z}); Neutral / zero electrical charge",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_calculating_neutron_count_from_a_minus_z",
        "misconception_tags": ["neutron_calculation_a_minus_z"],
        "hints": {
            "tier_1": f"Neutrons = Mass Number ({a}) minus Atomic Number ({z}).",
            "tier_2": f"{a} - {z} = {neutrons}.",
            "tier_3": f"N = A - Z; {neutrons}; zero charge."
        }
    }


def arch_22_standard_atomic_notation_a_z_x_interpretation(rng: random.Random) -> Dict[str, Any]:
    notations = [
        ("Carbon", "C", 6, 12),
        ("Nitrogen", "N", 7, 14),
        ("Oxygen", "O", 8, 16),
        ("Fluorine", "F", 9, 19),
        ("Sodium", "Na", 11, 23),
        ("Magnesium", "Mg", 12, 24),
        ("Aluminum", "Al", 13, 27),
        ("Chlorine", "Cl", 17, 35),
    ]
    name, sym, z, a = rng.choice(notations)
    neutrons = a - z

    prompt = (
        f"In standard nuclear notation, an atom of **{name}** is written as:\n"
        f"$$\\Large _{{ {z} }}^{{ {a} }} \\text{{{sym}}} $$\n\n"
        f"1. Identify the number represented by the superscript ({a}) and the subscript ({z}).\n"
        f"2. Determine the full subatomic breakdown for this atom:\n"
        f"   - Number of protons:\n"
        f"   - Number of electrons (in neutral state):\n"
        f"   - Number of neutrons:\n"
        f"3. If this atom gains or loses electrons to become an ion, does its atomic number ($Z$) change? Explain."
    )
    sol = (
        f"**Step 1:** Superscript ${a}$ is the **Mass Number ($A$)**; Subscript ${z}$ is the **Atomic Number ($Z$)** [1 Mark: Notation labels].\n\n"
        f"**Step 2:** Subatomic breakdown:\n"
        f"- Protons = **{z}**\n"
        f"- Electrons = **{z}**\n"
        f"- Neutrons = ${a} - {z} =$ **{neutrons}** [1 Mark: Subatomic counts].\n\n"
        f"**Step 3:** **No**; changing electrons creates an ion, but the atomic number ($Z$) represents the number of protons in the nucleus, which remains unchanged [1 Mark: Z remains unchanged]."
    )
    return {
        "id": f"ns9_comp_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Superscript = Mass Number ({a}), Subscript = Atomic Number ({z}); {z} protons, {z} electrons, {neutrons} neutrons; No, Z is proton count and does not change during ionization",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_standard_atomic_notation_a_z_x_interpretation",
        "misconception_tags": ["standard_atomic_notation_interpretation"],
        "hints": {
            "tier_1": f"Top number is mass number ({a}), bottom is atomic number ({z}).",
            "tier_2": f"Protons = {z}, Electrons = {z}, Neutrons = {a} - {z} = {neutrons}.",
            "tier_3": f"Top=A, Bottom=Z; {z}p, {z}e, {neutrons}n; No, Z depends on protons only."
        }
    }


def arch_23_bohr_energy_levels_and_electron_arrangement_first_20(rng: random.Random) -> Dict[str, Any]:
    configs = [
        ("Helium ($He$)", 2, "2", 2, "full first shell"),
        ("Carbon ($C$)", 6, "2, 4", 4, "4 valence electrons"),
        ("Nitrogen ($N$)", 7, "2, 5", 5, "5 valence electrons"),
        ("Oxygen ($O$)", 8, "2, 6", 6, "6 valence electrons"),
        ("Neon ($Ne$)", 10, "2, 8", 8, "full second shell, noble gas"),
        ("Sodium ($Na$)", 11, "2, 8, 1", 1, "1 valence electron"),
        ("Magnesium ($Mg$)", 12, "2, 8, 2", 2, "2 valence electrons"),
        ("Chlorine ($Cl$)", 17, "2, 8, 7", 7, "7 valence electrons"),
        ("Argon ($Ar$)", 18, "2, 8, 8", 8, "full third shell, noble gas"),
        ("Calcium ($Ca$)", 20, "2, 8, 8, 2", 2, "2 valence electrons"),
    ]
    elem, z, cfg, val, note = rng.choice(configs)

    prompt = (
        f"In the Bohr model of the atom, electrons occupy discrete circular energy levels (shells) around the nucleus.\n"
        f"Consider a neutral atom of **{elem}** (Atomic Number $Z = {z}$).\n\n"
        f"1. State the maximum number of electrons that can be held in Shell 1 and Shell 2.\n"
        f"2. Write the electron configuration (arrangement in energy levels) for {elem}.\n"
        f"3. How many electrons are present in its outermost (valence) energy level ({val})?"
    )
    sol = (
        f"**Step 1:** Maximum capacities: **Shell 1 holds a maximum of 2 electrons**; **Shell 2 holds a maximum of 8 electrons** [1 Mark: Shell capacities].\n\n"
        f"**Step 2:** Electron configuration for $Z = {z}$: **{cfg}** [1 Mark: Electron configuration].\n\n"
        f"**Step 3:** Outermost valence electrons: **{val} valence electron{'s' if val > 1 else ''}** [1 Mark: Valence count]."
    )
    return {
        "id": f"ns9_comp_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Shell 1 = max 2, Shell 2 = max 8; Configuration: {cfg}; {val} valence electron(s)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "23_bohr_energy_levels_and_electron_arrangement_first_20",
        "misconception_tags": ["bohr_model_electron_configuration"],
        "hints": {
            "tier_1": "Capacities: 2 in first shell, 8 in second, 8 in third.",
            "tier_2": f"For {z} electrons: fill 2, then up to 8. Result is {cfg}.",
            "tier_3": f"Shell 1: 2, Shell 2: 8; {cfg}; {val} valence electrons."
        }
    }


def arch_24_valence_electrons_and_group_number_correlation(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Lithium ($Li$)", 1, 1, "Alkali metal"),
        ("Sodium ($Na$)", 1, 1, "Alkali metal"),
        ("Magnesium ($Mg$)", 2, 2, "Alkaline earth metal"),
        ("Calcium ($Ca$)", 2, 2, "Alkaline earth metal"),
        ("Aluminum ($Al$)", 13, 3, "Group 13 metal"),
        ("Carbon ($C$)", 14, 4, "Group 14 non-metal"),
        ("Nitrogen ($N$)", 15, 5, "Group 15 non-metal"),
        ("Oxygen ($O$)", 16, 6, "Group 16 non-metal"),
        ("Chlorine ($Cl$)", 17, 7, "Group 17 halogen"),
    ]
    elem, grp, val, desc = rng.choice(examples)

    prompt = (
        f"The Periodic Table is structured so that an element's position directly reflects its electronic structure.\n\n"
        f"Consider **{elem}**, located in **Group {grp}**:\n\n"
        f"1. How many **valence electrons** does this element have ({val})?\n"
        f"2. Explain the general rule connecting main group numbers (Groups 1, 2, 13–18) to the number of valence electrons.\n"
        f"3. Why are valence electrons so important in the formation of chemical compounds?"
    )
    sol = (
        f"**Step 1:** It has **{val} valence electron{'s' if val > 1 else ''}** [1 Mark: Valence electrons].\n\n"
        f"**Step 2:** For Groups 1 and 2, valence electrons equal the group number (1 and 2); for Groups 13 to 18, valence electrons equal the **group number minus 10** (e.g. Group {grp} $\\rightarrow$ {val}) [1 Mark: Group number rule].\n\n"
        f"**Step 3:** Valence electrons are the outermost electrons that **participate in chemical bonding** (by being shared, lost, or gained) to achieve stable octet arrangements [1 Mark: Role in bonding]."
    )
    return {
        "id": f"ns9_comp_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{val} valence electron(s); Group number rule: Grp 1-2 = group number, Grp 13-18 = group number minus 10; Valence electrons participate directly in chemical bonding",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_valence_electrons_and_group_number_correlation",
        "misconception_tags": ["valence_electrons_group_relationship"],
        "hints": {
            "tier_1": f"For Group {grp}: if above 10, subtract 10 to find valence electrons.",
            "tier_2": f"{grp} -> {val} valence electrons.",
            "tier_3": f"{val}; Group minus 10 rule; valence electrons participate in bonding."
        }
    }


def arch_25_noble_gases_group_18_stability_and_inert_nature(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("Helium ($He$)", 2, "2 electrons (full duet in Shell 1)", "filling weather balloons and party balloons safely without fire risk"),
        ("Neon ($Ne$)", 10, "2, 8 (full octet of 8 in Shell 2)", "high-voltage advertising signs that glow red-orange"),
        ("Argon ($Ar$)", 18, "2, 8, 8 (full octet of 8 in Shell 3)", "inert shielding gas in tungsten arc welding and incandescent light bulbs"),
    ]
    elem, z, cfg, app = rng.choice(gases)

    prompt = (
        f"The elements of **Group 18** (the Noble Gases), such as **{elem}**, are famously non-reactive.\n\n"
        f"1. Describe the electron configuration of {elem} ({cfg}) and explain why its outer shell makes it so stable.\n"
        f"2. Why do noble gases almost never form chemical compounds with other elements under normal conditions?\n"
        f"3. Name the practical application of {elem} related to its chemical inertness ({app.split(' ')[0]})."
    )
    sol = (
        f"**Step 1:** {elem} has {cfg}; its outermost energy level is **completely full (stable octet/duet)** [1 Mark: Full outer shell].\n\n"
        f"**Step 2:** Because their outer shell is completely full, they have **zero tendency to lose, gain, or share electrons**, making them chemically inert and unreactive [1 Mark: Inert nature].\n\n"
        f"**Step 3:** Practical application: **{app}** [1 Mark: Practical use]."
    )
    return {
        "id": f"ns9_comp_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Full outer electron shell ({cfg}); Inert because they have no tendency to lose, gain or share electrons; Application: {app}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_noble_gases_group_18_stability_and_inert_nature",
        "misconception_tags": ["noble_gases_inert_stability"],
        "hints": {
            "tier_1": "Group 18 elements have full valence shells.",
            "tier_2": "Full shell means they don't gain or lose electrons.",
            "tier_3": f"Full outer shell ({cfg}); inert / no tendency to bond; {app}."
        }
    }


# ==============================================================================
# DISPATCH DICT (01 - 25)
# ==============================================================================

BUILDERS_01_25 = {
    "01_compound_definition_and_chemical_bonding": arch_01_compound_definition_and_chemical_bonding,
    "02_element_vs_compound_fundamental_distinction": arch_02_element_vs_compound_fundamental_distinction,
    "03_pure_substance_vs_mixture_particulate_model": arch_03_pure_substance_vs_mixture_particulate_model,
    "04_diatomic_elements_seven_homonuclear_molecules": arch_04_diatomic_elements_seven_homonuclear_molecules,
    "05_molecular_compounds_discrete_particle_clusters": arch_05_molecular_compounds_discrete_particle_clusters,
    "06_crystal_lattice_structures_ionic_repeating_networks": arch_06_crystal_lattice_structures_ionic_repeating_networks,
    "07_fixed_ratio_of_atoms_law_of_constant_composition": arch_07_fixed_ratio_of_atoms_law_of_constant_composition,
    "08_physical_mixture_vs_chemical_compound_separation": arch_08_physical_mixture_vs_chemical_compound_separation,
    "09_particle_diagram_classifying_element_compound_mixture": arch_09_particle_diagram_classifying_element_compound_mixture,
    "10_periodic_table_groups_and_periods_definitions": arch_10_periodic_table_groups_and_periods_definitions,
    "11_group_number_and_similar_chemical_properties": arch_11_group_number_and_similar_chemical_properties,
    "12_metals_nonmetals_and_semimetals_locations": arch_12_metals_nonmetals_and_semimetals_locations,
    "13_properties_of_metals_electrical_thermal_malleability": arch_13_properties_of_metals_electrical_thermal_malleability,
    "14_properties_of_nonmetals_and_semimetals_silicon": arch_14_properties_of_nonmetals_and_semimetals_silicon,
    "15_first_20_elements_symbols_and_names": arch_15_first_20_elements_symbols_and_names,
    "16_latin_origin_chemical_symbols_iron_copper_sodium": arch_16_latin_origin_chemical_symbols_iron_copper_sodium,
    "17_alkali_metals_group_1_properties_and_oil_storage": arch_17_alkali_metals_group_1_properties_and_oil_storage,
    "18_alkali_metals_reaction_with_water_and_reactivity_trend": arch_18_alkali_metals_reaction_with_water_and_reactivity_trend,
    "19_atomic_number_z_protons_and_electrons_identity": arch_19_atomic_number_z_protons_and_electrons_identity,
    "20_mass_number_a_protons_plus_neutrons": arch_20_mass_number_a_protons_plus_neutrons,
    "21_calculating_neutron_count_from_a_minus_z": arch_21_calculating_neutron_count_from_a_minus_z,
    "22_standard_atomic_notation_a_z_x_interpretation": arch_22_standard_atomic_notation_a_z_x_interpretation,
    "23_bohr_energy_levels_and_electron_arrangement_first_20": arch_23_bohr_energy_levels_and_electron_arrangement_first_20,
    "24_valence_electrons_and_group_number_correlation": arch_24_valence_electrons_and_group_number_correlation,
    "25_noble_gases_group_18_stability_and_inert_nature": arch_25_noble_gases_group_18_stability_and_inert_nature,
}
