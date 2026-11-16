"""Physical Sciences Grade 11 Term 3 — Quantitative Aspects of Chemical Change.
Archetypes 26 to 50: Mole concept and Avogadro's constant, molar mass, molar volume of gases at STP,
solution concentration and dilution, percentage composition, empirical and molecular formulas,
water of crystallisation, stoichiometric calculations (mole-mole, mass-mass, volume-volume, solid-gas),
limiting and excess reagents, theoretical and percentage yield, percentage purity,
fertiliser stoichiometry, back titrations, and post-exam diagnostic autopsy.

Complies with the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import fmt_sa, make_science_question

TOPIC = "grade11_physical_sciences_acids_bases_stoichiometry"
LO = "ps11_quantitative_aspects_of_chemical_change"


def _build_q(
    subskill: str,
    prompt: str,
    ans: str,
    hints: Dict[str, str],
    schema: Dict[str, Any],
    diag: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    marks = schema.get("total_marks", 7)
    return make_science_question(
        prefix="ps11_stoich",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=LO,
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans,
        sample_answer=ans,
        marking_schema=schema,
        hints=hints,
        misconception_tags=[f"{subskill}_concept_error"],
        keywords=[subskill, TOPIC],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=7,
        marks=marks,
        diagram_spec=diag,
    )


# --------------------------------------------------------------------------- #
# Subskill 26: The Mole Concept & Avogadro's Constant
# --------------------------------------------------------------------------- #
def builder_26_mole_and_avogadro_constant(rng: random.Random) -> Dict[str, Any]:
    substances = [
        {"name": "carbon dioxide", "formula": "\\text{CO}_2", "molar_mass": 44.01, "m_str": "44{{,}}01"},
        {"name": "water", "formula": "\\text{H}_2\\text{O}", "molar_mass": 18.02, "m_str": "18{{,}}02"},
        {"name": "methane", "formula": "\\text{CH}_4", "molar_mass": 16.04, "m_str": "16{{,}}04"},
        {"name": "ammonia", "formula": "\\text{NH}_3", "molar_mass": 17.03, "m_str": "17{{,}}03"},
    ]
    s = rng.choice(substances)
    moles = rng.choice([0.25, 0.50, 1.25, 2.00, 2.50])
    mass = moles * s["molar_mass"]
    particles_coeff = moles * 6.022

    prompt = (
        f"A sample of pure {s['name']} (${s['formula']}$) has a mass of {fmt_sa(mass, 2)} g.\n\n"
        f"1. Define the *mole* in terms of elementary particles.\n"
        f"2. State the numerical value and unit of Avogadro's constant ($N_A$).\n"
        f"3. Calculate the number of moles of {s['name']} present in the sample ($M = {s['m_str']}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}).\n"
        f"4. Calculate the total number of {s['formula']} molecules present in the sample."
    )
    ans = (
        f"1. The mole is the amount of substance having the same number of elementary entities as there are atoms in 12 g of carbon-12; "
        f"2. NA = 6,022 x 10^23 mol^-1; "
        f"3. n = m / M = {fmt_sa(mass, 2)} / {s['m_str']} = {fmt_sa(moles, 2)} mol; "
        f"4. N = n * NA = {fmt_sa(moles, 2)} * 6,022 x 10^23 = {fmt_sa(particles_coeff, 3)} x 10^23 molecules."
    )
    memo = (
        f"1. Mole definition [2]: The SI unit for amount of substance, containing exactly $6{{,}}022 \\times 10^{{23}}$ elementary entities. [2]\n"
        f"2. Avogadro's constant [1]: $N_A = 6{{,}}022 \\times 10^{{23}}\\text{{ mol}}^{{-1}}$. [1]\n"
        f"3. Moles calculation [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{fmt_sa(mass, 2)}}}{{{s['m_str']}}} = {fmt_sa(moles, 2)}\\text{{ mol}}$$ [2]\n"
        f"4. Molecules calculation [2]:\n"
        f"   $$N = n \\cdot N_A = ({fmt_sa(moles, 2)}) \\times (6{{,}}022 \\times 10^{{23}}) = {fmt_sa(particles_coeff, 3)} \\times 10^{{23}}\\text{{ molecules}}$$ [2]"
    )
    hints = {
        "tier_1": "Use the relationship n = m / M to find the moles first.",
        "tier_2": "Multiply moles by Avogadro's number N_A to get the number of molecules.",
        "tier_3": f"N = ({fmt_sa(moles, 2)}) * (6,022 x 10^23) = {fmt_sa(particles_coeff, 3)} x 10^23 molecules.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of the mole", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Avogadro's constant value and unit", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Moles calculation n = m / M", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Number of molecules N = n * NA", "marks": 2, "editable": True},
        ],
    }
    return _build_q("26_mole_and_avogadro_constant", prompt, ans, hints, schema)


# --------------------------------------------------------------------------- #
# Subskill 27: Molar Mass Calculations
# --------------------------------------------------------------------------- #
def builder_27_molar_mass_compound_calculations(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        {
            "name": "aluminium sulphate",
            "formula": "\\text{Al}_2(\\text{SO}_4)_3",
            "breakdown": "2(26,98) + 3[32,06 + 4(16,00)] = 53,96 + 3(96,06) = 342,14",
            "molar_mass": 342.14,
            "m_str": "342{{,}}14",
        },
        {
            "name": "calcium nitrate",
            "formula": "\\text{Ca(NO}_3)_2",
            "breakdown": "40,08 + 2[14,01 + 3(16,00)] = 40,08 + 2(62,01) = 164,10",
            "molar_mass": 164.10,
            "m_str": "164{{,}}10",
        },
        {
            "name": "ammonium phosphate",
            "formula": "(\\text{NH}_4)_3\\text{PO}_4",
            "breakdown": "3[14,01 + 4(1,01)] + 30,97 + 4(16,00) = 3(18,05) + 30,97 + 64,00 = 149,12",
            "molar_mass": 149.12,
            "m_str": "149{{,}}12",
        },
    ]
    c = rng.choice(compounds)
    mass_sample = rng.choice([25.0, 50.0, 75.0, 100.0])
    moles = mass_sample / c["molar_mass"]

    prompt = (
        f"Consider a pure sample of {c['name']} (${c['formula']}$) of mass {fmt_sa(mass_sample, 1)} g.\n\n"
        f"1. Define the term *molar mass*.\n"
        f"2. Calculate the molar mass of {c['name']} (${c['formula']}$), showing the individual elemental contributions.\n"
        f"3. Calculate the number of moles of {c['formula']} in the {fmt_sa(mass_sample, 1)} g sample."
    )
    ans = (
        f"1. Molar mass is the mass in grams of one mole of a chemical substance (unit: g·mol⁻¹); "
        f"2. M = {c['breakdown']} = {c['m_str']} g·mol⁻¹; "
        f"3. n = m / M = {fmt_sa(mass_sample, 1)} / {c['m_str']} = {fmt_sa(moles, 3)} mol."
    )
    memo = (
        f"1. Molar mass definition [2]: The mass in grams of one mole of that substance. [2]\n"
        f"2. Molar mass calculation [3]:\n"
        f"   $$M = {c['breakdown']} = {c['m_str']}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$$ [3]\n"
        f"3. Moles calculation [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{fmt_sa(mass_sample, 1)}}}{{{c['m_str']}}} = {fmt_sa(moles, 3)}\\text{{ mol}}$$ [2]"
    )
    hints = {
        "tier_1": "Multiply each element's atomic mass by its subscript, taking brackets into account.",
        "tier_2": "Use atomic masses from the periodic table: Al=26,98; S=32,06; O=16,00; Ca=40,08; N=14,01; H=1,01; P=30,97.",
        "tier_3": f"M = {c['m_str']} g·mol⁻¹, then n = m / M = {fmt_sa(moles, 3)} mol.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Molar mass definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Molar mass summation with units", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Moles calculation n = m / M", "marks": 2, "editable": True},
        ],
    }
    return _build_q("27_molar_mass_compound_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 28: Molar Gas Volume at STP
# --------------------------------------------------------------------------- #
def builder_28_molar_gas_volume_stp_calculations(rng: random.Random) -> Dict[str, Any]:
    gases = [
        {"name": "oxygen gas", "formula": "\\text{O}_2", "molar_mass": 32.0, "m_str": "32{{,}}0"},
        {"name": "nitrogen gas", "formula": "\\text{N}_2", "molar_mass": 28.0, "m_str": "28{{,}}0"},
        {"name": "carbon dioxide gas", "formula": "\\text{CO}_2", "molar_mass": 44.0, "m_str": "44{{,}}0"},
        {"name": "hydrogen gas", "formula": "\\text{H}_2", "molar_mass": 2.02, "m_str": "2{{,}}02"},
    ]
    g = rng.choice(gases)
    vol_dm3 = rng.choice([5.6, 11.2, 33.6, 44.8, 56.0])
    # n = V / Vm = vol_dm3 / 22.4
    moles = vol_dm3 / 22.4
    mass = moles * g["molar_mass"]

    prompt = (
        f"A cylinder contains {fmt_sa(vol_dm3, 1)} dm³ of pure {g['name']} (${g['formula']}$) measured at standard temperature and pressure (STP).\n\n"
        f"1. State the standard temperature in °C (and K) and standard pressure in kPa.\n"
        f"2. State the value of the molar gas volume ($V_m$) at STP.\n"
        f"3. Calculate the number of moles of {g['formula']} gas in the cylinder.\n"
        f"4. Calculate the mass in grams of the gas sample."
    )
    ans = (
        f"1. Standard temperature = 0 °C (273 K); Standard pressure = 101,3 kPa; "
        f"2. Vm = 22,4 dm³·mol⁻¹; "
        f"3. n = V / Vm = {fmt_sa(vol_dm3, 1)} / 22,4 = {fmt_sa(moles, 2)} mol; "
        f"4. m = n * M = {fmt_sa(moles, 2)} * {g['m_str']} = {fmt_sa(mass, 2)} g."
    )
    memo = (
        f"1. STP conditions [2]: $T = 0\\text{{ }}^\\circ\\text{{C}} = 273\\text{{ K}}$ [1]; $P = 101{{,}}3\\text{{ kPa}}$ [1].\n"
        f"2. Molar gas volume [1]: $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$. [1]\n"
        f"3. Moles of gas [2]:\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{fmt_sa(vol_dm3, 1)}}}{{22{{,}}4}} = {fmt_sa(moles, 2)}\\text{{ mol}}$$ [2]\n"
        f"4. Mass calculation [2]:\n"
        f"   $$m = n \\cdot M = ({fmt_sa(moles, 2)})({g['m_str']}) = {fmt_sa(mass, 2)}\\text{{ g}}$$ [2]"
    )
    hints = {
        "tier_1": "Recall that 1 mole of any ideal gas occupies 22,4 dm³ at STP.",
        "tier_2": "Use n = V / 22,4 to find moles, then m = n * M to find mass.",
        "tier_3": f"n = {fmt_sa(vol_dm3, 1)} / 22,4 = {fmt_sa(moles, 2)} mol, and m = {fmt_sa(mass, 2)} g.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Standard temperature and pressure values", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Molar gas volume at STP", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Moles calculation n = V / Vm", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Mass calculation m = n * M", "marks": 2, "editable": True},
        ],
    }
    return _build_q("28_molar_gas_volume_stp_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 29: Solution Concentration Calculations
# --------------------------------------------------------------------------- #
def builder_29_solution_concentration_calculations(rng: random.Random) -> Dict[str, Any]:
    solutes = [
        {"name": "sodium chloride", "formula": "\\text{NaCl}", "molar_mass": 58.44, "m_str": "58{{,}}44"},
        {"name": "potassium chloride", "formula": "\\text{KCl}", "molar_mass": 74.55, "m_str": "74{{,}}55"},
        {"name": "copper(II) sulphate", "formula": "\\text{CuSO}_4", "molar_mass": 159.61, "m_str": "159{{,}}61"},
    ]
    sol = rng.choice(solutes)
    vol_cm3 = rng.choice([250.0, 500.0, 750.0])
    vol_dm3 = vol_cm3 / 1000.0
    conc = rng.choice([0.15, 0.25, 0.40, 0.50])
    mass = conc * sol["molar_mass"] * vol_dm3
    mass_conc = mass / vol_dm3  # in g/dm3

    prompt = (
        f"A learner dissolves {fmt_sa(mass, 2)} g of pure {sol['name']} (${sol['formula']}$) in deionised water to make exactly "
        f"{fmt_sa(vol_cm3, 0)} cm³ of solution.\n\n"
        f"1. Define the *concentration* of a solution.\n"
        f"2. Calculate the concentration of the solution in mol·dm⁻³ ($M = {sol['m_str']}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Calculate the concentration of the solution in g·dm⁻³."
    )
    ans = (
        f"1. Concentration is the amount of solute per unit volume of solution; "
        f"2. c = m / (M * V) = {fmt_sa(mass, 2)} / ({sol['m_str']} * {fmt_sa(vol_dm3, 3)}) = {fmt_sa(conc, 2)} mol·dm⁻³; "
        f"3. Mass concentration = m / V = {fmt_sa(mass, 2)} / {fmt_sa(vol_dm3, 3)} = {fmt_sa(mass_conc, 2)} g·dm⁻³."
    )
    memo = (
        f"1. Concentration definition [2]: The amount of solute per unit volume of solution. [2]\n"
        f"2. Molar concentration [3]:\n"
        f"   $$V = \\frac{{{fmt_sa(vol_cm3, 0)}}}{{1000}} = {fmt_sa(vol_dm3, 3)}\\text{{ dm}}^3$$\n"
        f"   $$c = \\frac{{m}}{{M \\cdot V}} = \\frac{{{fmt_sa(mass, 2)}}}{{{sol['m_str']} \\times {fmt_sa(vol_dm3, 3)}}} = {fmt_sa(conc, 2)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$ [3]\n"
        f"3. Mass concentration [2]:\n"
        f"   $$\\rho = \\frac{{m}}{{V}} = \\frac{{{fmt_sa(mass, 2)}}}{{{fmt_sa(vol_dm3, 3)}}} = {fmt_sa(mass_conc, 2)}\\text{{ g}}\\cdot\\text{{dm}}^{{-3}}$$ [2]"
    )
    hints = {
        "tier_1": "Convert cm³ to dm³ by dividing by 1000.",
        "tier_2": "Molar concentration is c = n / V = m / (M * V).",
        "tier_3": f"c = {fmt_sa(mass, 2)} / ({sol['m_str']} * {fmt_sa(vol_dm3, 3)}) = {fmt_sa(conc, 2)} mol·dm⁻³.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Concentration definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Molar concentration formula, substitution, answer", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Mass concentration calculation in g/dm3", "marks": 2, "editable": True},
        ],
    }
    return _build_q("29_molar_concentration_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 30: Solution Dilution Calculations
# --------------------------------------------------------------------------- #
def builder_30_solution_dilution_calculation(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([1.00, 2.00, 2.50, 3.00])  # stock
    v2_cm3 = rng.choice([250.0, 500.0, 1000.0])  # final
    c2 = rng.choice([0.10, 0.20, 0.25, 0.50])
    # c1 * v1 = c2 * v2 => v1 = (c2 * v2) / c1
    v1_cm3 = (c2 * v2_cm3) / c1
    water_added_cm3 = v2_cm3 - v1_cm3

    prompt = (
        f"A laboratory technician needs to prepare {fmt_sa(v2_cm3, 0)} cm³ of a dilute {fmt_sa(c2, 2)} mol·dm⁻³ hydrochloric acid "
        f"solution from a concentrated stock bottle of {fmt_sa(c1, 2)} mol·dm⁻³.\n\n"
        f"1. State the principle of conservation of moles during a solution dilution.\n"
        f"2. Write down the dilution equation relating concentration and volume.\n"
        f"3. Calculate the volume of concentrated stock solution ($V_1$) required in cm³.\n"
        f"4. Calculate the volume of distilled water that must be added to achieve the desired concentration."
    )
    ans = (
        f"1. Dilution adds solvent without altering the total number of moles of solute present (n1 = n2); "
        f"2. c1 * V1 = c2 * V2; "
        f"3. V1 = (c2 * V2) / c1 = ({fmt_sa(c2, 2)} * {fmt_sa(v2_cm3, 0)}) / {fmt_sa(c1, 2)} = {fmt_sa(v1_cm3, 1)} cm³; "
        f"4. V(water) = V2 - V1 = {fmt_sa(v2_cm3, 0)} - {fmt_sa(v1_cm3, 1)} = {fmt_sa(water_added_cm3, 1)} cm³."
    )
    memo = (
        f"1. Conservation principle [1]: Solute moles remain constant ($n_1 = n_2$) as solvent is added. [1]\n"
        f"2. Dilution formula [1]: $c_1 V_1 = c_2 V_2$. [1]\n"
        f"3. Stock volume calculation [3]:\n"
        f"   $$V_1 = \\frac{{c_2 \\cdot V_2}}{{c_1}} = \\frac{{({fmt_sa(c2, 2)})({fmt_sa(v2_cm3, 0)})}}{{{fmt_sa(c1, 2)}}} = {fmt_sa(v1_cm3, 1)}\\text{{ cm}}^3$$ [3]\n"
        f"4. Water volume [1]: $$V_{{\\text{{water}}}} = {fmt_sa(v2_cm3, 0)} - {fmt_sa(v1_cm3, 1)} = {fmt_sa(water_added_cm3, 1)}\\text{{ cm}}^3$$ [1]"
    )
    hints = {
        "tier_1": "Recall that the total moles of solute do not change when water is added.",
        "tier_2": "Use c1 * V1 = c2 * V2.",
        "tier_3": f"V1 = ({fmt_sa(c2, 2)} * {fmt_sa(v2_cm3, 0)}) / {fmt_sa(c1, 2)} = {fmt_sa(v1_cm3, 1)} cm³.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Conservation of moles statement", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Dilution equation statement", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Stock volume calculation", "marks": 3, "editable": True},
            {"id": "mp4", "desc": "Volume of water added calculation", "marks": 1, "editable": True},
        ],
    }
    return _build_q("30_solution_dilution_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 31: Percentage Composition by Mass
# --------------------------------------------------------------------------- #
def builder_31_percentage_composition_by_mass(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        {
            "name": "glucose",
            "formula": "\\text{C}_6\\text{H}_{12}\\text{O}_6",
            "m_total": 180.18,
            "c_pct": (6 * 12.011 / 180.18) * 100,
            "h_pct": (12 * 1.008 / 180.18) * 100,
            "o_pct": (6 * 15.999 / 180.18) * 100,
            "m_str": "180{{,}}18",
        },
        {
            "name": "ethanol",
            "formula": "\\text{C}_2\\text{H}_5\\text{OH}",
            "m_total": 46.07,
            "c_pct": (2 * 12.011 / 46.07) * 100,
            "h_pct": (6 * 1.008 / 46.07) * 100,
            "o_pct": (1 * 15.999 / 46.07) * 100,
            "m_str": "46{{,}}07",
        },
        {
            "name": "methanoic acid",
            "formula": "\\text{HCOOH}",
            "m_total": 46.03,
            "c_pct": (1 * 12.011 / 46.03) * 100,
            "h_pct": (2 * 1.008 / 46.03) * 100,
            "o_pct": (2 * 15.999 / 46.03) * 100,
            "m_str": "46{{,}}03",
        },
    ]
    c = rng.choice(compounds)

    prompt = (
        f"Consider pure {c['name']} (${c['formula']}$) with a molar mass of {c['m_str']} g·mol⁻¹.\n\n"
        f"1. Define *percentage composition by mass*.\n"
        f"2. Calculate the percentage by mass of carbon (C) in {c['name']}.\n"
        f"3. Calculate the percentage by mass of hydrogen (H) in {c['name']}.\n"
        f"4. Calculate the percentage by mass of oxygen (O) in {c['name']}."
    )
    ans = (
        f"1. Percentage composition by mass is the percentage of the total mass of a compound contributed by each element; "
        f"2. %C = {fmt_sa(c['c_pct'], 2)}%; "
        f"3. %H = {fmt_sa(c['h_pct'], 2)}%; "
        f"4. %O = {fmt_sa(c['o_pct'], 2)}%."
    )
    memo = (
        f"1. Definition [2]: The mass percentage of each element relative to the total molecular mass of the compound. [2]\n"
        f"2. Carbon percentage [2]:\n"
        f"   $$\\%\\text{{C}} = \\frac{{n_C \\cdot M_C}}{{M_{{\\text{{total}}}}}} \\times 100 = {fmt_sa(c['c_pct'], 2)}\\%$$ [2]\n"
        f"3. Hydrogen percentage [2]:\n"
        f"   $$\\%\\text{{H}} = \\frac{{n_H \\cdot M_H}}{{M_{{\\text{{total}}}}}} \\times 100 = {fmt_sa(c['h_pct'], 2)}\\%$$ [2]\n"
        f"4. Oxygen percentage [2]:\n"
        f"   $$\\%\\text{{O}} = \\frac{{n_O \\cdot M_O}}{{M_{{\\text{{total}}}}}} \\times 100 = {fmt_sa(c['o_pct'], 2)}\\%$$ [2]"
    )
    hints = {
        "tier_1": "Divide the total mass of each element by the molar mass and multiply by 100.",
        "tier_2": "Remember to multiply the atomic mass by the subscript of that element in the formula.",
        "tier_3": f"The percentages must sum up to approximately 100%: %C={fmt_sa(c['c_pct'], 2)}%, %H={fmt_sa(c['h_pct'], 2)}%, %O={fmt_sa(c['o_pct'], 2)}%.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Percentage composition definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "% Carbon calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "% Hydrogen calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "% Oxygen calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("31_percentage_composition_by_mass", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 32: Empirical Formula from Percentage Composition
# --------------------------------------------------------------------------- #
def builder_32_empirical_formula_from_percentage(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "name": "Compound A",
            "pct_c": 40.00,
            "pct_h": 6.71,
            "pct_o": 53.29,
            "n_c": 3.33,
            "n_h": 6.66,
            "n_o": 3.33,
            "ratio": "1 : 2 : 1",
            "empirical": "\\text{CH}_2\\text{O}",
        },
        {
            "name": "Compound B",
            "pct_c": 52.14,
            "pct_h": 13.13,
            "pct_o": 34.73,
            "n_c": 4.34,
            "n_h": 13.03,
            "n_o": 2.17,
            "ratio": "2 : 6 : 1",
            "empirical": "\\text{C}_2\\text{H}_6\\text{O}",
        },
        {
            "name": "Compound C",
            "pct_c": 82.66,
            "pct_h": 17.34,
            "pct_o": 0.0,
            "n_c": 6.88,
            "n_h": 17.20,
            "n_o": 0.0,
            "ratio": "2 : 5",
            "empirical": "\\text{C}_2\\text{H}_5",
        },
    ]
    c = rng.choice(cases)

    if c["pct_o"] > 0:
        desc = f"{fmt_sa(c['pct_c'], 2)}% carbon, {fmt_sa(c['pct_h'], 2)}% hydrogen, and {fmt_sa(c['pct_o'], 2)}% oxygen by mass"
    else:
        desc = f"{fmt_sa(c['pct_c'], 2)}% carbon and {fmt_sa(c['pct_h'], 2)}% hydrogen by mass"

    prompt = (
        f"A qualitative elemental analysis of an unknown organic substance reveals that it contains {desc}.\n\n"
        f"1. Define the term *empirical formula*.\n"
        f"2. Show that by assuming a 100 g sample, the mole quantities of each constituent element can be determined.\n"
        f"3. Divide by the smallest mole value to find the simplest whole-number atomic ratio.\n"
        f"4. Write down the empirical formula of the compound."
    )
    ans = (
        f"1. The empirical formula is the simplest whole-number ratio of atoms of each element present in a compound; "
        f"2. In 100 g sample: m(C) = {fmt_sa(c['pct_c'], 2)} g => n(C) = {fmt_sa(c['n_c'], 2)} mol; m(H) = {fmt_sa(c['pct_h'], 2)} g => n(H) = {fmt_sa(c['n_h'], 2)} mol; "
        f"3. Simplest ratio: {c['ratio']}; "
        f"4. Empirical formula: {c['empirical']}."
    )
    memo = (
        f"1. Empirical formula definition [2]: The simplest whole-number ratio of the elements in a compound. [2]\n"
        f"2. Mole determinations [3]:\n"
        f"   $$n(\\text{{C}}) = \\frac{{{fmt_sa(c['pct_c'], 2)}}}{{12{{,}}01}} = {fmt_sa(c['n_c'], 2)}\\text{{ mol}}$$ [1]\n"
        f"   $$n(\\text{{H}}) = \\frac{{{fmt_sa(c['pct_h'], 2)}}}{{1{{,}}01}} = {fmt_sa(c['n_h'], 2)}\\text{{ mol}}$$ [1]\n"
        f"3. Ratio calculation [2]: Ratio = ${c['ratio']}$. [2]\n"
        f"4. Empirical formula [1]: $${c['empirical']}$$ [1]"
    )
    hints = {
        "tier_1": "Assume 100 g of compound so percentages become masses in grams.",
        "tier_2": "Convert each mass to moles using n = m / M.",
        "tier_3": f"Divide each mole value by the smallest mole value to obtain the ratio {c['ratio']}.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Empirical formula definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Conversion from mass percentage to moles", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Simplest whole-number ratio derivation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Final empirical formula", "marks": 1, "editable": True},
        ],
    }
    return _build_q("32_empirical_formula_from_percentage", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 33: Empirical Formula from Mass Data
# --------------------------------------------------------------------------- #
def builder_33_empirical_formula_from_combustion_masses(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "metal": "magnesium",
            "symbol": "\\text{Mg}",
            "m_metal": 2.43,
            "m_oxide": 4.03,
            "m_o": 1.60,
            "n_metal": 0.100,
            "n_o": 0.100,
            "formula": "\\text{MgO}",
            "ratio": "1 : 1",
        },
        {
            "metal": "iron",
            "symbol": "\\text{Fe}",
            "m_metal": 5.58,
            "m_oxide": 7.98,
            "m_o": 2.40,
            "n_metal": 0.100,
            "n_o": 0.150,
            "formula": "\\text{Fe}_2\\text{O}_3",
            "ratio": "2 : 3",
        },
    ]
    c = rng.choice(cases)

    prompt = (
        f"In a laboratory synthesis experiment, a learner heats a crucible containing {fmt_sa(c['m_metal'], 2)} g of pure {c['metal']} "
        f"ribbon strongly in air until completely converted into an oxide of total mass {fmt_sa(c['m_oxide'], 2)} g.\n\n"
        f"1. Calculate the mass of oxygen that combined with the {c['metal']}.\n"
        f"2. Calculate the number of moles of {c['metal']} reacted.\n"
        f"3. Calculate the number of moles of oxygen atoms that reacted.\n"
        f"4. Determine the simplest whole-number empirical formula of the metal oxide formed."
    )
    ans = (
        f"1. m(O) = m(oxide) - m(metal) = {fmt_sa(c['m_oxide'], 2)} - {fmt_sa(c['m_metal'], 2)} = {fmt_sa(c['m_o'], 2)} g; "
        f"2. n(metal) = {fmt_sa(c['n_metal'], 3)} mol; "
        f"3. n(O) = {fmt_sa(c['n_o'], 3)} mol; "
        f"4. Ratio: {c['ratio']} => Empirical formula: {c['formula']}."
    )
    memo = (
        f"1. Mass of oxygen [1]:\n"
        f"   $$m(\\text{{O}}) = {fmt_sa(c['m_oxide'], 2)} - {fmt_sa(c['m_metal'], 2)} = {fmt_sa(c['m_o'], 2)}\\text{{ g}}$$ [1]\n"
        f"2. Moles of metal [2]:\n"
        f"   $$n = \\frac{{{fmt_sa(c['m_metal'], 2)}}}{{M}} = {fmt_sa(c['n_metal'], 3)}\\text{{ mol}}$$ [2]\n"
        f"3. Moles of oxygen atoms [2]:\n"
        f"   $$n(\\text{{O}}) = \\frac{{{fmt_sa(c['m_o'], 2)}}}{{16{{,}}00}} = {fmt_sa(c['n_o'], 3)}\\text{{ mol}}$$ [2]\n"
        f"4. Empirical formula [2]: Mole ratio is {c['ratio']}, yielding $${c['formula']}$$ [2]"
    )
    hints = {
        "tier_1": "Subtract the initial metal mass from the final oxide mass to get the mass of oxygen.",
        "tier_2": "Convert both masses to moles of atoms.",
        "tier_3": f"Mole ratio is {c['ratio']}, so the empirical formula is {c['formula']}.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Oxygen mass calculation by difference", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Metal moles calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Oxygen moles calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Simplest ratio and empirical formula", "marks": 2, "editable": True},
        ],
    }
    return _build_q("33_empirical_formula_from_mass_data", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 34: Molecular Formula from Empirical & Molar Mass
# --------------------------------------------------------------------------- #
def builder_34_molecular_formula_from_empirical_and_molar_mass(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        {
            "name": "butane",
            "empirical": "\\text{C}_2\\text{H}_5",
            "m_emp": 29.06,
            "factor": 2,
            "m_mol": 58.12,
            "molecular": "\\text{C}_4\\text{H}_{10}",
        },
        {
            "name": "benzene",
            "empirical": "\\text{CH}",
            "m_emp": 13.02,
            "factor": 6,
            "m_mol": 78.12,
            "molecular": "\\text{C}_6\\text{H}_6",
        },
        {
            "name": "glucose",
            "empirical": "\\text{CH}_2\\text{O}",
            "m_emp": 30.03,
            "factor": 6,
            "m_mol": 180.18,
            "molecular": "\\text{C}_6\\text{H}_{12}\\text{O}_6",
        },
        {
            "name": "hydrogen peroxide",
            "empirical": "\\text{HO}",
            "m_emp": 17.01,
            "factor": 2,
            "m_mol": 34.02,
            "molecular": "\\text{H}_2\\text{O}_2",
        },
    ]
    c = rng.choice(compounds)

    prompt = (
        f"A chemical compound has the empirical formula ${c['empirical']}$. Experimental mass spectrometry reveals "
        f"that its actual molar mass is {fmt_sa(c['m_mol'], 2)} g·mol⁻¹.\n\n"
        f"1. Distinguish between an *empirical formula* and a *molecular formula*.\n"
        f"2. Calculate the formula mass of the empirical unit ${c['empirical']}$.\n"
        f"3. Determine the whole-number multiplier factor ($x$) relating the empirical formula to the molecular formula.\n"
        f"4. State the molecular formula of the compound."
    )
    ans = (
        f"1. An empirical formula gives the simplest whole-number ratio of atoms, whereas a molecular formula gives the actual number of atoms of each element in a molecule; "
        f"2. Empirical formula mass = {fmt_sa(c['m_emp'], 2)} g·mol⁻¹; "
        f"3. x = M(molecular) / M(empirical) = {fmt_sa(c['m_mol'], 2)} / {fmt_sa(c['m_emp'], 2)} = {c['factor']}; "
        f"4. Molecular formula: {c['molecular']}."
    )
    memo = (
        f"1. Distinction [2]: Empirical formula is the simplest ratio [1]; molecular formula represents the actual number of atoms in a molecule [1].\n"
        f"2. Empirical mass calculation [2]:\n"
        f"   $$M_{{\\text{{emp}}}} = {fmt_sa(c['m_emp'], 2)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$$ [2]\n"
        f"3. Multiplier factor [2]:\n"
        f"   $$x = \\frac{{M_{{\\text{{molecular}}}}}}{{M_{{\\text{{empirical}}}}}} = \\frac{{{fmt_sa(c['m_mol'], 2)}}}{{{fmt_sa(c['m_emp'], 2)}}} = {c['factor']}$$ [2]\n"
        f"4. Molecular formula [1]: $${c['molecular']}$$ [1]"
    )
    hints = {
        "tier_1": "Divide the experimental molar mass by the molar mass of the empirical formula.",
        "tier_2": "The multiplier must be a whole number (1, 2, 3, etc.).",
        "tier_3": f"x = {fmt_sa(c['m_mol'], 2)} / {fmt_sa(c['m_emp'], 2)} = {c['factor']}, so multiply each subscript by {c['factor']}.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Distinction between empirical and molecular formula", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Empirical formula mass calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Multiplier factor calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Final molecular formula", "marks": 1, "editable": True},
        ],
    }
    return _build_q("34_molecular_formula_from_empirical", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 35: Water of Crystallisation in Hydrated Salts
# --------------------------------------------------------------------------- #
def builder_35_water_of_crystallisation_hydrated_salts(rng: random.Random) -> Dict[str, Any]:
    salts = [
        {
            "name": "copper(II) sulphate hydrate",
            "anhydrous_form": "\\text{CuSO}_4",
            "m_anhydrous": 159.61,
            "x": 5,
            "hydrated_form": "\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}",
        },
        {
            "name": "magnesium sulphate hydrate (Epsom salts)",
            "anhydrous_form": "\\text{MgSO}_4",
            "m_anhydrous": 120.37,
            "x": 7,
            "hydrated_form": "\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}",
        },
        {
            "name": "cobalt(II) chloride hydrate",
            "anhydrous_form": "\\text{CoCl}_2",
            "m_anhydrous": 129.84,
            "x": 6,
            "hydrated_form": "\\text{CoCl}_2 \\cdot 6\\text{H}_2\\text{O}",
        },
    ]
    s = rng.choice(salts)
    moles_salt = 0.020
    mass_anh = moles_salt * s["m_anhydrous"]
    mass_water = moles_salt * (s["x"] * 18.02)
    mass_hydrated = mass_anh + mass_water

    prompt = (
        f"A sample of hydrated {s['name']} of initial mass {fmt_sa(mass_hydrated, 2)} g is heated gently in a crucible "
        f"until all the water of crystallisation has driven off. The mass of the anhydrous residue (${s['anhydrous_form']}$) is {fmt_sa(mass_anh, 2)} g.\n\n"
        f"1. Define the term *water of crystallisation*.\n"
        f"2. Calculate the mass of water lost during the heating process.\n"
        f"3. Calculate the number of moles of anhydrous ${s['anhydrous_form']}$ and moles of water ($\text{{H}}_2\text{{O}}$) driven off.\n"
        f"4. Determine the value of the integer $x$ in the formula ${s['anhydrous_form']} \\cdot x\\text{{H}}_2\\text{{O}}$."
    )
    ans = (
        f"1. Water of crystallisation is water that is chemically bonded into the crystal structure of a salt in a definite stoichiometric ratio; "
        f"2. m(water) = {fmt_sa(mass_water, 2)} g; "
        f"3. n(anhydrous) = {fmt_sa(moles_salt, 3)} mol; n(water) = {fmt_sa(moles_salt * s['x'], 3)} mol; "
        f"4. x = n(water) / n(anhydrous) = {s['x']} => Formula: {s['hydrated_form']}."
    )
    memo = (
        f"1. Definition [2]: Water molecules chemically integrated within the crystal lattice of a salt in a definite mole ratio. [2]\n"
        f"2. Water mass [1]:\n"
        f"   $$m_{{\\text{{water}}}} = {fmt_sa(mass_hydrated, 2)} - {fmt_sa(mass_anh, 2)} = {fmt_sa(mass_water, 2)}\\text{{ g}}$$ [1]\n"
        f"3. Moles calculation [3]:\n"
        f"   $$n_{{\\text{{anh}}}} = \\frac{{{fmt_sa(mass_anh, 2)}}}{{{fmt_sa(s['m_anhydrous'], 2)}}} = {fmt_sa(moles_salt, 3)}\\text{{ mol}}$$ [1M]\n"
        f"   $$n_{{\\text{{water}}}} = \\frac{{{fmt_sa(mass_water, 2)}}}{{18{{,}}02}} = {fmt_sa(moles_salt * s['x'], 3)}\\text{{ mol}}$$ [1M]\n"
        f"4. Value of x [2]:\n"
        f"   $$x = \\frac{{n_{{\\text{{water}}}}}}{{n_{{\\text{{anh}}}}}} = \\frac{{{fmt_sa(moles_salt * s['x'], 3)}}}{{{fmt_sa(moles_salt, 3)}}} = {s['x']}$$ [2]"
    )
    hints = {
        "tier_1": "Subtract the mass of the anhydrous residue from the mass of the hydrated salt to find the mass of water.",
        "tier_2": "Convert both masses to moles (M_water = 18,02 g/mol).",
        "tier_3": f"Divide moles of water by moles of anhydrous salt: x = {s['x']}.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Water of crystallisation definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Mass of water calculation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Moles of anhydrous salt and water", "marks": 3, "editable": True},
            {"id": "mp4", "desc": "Determination of coefficient x", "marks": 2, "editable": True},
        ],
    }
    return _build_q("35_water_of_crystallisation_analysis", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 36: Stoichiometric Mole-to-Mole Calculations
# --------------------------------------------------------------------------- #
def builder_36_stoichiometric_mole_ratio_calculations(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "2\\text{H}_2\\text{(g)} + \\text{O}_2\\text{(g)} \\rightarrow 2\\text{H}_2\\text{O(g)}",
            "reactant": "\\text{H}_2",
            "product": "\\text{H}_2\\text{O}",
            "ratio": 1.0,  # 2:2 => 1:1
            "name": "combustion of hydrogen",
        },
        {
            "eq": "\\text{N}_2\\text{(g)} + 3\\text{H}_2\\text{(g)} \\rightarrow 2\\text{NH}_3\\text{(g)}",
            "reactant": "\\text{N}_2",
            "product": "\\text{NH}_3",
            "ratio": 2.0,  # 1:2
            "name": "Haber-Bosch ammonia synthesis",
        },
        {
            "eq": "4\\text{Fe(s)} + 3\\text{O}_2\\text{(g)} \\rightarrow 2\\text{Fe}_2\\text{O}_3\\text{(s)}",
            "reactant": "\\text{Fe}",
            "product": "\\text{Fe}_2\\text{O}_3",
            "ratio": 0.5,  # 4:2 => 1:0.5
            "name": "oxidation of iron",
        },
    ]
    r = rng.choice(reactions)
    moles_given = rng.choice([1.50, 2.00, 3.50, 4.00, 5.00])
    moles_produced = moles_given * r["ratio"]

    prompt = (
        f"Consider the chemical reaction represented by the balanced equation:\n"
        f"$${r['eq']}$$\n\n"
        f"1. State the stoichiometric mole ratio between {r['reactant']} and {r['product']}.\n"
        f"2. Calculate the number of moles of {r['product']} produced when exactly {fmt_sa(moles_given, 2)} mol of {r['reactant']} reacts completely.\n"
        f"3. Explain why chemical calculations must be performed using mole ratios rather than mass ratios."
    )
    ans = (
        f"1. Mole ratio of {r['reactant']} to {r['product']} is derived directly from the balanced coefficients; "
        f"2. n({r['product']}) = {fmt_sa(moles_produced, 2)} mol; "
        f"3. Because different elements and compounds have different molar masses; atoms react in whole-number particle (mole) ratios, not in mass proportions."
    )
    memo = (
        f"1. Stoichiometric ratio [1]: Extracted from balanced coefficients. [1]\n"
        f"2. Moles produced [2]:\n"
        f"   $$n({r['product']}) = ({fmt_sa(moles_given, 2)}) \\times ({fmt_sa(r['ratio'], 2)}) = {fmt_sa(moles_produced, 2)}\\text{{ mol}}$$ [2]\n"
        f"3. Mole vs mass explanation [2]: Atoms and molecules react according to fixed particle ratios (moles) rather than equal mass amounts because each species has a unique molar mass. [2]"
    )
    hints = {
        "tier_1": "Look at the big numbers (coefficients) in front of the chemical formulas.",
        "tier_2": "Set up a proportion: moles product = moles reactant * (product coefficient / reactant coefficient).",
        "tier_3": f"n = {fmt_sa(moles_given, 2)} * {fmt_sa(r['ratio'], 2)} = {fmt_sa(moles_produced, 2)} mol.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Stoichiometric mole ratio from equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Mole calculation of product", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explanation of mole ratio vs mass ratio", "marks": 2, "editable": True},
        ],
    }
    return _build_q("36_stoichiometric_mole_ratio_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 37: Stoichiometric Mass-to-Mass Calculations
# --------------------------------------------------------------------------- #
def builder_37_stoichiometric_mass_mass_calculations(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "2\\text{Mg(s)} + \\text{O}_2\\text{(g)} \\rightarrow 2\\text{MgO(s)}",
            "reactant": "\\text{Mg}",
            "m_r": 24.31,
            "product": "\\text{MgO}",
            "m_p": 40.31,
            "ratio": 1.0,  # 2:2
        },
        {
            "eq": "\\text{CaCO}_3\\text{(s)} \\rightarrow \\text{CaO(s)} + \\text{CO}_2\\text{(g)}",
            "reactant": "\\text{CaCO}_3",
            "m_r": 100.09,
            "product": "\\text{CaO}",
            "m_p": 56.08,
            "ratio": 1.0,  # 1:1
        },
    ]
    r = rng.choice(reactions)
    m_given = rng.choice([12.0, 24.0, 48.0, 50.0])
    n_given = m_given / r["m_r"]
    n_prod = n_given * r["ratio"]
    m_prod = n_prod * r["m_p"]

    prompt = (
        f"Consider the reaction represented by the balanced equation:\n"
        f"$${r['eq']}$$\n\n"
        f"1. Calculate the number of moles in {fmt_sa(m_given, 1)} g of {r['reactant']} ($M = {fmt_sa(r['m_r'], 2)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"2. Use the stoichiometric mole ratio to determine the moles of {r['product']} produced.\n"
        f"3. Calculate the theoretical mass of {r['product']} produced in grams ($M = {fmt_sa(r['m_p'], 2)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. n({r['reactant']}) = m / M = {fmt_sa(m_given, 1)} / {fmt_sa(r['m_r'], 2)} = {fmt_sa(n_given, 3)} mol; "
        f"2. n({r['product']}) = {fmt_sa(n_prod, 3)} mol; "
        f"3. m({r['product']}) = n * M = {fmt_sa(n_prod, 3)} * {fmt_sa(r['m_p'], 2)} = {fmt_sa(m_prod, 2)} g."
    )
    memo = (
        f"1. Moles of reactant [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{fmt_sa(m_given, 1)}}}{{{fmt_sa(r['m_r'], 2)}}} = {fmt_sa(n_given, 3)}\\text{{ mol}}$$ [2]\n"
        f"2. Moles of product [1]:\n"
        f"   $$n({r['product']}) = {fmt_sa(n_prod, 3)}\\text{{ mol}}$$ (1:1 mole ratio) [1]\n"
        f"3. Mass of product [2]:\n"
        f"   $$m = n \\cdot M = ({fmt_sa(n_prod, 3)})({fmt_sa(r['m_p'], 2)}) = {fmt_sa(m_prod, 2)}\\text{{ g}}$$ [2]"
    )
    hints = {
        "tier_1": "Follow the 3-step pathway: Mass A -> Moles A -> Moles B -> Mass B.",
        "tier_2": "Convert mass to moles with n = m / M, use the mole ratio, then multiply by molar mass of product.",
        "tier_3": f"Theoretical mass produced = {fmt_sa(m_prod, 2)} g.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Moles of reactant calculation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Stoichiometric mole ratio conversion", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Mass of product calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("37_stoichiometric_mass_mass_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 38: Volume-Volume Stoichiometry for Gases
# --------------------------------------------------------------------------- #
def builder_38_stoichiometric_gas_volume_calculations(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "2\\text{CO(g)} + \\text{O}_2\\text{(g)} \\rightarrow 2\\text{CO}_2\\text{(g)}",
            "r1": "\\text{CO}",
            "r2": "\\text{O}_2",
            "prod": "\\text{CO}_2",
            "v_ratio_prod": 1.0,  # 2:2
            "v_ratio_r2": 0.5,    # 2:1
        },
        {
            "eq": "\\text{N}_2\\text{(g)} + 3\\text{H}_2\\text{(g)} \\rightarrow 2\\text{NH}_3\\text{(g)}",
            "r1": "\\text{N}_2",
            "r2": "\\text{H}_2",
            "prod": "\\text{NH}_3",
            "v_ratio_prod": 2.0,  # 1:2
            "v_ratio_r2": 3.0,    # 1:3
        },
    ]
    r = rng.choice(reactions)
    v_given = rng.choice([15.0, 20.0, 30.0, 50.0])
    v_r2_needed = v_given * r["v_ratio_r2"]
    v_prod = v_given * r["v_ratio_prod"]

    prompt = (
        f"Consider the gaseous reaction represented by the balanced equation at constant temperature and pressure:\n"
        f"$${r['eq']}$$\n\n"
        f"1. State Gay-Lussac's Law of combining volumes of gases.\n"
        f"2. Calculate the volume of {r['r2']} gas required to react completely with {fmt_sa(v_given, 1)} dm³ of {r['r1']}.\n"
        f"3. Calculate the volume of {r['prod']} gas formed."
    )
    ans = (
        f"1. Gay-Lussac's Law states that at constant temperature and pressure, the volumes of reacting gases and gaseous products are in simple whole-number ratios; "
        f"2. V({r['r2']}) = {fmt_sa(v_r2_needed, 1)} dm³; "
        f"3. V({r['prod']}) = {fmt_sa(v_prod, 1)} dm³."
    )
    memo = (
        f"1. Gay-Lussac's Law [2]: At constant temperature and pressure, volumes of reacting gases and products stand in simple whole-number ratios governed by stoichiometric coefficients. [2]\n"
        f"2. Volume of reactant required [2]:\n"
        f"   $$V({r['r2']}) = ({fmt_sa(v_given, 1)}) \\times ({fmt_sa(r['v_ratio_r2'], 1)}) = {fmt_sa(v_r2_needed, 1)}\\text{{ dm}}^3$$ [2]\n"
        f"3. Volume of product formed [2]:\n"
        f"   $$V({r['prod']}) = ({fmt_sa(v_given, 1)}) \\times ({fmt_sa(r['v_ratio_prod'], 1)}) = {fmt_sa(v_prod, 1)}\\text{{ dm}}^3$$ [2]"
    )
    hints = {
        "tier_1": "At constant T and P, the mole ratios in the balanced equation equal the gas volume ratios directly.",
        "tier_2": "Multiply the given volume by the stoichiometric ratio.",
        "tier_3": f"V({r['prod']}) = {fmt_sa(v_prod, 1)} dm³.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Gay-Lussac combining volumes law", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Volume of second reactant calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Volume of gaseous product calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("38_stoichiometric_gas_volume_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 39: Stoichiometric Solid-to-Gas Calculations at STP
# --------------------------------------------------------------------------- #
def builder_39_stoichiometric_mass_gas_volume_at_stp(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "\\text{CaCO}_3\\text{(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{CaCl}_2\\text{(aq)} + \\text{H}_2\\text{O(l)} + \\text{CO}_2\\text{(g)}",
            "solid": "\\text{CaCO}_3",
            "m_solid": 100.09,
            "gas": "\\text{CO}_2",
            "ratio": 1.0,  # 1:1
        },
        {
            "eq": "2\\text{KClO}_3\\text{(s)} \\rightarrow 2\\text{KCl(s)} + 3\\text{O}_2\\text{(g)}",
            "solid": "\\text{KClO}_3",
            "m_solid": 122.55,
            "gas": "\\text{O}_2",
            "ratio": 1.5,  # 2:3 => 1:1.5
        },
    ]
    r = rng.choice(reactions)
    mass_solid = rng.choice([10.0, 20.0, 25.0, 50.0])
    n_solid = mass_solid / r["m_solid"]
    n_gas = n_solid * r["ratio"]
    vol_gas_stp = n_gas * 22.4

    prompt = (
        f"Consider the reaction represented by the balanced equation:\n"
        f"$${r['eq']}$$\n\n"
        f"1. Calculate the number of moles of {r['solid']} in a {fmt_sa(mass_solid, 1)} g sample ($M = {fmt_sa(r['m_solid'], 2)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"2. Use the stoichiometric ratio to calculate the moles of {r['gas']} gas produced.\n"
        f"3. Calculate the volume of {r['gas']} gas produced at STP in dm³ ($V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. n({r['solid']}) = m / M = {fmt_sa(mass_solid, 1)} / {fmt_sa(r['m_solid'], 2)} = {fmt_sa(n_solid, 3)} mol; "
        f"2. n({r['gas']}) = {fmt_sa(n_gas, 3)} mol; "
        f"3. V({r['gas']}) = n * Vm = {fmt_sa(n_gas, 3)} * 22,4 = {fmt_sa(vol_gas_stp, 2)} dm³."
    )
    memo = (
        f"1. Moles of solid [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{fmt_sa(mass_solid, 1)}}}{{{fmt_sa(r['m_solid'], 2)}}} = {fmt_sa(n_solid, 3)}\\text{{ mol}}$$ [2]\n"
        f"2. Moles of gas [1]:\n"
        f"   $$n({r['gas']}) = ({fmt_sa(n_solid, 3)}) \\times ({fmt_sa(r['ratio'], 2)}) = {fmt_sa(n_gas, 3)}\\text{{ mol}}$$ [1]\n"
        f"3. Volume at STP [2]:\n"
        f"   $$V = n \\cdot V_m = ({fmt_sa(n_gas, 3)})(22{{,}}4) = {fmt_sa(vol_gas_stp, 2)}\\text{{ dm}}^3$$ [2]"
    )
    hints = {
        "tier_1": "Convert solid mass to moles: n = m / M.",
        "tier_2": "Apply the stoichiometric mole ratio to get the moles of gas produced.",
        "tier_3": f"Multiply moles of gas by 22,4 dm³/mol: V = {fmt_sa(vol_gas_stp, 2)} dm³.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Solid moles calculation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Gas moles stoichiometric conversion", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Gas volume at STP calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("39_stoichiometric_solid_gas_at_stp", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 40: Stoichiometric Precipitation Mass from Solution
# --------------------------------------------------------------------------- #
def builder_40_stoichiometric_solution_mass_calculations(rng: random.Random) -> Dict[str, Any]:
    v_cm3 = rng.choice([100.0, 150.0, 200.0, 250.0])
    v_dm3 = v_cm3 / 1000.0
    c_ba = rng.choice([0.10, 0.20, 0.25, 0.30])
    n_ba = c_ba * v_dm3
    # BaCl2 + Na2SO4 -> BaSO4(s) + 2 NaCl
    # 1:1 mole ratio => n(BaSO4) = n_ba
    m_baso4 = n_ba * 233.39

    prompt = (
        f"An excess of aqueous sodium sulphate ($\text{{Na}}_2\text{{SO}}_4$) is added to {fmt_sa(v_cm3, 0)} cm³ of a "
        f"{fmt_sa(c_ba, 2)} mol·dm⁻³ barium chloride ($\text{{BaCl}}_2$) solution.\n"
        f"The balanced equation is:\n"
        f"$$\\text{{BaCl}}_2\\text{{(aq)}} + \\text{{Na}}_2\\text{{SO}}_4\\text{{(aq)}} \\rightarrow \\text{{BaSO}}_4\\text{{(s)}} + 2\\text{{NaCl(aq)}}$$\n\n"
        f"1. Write down an overall balanced net ionic equation for the precipitation reaction.\n"
        f"2. Calculate the number of moles of barium chloride present.\n"
        f"3. Calculate the maximum theoretical mass of barium sulphate ($\text{{BaSO}}_4$) precipitate formed ($M = 233{{,}}39\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. Ba^2+(aq) + SO4^2-(aq) -> BaSO4(s); "
        f"2. n(BaCl2) = c * V = {fmt_sa(c_ba, 2)} * {fmt_sa(v_dm3, 3)} = {fmt_sa(n_ba, 3)} mol; "
        f"3. m(BaSO4) = n * M = {fmt_sa(n_ba, 3)} * 233,39 = {fmt_sa(m_baso4, 2)} g."
    )
    memo = (
        f"1. Net ionic equation [2]:\n"
        f"   $$\\text{{Ba}}^{{2+}}\\text{{(aq)}} + \\text{{SO}}_4^{{2-}}\\text{{(aq)}} \\rightarrow \\text{{BaSO}}_4\\text{{(s)}}$$ [2]\n"
        f"2. Moles of reactant [2]:\n"
        f"   $$n = c \\cdot V = ({fmt_sa(c_ba, 2)})({fmt_sa(v_dm3, 3)}) = {fmt_sa(n_ba, 3)}\\text{{ mol}}$$ [2]\n"
        f"3. Mass of precipitate [2]:\n"
        f"   $$m = n \\cdot M = ({fmt_sa(n_ba, 3)})(233{{,}}39) = {fmt_sa(m_baso4, 2)}\\text{{ g}}$$ [2]"
    )
    hints = {
        "tier_1": "Convert cm³ to dm³ by dividing by 1000.",
        "tier_2": "Calculate moles with n = c * V, then use the 1:1 mole ratio.",
        "tier_3": f"m = n * M = {fmt_sa(n_ba, 3)} * 233,39 = {fmt_sa(m_baso4, 2)} g.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Net ionic precipitation equation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Moles of reactant calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Mass of precipitate calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("40_stoichiometric_precipitation_mass", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 41: Limiting Reagent Identification
# --------------------------------------------------------------------------- #
def builder_41_limiting_reagent_identification(rng: random.Random) -> Dict[str, Any]:
    # 2 H2 + O2 -> 2 H2O
    moles_h2 = rng.choice([2.0, 3.0, 4.0, 5.0])
    moles_o2 = rng.choice([1.0, 1.5, 2.5, 3.0])
    # needed O2 = moles_h2 / 2
    if moles_h2 / 2.0 < moles_o2:
        limiting = "\\text{H}_2"
        excess = "\\text{O}_2"
        reason = f"reacting all {fmt_sa(moles_h2, 1)} mol of H2 requires {fmt_sa(moles_h2 / 2.0, 2)} mol of O2, but {fmt_sa(moles_o2, 1)} mol is available"
    else:
        limiting = "\\text{O}_2"
        excess = "\\text{H}_2"
        reason = f"reacting all {fmt_sa(moles_o2, 1)} mol of O2 requires {fmt_sa(moles_o2 * 2.0, 1)} mol of H2, but only {fmt_sa(moles_h2, 1)} mol is available"

    prompt = (
        f"Consider the combustion of hydrogen gas according to the balanced equation:\n"
        f"$$2\\text{{H}}_2\\text{{(g)}} + \\text{{O}}_2\\text{{(g)}} \\rightarrow 2\\text{{H}}_2\\text{{O(g)}}$$\n"
        f"A closed reaction vessel is charged with {fmt_sa(moles_h2, 1)} mol of $\\text{{H}}_2$ and {fmt_sa(moles_o2, 1)} mol of $\\text{{O}}_2$.\n\n"
        f"1. Define the term *limiting reagent*.\n"
        f"2. Determine which reactant is the limiting reagent, showing a clear stoichiometric mole comparison.\n"
        f"3. Identify the excess reagent."
    )
    ans = (
        f"1. A limiting reagent is the reactant that is completely consumed first in a reaction, determining the maximum amount of product formed; "
        f"2. Limiting reagent: {limiting} ({reason}); "
        f"3. Excess reagent: {excess}."
    )
    memo = (
        f"1. Limiting reagent definition [2]: The reactant that is completely consumed first and limits the amount of product formed. [2]\n"
        f"2. Limiting reagent determination [3]:\n"
        f"   - Ratio $\\text{{H}}_2 : \\text{{O}}_2 = 2 : 1$.\n"
        f"   - {reason}. [2M]\n"
        f"   - Limiting reagent is ${limiting}$. [1A]\n"
        f"3. Excess reagent [1]: ${excess}$. [1]"
    )
    hints = {
        "tier_1": "Divide available moles by stoichiometric coefficient: compare n(H2)/2 with n(O2)/1.",
        "tier_2": "The reactant with the smaller ratio is the limiting reagent.",
        "tier_3": f"Limiting reagent is {limiting}.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Limiting reagent definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Stoichiometric comparison working", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Limiting reagent identification", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Excess reagent identification", "marks": 1, "editable": True},
        ],
    }
    return _build_q("41_limiting_reagent_mole_identification", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 42: Limiting Reagent Product Yield Calculation
# --------------------------------------------------------------------------- #
def builder_42_limiting_reagent_mass_product_yield(rng: random.Random) -> Dict[str, Any]:
    # N2 + 3 H2 -> 2 NH3
    m_n2 = rng.choice([28.0, 56.0])
    m_h2 = rng.choice([9.0, 12.0, 18.0])
    n_n2 = m_n2 / 28.02
    n_h2 = m_h2 / 2.016

    # n_n2 requires 3 * n_n2 moles of H2
    if n_h2 < 3.0 * n_n2:
        limiting = "\\text{H}_2"
        n_nh3_theo = (2.0 / 3.0) * n_h2
    else:
        limiting = "\\text{N}_2"
        n_nh3_theo = 2.0 * n_n2
    m_nh3_theo = n_nh3_theo * 17.031

    prompt = (
        f"In the Haber process, ammonia is synthesised according to the equation:\n"
        f"$$\\text{{N}}_2\\text{{(g)}} + 3\\text{{H}}_2\\text{{(g)}} \\rightarrow 2\\text{{NH}}_3\\text{{(g)}}$$\n"
        f"A chemist mixes {fmt_sa(m_n2, 1)} g of $\\text{{N}}_2$ ($M = 28{{,}}02\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) with "
        f"{fmt_sa(m_h2, 1)} g of $\\text{{H}}_2$ ($M = 2{{,}}016\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the initial number of moles of $\\text{{N}}_2$ and $\\text{{H}}_2$.\n"
        f"2. Show by calculation which reactant is the limiting reagent.\n"
        f"3. Calculate the maximum theoretical mass of ammonia ($\text{{NH}}_3$) that can be produced in grams ($M = 17{{,}}031\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. n(N2) = {fmt_sa(n_n2, 2)} mol; n(H2) = {fmt_sa(n_h2, 2)} mol; "
        f"2. Limiting reagent is {limiting}; "
        f"3. Theoretical mass of NH3 = {fmt_sa(m_nh3_theo, 2)} g."
    )
    memo = (
        f"1. Initial moles [2]:\n"
        f"   $$n(\\text{{N}}_2) = \\frac{{{fmt_sa(m_n2, 1)}}}{{28{{,}}02}} = {fmt_sa(n_n2, 2)}\\text{{ mol}}$$ [1]\n"
        f"   $$n(\\text{{H}}_2) = \\frac{{{fmt_sa(m_h2, 1)}}}{{2{{,}}016}} = {fmt_sa(n_h2, 2)}\\text{{ mol}}$$ [1]\n"
        f"2. Limiting reagent check [2]: Comparing mole ratios identifies ${limiting}$ as limiting. [2]\n"
        f"3. Maximum mass of product [3]:\n"
        f"   $$n(\\text{{NH}}_3) = {fmt_sa(n_nh3_theo, 2)}\\text{{ mol}}$$ [1M]\n"
        f"   $$m(\\text{{NH}}_3) = ({fmt_sa(n_nh3_theo, 2)})(17{{,}}031) = {fmt_sa(m_nh3_theo, 2)}\\text{{ g}}$$ [2A]"
    )
    hints = {
        "tier_1": "Calculate moles of both reactants first.",
        "tier_2": "Identify which reactant runs out first; base the product calculation strictly on that limiting reagent.",
        "tier_3": f"Theoretical yield of NH3 = {fmt_sa(m_nh3_theo, 2)} g.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Initial moles calculations", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Limiting reagent identification with working", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Maximum mass of product calculation", "marks": 3, "editable": True},
        ],
    }
    return _build_q("42_limiting_reagent_product_yield_mass", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 43: Excess Reagent Remaining Unreacted Mass
# --------------------------------------------------------------------------- #
def builder_43_excess_reagent_remaining_mass(rng: random.Random) -> Dict[str, Any]:
    # Zn + 2 HCl -> ZnCl2 + H2
    m_zn = rng.choice([13.08, 19.62, 26.16])
    n_zn = m_zn / 65.38
    # Give excess HCl
    n_hcl_avail = n_zn * 3.0  # excess!
    v_hcl_dm3 = 0.50
    c_hcl = n_hcl_avail / v_hcl_dm3
    # Zn is limiting. HCl used = 2 * n_zn
    n_hcl_used = 2.0 * n_zn
    n_hcl_excess = n_hcl_avail - n_hcl_used
    m_hcl_excess = n_hcl_excess * 36.46

    prompt = (
        f"A {fmt_sa(m_zn, 2)} g sample of pure zinc ($\text{{Zn}}$, $M = 65{{,}}38\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) is reacted with "
        f"{fmt_sa(v_hcl_dm3 * 1000, 0)} cm³ of {fmt_sa(c_hcl, 2)} mol·dm⁻³ hydrochloric acid ($\text{{HCl}}$).\n"
        f"The balanced equation is:\n"
        f"$$\\text{{Zn(s)}} + 2\\text{{HCl(aq)}} \\rightarrow \\text{{ZnCl}}_2\\text{{(aq)}} + \\text{{H}}_2\\text{{(g)}}$$\n\n"
        f"1. Calculate the initial moles of zinc and hydrochloric acid.\n"
        f"2. Confirm that zinc is the limiting reagent.\n"
        f"3. Calculate the number of moles of hydrochloric acid that remain unreacted (in excess).\n"
        f"4. Calculate the mass of unreacted hydrochloric acid remaining in solution ($M = 36{{,}}46\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. n(Zn) = {fmt_sa(n_zn, 2)} mol; n(HCl initial) = {fmt_sa(n_hcl_avail, 2)} mol; "
        f"2. n(HCl required) = 2 * n(Zn) = {fmt_sa(n_hcl_used, 2)} mol < {fmt_sa(n_hcl_avail, 2)} mol available, confirming Zn is limiting; "
        f"3. n(HCl excess) = {fmt_sa(n_hcl_avail, 2)} - {fmt_sa(n_hcl_used, 2)} = {fmt_sa(n_hcl_excess, 2)} mol; "
        f"4. m(HCl excess) = {fmt_sa(n_hcl_excess, 2)} * 36,46 = {fmt_sa(m_hcl_excess, 2)} g."
    )
    memo = (
        f"1. Initial moles [2]:\n"
        f"   $$n(\\text{{Zn}}) = \\frac{{{fmt_sa(m_zn, 2)}}}{{65{{,}}38}} = {fmt_sa(n_zn, 2)}\\text{{ mol}}$$ [1]\n"
        f"   $$n(\\text{{HCl}}) = ({fmt_sa(c_hcl, 2)})({fmt_sa(v_hcl_dm3, 2)}) = {fmt_sa(n_hcl_avail, 2)}\\text{{ mol}}$$ [1]\n"
        f"2. Limiting reagent check [1]: 1 mol Zn requires 2 mol HCl. Zn requires {fmt_sa(n_hcl_used, 2)} mol HCl, so Zn is limiting. [1]\n"
        f"3. Excess moles [2]:\n"
        f"   $$n_{{\\text{{excess}}}} = {fmt_sa(n_hcl_avail, 2)} - {fmt_sa(n_hcl_used, 2)} = {fmt_sa(n_hcl_excess, 2)}\\text{{ mol}}$$ [2]\n"
        f"4. Excess mass [2]:\n"
        f"   $$m_{{\\text{{excess}}}} = ({fmt_sa(n_hcl_excess, 2)})(36{{,}}46) = {fmt_sa(m_hcl_excess, 2)}\\text{{ g}}$$ [2]"
    )
    hints = {
        "tier_1": "Calculate moles used = moles limiting reagent * mole ratio.",
        "tier_2": "Moles remaining unreacted = moles initial - moles used.",
        "tier_3": f"Mass of excess HCl = {fmt_sa(m_hcl_excess, 2)} g.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Initial moles calculations", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Confirmation of limiting reactant", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Moles of excess reagent remaining", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Mass of excess reagent remaining", "marks": 2, "editable": True},
        ],
    }
    return _build_q("43_excess_reagent_unreacted_mass", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 44: Theoretical Yield Determination
# --------------------------------------------------------------------------- #
def builder_44_theoretical_yield_calculation(rng: random.Random) -> Dict[str, Any]:
    # 2 Al + 3 Cl2 -> 2 AlCl3
    m_al = rng.choice([5.40, 10.80, 27.00])
    n_al = m_al / 26.98
    # 2 Al gives 2 AlCl3 => n_alcl3 = n_al
    m_alcl3_theo = n_al * 133.34

    prompt = (
        f"Consider the reaction of aluminium metal with excess chlorine gas according to the balanced equation:\n"
        f"$$2\\text{{Al(s)}} + 3\\text{{Cl}}_2\\text{{(g)}} \\rightarrow 2\\text{{AlCl}}_3\\text{{(s)}}$$\n\n"
        f"1. Define the term *theoretical yield*.\n"
        f"2. Calculate the number of moles of aluminium present in a {fmt_sa(m_al, 2)} g sample ($M = 26{{,}}98\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Calculate the theoretical yield of aluminium chloride ($\text{{AlCl}}_3$) in grams ($M = 133{{,}}34\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"4. State two experimental reasons why the actual yield in a laboratory synthesis is almost always less than the theoretical yield."
    )
    ans = (
        f"1. Theoretical yield is the maximum amount of product that can be formed from a given amount of reactant, assuming complete reaction without losses; "
        f"2. n(Al) = {fmt_sa(n_al, 2)} mol; "
        f"3. Theoretical yield = {fmt_sa(m_alcl3_theo, 2)} g; "
        f"4. Competing side reactions, incomplete reaction reaching equilibrium, and mechanical losses during transfer, filtering, or recrystallisation."
    )
    memo = (
        f"1. Theoretical yield definition [2]: The maximum calculated mass of product predicted by stoichiometry assuming 100% conversion. [2]\n"
        f"2. Moles calculation [2]:\n"
        f"   $$n(\\text{{Al}}) = \\frac{{{fmt_sa(m_al, 2)}}}{{26{{,}}98}} = {fmt_sa(n_al, 2)}\\text{{ mol}}$$ [2]\n"
        f"3. Theoretical yield calculation [2]:\n"
        f"   $$m(\\text{{AlCl}}_3) = ({fmt_sa(n_al, 2)})(133{{,}}34) = {fmt_sa(m_alcl3_theo, 2)}\\text{{ g}}$$ [2]\n"
        f"4. Reasons for yield loss [2]: Incomplete reaction / reversible equilibrium [1]; physical losses during filtering/purification or side reactions [1]."
    )
    hints = {
        "tier_1": "Theoretical yield assumes 100% stoichiometric conversion of the reactant.",
        "tier_2": "Convert Al mass to moles, use the 2:2 (1:1) ratio, and multiply by M(AlCl3).",
        "tier_3": f"Theoretical yield = {fmt_sa(m_alcl3_theo, 2)} g.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Theoretical yield definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Moles of reactant calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Theoretical mass of product calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Reasons for actual yield discrepancies", "marks": 2, "editable": True},
        ],
    }
    return _build_q("44_theoretical_yield_determination", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 45: Percentage Yield Calculations
# --------------------------------------------------------------------------- #
def builder_45_percentage_yield_calculations(rng: random.Random) -> Dict[str, Any]:
    theo_mass = rng.choice([45.0, 60.0, 80.0, 100.0])
    pct_yield = rng.choice([72.5, 78.0, 82.4, 85.0, 91.5])
    actual_mass = (pct_yield / 100.0) * theo_mass

    prompt = (
        f"In an industrial chemical synthesis, the stoichiometric calculations indicate that a maximum theoretical yield "
        f"of {fmt_sa(theo_mass, 1)} g of an organic ester should be formed. Upon purification, the chemist isolates {fmt_sa(actual_mass, 2)} g of pure ester.\n\n"
        f"1. Define the term *percentage yield*.\n"
        f"2. Write down the mathematical formula used to calculate percentage yield.\n"
        f"3. Calculate the percentage yield of the ester achieved in this reaction.\n"
        f"4. State whether a percentage yield can ever exceed 100% under ideal scientific conditions, and explain."
    )
    ans = (
        f"1. Percentage yield is the ratio of actual yield to theoretical yield expressed as a percentage; "
        f"2. % yield = (actual yield / theoretical yield) * 100%; "
        f"3. % yield = ({fmt_sa(actual_mass, 2)} / {fmt_sa(theo_mass, 1)}) * 100% = {fmt_sa(pct_yield, 1)}%; "
        f"4. No; a yield > 100% violates the Law of Conservation of Mass and indicates an impure or un-dried product."
    )
    memo = (
        f"1. Definition [2]: The measure of reaction efficiency: actual yield divided by theoretical yield as a percentage. [2]\n"
        f"2. Formula [1]: $$\\text{{Percentage yield}} = \\frac{{\\text{{Actual yield}}}}{{\\text{{Theoretical yield}}}} \\times 100\\%$$ [1]\n"
        f"3. Calculation [2]:\n"
        f"   $$\\%\\text{{ yield}} = \\frac{{{fmt_sa(actual_mass, 2)}}}{{{fmt_sa(theo_mass, 1)}}} \\times 100 = {fmt_sa(pct_yield, 1)}\\%$$ [2]\n"
        f"4. Yield > 100% explanation [2]: Impossible under valid conditions; indicates impurities, residual solvent, or moisture. [2]"
    )
    hints = {
        "tier_1": "Divide actual yield by theoretical yield and multiply by 100.",
        "tier_2": "Actual yield is always the amount measured in the laboratory.",
        "tier_3": f"% yield = ({fmt_sa(actual_mass, 2)} / {fmt_sa(theo_mass, 1)}) * 100% = {fmt_sa(pct_yield, 1)}%.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Percentage yield definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Percentage yield formula", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Percentage yield calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Conservation of mass and >100% explanation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("45_percentage_yield_calculations", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 46: Percentage Purity of Reactants
# --------------------------------------------------------------------------- #
def builder_46_percentage_purity_reactants(rng: random.Random) -> Dict[str, Any]:
    # Impure CaCO3 sample heated: CaCO3 -> CaO + CO2
    pct_purity = rng.choice([75.0, 80.0, 85.0, 90.0, 92.5])
    impure_sample_mass = rng.choice([10.0, 15.0, 20.0, 25.0])
    pure_caco3_mass = (pct_purity / 100.0) * impure_sample_mass
    n_caco3 = pure_caco3_mass / 100.09
    vol_co2_stp = n_caco3 * 22.4

    prompt = (
        f"An impure sample of limestone (containing calcium carbonate, $\text{{CaCO}}_3$) of mass {fmt_sa(impure_sample_mass, 1)} g "
        f"is heated strongly until complete decomposition according to the equation:\n"
        f"$$\\text{{CaCO}}_3\\text{{(s)}} \\rightarrow \\text{{CaO(s)}} + \\text{{CO}}_2\\text{{(g)}}$$\n"
        f"The volume of $\\text{{CO}}_2$ gas collected at STP is {fmt_sa(vol_co2_stp, 2)} dm³ ($V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$, $M(\\text{{CaCO}}_3) = 100{{,}}09\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Define the term *percentage purity*.\n"
        f"2. Calculate the number of moles of $\\text{{CO}}_2$ gas produced.\n"
        f"3. Calculate the mass of pure $\\text{{CaCO}}_3$ present in the original sample.\n"
        f"4. Calculate the percentage purity of the limestone sample."
    )
    ans = (
        f"1. Percentage purity is the mass of pure substance present divided by the total mass of the impure sample, expressed as a percentage; "
        f"2. n(CO2) = V / 22,4 = {fmt_sa(n_caco3, 3)} mol; "
        f"3. m(pure CaCO3) = n * M = {fmt_sa(n_caco3, 3)} * 100,09 = {fmt_sa(pure_caco3_mass, 2)} g; "
        f"4. % purity = (pure mass / impure mass) * 100% = ({fmt_sa(pure_caco3_mass, 2)} / {fmt_sa(impure_sample_mass, 1)}) * 100% = {fmt_sa(pct_purity, 1)}%."
    )
    memo = (
        f"1. Definition [2]: Percentage of the total sample mass consisting of the desired pure compound. [2]\n"
        f"2. Moles of gas [2]:\n"
        f"   $$n(\\text{{CO}}_2) = \\frac{{{fmt_sa(vol_co2_stp, 2)}}}{{22{{,}}4}} = {fmt_sa(n_caco3, 3)}\\text{{ mol}}$$ [2]\n"
        f"3. Mass of pure reactant [2]:\n"
        f"   $$m(\\text{{pure}}) = ({fmt_sa(n_caco3, 3)})(100{{,}}09) = {fmt_sa(pure_caco3_mass, 2)}\\text{{ g}}$$ [2]\n"
        f"4. Percentage purity [2]:\n"
        f"   $$\\%\\text{{ purity}} = \\frac{{{fmt_sa(pure_caco3_mass, 2)}}}{{{fmt_sa(impure_sample_mass, 1)}}} \\times 100 = {fmt_sa(pct_purity, 1)}\\%$$ [2]"
    )
    hints = {
        "tier_1": "Work backwards from the volume of CO2 gas produced to find the moles of pure CaCO3.",
        "tier_2": "Calculate mass of pure CaCO3 = n * M.",
        "tier_3": f"% purity = ({fmt_sa(pure_caco3_mass, 2)} / {fmt_sa(impure_sample_mass, 1)}) * 100% = {fmt_sa(pct_purity, 1)}%.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Percentage purity definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Moles of product gas calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Mass of pure reactant calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Percentage purity calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("46_percentage_purity_of_reactants", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 47: Industrial Process Stoichiometry: Fertilisers
# --------------------------------------------------------------------------- #
def builder_47_industrial_stoichiometry_fertiliser(rng: random.Random) -> Dict[str, Any]:
    # Ostwald / Nitric acid neutralization: NH3 + HNO3 -> NH4NO3
    mass_nh3_kg = rng.choice([34.0, 68.0, 102.0])  # in kg
    n_nh3_kmol = mass_nh3_kg / 17.031
    # 1:1 ratio => n(NH4NO3) = n_nh3_kmol
    mass_fertiliser_kg = n_nh3_kmol * 80.052

    prompt = (
        f"In an industrial chemical plant manufacturing ammonium nitrate fertiliser ($\text{{NH}}_4\text{{NO}}_3$), "
        f"ammonia gas is reacted with nitric acid according to the equation:\n"
        f"$$\\text{{NH}}_3\\text{{(g)}} + \\text{{HNO}}_3\\text{{(aq)}} \\rightarrow \\text{{NH}}_4\\text{{NO}}_3\\text{{(aq)}}$$\n\n"
        f"1. State the primary macronutrient provided by this fertiliser to crops.\n"
        f"2. Calculate the number of moles (in kmol) of ammonia present in {fmt_sa(mass_nh3_kg, 1)} kg of $\\text{{NH}}_3$ ($M = 17{{,}}031\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Calculate the mass in kg of ammonium nitrate fertiliser produced assuming 100% conversion ($M = 80{{,}}052\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"4. Calculate the percentage by mass of nitrogen (N) in pure ammonium nitrate."
    )
    n_pct = (2 * 14.007 / 80.052) * 100.0
    ans = (
        f"1. Nitrogen (N); "
        f"2. n(NH3) = {fmt_sa(n_nh3_kmol, 2)} kmol; "
        f"3. m(NH4NO3) = {fmt_sa(mass_fertiliser_kg, 2)} kg; "
        f"4. %N = (2 * 14,007 / 80,052) * 100% = {fmt_sa(n_pct, 1)}%."
    )
    memo = (
        f"1. Macronutrient [1]: Nitrogen (N). [1]\n"
        f"2. Moles of ammonia [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{fmt_sa(mass_nh3_kg, 1)}\\text{{ kg}}}}{{17{{,}}031\\text{{ g/mol}}}} = {fmt_sa(n_nh3_kmol, 2)}\\text{{ kmol}}$$ [2]\n"
        f"3. Mass of fertiliser [2]:\n"
        f"   $$m = n \\cdot M = ({fmt_sa(n_nh3_kmol, 2)})(80{{,}}052) = {fmt_sa(mass_fertiliser_kg, 2)}\\text{{ kg}}$$ [2]\n"
        f"4. Nitrogen percentage [2]:\n"
        f"   $$\\%\\text{{N}} = \\frac{{2 \\times 14{{,}}007}}{{80{{,}}052}} \\times 100 = {fmt_sa(n_pct, 1)}\\%$$ [2]"
    )
    hints = {
        "tier_1": "1 kmol = 1000 mol; mass in kg divided by molar mass in g/mol gives kmol.",
        "tier_2": "Note that ammonium nitrate has two nitrogen atoms per formula unit (NH4 and NO3).",
        "tier_3": f"Mass of ammonium nitrate produced = {fmt_sa(mass_fertiliser_kg, 2)} kg; %N = {fmt_sa(n_pct, 1)}%.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of nitrogen macronutrient", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Moles of ammonia calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Mass of fertiliser calculation in kg", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Percentage nitrogen content calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("47_industrial_stoichiometry_fertiliser", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 48: Back Titration Stoichiometry
# --------------------------------------------------------------------------- #
def builder_48_back_titration_stoichiometry(rng: random.Random) -> Dict[str, Any]:
    # Insoluble antacid (Mg(OH)2 or CaCO3) dissolved in excess HCl, then remaining HCl titrated with NaOH
    # Excess HCl = 50.0 cm3 of 0.20 mol/dm3 => n_initial = 0.010 mol
    # Titration of excess: 20.0 cm3 of 0.10 mol/dm3 NaOH => n_excess = 0.002 mol
    # HCl reacted with antacid = 0.010 - 0.002 = 0.008 mol
    # Mg(OH)2 + 2 HCl -> MgCl2 + 2 H2O => n(Mg(OH)2) = 0.008 / 2 = 0.004 mol
    # Mass Mg(OH)2 = 0.004 * 58.32 = 0.233 g
    v_hcl_cm3 = 50.0
    c_hcl = 0.20
    n_hcl_init = (v_hcl_cm3 / 1000.0) * c_hcl  # 0.010

    v_naoh_cm3 = rng.choice([15.0, 20.0, 25.0])
    c_naoh = 0.10
    n_naoh_used = (v_naoh_cm3 / 1000.0) * c_naoh
    n_hcl_excess = n_naoh_used  # 1:1
    n_hcl_reacted = n_hcl_init - n_hcl_excess
    n_mgoh2 = n_hcl_reacted / 2.0
    mass_mgoh2 = n_mgoh2 * 58.32

    prompt = (
        f"An antacid tablet containing magnesium hydroxide ($\text{{Mg(OH)}}_2$) is crushed and dissolved in exactly "
        f"{fmt_sa(v_hcl_cm3, 0)} cm³ of a {fmt_sa(c_hcl, 2)} mol·dm⁻³ hydrochloric acid ($\text{{HCl}}$) solution (an excess).\n"
        f"The unreacted excess hydrochloric acid requires exactly {fmt_sa(v_naoh_cm3, 1)} cm³ of a {fmt_sa(c_naoh, 2)} mol·dm⁻³ "
        f"sodium hydroxide ($\text{{NaOH}}$) solution to reach the neutralisation endpoint.\n\n"
        f"1. Define the experimental concept of a *back titration*.\n"
        f"2. Calculate the initial number of moles of hydrochloric acid added.\n"
        f"3. Calculate the number of moles of hydrochloric acid that reacted with the $\text{{NaOH}}$ solution.\n"
        f"4. Calculate the mass in grams of magnesium hydroxide present in the antacid tablet ($M = 58{{,}}32\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = (
        f"1. A back titration involves adding a known excess of standard reagent to an analyte, and then titrating the unreacted excess; "
        f"2. n(HCl initial) = {fmt_sa(n_hcl_init, 4)} mol; "
        f"3. n(HCl excess) = {fmt_sa(n_hcl_excess, 4)} mol; "
        f"4. n(reacted with antacid) = {fmt_sa(n_hcl_reacted, 4)} mol => m(Mg(OH)2) = (0,5 * n) * M = {fmt_sa(mass_mgoh2, 3)} g."
    )
    memo = (
        f"1. Back titration concept [2]: Technique where a known excess of reactant is added to an analyte, and the unreacted excess is back-titrated. [2]\n"
        f"2. Initial moles [2]:\n"
        f"   $$n(\\text{{HCl}}_{{\\text{{init}}}}) = ({fmt_sa(c_hcl, 2)})(0{{,}}050) = {fmt_sa(n_hcl_init, 4)}\\text{{ mol}}$$ [2]\n"
        f"3. Excess moles [2]:\n"
        f"   $$n(\\text{{HCl}}_{{\\text{{excess}}}}) = ({fmt_sa(c_naoh, 2)})({fmt_sa(v_naoh_cm3 / 1000, 4)}) = {fmt_sa(n_hcl_excess, 4)}\\text{{ mol}}$$ [2]\n"
        f"4. Mass of antacid [3]:\n"
        f"   $$n(\\text{{reacted}}) = {fmt_sa(n_hcl_init, 4)} - {fmt_sa(n_hcl_excess, 4)} = {fmt_sa(n_hcl_reacted, 4)}\\text{{ mol}}$$ [1M]\n"
        f"   $$n(\\text{{Mg(OH)}}_2) = \\frac{{{fmt_sa(n_hcl_reacted, 4)}}}{{2}} = {fmt_sa(n_mgoh2, 4)}\\text{{ mol}}$$ [1M]\n"
        f"   $$m = ({fmt_sa(n_mgoh2, 4)})(58{{,}}32) = {fmt_sa(mass_mgoh2, 3)}\\text{{ g}}$$ [1A]"
    )
    hints = {
        "tier_1": "Calculate: moles reacted with antacid = total initial moles of acid - moles acid neutralized by NaOH.",
        "tier_2": "Remember that 1 mole of Mg(OH)2 reacts with 2 moles of HCl.",
        "tier_3": f"Mass of Mg(OH)2 = {fmt_sa(mass_mgoh2, 3)} g.",
    }
    schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp1", "desc": "Back titration concept definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Initial acid moles calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Excess acid moles calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Mass of active ingredient calculation", "marks": 3, "editable": True},
        ],
    }
    return _build_q("48_back_titration_stoichiometry", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 49: Capstone Chemical Change Stoichiometry
# --------------------------------------------------------------------------- #
def builder_49_capstone_chemical_change_stoichiometry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A multi-stage chemical synthesis produces aspirin (acetylsalicylic acid, $\text{{C}}_9\text{{H}}_8\text{{O}}_4$, $M = 180{{,}}16\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) "
        f"by reacting salicylic acid ($\text{{C}}_7\text{{H}}_6\text{{O}}_3$, $M = 138{{,}}12\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) with acetic anhydride.\n"
        f"The balanced equation is:\n"
        f"$$\\text{{C}}_7\\text{{H}}_6\\text{{O}}_3\\text{{(s)}} + \\text{{C}}_4\\text{{H}}_6\\text{{O}}_3\\text{{(l)}} \\rightarrow \\text{{C}}_9\\text{{H}}_8\\text{{O}}_4\\text{{(s)}} + \\text{{C}}_2\\text{{H}}_4\\text{{O}}_2\\text{{(l)}}$$\n"
        f"A student uses 13,81 g of salicylic acid and isolates 14,41 g of dry purified aspirin.\n\n"
        f"1. Calculate the number of moles of salicylic acid reacted.\n"
        f"2. Calculate the theoretical yield of aspirin in grams.\n"
        f"3. Calculate the percentage yield achieved by the student.\n"
        f"4. If the purified aspirin is analysed by titration with 0,10 mol·dm⁻³ NaOH ($1:1$ stoichiometric ratio), calculate the volume of NaOH solution in cm³ required to neutralise 0,90 g of the aspirin sample."
    )
    ans = (
        f"1. n(salicylic acid) = 13,81 / 138,12 = 0,100 mol; "
        f"2. Theoretical yield = 0,100 * 180,16 = 18,02 g; "
        f"3. % yield = (14,41 / 18,02) * 100% = 79,97% (80,0%); "
        f"4. n(aspirin) = 0,90 / 180,16 = 0,0050 mol => V = n / c = 0,0050 / 0,10 = 0,050 dm³ = 50,0 cm³."
    )
    memo = (
        f"1. Moles of reactant [2]:\n"
        f"   $$n = \\frac{{13{{,}}81}}{{138{{,}}12}} = 0{{,}}100\\text{{ mol}}$$ [2]\n"
        f"2. Theoretical yield [2]:\n"
        f"   $$m = (0{{,}}100)(180{{,}}16) = 18{{,}}02\\text{{ g}}$$ [2]\n"
        f"3. Percentage yield [2]:\n"
        f"   $$\\%\\text{{ yield}} = \\frac{{14{{,}}41}}{{18{{,}}02}} \\times 100 = 80{{,}}0\\%$$ [2]\n"
        f"4. Titration volume [3]:\n"
        f"   $$n = \\frac{{0{{,}}90}}{{180{{,}}16}} = 0{{,}}0050\\text{{ mol}}$$ [1M]\n"
        f"   $$V = \\frac{{n}}{{c}} = \\frac{{0{{,}}0050}}{{0{{,}}10}} = 0{{,}}050\\text{{ dm}}^3 = 50{{,}}0\\text{{ cm}}^3$$ [2A]"
    )
    hints = {
        "tier_1": "Follow the stoichiometric sequence: moles -> theoretical mass -> percentage yield.",
        "tier_2": "For part 4, convert 0,90 g to moles using aspirin's molar mass (180,16 g/mol).",
        "tier_3": "V = n / c = 0,0050 / 0,10 = 0,050 dm³ = 50,0 cm³.",
    }
    schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp1", "desc": "Moles of salicylic acid calculation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Theoretical yield of aspirin calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Percentage yield calculation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Titration volume calculation", "marks": 3, "editable": True},
        ],
    }
    return _build_q("49_capstone_chemical_change_synthesis", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 50: Post-Exam Autopsy: Stoichiometric Misconceptions
# --------------------------------------------------------------------------- #
def builder_50_post_exam_autopsy_stoichiometric_misconceptions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During a post-examination diagnostic autopsy of a Physical Sciences paper, three recurring misconceptions were identified:\n\n"
        f"Misconception 1: A learner writes: 'Since 10 g of reactant A reacts with 10 g of reactant B, the mole ratio of the reaction must be 1:1.'\n"
        f"Misconception 2: A learner assumes that the molar gas volume of 22,4 dm³·mol⁻¹ applies to all chemical reactions at any temperature and pressure.\n"
        f"Misconception 3: A learner identifies the reactant with the smaller initial mass in grams as always being the limiting reagent.\n\n"
        f"1. Provide a scientifically rigorous refutation of Misconception 1.\n"
        f"2. Provide a scientifically rigorous refutation of Misconception 2.\n"
        f"3. Provide a scientifically rigorous refutation of Misconception 3, demonstrating how molar mass and stoichiometric coefficients dictate the limiting reactant."
    )
    ans = (
        f"1. Refutation 1: Mass ratios depend on molar mass (m = n * M); equal masses do NOT imply equal moles unless the molar masses are identical; "
        f"2. Refutation 2: 22,4 dm³·mol⁻¹ applies strictly to ideal gases at STP (0 °C and 101,3 kPa); at other temperatures or pressures (like room temperature), Vm is different; "
        f"3. Refutation 3: The limiting reagent is governed by the ratio of available moles to stoichiometric coefficient (n / coeff), not initial mass. A substance with smaller mass could have a much smaller molar mass and thus have more moles."
    )
    memo = (
        f"1. Misconception 1 refutation [2]: Mass is not conserved by proportion; moles depend on $n = m / M$. Equal mass yields different mole quantities whenever molar masses differ. [2]\n"
        f"2. Misconception 2 refutation [2]: $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$ is strictly valid at STP ($0\\text{{ }}^\\circ\\text{{C}}, 101{{,}}3\\text{{ kPa}}$); at room temperature/pressure $V_m \\approx 24\\text{{ dm}}^3$. [2]\n"
        f"3. Misconception 3 refutation [3]: Limiting reagent depends on available moles divided by stoichiometric coefficient ($\\frac{{n}}{{\\text{{coefficient}}}}$). A reactant with smaller mass can have higher moles if $M$ is small. [3]"
    )
    hints = {
        "tier_1": "Recall the fundamental difference between mass and moles.",
        "tier_2": "STP is strictly 0 °C and 101,3 kPa.",
        "tier_3": "The limiting reagent is determined by n / stoichiometric coefficient, never by mass alone.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Refutation of mass ratio equal to mole ratio", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Refutation of universal STP molar volume assumption", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Refutation of smaller mass limiting reagent fallacy", "marks": 3, "editable": True},
        ],
    }
    return _build_q("50_post_exam_autopsy_stoichiometry", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Export Map
# --------------------------------------------------------------------------- #
BUILDERS_26_50 = {
    "26_mole_and_avogadro_constant": builder_26_mole_and_avogadro_constant,
    "27_molar_mass_compound_calculations": builder_27_molar_mass_compound_calculations,
    "28_molar_gas_volume_stp_calculations": builder_28_molar_gas_volume_stp_calculations,
    "29_molar_concentration_calculations": builder_29_solution_concentration_calculations,
    "30_solution_dilution_calculations": builder_30_solution_dilution_calculation,
    "31_percentage_composition_by_mass": builder_31_percentage_composition_by_mass,
    "32_empirical_formula_from_percentage": builder_32_empirical_formula_from_percentage,
    "33_empirical_formula_from_mass_data": builder_33_empirical_formula_from_combustion_masses,
    "34_molecular_formula_from_empirical": builder_34_molecular_formula_from_empirical_and_molar_mass,
    "35_water_of_crystallisation_analysis": builder_35_water_of_crystallisation_hydrated_salts,
    "36_stoichiometric_mole_ratio_calculations": builder_36_stoichiometric_mole_ratio_calculations,
    "37_stoichiometric_mass_mass_calculations": builder_37_stoichiometric_mass_mass_calculations,
    "38_stoichiometric_gas_volume_calculations": builder_38_stoichiometric_gas_volume_calculations,
    "39_stoichiometric_solid_gas_at_stp": builder_39_stoichiometric_mass_gas_volume_at_stp,
    "40_stoichiometric_precipitation_mass": builder_40_stoichiometric_solution_mass_calculations,
    "41_limiting_reagent_mole_identification": builder_41_limiting_reagent_identification,
    "42_limiting_reagent_product_yield_mass": builder_42_limiting_reagent_mass_product_yield,
    "43_excess_reagent_unreacted_mass": builder_43_excess_reagent_remaining_mass,
    "44_theoretical_yield_determination": builder_44_theoretical_yield_calculation,
    "45_percentage_yield_calculations": builder_45_percentage_yield_calculations,
    "46_percentage_purity_of_reactants": builder_46_percentage_purity_reactants,
    "47_industrial_stoichiometry_fertiliser": builder_47_industrial_stoichiometry_fertiliser,
    "48_back_titration_stoichiometry": builder_48_back_titration_stoichiometry,
    "49_capstone_chemical_change_synthesis": builder_49_capstone_chemical_change_stoichiometry,
    "50_post_exam_autopsy_stoichiometry": builder_50_post_exam_autopsy_stoichiometric_misconceptions,
}
