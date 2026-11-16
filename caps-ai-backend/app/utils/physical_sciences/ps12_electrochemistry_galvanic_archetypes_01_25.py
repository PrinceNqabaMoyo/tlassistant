"""Physical Sciences (Grade 12 Term 3) — Electrochemical Reactions Archetypes 01 to 25.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Topic: Electrochemical Reactions (Galvanic / Voltaic Cells).
- Subskills 01–25: Galvanic foundations, standard conditions (298 K, 1 mol/dm^3, 101,3 kPa),
  Standard Hydrogen Electrode (SHE, E0 = 0,00 V), Anode (oxidation, negative) vs
  Cathode (reduction, positive), electron flow in external circuit, Standard Reduction Potentials
  (Table 4A / 4B), predicting spontaneity, Daniell cell (Zn-Cu), Mg-Cu, Al-Cu, Ni-Ag, Pb-Ag pairs,
  standard cell notation, inert platinum electrodes, E0_cell = E0_cathode - E0_anode,
  concentration effects via Le Chatelier, electrode surface area, equilibrium E_cell = 0 V,
  electrode mass stoichiometry, Faraday charge and current, and halogen half-cells.

100% deterministic, math backed, zero-LLM, compliant with 6-pillar contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

FARADAY_CONST = 96500  # C/mol e-

STANDARD_REDUCTION_DATA: Dict[str, Dict[str, Any]] = {
    "Li": {"symbol": "Li", "name": "lithium", "e0": -3.05, "charge": 1, "molar_mass": 6.94},
    "K": {"symbol": "K", "name": "potassium", "e0": -2.93, "charge": 1, "molar_mass": 39.10},
    "Ca": {"symbol": "Ca", "name": "calcium", "e0": -2.87, "charge": 2, "molar_mass": 40.08},
    "Na": {"symbol": "Na", "name": "sodium", "e0": -2.71, "charge": 1, "molar_mass": 22.99},
    "Mg": {"symbol": "Mg", "name": "magnesium", "e0": -2.37, "charge": 2, "molar_mass": 24.31},
    "Al": {"symbol": "Al", "name": "aluminium", "e0": -1.66, "charge": 3, "molar_mass": 26.98},
    "Mn": {"symbol": "Mn", "name": "manganese", "e0": -1.18, "charge": 2, "molar_mass": 54.94},
    "Zn": {"symbol": "Zn", "name": "zinc", "e0": -0.76, "charge": 2, "molar_mass": 65.38},
    "Cr": {"symbol": "Cr", "name": "chromium", "e0": -0.74, "charge": 3, "molar_mass": 52.00},
    "Fe": {"symbol": "Fe", "name": "iron", "e0": -0.44, "charge": 2, "molar_mass": 55.85},
    "Cd": {"symbol": "Cd", "name": "cadmium", "e0": -0.40, "charge": 2, "molar_mass": 112.41},
    "Ni": {"symbol": "Ni", "name": "nickel", "e0": -0.27, "charge": 2, "molar_mass": 58.69},
    "Sn": {"symbol": "Sn", "name": "tin", "e0": -0.14, "charge": 2, "molar_mass": 118.71},
    "Pb": {"symbol": "Pb", "name": "lead", "e0": -0.13, "charge": 2, "molar_mass": 207.20},
    "H2": {"symbol": "H2", "name": "hydrogen", "e0": 0.00, "charge": 1, "molar_mass": 1.01},
    "Cu": {"symbol": "Cu", "name": "copper", "e0": 0.34, "charge": 2, "molar_mass": 63.55},
    "I2": {"symbol": "I2", "name": "iodine", "e0": 0.54, "charge": 1, "molar_mass": 126.90},
    "Ag": {"symbol": "Ag", "name": "silver", "e0": 0.80, "charge": 1, "molar_mass": 107.87},
    "Br2": {"symbol": "Br2", "name": "bromine", "e0": 1.07, "charge": 1, "molar_mass": 79.90},
    "Pt": {"symbol": "Pt", "name": "platinum", "e0": 1.20, "charge": 2, "molar_mass": 195.08},
    "Cl2": {"symbol": "Cl2", "name": "chlorine", "e0": 1.36, "charge": 1, "molar_mass": 35.45},
    "Au": {"symbol": "Au", "name": "gold", "e0": 1.50, "charge": 3, "molar_mass": 196.97},
}


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Format number with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and abs(val - round(val)) < 1e-6):
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _clean_svg(svg: str) -> str:
    return svg.strip()


# Archetype 01: Galvanic cell definition and energy conversion
def _b01_galvanic_cell_definition_energy_conversion(r: random.Random) -> Dict[str, Any]:
    metal_a, metal_c = r.choice([("Zn", "Cu"), ("Mg", "Cu"), ("Al", "Ag"), ("Ni", "Ag")])
    e0_a = STANDARD_REDUCTION_DATA[metal_a]["e0"]
    e0_c = STANDARD_REDUCTION_DATA[metal_c]["e0"]
    ecell = round(e0_c - e0_a, 2)

    prompt = (
        f"A laboratory galvanic cell is constructed by coupling a ${_fmt_sa(e0_a)}\\text{{ V}}$ half-cell "
        f"({STANDARD_REDUCTION_DATA[metal_a]['name']}) with a ${_fmt_sa(e0_c)}\\text{{ V}}$ half-cell "
        f"({STANDARD_REDUCTION_DATA[metal_c]['name']}) using a voltmeter in the external circuit.\n\n"
        f"1. Define a **galvanic (voltaic) cell** in words.\n"
        f"2. State the energy conversion that takes place inside an operating galvanic cell.\n"
        f"3. State whether the overall chemical reaction occurring in this cell is **spontaneous** or **non-spontaneous**.\n"
        f"4. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$) of this cell."
    )

    ans_latex = (
        rf"1.\; \text{{A cell in which chemical energy is converted to electrical energy as a result of self-sustaining (spontaneous) chemical reactions.}}\n"
        rf"2.\; \text{{Chemical energy is converted into electrical energy.}}\n"
        rf"3.\; \text{{Spontaneous (self-sustaining).}}\n"
        rf"4.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\text{{ V}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of galvanic cell", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Energy conversion: chemical to electrical energy", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Spontaneous reaction identification", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation of standard EMF: {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_volts", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Galvanic cells convert chemical energy into electrical energy spontaneously.",
        "tier_2": "Calculate $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$ where cathode has the higher potential.",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_01_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_01_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "01_galvanic_cell_definition_energy_conversion",
        "learning_objective_id": "ps12_ec_01_definition",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_galvanic_with_electrolytic_energy_conversion", "assumed_galvanic_reactions_are_non_spontaneous"],
        "keywords": ["galvanic cell", "energy conversion", "spontaneous", "cell potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 02: Standard conditions for galvanic cells
def _b02_standard_conditions_galvanic_cells(r: random.Random) -> Dict[str, Any]:
    temp_c = r.choice([20, 25, 30])
    conc_val = r.choice([0.5, 1.0, 1.5, 2.0])
    is_standard = (temp_c == 25 and conc_val == 1.0)

    prompt = (
        f"A laboratory technician measures the potential of a zinc-copper electrochemical cell under the following conditions:\n"
        f"- Temperature: ${temp_c}^\\circ\\text{{C}}$\n"
        f"- Electrolyte concentrations: $[\\text{{Zn}}^{{2+}}] = {_fmt_sa(conc_val)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ "
        f"and $[\\text{{Cu}}^{{2+}}] = 1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
        f"- Atmospheric pressure: $101{{,}}3\\text{{ kPa}}$\n\n"
        f"1. State the **three standard conditions** under which standard electrode potentials ($E^\\circ$) are tabulated.\n"
        f"2. State whether the technician's cell is currently operating under standard conditions. Give a clear reason.\n"
        f"3. State the standard unit symbol used to indicate standard state conditions in $E^\\circ$."
    )

    std_check_text = (
        r"\text{Yes, all conditions match standard specifications (25}^\circ\text{C, 1,0 mol}\cdot\text{dm}^{-3}\text{, and 101,3 kPa).}"
        if is_standard
        else rf"\text{{No, because the temperature is }}{temp_c}^\circ\text{{C (standard is 25}}^\circ\text{{C or 298 K) and/or the concentration of Zn}}^{{2+}}\text{{ is }}{_fmt_sa(conc_val)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}\text{{ (standard is 1,0 mol}}\cdot\text{{dm}}^{{-3}}\text{{).}}"
    )

    ans_latex = (
        rf"1.\; \text{{(i) Temperature of }} 25^\circ\text{{C}} \; (298\text{{ K}}).\n"
        rf"\quad \text{{(ii) Solute concentration of }} 1{{,}}0\text{{ mol}}\cdot\text{{dm}}^{{-3}} \; (1\text{{ M}}).\n"
        rf"\quad \text{{(iii) Pressure of gases at }} 101{{,}}3\text{{ kPa}} \; (1\text{{ atm}}).\n"
        rf"2.\; {std_check_text}\n"
        rf"3.\; \text{{The standard degree symbol (}}^\circ\text{{) as in }} E^\circ."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Standard temperature: 25 deg C / 298 K", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Standard concentration: 1.0 mol/dm^3", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Standard pressure: 101.3 kPa (for gases)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Accurate standard condition assessment with valid reason", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Standard state superscript symbol identification", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_temperature_or_concentration", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Standard conditions are: $T = 25^\\circ\\text{C}$ ($298\\text{ K}$), $c = 1{,}0\\text{ mol}\\cdot\\text{dm}^{-3}$, $p = 101{,}3\\text{ kPa}$.",
        "tier_2": f"Compare the given temperature ({temp_c} °C) and concentration ({conc_val} mol/dm^3) with the standard values.",
        "tier_3": f"Condition standard assessment: {std_check_text}",
    }

    return {
        "id": f"ps12_ec_02_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_02_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "02_standard_conditions_galvanic_cells",
        "learning_objective_id": "ps12_ec_02_standard_conditions",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_stp_0_deg_c_instead_of_25_deg_c", "forgot_gas_pressure_condition"],
        "keywords": ["standard conditions", "298 K", "1 mol/dm3", "101.3 kPa"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 03: Standard Hydrogen Electrode (SHE) reference
def _b03_standard_hydrogen_electrode_she_reference(r: random.Random) -> Dict[str, Any]:
    tested_metal = r.choice(["Zn", "Cu", "Mg", "Ag", "Pb", "Ni"])
    m_data = STANDARD_REDUCTION_DATA[tested_metal]
    m_name = m_data["name"]
    m_e0 = m_data["e0"]

    prompt = (
        f"A Standard Hydrogen Electrode (SHE) is connected to a standard half-cell containing a strip of "
        f"{m_name} ({m_data['symbol']}) immersed in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ solution "
        f"of its nitrate salt at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Write down the reduction half-reaction occurring at the Standard Hydrogen Electrode.\n"
        f"2. State the assigned standard reduction potential ($E^\\circ$) of the SHE in volts.\n"
        f"3. Explain the two essential roles of the platinized platinum ($\\text{{Pt}}$) foil used in the SHE.\n"
        f"4. If the voltmeter reads ${_fmt_sa(abs(m_e0))}\\text{{ V}}$, state whether the {m_name} electrode acts as the "
        f"**anode** or **cathode** in this setup."
    )

    role_text = "cathode" if m_e0 > 0 else "anode"

    ans_latex = (
        rf"1.\; 2\text{{H}}^+(aq) + 2e^- \rightleftharpoons \text{{H}}_2(g)\n"
        rf"2.\; E^\circ = 0{{,}}00\text{{ V}}\n"
        rf"3.\; \text{{(i) Provides an inert electrical conductor to transfer electrons without reacting.}}\n"
        rf"\quad \text{{(ii) Serves as a catalytic surface for the adsorption and dissociation of }} \text{{H}}_2(g).\n"
        rf"4.\; \text{{Since }} E^\circ({m_data['symbol']}) = {_fmt_sa(m_e0)}\text{{ V}}, \text{{ the {m_name} electrode acts as the }} \mathbf{{{role_text}}}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "SHE half-reaction: 2H+ + 2e- <=> H2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Assigned potential: 0.00 V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Role of Pt: inert conductor and catalyst surface", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Identification of role: {role_text}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_platinum_catalytic_function", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The standard reduction potential of the SHE is defined as $0{,}00\\text{ V}$.",
        "tier_2": "Platinum is chemically inert (does not react) and provides a high surface area to catalyze electron transfer.",
        "tier_3": f"For {m_name}, $E^\\circ = {_fmt_sa(m_e0)}\\text{{ V}}$, so it is the {role_text}.",
    }

    return {
        "id": f"ps12_ec_03_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_03_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "03_standard_hydrogen_electrode_she_reference",
        "learning_objective_id": "ps12_ec_03_she_reference",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_platinum_participates_in_redox_reaction", "confused_she_potential_with_cell_potential"],
        "keywords": ["Standard Hydrogen Electrode", "SHE", "platinum foil", "0.00 V"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 04: Anode and cathode definitions in redox
def _b04_anode_and_cathode_definitions_redox(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Ag"), ("Al", "Cu"), ("Pb", "Ag")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]

    prompt = (
        f"A standard galvanic cell is assembled using a {anode_data['name']} electrode and a {cath_data['name']} electrode.\n\n"
        f"1. Define the **anode** of an electrochemical cell in terms of the redox process taking place.\n"
        f"2. Define the **cathode** of an electrochemical cell in terms of the redox process taking place.\n"
        f"3. State the electrical polarity (positive or negative) of the anode and cathode in this **galvanic cell**.\n"
        f"4. Identify which electrode is the anode and which is the cathode for the {anode_sym}–{cath_sym} cell."
    )

    ans_latex = (
        rf"1.\; \text{{The anode is the electrode where oxidation takes place (loss of electrons).}}\n"
        rf"2.\; \text{{The cathode is the electrode where reduction takes place (gain of electrons).}}\n"
        rf"3.\; \text{{In a galvanic cell: Anode is negative (-); Cathode is positive (+).}}\n"
        rf"4.\; \text{{Anode: }} \text{{{anode_sym}}} \; (E^\circ = {_fmt_sa(anode_data['e0'])}\text{{ V}});\quad \text{{Cathode: }} \text{{{cath_sym}}} \; (E^\circ = {_fmt_sa(cath_data['e0'])}\text{{ V}})."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of anode (site of oxidation)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Definition of cathode (site of reduction)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Galvanic polarities: Anode negative, Cathode positive", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Identification of {anode_sym} as anode", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Identification of {cath_sym} as cathode", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "inverted_anode_cathode_definitions", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Remember the mnemonic: 'An Ox' (Anode = Oxidation) and 'Red Cat' (Reduction = Cathode).",
        "tier_2": "In a galvanic cell, oxidation releases electrons at the anode, making it the negative terminal.",
        "tier_3": f"Anode = {anode_sym} (negative); Cathode = {cath_sym} (positive).",
    }

    return {
        "id": f"ps12_ec_04_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_04_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "04_anode_and_cathode_definitions_redox",
        "learning_objective_id": "ps12_ec_04_anode_cathode_def",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_anode_charge_with_positive_sign", "swapped_oxidation_and_reduction_sites"],
        "keywords": ["anode", "cathode", "oxidation", "reduction", "polarity"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 05: Electron flow direction in external circuit
def _b05_electron_flow_direction_external_circuit(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Pb"), ("Fe", "Ag"), ("Ni", "Cu")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]

    prompt = (
        f"An operating galvanic cell consists of a {anode_data['name']} ({anode_sym}) half-cell and a "
        f"{cath_data['name']} ({cath_sym}) half-cell connected by a conductive wire through an ammeter and a salt bridge.\n\n"
        f"1. State the direction in which **electrons** flow through the external wire (from which electrode to which electrode).\n"
        f"2. Explain why electrons travel in this specific direction based on oxidation and reduction half-reactions.\n"
        f"3. Distinguish between the direction of electron flow and the direction of **conventional current** in the external circuit.\n"
        f"4. State whether electrons travel through the liquid electrolyte or salt bridge."
    )

    ans_latex = (
        rf"1.\; \text{{Electrons flow from the }} \text{{{anode_sym}}} \text{{ (anode) electrode to the }} \text{{{cath_sym}}} \text{{ (cathode) electrode.}}\n"
        rf"2.\; \text{{Oxidation occurs at the }} \text{{{anode_sym}}} \text{{ anode, liberating electrons. Reduction at the }} \text{{{cath_sym}}} \text{{ cathode consumes electrons, creating a potential difference that drives electrons from anode to cathode.}}\n"
        rf"3.\; \text{{Conventional current flows in the opposite direction: from cathode (positive) to anode (negative).}}\n"
        rf"4.\; \text{{No, electrons do not travel through electrolytes or salt bridges; charge in solutions is carried exclusively by ions.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Electron flow from {anode_sym} to {cath_sym}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Redox justification (liberation at anode, consumption at cathode)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Conventional current contrast statement", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Clarification: ions carry charge in solution, zero electrons in solution", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_electrons_flow_through_salt_bridge", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Electrons are released at the anode (oxidation) and travel through the wire to the cathode (reduction).",
        "tier_2": "Conventional current is defined as the flow of positive charge, so it flows opposite to electron flow.",
        "tier_3": f"Wire: {anode_sym} $\\to$ {cath_sym}. Solution: ions carry charge, not electrons.",
    }

    return {
        "id": f"ps12_ec_05_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_05_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "05_electron_flow_direction_external_circuit",
        "learning_objective_id": "ps12_ec_05_electron_flow",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["believed_electrons_travel_through_salt_bridge", "confused_electron_flow_with_conventional_current"],
        "keywords": ["electron flow", "external circuit", "conventional current", "anode to cathode"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 06: Table of standard reduction potentials interpretation
def _b06_table_of_standard_reduction_potentials_table_4a_4b(r: random.Random) -> Dict[str, Any]:
    species = r.sample(["F2", "Cl2", "Ag", "Cu", "Pb", "Zn", "Mg", "Na"], 4)
    # sort by E0
    sorted_s = sorted(species, key=lambda s: STANDARD_REDUCTION_DATA[s]["e0"])
    weakest_ox = sorted_s[0]
    strongest_ox = sorted_s[-1]

    prompt = (
        f"Consider the following four chemical species listed with their standard reduction potentials from Table 4A/4B:\n"
        f"- ${sorted_s[0]}\\text{{ / ion pair}}: E^\\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[sorted_s[0]]['e0'])}\\text{{ V}}$\n"
        f"- ${sorted_s[1]}\\text{{ / ion pair}}: E^\\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[sorted_s[1]]['e0'])}\\text{{ V}}$\n"
        f"- ${sorted_s[2]}\\text{{ / ion pair}}: E^\\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[sorted_s[2]]['e0'])}\\text{{ V}}$\n"
        f"- ${sorted_s[3]}\\text{{ / ion pair}}: E^\\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[sorted_s[3]]['e0'])}\\text{{ V}}$\n\n"
        f"1. State which of these species is the **strongest oxidizing agent**.\n"
        f"2. State which of these species is the **strongest reducing agent**.\n"
        f"3. Explain how the magnitude and sign of $E^\\circ$ indicates the tendency of a species to gain electrons."
    )

    ans_latex = (
        rf"1.\; \text{{Strongest oxidizing agent: }} \mathbf{{{strongest_ox}}} \text{{ (has the most positive }} E^\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[strongest_ox]['e0'])}\text{{ V}}).\n"
        rf"2.\; \text{{Strongest reducing agent: }} \mathbf{{{weakest_ox}}} \text{{ (has the most negative }} E^\circ = {_fmt_sa(STANDARD_REDUCTION_DATA[weakest_ox]['e0'])}\text{{ V}}).\n"
        rf"3.\; \text{{A more positive }} E^\circ \text{{ value indicates a greater tendency to be reduced (gain electrons), making the reactant a stronger oxidizing agent. A more negative }} E^\circ \text{{ indicates greater tendency to be oxidized (lose electrons).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Strongest oxidizing agent: {strongest_ox}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Strongest reducing agent: {weakest_ox}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explanation of E0 sign and electron affinity", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "inverted_oxidizing_and_reducing_agents", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The most positive $E^\\circ$ is the strongest oxidizing agent (most readily gains electrons).",
        "tier_2": "The most negative $E^\\circ$ is the strongest reducing agent (most readily loses electrons).",
        "tier_3": f"Strongest oxidizing agent = {strongest_ox}, Strongest reducing agent = {weakest_ox}.",
    }

    return {
        "id": f"ps12_ec_06_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_06_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "06_table_of_standard_reduction_potentials_table_4a_4b",
        "learning_objective_id": "ps12_ec_06_table_interpretation",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_oxidizing_agent_with_reducing_agent", "assumed_negative_e0_means_non_reactive"],
        "keywords": ["Table 4A", "reduction potentials", "oxidizing agent", "reducing agent"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 07: Predicting spontaneity from reduction potentials
def _b07_predicting_spontaneity_from_reduction_potentials(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Fe"), ("Sn", "Ag"), ("Ni", "Pb")])
    anode_sym, cath_sym = pair
    e0_anode = STANDARD_REDUCTION_DATA[anode_sym]["e0"]
    e0_cath = STANDARD_REDUCTION_DATA[cath_sym]["e0"]
    ecell_fwd = round(e0_cath - e0_anode, 2)

    reverse_prompt = r.choice([True, False])
    if reverse_prompt:
        tested_reaction = f"\\text{{{cath_sym}}}(s) + \\text{{{anode_sym}}}^{{2+}}(aq) \\to \\text{{{cath_sym}}}^{{2+}}(aq) + \\text{{{anode_sym}}}(s)"
        spontaneous = False
        calculated_e0 = round(e0_anode - e0_cath, 2)
    else:
        tested_reaction = f"\\text{{{anode_sym}}}(s) + \\text{{{cath_sym}}}^{{2+}}(aq) \\to \\text{{{anode_sym}}}^{{2+}}(aq) + \\text{{{cath_sym}}}(s)"
        spontaneous = True
        calculated_e0 = ecell_fwd

    prompt = (
        f"Consider the chemical equation:\n"
        f"$${tested_reaction}$$\n"
        f"Given standard reduction potentials: $E^\\circ(\\text{{{anode_sym}}}^{{2+}}/\\text{{{anode_sym}}}) = {_fmt_sa(e0_anode)}\\text{{ V}}$ "
        f"and $E^\\circ(\\text{{{cath_sym}}}^{{2+}}/\\text{{{cath_sym}}}) = {_fmt_sa(e0_cath)}\\text{{ V}}$.\n\n"
        f"1. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$) for the reaction as written.\n"
        f"2. Use your calculated value to state whether the reaction is **spontaneous** or **non-spontaneous** under standard conditions.\n"
        f"3. State the universal thermodynamic criterion relating the sign of $E^\\circ_{{\\text{{cell}}}}$ to spontaneity."
    )

    ans_latex = (
        rf"1.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{reduction}}}} - E^\circ_{{\text{{oxidation}}}} = {_fmt_sa(calculated_e0)}\text{{ V}}\n"
        rf"2.\; \text{{The reaction is }} \mathbf{{{('spontaneous' if spontaneous else 'non-spontaneous')}}}.\n"
        rf"3.\; \text{{A reaction is spontaneous under standard conditions if and only if }} E^\circ_{{\text{{cell}}}} > 0\text{{ (positive). If }} E^\circ_{{\text{{cell}}}} < 0\text{{, it is non-spontaneous.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculation of E0_cell: {_fmt_sa(calculated_e0)} V", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Spontaneity conclusion: {'spontaneous' if spontaneous else 'non-spontaneous'}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Criterion statement: E0_cell > 0 implies spontaneous", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_in_ecell_calculation", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$.",
        "tier_2": "If $E^\\circ_{\\text{cell}} > 0$, the reaction is spontaneous. If $E^\\circ_{\\text{cell}} < 0$, it is non-spontaneous.",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(calculated_e0)}\\text{{ V}} \\implies$ {'spontaneous' if spontaneous else 'non-spontaneous'}.",
    }

    return {
        "id": f"ps12_ec_07_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_07_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "07_predicting_spontaneity_from_reduction_potentials",
        "learning_objective_id": "ps12_ec_07_spontaneity",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_all_reactions_in_tables_are_spontaneous", "subtracted_potentials_in_wrong_order"],
        "keywords": ["spontaneity", "cell potential", "Table 4A", "E_cell > 0"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 08: Daniell cell Zn-Cu reactions and observations
def _b08_daniell_cell_zn_cu_reactions_and_observations(r: random.Random) -> Dict[str, Any]:
    e0_zn = -0.76
    e0_cu = 0.34
    ecell = 1.10
    initial_zn_mass = r.choice([15.0, 20.0, 25.0, 30.0, 35.0])

    prompt = (
        f"A standard Daniell cell operates using a zinc electrode (initial mass: {_fmt_sa(initial_zn_mass)}\\text{{ g}}) in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{ZnSO}}_4$ solution "
        f"and a copper electrode in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{CuSO}}_4$ solution ($25^\\circ\\text{{C}}$).\n\n"
        f"1. Write down the oxidation half-reaction occurring at the anode.\n"
        f"2. Write down the reduction half-reaction occurring at the cathode.\n"
        f"3. Write down the overall balanced cell reaction.\n"
        f"4. State whether the zinc electrode's mass increases or decreases during cell discharge, and explain why.\n"
        f"5. State what happens to the intensity of the blue colour in the copper(II) sulfate electrolyte."
    )

    ans_latex = (
        rf"1.\; \text{{Oxidation (anode): }} \text{{Zn}}(s) \to \text{{Zn}}^{{2+}}(aq) + 2e^-\n"
        rf"2.\; \text{{Reduction (cathode): }} \text{{Cu}}^{{2+}}(aq) + 2e^- \to \text{{Cu}}(s)\n"
        rf"3.\; \text{{Overall cell reaction: }} \text{{Zn}}(s) + \text{{Cu}}^{{2+}}(aq) \to \text{{Zn}}^{{2+}}(aq) + \text{{Cu}}(s)\n"
        rf"4.\; \text{{The zinc electrode decreases in mass from its initial }}{_fmt_sa(initial_zn_mass)}\text{{ g because solid zinc is oxidized into aqueous }}\text{{Zn}}^{{2+}}\text{{ ions. (The copper cathode increases in mass as }}\text{{Cu}}^{{2+}}\text{{ precipitates as copper metal).}}\n"
        rf"5.\; \text{{The blue colour fades (becomes lighter) because }} \text{{Cu}}^{{2+}}(aq) \text{{ ions are consumed.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidation half-reaction: Zn -> Zn2+ + 2e-", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reduction half-reaction: Cu2+ + 2e- -> Cu", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Balanced overall reaction: Zn + Cu2+ -> Zn2+ + Cu", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Zinc electrode mass decreases", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Copper electrode mass increases", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Blue colour fades due to Cu2+ consumption", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_charges_on_ions", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Zinc is oxidized to $\\text{Zn}^{2+}$, and $\\text{Cu}^{2+}$ is reduced to metallic copper.",
        "tier_2": "Because $\\text{Cu}^{2+}$ ions give the solution its blue colour, consuming them causes the colour to fade.",
        "tier_3": "Overall: $\\text{Zn} + \\text{Cu}^{2+} \\to \\text{Zn}^{2+} + \\text{Cu}$. Zinc loses mass; copper gains mass.",
    }

    return {
        "id": f"ps12_ec_08_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_08_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "08_daniell_cell_zn_cu_reactions_and_observations",
        "learning_objective_id": "ps12_ec_08_daniell_cell",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_oxidation_and_reduction_half_reactions", "thought_zinc_electrode_gains_mass"],
        "keywords": ["Daniell cell", "zinc copper", "half-reactions", "colour fading"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 09: Mg-Cu galvanic cell high potential pair
def _b09_mg_cu_galvanic_cell_high_potential_pair(r: random.Random) -> Dict[str, Any]:
    e0_mg = -2.37
    e0_cu = 0.34
    ecell = round(e0_cu - e0_mg, 2)

    mg_mass = r.choice([2.4, 4.8, 7.2, 9.6, 12.0])
    moles_mg = round(mg_mass / 24.3, 3)

    prompt = (
        f"A galvanic cell is set up using a magnesium electrode in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{Mg(NO}}_3)_2$ solution "
        f"and a copper electrode in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{CuSO}}_4$ solution under standard conditions.\n\n"
        f"1. Identify the reducing agent in this cell reaction.\n"
        f"2. Write down the balanced equation for the spontaneous cell reaction.\n"
        f"3. Calculate the standard electromotive force ($E^\\circ_{{\\text{{cell}}}}$) of the cell.\n"
        f"4. Explain why this cell delivers a substantially higher potential than the standard Daniell ($\\text{{Zn}}-\\text{{Cu}}$) cell.\n"
        f"5. If {_fmt_sa(mg_mass)}\\text{{ g}} of magnesium reacts completely, calculate the moles of electrons transferred through the external circuit ($M(\\text{{Mg}}) = 24{{,}}3\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{Reducing agent: }} \text{{Mg}}(s)\n"
        rf"2.\; \text{{Mg}}(s) + \text{{Cu}}^{{2+}}(aq) \to \text{{Mg}}^{{2+}}(aq) + \text{{Cu}}(s)\n"
        rf"3.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = 0{{,}}34 - (-2{{,}}37) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"4.\; \text{{Magnesium has a much more negative standard reduction potential (}}-2{{,}}37\text{{ V) than zinc (}}-0{{,}}76\text{{ V), meaning magnesium is a far stronger reducing agent, resulting in a larger difference in electrode potentials.}}\n"
        rf"5.\; n(\text{{Mg}}) = \frac{{{_fmt_sa(mg_mass)}}}{{24{{,}}3}} = {_fmt_sa(moles_mg)}\text{{ mol}} \implies n(e^-) = 2 \times {_fmt_sa(moles_mg)} = {_fmt_sa(round(moles_mg * 2, 3))}\text{{ mol}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of Mg as reducing agent", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Balanced equation: Mg + Cu2+ -> Mg2+ + Cu", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"EMF calculation: {_fmt_sa(ecell)} V", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Higher potential explanation (Mg stronger reducing agent than Zn)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_formula_ecell", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Magnesium is oxidized: $\\text{Mg} \\to \\text{Mg}^{2+} + 2e^-$. Copper is reduced: $\\text{Cu}^{2+} + 2e^- \\to \\text{Cu}$.",
        "tier_2": "Calculate $E^\\circ_{\\text{cell}} = 0{,}34 - (-2{,}37)$.",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_09_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_09_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "09_mg_cu_galvanic_cell_high_potential_pair",
        "learning_objective_id": "ps12_ec_09_mg_cu_cell",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_reducing_agent_with_substance_reduced", "used_addition_instead_of_subtraction_for_ecell"],
        "keywords": ["magnesium copper cell", "reducing agent", "high EMF", "standard reduction potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 10: Al-Cu galvanic cell electron balancing
def _b10_al_cu_galvanic_cell_electron_balancing(r: random.Random) -> Dict[str, Any]:
    e0_al = -1.66
    e0_cu = 0.34
    ecell = round(e0_cu - e0_al, 2)

    al_moles = r.choice([0.1, 0.2, 0.3, 0.4, 0.5])
    cu_moles = round(al_moles * 1.5, 3)

    prompt = (
        f"A galvanic cell consists of an aluminium half-cell ($\\text{{Al}} \\mid \\text{{Al}}^{{3+}}$) "
        f"and a copper half-cell ($\\text{{Cu}}^{{2+}} \\mid \\text{{Cu}}$) connected under standard conditions.\n\n"
        f"1. Write down the oxidation half-reaction.\n"
        f"2. Write down the reduction half-reaction.\n"
        f"3. State the total number of electrons transferred in the balanced overall cell equation.\n"
        f"4. Write down the balanced overall cell equation.\n"
        f"5. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$).\n"
        f"6. If {_fmt_sa(al_moles)}\\text{{ mol}} of aluminium is oxidized, calculate the moles of copper metal deposited at the cathode."
    )

    ans_latex = (
        rf"1.\; \text{{Oxidation: }} \text{{Al}}(s) \to \text{{Al}}^{{3+}}(aq) + 3e^-\n"
        rf"2.\; \text{{Reduction: }} \text{{Cu}}^{{2+}}(aq) + 2e^- \to \text{{Cu}}(s)\n"
        rf"3.\; \text{{Lowest common multiple of 2 and 3 is 6 electrons transferred (}}6e^-\text{{).}}\n"
        rf"4.\; 2\text{{Al}}(s) + 3\text{{Cu}}^{{2+}}(aq) \to 2\text{{Al}}^{{3+}}(aq) + 3\text{{Cu}}(s)\n"
        rf"5.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = 0{{,}}34 - (-1{{,}}66) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"6.\; n(\text{{Cu}}) = \frac{{3}}{{2}} n(\text{{Al}}) = 1{{,}}5 \times {_fmt_sa(al_moles)} = {_fmt_sa(cu_moles)}\text{{ mol}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Aluminium oxidation half-reaction", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Copper reduction half-reaction", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Total electrons transferred: 6e-", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Balanced overall equation: 2Al + 3Cu2+ -> 2Al3+ + 3Cu", "marks": 2, "editable": True},
            {"id": "mp5", "desc": f"Calculation of E0_cell: {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "unbalanced_electrons_in_overall_equation", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Multiply the Al half-reaction by 2 and the Cu half-reaction by 3 to balance electrons.",
        "tier_2": "Do NOT multiply the reduction potentials $E^\\circ$ by the stoichiometric coefficients!",
        "tier_3": f"Equation: $2\\text{{Al}} + 3\\text{{Cu}}^{{2+}} \\to 2\\text{{Al}}^{{3+}} + 3\\text{{Cu}}$, $E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_10_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_10_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "10_al_cu_galvanic_cell_electron_balancing",
        "learning_objective_id": "ps12_ec_10_electron_balancing",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["multiplied_e0_potentials_by_balancing_coefficients", "failed_to_balance_electrons_in_overall_redox"],
        "keywords": ["aluminium copper", "electron balancing", "stoichiometric coefficients", "cell potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 11: Ni-Ag galvanic cell stoichiometry
def _b11_ni_ag_galvanic_cell_stoichiometry(r: random.Random) -> Dict[str, Any]:
    e0_ni = -0.27
    e0_ag = 0.80
    ecell = round(e0_ag - e0_ni, 2)

    ni_moles = r.choice([0.05, 0.10, 0.15, 0.20])
    ag_moles = round(ni_moles * 2, 3)

    prompt = (
        f"A standard electrochemical cell is built using nickel and silver electrodes in solutions of their respective salts.\n\n"
        f"1. Using standard reduction potentials ($E^\\circ_{{\\text{{Ni}}}} = {_fmt_sa(e0_ni)}\\text{{ V}}$, "
        f"$E^\\circ_{{\\text{{Ag}}}} = {_fmt_sa(e0_ag)}\\text{{ V}}$), identify the anode metal.\n"
        f"2. Write down the oxidation and reduction half-reactions.\n"
        f"3. Write down the balanced overall cell equation.\n"
        f"4. Calculate the standard electromotive force ($E^\\circ_{{\\text{{cell}}}}$).\n"
        f"5. If {_fmt_sa(ni_moles)}\\text{{ mol}} of nickel dissolves, calculate the moles of silver atoms deposited at the cathode."
    )

    ans_latex = (
        rf"1.\; \text{{Anode: Nickel (}}\text{{Ni}}\text{{), because it has the more negative reduction potential (}}-0{{,}}27\text{{ V}}).\n"
        rf"2.\; \text{{Oxidation: }} \text{{Ni}}(s) \to \text{{Ni}}^{{2+}}(aq) + 2e^-\n"
        rf"\quad \text{{Reduction: }} \text{{Ag}}^+(aq) + e^- \to \text{{Ag}}(s)\n"
        rf"3.\; \text{{Overall: }} \text{{Ni}}(s) + 2\text{{Ag}}^+(aq) \to \text{{Ni}}^{{2+}}(aq) + 2\text{{Ag}}(s)\n"
        rf"4.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = 0{{,}}80 - (-0{{,}}27) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"5.\; n(\text{{Ag}}) = 2 \times n(\text{{Ni}}) = 2 \times {_fmt_sa(ni_moles)} = {_fmt_sa(ag_moles)}\text{{ mol}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of Ni as anode", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Oxidation half-reaction", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Reduction half-reaction", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Balanced overall equation: Ni + 2Ag+ -> Ni2+ + 2Ag", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Calculation of E0_cell: {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_2_coefficient_on_silver", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Nickel releases 2 electrons, while silver ion needs only 1 electron. Multiply silver half-reaction by 2.",
        "tier_2": "Remember that $E^\\circ$ is an intensive property; do NOT multiply $0{,}80\\text{ V}$ by 2.",
        "tier_3": f"Equation: $\\text{{Ni}} + 2\\text{{Ag}}^+ \\to \\text{{Ni}}^{{2+}} + 2\\text{{Ag}}$, $E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_11_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_11_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "11_ni_ag_galvanic_cell_stoichiometry",
        "learning_objective_id": "ps12_ec_11_ni_ag_cell",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["multiplied_e0_by_2_for_silver", "forgot_to_balance_silver_ions"],
        "keywords": ["nickel silver cell", "stoichiometry", "intensive property", "cell potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 12: Pb-Ag galvanic cell stoichiometry
def _b12_pb_ag_galvanic_cell_stoichiometry(r: random.Random) -> Dict[str, Any]:
    e0_pb = -0.13
    e0_ag = 0.80
    ecell = round(e0_ag - e0_pb, 2)

    pb_mass = r.choice([2.07, 4.14, 6.21, 8.28])
    ag_mass = round((pb_mass / 207.2) * 2 * 107.9, 2)

    prompt = (
        f"A standard galvanic cell couples a lead half-cell ($\\text{{Pb}} \\mid \\text{{Pb}}^{{2+}}$) "
        f"with a silver half-cell ($\\text{{Ag}} \\mid \\text{{Ag}}^+$).\n\n"
        f"1. Write down the cell reaction equation.\n"
        f"2. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$).\n"
        f"3. State which electrode gains mass as the cell discharges.\n"
        f"4. If {_fmt_sa(pb_mass)}\\text{{ g}} of lead dissolves from the anode, calculate the mass of silver deposited on the cathode ($M(\\text{{Pb}}) = 207{{,}}2\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}, M(\\text{{Ag}}) = 107{{,}}9\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{Pb}}(s) + 2\text{{Ag}}^+(aq) \to \text{{Pb}}^{{2+}}(aq) + 2\text{{Ag}}(s)\n"
        rf"2.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = 0{{,}}80 - (-0{{,}}13) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"3.\; \text{{The silver (}}\text{{Ag}}\text{{) cathode gains mass as metallic silver precipitates onto the electrode.}}\n"
        rf"4.\; n(\text{{Pb}}) = \frac{{{_fmt_sa(pb_mass)}}}{{207{{,}}2}} = {_fmt_sa(round(pb_mass/207.2, 3))}\text{{ mol}} \implies m(\text{{Ag}}) = 2 \times n(\text{{Pb}}) \times 107{{,}}9 = {_fmt_sa(ag_mass)}\text{{ g}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Balanced overall equation: Pb + 2Ag+ -> Pb2+ + 2Ag", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculation of E0_cell: {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Silver electrode gains mass", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_formula_substitution", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Lead has $E^\\circ = -0{,}13\\text{ V}$ and silver has $E^\\circ = +0{,}80\\text{ V}$.",
        "tier_2": "Lead is the anode (oxidized) and silver is the cathode (reduced).",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$. Silver cathode gains mass.",
    }

    return {
        "id": f"ps12_ec_12_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_12_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "12_pb_ag_galvanic_cell_stoichiometry",
        "learning_objective_id": "ps12_ec_12_pb_ag_cell",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["swapped_cathode_and_anode_mass_changes", "sign_error_subtracting_negative_potential"],
        "keywords": ["lead silver cell", "mass gain", "reduction potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 13: Fe-Cu galvanic cell and corrosion protection
def _b13_fe_cu_galvanic_cell_corrosion_protection(r: random.Random) -> Dict[str, Any]:
    e0_fe = -0.44
    e0_cu = 0.34
    ecell = round(e0_cu - e0_fe, 2)

    prompt = (
        f"An underground steel pipeline (predominantly iron, $\\text{{Fe}}$) is in direct contact with copper plumbing fittings.\n\n"
        f"1. Using standard reduction potentials ($E^\\circ_{{\\text{{Fe}}}} = -0{{,}}44\\text{{ V}}$, "
        f"$E^\\circ_{{\\text{{Cu}}}} = +0{{,}}34\\text{{ V}}$), explain why connecting iron directly to copper accelerates the rusting (corrosion) of the iron.\n"
        f"2. Write down the oxidation half-reaction for the corrosion of iron.\n"
        f"3. Calculate the galvanic cell potential ($E^\\circ$) formed by this iron-copper couple.\n"
        f"4. Propose a method to protect the iron pipeline using a **sacrificial anode** (such as zinc or magnesium) and explain how it prevents corrosion."
    )

    ans_latex = (
        rf"1.\; \text{{Iron has a more negative reduction potential (}}-0{{,}}44\text{{ V) than copper (}}+0{{,}}34\text{{ V). A galvanic cell is set up where iron acts as the anode and is preferentially oxidized (corrodes).}}\n"
        rf"2.\; \text{{Fe}}(s) \to \text{{Fe}}^{{2+}}(aq) + 2e^-\n"
        rf"3.\; E^\circ_{{\text{{cell}}}} = 0{{,}}34 - (-0{{,}}44) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"4.\; \text{{Connect zinc (or magnesium) blocks to the iron pipe. Because zinc has a more negative reduction potential (}}-0{{,}}76\text{{ V) than iron (}}-0{{,}}44\text{{ V), zinc is more readily oxidized and acts as the sacrificial anode, protecting the iron pipe (cathodic protection).}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Galvanic corrosion explanation (iron as anode relative to copper)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Iron oxidation half-reaction: Fe -> Fe2+ + 2e-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Cell potential calculation: {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Sacrificial protection explanation (zinc more easily oxidized than iron)", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "suggested_noble_metal_as_sacrificial_anode", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Iron is oxidized because it has a more negative $E^\\circ$ than copper.",
        "tier_2": "A sacrificial anode must have a MORE negative $E^\\circ$ than iron (e.g. Zn or Mg).",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$. Zinc protects iron by being oxidized preferentially.",
    }

    return {
        "id": f"ps12_ec_13_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_13_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "13_fe_cu_galvanic_cell_corrosion_protection",
        "learning_objective_id": "ps12_ec_13_corrosion_protection",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["suggested_copper_protects_iron", "confused_sacrificial_anode_with_protective_coating"],
        "keywords": ["galvanic corrosion", "sacrificial anode", "cathodic protection", "iron copper"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 14: Standard cell notation for solid electrodes
def _b14_standard_cell_notation_solid_electrodes(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Cu"), ("Al", "Ag"), ("Ni", "Ag"), ("Pb", "Cu")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]
    a_chg = anode_data["charge"]
    c_chg = cath_data["charge"]

    a_ion = f"{anode_sym}^{{{a_chg}+}}" if a_chg > 1 else f"{anode_sym}^+"
    c_ion = f"{cath_sym}^{{{c_chg}+}}" if c_chg > 1 else f"{cath_sym}^+"

    notation = f"\\text{{{anode_sym}}}(s) \\mid \\text{{{a_ion}}}(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \\parallel \\text{{{c_ion}}}(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \\mid \\text{{{cath_sym}}}(s)"

    prompt = (
        f"A standard galvanic cell operates using a {anode_data['name']} ({anode_sym}) half-cell "
        f"and a {cath_data['name']} ({cath_sym}) half-cell.\n\n"
        f"1. Write down the **standard cell notation** for this galvanic cell, including phase symbols and standard concentrations.\n"
        f"2. State what the single vertical line ($\\mid$) represents in standard cell notation.\n"
        f"3. State what the double vertical line ($\\parallel$) represents in standard cell notation.\n"
        f"4. State the convention for whether the anode or cathode is written on the left in standard cell notation."
    )

    ans_latex = (
        rf"1.\; {notation}\n"
        rf"2.\; \text{{A single vertical line (}}\mid\text{{) represents a phase boundary (e.g. between solid electrode and aqueous solution).}}\n"
        rf"3.\; \text{{A double vertical line (}}\parallel\text{{) represents the salt bridge (or liquid junction).}}\n"
        rf"4.\; \text{{By IUPAC convention, the anode (oxidation half-cell) is always written on the left.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Standard cell notation format and order", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Phase boundary single line explanation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Salt bridge double line explanation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Convention: anode on left", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_phase_symbols_or_concentrations", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Convention: Anode (oxidation) on left, Cathode (reduction) on right. Salt bridge is $\\parallel$.",
        "tier_2": "Format: Metal(s) | Ion(aq, 1 M) || Ion(aq, 1 M) | Metal(s).",
        "tier_3": f"${notation}$.",
    }

    return {
        "id": f"ps12_ec_14_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_14_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "14_standard_cell_notation_solid_electrodes",
        "learning_objective_id": "ps12_ec_14_cell_notation",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_anode_and_cathode_in_cell_notation", "used_double_line_for_phase_boundary"],
        "keywords": ["cell notation", "phase boundary", "salt bridge", "anode on left"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 15: Standard cell notation with inert platinum electrodes
def _b15_standard_cell_notation_inert_platinum_electrodes(r: random.Random) -> Dict[str, Any]:
    metal = r.choice(["Zn", "Cu", "Mg", "Ag"])
    m_data = STANDARD_REDUCTION_DATA[metal]
    m_e0 = m_data["e0"]
    # If m_e0 < 0, metal is anode, SHE is cathode. If m_e0 > 0, SHE is anode, metal is cathode.
    if m_e0 < 0:
        notation = (
            f"\\text{{{metal}}}(s) \\mid \\text{{{metal}}}^{{2+}}(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) "
            f"\\parallel \\text{{H}}^+(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \\mid \\text{{H}}_2(g, 101{{,}}3\\text{{ kPa}}) \\mid \\text{{Pt}}(s)"
        )
        anode_desc = f"{m_data['name']} ({metal})"
        cath_desc = "Standard Hydrogen Electrode (Pt)"
    else:
        notation = (
            f"\\text{{Pt}}(s) \\mid \\text{{H}}_2(g, 101{{,}}3\\text{{ kPa}}) \\mid \\text{{H}}^+(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) "
            f"\\parallel \\text{{{metal}}}^{{2+}}(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \\mid \\text{{{metal}}}(s)"
        )
        anode_desc = "Standard Hydrogen Electrode (Pt)"
        cath_desc = f"{m_data['name']} ({metal})"

    prompt = (
        f"A standard galvanic cell couples a {m_data['name']} ({metal}) half-cell with a Standard Hydrogen Electrode (SHE).\n\n"
        f"1. Explain why an inert electrode such as platinum ($\\text{{Pt}}$) is required in the hydrogen half-cell.\n"
        f"2. Write down the complete **standard cell notation** for this galvanic cell, specifying the platinum electrode, "
        f"phase symbols, gas pressure, and ion concentrations.\n"
        f"3. Identify which half-cell is the anode ({anode_desc}) and which is the cathode ({cath_desc})."
    )

    ans_latex = (
        rf"1.\; \text{{Hydrogen is a gas and }} \text{{H}}^+ \text{{ is an ion in solution; neither is a solid electrical conductor. An inert, non-reactive conductor (platinum) is required to conduct electrons into or out of the half-cell.}}\n"
        rf"2.\; {notation}\n"
        rf"3.\; \text{{Anode: }} {anode_desc};\quad \text{{Cathode: }} {cath_desc}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Justification for inert Pt conductor", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Accurate cell notation with Pt electrode and standard parameters", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Identification of anode and cathode half-cells", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_platinum_in_cell_notation", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Gaseous reactants need a solid inert conductor (Pt). Place Pt at the extreme outer end of the notation.",
        "tier_2": f"Since $E^\\circ({metal}) = {_fmt_sa(m_e0)}\\text{{ V}}$, determine if {metal} is anode or cathode.",
        "tier_3": f"${notation}$.",
    }

    return {
        "id": f"ps12_ec_15_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_15_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "15_standard_cell_notation_inert_platinum_electrodes",
        "learning_objective_id": "ps12_ec_15_pt_cell_notation",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_platinum_from_gas_half_cell", "placed_pt_in_middle_of_half_cell_notation"],
        "keywords": ["platinum electrode", "inert electrode", "cell notation", "gas half-cell"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 16: Cell potential formula Ecell = Ecathode - Eanode
def _b16_cell_potential_formula_ecell_ecathode_minus_eanode(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Mg", "Ag"), ("Al", "Cu"), ("Zn", "Ag"), ("Pb", "Cu"), ("Ni", "Ag")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]
    e0_a = anode_data["e0"]
    e0_c = cath_data["e0"]
    ecell = round(e0_c - e0_a, 2)

    prompt = (
        f"A learner constructs a standard galvanic cell using {anode_data['name']} ({anode_sym}) "
        f"and {cath_data['name']} ({cath_sym}) half-cells.\n\n"
        f"Given reduction potentials:\n"
        f"- $E^\\circ_{{\\text{{{anode_sym}}}}} = {_fmt_sa(e0_a)}\\text{{ V}}$\n"
        f"- $E^\\circ_{{\\text{{{cath_sym}}}}} = {_fmt_sa(e0_c)}\\text{{ V}}$\n\n"
        f"1. Write down the official standard formula used to calculate the standard electromotive force of a cell ($E^\\circ_{{\\text{{cell}}}}$).\n"
        f"2. Substitute the given values into the formula and calculate $E^\\circ_{{\\text{{cell}}}}$.\n"
        f"3. Explain why the negative sign in the formula ensures that the anode potential is subtracted rather than added."
    )

    ans_latex = (
        rf"1.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} \quad \text{{(or }} E^\circ_{{\text{{oxidizing agent}}}} - E^\circ_{{\text{{reducing agent}}}}\text{{)}}\n"
        rf"2.\; E^\circ_{{\text{{cell}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"3.\; \text{{Because tabulated standard reduction potentials are defined for the reduction half-reaction. At the anode, oxidation occurs (the reverse reaction), so subtracting the reduction potential accounts for reversing the half-reaction without changing the table value.}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: E0_cell = E0_cathode - E0_anode", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of E0_cell: {_fmt_sa(ecell)} V", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explanation of subtraction due to tabulated reduction convention", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_e_ox_plus_e_red_without_signs", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Formula: $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$.",
        "tier_2": f"Cathode is {cath_sym} (${_fmt_sa(e0_c)}\\text{{ V}}$) and Anode is {anode_sym} (${_fmt_sa(e0_a)}\\text{{ V}}$).",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_16_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_16_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "16_cell_potential_formula_ecell_ecathode_minus_eanode",
        "learning_objective_id": "ps12_ec_16_ecell_formula",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["inverted_subtraction_order", "added_potentials_instead_of_subtracting"],
        "keywords": ["E0_cell formula", "E0_cathode - E0_anode", "cell potential", "reduction potentials"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 17: Determining unknown electrode potential from Ecell
def _b17_determining_unknown_electrode_potential_from_ecell(r: random.Random) -> Dict[str, Any]:
    unknown_metal = r.choice(["Cr", "Mn", "Cd", "Ni", "Sn", "Pb"])
    ref_metal = "Cu"
    u_data = STANDARD_REDUCTION_DATA[unknown_metal]
    ref_data = STANDARD_REDUCTION_DATA[ref_metal]

    e0_u = u_data["e0"]
    e0_ref = ref_data["e0"]
    measured_emf = round(e0_ref - e0_u, 2)

    prompt = (
        f"A researcher connects an unknown metal electrode $\\text{{X}}$ immersed in a $1{{,}}0\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ solution "
        f"of $\\text{{X}}^{{2+}}$ ions to a standard copper half-cell ($\\text{{Cu}} \\mid \\text{{Cu}}^{{2+}}$, $E^\\circ = +0{{,}}34\\text{{ V}}$).\n"
        f"Under standard conditions, the cell generates an electromotive force of $E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(measured_emf)}\\text{{ V}}$, "
        f"and the copper electrode is observed to gain mass.\n\n"
        f"1. State whether the copper electrode is the anode or cathode.\n"
        f"2. Use the cell potential formula ($E^\\circ_{{\\text{{cell}}}} = E^\\circ_{{\\text{{cathode}}}} - E^\\circ_{{\\text{{anode}}}}$) "
        f"to calculate the standard reduction potential of the unknown metal ($E^\\circ_{{\\text{{X}}}}$).\n"
        f"3. Identify metal $\\text{{X}}$ from the calculated reduction potential."
    )

    ans_latex = (
        rf"1.\; \text{{Copper gains mass, which means reduction occurs at the copper electrode: Copper is the cathode.}}\n"
        rf"2.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}}\n"
        rf"\quad {_fmt_sa(measured_emf)} = 0{{,}}34 - E^\circ_{{\text{{X}}}}\n"
        rf"\quad E^\circ_{{\text{{X}}}} = 0{{,}}34 - {_fmt_sa(measured_emf)} = {_fmt_sa(e0_u)}\text{{ V}}\n"
        rf"3.\; \text{{From Table 4A/4B, the metal with }} E^\circ = {_fmt_sa(e0_u)}\text{{ V}} \text{{ is }} \mathbf{{{u_data['name']} ({unknown_metal})}}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of copper as cathode from mass gain", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Substitution into E0_cell formula", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of E0_X: {_fmt_sa(e0_u)} V", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Identification of metal X: {u_data['name']} ({unknown_metal})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_solving_for_anode_potential", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Mass gain indicates reduction: copper is the cathode ($E^\\circ_{\\text{cathode}} = +0{,}34\\text{ V}$).",
        "tier_2": "Solve for $E^\\circ_{\\text{anode}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{cell}} = 0{,}34 - {_fmt_sa(measured_emf)}$.",
        "tier_3": f"$E^\\circ_{{\\text{{X}}}} = {_fmt_sa(e0_u)}\\text{{ V}}$, which corresponds to {u_data['name']} ({unknown_metal}).",
    }

    return {
        "id": f"ps12_ec_17_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_17_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "17_determining_unknown_electrode_potential_from_ecell",
        "learning_objective_id": "ps12_ec_17_unknown_potential",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["sign_error_solving_for_eanode", "incorrectly_identified_copper_as_anode"],
        "keywords": ["unknown electrode potential", "cathode mass gain", "reduction potential identification"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 18: Effect of concentration changes on cell potential
def _b18_effect_of_concentration_changes_on_cell_potential(r: random.Random) -> Dict[str, Any]:
    # Zn + Cu2+ <=> Zn2+ + Cu
    altered_ion = r.choice(["Cu2+_increase", "Cu2+_decrease", "Zn2+_increase", "Zn2+_decrease"])

    if altered_ion == "Cu2+_increase":
        action = "Concentrated copper(II) sulfate is added to the copper half-cell, increasing $[\\text{Cu}^{2+}]$ above $1{,}0\\text{ mol}\\cdot\\text{dm}^{-3}$."
        shift = "forward (to the right)"
        effect = "increases"
        reason = "increasing reactant concentration $[\text{Cu}^{2+}]$ favours the forward reaction, thereby increasing the driving force (cell potential)"
    elif altered_ion == "Cu2+_decrease":
        action = "Water is added to dilute the copper half-cell, decreasing $[\\text{Cu}^{2+}]$ below $1{,}0\\text{ mol}\\cdot\\text{dm}^{-3}$."
        shift = "reverse (to the left)"
        effect = "decreases"
        reason = "decreasing reactant concentration $[\text{Cu}^{2+}]$ favours the reverse reaction, thereby reducing the cell potential"
    elif altered_ion == "Zn2+_increase":
        action = "Solid $\\text{ZnSO}_4$ is dissolved into the zinc half-cell, increasing $[\\text{Zn}^{2+}]$ above $1{,}0\\text{ mol}\\cdot\\text{dm}^{-3}$."
        shift = "reverse (to the left)"
        effect = "decreases"
        reason = "increasing product concentration $[\text{Zn}^{2+}]$ favours the reverse reaction, thereby opposing the cell reaction and decreasing the cell potential"
    else:
        action = "A precipitating agent (e.g. $\\text{Na}_2\\text{S}$) is added to the zinc half-cell, precipitating $\\text{ZnS}$ and drastically decreasing $[\\text{Zn}^{2+}]$. "
        shift = "forward (to the right)"
        effect = "increases"
        reason = "decreasing product concentration $[\text{Zn}^{2+}]$ shifts equilibrium forward according to Le Chatelier's principle, thereby increasing the cell potential"

    prompt = (
        f"A standard Daniell cell operates according to the overall equilibrium:\n"
        f"$$\\text{{Zn}}(s) + \\text{{Cu}}^{{2+}}(aq) \\rightleftharpoons \\text{{Zn}}^{{2+}}(aq) + \\text{{Cu}}(s) \\quad (E^\\circ_{{\\text{{cell}}}} = 1{{,}}10\\text{{ V}})$$\n\n"
        f"The following adjustment is made to the cell:\n"
        f"> *{action}*\n\n"
        f"1. State whether the cell potential ($E_{{\\text{{cell}}}}$) **increases**, **decreases**, or **remains unchanged**.\n"
        f"2. Use **Le Chatelier's Principle** to explain your answer clearly."
    )

    ans_latex = (
        rf"1.\; \text{{The cell potential }} \mathbf{{{effect}}}.\n"
        rf"2.\; \text{{According to Le Chatelier's Principle, {reason}. The equilibrium shifts {shift}, causing the cell potential to {effect}.}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct prediction: {effect}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Le Chatelier explanation: equilibrium shifts {shift}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Link between forward/reverse driving force and cell potential", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_shift_direction", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Apply Le Chatelier's Principle to $\\text{Zn} + \\text{Cu}^{2+} \\rightleftharpoons \\text{Zn}^{2+} + \\text{Cu}$.",
        "tier_2": "If the shift is forward, $E_{\\text{cell}}$ increases. If the shift is reverse, $E_{\\text{cell}}$ decreases.",
        "tier_3": f"Equilibrium shifts {shift} $\\implies E_{{\\text{{cell}}}}$ {effect}.",
    }

    return {
        "id": f"ps12_ec_18_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_18_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "18_effect_of_concentration_changes_on_cell_potential",
        "learning_objective_id": "ps12_ec_18_le_chatelier_conc",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_cell_potential_is_unaffected_by_concentration", "inverted_le_chatelier_shift"],
        "keywords": ["Le Chatelier", "concentration effect", "cell potential", "equilibrium shift"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 19: Effect of electrode surface area on potential and current
def _b19_effect_of_electrode_surface_area_on_potential_and_current(r: random.Random) -> Dict[str, Any]:
    area_factor = r.choice([2, 3, 4])

    prompt = (
        f"A chemist modifies a standard zinc-copper galvanic cell ($E^\\circ_{{\\text{{cell}}}} = 1{{,}}10\\text{{ V}}$) by replacing "
        f"both electrodes with plates that have ${area_factor}\\text{{ times}}$ the surface area of the original electrodes. "
        f"All other parameters (concentrations, temperature, and electrolyte volume) remain identical.\n\n"
        f"1. State whether the standard electromotive force ($E^\\circ_{{\\text{{cell}}}}$) **increases**, **decreases**, or **remains unchanged**.\n"
        f"2. Explain your answer to question 1 using the concept of an intensive property.\n"
        f"3. State what effect increasing the electrode surface area has on the **maximum current** ($I_{{\\max}}$) that the cell can deliver to an external load.\n"
        f"4. Explain your answer to question 3 in terms of internal resistance and available reaction sites."
    )

    ans_latex = (
        rf"1.\; \text{{The standard electromotive force }} E^\circ_{{\text{{cell}}}} \mathbf{{\text{{remains unchanged (1,10 V)}}}}.\n"
        rf"2.\; \text{{Electrode potential is an intensive property; it depends on the chemical nature of the substances and concentrations, not on the physical size or surface area of the electrodes.}}\n"
        rf"3.\; \text{{The maximum current }} I_{{\max}} \mathbf{{\text{{increases}}}}.\n"
        rf"4.\; \text{{Larger surface area provides more reaction sites for simultaneous electron transfer and lowers the internal resistance of the cell, allowing a higher rate of charge flow (current).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "E0_cell remains unchanged", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explanation: intensive property, independent of area", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Maximum current increases", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Explanation: more reaction sites and reduced internal resistance", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "claimed_voltage_multiplies_by_area", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Cell potential ($E^\\circ$) is an intensive property and does NOT depend on electrode size.",
        "tier_2": "Current depends on the rate of reaction. Larger surface area allows more charge transfer per second.",
        "tier_3": "Potential remains $1{,}10\\text{ V}$; maximum current increases.",
    }

    return {
        "id": f"ps12_ec_19_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_19_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "19_effect_of_electrode_surface_area_on_potential_and_current",
        "learning_objective_id": "ps12_ec_19_surface_area",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_cell_potential_increases_with_electrode_size", "confused_potential_with_current_capacity"],
        "keywords": ["surface area", "intensive property", "maximum current", "internal resistance"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 20: Cell potential drop to zero at chemical equilibrium
def _b20_cell_potential_drop_to_zero_at_chemical_equilibrium(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A zinc-copper galvanic cell ($E^\\circ_{{\\text{{cell}}}} = 1{{,}}10\\text{{ V}}$) is connected to a small light bulb "
        f"and allowed to run continuously for several hours until the bulb eventually stops glowing completely.\n\n"
        f"1. State the reading on a high-resistance voltmeter connected across the terminals of the cell once the bulb stops glowing.\n"
        f"2. Explain in terms of chemical equilibrium why the voltmeter reading reaches this specific value.\n"
        f"3. State what has happened to the forward and reverse reaction rates at this stage.\n"
        f"4. Clarify the misconception that a 'flat battery' has zero chemical species remaining."
    )

    ans_latex = (
        rf"1.\; \text{{Voltmeter reading: }} \mathbf{{0{{,}}00\text{{ V}}}}.\n"
        rf"2.\; \text{{As the cell discharges, reactants (}}\text{{Cu}}^{{2+}}\text{{) are consumed and products (}}\text{{Zn}}^{{2+}}\text{{) accumulate until the reaction reaches dynamic chemical equilibrium. At equilibrium, the driving force (cell potential) is zero.}}\n"
        rf"3.\; \text{{The rate of the forward reaction equals the rate of the reverse reaction: }} \text{{rate}}_{{\text{{forward}}}} = \text{{rate}}_{{\text{{reverse}}}}.\n"
        rf"4.\; \text{{Chemical species have NOT run out completely; rather, the concentrations have reached the equilibrium constant ratio (}}Q = K_c\text{{), where no net chemical change or electron flow occurs.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Voltmeter reading: 0.00 V", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Chemical equilibrium explanation for zero potential", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Equality of forward and reverse reaction rates", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Clarification: equilibrium reached, species not completely exhausted", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_all_copper_or_zinc_atoms_vanished", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "When a galvanic cell runs down, it reaches chemical equilibrium: $E_{\\text{cell}} = 0\\text{ V}$.",
        "tier_2": "At equilibrium, forward and reverse rates are equal, so net electron transfer ceases.",
        "tier_3": "Voltmeter reads $0{,}00\\text{ V}$. The battery is flat because $Q = K_c$, not because all matter vanished.",
    }

    return {
        "id": f"ps12_ec_20_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_20_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "20_cell_potential_drop_to_zero_at_chemical_equilibrium",
        "learning_objective_id": "ps12_ec_20_equilibrium_zero_emf",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["believed_reactants_drop_to_absolute_zero", "confused_zero_potential_with_broken_circuit"],
        "keywords": ["chemical equilibrium", "flat battery", "0.00 V", "dynamic equilibrium"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 21: Mass changes of electrodes quantitative stoichiometry
def _b21_mass_changes_of_electrodes_quantitative_stoichiometry(r: random.Random) -> Dict[str, Any]:
    mass_lost_zn = r.choice([1.30, 2.60, 3.27, 6.54, 13.08])  # g of Zn
    m_zn = 65.38
    m_cu = 63.55
    moles_zn = mass_lost_zn / m_zn
    moles_cu = moles_zn  # 1:1 ratio
    mass_gained_cu = moles_cu * m_cu

    prompt = (
        f"A standard Daniell cell operates until the zinc electrode loses $\\Delta m_{{\\text{{Zn}}}} = {_fmt_sa(mass_lost_zn)}\\text{{ g}}$ of mass.\n"
        f"Molar masses: $M(\\text{{Zn}}) = 65{{,}}38\\text{{ g/mol}}$, $M(\\text{{Cu}}) = 63{{,}}55\\text{{ g/mol}}$.\n\n"
        f"1. Calculate the number of moles of zinc that oxidized and dissolved into solution.\n"
        f"2. Use the balanced cell equation ($\\text{{Zn}} + \\text{{Cu}}^{{2+}} \\to \\text{{Zn}}^{{2+}} + \\text{{Cu}}$) "
        f"to determine the number of moles of copper deposited on the cathode.\n"
        f"3. Calculate the mass of copper ($\\Delta m_{{\\text{{Cu}}}}$) deposited onto the cathode.\n"
        f"4. State why the mass gained by the copper electrode does not exactly equal the mass lost by the zinc electrode."
    )

    ans_latex = (
        rf"1.\; n_{{\text{{Zn}}}} = \frac{{\Delta m_{{\text{{Zn}}}}}}{{M_{{\text{{Zn}}}}}} = \frac{{{_fmt_sa(mass_lost_zn)}}}{{65{{,}}38}} = {_fmt_sa(moles_zn, 4)}\text{{ mol}}\n"
        rf"2.\; \text{{From the 1:1 mole ratio, }} n_{{\text{{Cu}}}} = n_{{\text{{Zn}}}} = {_fmt_sa(moles_cu, 4)}\text{{ mol}}\n"
        rf"3.\; \Delta m_{{\text{{Cu}}}} = n_{{\text{{Cu}}}} \times M_{{\text{{Cu}}}} = ({_fmt_sa(moles_cu, 4)})(63{{,}}55) = {_fmt_sa(mass_gained_cu, 2)}\text{{ g}}\n"
        rf"4.\; \text{{Zinc and copper have different molar masses (}}65{{,}}38\text{{ g/mol vs }} 63{{,}}55\text{{ g/mol). Mole ratios are conserved (1:1), but mass depends on molar mass.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Moles of Zn dissolved: {_fmt_sa(moles_zn, 4)} mol", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "1:1 mole ratio identification", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Mass of Cu deposited: {_fmt_sa(mass_gained_cu, 2)} g", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Explanation of different molar masses", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "assumed_mass_is_conserved_1_to_1", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Find moles of zinc: $n = m / M$. Then use the 1:1 mole ratio to find moles of copper.",
        "tier_2": "Calculate copper mass: $m_{\\text{Cu}} = n \\times 63{,}55$.",
        "tier_3": f"$n = {_fmt_sa(moles_zn, 4)}\\text{{ mol}}$, $\\Delta m_{{\\text{{Cu}}}} = {_fmt_sa(mass_gained_cu, 2)}\\text{{ g}}$.",
    }

    return {
        "id": f"ps12_ec_21_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_21_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "21_mass_changes_of_electrodes_quantitative_stoichiometry",
        "learning_objective_id": "ps12_ec_21_electrode_mass_stoichiometry",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_mass_lost_equals_mass_gained", "used_atomic_number_instead_of_molar_mass"],
        "keywords": ["mass changes", "stoichiometry", "molar mass", "Daniell cell"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 22: Faraday charge and electron moles in galvanic cell
def _b22_faraday_charge_and_electron_moles_in_galvanic_cell(r: random.Random) -> Dict[str, Any]:
    current_a = r.choice([0.5, 1.0, 1.5, 2.0])
    time_min = r.choice([30, 45, 60, 90])
    time_s = time_min * 60
    total_charge_c = current_a * time_s
    moles_e = total_charge_c / FARADAY_CONST
    # For Cu2+ + 2e- -> Cu: moles of Cu = moles_e / 2
    moles_cu = moles_e / 2.0
    mass_cu = moles_cu * 63.55

    prompt = (
        f"A Daniell cell delivers a steady current of $I = {_fmt_sa(current_a)}\\text{{ A}}$ through an external resistor "
        f"for a time interval of $\\Delta t = {time_min}\\text{{ minutes}}$ ($F = 96500\\text{{ C/mol }}\\text{{e}}^-$).\n\n"
        f"1. Calculate the total electric charge ($Q$) in coulombs that passed through the external circuit.\n"
        f"2. Calculate the number of moles of electrons ($n(e^-)$) transferred.\n"
        f"3. Use the reduction half-reaction ($\\text{{Cu}}^{{2+}} + 2e^- \\to \\text{{Cu}}$) to determine the mass of copper "
        f"deposited onto the cathode ($M(\\text{{Cu}}) = 63{{,}}55\\text{{ g/mol}}$)."
    )

    ans_latex = (
        rf"1.\; Q = I \Delta t = ({_fmt_sa(current_a)})\text{{ A}} \times ({time_min} \times 60\text{{ s}}) = {_fmt_sa(total_charge_c)}\text{{ C}}\n"
        rf"2.\; n(e^-) = \frac{{Q}}{{F}} = \frac{{{_fmt_sa(total_charge_c)}}}{{96500}} = {_fmt_sa(moles_e, 4)}\text{{ mol e}}^-\n"
        rf"3.\; n_{{\text{{Cu}}}} = \frac{{n(e^-)}}{{2}} = \frac{{{_fmt_sa(moles_e, 4)}}}{{2}} = {_fmt_sa(moles_cu, 4)}\text{{ mol}}\n"
        rf"\quad m_{{\text{{Cu}}}} = n_{{\text{{Cu}}}} \times M_{{\text{{Cu}}}} = ({_fmt_sa(moles_cu, 4)})(63{{,}}55) = {_fmt_sa(mass_cu, 3)}\text{{ g}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Charge calculation: {_fmt_sa(total_charge_c)} C", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Moles of electrons: {_fmt_sa(moles_e, 4)} mol", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Mass of copper deposited: {_fmt_sa(mass_cu, 3)} g", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_minutes_to_seconds_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$Q = I \\Delta t$. Convert minutes to seconds ($t = \\text{minutes} \\times 60$).",
        "tier_2": "Moles of electrons: $n(e^-) = Q / F$. Copper reduction needs 2 moles of $e^-$ per mole of Cu.",
        "tier_3": f"$Q = {_fmt_sa(total_charge_c)}\\text{{ C}}$, $n(e^-) = {_fmt_sa(moles_e, 4)}\\text{{ mol}}$, $m_{{\\text{{Cu}}}} = {_fmt_sa(mass_cu, 3)}\\text{{ g}}$.",
    }

    return {
        "id": f"ps12_ec_22_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_22_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "22_faraday_charge_and_electron_moles_in_galvanic_cell",
        "learning_objective_id": "ps12_ec_22_faraday_quant",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_divide_by_2_for_cu2_plus_electrons", "used_time_in_minutes_instead_of_seconds"],
        "keywords": ["Faraday constant", "electric charge", "current time", "deposited mass"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 23: Halide half-cells chlorine bromine iodine potentials
def _b23_halide_half_cells_chlorine_bromine_iodine_potentials(r: random.Random) -> Dict[str, Any]:
    hal_pair = r.choice([("Cl2", "Br2"), ("Cl2", "I2"), ("Br2", "I2")])
    stronger_ox, weaker_ox = hal_pair
    e0_strong = STANDARD_REDUCTION_DATA[stronger_ox]["e0"]
    e0_weak = STANDARD_REDUCTION_DATA[weaker_ox]["e0"]

    prompt = (
        f"Consider the halogen/halide half-reactions and their standard reduction potentials:\n"
        f"- $\\text{{{stronger_ox}}} + 2e^- \\rightleftharpoons 2\\text{{{stronger_ox[0]}}}^-: E^\\circ = {_fmt_sa(e0_strong)}\\text{{ V}}$\n"
        f"- $\\text{{{weaker_ox}}} + 2e^- \\rightleftharpoons 2\\text{{{weaker_ox[0]}}}^-: E^\\circ = {_fmt_sa(e0_weak)}\\text{{ V}}$\n\n"
        f"1. Identify which halogen is the stronger oxidizing agent.\n"
        f"2. State whether chlorine gas ($\\text{{Cl}}_2$) will spontaneously oxidize bromide ions ($\\text{{Br}}^-$) to bromine ($\\text{{Br}}_2$). Justify using $E^\\circ$ values.\n"
        f"3. Write down the balanced overall equation for the spontaneous displacement reaction between $\\text{{{stronger_ox}}}$ and $\\text{{{weaker_ox[0]}}}^-$.\n"
        f"4. State the observable colour change when the displacement reaction occurs in aqueous solution."
    )

    colour_desc = (
        "colourless to orange/brown (due to Br2 formation)"
        if weaker_ox == "Br2"
        else "colourless to deep yellow/brown or purple in organic solvent (due to I2 formation)"
    )

    ans_latex = (
        rf"1.\; \text{{{stronger_ox}}} \text{{ is the stronger oxidizing agent because it has the more positive }} E^\circ = {_fmt_sa(e0_strong)}\text{{ V}}.\n"
        rf"2.\; \text{{Yes, }} \text{{Cl}}_2 \text{{ will spontaneously oxidize }} \text{{Br}}^- \text{{ because }} E^\circ(\text{{Cl}}_2) = 1{{,}}36\text{{ V}} > E^\circ(\text{{Br}}_2) = 1{{,}}07\text{{ V}} \implies E^\circ_{{\text{{cell}}}} = 1{{,}}36 - 1{{,}}07 = +0{{,}}29\text{{ V}} > 0.\n"
        rf"3.\; \text{{{stronger_ox}}} + 2\text{{{weaker_ox[0]}}}^-(aq) \to 2\text{{{stronger_ox[0]}}}^-(aq) + \text{{{weaker_ox}}}\n"
        rf"4.\; \text{{The solution changes from }} {colour_desc}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Identification of {stronger_ox} as stronger oxidizing agent", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Justification with positive cell potential", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Balanced net ionic displacement equation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Observable colour change description", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "reversed_halogen_halide_species", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Higher $E^\\circ$ means a stronger oxidizing agent that can displace halides with lower $E^\\circ$.",
        "tier_2": "Chlorine ($1{,}36\\text{ V}$) oxidizes bromide ($1{,}07\\text{ V}$) and iodide ($0{,}54\\text{ V}$).",
        "tier_3": f"Equation: $\\text{{{stronger_ox}}} + 2\\text{{{weaker_ox[0]}}}^- \\to 2\\text{{{stronger_ox[0]}}}^- + \\text{{{weaker_ox}}}$. Colour: {colour_desc}.",
    }

    return {
        "id": f"ps12_ec_23_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_23_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "23_halide_half_cells_chlorine_bromine_iodine_potentials",
        "learning_objective_id": "ps12_ec_23_halogen_halide_potentials",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_halide_ion_with_elemental_halogen", "reversed_oxidizing_agent_trend_in_halogens"],
        "keywords": ["halogens", "halides", "displacement reaction", "colour change"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 24: Galvanic cell with seed-varied inline vector diagram
def _b24_galvanic_cell_with_seed_varied_inline_diagram(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Cu"), ("Al", "Ag"), ("Ni", "Ag")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]
    ecell = round(cath_data["e0"] - anode_data["e0"], 2)

    svg = _clean_svg(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="100%" height="220" style="background:#f8fafc;">
      <!-- Beaker 1 (Left: Anode) -->
      <rect x="50" y="90" width="130" height="130" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
      <rect x="90" y="50" width="24" height="130" fill="#94a3b8" stroke="#334155" stroke-width="1.5"/>
      <text x="102" y="40" font-size="12" font-family="sans-serif" fill="#1e293b" text-anchor="middle" font-weight="bold">Electrode A ({anode_sym})</text>
      <text x="115" y="195" font-size="11" font-family="sans-serif" fill="#2563eb" text-anchor="middle">1 M {anode_sym}²⁺(aq)</text>

      <!-- Beaker 2 (Right: Cathode) -->
      <rect x="280" y="90" width="130" height="130" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
      <rect x="320" y="50" width="24" height="130" fill="#d97706" stroke="#78350f" stroke-width="1.5"/>
      <text x="332" y="40" font-size="12" font-family="sans-serif" fill="#1e293b" text-anchor="middle" font-weight="bold">Electrode B ({cath_sym})</text>
      <text x="345" y="195" font-size="11" font-family="sans-serif" fill="#dc2626" text-anchor="middle">1 M {cath_sym}²⁺(aq)</text>

      <!-- Salt Bridge -->
      <path d="M 145,130 L 145,80 Q 145,65 160,65 L 300,65 Q 315,65 315,80 L 315,130" fill="none" stroke="#64748b" stroke-width="14" stroke-linecap="round"/>
      <path d="M 145,130 L 145,80 Q 145,65 160,65 L 300,65 Q 315,65 315,80 L 315,130" fill="none" stroke="#f1f5f9" stroke-width="8" stroke-linecap="round"/>
      <text x="230" y="58" font-size="11" font-family="sans-serif" fill="#475569" text-anchor="middle" font-weight="bold">Salt Bridge (KNO₃)</text>

      <!-- External Circuit with Voltmeter -->
      <polyline points="102,50 102,15 205,15" fill="none" stroke="#1e293b" stroke-width="2"/>
      <polyline points="255,15 332,15 332,50" fill="none" stroke="#1e293b" stroke-width="2"/>
      <circle cx="230" cy="15" r="16" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>
      <text x="230" y="20" font-size="13" font-family="sans-serif" fill="#1e293b" text-anchor="middle" font-weight="bold">V</text>
      <text x="230" y="-2" font-size="10" font-family="sans-serif" fill="#059669" text-anchor="middle">{_fmt_sa(ecell)} V</text>

      <!-- Electron Flow Arrow -->
      <line x1="130" y1="8" x2="180" y2="8" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="155" y="3" font-size="9" font-family="sans-serif" fill="#2563eb" text-anchor="middle">e⁻ flow →</text>
    </svg>
    """)

    prompt = (
        f"In the accompanying diagram, an operational standard galvanic cell is depicted featuring "
        f"Electrode A ({anode_data['name']}, {anode_sym}) and Electrode B ({cath_data['name']}, {cath_sym}) "
        f"coupled via a salt bridge containing potassium nitrate ($\\text{{KNO}}_3$).\n\n"
        f"1. Identify the anode and the cathode in this cell setup.\n"
        f"2. Write down the symbol of the electrode that acts as the positive terminal of the cell.\n"
        f"3. Write down the oxidation half-reaction occurring at Electrode A.\n"
        f"4. Calculate the theoretical voltmeter reading ($E^\\circ_{{\\text{{cell}}}}$) under standard conditions.\n"
        f"5. State the direction in which potassium ions ($\\text{{K}}^+$) migrate from the salt bridge."
    )

    ans_latex = (
        rf"1.\; \text{{Anode: Electrode A (}}\text{{{anode_sym}}}\text{{); Cathode: Electrode B (}}\text{{{cath_sym}}}\text{{).}}\n"
        rf"2.\; \text{{Positive terminal: Electrode B (}}\text{{{cath_sym}}}\text{{, cathode).}}\n"
        rf"3.\; \text{{{anode_sym}}}(s) \to \text{{{anode_sym}}}^{{2+}}(aq) + 2e^-\n"
        rf"4.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = {_fmt_sa(cath_data['e0'])} - ({_fmt_sa(anode_data['e0'])}) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"5.\; \text{{Potassium ions (}}\text{{K}}^+\text{{, cations) migrate toward the cathode half-cell (Beaker B containing }} \text{{{cath_sym}}}^{{2+}}\text{{) to replenish positive charge consumed by reduction.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of Anode A and Cathode B", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Positive terminal identification (Cathode B)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Oxidation half-reaction at Electrode A", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Voltmeter reading: {_fmt_sa(ecell)} V", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "K+ cation migration toward cathode half-cell B", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_volts", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The half-cell with the more negative potential is the anode (Electrode A).",
        "tier_2": "Cations in the salt bridge ($K^+$) migrate toward the cathode (Beaker B).",
        "tier_3": f"Anode = {anode_sym}, Cathode = {cath_sym}, $E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_24_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_24_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "24_galvanic_cell_with_seed_varied_inline_diagram",
        "learning_objective_id": "ps12_ec_24_inline_diagram",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_salt_bridge_ion_migration", "misidentified_positive_terminal_in_galvanic_cell"],
        "keywords": ["galvanic cell diagram", "salt bridge migration", "voltmeter reading", "positive terminal"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg},
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 25: Galvanic cell comprehensive 5-part rider
def _b25_galvanic_cell_comprehensive_5_part_rider(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Mg", "Ag"), ("Al", "Cu"), ("Zn", "Ag"), ("Ni", "Ag")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]
    e0_a = anode_data["e0"]
    e0_c = cath_data["e0"]
    ecell = round(e0_c - e0_a, 2)

    prompt = (
        f"A standard galvanic cell is set up consisting of a {anode_data['name']} ({anode_sym}) half-cell and a "
        f"{cath_data['name']} ({cath_sym}) half-cell.\n\n"
        f"1. State the energy conversion taking place inside this cell.\n"
        f"2. Write down the standard cell notation for this cell.\n"
        f"3. Write down the overall balanced equation for the cell reaction.\n"
        f"4. Calculate the initial electromotive force ($E^\\circ_{{\\text{{cell}}}}$) of the cell.\n"
        f"5. The cell operates until dynamic chemical equilibrium is established. Write down the voltmeter reading at equilibrium."
    )

    ans_latex = (
        rf"1.\; \text{{Chemical energy is converted into electrical energy.}}\n"
        rf"2.\; \text{{{anode_sym}}}(s) \mid \text{{{anode_sym}}}^{{2+}}(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \\parallel \text{{{cath_sym}}}^+(aq, 1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}) \mid \text{{{cath_sym}}}(s)\n"
        rf"3.\; \text{{{anode_sym}}}(s) + 2\text{{{cath_sym}}}^+(aq) \to \text{{{anode_sym}}}^{{2+}}(aq) + 2\text{{{cath_sym}}}(s)\n"
        rf"4.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"5.\; \mathbf{{0{{,}}00\text{{ V}}}} \text{{ (at chemical equilibrium, the rate of forward and reverse reactions are equal and the driving force is zero).}}"
    )

    marking_schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Energy conversion: chemical to electrical energy", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Standard cell notation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Overall balanced equation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Cell potential calculation: {_fmt_sa(ecell)} V", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Equilibrium EMF: 0.00 V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_equilibrium_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Anode is on the left in cell notation. Cell potential is $E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$.",
        "tier_2": "At chemical equilibrium, the cell potential is always $0{,}00\\text{ V}$.",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$, equilibrium voltage = $0{{,}}00\\text{{ V}}$.",
    }

    return {
        "id": f"ps12_ec_25_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_25_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "25_galvanic_cell_comprehensive_5_part_rider",
        "learning_objective_id": "ps12_ec_25_comprehensive_rider",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_voltage_drops_to_zero_at_equilibrium", "inverted_cell_notation_order"],
        "keywords": ["comprehensive rider", "cell notation", "EMF calculation", "equilibrium potential"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 7,
    }


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_galvanic_cell_definition_energy_conversion": _b01_galvanic_cell_definition_energy_conversion,
    "02_standard_conditions_galvanic_cells": _b02_standard_conditions_galvanic_cells,
    "03_standard_hydrogen_electrode_she_reference": _b03_standard_hydrogen_electrode_she_reference,
    "04_anode_and_cathode_definitions_redox": _b04_anode_and_cathode_definitions_redox,
    "05_electron_flow_direction_external_circuit": _b05_electron_flow_direction_external_circuit,
    "06_table_of_standard_reduction_potentials_table_4a_4b": _b06_table_of_standard_reduction_potentials_table_4a_4b,
    "07_predicting_spontaneity_from_reduction_potentials": _b07_predicting_spontaneity_from_reduction_potentials,
    "08_daniell_cell_zn_cu_reactions_and_observations": _b08_daniell_cell_zn_cu_reactions_and_observations,
    "09_mg_cu_galvanic_cell_high_potential_pair": _b09_mg_cu_galvanic_cell_high_potential_pair,
    "10_al_cu_galvanic_cell_electron_balancing": _b10_al_cu_galvanic_cell_electron_balancing,
    "11_ni_ag_galvanic_cell_stoichiometry": _b11_ni_ag_galvanic_cell_stoichiometry,
    "12_pb_ag_galvanic_cell_stoichiometry": _b12_pb_ag_galvanic_cell_stoichiometry,
    "13_fe_cu_galvanic_cell_corrosion_protection": _b13_fe_cu_galvanic_cell_corrosion_protection,
    "14_standard_cell_notation_solid_electrodes": _b14_standard_cell_notation_solid_electrodes,
    "15_standard_cell_notation_inert_platinum_electrodes": _b15_standard_cell_notation_inert_platinum_electrodes,
    "16_cell_potential_formula_ecell_ecathode_minus_eanode": _b16_cell_potential_formula_ecell_ecathode_minus_eanode,
    "17_determining_unknown_electrode_potential_from_ecell": _b17_determining_unknown_electrode_potential_from_ecell,
    "18_effect_of_concentration_changes_on_cell_potential": _b18_effect_of_concentration_changes_on_cell_potential,
    "19_effect_of_electrode_surface_area_on_potential_and_current": _b19_effect_of_electrode_surface_area_on_potential_and_current,
    "20_cell_potential_drop_to_zero_at_chemical_equilibrium": _b20_cell_potential_drop_to_zero_at_chemical_equilibrium,
    "21_mass_changes_of_electrodes_quantitative_stoichiometry": _b21_mass_changes_of_electrodes_quantitative_stoichiometry,
    "22_faraday_charge_and_electron_moles_in_galvanic_cell": _b22_faraday_charge_and_electron_moles_in_galvanic_cell,
    "23_halide_half_cells_chlorine_bromine_iodine_potentials": _b23_halide_half_cells_chlorine_bromine_iodine_potentials,
    "24_galvanic_cell_with_seed_varied_inline_diagram": _b24_galvanic_cell_with_seed_varied_inline_diagram,
    "25_galvanic_cell_comprehensive_5_part_rider": _b25_galvanic_cell_comprehensive_5_part_rider,
}
