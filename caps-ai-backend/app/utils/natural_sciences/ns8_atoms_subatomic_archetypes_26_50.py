"""
Grade 8 Natural Sciences - Term 2: Atoms (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/01. Atoms.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Molecules of Elements & Diatomic Gases (26 - 32)
# ==============================================================================

def arch_26_molecules_of_elements_definition(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Oxygen gas ($O_2$)", "two oxygen atoms chemically bonded together"),
        ("Nitrogen gas ($N_2$)", "two nitrogen atoms chemically bonded together"),
        ("Ozone gas ($O_3$)", "three oxygen atoms chemically bonded together"),
        ("Phosphorus ($P_4$)", "four phosphorus atoms chemically bonded in a tetrahedral unit"),
    ]
    sub, desc = rng.choice(examples)

    prompt = (
        f"Consider the substance: **{sub}** ({desc}).\n\n"
        f"1. Define what a **molecule of an element** is in chemistry.\n"
        f"2. Explain why {sub.split(' ')[0]} is classified as an element even though it exists as molecules rather than isolated single atoms."
    )
    sol = (
        f"**Step 1:** A molecule of an element consists of **two or more atoms of the same chemical element chemically bonded together** [1 Mark: Definition].\n\n"
        f"**Step 2:** It is an element because it contains **only one type (kind) of atom**; there are no other chemical elements bonded to it [1 Mark: Element classification]."
    )
    return {
        "id": f"ns8_atom_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Two or more identical atoms chemically bonded; classified as an element because it contains only one type of atom",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "26_molecules_of_elements_definition",
        "misconception_tags": ["molecule_of_an_element"],
        "hints": {
            "tier_1": "Does it have more than one type of atom or only one type?",
            "tier_2": "A molecule is bonded atoms. If all atoms are the same, it's a molecule of an element.",
            "tier_3": "Two or more identical atoms bonded; only one type of atom means it's an element."
        }
    }


def arch_27_diatomic_elements_the_septet(rng: random.Random) -> Dict[str, Any]:
    diatomics = [
        ("Hydrogen", "H_2", "gas", "burns with a characteristic 'pop' sound"),
        ("Nitrogen", "N_2", "gas", "triple-bonded inert atmospheric gas"),
        ("Oxygen", "O_2", "gas", "relights a glowing wooden splint"),
        ("Fluorine", "F_2", "pale yellow gas", "most reactive diatomic halogen"),
        ("Chlorine", "Cl_2", "yellow-green gas", "toxic bleaching gas"),
        ("Bromine", "Br_2", "reddish-brown liquid", "only liquid diatomic non-metal at room temp"),
        ("Iodine", "I_2", "purple-black solid", "sublimes into purple gas upon heating"),
    ]
    elem, formula, state, fact = rng.choice(diatomics)

    prompt = (
        f"There are seven non-metal elements on the Periodic Table that naturally exist as **diatomic molecules**.\n\n"
        f"1. State what the word **diatomic** literally means.\n"
        f"2. Write the correct chemical formula and state of matter for pure **{elem}** at room temperature ($25^\\circ\\text{{C}}$).\n"
        f"3. Name any two other diatomic elements from the seven."
    )
    sol = (
        f"**Step 1:** Diatomic literally means consisting of **two atoms** chemically bonded together [1 Mark: Diatomic meaning].\n\n"
        f"**Step 2:** Formula: **${formula}$**; State: **{state}** [1 Mark: Formula and State].\n\n"
        f"**Step 3:** Other examples include: Hydrogen ($H_2$), Nitrogen ($N_2$), Oxygen ($O_2$), Fluorine ($F_2$), Chlorine ($Cl_2$), Bromine ($Br_2$), or Iodine ($I_2$) [1 Mark: Other examples]."
    )
    return {
        "id": f"ns8_atom_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Consisting of two atoms bonded; {formula} ({state}); e.g. H2, N2, O2, Cl2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "27_diatomic_elements_the_septet",
        "misconception_tags": ["diatomic_elements_septet"],
        "hints": {
            "tier_1": "Di = two. Diatomic = two atoms bonded together.",
            "tier_2": f"Formula for {elem} has subscript 2: {formula}.",
            "tier_3": f"Consisting of two bonded atoms; ${formula}$; examples: $O_2, N_2, H_2, Cl_2$."
        }
    }


def arch_28_chemical_bonding_forces_between_atoms(rng: random.Random) -> Dict[str, Any]:
    analogies = [
        ("powerful microscopic magnets", "electrostatic forces of attraction hold atoms tightly together"),
        ("interlocking puzzle pieces held by electrostatic glue", "shared or transferred electrons create mutual attraction between atomic nuclei"),
        ("two people holding hands tightly", "chemical bonds require significant energy input to break apart"),
    ]
    analogy, explanation = rng.choice(analogies)

    prompt = (
        f"When atoms combine to form molecules, they are held together by **chemical bonds** ({analogy}).\n\n"
        f"1. What is a **chemical bond** in terms of forces of attraction?\n"
        f"2. Which subatomic particles are directly involved in forming chemical bonds between atoms?\n"
        f"3. What must be supplied to a molecule in order to break its chemical bonds?"
    )
    sol = (
        f"**Step 1:** A chemical bond is a **strong electrostatic force of attraction** that holds atoms together in a molecule or crystal lattice [1 Mark: Bond definition].\n\n"
        f"**Step 2:** **Electrons** (specifically valence electrons in the outermost shells) are directly involved in bonding [1 Mark: Subatomic particle].\n\n"
        f"**Step 3:** **Energy** (such as heat or electrical energy) must be absorbed/supplied to break chemical bonds [1 Mark: Energy requirement]."
    )
    return {
        "id": f"ns8_atom_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Electrostatic force of attraction holding atoms together; electrons (valence); energy (heat/electricity) is required to break bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_chemical_bonding_forces_between_atoms",
        "misconception_tags": ["chemical_bonding_concept"],
        "hints": {
            "tier_1": "Bonds are electrical attractions between atoms.",
            "tier_2": "Electrons form the bond; breaking bonds takes energy.",
            "tier_3": "Electrostatic attraction; electrons; energy (heat/electricity) needed to break bonds."
        }
    }


def arch_29_particle_model_diatomic_molecules(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Oxygen gas ($O_2$)", "#ef4444", "red", "pairs of identical red spheres touching/bonded"),
        ("Nitrogen gas ($N_2$)", "#3b82f6", "blue", "pairs of identical blue spheres touching/bonded"),
        ("Chlorine gas ($Cl_2$)", "#10b981", "green", "pairs of identical green spheres touching/bonded"),
    ]
    name, col, col_name, desc = rng.choice(cases)

    # Dynamic particle SVG showing diatomic pairs vs single atoms
    svg = (
        f'<svg viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="15" y="15" width="310" height="150" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="170" y="35" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Particle Model: {name}</text>'
        # Pair 1
        f'<circle cx="70" cy="80" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        f'<circle cx="98" cy="80" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        # Pair 2
        f'<circle cx="160" cy="115" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        f'<circle cx="188" cy="115" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        # Pair 3
        f'<circle cx="235" cy="75" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        f'<circle cx="263" cy="75" r="16" fill="{col}" stroke="#1e293b" stroke-width="1.5"/>'
        f'<text x="170" y="155" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">{desc}</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model representation for **{name}**.\n\n"
        f"1. How many molecules of {name.split(' ')[0]} are shown in this container?\n"
        f"2. How many individual atoms are present in total?\n"
        f"3. Explain why the spheres are grouped in touching pairs rather than floating as single isolated spheres."
    )
    sol = (
        f"**Step 1:** There are **3 diatomic molecules** shown [1 Mark: Molecule count].\n\n"
        f"**Step 2:** Each molecule has 2 atoms, so $3 \\times 2 = \\mathbf{{6}}$ **total atoms** [1 Mark: Total atoms].\n\n"
        f"**Step 3:** {name.split(' ')[0]} is a **diatomic element**; its atoms are chemically bonded in pairs ($O_2$, $N_2$, or $Cl_2$) because bonded pairs are chemically stable [1 Mark: Diatomic bonding explanation]."
    )
    return {
        "id": f"ns8_atom_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"3 molecules; 6 atoms total; touching pairs represent diatomic molecules chemically bonded together",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_particle_model_diatomic_molecules",
        "misconception_tags": ["particle_model_diatomic_molecules"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Count the pairs to find molecules; count each circle to find atoms.",
            "tier_2": "3 pairs = 3 molecules; 6 circles = 6 atoms.",
            "tier_3": "3 molecules; 6 total atoms; diatomic molecules bond in pairs."
        }
    }


def arch_30_monoatomic_noble_gases_vs_diatomic_gases(rng: random.Random) -> Dict[str, Any]:
    noble = rng.choice([("Helium (He)", "party balloons"), ("Neon (Ne)", "advertising signs"), ("Argon (Ar)", "welding shielding gas")])
    diatomic = rng.choice([("Oxygen ($O_2$)", "breathing"), ("Nitrogen ($N_2$)", "atmospheric stability"), ("Chlorine ($Cl_2$)", "water treatment")])

    prompt = (
        f"Compare the microscopic particle arrangements of two gases:\n"
        f"- Gas A: **{noble[0]}** (used in {noble[1]})\n"
        f"- Gas B: **{diatomic[0]}** (used in {diatomic[1]})\n\n"
        f"1. Explain why Gas A exists naturally as **monoatomic** (single isolated) atoms while Gas B exists as **diatomic** molecules.\n"
        f"2. How does the outer electron shell configuration of {noble[0].split(' ')[0]} explain its lack of bonding?"
    )
    sol = (
        f"**Step 1:** {noble[0].split(' ')[0]} has a **full, stable outer electron shell** and has no need to bond with other atoms, existing as monoatomic atoms. In contrast, {diatomic[0].split(' ')[0]} has an incomplete valence shell and must share electrons with another atom to achieve stability, forming diatomic molecules [1 Mark: Monoatomic vs Diatomic reason].\n\n"
        f"**Step 2:** Its full outer shell gives it **maximum chemical stability (inertness)**, meaning it does not gain, lose, or share electrons under standard conditions [1 Mark: Valence stability]."
    )
    return {
        "id": f"ns8_atom_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{noble[0].split(' ')[0]} has full outer electron shell so it stays single; {diatomic[0].split(' ')[0]} needs to share electrons to fill outer shell; full shell equals inertness",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "30_monoatomic_noble_gases_vs_diatomic_gases",
        "misconception_tags": ["monoatomic_vs_diatomic_gases"],
        "hints": {
            "tier_1": "Noble gases already have full outer electron shells.",
            "tier_2": "Full shell = happy single atom. Incomplete shell = must bond with a partner.",
            "tier_3": "Noble gases have full outer shells (monoatomic); active non-metals share electrons (diatomic)."
        }
    }


def arch_31_subscript_notation_in_element_molecules(rng: random.Random) -> Dict[str, Any]:
    symbols = [
        ("2O", "O_2", "Oxygen"),
        ("2H", "H_2", "Hydrogen"),
        ("2N", "N_2", "Nitrogen"),
        ("2Cl", "Cl_2", "Chlorine"),
    ]
    coeff, sub, elem = rng.choice(symbols)

    prompt = (
        f"In chemistry, careful notation distinguishes between **${coeff}$** and **${sub}$**.\n\n"
        f"1. Explain what **${coeff}$** represents at a particle level.\n"
        f"2. Explain what **${sub}$** represents at a particle level.\n"
        f"3. Are the chemical properties of ${coeff}$ and ${sub}$ identical? Explain."
    )
    sol = (
        f"**Step 1:** **${coeff}$** represents **two separate, unbonded (isolated) atoms** of {elem} [1 Mark: Coefficient meaning].\n\n"
        f"**Step 2:** **${sub}$** represents **one single molecule** composed of two {elem} atoms **chemically bonded together** [1 Mark: Subscript meaning].\n\n"
        f"**Step 3:** **No**, isolated single atoms (${coeff}$) are extremely reactive and unstable free radicals, whereas bonded diatomic molecules (${sub}$) are stable chemical substances [1 Mark: Property contrast]."
    )
    return {
        "id": f"ns8_atom_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"${coeff}$ = two separate unbonded atoms; ${sub}$ = one molecule of two bonded atoms; Not identical properties because free atoms are much more reactive",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_subscript_notation_in_element_molecules",
        "misconception_tags": ["coefficients_vs_subscripts"],
        "hints": {
            "tier_1": "A big number in front means separate items; a small number below means bonded together.",
            "tier_2": f"{coeff} is two separate atoms; {sub} is one bonded molecule.",
            "tier_3": f"${coeff}$ = two unbonded atoms; ${sub}$ = one bonded molecule; different chemical reactivity."
        }
    }


def arch_32_gaseous_diatomic_elements_in_atmosphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Clean, dry atmospheric air at sea level is a mixture of several gases.\n\n"
        f"1. What are the two most abundant gases in Earth's atmosphere, and what approximate percentage does each comprise?\n"
        f"2. Write the chemical formula for each of these two gases, explaining why they are written with a subscript '2'.\n"
        f"3. Name one noble gas present in small quantities (~0,93%) in air, stating its chemical formula."
    )
    sol = (
        f"**Step 1:** The two most abundant gases are **Nitrogen ($~78\\%$)** and **Oxygen ($~21\\%$)** [1 Mark: Gases and percentages].\n\n"
        f"**Step 2:** Their formulas are **$N_2$** and **$O_2$**. They have subscript '2' because both exist as **diatomic molecules** (pairs of bonded atoms) [1 Mark: Diatomic formulas].\n\n"
        f"**Step 3:** The noble gas is **Argon ($Ar$)**, written as a single atom without subscripts because it is monoatomic [1 Mark: Argon]."
    )
    return {
        "id": f"ns8_atom_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Nitrogen (~78%) and Oxygen (~21%); Formulas N2 and O2 (diatomic molecules); Argon (Ar) is monoatomic noble gas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_gaseous_diatomic_elements_in_atmosphere",
        "misconception_tags": ["atmospheric_gases_composition"],
        "hints": {
            "tier_1": "Air is mostly nitrogen and oxygen.",
            "tier_2": "Nitrogen is ~78% (N2), Oxygen is ~21% (O2). Argon is ~1% (Ar).",
            "tier_3": "Nitrogen 78% (N2), Oxygen 21% (O2); Argon (Ar) noble gas."
        }
    }


# ==============================================================================
# CLUSTER 5: Compounds & Chemical Formulas (33 - 40)
# ==============================================================================

def arch_33_compounds_definition_fixed_ratio(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Water", "H_2O", "Hydrogen and Oxygen", "2 : 1", "2 hydrogen atoms to every 1 oxygen atom"),
        ("Carbon dioxide", "CO_2", "Carbon and Oxygen", "1 : 2", "1 carbon atom to every 2 oxygen atoms"),
        ("Methane", "CH_4", "Carbon and Hydrogen", "1 : 4", "1 carbon atom to every 4 hydrogen atoms"),
        ("Ammonia", "NH_3", "Nitrogen and Hydrogen", "1 : 3", "1 nitrogen atom to every 3 hydrogen atoms"),
    ]
    name, formula, elements, ratio, ratio_desc = rng.choice(compounds)

    prompt = (
        f"Consider the chemical compound: **{name} (${formula}$)**.\n\n"
        f"1. Define what a **chemical compound** is.\n"
        f"2. Identify the constituent elements that form {name}, and state the **fixed ratio** of atoms in which they are chemically combined ({ratio_desc}).\n"
        f"3. Can the ratio of elements in {name} be changed while still remaining {name}?"
    )
    sol = (
        f"**Step 1:** A chemical compound is a pure substance formed when **two or more different elements are chemically bonded together in a fixed ratio** [1 Mark: Definition].\n\n"
        f"**Step 2:** {name} is made of **{elements}** in a fixed atom ratio of **{ratio}** [1 Mark: Elements and Ratio].\n\n"
        f"**Step 3:** **No**, if the ratio changes (e.g. changing $H_2O$ to $H_2O_2$), an entirely different chemical substance is formed [1 Mark: Fixed ratio law]."
    )
    return {
        "id": f"ns8_atom_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Substance of two or more different elements chemically bonded in fixed ratio; {elements} in ratio {ratio}; No, ratio is strictly fixed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_compounds_definition_fixed_ratio",
        "misconception_tags": ["compound_definition_fixed_ratio"],
        "hints": {
            "tier_1": "Compounds have different elements bonded in a fixed recipe.",
            "tier_2": f"Water is always H2O; if you change the ratio it's not {name} anymore.",
            "tier_3": f"Two or more different elements bonded in fixed ratio; {elements} in {ratio}; No, ratio is strictly fixed."
        }
    }


def arch_34_properties_of_compound_differ_from_elements(rng: random.Random) -> Dict[str, Any]:
    examples = [
        (
            "Sodium chloride (table salt, $NaCl$)",
            "Sodium metal is a soft, silvery, highly dangerous metal that explodes in water; Chlorine is a choking yellow-green poisonous gas",
            "safe, edible white crystalline seasoning essential for animal life",
        ),
        (
            "Water ($H_2O$)",
            "Hydrogen gas is explosive and extremely flammable; Oxygen gas actively supports combustion and burning",
            "liquid water puts out fires and is non-flammable",
        ),
        (
            "Carbon dioxide ($CO_2$)",
            "Carbon is a black combustible solid (coal/charcoal); Oxygen is a reactive gas supporting combustion",
            "a colourless, heavy gas used in fire extinguishers to smother flames",
        ),
    ]
    compound, element_props, compound_props = rng.choice(examples)

    prompt = (
        f"A fundamental principle in chemistry is that **the properties of a compound are completely different from the properties of the individual elements that make it up**.\n\n"
        f"Examine: **{compound}**.\n\n"
        f"1. Describe the hazardous or distinct properties of its constituent elements ({element_props.split(';')[0]}).\n"
        f"2. Contrast these with the properties of the resulting compound ({compound_props}).\n"
        f"3. Why do the original properties disappear when a compound forms?"
    )
    sol = (
        f"**Step 1:** Constituent element properties: {element_props} [1 Mark: Element properties].\n\n"
        f"**Step 2:** Resulting compound properties: {compound_props} [1 Mark: Compound contrast].\n\n"
        f"**Step 3:** During chemical bonding, atoms share or transfer electrons, rearranging into a completely **new chemical structure with entirely new chemical bonds and properties** [1 Mark: Bonding explanation]."
    )
    return {
        "id": f"ns8_atom_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Elements have distinct/dangerous properties ({element_props}); Compound is completely different ({compound_props}); Chemical bonding rearranges electrons into a new substance",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "34_properties_of_compound_differ_from_elements",
        "misconception_tags": ["compound_vs_element_properties"],
        "hints": {
            "tier_1": "Salt is made of explosive sodium and toxic chlorine, yet you eat it on chips.",
            "tier_2": "Chemical reactions create completely new substances with brand new properties.",
            "tier_3": "Elements differ radically from compound; bonding creates new properties."
        }
    }


def arch_35_interpreting_formulas_binary_compounds(rng: random.Random) -> Dict[str, Any]:
    binaries = [
        ("Sodium chloride", "NaCl", "Sodium and Chlorine", 1, 1),
        ("Magnesium oxide", "MgO", "Magnesium and Oxygen", 1, 1),
        ("Copper(II) oxide", "CuO", "Copper and Oxygen", 1, 1),
        ("Iron(II) sulfide", "FeS", "Iron and Sulfur", 1, 1),
        ("Carbon monoxide", "CO", "Carbon and Oxygen", 1, 1),
    ]
    name, formula, elements, c1, c2 = rng.choice(binaries)

    prompt = (
        f"The chemical formula for **{name}** is written as **${formula}$**.\n\n"
        f"1. What is meant by a **binary compound**?\n"
        f"2. Name the two elements present in {name}.\n"
        f"3. In what ratio are these two elements combined in one unit of ${formula}$?"
    )
    sol = (
        f"**Step 1:** A binary compound is a chemical compound composed of **exactly two different chemical elements** [1 Mark: Binary definition].\n\n"
        f"**Step 2:** The elements are **{elements}** [1 Mark: Elements].\n\n"
        f"**Step 3:** They combine in a **{c1} : {c2} ratio** (1 atom of each element per formula unit) [1 Mark: Ratio]."
    )
    return {
        "id": f"ns8_atom_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Compound of two different elements; {elements}; Ratio is {c1}:{c2}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_interpreting_formulas_binary_compounds",
        "misconception_tags": ["binary_compounds_formula"],
        "hints": {
            "tier_1": "Binary means two. A binary compound has two elements.",
            "tier_2": f"{name} is made of {elements}.",
            "tier_3": f"Two elements; {elements}; {c1}:{c2} ratio."
        }
    }


def arch_36_counting_atoms_in_polyatomic_formulas(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Calcium carbonate (limestone/chalk)", "CaCO_3", [("Calcium", 1), ("Carbon", 1), ("Oxygen", 3)], 5),
        ("Sulfuric acid", "H_2SO_4", [("Hydrogen", 2), ("Sulfur", 1), ("Oxygen", 4)], 7),
        ("Glucose", "C_6H_{12}O_6", [("Carbon", 6), ("Hydrogen", 12), ("Oxygen", 6)], 24),
        ("Sodium hydroxide", "NaOH", [("Sodium", 1), ("Oxygen", 1), ("Hydrogen", 1)], 3),
        ("Nitric acid", "HNO_3", [("Hydrogen", 1), ("Nitrogen", 1), ("Oxygen", 3)], 5),
    ]
    name, formula, breakdown, total = rng.choice(compounds)
    breakdown_str = ", ".join([f"{count} {elem} atom(s)" for elem, count in breakdown])

    prompt = (
        f"Consider the chemical formula for **{name}**: **${formula}$**.\n\n"
        f"1. How many different chemical elements are present in this compound?\n"
        f"2. Give the exact count of each element's atoms in one molecule/unit of ${formula}$.\n"
        f"3. Calculate the total number of atoms combined in one single formula unit."
    )
    sol = (
        f"**Step 1:** Number of different elements: **{len(breakdown)}** [1 Mark: Element count].\n\n"
        f"**Step 2:** Atom breakdown: **{breakdown_str}** [1 Mark: Breakdown].\n\n"
        f"**Step 3:** Total number of atoms = **{total} atoms** [1 Mark: Total count]."
    )
    return {
        "id": f"ns8_atom_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{len(breakdown)} elements; {breakdown_str}; Total: {total} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_counting_atoms_in_polyatomic_formulas",
        "misconception_tags": ["counting_atoms_in_formulas"],
        "hints": {
            "tier_1": "Count capital letters for elements; sum all subscripts (or 1 if no number).",
            "tier_2": f"{name} contains {len(breakdown)} elements.",
            "tier_3": f"{len(breakdown)} elements; {breakdown_str}; total {total} atoms."
        }
    }


def arch_37_particle_diagram_compounds_vs_elements(rng: random.Random) -> Dict[str, Any]:
    models = [
        (
            "Water ($H_2O$)",
            "one red central Oxygen atom bonded to two smaller white Hydrogen atoms",
            "#ef4444", "#f8fafc", "#334155",
            "Compound",
            "atoms of two different elements are chemically bonded together"
        ),
        (
            "Carbon dioxide ($CO_2$)",
            "one central black Carbon atom bonded to two red Oxygen atoms",
            "#1e293b", "#ef4444", "#ffffff",
            "Compound",
            "atoms of different elements are bonded in a fixed 1:2 ratio"
        ),
    ]
    name, desc, c_main, c_sub, text_col, classification, reason = rng.choice(models)

    svg = (
        f'<svg viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="15" y="15" width="310" height="150" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="170" y="35" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Molecular Model: {name}</text>'
        # Molecule 1
        f'<circle cx="80" cy="90" r="18" fill="{c_main}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="60" cy="74" r="12" fill="{c_sub}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="100" cy="74" r="12" fill="{c_sub}" stroke="#0f172a" stroke-width="1.5"/>'
        # Molecule 2
        f'<circle cx="240" cy="90" r="18" fill="{c_main}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="220" cy="74" r="12" fill="{c_sub}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="260" cy="74" r="12" fill="{c_sub}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="170" y="150" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{desc}</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram representing **{name}**.\n\n"
        f"1. Is this substance classified as an **element** or a **compound**?\n"
        f"2. Provide evidence from the diagram supporting your classification.\n"
        f"3. How many molecules and how many total atoms are represented in this container?"
    )
    sol = (
        f"**Step 1:** It is classified as a **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Evidence: {reason} (represented by two different colours/sizes of spheres joined together) [1 Mark: Evidence].\n\n"
        f"**Step 3:** There are **2 molecules** containing a total of **6 atoms** (3 atoms per molecule) [1 Mark: Counts]."
    )
    return {
        "id": f"ns8_atom_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{classification}; {reason}; 2 molecules, 6 atoms total",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_particle_diagram_compounds_vs_elements",
        "misconception_tags": ["particle_diagram_element_vs_compound"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Different colors/sizes of spheres bonded together = compound.",
            "tier_2": "Count the clusters: 2 clusters (molecules). Each cluster has 3 spheres = 6 spheres total.",
            "tier_3": f"{classification}; {reason}; 2 molecules, 6 atoms total."
        }
    }


def arch_38_naming_binary_compounds_rules(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Magnesium", "Oxygen", "Magnesium oxide", "MgO"),
        ("Iron", "Sulfur", "Iron sulfide", "FeS"),
        ("Sodium", "Chlorine", "Sodium chloride", "NaCl"),
        ("Calcium", "Bromine", "Calcium bromide", "CaBr2"),
        ("Potassium", "Iodine", "Potassium iodide", "KI"),
    ]
    metal, nonmetal, comp_name, formula = rng.choice(pairs)

    prompt = (
        f"When a metal chemically reacts with a non-metal, a binary compound is produced.\n\n"
        f"Consider the reaction between **{metal}** and **{nonmetal}**:\n"
        f"1. Which element's name is written first in the compound's chemical name?\n"
        f"2. How is the ending of the non-metal's name modified?\n"
        f"3. State the correct scientific name and formula for this compound ({comp_name}, ${formula}$)."
    )
    sol = (
        f"**Step 1:** The **metal** is always written first ({metal}) [1 Mark: Metal first].\n\n"
        f"**Step 2:** The non-metal's suffix changes to **'-ide'** (e.g. {nonmetal.lower()} becomes {comp_name.split(' ')[1].lower()}) [1 Mark: -ide suffix].\n\n"
        f"**Step 3:** The scientific name is **{comp_name}** (formula: **${formula}$**) [1 Mark: Name and formula]."
    )
    return {
        "id": f"ns8_atom_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Metal is written first; non-metal suffix changes to '-ide'; {comp_name} (${formula}$)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_naming_binary_compounds_rules",
        "misconception_tags": ["binary_compound_naming_rules"],
        "hints": {
            "tier_1": "Metal comes first, then non-metal ending in -ide.",
            "tier_2": f"Oxygen becomes oxide, chlorine becomes chloride. {metal} + {nonmetal} = {comp_name}.",
            "tier_3": f"Metal first; '-ide' suffix; {comp_name} (${formula}$)."
        }
    }


def arch_39_naming_covalent_compounds_prefixes(rng: random.Random) -> Dict[str, Any]:
    prefixes = [
        ("CO", "Carbon monoxide", "mono- means 1 oxygen atom"),
        ("CO_2", "Carbon dioxide", "di- means 2 oxygen atoms"),
        ("SO_2", "Sulfur dioxide", "di- means 2 oxygen atoms"),
        ("SO_3", "Sulfur trioxide", "tri- means 3 oxygen atoms"),
        ("CCl_4", "Carbon tetrachloride", "tetra- means 4 chlorine atoms"),
    ]
    formula, name, meaning = rng.choice(prefixes)

    prompt = (
        f"When two non-metals bond together, Greek numerical prefixes are used to indicate the number of atoms present.\n\n"
        f"Consider the substance: **${formula}$** (**{name}**).\n\n"
        f"1. What Greek prefix is used in this name, and what number of atoms does it represent ({meaning})?\n"
        f"2. State the meanings of the prefixes: **mono-**, **di-**, and **tri-**.\n"
        f"3. Why is carbon monoxide ($CO$) so dangerous to inhale compared to carbon dioxide ($CO_2$)?"
    )
    sol = (
        f"**Step 1:** Prefix used: {meaning} [1 Mark: Prefix explanation].\n\n"
        f"**Step 2:** **mono- = 1**, **di- = 2**, **tri- = 3** [1 Mark: Prefix meanings].\n\n"
        f"**Step 3:** Carbon monoxide binds irreversibly to haemoglobin in red blood cells, starving the body of oxygen and causing suffocation/death [1 Mark: CO toxicity]."
    )
    return {
        "id": f"ns8_atom_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{meaning}; mono- = 1, di- = 2, tri- = 3; CO binds to haemoglobin preventing oxygen transport",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_naming_covalent_compounds_prefixes",
        "misconception_tags": ["covalent_naming_prefixes"],
        "hints": {
            "tier_1": "Mono = 1, Di = 2, Tri = 3.",
            "tier_2": f"In {name}, the prefix tells you how many atoms there are.",
            "tier_3": f"{meaning}; mono=1, di=2, tri=3; CO blocks oxygen in blood."
        }
    }


def arch_40_lattice_compounds_vs_covalent_molecules(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Table salt (Sodium chloride, $NaCl$)", "crystal lattice", "a giant three-dimensional repeating grid of alternating positive sodium ions and negative chloride ions"),
        ("Water ($H_2O$)", "discrete molecule", "separate, individual units consisting of one oxygen atom bonded to two hydrogen atoms"),
        ("Quartz (Silicon dioxide, $SiO_2$)", "crystal lattice", "a giant network of silicon and oxygen atoms bonded in a continuous 3D structure"),
    ]
    name, struct_type, desc = rng.choice(compounds)

    prompt = (
        f"Compounds can exist either as discrete individual molecules or as continuous repeating crystal lattices.\n\n"
        f"Consider **{name}** ({desc}).\n\n"
        f"1. Is {name.split(' ')[0]} structured as **discrete molecules** or as a **crystal lattice**?\n"
        f"2. Explain what is meant by a {struct_type}.\n"
        f"3. Why do crystal lattice compounds typically have much higher melting points than simple covalent molecular substances?"
    )
    sol = (
        f"**Step 1:** It is structured as a **{struct_type}** [1 Mark: Structure type].\n\n"
        f"**Step 2:** {desc} [1 Mark: Description].\n\n"
        f"**Step 3:** Lattices are held together by **strong continuous chemical bonds throughout the entire structure**, which require vast amounts of thermal energy to break apart, resulting in high melting points [1 Mark: High melting point explanation]."
    )
    return {
        "id": f"ns8_atom_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{struct_type}; {desc}; Lattice requires vast energy to break continuous strong bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_lattice_compounds_vs_covalent_molecules",
        "misconception_tags": ["lattice_vs_molecular_compounds"],
        "hints": {
            "tier_1": "Salt forms crystals (lattice); water forms individual separate molecules.",
            "tier_2": "Lattices have strong bonds in all directions, so they melt at very high temperatures.",
            "tier_3": f"{struct_type}; {desc}; high melting point due to strong 3D bonds."
        }
    }


# ==============================================================================
# CLUSTER 6: Mixtures vs Compounds & Chemical Decomposition (41 - 50)
# ==============================================================================

def arch_41_mixture_vs_compound_distinction_iron_sulfur(rng: random.Random) -> Dict[str, Any]:
    stages = [
        ("Stage 1: Grey iron filings and yellow sulfur powder are stirred together in a beaker", "Mixture", "Iron filings can be easily pulled out with a magnet; sulfur can be dissolved with carbon disulfide; no chemical bonding has occurred"),
        ("Stage 2: The mixture is strongly heated with a Bunsen burner until a red glow spreads and forms a black crusty solid (iron sulfide, $FeS$)", "Compound", "A magnet no longer attracts the iron because it is chemically bonded to sulfur in a new substance with entirely new properties"),
    ]
    stage_desc, classification, evidence = rng.choice(stages)

    prompt = (
        f"An educator demonstrates the famous iron and sulfur experiment:\n"
        f"**{stage_desc}**.\n\n"
        f"1. Classify the resulting material as a **mixture** or a **compound**.\n"
        f"2. Explain what happens when a bar magnet is brought near the material.\n"
        f"3. Explain the scientific reason behind the magnet's effect ({evidence.split(';')[0]})."
    )
    sol = (
        f"**Step 1:** It is classified as a **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** {evidence.split(';')[0]} [1 Mark: Magnetic observation].\n\n"
        f"**Step 3:** {evidence} [1 Mark: Scientific explanation]."
    )
    return {
        "id": f"ns8_atom_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{classification}; {evidence}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_mixture_vs_compound_distinction_iron_sulfur",
        "misconception_tags": ["iron_sulfur_mixture_vs_compound"],
        "hints": {
            "tier_1": "Before heating it's a mixture; after heating it's a compound.",
            "tier_2": "A magnet pulls iron out of a mixture, but cannot pull iron out of iron sulfide.",
            "tier_3": f"{classification}; {evidence}."
        }
    }


def arch_42_physical_vs_chemical_separation_methods(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("Saltwater solution (salt + water)", "Mixture", "Physical method (evaporation or simple distillation)", "physical forces between particles are overcome without breaking chemical bonds"),
        ("Pure liquid water ($H_2O$)", "Compound", "Chemical method (electrolysis)", "requires chemical energy to break strong covalent bonds between hydrogen and oxygen"),
        ("Sand and iron filings", "Mixture", "Physical method (magnetic separation)", "iron retains its individual magnetic properties"),
        ("Copper carbonate ($CuCO_3$)", "Compound", "Chemical method (thermal decomposition / strong heating)", "heat breaks chemical bonds to form copper oxide and carbon dioxide"),
    ]
    sub, cat, method, reason = rng.choice(substances)

    prompt = (
        f"Separating matter depends fundamentally on whether it is a mixture or a compound.\n\n"
        f"Consider: **{sub}**.\n\n"
        f"1. Is this substance a **mixture** or a **compound**?\n"
        f"2. Can it be separated/broken down by a **physical method** or does it require a **chemical method**? (Name an appropriate method: {method.split(' (')[0]}).\n"
        f"3. Explain why physical methods are powerless to break down chemical compounds."
    )
    sol = (
        f"**Step 1:** {sub} is a **{cat}** [1 Mark: Classification].\n\n"
        f"**Step 2:** It requires a **{method}** [1 Mark: Method].\n\n"
        f"**Step 3:** Physical methods only overcome weak intermolecular forces; they do not possess enough energy to break the **strong chemical bonds** holding atoms together in compounds [1 Mark: Chemical bond explanation]."
    )
    return {
        "id": f"ns8_atom_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cat}; {method}; Physical methods cannot break strong chemical bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_physical_vs_chemical_separation_methods",
        "misconception_tags": ["physical_vs_chemical_separation"],
        "hints": {
            "tier_1": "Mixtures are separated physically; compounds require chemical breakdown.",
            "tier_2": f"{sub} is a {cat}, so it needs {method}.",
            "tier_3": f"{cat}; {method}; physical methods cannot break chemical bonds."
        }
    }


def arch_43_decomposition_reactions_definition(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("thermal decomposition", "using intense heat energy to break down a compound into simpler substances"),
        ("electrolytic decomposition (electrolysis)", "using electrical energy passed through a solution or melt to break chemical bonds"),
    ]
    t_name, t_desc = rng.choice(types)

    prompt = (
        f"Compounds can be broken down into simpler substances through chemical decomposition.\n\n"
        f"1. Define what a **chemical decomposition reaction** is.\n"
        f"2. Explain what is meant by **{t_name}** ({t_desc}).\n"
        f"3. Give one everyday or industrial example of where decomposition reactions are used."
    )
    sol = (
        f"**Step 1:** A decomposition reaction is a chemical reaction in which a **single compound breaks down into two or more simpler substances (elements or simpler compounds)** [1 Mark: Definition].\n\n"
        f"**Step 2:** {t_name.capitalize()} is the process of {t_desc} [1 Mark: Process explanation].\n\n"
        f"**Step 3:** Examples include: extracting metals from mineral ores by smelting/electrolysis, producing oxygen and hydrogen from water, or decomposition of baking powder during baking [1 Mark: Real-world application]."
    )
    return {
        "id": f"ns8_atom_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Single compound breaks down into two or more simpler substances; {t_name} is {t_desc}; e.g. metal extraction or electrolysis of water",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_decomposition_reactions_definition",
        "misconception_tags": ["decomposition_reaction_definition"],
        "hints": {
            "tier_1": "Decompose means to break down.",
            "tier_2": f"{t_name} breaks down compounds using heat or electricity.",
            "tier_3": f"Compound splits into simpler parts; {t_name} is {t_desc}; e.g. water electrolysis."
        }
    }


def arch_44_electrolysis_of_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a Hoffmann voltameter, an electric current is passed through acidified water ($H_2O$) to break it down.\n\n"
        f"1. What are the two gases produced during the electrolysis of water?\n"
        f"2. In what **volume ratio** are these two gases collected (explain why based on the chemical formula $H_2O$)?\n"
        f"3. Write the balanced word equation for this decomposition reaction."
    )
    sol = (
        f"**Step 1:** The two gases produced are **Hydrogen gas ($H_2$)** and **Oxygen gas ($O_2$)** [1 Mark: Gases].\n\n"
        f"**Step 2:** They are collected in a **$2 : 1$ volume ratio** ($2$ parts Hydrogen to $1$ part Oxygen) because water has two hydrogen atoms for every one oxygen atom ($2H_2O \\rightarrow 2H_2 + O_2$) [1 Mark: Ratio and explanation].\n\n"
        f"**Step 3:** Word equation: **Water $\\rightarrow$ Hydrogen + Oxygen** [1 Mark: Word equation]."
    )
    return {
        "id": f"ns8_atom_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Hydrogen and Oxygen; 2:1 ratio because formula is H2O; Water -> Hydrogen + Oxygen",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_electrolysis_of_water",
        "misconception_tags": ["electrolysis_of_water_ratio"],
        "hints": {
            "tier_1": "Water is H2O. What two gases come out?",
            "tier_2": "Hydrogen has twice the volume of oxygen (2:1 ratio).",
            "tier_3": "Hydrogen and Oxygen; 2:1 volume ratio; Water -> Hydrogen + Oxygen."
        }
    }


def arch_45_electrolysis_of_copper_chloride(rng: random.Random) -> Dict[str, Any]:
    voltage = rng.choice([6, 9, 12])
    cu_width = rng.choice([5, 7, 9])
    bubble_y = rng.choice([85, 95, 105])

    svg = (
        f'<svg viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="320" height="200" rx="6" fill="#f8fafc"/>'
        f'<text x="170" y="30" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Electrolysis of CuCl₂ ({voltage}V DC)</text>'
        # Beaker & solution
        f'<rect x="70" y="60" width="200" height="130" rx="4" fill="#67e8f9" opacity="0.6" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="170" y="180" font-family="sans-serif" font-size="10" fill="#0369a1" text-anchor="middle">Blue CuCl₂ solution</text>'
        # Anode (positive)
        f'<rect x="100" y="45" width="20" height="110" fill="#334155"/>'
        f'<text x="110" y="40" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">(+)</text>'
        # Chlorine bubbles
        f'<circle cx="95" cy="{bubble_y}" r="4" fill="#bef264" stroke="#65a30d"/>'
        f'<circle cx="125" cy="{bubble_y + 20}" r="5" fill="#bef264" stroke="#65a30d"/>'
        f'<circle cx="100" cy="{bubble_y + 40}" r="4" fill="#bef264" stroke="#65a30d"/>'
        # Cathode (negative)
        f'<rect x="220" y="45" width="20" height="110" fill="#334155"/>'
        f'<text x="230" y="40" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">(-)</text>'
        # Copper coating
        f'<rect x="{220 - cu_width}" y="100" width="{cu_width}" height="55" fill="#ea580c"/>'
        f'<rect x="240" y="100" width="{cu_width}" height="55" fill="#ea580c"/>'
        f'<text x="230" y="170" font-family="sans-serif" font-size="9" fill="#9a3412" text-anchor="middle">Copper coating</text>'
        f'</svg>'
    )

    prompt = (
        f"An electric current is passed through a blue solution of **copper(II) chloride ($CuCl_2$)** using two carbon (graphite) electrodes.\n\n"
        f"1. What is observed at the negative electrode (cathode)? Name the metal deposited.\n"
        f"2. What is observed at the positive electrode (anode)? Name the gas produced and describe its smell.\n"
        f"3. Write the word equation for this decomposition reaction."
    )
    sol = (
        f"**Step 1:** A **reddish-brown solid coating** forms on the negative cathode: **copper metal ($Cu$)** [1 Mark: Cathode observation].\n\n"
        f"**Step 2:** Bubbles of gas form at the positive anode: **chlorine gas ($Cl_2$)**, which has a pungent, choking swimming pool bleach smell [1 Mark: Anode observation].\n\n"
        f"**Step 3:** Word equation: **Copper chloride $\\rightarrow$ Copper + Chlorine** [1 Mark: Word equation]."
    )
    return {
        "id": f"ns8_atom_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Reddish-brown copper metal on cathode; Bubbles of pungent chlorine gas at anode; Copper chloride -> Copper + Chlorine",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_electrolysis_of_copper_chloride",
        "misconception_tags": ["electrolysis_copper_chloride"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Copper coats the negative electrode; chlorine gas bubbles off the positive electrode.",
            "tier_2": "Copper is reddish-brown; chlorine smells like swimming pool bleach.",
            "tier_3": "Copper deposits at cathode; chlorine gas at anode; Copper chloride -> Copper + Chlorine."
        }
    }


def arch_46_thermal_decomposition_copper_carbonate(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A green powder of **copper carbonate ($CuCO_3$)** is placed in a test tube and heated strongly over a Bunsen burner flame.\n\n"
        f"1. What color change is observed in the test tube solid as heating progresses?\n"
        f"2. Name the black solid product left in the test tube and the invisible gas released.\n"
        f"3. How can you test the gas released to confirm its identity?"
    )
    sol = (
        f"**Step 1:** The solid changes from **green to black** [1 Mark: Color change].\n\n"
        f"**Step 2:** The black solid is **copper(II) oxide ($CuO$)** and the gas released is **carbon dioxide ($CO_2$)** [1 Mark: Products].\n\n"
        f"**Step 3:** Bubble the gas through **clear limewater**: the limewater turns **milky/cloudy white** in the presence of carbon dioxide [1 Mark: Gas test]."
    )
    return {
        "id": f"ns8_atom_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Green powder turns black; Black copper oxide and carbon dioxide gas; Bubble through clear limewater which turns milky",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_thermal_decomposition_copper_carbonate",
        "misconception_tags": ["thermal_decomposition_copper_carbonate"],
        "hints": {
            "tier_1": "Green copper carbonate turns black when heated.",
            "tier_2": "Products are copper oxide and CO2. Test CO2 with limewater.",
            "tier_3": "Green turns black (copper oxide); CO2 gas turns limewater milky."
        }
    }


def arch_47_thermal_decomposition_mercury_oxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In historical experiments (such as those by Joseph Priestley in 1774), red **mercury(II) oxide ($HgO$)** powder was heated strongly.\n\n"
        f"1. Describe the dramatic visual observation that occurs as red mercury oxide decomposes.\n"
        f"2. Name the two elemental products formed (one metal and one non-metal gas).\n"
        f"3. How is the gas product confirmed using a wooden splint?"
    )
    sol = (
        f"**Step 1:** The red powder disappears, forming **silvery liquid droplets (droplets of mercury)** on the cool sides of the glass tube [1 Mark: Visual observation].\n\n"
        f"**Step 2:** The metal is **mercury ($Hg$)** and the non-metal gas is **oxygen ($O_2$)** [1 Mark: Products].\n\n"
        f"**Step 3:** Place a **glowing wooden splint** into the mouth of the tube: the splint **relights (bursts into flame)**, proving oxygen gas is present [1 Mark: Oxygen test]."
    )
    return {
        "id": f"ns8_atom_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Red powder forms silvery liquid droplets; Liquid mercury metal and oxygen gas; Relights a glowing splint",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_thermal_decomposition_mercury_oxide",
        "misconception_tags": ["mercury_oxide_decomposition"],
        "hints": {
            "tier_1": "Red powder breaks down into shiny liquid mercury and oxygen gas.",
            "tier_2": "Oxygen makes things burn brighter.",
            "tier_3": "Silvery liquid mercury and oxygen gas; oxygen relights a glowing splint."
        }
    }


def arch_48_testing_gases_from_decomposition(rng: random.Random) -> Dict[str, Any]:
    tests = [
        ("Oxygen ($O_2$)", "insert a glowing wooden splint into the gas", "the glowing splint relights (bursts into flame)"),
        ("Hydrogen ($H_2$)", "bring a burning wooden splint near the mouth of the test tube", "the gas burns with a distinctive 'pop' sound"),
        ("Carbon dioxide ($CO_2$)", "bubble the gas through clear limewater", "the limewater turns milky / cloudy white due to calcium carbonate precipitate"),
    ]
    gas, method, positive_result = rng.choice(tests)

    prompt = (
        f"Identifying the gases produced during decomposition reactions is an essential laboratory skill.\n\n"
        f"Consider the test for: **{gas}**.\n\n"
        f"1. Describe the exact experimental procedure used to test for {gas.split(' ')[0]} ({method}).\n"
        f"2. State the positive result that confirms the presence of {gas.split(' ')[0]}.\n"
        f"3. What distinguishes the test for hydrogen from the test for oxygen?"
    )
    sol = (
        f"**Step 1:** Procedure: {method} [1 Mark: Test procedure].\n\n"
        f"**Step 2:** Positive result: {positive_result} [1 Mark: Positive result].\n\n"
        f"**Step 3:** Hydrogen is tested with a **burning flame** (giving a 'pop'), whereas oxygen is tested with a **glowing (unlit) ember** which relights [1 Mark: Hydrogen vs Oxygen test distinction]."
    )
    return {
        "id": f"ns8_atom_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{method}; {positive_result}; Hydrogen = burning splint 'pop', Oxygen = glowing splint relights",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_testing_gases_from_decomposition",
        "misconception_tags": ["gas_identification_tests"],
        "hints": {
            "tier_1": "Oxygen relights glowing splint; hydrogen pops with burning splint; CO2 turns limewater milky.",
            "tier_2": f"For {gas}: {method} -> {positive_result}.",
            "tier_3": f"{method}; {positive_result}; burning pop vs glowing relight."
        }
    }


def arch_49_scientific_inquiry_identifying_unknown_substance(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Substance X",
            "Yellow solid powder",
            "Melts into a brown liquid at 115 °C without releasing gas; cannot be broken down by heating or electrolysis",
            "Insoluble in water, does not conduct electricity",
            "Element (Sulfur)",
            "cannot be decomposed into simpler substances by chemical means"
        ),
        (
            "Substance Y",
            "Blue crystalline solid",
            "When heated, releases steam and leaves white powder; dissolving in water and applying electric current deposits brown copper and bubbles chlorine gas",
            "Forms an electrical conducting solution",
            "Compound (Hydrated copper chloride)",
            "can be broken down chemically into simpler elements (copper and chlorine)"
        ),
        (
            "Substance Z",
            "Grey and yellow mixed powder",
            "A magnet instantly extracts all the grey particles; the remaining yellow powder is left behind unchanged",
            "No heating was required for separation",
            "Mixture (Iron filings and Sulfur)",
            "components can be separated by a simple physical method (magnetism) and are not chemically bonded"
        ),
    ]
    name, app, heat_test, other_test, classification, reason = rng.choice(scenarios)

    prompt = (
        f"A laboratory researcher conducts investigations on an unknown sample labelled **{name}**:\n\n"
        f"- **Visual Appearance:** {app}\n"
        f"- **Heating & Decomposition Test:** {heat_test}\n"
        f"- **Physical / Electrical Behavior:** {other_test}\n\n"
        f"1. Classify {name} as an **element**, **compound**, or **mixture**.\n"
        f"2. State two pieces of evidence from the test results justifying your classification.\n"
        f"3. Explain the fundamental difference between {name} and the other two categories."
    )
    sol = (
        f"**Step 1:** {name} is classified as a **{classification.split(' (')[0]}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Evidence: {heat_test}; {other_test} [1 Mark: Supporting evidence].\n\n"
        f"**Step 3:** Reason: It is a {classification.split(' (')[0]} because it {reason} [1 Mark: Scientific justification]."
    )
    return {
        "id": f"ns8_atom_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{classification.split(' (')[0]}; Evidence: {heat_test}; Reason: {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_scientific_inquiry_identifying_unknown_substance",
        "misconception_tags": ["element_compound_mixture_inquiry"],
        "hints": {
            "tier_1": "Can it be separated physically (mixture)? Can it be broken down chemically (compound)? Or neither (element)?",
            "tier_2": f"Look at the decomposition results: {heat_test}.",
            "tier_3": f"{classification.split(' (')[0]}; {reason}."
        }
    }


def arch_50_atoms_compounds_master_synthesis_challenge(rng: random.Random) -> Dict[str, Any]:
    elem = rng.choice([
        ("Magnesium", "Mg", 12, 24, "metal", "MgO"),
        ("Sodium", "Na", 11, 23, "alkali metal", "NaCl"),
        ("Calcium", "Ca", 20, 40, "metal", "CaO"),
    ])
    name, sym, z, a, cat, oxide_f = elem
    neutrons = a - z

    prompt = (
        f"Complete the comprehensive Grade 8 Matter and Materials master synthesis for **{name} ({sym})**:\n\n"
        f"1. **Atomic Structure:** An atom of {name} has an atomic number $Z = {z}$ and mass number $A = {a}$. State the number of protons, neutrons, and electrons in a neutral atom.\n"
        f"2. **Electron Arrangement:** Write the electron arrangement in energy shells (following the 2, 8, 8 rule).\n"
        f"3. **Element vs Compound:** {name} reacts with oxygen gas ($O_2$) to form **{name} oxide (${oxide_f}$)**. Explain whether $O_2$ is a molecule of an element or a compound, and whether ${oxide_f}$ is an element or a compound.\n"
        f"4. **Decomposition:** Can ${oxide_f}$ be separated back into its elements using a simple physical method like filtration? Explain why or why not."
    )
    sol = (
        f"**Step 1:** Protons = **{z}**, Neutrons = ${a} - {z} = \\mathbf{{{neutrons}}}$, Electrons = **{z}** [2 Marks: Subatomic counts].\n\n"
        f"**Step 2:** Electron arrangement: **{z} electrons $\\rightarrow$ {[2, min(8, z-2), max(0, z-10)] if z > 10 else [2, z-2]}** [1 Mark: Electron arrangement].\n\n"
        f"**Step 3:** $O_2$ is a **molecule of an element** (contains only oxygen atoms bonded together); ${oxide_f}$ is a **compound** (contains {name} and Oxygen chemically bonded) [2 Marks: Element vs Compound].\n\n"
        f"**Step 4:** **No**, ${oxide_f}$ cannot be separated by physical methods because its atoms are held together by strong chemical bonds that can only be broken by chemical decomposition [1 Mark: Chemical decomposition explanation]."
    )
    return {
        "id": f"ns8_atom_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Protons: {z}, Neutrons: {neutrons}, Electrons: {z}; O2 is element molecule, {oxide_f} is compound; No, physical methods cannot break chemical bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 6,
        "term": 2,
        "subskill": "50_atoms_compounds_master_synthesis_challenge",
        "misconception_tags": ["atoms_and_compounds_master_synthesis"],
        "hints": {
            "tier_1": f"Z = {z} protons and electrons. Neutrons = {a} - {z} = {neutrons}.",
            "tier_2": "O2 has one element (element molecule); oxide has two elements (compound).",
            "tier_3": f"{z}p, {neutrons}n, {z}e; O2 is element, {oxide_f} is compound; cannot separate physically."
        }
    }
