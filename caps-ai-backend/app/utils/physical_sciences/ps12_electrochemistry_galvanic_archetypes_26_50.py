"""Physical Sciences (Grade 12 Term 3) — Electrochemical Reactions Archetypes 26 to 50.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Topic: Electrochemical Reactions (Salt Bridge, Electrolytic Cells, Industrial Electrochemistry).
- Subskills 26–50: Salt bridge functions and mechanics (ion migration, K+, NO3-, electrical neutrality),
  salt bridge removal, electrolyte precipitation incompatibility, cell internal resistance,
  electrolytic cell definitions, energy conversion (electrical to chemical), non-spontaneous reactions,
  polarity comparisons (galvanic vs electrolytic), electrolysis of molten NaCl (Downs cell),
  electrolysis of aqueous CuCl2, competing reactions in aqueous electrolytes, industrial electroplating
  (silver, nickel), quantitative electroplating (Faraday's law), electrorefining of blister copper,
  anode sludge recovery (Au, Ag, Pt), Hall-Héroult extraction of aluminium (bauxite, cryolite flux,
  carbon anode consumption into CO2), chlor-alkali membrane cell (Cl2, H2, NaOH), composite galvanic-electrolytic
  circuits, capstone synthesis rider, and diagnostic autopsy.

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


# Archetype 26: Salt bridge functions and mechanics
def _b26_salt_bridge_functions_and_mechanics(r: random.Random) -> Dict[str, Any]:
    salt_choice = r.choice(["potassium nitrate (\\text{KNO}_3)", "potassium chloride (\\text{KCl})"])

    prompt = (
        f"A standard galvanic cell features two half-cells connected externally by copper wires and internally by a U-tube "
        f"salt bridge containing {salt_choice} suspended in agar gel.\n\n"
        f"1. State the **two primary functions** of the salt bridge in an operating galvanic cell.\n"
        f"2. Explain why the electrolyte used in the salt bridge must be chemically inert with respect to the ions in both half-cells.\n"
        f"3. State what would happen to the reading on the voltmeter if the salt bridge is lifted out of the solutions."
    )

    ans_latex = (
        rf"1.\; \text{{(i) Completes the electrical circuit by providing an internal conduction path for mobile ions.}}\n"
        rf"\quad \text{{(ii) Maintains electrical neutrality in both half-cell solutions by allowing the migration of cations and anions.}}\n"
        rf"2.\; \text{{The salt bridge ions must not react or form insoluble precipitates with the ions present in the half-cells, which would reduce ion concentrations and increase internal resistance.}}\n"
        rf"3.\; \text{{The voltmeter reading drops immediately to }} \mathbf{{0{{,}}00\text{{ V}}}} \text{{ (the circuit is broken).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Function 1: Completes the electrical circuit", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Function 2: Maintains electrical neutrality via ion migration", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Inert electrolyte explanation (avoid precipitation/reactions)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Voltmeter reading drops to 0.00 V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_electrical_neutrality", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The salt bridge completes the circuit and maintains electrical neutrality.",
        "tier_2": "Without the salt bridge, charge would quickly build up in both beakers, stopping electron flow.",
        "tier_3": "Functions: complete circuit and maintain electrical neutrality. Voltage drops to $0{,}00\\text{ V}$.",
    }

    return {
        "id": f"ps12_ec_26_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_26_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "26_salt_bridge_functions_and_mechanics",
        "learning_objective_id": "ps12_ec_26_salt_bridge_functions",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_electrons_travel_through_salt_bridge", "forgot_electrical_neutrality_role"],
        "keywords": ["salt bridge", "completing circuit", "electrical neutrality", "inert electrolyte"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 27: Salt bridge ion migration anion and cation directions
def _b27_salt_bridge_ion_migration_anion_cation(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Cu"), ("Al", "Ag"), ("Ni", "Ag")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]

    prompt = (
        f"A galvanic cell consists of a {anode_data['name']} ({anode_sym}) anode half-cell and a "
        f"{cath_data['name']} ({cath_sym}) cathode half-cell connected by a salt bridge filled with potassium nitrate ($\\text{{KNO}}_3$).\n\n"
        f"1. State the direction in which the **anions** ($\\text{{NO}}_3^-$) migrate from the salt bridge (toward which half-cell).\n"
        f"2. Explain why anions migrate toward this specific half-cell in terms of the charge balance.\n"
        f"3. State the direction in which the **cations** ($\\text{{K}}^+$) migrate from the salt bridge (toward which half-cell).\n"
        f"4. Explain why cations migrate toward this specific half-cell in terms of the charge balance."
    )

    ans_latex = (
        rf"1.\; \text{{Anions (}}\text{{NO}}_3^-\text{{) migrate toward the }} \mathbf{{{anode_sym}\text{{ (anode) half-cell}}}}.\n"
        rf"2.\; \text{{At the anode, oxidation generates positive }} \text{{{anode_sym}}}^{{2+}}\text{{ ions, creating an excess of positive charge. Anions migrate in to neutralize this positive charge buildup.}}\n"
        rf"3.\; \text{{Cations (}}\text{{K}}^+\text{{) migrate toward the }} \mathbf{{{cath_sym}\text{{ (cathode) half-cell}}}}.\n"
        rf"4.\; \text{{At the cathode, reduction consumes positive }} \text{{{cath_sym}}}^{{2+}}\text{{ ions to form neutral metal, leaving an excess of negative spectator anions. Cations migrate in to replace the lost positive charge and maintain neutrality.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Anions migrate to {anode_sym} anode half-cell", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Neutralizing excess positive cations at anode", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Cations migrate to {cath_sym} cathode half-cell", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Replacing consumed positive cations at cathode", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "reversed_anion_and_cation_migration_destinations", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Memory rule: Anions $\\to$ Anode; Cations $\\to$ Cathode.",
        "tier_2": "At the anode, oxidation produces positive ions (needs negative $\\text{NO}_3^-$). At the cathode, positive ions are consumed (needs positive $\\text{K}^+$).",
        "tier_3": f"$\\text{{NO}}_3^- \\to {anode_sym}$ anode; $\\text{{K}}^+ \\to {cath_sym}$ cathode.",
    }

    return {
        "id": f"ps12_ec_27_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_27_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "27_salt_bridge_ion_migration_anion_cation",
        "learning_objective_id": "ps12_ec_27_ion_migration",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_anion_and_cation_migration", "confused_electron_flow_with_ion_migration"],
        "keywords": ["salt bridge", "ion migration", "anions to anode", "cations to cathode"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 28: Salt bridge removal effect on current and voltage
def _b28_salt_bridge_removal_effect_on_current(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Cu"), ("Al", "Cu")])
    anode_sym, cath_sym = pair
    ecell = round(STANDARD_REDUCTION_DATA[cath_sym]["e0"] - STANDARD_REDUCTION_DATA[anode_sym]["e0"], 2)

    prompt = (
        f"A galvanic cell ($\\text{{{anode_sym}}} \\mid \\text{{{anode_sym}}}^{{2+}} \\parallel \\text{{{cath_sym}}}^{{2+}} \\mid \\text{{{cath_sym}}}$) "
        f"is operating under standard conditions, delivering an initial electromotive force of $E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$. "
        f"A laboratory learner suddenly removes the salt bridge from the two beakers.\n\n"
        f"1. State what happens to the electric current flowing through the external circuit immediately after the salt bridge is removed.\n"
        f"2. State what happens to the reading on a voltmeter connected across the two terminals immediately after removal.\n"
        f"3. Explain why the cell stops functioning in terms of internal charge accumulation and circuit continuity."
    )

    ans_latex = (
        rf"1.\; \text{{The electric current drops immediately to }} \mathbf{{0\text{{ A}}}}.\n"
        rf"2.\; \text{{The voltmeter reading drops immediately to }} \mathbf{{0{{,}}00\text{{ V}}}}.\n"
        rf"3.\; \text{{Removing the salt bridge breaks the internal electrical circuit. Without ion migration, any initial oxidation would create unneutralized positive charge in the anode beaker and unneutralized negative charge in the cathode beaker, instantly establishing an opposing electric field that halts further electron transfer.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Current drops to 0 A", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Voltage drops to 0.00 V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Circuit broken / discontinuous path", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Opposing electric field from charge buildup explanation", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "claimed_cell_continues_delivering_current", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Without the salt bridge, the electrical circuit is open (broken).",
        "tier_2": "Current is $0\\text{ A}$ and voltage drops to $0{,}00\\text{ V}$.",
        "tier_3": "Open circuit + immediate charge accumulation halts electron transfer.",
    }

    return {
        "id": f"ps12_ec_28_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_28_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "28_salt_bridge_removal_effect_on_current",
        "learning_objective_id": "ps12_ec_28_salt_bridge_removal",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["thought_voltage_remains_intact_without_salt_bridge", "failed_to_recognize_open_circuit"],
        "keywords": ["salt bridge removal", "open circuit", "zero voltage", "charge accumulation"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 29: Salt bridge electrolyte precipitation incompatibility
def _b29_salt_bridge_electrolyte_precipitation_incompatibility(r: random.Random) -> Dict[str, Any]:
    cell_metal = r.choice(["Ag", "Pb"])
    precip_color = "white precipitate of AgCl" if cell_metal == "Ag" else "white precipitate of PbCl2"
    precip_formula = "AgCl" if cell_metal == "Ag" else "PbCl_2"
    cell_ion = "\\text{Ag}^+" if cell_metal == "Ag" else "\\text{Pb}^{2+}"

    prompt = (
        f"A learner constructs a standard galvanic cell featuring a {STANDARD_REDUCTION_DATA[cell_metal]['name']} ({cell_metal}) "
        f"half-cell. By mistake, the learner prepares the salt bridge using potassium chloride ($\\text{{KCl}}$) instead of potassium nitrate ($\\text{{KNO}}_3$).\n\n"
        f"1. Explain why potassium chloride is unsuitable for this specific cell.\n"
        f"2. Write down the chemical formula and appearance of the precipitate that forms at the junction of the salt bridge and the {cell_metal} half-cell.\n"
        f"3. Explain the negative effect this precipitation reaction has on the cell potential ($E_{{\\text{{cell}}}}$) and the internal resistance of the cell."
    )

    ans_latex = (
        rf"1.\; \text{{Chloride ions (}}\text{{Cl}}^-\text{{) from }} \text{{KCl}} \text{{ react with }} {cell_ion} \text{{ ions to form an insoluble precipitate, removing active ions from solution and clogging the salt bridge pores.}}\n"
        rf"2.\; \text{{Formula: }} \mathbf{{\text{{{precip_formula}}}(s)}}; \quad \text{{Appearance: }} {precip_color}.\n"
        rf"3.\; \text{{Precipitation drastically reduces }}[{cell_ion}]\text{{, which shifts the equilibrium reverse according to Le Chatelier's Principle, reducing the cell potential (}}E_{{\text{{cell}}}}\text{{). Furthermore, the solid precipitate blocks ion migration in the salt bridge, substantially increasing internal resistance.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Incompatibility explanation (precipitation of insoluble chloride)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Precipitate formula: {precip_formula}(s)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Decreased cell potential via Le Chatelier", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Increased internal resistance from blocked pores", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_solubility_prediction", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall solubility rules: Silver chloride ($\\text{AgCl}$) and lead(II) chloride ($\\text{PbCl}_2$) are insoluble.",
        "tier_2": "Precipitation lowers $[\\text{Ag}^+]$ or $[\\text{Pb}^{2+}]$, reducing $E_{\\text{cell}}$ and clogging the salt bridge.",
        "tier_3": f"Precipitate: $\\text{{{precip_formula}}}(s)$. Increases internal resistance.",
    }

    return {
        "id": f"ps12_ec_29_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_29_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "29_salt_bridge_electrolyte_precipitation_incompatibility",
        "learning_objective_id": "ps12_ec_29_salt_bridge_incompatibility",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_all_chlorides_are_soluble", "overlooked_effect_of_precipitation_on_internal_resistance"],
        "keywords": ["precipitation", "KCl incompatibility", "silver chloride", "internal resistance"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 30: Internal resistance of galvanic cell
def _b30_internal_resistance_of_galvanic_cell(r: random.Random) -> Dict[str, Any]:
    emf = 1.10  # Zn-Cu cell
    r_int = r.choice([0.5, 0.8, 1.0, 1.2, 1.5])  # ohms
    r_load = r.choice([4.0, 5.0, 8.0, 10.0])  # ohms

    i_current = emf / (r_load + r_int)
    v_load = i_current * r_load
    v_lost = i_current * r_int

    prompt = (
        f"A standard Daniell cell has an open-circuit electromotive force of $\\mathcal{{E}} = {_fmt_sa(emf)}\\text{{ V}}$. "
        f"When connected across an external resistor of resistance $R = {_fmt_sa(r_load)}\\ \\Omega$, an ammeter measures "
        f"a current of $I = {_fmt_sa(i_current, 3)}\\text{{ A}}$ in the circuit.\n\n"
        f"1. Define the **internal resistance** ($r$) of an electrochemical cell in words.\n"
        f"2. Calculate the terminal potential difference ($V_{{\\text{{load}}}}$) across the external resistor.\n"
        f"3. Calculate the lost volts ($V_{{\\text{{lost}}}}$) inside the cell.\n"
        f"4. Calculate the internal resistance ($r$) of the galvanic cell."
    )

    ans_latex = (
        rf"1.\; \text{{The opposition to the flow of charge (ions) within the electrolyte solutions and salt bridge inside the cell itself.}}\n"
        rf"2.\; V_{{\text{{load}}}} = I R = ({_fmt_sa(i_current, 3)})({_fmt_sa(r_load)}) = {_fmt_sa(v_load, 2)}\text{{ V}}\n"
        rf"3.\; V_{{\text{{lost}}}} = \\mathcal{{E}} - V_{{\text{{load}}}} = {_fmt_sa(emf)} - {_fmt_sa(v_load, 2)} = {_fmt_sa(v_lost, 2)}\text{{ V}}\n"
        rf"4.\; r = \frac{{V_{{\text{{lost}}}}}}{{I}} = \frac{{{_fmt_sa(v_lost, 2)}}}{{{_fmt_sa(i_current, 3)}}} = {_fmt_sa(r_int, 2)}\\ \\Omega"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of internal resistance", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Terminal voltage: {_fmt_sa(v_load, 2)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Lost volts: {_fmt_sa(v_lost, 2)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Internal resistance: {_fmt_sa(r_int, 2)} ohms", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_resistance_units_ohms", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Use the relationship $\\mathcal{E} = V_{\\text{load}} + V_{\\text{lost}} = I(R + r)$.",
        "tier_2": "Calculate $V_{\\text{load}} = IR$, then $V_{\\text{lost}} = \\mathcal{E} - V_{\\text{load}}$.",
        "tier_3": f"$V_{{\\text{{load}}}} = {_fmt_sa(v_load, 2)}\\text{{ V}}$, $r = {_fmt_sa(r_int, 2)}\\ \\Omega$.",
    }

    return {
        "id": f"ps12_ec_30_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_30_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "30_internal_resistance_of_galvanic_cell",
        "learning_objective_id": "ps12_ec_30_internal_resistance",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_terminal_voltage_with_emf_under_load", "ignored_internal_resistance_in_galvanic_cells"],
        "keywords": ["internal resistance", "lost volts", "terminal voltage", "load resistance"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 31: Electrolytic cell definition and energy conversion
def _b31_electrolytic_cell_definition_and_energy_conversion(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An industrial chemical plant operates a bank of electrolytic cells connected to a direct current (DC) power source.\n\n"
        f"1. Define an **electrolytic cell** in words.\n"
        f"2. State the energy conversion that takes place inside an operating electrolytic cell.\n"
        f"3. State whether the redox reaction occurring in an electrolytic cell is **spontaneous** or **non-spontaneous**.\n"
        f"4. State the sign of the overall standard cell potential ($E^\\circ_{{\\text{{cell}}}}$) for the non-spontaneous reaction."
    )

    ans_latex = (
        rf"1.\; \text{{A cell in which electrical energy is converted into chemical energy through a non-spontaneous redox reaction driven by an external power source.}}\n"
        rf"2.\; \text{{Electrical energy is converted into chemical energy.}}\n"
        rf"3.\; \text{{Non-spontaneous (forced by an external DC supply).}}\n"
        rf"4.\; \text{{Negative (}}E^\circ_{{\text{{cell}}}} < 0\text{{).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of electrolytic cell", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Energy conversion: electrical to chemical energy", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Non-spontaneous reaction statement", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_electrolytic_cells_generate_electricity", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Electrolytic cells use an external DC source to drive non-spontaneous chemical reactions.",
        "tier_2": "Energy conversion: electrical energy $\\to$ chemical energy.",
        "tier_3": "Electrolytic = electrical $\\to$ chemical (non-spontaneous, $E^\\circ < 0$).",
    }

    return {
        "id": f"ps12_ec_31_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_31_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "31_electrolytic_cell_definition_and_energy_conversion",
        "learning_objective_id": "ps12_ec_31_electrolytic_definition",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_electrolytic_with_galvanic_cell", "assumed_reactions_in_electrolytic_cells_are_spontaneous"],
        "keywords": ["electrolytic cell", "energy conversion", "non-spontaneous", "DC power source"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 32: Galvanic vs electrolytic cell structural comparison
def _b32_galvanic_vs_electrolytic_cell_structural_comparison(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Tabulate the key differences between a **galvanic cell** and an **electrolytic cell** across the following four criteria:\n"
        f"1. Energy conversion\n"
        f"2. Spontaneity of chemical reaction\n"
        f"3. Polarity of the anode and cathode\n"
        f"4. Necessity of a salt bridge"
    )

    ans_latex = (
        rf"\begin{{array}}{{|l|l|l|}}\n"
        rf"\hline\n"
        rf"\textbf{{Criterion}} & \textbf{{Galvanic Cell}} & \textbf{{Electrolytic Cell}} \\\\\n"
        rf"\hline\n"
        rf"\text{{1. Energy conversion}} & \text{{Chemical }}\\to\\text{{ Electrical}} & \text{{Electrical }}\\to\\text{{ Chemical}} \\\\\n"
        rf"\hline\n"
        rf"\text{{2. Spontaneity}} & \text{{Spontaneous (}}E^\circ > 0\text{{)}} & \text{{Non-spontaneous (}}E^\circ < 0\text{{)}} \\\\\n"
        rf"\hline\n"
        rf"\text{{3. Electrode polarities}} & \text{{Anode: (-); Cathode: (+)}} & \text{{Anode: (+); Cathode: (-)}} \\\\\n"
        rf"\hline\n"
        rf"\text{{4. Salt bridge}} & \text{{Essential (separate beakers)}} & \text{{Not needed (single container)}} \\\\\n"
        rf"\hline\n"
        rf"\end{{array}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Energy conversion comparison", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Spontaneity comparison", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Polarity comparison (Anode negative in Galvanic, positive in Electrolytic)", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Salt bridge comparison", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "reversed_polarities", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Notice that oxidation is ALWAYS at the anode and reduction is ALWAYS at the cathode for BOTH cells.",
        "tier_2": "In galvanic cells, the anode is negative. In electrolytic cells, the anode is connected to the positive terminal.",
        "tier_3": "Review the 4 rows: Energy, Spontaneity, Polarity, Salt bridge requirement.",
    }

    return {
        "id": f"ps12_ec_32_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_32_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "32_galvanic_vs_electrolytic_cell_structural_comparison",
        "learning_objective_id": "ps12_ec_32_cell_comparison",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["swapped_anode_and_cathode_polarities_between_cells", "thought_salt_bridge_needed_in_electrolytic_cell"],
        "keywords": ["galvanic vs electrolytic", "comparison table", "polarities", "spontaneity"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 33: Electrolytic cell anode and cathode polarities
def _b33_electrolytic_cell_anode_and_cathode_polarities(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An electrolytic cell is connected to a $12\\text{{ V}}$ direct current (DC) battery.\n\n"
        f"1. State whether the anode is connected to the positive or negative terminal of the DC battery.\n"
        f"2. State whether the cathode is connected to the positive or negative terminal of the DC battery.\n"
        f"3. Explain why oxidation still occurs at the anode despite it having a positive polarity.\n"
        f"4. State the mnemonic or fundamental rule that applies to oxidation and reduction electrodes in **all** electrochemical cells."
    )

    ans_latex = (
        rf"1.\; \text{{The anode is connected to the }} \mathbf{{\text{{positive terminal}}}} \text{{ of the battery.}}\n"
        rf"2.\; \text{{The cathode is connected to the }} \mathbf{{\text{{negative terminal}}}} \text{{ of the battery.}}\n"
        rf"3.\; \text{{The positive terminal of the power supply pulls electrons away from the anode, forcing anions in the solution to lose electrons (oxidation) at this electrode.}}\n"
        rf"4.\; \text{{'An Ox' and 'Red Cat': Oxidation }} \mathbf{{\text{{always}}}} \text{{ occurs at the anode, and reduction }} \mathbf{{\text{{always}}}} \text{{ occurs at the cathode, in every type of cell.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Anode connected to positive terminal", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Cathode connected to negative terminal", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Oxidation explanation at positive electrode", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Universal rule: An Ox and Red Cat in all cells", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_reduction_occurs_at_anode", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "In electrolytic cells, the power source dictates polarity: Anode = positive (+), Cathode = negative (-).",
        "tier_2": "Oxidation ALWAYS occurs at the anode, regardless of whether the cell is galvanic or electrolytic.",
        "tier_3": "Anode = positive (oxidation); Cathode = negative (reduction).",
    }

    return {
        "id": f"ps12_ec_33_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_33_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "33_electrolytic_cell_anode_and_cathode_polarities",
        "learning_objective_id": "ps12_ec_33_electrolytic_polarities",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_anode_polarity_in_electrolytic_cells", "thought_anode_undergoes_reduction_in_electrolytic_cells"],
        "keywords": ["electrolytic polarity", "DC battery", "An Ox", "Red Cat"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 34: Electrolysis of molten sodium chloride (Downs cell)
def _b34_electrolysis_of_molten_sodium_chloride_downs_cell(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In industrial metallurgy (the Downs cell process), molten sodium chloride ($\\text{{NaCl}}(l)$) "
        f"is electrolyzed using inert electrodes at approximately $800^\\circ\\text{{C}}$.\n\n"
        f"1. Write down the reduction half-reaction occurring at the cathode.\n"
        f"2. Write down the oxidation half-reaction occurring at the anode.\n"
        f"3. Write down the overall balanced chemical equation for the decomposition of molten sodium chloride.\n"
        f"4. State the physical states of the products formed at the cathode and anode.\n"
        f"5. Explain why the sodium chloride must be in the **molten** state rather than solid form."
    )

    ans_latex = (
        rf"1.\; \text{{Cathode (reduction): }} \text{{Na}}^+(l) + e^- \to \text{{Na}}(l)\n"
        rf"2.\; \text{{Anode (oxidation): }} 2\text{{Cl}}^-(l) \to \text{{Cl}}_2(g) + 2e^-\n"
        rf"3.\; \text{{Overall reaction: }} 2\text{{NaCl}}(l) \to 2\text{{Na}}(l) + \text{{Cl}}_2(g)\n"
        rf"4.\; \text{{Cathode product: liquid sodium metal (}}\text{{Na}}(l)\text{{); Anode product: chlorine gas (}}\text{{Cl}}_2(g)\text{{).}}\n"
        rf"5.\; \text{{In the solid state, ions are locked in fixed positions in the crystal lattice and cannot conduct electricity. Melting frees the ions (}}\text{{Na}}^+ \text{{ and }} \text{{Cl}}^-\text{{) so they are mobile and can migrate to the electrodes.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Cathode half-reaction: Na+ + e- -> Na(l)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Anode half-reaction: 2Cl- -> Cl2(g) + 2e-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Overall equation: 2NaCl -> 2Na + Cl2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Physical states: Na liquid and Cl2 gas", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Molten state explanation (free mobile ions for electrical conduction)", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_chlorine_diatomic_subscript", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Sodium ions gain electrons to form sodium metal; chloride ions lose electrons to form chlorine gas.",
        "tier_2": "Chlorine exists as a diatomic gas: $\\text{Cl}_2$. Melting frees ions to move.",
        "tier_3": "Cathode: $\\text{Na}^+ + e^- \\to \\text{Na}(l)$; Anode: $2\\text{Cl}^- \\to \\text{Cl}_2(g) + 2e^-$.",
    }

    return {
        "id": f"ps12_ec_34_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_34_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "34_electrolysis_of_molten_sodium_chloride_downs_cell",
        "learning_objective_id": "ps12_ec_34_molten_nacl",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["wrote_chlorine_as_monatomic_cl", "assumed_solid_salts_conduct_electricity"],
        "keywords": ["Downs cell", "molten sodium chloride", "mobile ions", "liquid sodium"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 35: Electrolysis of aqueous copper(II) chloride
def _b35_electrolysis_of_aqueous_copper_chloride(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A laboratory electrolytic cell consists of two inert carbon (graphite) electrodes immersed in a "
        f"blue aqueous solution of copper(II) chloride ($\\text{{CuCl}}_2(aq)$) connected to a DC power supply.\n\n"
        f"1. Write down the reduction half-reaction occurring at the cathode.\n"
        f"2. Write down the oxidation half-reaction occurring at the anode.\n"
        f"3. State the observation made at the cathode electrode during electrolysis.\n"
        f"4. State the observation made at the anode electrode, including the distinctive odour or test for the gas produced.\n"
        f"5. State what happens to the blue colour of the electrolyte solution as electrolysis continues, and explain why."
    )

    ans_latex = (
        rf"1.\; \text{{Cathode (reduction): }} \text{{Cu}}^{{2+}}(aq) + 2e^- \to \text{{Cu}}(s)\n"
        rf"2.\; \text{{Anode (oxidation): }} 2\text{{Cl}}^-(aq) \to \text{{Cl}}_2(g) + 2e^-\n"
        rf"3.\; \text{{Cathode observation: A reddish-brown (pinkish-brown) metallic deposit forms on the carbon rod.}}\n"
        rf"4.\; \text{{Anode observation: Bubbles of a pale yellow-green gas with a pungent, choking smell (chlorine) are released; the gas bleaches damp blue litmus paper.}}\n"
        rf"5.\; \text{{The blue colour fades (becomes lighter/colourless) because hydrated copper(II) ions (}}\text{{Cu}}^{{2+}}(aq)\text{{) are continuously removed from solution as metallic copper.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Cathode half-reaction: Cu2+ + 2e- -> Cu(s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Anode half-reaction: 2Cl- -> Cl2(g) + 2e-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Red-brown copper deposit observation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Chlorine gas bubbles and bleach test/odour", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Blue colour fading due to Cu2+ consumption", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_chlorine_gas_test_or_colour", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$\\text{Cu}^{2+}$ ions are reduced to copper metal (red-brown deposit) at the cathode.",
        "tier_2": "$\\text{Cl}^-$ ions are oxidized to chlorine gas (bubbles, pungent odour) at the anode.",
        "tier_3": "Cathode: $\\text{Cu}^{2+} + 2e^- \\to \\text{Cu}$. Anode: $2\\text{Cl}^- \\to \\text{Cl}_2 + 2e^-$. Blue colour fades.",
    }

    return {
        "id": f"ps12_ec_35_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_35_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "35_electrolysis_of_aqueous_copper_chloride",
        "learning_objective_id": "ps12_ec_35_aqueous_cucl2",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_anode_and_cathode_products_in_cucl2", "thought_carbon_rod_dissolved"],
        "keywords": ["aqueous CuCl2", "copper deposit", "chlorine gas", "colour fading"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 36: Electrolysis competing reactions (water vs halide / metal)
def _b36_electrolysis_competing_reactions_water_vs_halide(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A chemist performs the electrolysis of a concentrated aqueous solution of sodium chloride ($\\text{{NaCl}}(aq)$, brine).\n"
        f"Relevant standard reduction potentials from Table 4A/4B are:\n"
        f"- $\\text{{Na}}^+(aq) + e^- \\rightleftharpoons \\text{{Na}}(s): E^\\circ = -2{{,}}71\\text{{ V}}$\n"
        f"- $2\\text{{H}}_2\\text{{O}}(l) + 2e^- \\rightleftharpoons \\text{{H}}_2(g) + 2\\text{{OH}}^-(aq): E^\\circ = -0{{,}}83\\text{{ V}}$\n"
        f"- $\\text{{Cl}}_2(g) + 2e^- \\rightleftharpoons 2\\text{{Cl}}^-(aq): E^\\circ = +1{{,}}36\\text{{ V}}$\n"
        f"- $\\text{{O}}_2(g) + 4\\text{{H}}^+(aq) + 4e^- \\rightleftharpoons 2\\text{{H}}_2\\text{{O}}(l): E^\\circ = +1{{,}}23\\text{{ V}}$\n\n"
        f"1. Predict whether sodium metal ($\\text{{Na}}$) or hydrogen gas ($\\text{{H}}_2$) is produced at the cathode. Justify using $E^\\circ$ values.\n"
        f"2. Write down the reduction half-reaction taking place at the cathode.\n"
        f"3. In concentrated brine, chloride ions are oxidized at the anode rather than water molecules. Write down the anode half-reaction.\n"
        f"4. Name the third valuable industrial chemical that remains in solution after electrolysis of brine."
    )

    ans_latex = (
        rf"1.\; \text{{Hydrogen gas (}}\text{{H}}_2\text{{) is produced. Water has a far less negative reduction potential (}}-0{{,}}83\text{{ V) than sodium ions (}}-2{{,}}71\text{{ V), meaning water is a much stronger oxidizing agent and is preferentially reduced.}}\n"
        rf"2.\; 2\text{{H}}_2\text{{O}}(l) + 2e^- \to \text{{H}}_2(g) + 2\text{{OH}}^-(aq)\n"
        rf"3.\; 2\text{{Cl}}^-(aq) \to \text{{Cl}}_2(g) + 2e^-\n"
        rf"4.\; \text{{Sodium hydroxide (}}\text{{NaOH}}\text{{) (caustic soda).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Hydrogen gas prediction with E0 comparison", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Water reduction half-reaction", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Chloride oxidation half-reaction", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Identification of sodium hydroxide (NaOH)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "predicted_sodium_metal_formation_in_water", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "In aqueous solution, water is reduced much more easily ($-0{,}83\\text{ V}$) than $\\text{Na}^+$ ($-2{,}71\\text{ V}$).",
        "tier_2": "The cathode produces $\\text{H}_2(g)$ and $\\text{OH}^-$. The anode produces $\\text{Cl}_2(g)$.",
        "tier_3": "Products: $\\text{H}_2$, $\\text{Cl}_2$, and $\\text{NaOH}$ solution.",
    }

    return {
        "id": f"ps12_ec_36_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_36_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "36_electrolysis_competing_reactions_water_vs_halide",
        "learning_objective_id": "ps12_ec_36_competing_reactions",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_sodium_metal_forms_in_aqueous_electrolysis", "failed_to_compare_water_and_metal_reduction_potentials"],
        "keywords": ["brine electrolysis", "competing reactions", "chlor-alkali", "water reduction"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 37: Electroplating principles and setup
def _b37_electroplating_principles_and_setup(r: random.Random) -> Dict[str, Any]:
    plated_obj = r.choice(["brass door handle", "steel car key", "iron medallion", "zinc bolt"])
    coating_metal = r.choice(["copper", "chromium", "silver", "nickel"])

    prompt = (
        f"A manufacturing technician must coat a {plated_obj} with a thin, uniform protective layer of {coating_metal}.\n\n"
        f"1. Define **electroplating** in words.\n"
        f"2. State the two main industrial purposes of electroplating objects.\n"
        f"3. State which electrode (the anode or the cathode) the {plated_obj} must be connected to.\n"
        f"4. State the composition of the electrode connected to the other terminal of the power source.\n"
        f"5. State what type of electrolyte solution must be used in the electroplating bath."
    )

    ans_latex = (
        rf"1.\; \text{{The process of using electrolysis to coat a conductive object with a thin layer of metal.}}\n"
        rf"2.\; \text{{(i) To prevent corrosion (rusting/oxidation); (ii) To improve aesthetic appearance (decorative shine).}}\n"
        rf"3.\; \text{{The {plated_obj} must be connected as the }} \mathbf{{\text{{cathode}}}} \text{{ (negative terminal).}}\n"
        rf"4.\; \text{{The anode must be composed of a pure bar of }} \mathbf{{{coating_metal}}} \text{{ (the coating metal).}}\n"
        rf"5.\; \text{{An aqueous solution containing soluble ions of the coating metal (e.g. }} \text{{{coating_metal}}} \text{{ nitrate or sulfate).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of electroplating", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Purposes: corrosion prevention and decorative appearance", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Object to be plated = cathode", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Anode = pure {coating_metal}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Electrolyte = soluble salt of coating metal", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "connected_object_as_anode", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The object to be plated is always the CATHODE (negative terminal) where metal ions are reduced.",
        "tier_2": f"The anode is pure {coating_metal}, and the electrolyte contains {coating_metal} ions.",
        "tier_3": f"Object = Cathode; Anode = Pure {coating_metal}; Solution = {coating_metal} salt.",
    }

    return {
        "id": f"ps12_ec_37_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_37_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "37_electroplating_principles_and_setup",
        "learning_objective_id": "ps12_ec_37_electroplating_rules",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["connected_object_to_be_plated_to_positive_terminal", "used_insoluble_salt_electrolyte"],
        "keywords": ["electroplating", "cathode object", "anode sacrificial", "coating metal"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 38: Electroplating silver onto cutlery
def _b38_electroplating_silver_onto_cutlery(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A nickel-plated brass teapot is being silver-plated in an electroplating bath containing "
        f"silver nitrate solution ($\\text{{AgNO}}_3(aq)$).\n\n"
        f"1. Write down the reduction half-reaction taking place on the teapot surface.\n"
        f"2. Write down the oxidation half-reaction taking place at the pure silver anode.\n"
        f"3. State whether the concentration of silver ions ($[\\text{{Ag}}^+]$) in the electrolyte solution increases, decreases, or remains constant during electroplating. Give a reason.\n"
        f"4. State why an alternating current (AC) power source cannot be used for electroplating."
    )

    ans_latex = (
        rf"1.\; \text{{Cathode (teapot): }} \text{{Ag}}^+(aq) + e^- \to \text{{Ag}}(s)\n"
        rf"2.\; \text{{Anode (silver bar): }} \text{{Ag}}(s) \to \text{{Ag}}^+(aq) + e^-\n"
        rf"3.\; \text{{The concentration }} [\text{{Ag}}^+] \mathbf{{\text{{remains constant}}}}, \text{{ because the rate of silver oxidation at the anode equals the rate of silver reduction and deposition at the cathode.}}\n"
        rf"4.\; \text{{Alternating current periodically reverses polarity (e.g. 50 times per second), meaning the teapot would alternately plate and unplate, preventing a permanent, coherent layer from depositing. A direct current (DC) source is essential.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Cathode half-reaction: Ag+ + e- -> Ag", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Anode half-reaction: Ag -> Ag+ + e-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Concentration remains constant with valid rate equality explanation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "AC failure explanation (reversing polarity prevents deposit)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_ag_concentration_decreases", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Silver dissolves at the anode at the same rate it deposits at the cathode, keeping $[\\text{Ag}^+]$ constant.",
        "tier_2": "AC switches positive and negative terminals constantly, so plating would be undone every half cycle.",
        "tier_3": "Cathode: $\\text{Ag}^+ + e^- \\to \\text{Ag}$. Anode: $\\text{Ag} \\to \\text{Ag}^+ + e^-$. $[\\text{Ag}^+]$ is constant. DC is required.",
    }

    return {
        "id": f"ps12_ec_38_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_38_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "38_electroplating_silver_onto_cutlery",
        "learning_objective_id": "ps12_ec_38_silver_plating",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_silver_ion_concentration_decreases", "believed_ac_can_be_used_for_electroplating"],
        "keywords": ["silver plating", "constant concentration", "DC power source", "rate of deposition"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 39: Electroplating nickel onto iron
def _b39_electroplating_nickel_onto_iron(r: random.Random) -> Dict[str, Any]:
    mass_g = r.choice([2.5, 3.0, 4.5, 5.0])
    m_ni = 58.69
    moles_ni = mass_g / m_ni
    moles_e = moles_ni * 2
    charge_c = moles_e * FARADAY_CONST

    prompt = (
        f"An iron bracket is electroplated with nickel in a bath of nickel(II) sulfate ($\\text{{NiSO}}_4(aq)$).\n\n"
        f"1. Write down the reduction half-reaction occurring on the iron bracket.\n"
        f"2. Write down the oxidation half-reaction occurring at the nickel anode.\n"
        f"3. If a total mass of $\\Delta m = {_fmt_sa(mass_g)}\\text{{ g}}$ of nickel is deposited onto the bracket "
        f"($M(\\text{{Ni}}) = 58{{,}}69\\text{{ g/mol}}$), calculate the total electric charge in coulombs that passed through the cell ($F = 96500\\text{{ C/mol }}\\text{{e}}^-$)."
    )

    ans_latex = (
        rf"1.\; \text{{Cathode (bracket): }} \text{{Ni}}^{{2+}}(aq) + 2e^- \to \text{{Ni}}(s)\n"
        rf"2.\; \text{{Anode (nickel plate): }} \text{{Ni}}(s) \to \text{{Ni}}^{{2+}}(aq) + 2e^-\n"
        rf"3.\; n_{{\text{{Ni}}}} = \frac{{\Delta m}}{{M}} = \frac{{{_fmt_sa(mass_g)}}}{{58{{,}}69}} = {_fmt_sa(moles_ni, 4)}\text{{ mol}}\n"
        rf"\quad \text{{Each mole of Ni requires 2 moles of electrons: }} n(e^-) = 2 \times n_{{\text{{Ni}}}} = {_fmt_sa(moles_e, 4)}\text{{ mol e}}^-\n"
        rf"\quad Q = n(e^-) \times F = ({_fmt_sa(moles_e, 4)})(96500) = {_fmt_sa(charge_c, 1)}\text{{ C}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Cathode half-reaction: Ni2+ + 2e- -> Ni", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Anode half-reaction: Ni -> Ni2+ + 2e-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Moles of Ni: {_fmt_sa(moles_ni, 4)} mol", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Total charge calculation: {_fmt_sa(charge_c, 1)} C", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "forgot_2_electrons_per_nickel_ion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Nickel has a $+2$ charge ($\\text{Ni}^{2+}$), so 2 moles of electrons are required per mole of nickel.",
        "tier_2": "Find moles of nickel: $n = m / 58{,}69$. Multiply by 2 for moles of $e^-$, then multiply by 96500.",
        "tier_3": f"$n_{{\\text{{Ni}}}} = {_fmt_sa(moles_ni, 4)}\\text{{ mol}}$, $Q = {_fmt_sa(charge_c, 1)}\\text{{ C}}$.",
    }

    return {
        "id": f"ps12_ec_39_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_39_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "39_electroplating_nickel_onto_iron",
        "learning_objective_id": "ps12_ec_39_nickel_plating",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_factor_of_2_for_ni2_plus", "used_atomic_number_for_molar_mass"],
        "keywords": ["nickel electroplating", "Faraday charge", "mole ratio", "iron bracket"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 40: Quantitative electroplating Faraday law mass deposited
def _b40_quantitative_electroplating_faraday_law_mass_deposited(r: random.Random) -> Dict[str, Any]:
    metal = r.choice(["Ag", "Cu", "Ni", "Au"])
    m_data = STANDARD_REDUCTION_DATA[metal]
    val = m_data["charge"]
    molar_m = m_data["molar_mass"]

    current_a = r.choice([2.0, 3.0, 4.0, 5.0])
    time_min = r.choice([20, 30, 45, 60])
    time_s = time_min * 60
    charge_c = current_a * time_s
    moles_e = charge_c / FARADAY_CONST
    moles_m = moles_e / val
    mass_g = moles_m * molar_m

    prompt = (
        f"An electroplating bath deposits {m_data['name']} ({metal}) onto an automotive component using a constant "
        f"current of $I = {_fmt_sa(current_a)}\\text{{ A}}$ operating for $\\Delta t = {time_min}\\text{{ minutes}}$.\n"
        f"The ion in solution is $\\text{{{metal}}}^{{{val}+}}$, $M(\\text{{{metal}}}) = {_fmt_sa(molar_m)}\\text{{ g/mol}}$, "
        f"and $F = 96500\\text{{ C/mol }}\\text{{e}}^-$.\n\n"
        f"1. Write down the reduction half-reaction occurring on the component.\n"
        f"2. Calculate the total charge ($Q$) transferred in coulombs.\n"
        f"3. Calculate the number of moles of electrons transferred.\n"
        f"4. Calculate the mass in grams of {m_data['name']} deposited onto the component."
    )

    ans_latex = (
        rf"1.\; \text{{{metal}}}^{{{val}+}}(aq) + {val}e^- \to \text{{{metal}}}(s)\n"
        rf"2.\; Q = I \Delta t = ({_fmt_sa(current_a)})\text{{ A}} \times ({time_min} \times 60\text{{ s}}) = {_fmt_sa(charge_c)}\text{{ C}}\n"
        rf"3.\; n(e^-) = \frac{{Q}}{{F}} = \frac{{{_fmt_sa(charge_c)}}}{{96500}} = {_fmt_sa(moles_e, 4)}\text{{ mol e}}^-\n"
        rf"4.\; n_{{\text{{{metal}}}}} = \frac{{n(e^-)}}{{{val}}} = \frac{{{_fmt_sa(moles_e, 4)}}}{{{val}}} = {_fmt_sa(moles_m, 4)}\text{{ mol}}\n"
        rf"\quad m_{{\text{{{metal}}}}} = n_{{\text{{{metal}}}}} \times M = ({_fmt_sa(moles_m, 4)})({_fmt_sa(molar_m)}) = {_fmt_sa(mass_g, 2)}\text{{ g}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Reduction half-reaction", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Charge calculation: {_fmt_sa(charge_c)} C", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Moles of electrons: {_fmt_sa(moles_e, 4)} mol", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Mass deposited: {_fmt_sa(mass_g, 2)} g", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_minutes_to_seconds", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$Q = I \\Delta t$. Convert minutes to seconds ($t = \\text{minutes} \\times 60$).",
        "tier_2": "Divide charge by 96500 to get moles of electrons. Divide by valence for moles of metal.",
        "tier_3": f"$Q = {_fmt_sa(charge_c)}\\text{{ C}}$, mass = {_fmt_sa(mass_g, 2)} g.",
    }

    return {
        "id": f"ps12_ec_40_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_40_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "40_quantitative_electroplating_faraday_law_mass_deposited",
        "learning_objective_id": "ps12_ec_40_faraday_mass",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_valency_factor_in_faradays_law", "used_time_in_minutes"],
        "keywords": ["Faraday's law", "mass deposited", "electroplating calculation", "charge transfer"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 41: Electrorefining of copper (impure blister copper)
def _b41_electrorefining_of_copper_impure_blister_copper(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In industrial metallurgy (such as at Palabora Mining in Limpopo), impure 'blister copper' (approx. 98% pure) "
        f"is purified to 99,99% electrolytic copper via an electrochemical process.\n\n"
        f"1. Name the electrochemical process used to purify the copper.\n"
        f"2. State what material is used as the **anode** in the refining tank.\n"
        f"3. State what material is used as the **cathode** in the refining tank.\n"
        f"4. Name a suitable electrolyte solution used in the refining tank.\n"
        f"5. Write down the half-reactions taking place at the anode and cathode."
    )

    ans_latex = (
        rf"1.\; \text{{Electrorefining (electrolytic refining).}}\n"
        rf"2.\; \text{{Anode: A thick slab of }} \mathbf{{\text{{impure blister copper}}}}.\n"
        rf"3.\; \text{{Cathode: A thin sheet of }} \mathbf{{\text{{pure copper}}}}.\n"
        rf"4.\; \text{{Electrolyte: Acidified copper(II) sulfate solution (}}\text{{CuSO}}_4(aq) + \text{{H}}_2\text{{SO}}_4(aq)\text{{).}}\n"
        rf"5.\; \text{{Anode: }} \text{{Cu}}(s, \text{{impure}}) \to \text{{Cu}}^{{2+}}(aq) + 2e^-\n"
        rf"\quad \text{{Cathode: }} \text{{Cu}}^{{2+}}(aq) + 2e^- \to \text{{Cu}}(s, \text{{pure}})"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Process name: electrorefining", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Anode = impure blister copper", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Cathode = pure copper sheet", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Electrolyte: acidified copper(II) sulfate", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Anode and cathode half-reactions", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "swapped_impure_and_pure_electrodes", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Impure copper dissolves at the anode; pure copper deposits at the cathode.",
        "tier_2": "Electrolyte is acidified copper(II) sulfate solution.",
        "tier_3": "Anode: blister copper (dissolves); Cathode: pure copper (grows).",
    }

    return {
        "id": f"ps12_ec_41_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_41_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "41_electrorefining_of_copper_impure_blister_copper",
        "learning_objective_id": "ps12_ec_41_copper_refining",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["swapped_anode_and_cathode_materials_in_refining", "confused_electrorefining_with_smelting"],
        "keywords": ["electrorefining", "blister copper", "pure copper cathode", "acidified CuSO4"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 42: Anode sludge recovery in copper electrorefining
def _b42_anode_sludge_recovery_in_copper_electrorefining(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During the electrolytic refining of copper, a dense sludge (anode slime) accumulates on the tank floor beneath the anode.\n"
        f"Blister copper typically contains impurities such as zinc ($\\text{{Zn}}$), iron ($\\text{{Fe}}$), silver ($\\text{{Ag}}$), and gold ($\\text{{Au}}$).\n"
        f"Standard reduction potentials:\n"
        f"- $E^\\circ(\\text{{Zn}}^{{2+}}/\\text{{Zn}}) = -0{{,}}76\\text{{ V}}$\n"
        f"- $E^\\circ(\\text{{Fe}}^{{2+}}/\\text{{Fe}}) = -0{{,}}44\\text{{ V}}$\n"
        f"- $E^\\circ(\\text{{Cu}}^{{2+}}/\\text{{Cu}}) = +0{{,}}34\\text{{ V}}$\n"
        f"- $E^\\circ(\\text{{Ag}}^+/\\text{{Ag}}) = +0{{,}}80\\text{{ V}}$\n"
        f"- $E^\\circ(\\text{{Au}}^{{3+}}/\\text{{Au}}) = +1{{,}}50\\text{{ V}}$\n\n"
        f"1. Explain what happens to the reactive impurities ($\\text{{Zn}}$ and $\\text{{Fe}}$) during electrorefining.\n"
        f"2. Explain why silver ($\\text{{Ag}}$) and gold ($\\text{{Au}}$) do not oxidize and instead fall to the bottom as anode sludge.\n"
        f"3. Explain why the zinc and iron ions in solution do not plate out onto the pure copper cathode.\n"
        f"4. State the economic significance of the anode sludge to mining companies."
    )

    ans_latex = (
        rf"1.\; \text{{Zinc and iron have more negative reduction potentials (}}-0{{,}}76\text{{ V and }}-0{{,}}44\text{{ V) than copper (}}+0{{,}}34\text{{ V). They are more easily oxidized than copper, so they dissolve into the electrolyte as }} \text{{Zn}}^{{2+}} \text{{ and }} \text{{Fe}}^{{2+}} \text{{ ions.}}\n"
        rf"2.\; \text{{Silver and gold have much more positive reduction potentials (}}+0{{,}}80\text{{ V and }}+1{{,}}50\text{{ V) than copper. Under the operating cell voltage (calibrated to oxidize copper), they cannot be oxidized, so as the copper dissolves away around them, they fall to the floor as unreacted metallic particles (anode sludge).}}\n"
        rf"3.\; \text{{Copper ions have a much more positive reduction potential (}}+0{{,}}34\text{{ V) than }} \text{{Zn}}^{{2+}} \text{{ and }} \text{{Fe}}^{{2+}}\text{{. Therefore, }} \text{{Cu}}^{{2+}} \text{{ is far more readily reduced, so only pure copper deposits onto the cathode.}}\n"
        rf"4.\; \text{{The anode sludge contains valuable precious metals (silver, gold, platinum) that can be recovered and sold, often offsetting the electricity cost of the refining process.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidation of reactive impurities Zn/Fe into solution", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Noble metals Ag/Au drop as insoluble sludge (higher E0 than Cu)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Preferential reduction of Cu2+ over Zn2+/Fe2+ at cathode", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Economic value of precious metal recovery", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_gold_oxidizes_into_solution", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "More reactive metals ($\\text{Zn}$, $\\text{Fe}$) dissolve into solution. Noble metals ($\\text{Ag}$, $\\text{Au}$) do not oxidize and drop as sludge.",
        "tier_2": "At the cathode, $\\text{Cu}^{2+}$ is reduced preferentially because it has a higher $E^\\circ$ than $\\text{Zn}^{2+}$ or $\\text{Fe}^{2+}$.",
        "tier_3": "Anode sludge is rich in precious metals ($\text{Au}$, $\text{Ag}$), providing huge commercial revenue.",
    }

    return {
        "id": f"ps12_ec_42_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_42_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "42_anode_sludge_recovery_in_copper_electrorefining",
        "learning_objective_id": "ps12_ec_42_anode_sludge",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["thought_noble_metals_plate_onto_cathode", "assumed_zinc_and_iron_deposit_with_copper"],
        "keywords": ["anode sludge", "precious metals", "selective oxidation", "copper electrorefining"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 43: Hall-Héroult aluminium extraction principles
def _b43_hall_heroult_aluminium_extraction_principles(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"At aluminium smelters (such as the Hillside smelter in Richards Bay, South Africa), aluminium metal is extracted "
        f"from purified bauxite ore (alumina, $\\text{{Al}}_2\\text{{O}}_3$) using the Hall-Héroult electrolytic process.\n\n"
        f"1. Explain why molten **cryolite** ($\\text{{Na}}_3\\text{{AlF}}_6$) is added to the alumina.\n"
        f"2. Write down the reduction half-reaction occurring at the carbon cathode lining.\n"
        f"3. Write down the oxidation half-reaction occurring at the carbon anodes.\n"
        f"4. State the physical state in which aluminium is collected and explain why it collects at the bottom of the cell."
    )

    ans_latex = (
        rf"1.\; \text{{Pure alumina has a very high melting point (> 2000}}^\circ\text{{C). Dissolving alumina in molten cryolite lowers the operating temperature to approximately 950}}^\circ\text{{C, dramatically reducing energy costs and improving electrical conductivity.}}\n"
        rf"2.\; \text{{Cathode: }} \text{{Al}}^{{3+}}(l) + 3e^- \to \text{{Al}}(l)\n"
        rf"3.\; \text{{Anode: }} 2\text{{O}}^{{2-}}(l) \to \text{{O}}_2(g) + 4e^-\n"
        rf"4.\; \text{{Liquid state (}}\text{{Al}}(l)\text{{). Liquid aluminium is denser than the molten cryolite electrolyte, so it sinks to the bottom where it is periodically tapped off.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Role of cryolite (lowers melting point from 2000C to 950C)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Cathode half-reaction: Al3+ + 3e- -> Al(l)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Anode half-reaction: 2O2- -> O2 + 4e-", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Liquid aluminium sinks due to higher density", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_temperature_lowering_by_cryolite", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Cryolite acts as a solvent and flux that lowers the melting point from $> 2000^\\circ\\text{C}$ to $\\sim 950^\\circ\\text{C}$.",
        "tier_2": "Aluminium is denser than the cryolite bath, so liquid $\\text{Al}$ pools at the bottom.",
        "tier_3": "Cathode: $\\text{Al}^{3+} + 3e^- \\to \\text{Al}(l)$. Anode: $2\\text{O}^{2-} \\to \\text{O}_2 + 4e^-$.",
    }

    return {
        "id": f"ps12_ec_43_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_43_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "43_hall_heroult_aluminium_extraction_principles",
        "learning_objective_id": "ps12_ec_43_hall_heroult",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_cryolite_with_the_ore_source", "thought_aluminium_floats_on_cryolite"],
        "keywords": ["Hall-Heroult", "cryolite", "alumina", "aluminium extraction"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 44: Carbon anode consumption in aluminium smelting
def _b44_carbon_anode_consumption_in_aluminium_smelting(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the Hall-Héroult electrolytic cell for aluminium extraction, carbon (graphite) blocks are used as anodes at $950^\\circ\\text{{C}}$.\n\n"
        f"1. Explain why the carbon anodes are gradually consumed during the operation of the cell and must be regularly replaced.\n"
        f"2. Write down the balanced chemical equation representing the reaction responsible for the consumption of the carbon anodes.\n"
        f"3. State one major environmental concern associated with the gas emitted during the consumption of the carbon anodes.\n"
        f"4. State why aluminium smelting plants require an enormous, uninterrupted supply of electrical power."
    )

    ans_latex = (
        rf"1.\; \text{{At the high operating temperature (950}}^\circ\text{{C), the oxygen gas (}}\text{{O}}_2\text{{) produced at the anodes reacts with the hot carbon blocks to form carbon dioxide (}}\text{{CO}}_2\text{{) gas, steadily burning away the electrodes.}}\n"
        rf"2.\; \text{{C}}(s) + \text{{O}}_2(g) \to \text{{CO}}_2(g) \quad \text{{(or }} 2\text{{Al}}_2\text{{O}}_3 + 3\text{{C}} \to 4\text{{Al}} + 3\text{{CO}}_2\text{{)}}\n"
        rf"3.\; \text{{Emission of carbon dioxide (}}\text{{CO}}_2\text{{), a major greenhouse gas contributing to global warming and climate change.}}\n"
        rf"4.\; \text{{Aluminium has a high charge-to-mass ratio (3 moles of electrons per mole of Al), and continuous electrical heating is necessary to maintain the cryolite bath in its molten liquid state (massive current demand, often hundreds of thousands of amperes).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Explanation of carbon reacting with oxygen at 950 deg C", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Equation: C + O2 -> CO2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Environmental concern: greenhouse gas / global warming", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Huge power demand justification (charge transfer + thermal maintenance)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_carbon_evaporates_without_reacting", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Oxygen formed at the anode burns the carbon block: $\\text{C} + \\text{O}_2 \\to \\text{CO}_2$.",
        "tier_2": "$\\text{CO}_2$ is a greenhouse gas.",
        "tier_3": "Anodes burn to form $\\text{CO}_2$; huge current needed to keep bath molten and reduce $\\text{Al}^{3+}$.",
    }

    return {
        "id": f"ps12_ec_44_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_44_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "44_carbon_anode_consumption_in_aluminium_smelting",
        "learning_objective_id": "ps12_ec_44_carbon_anode_consumption",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_carbon_anodes_are_completely_inert", "forgot_co2_environmental_impact"],
        "keywords": ["carbon anode", "anode consumption", "CO2 emission", "greenhouse gas"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 45: Membrane cell chlor-alkali industry overview
def _b45_membrane_cell_chloralkali_industry_overview(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the modern chlor-alkali industry, concentrated sodium chloride brine is electrolyzed inside a **membrane cell**.\n\n"
        f"1. Name the three primary commercial products manufactured by the chlor-alkali process.\n"
        f"2. Explain the crucial function of the ion-permeable cation-exchange membrane.\n"
        f"3. State which specific ion is permitted to pass through the membrane from the anode to the cathode compartment.\n"
        f"4. Explain why chlorine gas ($\\text{{Cl}}_2$) and hydroxide ions ($\\text{{OH}}^-$) must be kept strictly separated."
    )

    ans_latex = (
        rf"1.\; \text{{(i) Chlorine gas (}}\text{{Cl}}_2\text{{); (ii) Hydrogen gas (}}\text{{H}}_2\text{{); (iii) Sodium hydroxide (}}\text{{NaOH}}\text{{, caustic soda).}}\n"
        rf"2.\; \text{{The cation-permeable membrane allows only positive sodium ions (}}\text{{Na}}^+\text{{) to cross into the cathode chamber while preventing chloride (}}\text{{Cl}}^-\text{{) and hydroxide (}}\text{{OH}}^-\text{{) ions from mixing.}}\n"
        rf"3.\; \text{{Sodium ions (}}\mathbf{{\text{{Na}}^+}}\text{{).}}\n"
        rf"4.\; \text{{If chlorine gas contacts hydroxide ions, they react chemically to form hypochlorite (bleach, }}\text{{ClO}}^-\text{{) and chloride ions (}}\text{{Cl}}_2 + 2\text{{OH}}^- \to \text{{ClO}}^- + \text{{Cl}}^- + \text{{H}}_2\text{{O}}\text{{), contaminating the sodium hydroxide product and reducing chlorine yield.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "3 commercial products: Cl2, H2, NaOH", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Function of cation membrane (permits Na+, blocks anions)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Identification of Na+ ion", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Separation reason (avoids bleach reaction Cl2 + 2OH- -> ClO- + Cl- + H2O)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_one_of_the_three_products", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The three products of chlor-alkali are chlorine ($\\text{Cl}_2$), hydrogen ($\\text{H}_2$), and caustic soda ($\\text{NaOH}$).",
        "tier_2": "The membrane is cation-permeable: only positive $\\text{Na}^+$ ions pass through.",
        "tier_3": "Membrane prevents $\\text{Cl}_2$ from reacting with $\\text{OH}^-$ to form bleach.",
    }

    return {
        "id": f"ps12_ec_45_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_45_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "45_membrane_cell_chloralkali_industry_overview",
        "learning_objective_id": "ps12_ec_45_chloralkali_overview",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["thought_anions_pass_through_cation_membrane", "forgot_hydrogen_is_produced_at_cathode"],
        "keywords": ["chlor-alkali", "membrane cell", "caustic soda", "cation membrane"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 46: Chlor-alkali membrane cell half-reactions and overall equation
def _b46_chloralkali_membrane_cell_half_reactions(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a chlor-alkali membrane cell, saturated sodium chloride solution (brine) enters the anode compartment, "
        f"while pure water enters the cathode compartment.\n\n"
        f"1. Write down the balanced half-reaction occurring at the anode.\n"
        f"2. Write down the balanced half-reaction occurring at the cathode.\n"
        f"3. Write down the overall balanced chemical equation for the cell.\n"
        f"4. State why titanium ($\\text{{Ti}}$) coated with ruthenium oxide is used as the anode material rather than graphite."
    )

    ans_latex = (
        rf"1.\; \text{{Anode: }} 2\text{{Cl}}^-(aq) \to \text{{Cl}}_2(g) + 2e^-\n"
        rf"2.\; \text{{Cathode: }} 2\text{{H}}_2\text{{O}}(l) + 2e^- \to \text{{H}}_2(g) + 2\text{{OH}}^-(aq)\n"
        rf"3.\; \text{{Overall reaction: }} 2\text{{NaCl}}(aq) + 2\text{{H}}_2\text{{O}}(l) \to \text{{Cl}}_2(g) + \text{{H}}_2(g) + 2\text{{NaOH}}(aq)\n"
        rf"4.\; \text{{Titanium resists chemical attack by wet chlorine gas, has superior mechanical durability, and operates at lower electrical overpotential without degrading.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Anode half-reaction: 2Cl- -> Cl2 + 2e-", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Cathode half-reaction: 2H2O + 2e- -> H2 + 2OH-", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Overall balanced equation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Titanium anode durability justification", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_2naoh_in_overall_equation", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Anode oxidizes chloride to $\\text{Cl}_2$. Cathode reduces water to $\\text{H}_2$ and $\\text{OH}^-$.",
        "tier_2": "Combine: $2\\text{NaCl} + 2\\text{H}_2\\text{O} \\to \\text{Cl}_2 + \\text{H}_2 + 2\\text{NaOH}$.",
        "tier_3": "Cathode: $2\\text{H}_2\\text{O} + 2e^- \\to \\text{H}_2 + 2\\text{OH}^-$.",
    }

    return {
        "id": f"ps12_ec_46_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_46_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "46_chloralkali_membrane_cell_half_reactions",
        "learning_objective_id": "ps12_ec_46_chloralkali_half_rx",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["wrote_na_plus_reduction_instead_of_water_reduction", "failed_to_balance_hydroxide_ions"],
        "keywords": ["chlor-alkali equations", "brine electrolysis", "water reduction", "anode half-reaction"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 47: Electrolytic cell with seed-varied inline vector diagram
def _b47_electrochemical_cells_with_inline_svg_diagram(r: random.Random) -> Dict[str, Any]:
    voltage_val = r.choice([6, 9, 12])

    svg = _clean_svg(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 250" width="100%" height="210" style="background:#f8fafc;">
      <!-- Single Beaker -->
      <rect x="90" y="80" width="240" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
      <text x="210" y="215" font-size="12" font-family="sans-serif" fill="#1d4ed8" text-anchor="middle">Aqueous CuCl₂ solution</text>

      <!-- Electrode A (Left: Connected to positive -> Anode) -->
      <rect x="130" y="50" width="20" height="130" fill="#334155" stroke="#0f172a" stroke-width="1.5"/>
      <text x="140" y="42" font-size="12" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">Electrode P</text>
      <!-- Gas bubbles at Anode -->
      <circle cx="125" cy="110" r="3" fill="#cbd5e1" stroke="#64748b"/>
      <circle cx="122" cy="130" r="4" fill="#cbd5e1" stroke="#64748b"/>
      <circle cx="126" cy="150" r="3" fill="#cbd5e1" stroke="#64748b"/>
      <text x="110" y="135" font-size="10" font-family="sans-serif" fill="#15803d">Cl₂ (g)</text>

      <!-- Electrode B (Right: Connected to negative -> Cathode) -->
      <rect x="270" y="50" width="20" height="130" fill="#334155" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="268" y="90" width="24" height="85" fill="#f87171" stroke="#b91c1c" stroke-width="1"/>
      <text x="280" y="42" font-size="12" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">Electrode Q</text>
      <text x="310" y="135" font-size="10" font-family="sans-serif" fill="#b91c1c">Cu (s)</text>

      <!-- External Circuit with DC Battery -->
      <line x1="140" y1="50" x2="140" y2="15" stroke="#0f172a" stroke-width="2"/>
      <line x1="140" y1="15" x2="195" y2="15" stroke="#0f172a" stroke-width="2"/>
      <!-- Battery symbol -->
      <line x1="195" y1="5" x2="195" y2="25" stroke="#0f172a" stroke-width="3"/>
      <line x1="202" y1="10" x2="202" y2="20" stroke="#0f172a" stroke-width="1.5"/>
      <line x1="209" y1="5" x2="209" y2="25" stroke="#0f172a" stroke-width="3"/>
      <line x1="216" y1="10" x2="216" y2="20" stroke="#0f172a" stroke-width="1.5"/>
      <text x="188" y="28" font-size="11" font-family="sans-serif" fill="#dc2626" font-weight="bold">+</text>
      <text x="222" y="28" font-size="11" font-family="sans-serif" fill="#2563eb" font-weight="bold">-</text>
      <line x1="216" y1="15" x2="280" y2="15" stroke="#0f172a" stroke-width="2"/>
      <line x1="280" y1="15" x2="280" y2="50" stroke="#0f172a" stroke-width="2"/>
      <text x="205" y="40" font-size="11" font-family="sans-serif" fill="#475569" text-anchor="middle">{voltage_val} V DC</text>
    </svg>
    """)

    prompt = (
        f"In the accompanying diagram, an electrolytic apparatus is shown containing an aqueous copper(II) chloride solution "
        f"connected to a ${voltage_val}\\text{{ V}}$ DC power source via two carbon electrodes labelled P and Q.\n\n"
        f"1. Identify which electrode (P or Q) acts as the **anode** and which acts as the **cathode**.\n"
        f"2. Write down the reduction half-reaction occurring at the cathode.\n"
        f"3. Explain the observation of gas bubbling at electrode P.\n"
        f"4. State the direction in which copper ions ($\\text{{Cu}}^{{2+}}$) migrate in the solution (toward P or Q)."
    )

    ans_latex = (
        rf"1.\; \text{{Electrode P is connected to the positive terminal: }} \mathbf{{\text{{Anode}}}};\quad \text{{Electrode Q is connected to the negative terminal: }} \mathbf{{\text{{Cathode}}}}.\n"
        rf"2.\; \text{{Cathode (Q): }} \text{{Cu}}^{{2+}}(aq) + 2e^- \to \text{{Cu}}(s)\n"
        rf"3.\; \text{{Chloride ions (}}\text{{Cl}}^-\text{{) lose electrons at the positive anode P to form chlorine gas (}}\text{{Cl}}_2\text{{), which evolves as gas bubbles.}}\n"
        rf"4.\; \text{{Positive copper ions (}}\text{{Cu}}^{{2+}}\text{{) migrate toward }} \mathbf{{\text{{Electrode Q}}}} \text{{ (the negative cathode) due to electrostatic attraction.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of P as anode and Q as cathode", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Cathode half-reaction: Cu2+ + 2e- -> Cu", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Chlorine gas evolution explanation at anode P", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Cu2+ migration toward negative electrode Q", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "swapped_electrodes_p_and_q", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Look at the battery terminal symbols: longer line (+) connects to P; shorter line (-) connects to Q.",
        "tier_2": "In an electrolytic cell, positive terminal = Anode (oxidation); negative terminal = Cathode (reduction).",
        "tier_3": "P = Anode (forms $\\text{Cl}_2$); Q = Cathode (deposits $\\text{Cu}$). $\\text{Cu}^{2+} \\to Q$.",
    }

    return {
        "id": f"ps12_ec_47_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_47_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "47_electrochemical_cells_with_inline_svg_diagram",
        "learning_objective_id": "ps12_ec_47_electrolytic_diagram",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["misidentified_battery_terminal_polarities", "swapped_anode_and_cathode_identities"],
        "keywords": ["electrolytic cell diagram", "DC source", "chlorine bubbles", "copper deposition"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg},
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 48: Galvanic cell powering electrolytic cell composite rider
def _b48_galvanic_cell_powering_electrolytic_cell_composite_rider(r: random.Random) -> Dict[str, Any]:
    galv_anode = r.choice(["Mg", "Al", "Zn"])
    galv_cath = "Cu"
    e0_a = STANDARD_REDUCTION_DATA[galv_anode]["e0"]
    e0_c = STANDARD_REDUCTION_DATA[galv_cath]["e0"]
    e_galv = round(e0_c - e0_a, 2)

    # Electrolytic cell decomposes CuCl2: E0_cell = 0.34 - 1.36 = -1.02 V
    e_decomp = 1.02  # V required
    is_sufficient = (e_galv > e_decomp)

    prompt = (
        f"A composite electrical circuit connects a standard {STANDARD_REDUCTION_DATA[galv_anode]['name']}–copper "
        f"galvanic cell ($E^\\circ = {_fmt_sa(e_galv)}\\text{{ V}}$) directly to an electrolytic cell containing "
        f"an aqueous copper(II) chloride solution ($\\text{{CuCl}}_2$).\n"
        f"The decomposition potential required for copper(II) chloride electrolysis is $1{{,}}02\\text{{ V}}$.\n\n"
        f"1. Explain how a galvanic cell can function as the power source for an electrolytic cell.\n"
        f"2. State the condition regarding electromotive forces that must be satisfied for the galvanic cell to successfully drive electrolysis.\n"
        f"3. State whether this specific {galv_anode}–{galv_cath} galvanic cell provides sufficient electromotive force to drive the electrolysis of $\\text{{CuCl}}_2$.\n"
        f"4. State which terminal of the galvanic cell (the {galv_anode} anode or the {galv_cath} cathode) must be wired to the cathode of the electrolytic cell."
    )

    ans_latex = (
        rf"1.\; \text{{A galvanic cell generates a spontaneous direct current (DC) potential difference as it converts chemical energy to electrical energy. This DC voltage can be applied across the electrodes of an electrolytic cell to force non-spontaneous reactions.}}\n"
        rf"2.\; E^\circ_{{\text{{galvanic}}}} > |E^\circ_{{\text{{electrolytic}}}}| \text{{ (the galvanic EMF must exceed the decomposition potential of the electrolytic cell).}}\n"
        rf"3.\; \text{{{'Yes' if is_sufficient else 'No'}}}, \text{{ because }} E^\circ_{{\text{{galvanic}}}} = {_fmt_sa(e_galv)}\text{{ V}} {('>' if is_sufficient else '<')} 1{{,}}02\text{{ V}}.\n"
        rf"4.\; \text{{The negative terminal of the galvanic cell (the }} \mathbf{{{galv_anode}\text{{ anode}}}} \text{{) supplies electrons and must be connected to the cathode of the electrolytic cell.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Galvanic cell as DC voltage supplier explanation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Condition: E_galvanic > decomposition potential", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Sufficiency verdict with comparison ({_fmt_sa(e_galv)} V vs 1.02 V)", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Wiring connection: {galv_anode} anode connected to electrolytic cathode", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "reversed_terminal_connections", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The galvanic cell is the DC battery. Its EMF must exceed the decomposition potential ($1{,}02\\text{ V}$).",
        "tier_2": "The galvanic anode is negative; electrons flow from it into the electrolytic cathode.",
        "tier_3": f"$E^\\circ_{{\\text{{galvanic}}}} = {_fmt_sa(e_galv)}\\text{{ V}} > 1{{,}}02\\text{{ V}}$. Connect {galv_anode} anode to electrolytic cathode.",
    }

    return {
        "id": f"ps12_ec_48_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_48_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "48_galvanic_cell_powering_electrolytic_cell_composite_rider",
        "learning_objective_id": "ps12_ec_48_composite_circuit",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_terminal_connections_between_cells", "forgot_decomposition_voltage_condition"],
        "keywords": ["composite circuit", "galvanic driving electrolytic", "decomposition voltage", "terminal wiring"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 49: Electrochemistry capstone synthesis rider
def _b49_electrochemistry_capstone_synthesis_rider(r: random.Random) -> Dict[str, Any]:
    pair = r.choice([("Zn", "Cu"), ("Mg", "Ag"), ("Al", "Cu")])
    anode_sym, cath_sym = pair
    anode_data = STANDARD_REDUCTION_DATA[anode_sym]
    cath_data = STANDARD_REDUCTION_DATA[cath_sym]
    e0_a = anode_data["e0"]
    e0_c = cath_data["e0"]
    ecell = round(e0_c - e0_a, 2)

    prompt = (
        f"A standard electrochemical cell is constructed using {anode_data['name']} ({anode_sym}) "
        f"and {cath_data['name']} ({cath_sym}) half-cells.\n\n"
        f"1. State the energy conversion taking place when the cell operates spontaneously in galvanic mode.\n"
        f"2. Write down the balanced overall equation for the spontaneous cell reaction.\n"
        f"3. Calculate the standard electromotive force ($E^\\circ_{{\\text{{cell}}}}$) of the cell.\n"
        f"4. The cell is now connected to an external DC power supply whose potential difference is gradually increased.\n"
        f"   - (a) State what minimum voltage must be applied to force the reaction to occur in the reverse (electrolytic) direction.\n"
        f"   - (b) In reverse electrolytic mode, write down the reduction half-reaction occurring at the {anode_sym} electrode."
    )

    ans_latex = (
        rf"1.\; \text{{Chemical energy is converted into electrical energy.}}\n"
        rf"2.\; \text{{{anode_sym}}}(s) + \text{{{cath_sym}}}^{{2+}}(aq) \to \text{{{anode_sym}}}^{{2+}}(aq) + \text{{{cath_sym}}}(s)\n"
        rf"3.\; E^\circ_{{\text{{cell}}}} = E^\circ_{{\text{{cathode}}}} - E^\circ_{{\text{{anode}}}} = {_fmt_sa(e0_c)} - ({_fmt_sa(e0_a)}) = {_fmt_sa(ecell)}\text{{ V}}\n"
        rf"4.\; \text{{(a) A voltage strictly greater than the cell's standard EMF: }} V_{{\text{{applied}}}} > {_fmt_sa(ecell)}\text{{ V}}.\n"
        rf"\quad \text{{(b) In reverse mode, }} \text{{{anode_sym}}} \text{{ becomes the cathode (site of reduction): }} \text{{{anode_sym}}}^{{2+}}(aq) + 2e^- \to \text{{{anode_sym}}}(s)."
    )

    marking_schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Energy conversion: chemical to electrical energy", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Balanced overall equation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Standard EMF calculation: {_fmt_sa(ecell)} V", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Minimum reverse voltage: > {_fmt_sa(ecell)} V", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Reverse reduction half-reaction at {anode_sym}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_reverse_mode_electrons", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate standard EMF: $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$.",
        "tier_2": "To force the non-spontaneous reverse reaction, the external power supply must exceed the cell EMF.",
        "tier_3": f"$E^\\circ_{{\\text{{cell}}}} = {_fmt_sa(ecell)}\\text{{ V}}$. Reverse reduction: $\\text{{{anode_sym}}}^{{2+}} + 2e^- \\to \\text{{{anode_sym}}}$.",
    }

    return {
        "id": f"ps12_ec_49_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_49_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "49_electrochemistry_capstone_synthesis_rider",
        "learning_objective_id": "ps12_ec_49_capstone_synthesis",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["thought_any_external_voltage_reverses_reaction", "swapped_electrodes_in_reverse_mode"],
        "keywords": ["capstone synthesis", "galvanic to electrolytic", "reverse voltage", "electrochemical equilibrium"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 7,
    }


# Archetype 50: Electrochemistry diagnostic autopsy
def _b50_electrochemistry_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner is reviewing their examination script on electrochemical cells and identifies three common errors.\n\n"
        f"Analyze each error and provide the correct scientific principle:\n"
        f"1. **Error A**: *'In a galvanic cell, the anode is negative, so reduction must occur there because electrons are negative.'*\n"
        f"   - Explain why this reasoning is incorrect and state the actual process occurring at the galvanic anode.\n"
        f"2. **Error B**: *'Electrons leave the zinc anode, travel through the external wire into the cathode, enter the copper sulfate solution, and then travel through the salt bridge to complete the circuit.'*\n"
        f"   - Identify the physical error regarding electron conduction through solutions.\n"
        f"3. **Error C**: *'In calculating the standard cell potential for $2\\text{{Al}} + 3\\text{{Cu}}^{{2+}} \\to 2\\text{{Al}}^{{3+}} + 3\\text{{Cu}}$, ' 'I multiplied $E^\\circ_{{\\text{{Al}}}}$ by 2 and $E^\\circ_{{\\text{{Cu}}}}$ by 3 before subtracting.'*\n"
        f"   - Explain why electrode potentials must never be multiplied by stoichiometric coefficients."
    )

    ans_latex = (
        rf"1.\; \textbf{{Correction for Error A:}} \text{{Oxidation (loss of electrons) }} \mathbf{{\text{{always}}}} \text{{ occurs at the anode (An Ox). In a galvanic cell, oxidation releases electrons at the anode, giving the electrode a negative charge (it acts as the electron source). Negative polarity does not mean reduction.}}\n\n"
        rf"2.\; \textbf{{Correction for Error B:}} \text{{Electrons cannot exist or travel freely through aqueous solutions or salt bridges. Charge in electrolyte solutions and the salt bridge is conducted exclusively by the movement of mobile ions (anions and cations).}}\n\n"
        rf"3.\; \textbf{{Correction for Error C:}} \text{{Standard reduction potential (}}E^\circ\text{{) is an }} \mathbf{{\text{{intensive property}}}} \text{{ (measured in volts = Joules per coulomb of charge). It represents the intrinsic electrical potential difference, not the total energy. It does not depend on the quantity of material or the stoichiometric balancing coefficients.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Error A correction: Oxidation always at anode; negative polarity due to electron release", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Error B correction: Zero electrons in solution; ions conduct charge", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Error C correction: Intensive property (J/C); independent of stoichiometric multipliers", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "claimed_e0_is_extensive_property", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Remember: (1) An Ox always. (2) Ions move in liquids, electrons in wires. (3) $E^\\circ$ is an intensive property.",
        "tier_2": "Potential ($V = J/C$) is independent of the number of reacting moles.",
        "tier_3": "Review Error A (An Ox), Error B (ionic conduction), Error C (intensive property).",
    }

    return {
        "id": f"ps12_ec_50_{r.randint(100000, 999999)}",
        "question_id": f"ps12_ec_50_{r.randint(100000, 999999)}",
        "topic": "Electrochemical reactions",
        "subskill": "50_electrochemistry_diagnostic_autopsy",
        "learning_objective_id": "ps12_ec_50_diagnostic_autopsy",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_anode_charge_with_reduction", "believed_electrons_travel_through_electrolyte", "multiplied_e0_by_stoichiometric_coefficients"],
        "keywords": ["diagnostic autopsy", "intensive property", "ionic conduction", "An Ox Red Cat"],
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_salt_bridge_functions_and_mechanics": _b26_salt_bridge_functions_and_mechanics,
    "27_salt_bridge_ion_migration_anion_cation": _b27_salt_bridge_ion_migration_anion_cation,
    "28_salt_bridge_removal_effect_on_current": _b28_salt_bridge_removal_effect_on_current,
    "29_salt_bridge_electrolyte_precipitation_incompatibility": _b29_salt_bridge_electrolyte_precipitation_incompatibility,
    "30_internal_resistance_of_galvanic_cell": _b30_internal_resistance_of_galvanic_cell,
    "31_electrolytic_cell_definition_and_energy_conversion": _b31_electrolytic_cell_definition_and_energy_conversion,
    "32_galvanic_vs_electrolytic_cell_structural_comparison": _b32_galvanic_vs_electrolytic_cell_structural_comparison,
    "33_electrolytic_cell_anode_and_cathode_polarities": _b33_electrolytic_cell_anode_and_cathode_polarities,
    "34_electrolysis_of_molten_sodium_chloride_downs_cell": _b34_electrolysis_of_molten_sodium_chloride_downs_cell,
    "35_electrolysis_of_aqueous_copper_chloride": _b35_electrolysis_of_aqueous_copper_chloride,
    "36_electrolysis_competing_reactions_water_vs_halide": _b36_electrolysis_competing_reactions_water_vs_halide,
    "37_electroplating_principles_and_setup": _b37_electroplating_principles_and_setup,
    "38_electroplating_silver_onto_cutlery": _b38_electroplating_silver_onto_cutlery,
    "39_electroplating_nickel_onto_iron": _b39_electroplating_nickel_onto_iron,
    "40_quantitative_electroplating_faraday_law_mass_deposited": _b40_quantitative_electroplating_faraday_law_mass_deposited,
    "41_electrorefining_of_copper_impure_blister_copper": _b41_electrorefining_of_copper_impure_blister_copper,
    "42_anode_sludge_recovery_in_copper_electrorefining": _b42_anode_sludge_recovery_in_copper_electrorefining,
    "43_hall_heroult_aluminium_extraction_principles": _b43_hall_heroult_aluminium_extraction_principles,
    "44_carbon_anode_consumption_in_aluminium_smelting": _b44_carbon_anode_consumption_in_aluminium_smelting,
    "45_membrane_cell_chloralkali_industry_overview": _b45_membrane_cell_chloralkali_industry_overview,
    "46_chloralkali_membrane_cell_half_reactions": _b46_chloralkali_membrane_cell_half_reactions,
    "47_electrochemical_cells_with_inline_svg_diagram": _b47_electrochemical_cells_with_inline_svg_diagram,
    "48_galvanic_cell_powering_electrolytic_cell_composite_rider": _b48_galvanic_cell_powering_electrolytic_cell_composite_rider,
    "49_electrochemistry_capstone_synthesis_rider": _b49_electrochemistry_capstone_synthesis_rider,
    "50_electrochemistry_diagnostic_autopsy": _b50_electrochemistry_diagnostic_autopsy,
}
