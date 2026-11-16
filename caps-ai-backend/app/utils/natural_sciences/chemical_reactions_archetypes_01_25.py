"""Physical Sciences Grade 10 Term 3 — Reactions in Aqueous Solution.
Archetypes 01 to 25: Polarity of water, hydration, dissociation, electrolytes,
electrical conductivity apparatus, ion concentrations, precipitation rules,
spectator ions, full/net ionic equations, and qualitative tests for halides and sulphates.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import fmt_sa, make_science_question

TOPIC = "natural_sciences_chemical_reactions"
LO = "ps10_reactions_in_aqueous_solution"


# --------------------------------------------------------------------------- #
# Helper: Seed-varied Conductivity Circuit Inline SVG
# --------------------------------------------------------------------------- #
def _generate_conductivity_circuit_svg(
    rng: random.Random,
    cell_volts: int,
    ammeter_reading: float,
    bulb_lit: bool,
    solution_label: str,
    ions_text: str,
) -> str:
    seed_offset = rng.randint(0, 10)
    wire_color = "#374151"
    liquid_color = "#e0f2fe" if bulb_lit else "#f1f5f9"
    bulb_fill = "#fef08a" if bulb_lit else "#cbd5e1"
    bulb_glow = (
        f'<circle cx="200" cy="50" r="22" fill="#fef08a" opacity="0.6"/>'
        if bulb_lit
        else ""
    )
    amm_str = f"{ammeter_reading:.2f}".replace(".", ",")

    return (
        f'<svg viewBox="0 0 420 300" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" '
        f'style="background-color: #ffffff; font-family: sans-serif;">'
        f'<rect x="10" y="10" width="400" height="280" rx="8" fill="#fafafa" stroke="#e2e8f0" stroke-width="1.5"/>'
        # Battery / cells at top left
        f'<line x1="60" y1="50" x2="110" y2="50" stroke="{wire_color}" stroke-width="2.5"/>'
        f'<line x1="110" y1="36" x2="110" y2="64" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="118" y1="42" x2="118" y2="58" stroke="#1e293b" stroke-width="1.5"/>'
        f'<line x1="126" y1="36" x2="126" y2="64" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="134" y1="42" x2="134" y2="58" stroke="#1e293b" stroke-width="1.5"/>'
        f'<text x="122" y="28" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{cell_volts} V DC</text>'
        # Wire to light bulb
        f'<line x1="134" y1="50" x2="185" y2="50" stroke="{wire_color}" stroke-width="2.5"/>'
        f'{bulb_glow}'
        f'<circle cx="200" cy="50" r="14" fill="{bulb_fill}" stroke="#475569" stroke-width="2"/>'
        f'<path d="M 194 50 Q 200 42 206 50" fill="none" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="200" y="24" font-size="10" text-anchor="middle" fill="#475569">Indicator bulb</text>'
        # Wire to ammeter
        f'<line x1="214" y1="50" x2="280" y2="50" stroke="{wire_color}" stroke-width="2.5"/>'
        f'<circle cx="300" cy="50" r="18" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="300" y="55" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">A</text>'
        f'<text x="300" y="82" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">{amm_str} A</text>'
        # Wire going down to right electrode
        f'<line x1="318" y1="50" x2="350" y2="50" stroke="{wire_color}" stroke-width="2.5"/>'
        f'<line x1="350" y1="50" x2="350" y2="150" stroke="{wire_color}" stroke-width="2.5"/>'
        f'<line x1="350" y1="150" x2="270" y2="150" stroke="{wire_color}" stroke-width="2.5"/>'
        # Wire from battery going down to left electrode
        f'<line x1="60" y1="50" x2="60" y2="150" stroke="{wire_color}" stroke-width="2.5"/>'
        f'<line x1="60" y1="150" x2="150" y2="150" stroke="{wire_color}" stroke-width="2.5"/>'
        # Beaker container
        f'<rect x="110" y="140" width="200" height="130" rx="4" fill="none" stroke="#64748b" stroke-width="2.5"/>'
        f'<rect x="112" y="170" width="196" height="98" fill="{liquid_color}" opacity="0.8"/>'
        # Electrodes (carbon rods)
        f'<rect x="145" y="125" width="14" height="95" rx="2" fill="#334155" stroke="#0f172a" stroke-width="1"/>'
        f'<rect x="261" y="125" width="14" height="95" rx="2" fill="#334155" stroke="#0f172a" stroke-width="1"/>'
        f'<text x="152" y="118" font-size="9" text-anchor="middle" fill="#475569">Carbon rod</text>'
        f'<text x="268" y="118" font-size="9" text-anchor="middle" fill="#475569">Carbon rod</text>'
        # Labels for solution and ions
        f'<text x="210" y="210" font-size="11" font-weight="bold" text-anchor="middle" fill="#0369a1">{solution_label}</text>'
        f'<text x="210" y="230" font-size="10" text-anchor="middle" fill="#64748b">{ions_text}</text>'
        f'</svg>'
    )


# --------------------------------------------------------------------------- #
# Subskill 01: Water Dipole and Molecular Polarity
# --------------------------------------------------------------------------- #
def arch_01_water_dipole_molecular_polarity(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    electronegativity_diff = round(rng.uniform(1.2, 1.4), 2)
    o_en = 3.44
    h_en = 2.20
    angle = rng.choice([104.5, 105.0])

    prompt = (
        f"Water ($\\text{{H}}_2\\text{{O}}$) is a vital polar solvent in chemical and biological systems.\n\n"
        f"1. State the shape of a water molecule and give the approximate $\\text{{H-O-H}}$ bond angle (approximately **{fmt_sa(angle)}^\\circ**).\n"
        f"2. Explain why the water molecule has a permanent dipole moment by referring to the electronegativity values of oxygen ({fmt_sa(o_en)}) and hydrogen ({fmt_sa(h_en)}).\n"
        f"3. Indicate which atom carries the partial negative charge ($\\delta^-$) and which carry the partial positive charge ($\\delta^+$)."
    )

    ans_latex = (
        rf"\text{{Shape: Bent (angular), Bond angle: }} \approx {fmt_sa(angle)}^\circ; "
        rf"\quad \Delta\text{{EN}} = {fmt_sa(o_en - h_en)}; \quad \text{{O carries }} \delta^-, \text{{ H carries }} \delta^+"
    )

    sample_answer = (
        f"1. Shape: Bent (or angular / non-linear). Bond angle is approximately {fmt_sa(angle)}°.\n"
        f"2. Oxygen has an electronegativity of {fmt_sa(o_en)}, which is significantly higher than that of hydrogen ({fmt_sa(h_en)}). "
        f"The shared electron pairs in the polar covalent O-H bonds are drawn closer to the oxygen atom. "
        f"Because the molecule is bent (asymmetrical), the bond dipoles do not cancel each other out, resulting in a net molecular dipole.\n"
        f"3. The oxygen atom carries the partial negative charge (δ⁻), while the two hydrogen atoms carry partial positive charges (δ⁺)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct shape stated (bent / angular)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reference to electronegativity difference pulling electron density towards oxygen", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Asymmetrical shape prevents cancellation of bond dipoles", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Correct assignment of δ⁻ to O and δ⁺ to H atoms", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Consider the electron arrangement around oxygen: two bonded pairs and two lone pairs.",
        "concept": "A polar molecule requires both polar covalent bonds (due to an electronegativity difference) and an asymmetrical molecular geometry.",
        "breakdown": f"Oxygen is more electronegative than hydrogen ({fmt_sa(o_en)} vs {fmt_sa(h_en)}), making oxygen δ⁻ and hydrogens δ⁺. Because water is bent, the dipoles reinforce one another.",
    }

    return make_science_question(
        prefix="ps10_aq_dipole",
        topic=TOPIC,
        subskill="01_water_dipole_molecular_polarity",
        learning_objective_id=f"{LO}_dipole",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_bond_polarity_with_molecular_polarity", "assumed_linear_water_molecule"],
        keywords=["water", "dipole", "polar", "electronegativity", "partial charge", "bent"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 02: Hydration Mechanism of an Ionic Lattice
# --------------------------------------------------------------------------- #
def arch_02_hydration_mechanism_ionic_lattice(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt_name, cation_sym, anion_sym = rng.choice([
        ("sodium chloride", r"\text{Na}^+", r"\text{Cl}^-"),
        ("potassium bromide", r"\text{K}^+", r"\text{Br}^-"),
        ("lithium fluoride", r"\text{Li}^+", r"\text{F}^-"),
        ("potassium chloride", r"\text{K}^+", r"\text{Cl}^-"),
    ])

    prompt = (
        f"When crystals of **{salt_name}** are added to water, dissolution occurs via hydration.\n\n"
        f"1. Define the term **hydration** in the context of aqueous solutions.\n"
        f"2. Describe how the polar water molecules orient themselves around the ${cation_sym}$ cations.\n"
        f"3. Describe how the polar water molecules orient themselves around the ${anion_sym}$ anions.\n"
        f"4. State the name of the attractive force that operates between the ions and the polar water molecules."
    )

    ans_latex = (
        rf"\text{{Hydration: Ions become surrounded by water molecules; }}"
        rf"\quad \text{{Oxygen (}}\delta^-\text{{) faces }}{cation_sym}; \quad \text{{Hydrogen (}}\delta^+\text{{) faces }}{anion_sym}; "
        rf"\quad \text{{Ion-dipole force}}"
    )

    sample_answer = (
        f"1. Hydration is the process in which solute ions become surrounded by water molecules.\n"
        f"2. Water molecules orient with their partially negative oxygen atoms (δ⁻) facing towards the positive {salt_name.split()[0]} cations ({cation_sym}).\n"
        f"3. Water molecules orient with their partially positive hydrogen atoms (δ⁺) facing towards the negative {salt_name.split()[1]} anions ({anion_sym}).\n"
        f"4. Ion-dipole forces (or ion-dipole attractions)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of hydration: ions surrounded by water molecules", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct orientation around {cation_sym}: delta-negative oxygen pole faces cation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct orientation around {anion_sym}: delta-positive hydrogen poles face anion", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Identification of ion-dipole forces", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Opposite charges attract: which pole of the water molecule carries a negative charge, and which carries a positive charge?",
        "concept": "Hydration involves ion-dipole interactions where polar water molecules cluster around ions according to electrostatic attractions.",
        "breakdown": f"Positive {cation_sym} attracts the δ⁻ oxygen end of water. Negative {anion_sym} attracts the δ⁺ hydrogen ends of water.",
    }

    return make_science_question(
        prefix="ps10_aq_hydration",
        topic=TOPIC,
        subskill="02_hydration_mechanism_ionic_lattice",
        learning_objective_id=f"{LO}_hydration",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["inverted_water_pole_orientation", "confused_hydration_with_hydrolysis"],
        keywords=["hydration", "ionic lattice", "ion-dipole", "cation", "anion", "water dipole"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 03: Dissociation Equations of 1:1 Salts
# --------------------------------------------------------------------------- #
def arch_03_dissociation_single_charge_salts(rng: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    salts = [
        {"name": "Sodium chloride", "formula": r"\text{NaCl}", "cation": r"\text{Na}^+", "anion": r"\text{Cl}^-"},
        {"name": "Potassium nitrate", "formula": r"\text{KNO}_3", "cation": r"\text{K}^+", "anion": r"\text{NO}_3^-"},
        {"name": "Lithium bromide", "formula": r"\text{LiBr}", "cation": r"\text{Li}^+", "anion": r"\text{Br}^-"},
        {"name": "Silver nitrate", "formula": r"\text{AgNO}_3", "cation": r"\text{Ag}^+", "anion": r"\text{NO}_3^-"},
    ]
    s = rng.choice(salts)

    prompt = (
        f"Solid **{s['name']}** (${s['formula']}$) dissolves in pure water.\n\n"
        f"1. Write down a balanced chemical equation for the dissociation of ${s['formula']}$ in water. "
        f"Include all state symbols (`(s)` and `(aq)`).\n"
        f"2. What is the ratio of cations to anions in the resulting solution?"
    )

    eq = rf"{s['formula']}\text{{(s)}} \xrightarrow{{\text{{H}}_2\text{{O}}}} {s['cation']}\text{{(aq)}} + {s['anion']}\text{{(aq)}}"
    ans_latex = rf"{eq}, \quad \text{{Ratio: }} 1 : 1"

    sample_answer = (
        f"1. Dissociation equation:\n"
        f"   $${eq}$$\n"
        f"2. The ratio of cations ({s['cation']}) to anions ({s['anion']}) is 1 : 1."
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct reactant formula and state symbol: {s['formula']}(s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct product ions with charges and (aq) state symbols: {s['cation']}(aq) + {s['anion']}(aq)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct 1 : 1 ion ratio stated", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "missing_state_symbols", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "In a dissociation reaction, the solid ionic lattice splits into aqueous ions.",
        "concept": "Dissociation does not create new chemical substances; it merely frees ions from their solid crystal lattice into aqueous solution.",
        "breakdown": f"Solid {s['formula']}(s) dissociates into equal numbers of {s['cation']}(aq) and {s['anion']}(aq).",
    }

    return make_science_question(
        prefix="ps10_aq_diss1",
        topic=TOPIC,
        subskill="03_dissociation_single_charge_salts",
        learning_objective_id=f"{LO}_dissociation_1_1",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_state_symbols", "forgot_ion_charges"],
        keywords=["dissociation", "1:1 salt", "state symbols", "ions", "aqueous"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="elementary_dissociation_equations",
        difficulty=difficulty,
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Subskill 04: Dissociation of Multivalent Cation Salts
# --------------------------------------------------------------------------- #
def arch_04_dissociation_multivalent_cation_salts(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salts = [
        {"name": "Calcium chloride", "formula": r"\text{CaCl}_2", "cat": r"\text{Ca}^{2+}", "cat_coef": 1, "an": r"\text{Cl}^-", "an_coef": 2},
        {"name": "Magnesium nitrate", "formula": r"\text{Mg(NO}_3)_2", "cat": r"\text{Mg}^{2+}", "cat_coef": 1, "an": r"\text{NO}_3^-", "an_coef": 2},
        {"name": "Iron(III) chloride", "formula": r"\text{FeCl}_3", "cat": r"\text{Fe}^{3+}", "cat_coef": 1, "an": r"\text{Cl}^-", "an_coef": 3},
        {"name": "Copper(II) chloride", "formula": r"\text{CuCl}_2", "cat": r"\text{Cu}^{2+}", "cat_coef": 1, "an": r"\text{Cl}^-", "an_coef": 2},
    ]
    s = rng.choice(salts)

    prompt = (
        f"Solid **{s['name']}** (${s['formula']}$) is dissolved in water to make an aqueous solution.\n\n"
        f"1. Write down the balanced dissociation equation for ${s['formula']}$ in water. Include state symbols.\n"
        f"2. For every $1\\text{{ mol}}$ of ${s['formula']}$ that completely dissolves, how many total moles of ions are produced in solution?"
    )

    total_ions = s["cat_coef"] + s["an_coef"]
    cat_part = s["cat"] if s["cat_coef"] == 1 else f"{s['cat_coef']}{s['cat']}"
    an_part = s["an"] if s["an_coef"] == 1 else f"{s['an_coef']}{s['an']}"
    eq = rf"{s['formula']}\text{{(s)}} \to {cat_part}\text{{(aq)}} + {an_part}\text{{(aq)}}"
    ans_latex = rf"{eq}, \quad \text{{Total moles of ions: }} {total_ions}\text{{ mol}}"

    sample_answer = (
        f"1. Balanced dissociation equation:\n"
        f"   $${eq}$$\n"
        f"2. $1\\text{{ mol}}$ of ${s['formula']}$ yields {s['cat_coef']}\\text{{ mol of }}{s['cat']} and {s['an_coef']}\\text{{ mol of }}{s['an']}.\n"
        f"   Total = {total_ions}\\text{{ moles of ions}}."
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct reactant and state symbol: {s['formula']}(s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correctly balanced ions with charges: {cat_part}(aq) + {an_part}(aq)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct total moles of ions stated ({total_ions} mol)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_subscript_as_polyatomic_ion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The subscript indicating the number of anions becomes the stoichiometric coefficient in front of the aqueous ion.",
        "concept": "For example, in CaCl₂, the subscript 2 means two individual Cl⁻ ions are released: Ca²⁺ + 2Cl⁻.",
        "breakdown": f"{s['formula']}(s) breaks into 1 {s['cat']}(aq) and {s['an_coef']} {s['an']}(aq), giving a total of {total_ions} moles of ions.",
    }

    return make_science_question(
        prefix="ps10_aq_diss_multi",
        topic=TOPIC,
        subskill="04_dissociation_multivalent_cation_salts",
        learning_objective_id=f"{LO}_multivalent_dissociation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["wrote_cl2_instead_of_2cl", "omitted_cation_charge"],
        keywords=["dissociation", "multivalent", "coefficients", "aqueous ions", "calcium chloride"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="elementary_dissociation_equations",
        difficulty=difficulty,
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Subskill 05: Dissociation of Polyatomic Anion Salts
# --------------------------------------------------------------------------- #
def arch_05_dissociation_polyatomic_anion_salts(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salts = [
        {"name": "Potassium sulphate", "formula": r"\text{K}_2\text{SO}_4", "eq": r"\text{K}_2\text{SO}_4\text{(s)} \to 2\text{K}^+\text{(aq)} + \text{SO}_4^{2-}\text{(aq)}", "total": 3},
        {"name": "Sodium carbonate", "formula": r"\text{Na}_2\text{CO}_3", "eq": r"\text{Na}_2\text{CO}_3\text{(s)} \to 2\text{Na}^+\text{(aq)} + \text{CO}_3^{2-}\text{(aq)}", "total": 3},
        {"name": "Ammonium carbonate", "formula": r"(\text{NH}_4)_2\text{CO}_3", "eq": r"(\text{NH}_4)_2\text{CO}_3\text{(s)} \to 2\text{NH}_4^+\text{(aq)} + \text{CO}_3^{2-}\text{(aq)}", "total": 3},
        {"name": "Aluminium sulphate", "formula": r"\text{Al}_2(\text{SO}_4)_3", "eq": r"\text{Al}_2(\text{SO}_4)_3\text{(s)} \to 2\text{Al}^{3+}\text{(aq)} + 3\text{SO}_4^{2-}\text{(aq)}", "total": 5},
    ]
    s = rng.choice(salts)

    prompt = (
        f"Consider the dissolution of solid **{s['name']}** (${s['formula']}$) in water.\n\n"
        f"1. Write down the balanced chemical equation for the dissociation of ${s['formula']}$ in water. Include state symbols.\n"
        f"2. Explain why the polyatomic ion does NOT break up into individual single atoms during dissociation."
    )

    ans_latex = rf"{s['eq']}; \quad \text{{Strong internal covalent bonds in polyatomic ion remain intact}}"

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $${s['eq']}$$\n"
        f"2. The atoms within the polyatomic ion are held together by strong covalent bonds. "
        f"Water molecules have enough energy to overcome the ionic lattice attractions between cations and anions, "
        f"but cannot break the strong covalent bonds within the polyatomic ion."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct reactant and state symbol: {s['formula']}(s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct product ions with charges and balancing coefficients", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explanation: strong internal covalent bonds hold polyatomic ion together", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "split_polyatomic_ion_into_elements", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Do not break SO₄²⁻ into sulphur and oxygen; it remains intact as a single polyatomic ion.",
        "concept": "Dissociation separates ionic bonds between cations and polyatomic anions. The covalent bonds within the polyatomic ion remain unaffected.",
        "breakdown": f"{s['formula']} releases separate cations and polyatomic anions: {s['eq']}.",
    }

    return make_science_question(
        prefix="ps10_aq_polyatomic",
        topic=TOPIC,
        subskill="05_dissociation_polyatomic_anion_salts",
        learning_objective_id=f"{LO}_polyatomic_dissociation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["broke_polyatomic_ion_into_atoms", "omitted_polyatomic_charge"],
        keywords=["polyatomic", "dissociation", "sulphate", "carbonate", "ammonium", "covalent bonds"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 06: Dissociation vs Ionisation Distinction
# --------------------------------------------------------------------------- #
def arch_06_dissociation_vs_ionisation(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compound_pair = rng.choice([
        ("sodium chloride (NaCl)", "hydrogen chloride (HCl)"),
        ("potassium nitrate (KNO3)", "pure ethanoic acid (CH3COOH)"),
        ("calcium chloride (CaCl2)", "hydrogen bromide (HBr)"),
    ])

    prompt = (
        f"When substances dissolve in water to produce ions, they may undergo either **dissociation** or **ionisation**.\n\n"
        f"1. Define the term **dissociation**.\n"
        f"2. Define the term **ionisation**.\n"
        f"3. Classify the behaviour of each of the following when added to water as either dissociation or ionisation:\n"
        f"   - **{compound_pair[0]}**\n"
        f"   - **{compound_pair[1]}**"
    )

    ans_latex = (
        r"\text{Dissociation: Separation of already-existing ions from an ionic solid; } "
        r"\quad \text{Ionisation: Formation of ions from neutral covalent molecules reacting with water}"
    )

    sample_answer = (
        f"1. Dissociation is the physical separation of already-existing ions in an ionic lattice when dissolved in water.\n"
        f"2. Ionisation is the chemical process where a neutral covalent molecular compound reacts with water to form new ions.\n"
        f"3. Classifications:\n"
        f"   - {compound_pair[0]}: **Dissociation** (it is an ionic compound composed of pre-existing ions).\n"
        f"   - {compound_pair[1]}: **Ionisation** (it is a covalent molecule that forms ions upon reacting with water molecules)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate definition of dissociation (pre-existing ions separated)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate definition of ionisation (neutral covalent molecules form ions)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct classification of {compound_pair[0]} as dissociation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct classification of {compound_pair[1]} as ionisation", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Check whether the starting compound is ionic (metal + non-metal) or covalent (non-metal + non-metal).",
        "concept": "Ionic compounds already contain ions (they dissociate). Covalent molecules do not contain ions until they react with water (they ionise).",
        "breakdown": f"Ionic solids like {compound_pair[0]} dissociate. Polar covalent molecules like {compound_pair[1]} ionise.",
    }

    return make_science_question(
        prefix="ps10_aq_diss_ion",
        topic=TOPIC,
        subskill="06_dissociation_vs_ionisation",
        learning_objective_id=f"{LO}_diss_vs_ion",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["treated_dissociation_and_ionisation_as_identical", "confused_covalent_and_ionic_nature"],
        keywords=["dissociation", "ionisation", "electrolyte", "covalent", "ionic lattice", "ions"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 07: Dissolution of Covalent Molecular Substances
# --------------------------------------------------------------------------- #
def arch_07_dissolution_covalent_molecular_substances(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    solute, formula, use = rng.choice([
        ("glucose", r"\text{C}_6\text{H}_{12}\text{O}_6", "cellular respiration"),
        ("sucrose", r"\text{C}_{12}\text{H}_{22}\text{O}_{11}", "table sugar in hot water"),
        ("ethanol", r"\text{C}_2\text{H}_5\text{OH}", "antiseptic disinfectant"),
        ("urea", r"\text{(NH}_2)_2\text{CO}", "nitrogenous fertiliser"),
    ])

    prompt = (
        f"Solid **{solute}** (${formula}$) is placed into a beaker of distilled water and stirred until it completely dissolves.\n\n"
        f"1. Write down an equation representing the dissolution of solid {solute} in water. Include state symbols.\n"
        f"2. Explain why {solute} dissolves readily in water even though it does not produce ions.\n"
        f"3. If a conductivity test is carried out on this solution, will the indicator bulb light up? Explain your answer."
    )

    eq = rf"{formula}\text{{(s)}} \xrightarrow{{\text{{H}}_2\text{{O}}}} {formula}\text{{(aq)}}"
    ans_latex = rf"{eq}; \quad \text{{Forms hydrogen bonds with water; Bulb will not light up (no free ions)}}"

    sample_answer = (
        f"1. Dissolution equation:\n"
        f"   $${eq}$$\n"
        f"2. {solute.capitalize()} contains polar hydroxyl (-OH) / amino groups that form extensive hydrogen bonds with polar water molecules.\n"
        f"3. No, the indicator bulb will NOT light up. Pure dissolved {solute} consists of neutral molecules with NO free mobile ions to carry an electric current (it is a non-electrolyte)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct equation with state symbols: {formula}(s) -> {formula}(aq)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reference to hydrogen bonding / polar interactions between solute and water", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Bulb will not light up stated", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Reason: absence of free mobile ions (non-electrolyte)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Dissolving does not necessarily mean breaking into ions. Some molecules remain intact as neutral molecules.",
        "concept": "Solubility depends on intermolecular forces (hydrogen bonding). Electrical conductivity requires free mobile charged particles (ions).",
        "breakdown": f"{solute} dissolves as neutral {formula}(aq) via hydrogen bonding. Without ions, it cannot conduct electricity.",
    }

    return make_science_question(
        prefix="ps10_aq_covalent_diss",
        topic=TOPIC,
        subskill="07_dissolution_covalent_molecular_substances",
        learning_objective_id=f"{LO}_covalent_dissolution",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_dissolved_substances_conduct", "split_glucose_into_ions"],
        keywords=["covalent dissolution", "non-electrolyte", "glucose", "sucrose", "hydrogen bonding", "conductivity"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 08: Electrolyte Definition and Classification
# --------------------------------------------------------------------------- #
def arch_08_electrolyte_definition_classification(rng: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    substances = [
        {"name": "Potassium nitrate (KNO3)", "class": "Strong electrolyte", "reason": "Dissociates completely into K+ and NO3- ions"},
        {"name": "Pure ethanoic acid (CH3COOH)", "class": "Weak electrolyte", "reason": "Only partially ionises in water (< 5% ions)"},
        {"name": "Liquid paraffin / cooking oil", "class": "Non-electrolyte", "reason": "Non-polar covalent compound that forms zero ions"},
        {"name": "Sodium hydroxide (NaOH)", "class": "Strong electrolyte", "reason": "Completely dissociates into Na+ and OH- ions"},
        {"name": "Ethanol (C2H5OH)", "class": "Non-electrolyte", "reason": "Dissolves as neutral molecules with zero free ions"},
    ]
    sample_substances = rng.sample(substances, 3)

    sub_list_str = "\n".join([f"   - **{s['name']}**" for s in sample_substances])

    prompt = (
        f"A chemist evaluates the conductivity of several substances dissolved in water.\n\n"
        f"1. Define the term **electrolyte**.\n"
        f"2. Distinguish between a **strong electrolyte** and a **weak electrolyte** in terms of ion concentration.\n"
        f"3. Classify each of the following substances as a **strong electrolyte**, **weak electrolyte**, or **non-electrolyte**:\n"
        f"{sub_list_str}"
    )

    ans_latex = r"\text{Electrolyte: A solution that contains free ions and conducts electricity via mobile charged particles}"

    sample_answer = (
        f"1. An electrolyte is a substance that contains free ions and behaves as an electrically conductive medium.\n"
        f"2. A strong electrolyte produces a high concentration of free ions in solution (complete dissociation or ionisation). "
        f"A weak electrolyte produces a low concentration of free ions in solution (only partial ionisation or dissociation).\n"
        f"3. Classifications:\n"
        + "\n".join([f"   - {s['name']}: **{s['class']}** ({s['reason']})" for s in sample_substances])
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate definition of electrolyte (free ions, conductive medium)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Distinction: strong (complete dissociation / high ion concentration) vs weak (partial / low ion concentration)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct classification of {sample_substances[0]['name']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct classification of {sample_substances[1]['name']}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Correct classification of {sample_substances[2]['name']}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Think about the extent to which the substance splits or ionises into charged particles in water.",
        "concept": "Strong electrolytes = 100% ions; Weak electrolytes = mostly molecules with few ions; Non-electrolytes = zero ions.",
        "breakdown": "Define electrolyte, distinguish high vs low ion concentrations, and classify the 3 specific substances.",
    }

    return make_science_question(
        prefix="ps10_aq_electrolyte_def",
        topic=TOPIC,
        subskill="08_electrolyte_definition_classification",
        learning_objective_id=f"{LO}_electrolyte_def",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_concentration_with_electrolyte_strength", "assumed_water_alone_is_strong_conductor"],
        keywords=["electrolyte", "strong electrolyte", "weak electrolyte", "non-electrolyte", "ions", "conductivity"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 09: Conductivity Apparatus & Circuit Interpretation (With SVG)
# --------------------------------------------------------------------------- #
def arch_09_conductivity_apparatus_circuit_interpretation(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    volts = rng.choice([6, 9, 12])
    test_case = rng.choice([
        {"substance": r"0{,}5\text{ mol}\cdot\text{dm}^{-3}\ \text{NaCl}(aq)", "amm": round(rng.uniform(1.2, 1.8), 2), "lit": True, "label": "0,5 M NaCl (aq)", "ions": "Na+ and Cl- ions present"},
        {"substance": r"0{,}5\text{ mol}\cdot\text{dm}^{-3}\ \text{CH}_3\text{COOH}(aq)", "amm": round(rng.uniform(0.05, 0.15), 2), "lit": False, "label": "0,5 M CH3COOH (aq)", "ions": "Few H3O+ and CH3COO- ions"},
        {"substance": r"\text{Distilled Water}", "amm": 0.00, "lit": False, "label": "Pure Distilled Water", "ions": "No free mobile ions"},
    ])

    svg = _generate_conductivity_circuit_svg(
        rng,
        cell_volts=volts,
        ammeter_reading=test_case["amm"],
        bulb_lit=test_case["lit"],
        solution_label=test_case["label"],
        ions_text=test_case["ions"],
    )

    prompt = (
        f"A learner constructs an electrical circuit to investigate the conductivity of different liquids.\n"
        f"Refer to the circuit showing two carbon electrodes connected to a **{volts} V DC** power source, "
        f"an ammeter, and an indicator bulb submerged in **{test_case['substance']}**.\n\n"
        f"1. State the role of the carbon electrodes in this investigation.\n"
        f"2. The ammeter records a current of **{fmt_sa(test_case['amm'])}\\text{{ A}}**. "
        f"Explain why this current is observed by referring to the nature and concentration of mobile charge carriers.\n"
        f"3. State what serves as the charge carriers in: (a) the copper conducting wires, and (b) the aqueous electrolyte solution."
    )

    ans_latex = (
        rf"I = {fmt_sa(test_case['amm'])}\text{{ A}}; \quad "
        rf"\text{{(a) Wires: Delocalised electrons; (b) Solution: Free mobile ions}}"
    )

    sample_answer = (
        f"1. The carbon electrodes conduct current into and out of the liquid without chemically reacting (they are inert conductors).\n"
        f"2. The ammeter reading of {fmt_sa(test_case['amm'])} A reflects the presence and concentration of free, mobile ions in the liquid. "
        + ("Because NaCl dissociates completely into free Na⁺ and Cl⁻ ions, they migrate under the electric field, providing high conductivity and lighting the bulb."
           if test_case["lit"]
           else ("Because ethanoic acid is a weak acid, it ionises only partially, providing very few mobile ions and insufficient current to light the bulb."
                 if test_case["amm"] > 0
                 else "Distilled water consists almost entirely of neutral H₂O molecules with negligible ions, resulting in zero measurable current."))
        + f"\n3. (a) In the copper connecting wires: **Delocalised valence electrons**.\n"
        f"   (b) In the aqueous solution: **Free mobile cations and anions**."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Role of carbon rods: inert electrodes to pass current into liquid", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explanation of ammeter reading in terms of mobile ion concentration", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Charge carriers in wires: delocalised electrons", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Charge carriers in solution: free mobile ions", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Do electrons travel through the liquid, or do ions carry the current in the solution?",
        "concept": "Current in metals is carried by delocalised electrons. Current in electrolytic solutions is carried by the migration of mobile ions towards oppositely charged electrodes.",
        "breakdown": f"Wires conduct via free electrons; the solution conducts via ions. The measured {fmt_sa(test_case['amm'])} A depends directly on ion availability.",
    }

    return make_science_question(
        prefix="ps10_aq_circuit_svg",
        topic=TOPIC,
        subskill="09_conductivity_apparatus_circuit_interpretation",
        learning_objective_id=f"{LO}_circuit_interpretation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["claimed_electrons_flow_through_solution", "confused_electrodes_with_electrolytes"],
        keywords=["conductivity circuit", "ammeter", "carbon electrodes", "free mobile ions", "electrons in wire"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=4,
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# --------------------------------------------------------------------------- #
# Subskill 10: Factors Affecting Conductivity — Ion Concentration
# --------------------------------------------------------------------------- #
def arch_10_conductivity_factors_ion_concentration(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt = rng.choice([r"\text{NaCl}", r"\text{KCl}", r"\text{KNO}_3"])
    c1 = round(rng.uniform(0.1, 0.2), 2)
    c2 = round(rng.uniform(0.8, 1.2), 2)
    amm1 = round(c1 * 2.2, 2)
    amm2 = round(c2 * 2.2, 2)

    prompt = (
        f"A laboratory investigation measures the electrical conductivity of two separate aqueous solutions of ${salt}$:\n"
        f"- **Solution A**: Concentration = ${fmt_sa(c1)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$, Ammeter reading = **{fmt_sa(amm1)}\\text{{ A}}**\n"
        f"- **Solution B**: Concentration = ${fmt_sa(c2)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$, Ammeter reading = **{fmt_sa(amm2)}\\text{{ A}}**\n\n"
        f"1. Formulate an investigative question for this experiment.\n"
        f"2. Identify the **independent variable** and the **dependent variable**.\n"
        f"3. Explain the relationship observed between electrolyte concentration and electrical conductivity."
    )

    ans_latex = (
        rf"\text{{Investigative Question: How does the concentration of }}{salt}\text{{ affect electrical conductivity?}}; "
        rf"\quad \text{{Independent: Concentration; Dependent: Current (conductivity)}}"
    )

    sample_answer = (
        f"1. Investigative Question: What is the relationship between the concentration of {salt} solution and its electrical conductivity? "
        f"(or: How does the concentration of an electrolyte affect the current flowing through it?)\n"
        f"2. Independent variable: Concentration of the {salt} solution.\n"
        f"   Dependent variable: Electrical conductivity (measured as electric current in amperes).\n"
        f"3. Relationship: Electrical conductivity increases as the concentration of {salt} increases. "
        f"A higher solute concentration yields a higher number of free, mobile ions per unit volume, "
        f"allowing more charge to be transported per second across the electrodes."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Valid investigative question including both variables and ending with a question mark", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct independent variable identified (concentration)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct dependent variable identified (current / conductivity)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Scientific explanation linking higher ion count per unit volume to greater conductivity", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "An investigative question must mention both variables and cannot be answered with a simple 'yes' or 'no'.",
        "concept": "Conductivity is directly proportional to the concentration of free charge carriers (ions per dm³).",
        "breakdown": f"Solution B has higher concentration ({fmt_sa(c2)} vs {fmt_sa(c1)} mol·dm⁻³), meaning more ions per cm³, yielding higher current ({fmt_sa(amm2)} vs {fmt_sa(amm1)} A).",
    }

    return make_science_question(
        prefix="ps10_aq_factors_conc",
        topic=TOPIC,
        subskill="10_conductivity_factors_ion_concentration",
        learning_objective_id=f"{LO}_factors_concentration",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_independent_and_dependent_variables", "yes_no_investigative_question"],
        keywords=["investigative question", "conductivity", "ion concentration", "independent variable", "dependent variable"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 11: Factors Affecting Conductivity — Ion Charge & Count
# --------------------------------------------------------------------------- #
def arch_11_conductivity_factors_ion_charge_and_count(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    conc = round(rng.uniform(0.2, 0.5), 1)

    prompt = (
        f"Two separate beakers contain solutions of equal concentration **${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**:\n"
        f"- **Beaker 1**: $\\text{{NaCl}}(aq)$\n"
        f"- **Beaker 2**: $\\text{{CaCl}}_2(aq)$\n\n"
        f"Both solutions are tested using identical conductivity apparatus under identical laboratory conditions.\n\n"
        f"1. Write down the dissociation equations for both salts in water.\n"
        f"2. Calculate the total concentration of ions present in:\n"
        f"   - Beaker 1 (${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{NaCl}}$)\n"
        f"   - Beaker 2 (${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{CaCl}}_2$)\n"
        f"3. Predict and explain which beaker will cause the indicator bulb to shine brighter."
    )

    ions_nacl = round(conc * 2, 2)
    ions_cacl2 = round(conc * 3, 2)

    ans_latex = (
        rf"\text{{Beaker 1: }} [\text{{Ions}}] = {fmt_sa(ions_nacl)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}; \quad "
        rf"\text{{Beaker 2: }} [\text{{Ions}}] = {fmt_sa(ions_cacl2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}; \quad "
        rf"\text{{Beaker 2 shines brighter}}"
    )

    sample_answer = (
        f"1. Dissociation equations:\n"
        f"   - $\\text{{NaCl}}(s) \\to \\text{{Na}}^+(aq) + \\text{{Cl}}^-(aq)$\n"
        f"   - $\\text{{CaCl}}_2(s) \\to \\text{{Ca}}^{{2+}}(aq) + 2\\text{{Cl}}^-(aq)$\n"
        f"2. Total ion concentration:\n"
        f"   - Beaker 1: $1\\text{{ mol NaCl}} \\to 2\\text{{ mol ions}}$, so $[\text{{ions}}] = 2 \\times {fmt_sa(conc)} = {fmt_sa(ions_nacl)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.\n"
        f"   - Beaker 2: $1\\text{{ mol CaCl}}_2 \\to 3\\text{{ mol ions}}$, so $[\text{{ions}}] = 3 \\times {fmt_sa(conc)} = {fmt_sa(ions_cacl2)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.\n"
        f"3. Prediction: **Beaker 2 (CaCl₂)** will shine brighter.\n"
        f"   Explanation: At identical solute concentrations, CaCl₂ releases 3 moles of ions per mole of formula units compared to 2 for NaCl. "
        f"Furthermore, Ca²⁺ ions carry a greater ionic charge (+2 vs +1). The higher total ion concentration ({fmt_sa(ions_cacl2)} vs {fmt_sa(ions_nacl)} mol·dm⁻³) "
        f"and higher charge density allow greater current flow."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct dissociation equation for NaCl", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct dissociation equation for CaCl2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct ion concentration for NaCl ({fmt_sa(ions_nacl)} mol·dm⁻³)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct ion concentration for CaCl2 ({fmt_sa(ions_cacl2)} mol·dm⁻³)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Correct prediction (CaCl2) and reasoning based on higher ion count / charge", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Count how many ions are produced when one formula unit of each salt dissolves.",
        "concept": "1 mole of NaCl produces 2 moles of ions (Na⁺ + Cl⁻); 1 mole of CaCl₂ produces 3 moles of ions (Ca²⁺ + 2Cl⁻).",
        "breakdown": f"CaCl₂ produces {fmt_sa(ions_cacl2)} mol·dm⁻³ of ions, whereas NaCl produces {fmt_sa(ions_nacl)} mol·dm⁻³. Higher ion concentration = greater conductivity.",
    }

    return make_science_question(
        prefix="ps10_aq_ion_count",
        topic=TOPIC,
        subskill="11_conductivity_factors_ion_charge_and_count",
        learning_objective_id=f"{LO}_ion_count_charge",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_equal_solute_concentration_gives_equal_conductivity", "forgot_stoichiometric_multiplier"],
        keywords=["equimolar", "calcium chloride", "sodium chloride", "ion concentration", "conductivity comparison"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 12: Factors Affecting Conductivity — Weak vs Strong Electrolytes
# --------------------------------------------------------------------------- #
def arch_12_conductivity_factors_weak_vs_strong_electrolytes(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    conc = round(rng.uniform(0.1, 0.5), 1)

    prompt = (
        f"A learner prepares two solutions of identical concentration **${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**:\n"
        f"- **Solution 1**: Hydrochloric acid ($\\text{{HCl}}$)\n"
        f"- **Solution 2**: Ethanoic acid ($\\text{{CH}}_3\\text{{COOH}}$)\n\n"
        f"When connected to a conductivity apparatus, the ammeter in Solution 1 reads **{fmt_sa(1.45)}\\text{{ A}}**, "
        f"while the ammeter in Solution 2 reads only **{fmt_sa(0.08)}\\text{{ A}}**.\n\n"
        f"1. Write down an equation showing how $\\text{{HCl}}$ ionises in water.\n"
        f"2. Write down an equation showing how $\\text{{CH}}_3\\text{{COOH}}$ ionises in water.\n"
        f"3. Explain why the conductivity of Solution 1 is significantly higher than Solution 2 despite having the same molar concentration."
    )

    ans_latex = (
        r"\text{HCl} + \text{H}_2\text{O} \to \text{H}_3\text{O}^+ + \text{Cl}^-; \quad "
        r"\text{CH}_3\text{COOH} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{CH}_3\text{COO}^-; \quad "
        r"\text{HCl completely ionises vs partial ionisation of ethanoic acid}"
    )

    sample_answer = (
        f"1. Ionisation of hydrochloric acid:\n"
        f"   $$\\text{{HCl}}(g) + \\text{{H}}_2\\text{{O}}(\\ell) \\to \\text{{H}}_3\\text{{O}}^+(aq) + \\text{{Cl}}^-(aq)$$\n"
        f"2. Ionisation of ethanoic acid:\n"
        f"   $$\\text{{CH}}_3\\text{{COOH}}(\\ell) + \\text{{H}}_2\\text{{O}}(\\ell) \\rightleftharpoons \\text{{H}}_3\\text{{O}}^+(aq) + \\text{{CH}}_3\\text{{COO}}^-(aq)$$\n"
        f"3. Explanation:\n"
        f"   Hydrochloric acid is a strong acid that ionises completely in water (100% ionised), creating a very high concentration of free mobile $\\text{{H}}_3\\text{{O}}^+$ and $\\text{{Cl}}^-$ ions.\n"
        f"   Ethanoic acid is a weak acid that only partially ionises in water (< 5% ionised); most molecules remain as neutral, uncharged $\\text{{CH}}_3\\text{{COOH}}$ molecules.\n"
        f"   Therefore, Solution 1 has a vastly higher concentration of charge carriers, producing a much higher current ({fmt_sa(1.45)} A vs {fmt_sa(0.08)} A)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct equation for complete ionisation of HCl", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct equation for partial reversible ionisation of CH3COOH (equilibrium arrow)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "State that HCl is a strong acid that ionises completely", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "State that CH3COOH is a weak acid that only partially ionises, producing fewer mobile ions", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Concentration of solute is the same, but the concentration of ions is vastly different. Why?",
        "concept": "Strong acids ionise 100% into ions; weak acids reach an equilibrium where only a small percentage forms ions.",
        "breakdown": "HCl ionises completely to produce many ions (high conductivity). CH₃COOH only partially ionises to produce few ions (low conductivity).",
    }

    return make_science_question(
        prefix="ps10_aq_weak_strong",
        topic=TOPIC,
        subskill="12_conductivity_factors_weak_vs_strong_electrolytes",
        learning_objective_id=f"{LO}_weak_vs_strong",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_acids_conduct_equally", "confused_acid_strength_with_concentration"],
        keywords=["strong acid", "weak acid", "complete ionisation", "partial ionisation", "conductivity", "hydrochloric acid", "ethanoic acid"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 13: Ion Concentration Calculation from Molarity
# --------------------------------------------------------------------------- #
def arch_13_ion_concentration_calculation_from_molarity(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt_data = [
        {"name": "Aluminium sulphate", "formula": r"\text{Al}_2(\text{SO}_4)_3", "cat": r"\text{Al}^{3+}", "cat_coef": 2, "an": r"\text{SO}_4^{2-}", "an_coef": 3},
        {"name": "Iron(III) sulphate", "formula": r"\text{Fe}_2(\text{SO}_4)_3", "cat": r"\text{Fe}^{3+}", "cat_coef": 2, "an": r"\text{SO}_4^{2-}", "an_coef": 3},
        {"name": "Magnesium phosphate", "formula": r"\text{Mg}_3(\text{PO}_4)_2", "cat": r"\text{Mg}^{2+}", "cat_coef": 3, "an": r"\text{PO}_4^{3-}", "an_coef": 2},
    ]
    s = rng.choice(salt_data)
    c_salt = round(rng.uniform(0.15, 0.45), 2)
    c_cat = round(c_salt * s["cat_coef"], 3)
    c_an = round(c_salt * s["an_coef"], 3)
    total_c = round(c_cat + c_an, 3)

    prompt = (
        f"An aqueous solution of **{s['name']}** (${s['formula']}$) has a concentration of "
        f"**${fmt_sa(c_salt)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**.\n"
        f"Assume complete dissociation in water.\n\n"
        f"1. Write down the dissociation equation for ${s['formula']}$ in water.\n"
        f"2. Calculate the molar concentration of the cation, $[{s['cat']}]$.\n"
        f"3. Calculate the molar concentration of the anion, $[{s['an']}]$.\n"
        f"4. Determine the total concentration of all dissolved ions in this solution."
    )

    ans_latex = (
        rf"[{s['cat']}] = {fmt_sa(c_cat)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}, \quad "
        rf"[{s['an']}] = {fmt_sa(c_an)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}, \quad "
        rf"[\text{{Total ions}}] = {fmt_sa(total_c)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}"
    )

    sample_answer = (
        f"1. Dissociation equation:\n"
        f"   $${s['formula']}(s) \\to {s['cat_coef']}{s['cat']}(aq) + {s['an_coef']}{s['an']}(aq)$$\n"
        f"2. Concentration of cation $[{s['cat']}]$:\n"
        f"   $$[{s['cat']}] = {s['cat_coef']} \\times c(\\text{{{s['name']}}}) = {s['cat_coef']} \\times {fmt_sa(c_salt)} = {fmt_sa(c_cat)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. Concentration of anion $[{s['an']}]$:\n"
        f"   $$[{s['an']}] = {s['an_coef']} \\times c(\\text{{{s['name']}}}) = {s['an_coef']} \\times {fmt_sa(c_salt)} = {fmt_sa(c_an)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"4. Total ion concentration:\n"
        f"   $$[\text{{Total}}] = {fmt_sa(c_cat)} + {fmt_sa(c_an)} = {fmt_sa(total_c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct balanced dissociation equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct cation concentration: {fmt_sa(c_cat)} mol·dm⁻³", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct anion concentration: {fmt_sa(c_an)} mol·dm⁻³", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct total ion concentration: {fmt_sa(total_c)} mol·dm⁻³", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Multiply the salt's concentration by the stoichiometric subscript of each ion.",
        "concept": "c(ion) = coefficient × c(salt). For Al₂(SO₄)₃, [Al³⁺] = 2 × c, and [SO₄²⁻] = 3 × c.",
        "breakdown": f"Salt concentration = {fmt_sa(c_salt)} mol·dm⁻³. [Cation] = {s['cat_coef']} × {fmt_sa(c_salt)} = {fmt_sa(c_cat)} mol·dm⁻³. [Anion] = {s['an_coef']} × {fmt_sa(c_salt)} = {fmt_sa(c_an)} mol·dm⁻³.",
    }

    return make_science_question(
        prefix="ps10_aq_molarity_calc",
        topic=TOPIC,
        subskill="13_ion_concentration_calculation_from_molarity",
        learning_objective_id=f"{LO}_molarity_calc",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["forgot_to_multiply_by_stoichiometric_coefficients", "confused_molarity_with_mass"],
        keywords=["molar concentration", "ion concentration", "stoichiometry", "dissociation", "aluminium sulphate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 14: Precipitation Definition & Driving Force
# --------------------------------------------------------------------------- #
def arch_14_precipitation_definition_driving_force(rng: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    reactants = rng.choice([
        (r"\text{AgNO}_3(aq)", r"\text{NaCl}(aq)", r"\text{AgCl}(s)", "silver chloride"),
        (r"\text{BaCl}_2(aq)", r"\text{Na}_2\text{SO}_4(aq)", r"\text{BaSO}_4(s)", "barium sulphate"),
        (r"\text{Pb(NO}_3)_2(aq)", r"2\text{KI}(aq)", r"\text{PbI}_2(s)", "lead(II) iodide"),
    ])

    prompt = (
        f"When clear aqueous solutions of **${reactants[0]}$** and **${reactants[1]}$** are mixed, "
        f"an insoluble solid **{reactants[3]}** (${reactants[2]}$) separates out immediately.\n\n"
        f"1. Define the term **precipitate**.\n"
        f"2. Define the term **precipitation reaction**.\n"
        f"3. Explain what constitutes the **driving force** for this precipitation reaction."
    )

    ans_latex = (
        r"\text{Precipitate: An insoluble solid formed in solution during a chemical reaction; } "
        r"\quad \text{Driving force: Formation of an insoluble ionic lattice with electrostatic lattice energy exceeding hydration energy}"
    )

    sample_answer = (
        f"1. A precipitate is an insoluble solid that forms in a solution during a chemical reaction.\n"
        f"2. A precipitation reaction is a chemical reaction in aqueous solution in which two soluble ionic compounds react to form an insoluble solid product.\n"
        f"3. The driving force is the electrostatic attraction between the reacting ions (e.g. {reactants[3]}), "
        f"which is stronger than the ion-dipole attractions between the ions and water molecules. "
        f"This drives the ions out of the aqueous phase into a stable solid crystal lattice."
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate definition of precipitate (insoluble solid formed in solution)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate definition of precipitation reaction", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Driving force explained: formation of insoluble precipitate removes ions from solution / lattice energy exceeds hydration", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "What makes a chemical reaction occur spontaneously in solution? Think about what is removed from the solution.",
        "concept": "The driving force in precipitation is the removal of ions from solution into an insoluble crystal lattice.",
        "breakdown": "Define precipitate, precipitation reaction, and state that the insoluble solid formation drives the reaction forward.",
    }

    return make_science_question(
        prefix="ps10_aq_precip_def",
        topic=TOPIC,
        subskill="14_precipitation_definition_driving_force",
        learning_objective_id=f"{LO}_precip_def",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_precipitate_with_residue", "assumed_all_mixed_salts_precipitate"],
        keywords=["precipitate", "precipitation reaction", "driving force", "insoluble salt", "lattice energy"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=3,
        mode="compound",
        difficulty=difficulty,
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Subskill 15: Solubility Rules — Halides
# --------------------------------------------------------------------------- #
def arch_15_solubility_rules_halides(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        {"sol1": r"\text{AgNO}_3", "sol2": r"\text{KCl}", "precip": r"\text{AgCl}", "color": "white", "is_precip": True},
        {"sol1": r"\text{Pb(NO}_3)_2", "sol2": r"\text{NaI}", "precip": r"\text{PbI}_2", "color": "bright yellow", "is_precip": True},
        {"sol1": r"\text{CuSO}_4", "sol2": r"\text{NaCl}", "precip": r"\text{None}", "color": "no precipitate", "is_precip": False},
        {"sol1": r"\text{AgNO}_3", "sol2": r"\text{KBr}", "precip": r"\text{AgBr}", "color": "cream / pale yellow", "is_precip": True},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A learner mixes equal volumes of aqueous **${c['sol1']}$** and **${c['sol2']}$** in a test tube.\n\n"
        f"1. State the general solubility rule regarding chloride, bromide, and iodide salts.\n"
        f"2. Predict whether a precipitate will form when these two solutions are mixed.\n"
        f"3. If a precipitate forms, write down its chemical formula and describe its colour. If no precipitate forms, explain why."
    )

    ans_latex = (
        rf"\text{{Precipitate: }}{c['precip'] if c['is_precip'] else 'No precipitate'}; \quad "
        rf"\text{{Colour: }}{c['color']}"
    )

    sample_answer = (
        f"1. Solubility Rule: All common chlorides, bromides, and iodides are soluble in water, EXCEPT those of silver (Ag⁺) and lead(II) (Pb²⁺).\n"
        f"2. Prediction: " + ("A precipitate will form." if c["is_precip"] else "NO precipitate will form.") + "\n"
        f"3. " + (f"Precipitate Formula: **{c['precip']}**.\n   Observable Colour: **{c['color']}**."
                  if c["is_precip"]
                  else "Both products (CuCl₂ and Na₂SO₄) are completely soluble in water, so all ions remain freely dissolved.")
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct general solubility rule for halides (soluble except Ag+ and Pb2+)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate prediction of whether a precipitate forms", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct precipitate formula ({c['precip']}) or explanation of why none forms", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct observable colour ({c['color']})", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Recall the halide exceptions: which metals form insoluble halides?",
        "concept": "Halides of Ag⁺ and Pb²⁺ are insoluble. AgCl is white, AgBr is cream, AgI is pale yellow, PbI₂ is bright yellow.",
        "breakdown": f"Mixing {c['sol1']} and {c['sol2']}: Ag⁺/Pb²⁺ with halide gives {c['precip']} ({c['color']}).",
    }

    return make_science_question(
        prefix="ps10_aq_sol_halides",
        topic=TOPIC,
        subskill="15_solubility_rules_halides",
        learning_objective_id=f"{LO}_sol_halides",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_chlorides_are_insoluble", "incorrect_precipitate_color"],
        keywords=["solubility rules", "halides", "silver chloride", "lead iodide", "precipitate"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 16: Solubility Rules — Sulphates
# --------------------------------------------------------------------------- #
def arch_16_solubility_rules_sulphates(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        {"sol1": r"\text{Ba(NO}_3)_2", "sol2": r"\text{Na}_2\text{SO}_4", "precip": r"\text{BaSO}_4", "is_precip": True, "name": "barium sulphate"},
        {"sol1": r"\text{Pb(NO}_3)_2", "sol2": r"\text{K}_2\text{SO}_4", "precip": r"\text{PbSO}_4", "is_precip": True, "name": "lead(II) sulphate"},
        {"sol1": r"\text{MgSO}_4", "sol2": r"\text{NaCl}", "precip": r"\text{None}", "is_precip": False, "name": "no precipitate"},
        {"sol1": r"\text{CaCl}_2", "sol2": r"\text{Na}_2\text{SO}_4", "precip": r"\text{CaSO}_4", "is_precip": True, "name": "calcium sulphate (sparingly soluble)"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A laboratory practical investigates sulphate solubility by mixing aqueous **${c['sol1']}$** and **${c['sol2']}$**.\n\n"
        f"1. State the general solubility rule regarding sulphate ($\\text{{SO}}_4^{{2-}}$) salts.\n"
        f"2. Predict whether an insoluble precipitate will form in this mixture.\n"
        f"3. Write down the chemical name and formula of the precipitate formed, or explain why none forms.\n"
        f"4. State the observable colour of the precipitate (if any)."
    )

    ans_latex = (
        rf"\text{{Solubility Rule: Most sulphates are soluble, except }}\text{{Ba}}^{{2+}}, \text{{Pb}}^{{2+}}, \text{{Ca}}^{{2+}}; \quad "
        rf"\text{{Precipitate: }}{c['precip']}"
    )

    sample_answer = (
        f"1. Solubility Rule: Most sulphate salts are soluble in water, EXCEPT barium sulphate (BaSO₄), lead(II) sulphate (PbSO₄), and calcium sulphate (CaSO₄, sparingly soluble).\n"
        f"2. Prediction: " + ("A precipitate will form." if c["is_precip"] else "NO precipitate will form.") + "\n"
        f"3. " + (f"Precipitate: **{c['name']}** (Formula: **${c['precip']}$**)."
                  if c["is_precip"]
                  else "Both MgCl₂ and Na₂SO₄ are highly soluble in water; all ions remain dissolved.") + "\n"
        f"4. Colour: " + ("White solid precipitate." if c["is_precip"] else "Clear colourless solution (no solid).")
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct solubility rule for sulphates and exceptions (Ba2+, Pb2+, Ca2+)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate prediction of precipitate formation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct chemical name and formula: {c['name']} ({c['precip']})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Accurate colour description (white precipitate)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which metals form insoluble sulphates? Remember Ba²⁺, Pb²⁺, Ca²⁺.",
        "concept": "Barium sulphate is extremely insoluble and forms a dense white precipitate.",
        "breakdown": f"Mixing {c['sol1']} with {c['sol2']}: Ba²⁺/Pb²⁺/Ca²⁺ + SO₄²⁻ gives {c['precip']} (white precipitate).",
    }

    return make_science_question(
        prefix="ps10_aq_sol_sulphates",
        topic=TOPIC,
        subskill="16_solubility_rules_sulphates",
        learning_objective_id=f"{LO}_sol_sulphates",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_sulphates_are_soluble", "confused_barium_with_beryllium"],
        keywords=["solubility rules", "sulphates", "barium sulphate", "precipitate", "insoluble"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 17: Solubility Rules — Carbonates and Hydroxides
# --------------------------------------------------------------------------- #
def arch_17_solubility_rules_carbonates_hydroxides(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        {"sol1": r"\text{CuSO}_4", "sol2": r"\text{NaOH}", "precip": r"\text{Cu(OH)}_2", "color": "blue precipitate", "type": "hydroxide"},
        {"sol1": r"\text{FeCl}_3", "sol2": r"\text{NaOH}", "precip": r"\text{Fe(OH)}_3", "color": "reddish-brown precipitate", "type": "hydroxide"},
        {"sol1": r"\text{CaCl}_2", "sol2": r"\text{Na}_2\text{CO}_3", "precip": r"\text{CaCO}_3", "color": "white precipitate", "type": "carbonate"},
        {"sol1": r"\text{FeSO}_4", "sol2": r"\text{NaOH}", "precip": r"\text{Fe(OH)}_2", "color": "dirty green precipitate", "type": "hydroxide"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A learner mixes aqueous solutions of **${c['sol1']}$** and **${c['sol2']}$** in a test tube.\n\n"
        f"1. State the general solubility rule for {c['type']} salts in water.\n"
        f"2. Write down the chemical formula of the insoluble precipitate that forms.\n"
        f"3. State the observable colour of this precipitate.\n"
        f"4. Name the ions that remain dissolved in solution as spectator ions."
    )

    ans_latex = rf"\text{{Precipitate: }}{c['precip']}; \quad \text{{Colour: }}{c['color']}"

    sample_answer = (
        f"1. General Solubility Rule:\n"
        + ("   - Most metal hydroxides are insoluble in water, EXCEPT those of Group 1 alkali metals (Li⁺, Na⁺, K⁺) and ammonium (NH₄⁺). (Ca(OH)₂ is sparingly soluble)."
           if c["type"] == "hydroxide"
           else "   - Most metal carbonates are insoluble in water, EXCEPT those of Group 1 alkali metals (Li⁺, Na⁺, K⁺) and ammonium (NH₄⁺).")
        + f"\n2. Chemical formula of the precipitate: **${c['precip']}$**.\n"
        f"3. Observable colour: **{c['color']}**.\n"
        f"4. Spectator ions: " + ("Na⁺ and SO₄²⁻ ions." if "SO_4" in c["sol1"] else ("Na⁺ and Cl⁻ ions." if "Cl" in c["sol1"] else "Dissolved Group 1 / nitrate ions."))
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct solubility rule for {c['type']}s (insoluble except Group 1 and NH4+)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct chemical formula: {c['precip']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct observable colour: {c['color']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Identification of spectator ions remaining in solution", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Carbonates and hydroxides are generally insoluble unless paired with a Group 1 metal (like Na⁺ or K⁺).",
        "concept": "Transition metal hydroxides have characteristic colours: Cu(OH)₂ is blue, Fe(OH)₂ is dirty green, Fe(OH)₃ is reddish-brown.",
        "breakdown": f"{c['sol1']} + {c['sol2']} forms insoluble {c['precip']} ({c['color']}).",
    }

    return make_science_question(
        prefix="ps10_aq_sol_carb_hyd",
        topic=TOPIC,
        subskill="17_solubility_rules_carbonates_hydroxides",
        learning_objective_id=f"{LO}_sol_carb_hyd",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_hydroxides_are_soluble", "incorrect_transition_metal_hydroxide_color"],
        keywords=["solubility rules", "carbonates", "hydroxides", "copper hydroxide", "iron hydroxide", "precipitate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 18: Spectator Ions Identification
# --------------------------------------------------------------------------- #
def arch_18_spectator_ions_identification(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    reactions = [
        {
            "name": "Barium chloride + Sodium sulphate",
            "overall": r"\text{BaCl}_2(aq) + \text{Na}_2\text{SO}_4(aq) \to \text{BaSO}_4(s) + 2\text{NaCl}(aq)",
            "spectators": [r"\text{Na}^+", r"\text{Cl}^-"],
            "precip": r"\text{BaSO}_4(s)",
        },
        {
            "name": "Silver nitrate + Potassium bromide",
            "overall": r"\text{AgNO}_3(aq) + \text{KBr}(aq) \to \text{AgBr}(s) + \text{KNO}_3(aq)",
            "spectators": [r"\text{K}^+", r"\text{NO}_3^-"],
            "precip": r"\text{AgBr}(s)",
        },
        {
            "name": "Lead(II) nitrate + Sodium chloride",
            "overall": r"\text{Pb(NO}_3)_2(aq) + 2\text{NaCl}(aq) \to \text{PbCl}_2(s) + 2\text{NaNO}_3(aq)",
            "spectators": [r"\text{Na}^+", r"\text{NO}_3^-"],
            "precip": r"\text{PbCl}_2(s)",
        },
    ]
    r_item = rng.choice(reactions)

    prompt = (
        f"Consider the precipitation reaction represented by the balanced equation below:\n"
        f"$${r_item['overall']}$$\n\n"
        f"1. Define the term **spectator ion**.\n"
        f"2. Identify the TWO spectator ions in this reaction (write their chemical symbols with correct ionic charges).\n"
        f"3. Explain why spectator ions are omitted when writing a **net ionic equation**."
    )

    spec_str = ", ".join(r_item["spectators"])
    ans_latex = rf"\text{{Spectator ions: }} {spec_str}"

    sample_answer = (
        f"1. A spectator ion is an ion that exists in the same form on both the reactant and product sides of a chemical reaction without undergoing any chemical change.\n"
        f"2. The spectator ions are **${r_item['spectators'][0]}$** and **${r_item['spectators'][1]}$**.\n"
        f"3. They are omitted from the net ionic equation because they do not participate in the formation of the insoluble precipitate (${r_item['precip']}); "
        f"cancelling them focuses strictly on the chemical species that undergo a transformation."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate definition of spectator ion (remains unchanged in aqueous phase on both sides)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct identification of first spectator ion: {r_item['spectators'][0]}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct identification of second spectator ion: {r_item['spectators'][1]}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Explanation: omitted because they do not take part in precipitate formation", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which ions remain dissolved in the aqueous state (aq) before and after the reaction?",
        "concept": "Spectator ions are like spectators at a sports match: they are present, but do not take part in the actual game.",
        "breakdown": f"In {r_item['overall']}, {r_item['precip']} forms the precipitate, leaving {spec_str} unchanged in solution.",
    }

    return make_science_question(
        prefix="ps10_aq_spectator",
        topic=TOPIC,
        subskill="18_spectator_ions_identification",
        learning_objective_id=f"{LO}_spectator_ions",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["included_precipitate_ions_as_spectators", "omitted_ionic_charge_on_spectators"],
        keywords=["spectator ions", "net ionic equation", "precipitation", "aqueous", "reaction"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 19: Full Ionic Equations for Precipitation
# --------------------------------------------------------------------------- #
def arch_19_full_ionic_equations_precipitation(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    systems = [
        {
            "name": "Barium chloride and sodium sulphate",
            "molecular": r"\text{BaCl}_2(aq) + \text{Na}_2\text{SO}_4(aq) \to \text{BaSO}_4(s) + 2\text{NaCl}(aq)",
            "full_ionic": r"\text{Ba}^{2+}(aq) + 2\text{Cl}^-(aq) + 2\text{Na}^+(aq) + \text{SO}_4^{2-}(aq) \to \text{BaSO}_4(s) + 2\text{Na}^+(aq) + 2\text{Cl}^-(aq)",
            "precip": r"\text{BaSO}_4(s)",
        },
        {
            "name": "Silver nitrate and calcium chloride",
            "molecular": r"2\text{AgNO}_3(aq) + \text{CaCl}_2(aq) \to 2\text{AgCl}(s) + \text{Ca(NO}_3)_2(aq)",
            "full_ionic": r"2\text{Ag}^+(aq) + 2\text{NO}_3^-(aq) + \text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq) \to 2\text{AgCl}(s) + \text{Ca}^{2+}(aq) + 2\text{NO}_3^-(aq)",
            "precip": r"2\text{AgCl}(s)",
        },
    ]
    s = rng.choice(systems)

    prompt = (
        f"A precipitation reaction occurs when aqueous solutions of **{s['name']}** are mixed:\n"
        f"$${s['molecular']}$$\n\n"
        f"1. Write down the **full ionic equation** (complete ionic equation) for this reaction. "
        f"Include all ionic charges and state symbols.\n"
        f"2. Explain why the precipitate (${s['precip']}$) is NOT split into separate ions in the full ionic equation."
    )

    ans_latex = s["full_ionic"]

    sample_answer = (
        f"1. Full ionic equation:\n"
        f"   $${s['full_ionic']}$$\n"
        f"2. Explanation:\n"
        f"   The precipitate (${s['precip']}$) is an insoluble solid compound bound within a solid crystal lattice. "
        f"It is not dissociated into separate free mobile ions in the aqueous medium, so it must be written as a neutral solid formula unit with the `(s)` state symbol."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "All soluble reactant compounds correctly dissociated into aqueous ions with charges", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Precipitate retained as intact solid: {s['precip']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct explanation: precipitate is an insoluble solid crystal lattice, not free ions", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "split_solid_precipitate_into_ions", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Split every aqueous (aq) ionic compound into its ions; leave the solid (s) precipitate intact.",
        "concept": "Only soluble electrolytes exist as dissociated ions in solution. Precipitates remain as solid formula units.",
        "breakdown": f"Break up all (aq) salts into ions. Keep {s['precip']} as a solid.",
    }

    return make_science_question(
        prefix="ps10_aq_full_ionic",
        topic=TOPIC,
        subskill="19_full_ionic_equations_precipitation",
        learning_objective_id=f"{LO}_full_ionic",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["split_solid_into_aqueous_ions", "omitted_ionic_coefficients"],
        keywords=["full ionic equation", "complete ionic equation", "precipitation", "ions", "state symbols"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 20: Net Ionic Equations — Silver Halides
# --------------------------------------------------------------------------- #
def arch_20_net_ionic_equations_silver_halides(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    halide_data = [
        {"name": "chloride", "sym": r"\text{Cl}^-", "precip": r"\text{AgCl}(s)", "color": "white", "source": r"\text{NaCl}(aq)"},
        {"name": "bromide", "sym": r"\text{Br}^-", "precip": r"\text{AgBr}(s)", "color": "cream / pale yellow", "source": r"\text{KBr}(aq)"},
        {"name": "iodide", "sym": r"\text{I}^-", "precip": r"\text{AgI}(s)", "color": "yellow", "source": r"\text{KI}(aq)"},
    ]
    h = rng.choice(halide_data)

    prompt = (
        f"A learner adds a few drops of aqueous silver nitrate ($\\text{{AgNO}}_3$) to a test tube containing **{h['source']}**.\n"
        f"A **{h['color']}** precipitate forms immediately.\n\n"
        f"1. Write down the molecular equation for this reaction.\n"
        f"2. Write down the balanced **net ionic equation** for the formation of the precipitate. Include state symbols.\n"
        f"3. Name the spectator ions that remain in the solution."
    )

    molecular = rf"\text{{AgNO}}_3(aq) + {h['source']} \to {h['precip']} + \text{{KNO}}_3(aq)" if "K" in h["source"] else rf"\text{{AgNO}}_3(aq) + {h['source']} \to {h['precip']} + \text{{NaNO}}_3(aq)"
    net_ionic = rf"\text{{Ag}}^+(aq) + {h['sym']}(aq) \to {h['precip']}"
    spectators = "K⁺ and NO₃⁻" if "K" in h["source"] else "Na⁺ and NO₃⁻"

    ans_latex = net_ionic

    sample_answer = (
        f"1. Molecular equation:\n"
        f"   $${molecular}$$\n"
        f"2. Net ionic equation:\n"
        f"   $${net_ionic}$$\n"
        f"3. Spectator ions: **{spectators}**."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct balanced molecular equation with state symbols", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct net ionic equation: {net_ionic}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct spectator ions identified: {spectators}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "retained_spectator_ions_in_net_ionic", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The net ionic equation includes ONLY the ions that combine to form the insoluble precipitate.",
        "concept": "Cancel out the spectator ions (Na⁺/K⁺ and NO₃⁻) from both sides of the full ionic equation.",
        "breakdown": f"Ag⁺(aq) combines with {h['sym']}(aq) to precipitate {h['precip']}.",
    }

    return make_science_question(
        prefix="ps10_aq_net_ag",
        topic=TOPIC,
        subskill="20_net_ionic_equations_silver_halides",
        learning_objective_id=f"{LO}_net_silver_halides",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["left_spectators_in_net_ionic", "omitted_charges_in_net_ionic"],
        keywords=["net ionic equation", "silver halide", "silver chloride", "spectator ions", "precipitate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 21: Net Ionic Equations — Barium Sulphate
# --------------------------------------------------------------------------- #
def arch_21_net_ionic_equations_barium_sulphate(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ba_source, so4_source = rng.choice([
        (r"\text{BaCl}_2(aq)", r"\text{Na}_2\text{SO}_4(aq)"),
        (r"\text{Ba(NO}_3)_2(aq)", r"\text{K}_2\text{SO}_4(aq)"),
        (r"\text{BaCl}_2(aq)", r"\text{MgSO}_4(aq)"),
    ])

    prompt = (
        f"A chemist mixes aqueous solutions of **${ba_source}$** and **${so4_source}$**.\n"
        f"A dense white precipitate forms instantly.\n\n"
        f"1. Write down the chemical formula of the white precipitate.\n"
        f"2. Write down the balanced **net ionic equation** for this precipitation reaction. Include state symbols.\n"
        f"3. Explain why adding dilute nitric acid ($\\text{{HNO}}_3$) to this precipitate produces no visible reaction."
    )

    net_ionic = r"\text{Ba}^{2+}(aq) + \text{SO}_4^{2-}(aq) \to \text{BaSO}_4(s)"
    ans_latex = rf"\text{{Precipitate: }}\text{{BaSO}}_4(s); \quad {net_ionic}"

    sample_answer = (
        f"1. Precipitate formula: **$\\text{{BaSO}}_4(s)$** (barium sulphate).\n"
        f"2. Net ionic equation:\n"
        f"   $${net_ionic}$$\n"
        f"3. Barium sulphate is completely insoluble in dilute nitric acid because sulphate is the conjugate base of a strong acid "
        f"and does not protonate in acidic solution; hence, the precipitate remains unchanged."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct precipitate formula: BaSO4(s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct net ionic equation with state symbols: {net_ionic}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Accurate explanation: BaSO4 does not dissolve in dilute HNO3", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which ions react to form the precipitate? Ba²⁺ and SO₄²⁻.",
        "concept": "The net ionic equation shows only the reacting ions forming the solid. BaSO₄ is insoluble even in strong dilute acid.",
        "breakdown": f"Net ionic equation: Ba²⁺(aq) + SO₄²⁻(aq) -> BaSO₄(s). The precipitate is unaffected by dilute HNO₃.",
    }

    return make_science_question(
        prefix="ps10_aq_net_baso4",
        topic=TOPIC,
        subskill="21_net_ionic_equations_barium_sulphate",
        learning_objective_id=f"{LO}_net_baso4",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["included_counter_ions_in_net_ionic", "claimed_baso4_dissolves_in_acid"],
        keywords=["barium sulphate", "net ionic equation", "nitric acid test", "precipitate", "sulphate test"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 22: Net Ionic Equations — Transition Metal Hydroxides
# --------------------------------------------------------------------------- #
def arch_22_net_ionic_equations_transition_metal_hydroxides(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    metal_case = rng.choice([
        {
            "name": "copper(II) sulphate and sodium hydroxide",
            "cation": r"\text{Cu}^{2+}",
            "cat_coef": 1,
            "oh_coef": 2,
            "precip": r"\text{Cu(OH)}_2(s)",
            "color": "light blue",
            "net": r"\text{Cu}^{2+}(aq) + 2\text{OH}^-(aq) \to \text{Cu(OH)}_2(s)",
        },
        {
            "name": "iron(III) chloride and sodium hydroxide",
            "cation": r"\text{Fe}^{3+}",
            "cat_coef": 1,
            "oh_coef": 3,
            "precip": r"\text{Fe(OH)}_3(s)",
            "color": "reddish-brown (rust brown)",
            "net": r"\text{Fe}^{3+}(aq) + 3\text{OH}^-(aq) \to \text{Fe(OH)}_3(s)",
        },
        {
            "name": "iron(II) sulphate and sodium hydroxide",
            "cation": r"\text{Fe}^{2+}",
            "cat_coef": 1,
            "oh_coef": 2,
            "precip": r"\text{Fe(OH)}_2(s)",
            "color": "dirty green",
            "net": r"\text{Fe}^{2+}(aq) + 2\text{OH}^-(aq) \to \text{Fe(OH)}_2(s)",
        },
    ])

    prompt = (
        f"A learner adds dilute aqueous sodium hydroxide ($\\text{{NaOH}}$) dropwise to a solution of **{metal_case['name']}**.\n\n"
        f"1. Describe the visible colour change and precipitate observed.\n"
        f"2. Write down the balanced **net ionic equation** for this reaction. Include state symbols.\n"
        f"3. Name the spectator ions in this reaction."
    )

    ans_latex = rf"\text{{Colour: }}{metal_case['color']}; \quad {metal_case['net']}"

    sample_answer = (
        f"1. A gelatinous **{metal_case['color']}** precipitate of {metal_case['precip']} forms.\n"
        f"2. Balanced net ionic equation:\n"
        f"   $${metal_case['net']}$$\n"
        f"3. Spectator ions: **Na⁺** and **" + ("SO₄²⁻" if "sulphate" in metal_case["name"] else "Cl⁻") + "**."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct observable precipitate colour: {metal_case['color']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct net ionic equation with state symbols: {metal_case['net']}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Identification of spectator ions", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "How many OH⁻ ions balance the positive charge on the transition metal cation?",
        "concept": "Net ionic equation: metal cation(aq) + hydroxide anions(aq) -> metal hydroxide precipitate(s).",
        "breakdown": f"Net ionic equation: {metal_case['net']}. Observable colour: {metal_case['color']}.",
    }

    return make_science_question(
        prefix="ps10_aq_net_trans_hyd",
        topic=TOPIC,
        subskill="22_net_ionic_equations_transition_metal_hydroxides",
        learning_objective_id=f"{LO}_net_trans_hyd",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["wrong_stoichiometric_hydroxide_count", "confused_iron_ii_and_iii_colours"],
        keywords=["transition metal", "hydroxide precipitate", "copper hydroxide", "iron hydroxide", "net ionic equation"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 23: Qualitative Test for Chloride Anion
# --------------------------------------------------------------------------- #
def arch_23_qualitative_test_for_chloride_anion(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt_name = rng.choice(["sodium chloride", "potassium chloride", "calcium chloride", "ammonium chloride"])

    prompt = (
        f"A learner is given an unlabelled solution suspected of containing **{salt_name}**.\n"
        f"The learner performs the standard qualitative test for chloride ions ($\\text{{Cl}}^-$).\n\n"
        f"1. Name the primary reagent added to the test solution.\n"
        f"2. Describe the immediate observation upon adding this reagent.\n"
        f"3. Name the acid that must subsequently be added to confirm that the precipitate is a chloride and NOT a carbonate.\n"
        f"4. What is the observation after adding this acid if chloride ions are present?"
    )

    ans_latex = r"\text{Reagent: }\text{AgNO}_3(aq); \quad \text{Observation: White precipitate; Confirming Acid: }\text{HNO}_3; \quad \text{Observation: Precipitate remains}"

    sample_answer = (
        f"1. Primary reagent: **Aqueous silver nitrate** ($\\text{{AgNO}}_3$).\n"
        f"2. Observation: A **white precipitate** (silver chloride, $\\text{{AgCl}}$) forms immediately.\n"
        f"3. Confirming acid: **Dilute nitric acid** ($\\text{{HNO}}_3$). (Do NOT use hydrochloric acid as it contains chloride ions!).\n"
        f"4. Observation: The white precipitate **remains unchanged / does not dissolve**.\n"
        f"   (If carbonate were present, it would dissolve with effervescence releasing $\\text{{CO}}_2$ gas)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct primary reagent: silver nitrate / AgNO3(aq)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct observation: white precipitate forms", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct confirming acid: dilute nitric acid / HNO3", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Observation: precipitate does not dissolve / remains unchanged", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "suggested_adding_hcl_to_test_chloride", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which reagent forms an insoluble white precipitate with chloride ions?",
        "concept": "Ag⁺ + Cl⁻ -> AgCl(s) (white ppt). Ag₂CO₃ also precipitates white with Ag⁺, so dilute HNO₃ is added to rule out carbonate.",
        "breakdown": "Add AgNO₃(aq) -> white precipitate forms. Add dilute HNO₃ -> precipitate does not dissolve, confirming Cl⁻.",
    }

    return make_science_question(
        prefix="ps10_aq_test_chloride",
        topic=TOPIC,
        subskill="23_qualitative_test_for_chloride_anion",
        learning_objective_id=f"{LO}_test_chloride",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["suggested_hcl_for_chloride_acidification", "confused_chloride_with_carbonate"],
        keywords=["chloride test", "silver nitrate", "nitric acid", "white precipitate", "qualitative analysis"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 24: Qualitative Test for Bromide and Iodide
# --------------------------------------------------------------------------- #
def arch_24_qualitative_test_for_bromide_and_iodide(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    target_halide = rng.choice([
        {"ion": "bromide", "sym": r"\text{Br}^-", "ppt": r"\text{AgBr}", "ppt_col": "cream / pale yellow", "org_col": "orange / reddish-brown", "prod": r"\text{Br}_2"},
        {"ion": "iodide", "sym": r"\text{I}^-", "ppt": r"\text{AgI}", "ppt_col": "pale yellow / yellow", "org_col": "purple / violet", "prod": r"\text{I}_2"},
    ])

    prompt = (
        f"A laboratory technician wishes to confirm whether an unknown halide solution contains **{target_halide['ion']} ions** (${target_halide['sym']}$).\n\n"
        f"1. What precipitate colour forms when aqueous silver nitrate ($\\text{{AgNO}}_3$) is added to this solution?\n"
        f"2. To distinguish definitively between bromide and iodide, **chlorine water** ($\\text{{Cl}}_2(aq)$) and an organic solvent "
        f"(such as cyclohexane or $\\text{{CCl}}_4$) are added and the tube is shaken.\n"
        f"   - Describe the colour of the upper organic layer if {target_halide['ion']} is present.\n"
        f"   - Write down a balanced chemical equation for the reaction between {target_halide['sym']} and chlorine water."
    )

    eq = rf"2{target_halide['sym']}(aq) + \text{{Cl}}_2(aq) \to 2\text{{Cl}}^-(aq) + {target_halide['prod']}"
    ans_latex = rf"\text{{Precipitate: }}{target_halide['ppt_col']}; \quad \text{{Organic Layer: }}{target_halide['org_col']}; \quad {eq}"

    sample_answer = (
        f"1. Precipitate colour with $\\text{{AgNO}}_3$: **{target_halide['ppt_col']}** (${target_halide['ppt']}$).\n"
        f"2. (a) Colour of organic solvent layer: **{target_halide['org_col']}** (due to dissolved ${target_halide['prod']}$).\n"
        f"   (b) Balanced chemical equation:\n"
        f"   $${eq}$$\n"
        f"   (Chlorine is a stronger oxidising agent than {target_halide['ion']} and oxidises it to elemental {target_halide['prod']})."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct silver halide precipitate colour: {target_halide['ppt_col']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct organic solvent colour: {target_halide['org_col']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct balanced redox displacement equation: {eq}", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Chlorine water displaces less reactive halogens. What colour is dissolved bromine vs dissolved iodine?",
        "concept": "Bromine (Br₂) turns non-polar organic solvents orange-brown. Iodine (I₂) turns non-polar organic solvents purple/violet.",
        "breakdown": f"AgNO₃ produces {target_halide['ppt_col']} {target_halide['ppt']}. Chlorine water oxidises {target_halide['sym']} to {target_halide['prod']}, colouring the organic layer {target_halide['org_col']}.",
    }

    return make_science_question(
        prefix="ps10_aq_test_br_i",
        topic=TOPIC,
        subskill="24_qualitative_test_for_bromide_and_iodide",
        learning_objective_id=f"{LO}_test_br_i",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_bromine_and_iodine_organic_colours", "incorrect_halogen_displacement_equation"],
        keywords=["bromide", "iodide", "chlorine water", "organic layer", "halogen displacement", "qualitative test"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 25: Qualitative Test for Sulphate Anion
# --------------------------------------------------------------------------- #
def arch_25_qualitative_test_for_sulphate_anion(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    test_salt = rng.choice(["sodium sulphate", "potassium sulphate", "zinc sulphate", "magnesium sulphate"])

    prompt = (
        f"A learner conducts an experiment to test an unknown aqueous solution of **{test_salt}** for the presence of **sulphate ions** ($\\text{{SO}}_4^{{2-}}$).\n\n"
        f"1. Name the primary reagent added to the test solution to form a precipitate.\n"
        f"2. State the formula and colour of the precipitate formed.\n"
        f"3. Name the acid added in the second step to confirm that the precipitate is a sulphate and NOT a carbonate or sulphite.\n"
        f"4. State the observation after the acid is added."
    )

    ans_latex = r"\text{Reagent: }\text{BaCl}_2(aq); \quad \text{Precipitate: }\text{BaSO}_4\text{ (white)}; \quad \text{Acid: Dilute }\text{HNO}_3\text{ (or HCl)}; \quad \text{Observation: Precipitate remains}"

    sample_answer = (
        f"1. Primary reagent: **Barium chloride solution** ($\\text{{BaCl}}_2(aq)$) or barium nitrate solution ($\\text{{Ba(NO}}_3)_2(aq)$).\n"
        f"2. Precipitate: **$\\text{{BaSO}}_4$** (white precipitate).\n"
        f"3. Acid: **Dilute nitric acid** ($\\text{{HNO}}_3$) or dilute hydrochloric acid ($\\text{{HCl}}$).\n"
        f"4. Observation: The white precipitate **does NOT dissolve / remains unchanged**.\n"
        f"   (If carbonate or sulphite were present, the precipitate would dissolve with effervescence)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct reagent: barium chloride / BaCl2(aq) or barium nitrate", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula and colour: BaSO4, white precipitate", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Confirming acid: dilute nitric acid / dilute hydrochloric acid", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Observation: precipitate does not dissolve / remains insoluble", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "suggested_sulfuric_acid_for_acidification", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which barium salt is completely insoluble in dilute acid?",
        "concept": "Ba²⁺ + SO₄²⁻ -> BaSO₄(s) (white ppt). BaSO₄ is insoluble in dilute acid, whereas BaCO₃ dissolves.",
        "breakdown": "Add BaCl₂ -> white precipitate (BaSO₄). Add dilute HNO₃ -> precipitate does not dissolve, confirming sulphate.",
    }

    return make_science_question(
        prefix="ps10_aq_test_sulphate",
        topic=TOPIC,
        subskill="25_qualitative_test_for_sulphate_anion",
        learning_objective_id=f"{LO}_test_sulphate",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["suggested_sulfuric_acid_to_acidify_sulphate_test", "confused_sulphate_with_sulphite"],
        keywords=["sulphate test", "barium chloride", "barium sulphate", "nitric acid", "white precipitate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Export Mapping for Archetypes 01 to 25
# --------------------------------------------------------------------------- #
BUILDERS_01_25 = {
    "01_water_dipole_molecular_polarity": arch_01_water_dipole_molecular_polarity,
    "02_hydration_mechanism_ionic_lattice": arch_02_hydration_mechanism_ionic_lattice,
    "03_dissociation_single_charge_salts": arch_03_dissociation_single_charge_salts,
    "04_dissociation_multivalent_cation_salts": arch_04_dissociation_multivalent_cation_salts,
    "05_dissociation_polyatomic_anion_salts": arch_05_dissociation_polyatomic_anion_salts,
    "06_dissociation_vs_ionisation": arch_06_dissociation_vs_ionisation,
    "07_dissolution_covalent_molecular_substances": arch_07_dissolution_covalent_molecular_substances,
    "08_electrolyte_definition_classification": arch_08_electrolyte_definition_classification,
    "09_conductivity_apparatus_circuit_interpretation": arch_09_conductivity_apparatus_circuit_interpretation,
    "10_conductivity_factors_ion_concentration": arch_10_conductivity_factors_ion_concentration,
    "11_conductivity_factors_ion_charge_and_count": arch_11_conductivity_factors_ion_charge_and_count,
    "12_conductivity_factors_weak_vs_strong_electrolytes": arch_12_conductivity_factors_weak_vs_strong_electrolytes,
    "13_ion_concentration_calculation_from_molarity": arch_13_ion_concentration_calculation_from_molarity,
    "14_precipitation_definition_driving_force": arch_14_precipitation_definition_driving_force,
    "15_solubility_rules_halides": arch_15_solubility_rules_halides,
    "16_solubility_rules_sulphates": arch_16_solubility_rules_sulphates,
    "17_solubility_rules_carbonates_hydroxides": arch_17_solubility_rules_carbonates_hydroxides,
    "18_spectator_ions_identification": arch_18_spectator_ions_identification,
    "19_full_ionic_equations_precipitation": arch_19_full_ionic_equations_precipitation,
    "20_net_ionic_equations_silver_halides": arch_20_net_ionic_equations_silver_halides,
    "21_net_ionic_equations_barium_sulphate": arch_21_net_ionic_equations_barium_sulphate,
    "22_net_ionic_equations_transition_metal_hydroxides": arch_22_net_ionic_equations_transition_metal_hydroxides,
    "23_qualitative_test_for_chloride_anion": arch_23_qualitative_test_for_chloride_anion,
    "24_qualitative_test_for_bromide_and_iodide": arch_24_qualitative_test_for_bromide_and_iodide,
    "25_qualitative_test_for_sulphate_anion": arch_25_qualitative_test_for_sulphate_anion,
}
