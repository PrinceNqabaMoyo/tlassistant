"""Grade 10 Physical Sciences — Chemical Change: Archetypes 01 to 25.
Ground truth curriculum:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/03. States of matter and the kinetic theory molecular theory.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/02. Physical and Chemical Changes.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/02. Representing chemical change.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 3/02. Quantitative aspects of chemical change.md

Covers:
- 01–05: States of matter, Kinetic Molecular Theory (KMT), Kelvin temperature conversion, heating & cooling curves.
- 06–10: Physical vs chemical changes, energy changes (endo/exo), conservation of mass, atom rearrangement particle models.
- 11–15: Balancing synthesis, decomposition, displacement, precipitation, and combustion reactions with state symbols.
- 16–21: Relative atomic mass, molar mass M, mole-mass conversions (n = m/M), Avogadro's number (N = n*NA), atom counting.
- 22–25: Percentage composition by mass, hydrated salts water of crystallisation (x H2O), and diagnostic autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

NA = 6.02e23
VM_STP = 22.4


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format numeric values with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_sci(val: float, decimals: int = 2) -> str:
    """Format scientific notation with South African comma decimal separator."""
    exponent = int(math.floor(math.log10(abs(val))))
    mantissa = val / (10 ** exponent)
    m_str = _fmt(mantissa, decimals)
    return f"{m_str} \\times 10^{{{exponent}}}"


def _svg_heating_curve(mp: int, bp: int, substance: str) -> str:
    """Dynamic SVG of a heating curve (temperature vs time) showing solid, liquid, gas and plateaus."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 260" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Heating Curve of {substance}</text>'
        f'<line x1="55" y1="30" x2="55" y2="215" stroke="#334155" stroke-width="2"/>'
        f'<line x1="55" y1="215" x2="355" y2="215" stroke="#334155" stroke-width="2"/>'
        f'<text x="350" y="235" font-size="10" font-weight="bold" fill="#334155">Time (min)</text>'
        f'<text x="25" y="45" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 25,45)">Temp (°C)</text>'
        f'<polyline points="55,200 100,150 160,150 215,90 280,90 330,45" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<line x1="55" y1="150" x2="160" y2="150" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="48" y="154" text-anchor="end" font-size="9" fill="#1e40af">{mp}°C (m.p.)</text>'
        f'<line x1="55" y1="90" x2="280" y2="90" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="48" y="94" text-anchor="end" font-size="9" fill="#1e40af">{bp}°C (b.p.)</text>'
        f'<text x="75" y="185" font-size="9" font-weight="bold" fill="#475569">Solid</text>'
        f'<text x="110" y="142" font-size="8" fill="#ea580c">Melting</text>'
        f'<text x="175" y="125" font-size="9" font-weight="bold" fill="#475569">Liquid</text>'
        f'<text x="230" y="82" font-size="8" fill="#ea580c">Boiling</text>'
        f'<text x="300" y="60" font-size="9" font-weight="bold" fill="#475569">Gas</text>'
        f'</svg>'
    )


def _svg_cooling_curve(cond_p: int, freez_p: int, substance: str) -> str:
    """Dynamic SVG of a cooling curve (temperature vs time) showing gas, liquid, solid and plateaus."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 260" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Cooling Curve of {substance}</text>'
        f'<line x1="55" y1="30" x2="55" y2="215" stroke="#334155" stroke-width="2"/>'
        f'<line x1="55" y1="215" x2="355" y2="215" stroke="#334155" stroke-width="2"/>'
        f'<text x="350" y="235" font-size="10" font-weight="bold" fill="#334155">Time (min)</text>'
        f'<text x="25" y="45" font-size="10" font-weight="bold" fill="#334155" transform="rotate(-90 25,45)">Temp (°C)</text>'
        f'<polyline points="55,45 105,95 165,95 220,155 285,155 335,200" fill="none" stroke="#0284c7" stroke-width="2.5"/>'
        f'<line x1="55" y1="95" x2="165" y2="95" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="48" y="99" text-anchor="end" font-size="9" fill="#0369a1">{cond_p}°C</text>'
        f'<line x1="55" y1="155" x2="285" y2="155" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="48" y="159" text-anchor="end" font-size="9" fill="#0369a1">{freez_p}°C</text>'
        f'<text x="75" y="65" font-size="9" font-weight="bold" fill="#475569">Gas</text>'
        f'<text x="110" y="87" font-size="8" fill="#d97706">Condensation</text>'
        f'<text x="175" y="130" font-size="9" font-weight="bold" fill="#475569">Liquid</text>'
        f'<text x="235" y="147" font-size="8" fill="#d97706">Freezing</text>'
        f'<text x="305" y="180" font-size="9" font-weight="bold" fill="#475569">Solid</text>'
        f'</svg>'
    )


def _svg_particle_rearrangement(r1: str, r2: str, p1: str) -> str:
    """Dynamic SVG showing microscopic rearrangement of atoms in a chemical reaction."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 200" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Atom Rearrangement in Chemical Reaction</text>'
        f'<rect x="25" y="45" width="130" height="110" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="90" y="60" text-anchor="middle" font-size="10" font-weight="bold" fill="#475569">Reactants: {r1} + {r2}</text>'
        f'<circle cx="65" cy="95" r="14" fill="#3b82f6"/>'
        f'<circle cx="85" cy="95" r="14" fill="#3b82f6"/>'
        f'<circle cx="65" cy="130" r="14" fill="#3b82f6"/>'
        f'<circle cx="85" cy="130" r="14" fill="#3b82f6"/>'
        f'<circle cx="120" cy="100" r="12" fill="#ef4444"/>'
        f'<circle cx="138" cy="100" r="12" fill="#ef4444"/>'
        f'<line x1="170" y1="100" x2="205" y2="100" stroke="#0f172a" stroke-width="2.5"/>'
        f'<polygon points="212,100 202,95 202,105" fill="#0f172a"/>'
        f'<rect x="220" y="45" width="135" height="110" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="287" y="60" text-anchor="middle" font-size="10" font-weight="bold" fill="#475569">Products: {p1}</text>'
        f'<circle cx="260" cy="100" r="14" fill="#ef4444"/>'
        f'<circle cx="247" cy="85" r="10" fill="#3b82f6"/>'
        f'<circle cx="273" cy="85" r="10" fill="#3b82f6"/>'
        f'<circle cx="315" cy="100" r="14" fill="#ef4444"/>'
        f'<circle cx="302" cy="85" r="10" fill="#3b82f6"/>'
        f'<circle cx="328" cy="85" r="10" fill="#3b82f6"/>'
        f'<text x="190" y="180" text-anchor="middle" font-size="10" fill="#334155">Total number of atoms of each element is conserved</text>'
        f'</svg>'
    )


def _make_q(
    r: random.Random,
    subskill: str,
    idx: int,
    prompt: str,
    correct_answer: str,
    solution_text: str,
    marks: int,
    tags: List[str],
    rubric: List[Dict[str, Any]],
    hints: Dict[str, str],
    svg: Optional[str] = None,
) -> Dict[str, Any]:
    q_id = f"g10_chem_{idx:02d}_{r.randint(100000, 999999)}"
    marking_points = [
        {
            "id": f"mp_{i + 1}",
            "desc": item.get("criterion", f"Step {i + 1}"),
            "marks": item.get("marks", 1),
            "editable": True,
        }
        for i, item in enumerate(rubric)
    ]
    out: Dict[str, Any] = {
        "id": q_id,
        "topic": "Quantitative aspects of chemical change",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "chemical_equation",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"g10_chem_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "Rubric": rubric,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
    }
    if svg:
        out["diagram_spec"] = {
            "kind": "inline_svg",
            "svg": svg,
            "width": 380,
            "height": 260,
        }
    return out


# 01. States of matter and kinetic molecular theory properties
def build_01_states_of_matter_kinetic_molecular_theory_properties(r: random.Random) -> Dict[str, Any]:
    state = r.choice(["solid", "liquid", "gas"])
    if state == "solid":
        shape = "Fixed (definite) shape and fixed volume"
        spacing = "Closely packed in a fixed, regular lattice"
        motion = "Vibrate about fixed positions"
        forces = "Strong intermolecular / interparticle forces"
    elif state == "liquid":
        shape = "No fixed shape (takes shape of container), but fixed volume"
        spacing = "Closely packed but disordered (can slide past one another)"
        motion = "Translate and rotate freely while remaining in contact"
        forces = "Moderate intermolecular forces"
    else:
        shape = "No fixed shape and no fixed volume (expands to fill container)"
        spacing = "Very far apart with large empty spaces between particles"
        motion = "Move rapidly and randomly in all directions"
        forces = "Negligible / very weak intermolecular forces"

    prompt = (
        f"According to the **Kinetic Molecular Theory (KMT)** of matter, describe the microscopic properties of a substance in the **{state}** state:\n\n"
        f"1. Arrangement and spacing of particles.\n"
        f"2. Movement of particles.\n"
        f"3. Relative strength of forces between particles.\n"
        f"4. Macroscopic shape and volume."
    )
    ans = f"Spacing: {spacing}; Motion: {motion}; Forces: {forces}; Macroscopic: {shape}"
    sol = (
        f"For a **{state}**:\n"
        f"• **Spacing:** {spacing}.\n"
        f"• **Motion:** {motion}.\n"
        f"• **Forces:** {forces}.\n"
        f"• **Macroscopic:** {shape}."
    )
    return _make_q(
        r, "01_states_of_matter_kinetic_molecular_theory_properties", 1, prompt, ans, sol, 4,
        ["confused_liquid_compressibility_with_gas", "assumed_solid_particles_are_completely_motionless"],
        [{"step": 1, "criterion": f"Particle spacing: {spacing}", "marks": 1}, {"step": 2, "criterion": f"Particle motion: {motion}", "marks": 1}, {"step": 3, "criterion": f"Forces: {forces}", "marks": 1}, {"step": 4, "criterion": f"Macroscopic properties: {shape}", "marks": 1}],
        {"tier_1": f"Think about how particles are arranged in a {state}.", "tier_2": "Solids vibrate in fixed positions; liquids slide past one another; gases move freely and rapidly.", "tier_3": ans},
    )


# 02. Temperature and average kinetic energy Kelvin conversion
def build_02_temperature_and_average_kinetic_energy_kelvin_conversion(r: random.Random) -> Dict[str, Any]:
    celsius = r.choice([-40, -10, 0, 20, 25, 37, 78, 100, 150, 250])
    kelvin = celsius + 273
    prompt = (
        f"The temperature of a gas is measured as $T = {celsius}^\\circ\\text{{C}}$.\n\n"
        f"1. State the relationship between the absolute temperature in Kelvin and the average kinetic energy of the particles.\n"
        f"2. Convert ${celsius}^\\circ\\text{{C}}$ to the Kelvin scale ($T_{{\\text{{K}}}} = T_{{^\\circ\\text{{C}}}} + 273$)."
    )
    ans = f"T = {kelvin}\\text{{ K}}"
    sol = (
        f"1. Temperature is a measure of the **average kinetic energy** of the particles ($E_k \\propto T$ in Kelvin).\n"
        f"2. $T = {celsius} + 273 = {kelvin}\\text{{ K}}$."
    )
    return _make_q(
        r, "02_temperature_and_average_kinetic_energy_kelvin_conversion", 2, prompt, ans, sol, 2,
        ["subtracted_273_instead_of_adding_for_kelvin"],
        [{"step": 1, "criterion": "Temperature is directly proportional to average kinetic energy", "marks": 1}, {"step": 2, "criterion": f"T = {kelvin} K", "marks": 1}],
        {"tier_1": "To convert degrees Celsius to Kelvin, add 273.", "tier_2": f"{celsius} + 273.", "tier_3": ans},
    )


# 03. Heating curve phase changes and plateaus (with SVG)
def build_03_heating_curve_phase_changes_and_plateaus_svg(r: random.Random) -> Dict[str, Any]:
    subs, mp, bp = r.choice([
        ("Water", 0, 100),
        ("Ethanol", -114, 78),
        ("Benzene", 6, 80),
        ("Naphthalene", 80, 218),
    ])
    svg = _svg_heating_curve(mp, bp, subs)
    prompt = (
        f"Refer to the heating curve for pure {subs} shown in the diagram, where heat is added at a constant rate.\n\n"
        f"1. Identify the physical state of {subs} at a temperature midway between ${mp}^\\circ\\text{{C}}$ and ${bp}^\\circ\\text{{C}}$.\n"
        f"2. Explain why the temperature remains **constant** during the plateaus at ${mp}^\\circ\\text{{C}}$ and ${bp}^\\circ\\text{{C}}$ even though heat is continuously supplied."
    )
    ans = f"\\text{{Liquid}};\\ \\text{{Energy is used to overcome intermolecular forces (latent heat), not to increase kinetic energy}}"
    sol = (
        f"1. Between the melting point (${mp}^\\circ\\text{{C}}$) and boiling point (${bp}^\\circ\\text{{C}}$), the substance is in the **liquid** state.\n"
        f"2. During phase changes, the heat energy added (latent heat of fusion/vaporisation) is used to **weaken or break intermolecular forces** "
        f"rather than increase the average kinetic energy of the particles, so temperature remains constant."
    )
    return _make_q(
        r, "03_heating_curve_phase_changes_and_plateaus_svg", 3, prompt, ans, sol, 3,
        ["thought_kinetic_energy_increases_during_phase_change_plateau"],
        [{"step": 1, "criterion": "Liquid state between mp and bp", "marks": 1}, {"step": 2, "criterion": "Energy overcomes intermolecular forces / latent heat", "marks": 1}, {"step": 3, "criterion": "Average kinetic energy does not change", "marks": 1}],
        {"tier_1": "Look at the horizontal plateaus on the heating curve.", "tier_2": "Temperature measures kinetic energy. During melting/boiling, energy goes into potential energy (breaking bonds/forces).", "tier_3": ans},
        svg=svg,
    )


# 04. Cooling curve condensation freezing latent heat (with SVG)
def build_04_cooling_curve_condensation_freezing_latent_heat_svg(r: random.Random) -> Dict[str, Any]:
    subs, cond, freez = r.choice([
        ("Water", 100, 0),
        ("Paraffin wax", 68, 52),
        ("Sulfur", 445, 115),
        ("Bromine", 59, -7),
    ])
    svg = _svg_cooling_curve(cond, freez, subs)
    prompt = (
        f"Refer to the cooling curve for {subs} shown in the diagram as it is cooled from the gaseous phase to below freezing.\n\n"
        f"1. Read off the **freezing point** of {subs} from the diagram.\n"
        f"2. State what happens to the potential energy and kinetic energy of the particles along the horizontal condensation plateau at ${cond}^\\circ\\text{{C}}$."
    )
    ans = f"\\text{{Freezing point}} = {freez}^\\circ\\text{{C}};\\ E_k\\text{{ remains constant, }}E_p\\text{{ decreases as bonds form}}"
    sol = (
        f"1. The lower plateau indicates freezing at **${freez}^\\circ\\text{{C}}$**.\n"
        f"2. Along the condensation plateau at ${cond}^\\circ\\text{{C}}$, the **kinetic energy remains constant** (temperature is unchanged) "
        f"while the **potential energy decreases** as intermolecular attractions draw particles closer together."
    )
    return _make_q(
        r, "04_cooling_curve_condensation_freezing_latent_heat_svg", 4, prompt, ans, sol, 3,
        ["confused_potential_energy_with_kinetic_energy_during_cooling"],
        [{"step": 1, "criterion": f"Freezing point = {freez}°C", "marks": 1}, {"step": 2, "criterion": "Kinetic energy remains constant", "marks": 1}, {"step": 3, "criterion": "Potential energy decreases", "marks": 1}],
        {"tier_1": "Horizontal plateaus mean constant temperature and therefore constant kinetic energy.", "tier_2": "As gas condenses into liquid, intermolecular forces pull particles together, decreasing potential energy.", "tier_3": ans},
        svg=svg,
    )


# 05. Brownian motion and diffusion rates particle model
def build_05_brownian_motion_and_diffusion_rates_particle_model(r: random.Random) -> Dict[str, Any]:
    gas_pairs = [
        ("Ammonia (NH₃)", 17.0, "Hydrogen chloride (HCl)", 36.5, "ammonium chloride (NH₄Cl)"),
        ("Methane (CH₄)", 16.0, "Sulfur dioxide (SO₂)", 64.1, "gas boundary marker"),
        ("Hydrogen (H₂)", 2.0, "Carbon dioxide (CO₂)", 44.0, "diffusion front"),
        ("Helium (He)", 4.0, "Argon (Ar)", 40.0, "tracer zone"),
    ]
    gas1, m1, gas2, m2, ring_desc = r.choice(gas_pairs)
    prompt = (
        f"In a laboratory investigation of gas diffusion, {gas1} (molar mass $M = {_fmt(m1)}\\text{{ g/mol}}$) "
        f"and {gas2} (molar mass $M = {_fmt(m2)}\\text{{ g/mol}}$) are released simultaneously from opposite ends of a sealed horizontal glass tube at constant temperature.\n\n"
        f"1. Define the term **diffusion**.\n"
        f"2. State which gas diffuses faster, and explain your choice with reference to molecular mass.\n"
        f"3. Predict whether the meeting point ({ring_desc}) will occur **closer to the {gas1} end** or **closer to the {gas2} end**."
    )
    ans = f"Diffusion: movement of particles from high to low concentration; {gas1} is faster (lower mass); Closer to {gas2} end"
    sol = (
        f"1. **Diffusion:** The spontaneous movement of particles from a region of higher concentration to a region of lower concentration until evenly distributed.\n"
        f"2. **{gas1}** diffuses faster because its particles have a lower molar mass (${_fmt(m1)}\\text{{ g/mol}} < {_fmt(m2)}\\text{{ g/mol}}$) "
        f"and therefore travel at higher average speeds at the same temperature.\n"
        f"3. The meeting point forms **closer to the {gas2} end**, because the lighter {gas1} particles travel further in the same time."
    )
    return _make_q(
        r, "05_brownian_motion_and_diffusion_rates_particle_model", 5, prompt, ans, sol, 3,
        ["thought_heavier_gas_diffuses_faster"],
        [{"step": 1, "criterion": "Definition of diffusion", "marks": 1}, {"step": 2, "criterion": f"{gas1} diffuses faster due to lower molar mass", "marks": 1}, {"step": 3, "criterion": f"Meeting point closer to {gas2} end", "marks": 1}],
        {"tier_1": "Lighter gas molecules move faster at the same temperature.", "tier_2": f"{gas1} ({_fmt(m1)} g/mol) is lighter than {gas2} ({_fmt(m2)} g/mol).", "tier_3": ans},
    )


# 06. Physical vs chemical change classification
def build_06_physical_vs_chemical_change_classification(r: random.Random) -> Dict[str, Any]:
    examples = [
        ("Dissolving table salt (NaCl) in water", "Physical", "No new chemical substance is formed; salt can be recovered by evaporating water."),
        ("Rusting of an iron nail (Fe -> Fe2O3)", "Chemical", "A new chemical substance (iron(III) oxide) with different properties is formed."),
        ("Boiling water to produce steam (H2O(l) -> H2O(g))", "Physical", "Water molecules remain H2O; only intermolecular spacing increases."),
        ("Combustion of magnesium ribbon in air", "Chemical", "Magnesium atoms react with oxygen to form magnesium oxide (MgO), releasing light and heat."),
        ("Sublimation of iodine crystals upon gentle warming", "Physical", "Solid iodine changes directly to gas; chemical formula I2 is unchanged."),
        ("Electrolysis of water into hydrogen and oxygen gases", "Chemical", "Covalent bonds in H2O are broken to produce new elementary substances H2 and O2."),
    ]
    ex1, ex2 = r.sample(examples, 2)
    prompt = (
        f"Classify each of the following processes as either a **Physical Change** or a **Chemical Change**, and provide a scientific reason for each:\n\n"
        f"• Process A: {ex1[0]}\n"
        f"• Process B: {ex2[0]}"
    )
    ans = f"A: {ex1[1]}; B: {ex2[1]}"
    sol = (
        f"• **Process A:** **{ex1[1]} change.** Reason: {ex1[2]}\n"
        f"• **Process B:** **{ex2[1]} change.** Reason: {ex2[2]}"
    )
    return _make_q(
        r, "06_physical_vs_chemical_change_classification", 6, prompt, ans, sol, 4,
        ["confused_dissolving_with_chemical_reaction"],
        [{"step": 1, "criterion": f"Process A classification: {ex1[1]}", "marks": 1}, {"step": 2, "criterion": f"Process A reason", "marks": 1}, {"step": 3, "criterion": f"Process B classification: {ex2[1]}", "marks": 1}, {"step": 4, "criterion": f"Process B reason", "marks": 1}],
        {"tier_1": "Ask yourself: Is a new substance formed with new bonds?", "tier_2": "State changes and dissolving are physical; reactions that create new products are chemical.", "tier_3": ans},
    )


# 07. Energy changes exothermic vs endothermic reactions
def build_07_energy_changes_exothermic_vs_endothermic_reactions(r: random.Random) -> Dict[str, Any]:
    rxn_type = r.choice(["exothermic", "endothermic"])
    if rxn_type == "exothermic":
        name = "Combustion of methane gas"
        eq = r"\text{CH}_4(g) + 2\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\text{H}_2\text{O}(g) + \text{Energy}"
        t_change = "increases (surroundings warm up)"
        delta_h = "\\Delta H < 0\\text{ (negative)}"
        comparison = "Energy released during bond formation in products is GREATER than energy absorbed to break reactant bonds"
    else:
        name = "Thermal decomposition of calcium carbonate"
        eq = r"\text{CaCO}_3(s) + \text{Energy} \rightarrow \text{CaO}(s) + \text{CO}_2(g)"
        t_change = "decreases (absorbs thermal energy from surroundings)"
        delta_h = "\\Delta H > 0\\text{ (positive)}"
        comparison = "Energy absorbed to break bonds in reactants is GREATER than energy released when product bonds form"

    prompt = (
        f"Consider the reaction: **{name}**\n$${eq}$$\n\n"
        f"1. Classify this reaction as **exothermic** or **endothermic**.\n"
        f"2. State what happens to the temperature of the reaction mixture / surroundings.\n"
        f"3. State whether the enthalpy change ($\\Delta H$) is positive or negative.\n"
        f"4. Compare the bond energy absorbed during bond breaking with the bond energy released during bond formation."
    )
    ans = f"{rxn_type.capitalize()};\\ \\text{{Temp }} {t_change};\\ {delta_h}"
    sol = (
        f"1. The reaction is **{rxn_type}**.\n"
        f"2. The temperature of the surroundings **{t_change}**.\n"
        f"3. Enthalpy change is **${delta_h}$**.\n"
        f"4. {comparison}."
    )
    return _make_q(
        r, "07_energy_changes_exothermic_vs_endothermic_reactions", 7, prompt, ans, sol, 4,
        ["inverted_exothermic_and_endothermic_temperature_effects"],
        [{"step": 1, "criterion": f"Classify as {rxn_type}", "marks": 1}, {"step": 2, "criterion": f"Temperature {t_change}", "marks": 1}, {"step": 3, "criterion": f"Delta H sign", "marks": 1}, {"step": 4, "criterion": "Bond energy comparison", "marks": 1}],
        {"tier_1": "Exothermic releases heat (temperature rises); endothermic absorbs heat (temperature falls).", "tier_2": "Bond breaking absorbs energy; bond making releases energy.", "tier_3": ans},
    )


# 08. Conservation of mass in closed reaction system
def build_08_conservation_of_mass_in_closed_reaction_system(r: random.Random) -> Dict[str, Any]:
    m_fe = r.randint(10, 30)
    m_s = r.randint(6, 20)
    total_reactants = m_fe + m_s
    prompt = (
        f"In an experiment, ${m_fe}\\text{{ g}}$ of iron filings and ${m_s}\\text{{ g}}$ of sulfur powder are heated in a sealed crucible "
        f"to produce iron(II) sulfide ($FeS$):\n"
        f"$$\\text{{Fe}}(s) + \\text{{S}}(s) \\rightarrow \\text{{FeS}}(s)$$\n\n"
        f"1. State the **Law of Conservation of Mass**.\n"
        f"2. Calculate the theoretical total mass of iron(II) sulfide formed if all reactants react completely.\n"
        f"3. Why must the crucible be sealed if a gaseous product were involved?"
    )
    ans = f"{total_reactants}\\text{{ g}}"
    sol = (
        f"1. **Law of Conservation of Mass:** The total mass of substances present after a chemical reaction is equal to the total mass of substances present before the reaction.\n"
        f"2. Total mass of products = Total mass of reactants = ${m_fe}\\text{{ g}} + {m_s}\\text{{ g}} = {total_reactants}\\text{{ g}}$.\n"
        f"3. A closed (sealed) system prevents gases from escaping into or entering from the atmosphere, which would cause an apparent change in mass."
    )
    return _make_q(
        r, "08_conservation_of_mass_in_closed_reaction_system", 8, prompt, ans, sol, 3,
        ["thought_mass_is_lost_as_heat_in_chemical_reaction"],
        [{"step": 1, "criterion": "Statement of Law of Conservation of Mass", "marks": 1}, {"step": 2, "criterion": f"Mass of FeS = {total_reactants} g", "marks": 1}, {"step": 3, "criterion": "Closed system prevents gas escape", "marks": 1}],
        {"tier_1": "In any chemical change, mass is neither created nor destroyed.", "tier_2": f"Mass of product = {m_fe} + {m_s}.", "tier_3": ans},
    )


# 09. Law of constant composition fixed mass proportions
def build_09_law_of_constant_composition_fixed_mass_proportions(r: random.Random) -> Dict[str, Any]:
    # Water is always 2.0g H to 16.0g O => 1 : 8 mass ratio
    mult = r.randint(2, 8)
    mass_h = mult * 2.0
    mass_o = mult * 16.0
    total_water = mass_h + mass_o
    prompt = (
        f"According to the **Law of Constant Composition**, pure water ($H_2O$) always contains hydrogen and oxygen in a fixed mass ratio of $1 : 8$.\n\n"
        f"1. If a sample of pure water contains ${_fmt(mass_h)}\\text{{ g}}$ of hydrogen, calculate the mass of oxygen present.\n"
        f"2. State the total mass of this water sample."
    )
    ans = f"\\text{{Oxygen}} = {_fmt(mass_o)}\\text{{ g}},\\ \\text{{Total water}} = {_fmt(total_water)}\\text{{ g}}"
    sol = (
        f"1. Since the mass ratio $\\text{{H}} : \\text{{O}} = 1 : 8$:\n"
        f"   $\\text{{Mass of oxygen}} = 8 \\times {_fmt(mass_h)}\\text{{ g}} = {_fmt(mass_o)}\\text{{ g}}$.\n"
        f"2. $\\text{{Total mass}} = {_fmt(mass_h)} + {_fmt(mass_o)} = {_fmt(total_water)}\\text{{ g}}$."
    )
    return _make_q(
        r, "09_law_of_constant_composition_fixed_mass_proportions", 9, prompt, ans, sol, 2,
        ["divided_by_8_instead_of_multiplying_by_8_for_oxygen_mass"],
        [{"step": 1, "criterion": f"Mass of oxygen = {_fmt(mass_o)} g", "marks": 1}, {"step": 2, "criterion": f"Total mass = {_fmt(total_water)} g", "marks": 1}],
        {"tier_1": "Multiply the mass of hydrogen by 8 to find the mass of oxygen.", "tier_2": f"{_fmt(mass_h)} * 8 = {_fmt(mass_o)}.", "tier_3": ans},
    )


# 10. Microscopic particle model atom rearrangement (with SVG)
def build_10_microscopic_particle_model_atom_rearrangement_svg(r: random.Random) -> Dict[str, Any]:
    rxn_models = [
        ("2H₂", "O₂", "2H₂O", r"2\text{H}_2(g) + \text{O}_2(g) \rightarrow 2\text{H}_2\text{O}(g)", "hydrogen", "oxygen", 4, 2),
        ("N₂", "3H₂", "2NH₃", r"\text{N}_2(g) + 3\text{H}_2(g) \rightarrow 2\text{NH}_3(g)", "nitrogen", "hydrogen", 2, 6),
        ("2CO", "O₂", "2CO₂", r"2\text{CO}(g) + \text{O}_2(g) \rightarrow 2\text{CO}_2(g)", "carbon", "oxygen", 2, 4),
        ("2SO₂", "O₂", "2SO₃", r"2\text{SO}_2(g) + \text{O}_2(g) \rightarrow 2\text{SO}_3(g)", "sulfur", "oxygen", 2, 6),
    ]
    r1_lbl, r2_lbl, p1_lbl, eq_tex, e1_name, e2_name, n1_cnt, n2_cnt = r.choice(rxn_models)
    svg = _svg_particle_rearrangement(r1_lbl, r2_lbl, p1_lbl)
    prompt = (
        f"Refer to the microscopic sub-micro particle model representing the chemical reaction:\n"
        f"$${eq_tex}$$\n\n"
        f"1. Count the total number of **{e1_name} atoms** on the reactant side and product side.\n"
        f"2. Count the total number of **{e2_name} atoms** on the reactant side and product side.\n"
        f"3. Explain how this sub-micro model proves the **Law of Conservation of Atoms**."
    )
    ans = f"{n1_cnt} {e1_name} atoms on both sides; {n2_cnt} {e2_name} atoms on both sides; Atoms are rearranged, none created or destroyed"
    sol = (
        f"1. Reactants: ${n1_cnt}$ {e1_name} atoms; Products: ${n1_cnt}$ {e1_name} atoms.\n"
        f"2. Reactants: ${n2_cnt}$ {e2_name} atoms; Products: ${n2_cnt}$ {e2_name} atoms.\n"
        f"3. In this sub-micro representation, the chemical bonds in reactants are broken and new bonds are formed to make products, "
        f"but the **number and identity of atoms remain identical**, proving the Law of Conservation of Atoms."
    )
    return _make_q(
        r, "10_microscopic_particle_model_atom_rearrangement_svg", 10, prompt, ans, sol, 3,
        ["confused_molecules_with_atoms_in_particle_model"],
        [{"step": 1, "criterion": f"{n1_cnt} {e1_name} atoms on both sides", "marks": 1}, {"step": 2, "criterion": f"{n2_cnt} {e2_name} atoms on both sides", "marks": 1}, {"step": 3, "criterion": "Conservation of atoms explanation", "marks": 1}],
        {"tier_1": "Count each individual atom before and after the reaction arrow.", "tier_2": f"Both sides have {n1_cnt} {e1_name} atoms and {n2_cnt} {e2_name} atoms.", "tier_3": ans},
        svg=svg,
    )


# 11. Balancing synthesis reactions with state symbols
def build_11_balancing_synthesis_reactions_with_state_symbols(r: random.Random) -> Dict[str, Any]:
    rxns = [
        (r"\text{Mg} + \text{O}_2 \rightarrow \text{MgO}", r"2\text{Mg}(s) + \text{O}_2(g) \rightarrow 2\text{MgO}(s)", "2, 1 -> 2"),
        (r"\text{Na} + \text{Cl}_2 \rightarrow \text{NaCl}", r"2\text{Na}(s) + \text{Cl}_2(g) \rightarrow 2\text{NaCl}(s)", "2, 1 -> 2"),
        (r"\text{Al} + \text{O}_2 \rightarrow \text{Al}_2\text{O}_3", r"4\text{Al}(s) + 3\text{O}_2(g) \rightarrow 2\text{Al}_2\text{O}_3(s)", "4, 3 -> 2"),
        (r"\text{Fe} + \text{O}_2 \rightarrow \text{Fe}_2\text{O}_3", r"4\text{Fe}(s) + 3\text{O}_2(g) \rightarrow 2\text{Fe}_2\text{O}_3(s)", "4, 3 -> 2"),
        (r"\text{H}_2 + \text{N}_2 \rightarrow \text{NH}_3", r"3\text{H}_2(g) + \text{N}_2(g) \rightarrow 2\text{NH}_3(g)", "3, 1 -> 2"),
    ]
    unbal, bal, coeff = r.choice(rxns)
    prompt = (
        f"Balance the following synthesis chemical reaction and include the appropriate **state symbols** "
        f"($(s), (l), (g), \\text{{ or }} (aq)$):\n"
        f"$${unbal}$$"
    )
    ans = f"${bal}$"
    sol = f"Balancing atoms on both sides gives:\n$${bal}$$\nCoefficients: {coeff}."
    return _make_q(
        r, "11_balancing_synthesis_reactions_with_state_symbols", 11, prompt, ans, sol, 3,
        ["changed_chemical_subscripts_instead_of_coefficients"],
        [{"step": 1, "criterion": "Correct stoichiometric coefficients", "marks": 2}, {"step": 2, "criterion": "Correct state symbols", "marks": 1}],
        {"tier_1": "Count atoms of each element on reactants and products, and adjust coefficients.", "tier_2": "Never change chemical subscripts!", "tier_3": ans},
    )


# 12. Balancing decomposition reactions with state symbols
def build_12_balancing_decomposition_reactions_with_state_symbols(r: random.Random) -> Dict[str, Any]:
    rxns = [
        (r"\text{H}_2\text{O}_2 \rightarrow \text{H}_2\text{O} + \text{O}_2", r"2\text{H}_2\text{O}_2(aq) \rightarrow 2\text{H}_2\text{O}(l) + \text{O}_2(g)", "2 -> 2, 1"),
        (r"\text{KClO}_3 \rightarrow \text{KCl} + \text{O}_2", r"2\text{KClO}_3(s) \rightarrow 2\text{KCl}(s) + 3\text{O}_2(g)", "2 -> 2, 3"),
        (r"\text{CaCO}_3 \rightarrow \text{CaO} + \text{CO}_2", r"\text{CaCO}_3(s) \rightarrow \text{CaO}(s) + \text{CO}_2(g)", "1 -> 1, 1"),
        (r"\text{HgO} \rightarrow \text{Hg} + \text{O}_2", r"2\text{HgO}(s) \rightarrow 2\text{Hg}(l) + \text{O}_2(g)", "2 -> 2, 1"),
    ]
    unbal, bal, coeff = r.choice(rxns)
    prompt = (
        f"Balance the following thermal/catalytic decomposition reaction and include the correct state symbols:\n"
        f"$${unbal}$$"
    )
    ans = f"${bal}$"
    sol = f"Balanced decomposition equation:\n$${bal}$$\nCoefficients: {coeff}."
    return _make_q(
        r, "12_balancing_decomposition_reactions_with_state_symbols", 12, prompt, ans, sol, 3,
        ["omitted_diatomic_subscript_on_oxygen_gas"],
        [{"step": 1, "criterion": "Correct coefficients", "marks": 2}, {"step": 2, "criterion": "Correct state symbols", "marks": 1}],
        {"tier_1": "Oxygen gas is diatomic: O2(g).", "tier_2": f"Balanced: {bal}.", "tier_3": ans},
    )


# 13. Balancing single displacement reactions
def build_13_balancing_single_displacement_reactions(r: random.Random) -> Dict[str, Any]:
    rxns = [
        (r"\text{Zn} + \text{HCl} \rightarrow \text{ZnCl}_2 + \text{H}_2", r"\text{Zn}(s) + 2\text{HCl}(aq) \rightarrow \text{ZnCl}_2(aq) + \text{H}_2(g)"),
        (r"\text{Mg} + \text{CuSO}_4 \rightarrow \text{MgSO}_4 + \text{Cu}", r"\text{Mg}(s) + \text{CuSO}_4(aq) \rightarrow \text{MgSO}_4(aq) + \text{Cu}(s)"),
        (r"\text{Al} + \text{HCl} \rightarrow \text{AlCl}_3 + \text{H}_2", r"2\text{Al}(s) + 6\text{HCl}(aq) \rightarrow 2\text{AlCl}_3(aq) + 3\text{H}_2(g)"),
        (r"\text{Fe} + \text{CuSO}_4 \rightarrow \text{FeSO}_4 + \text{Cu}", r"\text{Fe}(s) + \text{CuSO}_4(aq) \rightarrow \text{FeSO}_4(aq) + \text{Cu}(s)"),
    ]
    unbal, bal = r.choice(rxns)
    prompt = (
        f"Balance the single displacement chemical equation below and supply the state symbols:\n"
        f"$${unbal}$$"
    )
    ans = f"${bal}$"
    sol = f"Balanced equation:\n$${bal}$$\nHydrogen gas released is $\\text{{H}}_2(g)$."
    return _make_q(
        r, "13_balancing_single_displacement_reactions", 13, prompt, ans, sol, 3,
        ["failed_to_balance_polyatomic_or_chloride_ions"],
        [{"step": 1, "criterion": "Correct balancing coefficients", "marks": 2}, {"step": 2, "criterion": "Correct state symbols", "marks": 1}],
        {"tier_1": "Balance the atoms that appear in only one formula on each side first.", "tier_2": f"{bal}.", "tier_3": ans},
    )


# 14. Balancing double displacement precipitation reactions
def build_14_balancing_double_displacement_precipitation_reactions(r: random.Random) -> Dict[str, Any]:
    rxns = [
        (r"\text{AgNO}_3 + \text{NaCl} \rightarrow \text{AgCl} + \text{NaNO}_3", r"\text{AgNO}_3(aq) + \text{NaCl}(aq) \rightarrow \text{AgCl}(s) + \text{NaNO}_3(aq)", "AgCl is the insoluble precipitate"),
        (r"\text{BaCl}_2 + \text{Na}_2\text{SO}_4 \rightarrow \text{BaSO}_4 + \text{NaCl}", r"\text{BaCl}_2(aq) + \text{Na}_2\text{SO}_4(aq) \rightarrow \text{BaSO}_4(s) + 2\text{NaCl}(aq)", "BaSO4 is the insoluble precipitate"),
        (r"\text{Pb(NO}_3)_2 + \text{KI} \rightarrow \text{PbI}_2 + \text{KNO}_3", r"\text{Pb(NO}_3)_2(aq) + 2\text{KI}(aq) \rightarrow \text{PbI}_2(s) + 2\text{KNO}_3(aq)", "PbI2 is the yellow insoluble precipitate"),
    ]
    unbal, bal, ppt_note = r.choice(rxns)
    prompt = (
        f"When aqueous solutions are mixed, a precipitate forms. Balance the precipitation equation and indicate states:\n"
        f"$${unbal}$$\n\n"
        f"Identify the insoluble precipitate formed."
    )
    ans = f"${bal}$; {ppt_note}"
    sol = f"Balanced equation:\n$${bal}$$\n{ppt_note} with state $(s)$."
    return _make_q(
        r, "14_balancing_double_displacement_precipitation_reactions", 14, prompt, ans, sol, 3,
        ["assigned_aq_state_to_insoluble_precipitate"],
        [{"step": 1, "criterion": "Balanced equation coefficients", "marks": 2}, {"step": 2, "criterion": f"Identified precipitate: {ppt_note}", "marks": 1}],
        {"tier_1": "The solid precipitate is marked as (s), while spectator salts stay in solution as (aq).", "tier_2": f"{bal}.", "tier_3": ans},
    )


# 15. Balancing combustion reactions of hydrocarbons
def build_15_balancing_combustion_reactions_of_hydrocarbons(r: random.Random) -> Dict[str, Any]:
    hydrocarbons = [
        ("Methane (CH4)", r"\text{CH}_4 + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}", r"\text{CH}_4(g) + 2\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\text{H}_2\text{O}(g)"),
        ("Propane (C3H8)", r"\text{C}_3\text{H}_8 + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}", r"\text{C}_3\text{H}_8(g) + 5\text{O}_2(g) \rightarrow 3\text{CO}_2(g) + 4\text{H}_2\text{O}(g)"),
        ("Butane (C4H10)", r"\text{C}_4\text{H}_{10} + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}", r"2\text{C}_4\text{H}_{10}(g) + 13\text{O}_2(g) \rightarrow 8\text{CO}_2(g) + 10\text{H}_2\text{O}(g)"),
        ("Ethene (C2H4)", r"\text{C}_2\text{H}_4 + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}", r"\text{C}_2\text{H}_4(g) + 3\text{O}_2(g) \rightarrow 2\text{CO}_2(g) + 2\text{H}_2\text{O}(g)"),
    ]
    name, unbal, bal = r.choice(hydrocarbons)
    prompt = (
        f"Balance the complete combustion reaction for **{name}** in excess oxygen:\n"
        f"$${unbal}$$"
    )
    ans = f"${bal}$"
    sol = f"Balancing sequence: C first, then H, then O.\n$${bal}$$"
    return _make_q(
        r, "15_balancing_combustion_reactions_of_hydrocarbons", 15, prompt, ans, sol, 3,
        ["fractional_oxygen_coefficient_not_doubled_to_whole_numbers"],
        [{"step": 1, "criterion": "Balanced carbon and hydrogen atoms", "marks": 1}, {"step": 2, "criterion": "Balanced oxygen with whole-number coefficients", "marks": 2}],
        {"tier_1": "Balance C first, then H, and finally balance O2. If you get a fraction for O2, double all coefficients.", "tier_2": f"{bal}.", "tier_3": ans},
    )


# 16. Molar mass calculation of elements and compounds
def build_16_molar_mass_calculation_of_elements_and_compounds(r: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Sulfuric acid", r"\text{H}_2\text{SO}_4", [("H", 2, 1.0), ("S", 1, 32.1), ("O", 4, 16.0)], 98.1),
        ("Calcium carbonate", r"\text{CaCO}_3", [("Ca", 1, 40.1), ("C", 1, 12.0), ("O", 3, 16.0)], 100.1),
        ("Sodium hydroxide", r"\text{NaOH}", [("Na", 1, 23.0), ("O", 1, 16.0), ("H", 1, 1.0)], 40.0),
        ("Aluminium oxide", r"\text{Al}_2\text{O}_3", [("Al", 2, 27.0), ("O", 3, 16.0)], 102.0),
        ("Ammonium nitrate", r"\text{NH}_4\text{NO}_3", [("N", 2, 14.0), ("H", 4, 1.0), ("O", 3, 16.0)], 80.0),
        ("Copper(II) sulfate", r"\text{CuSO}_4", [("Cu", 1, 63.5), ("S", 1, 32.1), ("O", 4, 16.0)], 159.6),
    ]
    name, formula, parts, mm = r.choice(compounds)
    breakdown = " + ".join([f"({count} \\times {_fmt(ar)})" for elem, count, ar in parts])
    prompt = (
        f"Calculate the **molar mass** ($M$) of **{name}** (${formula}$) in $\\text{{g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"using the periodic table values:\n"
        + ", ".join([f"$A_r({elem}) = {_fmt(ar)}$" for elem, _, ar in parts]) + "."
    )
    ans = f"{_fmt(mm)}\\text{{ g/mol}}"
    sol = (
        f"$M({formula}) = {breakdown} = {_fmt(mm)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$."
    )
    return _make_q(
        r, "16_molar_mass_calculation_of_elements_and_compounds", 16, prompt, ans, sol, 3,
        ["used_atomic_number_instead_of_relative_atomic_mass_in_molar_mass"],
        [{"step": 1, "criterion": "Formula with correct element counts", "marks": 1}, {"step": 2, "criterion": f"Substitution {breakdown}", "marks": 1}, {"step": 3, "criterion": f"M = {_fmt(mm)} g/mol", "marks": 1}],
        {"tier_1": "Multiply the number of each atom by its relative atomic mass (Ar) and add them together.", "tier_2": f"M = {breakdown}.", "tier_3": ans},
    )


# 17. Moles from mass and molar mass
def build_17_moles_from_mass_and_molar_mass(r: random.Random) -> Dict[str, Any]:
    compound, mm = r.choice([
        ("water (H2O)", 18.0),
        ("carbon dioxide (CO2)", 44.0),
        ("sodium chloride (NaCl)", 58.5),
        ("calcium carbonate (CaCO3)", 100.1),
        ("glucose (C6H12O6)", 180.0),
    ])
    n_target = r.choice([0.25, 0.5, 0.75, 1.25, 1.5, 2.0, 2.5, 3.0])
    mass = round(n_target * mm, 1)
    prompt = (
        f"A laboratory sample contains ${_fmt(mass)}\\text{{ g}}$ of {compound} (molar mass $M = {_fmt(mm)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"Calculate the **number of moles** of {compound} present in the sample ($n = \\frac{{m}}{{M}}$)."
    )
    ans = f"{_fmt(n_target)}\\text{{ mol}}"
    sol = f"$n = \\frac{{m}}{{M}} = \\frac{{{_fmt(mass)}}}{{{_fmt(mm)}}} = {_fmt(n_target)}\\text{{ mol}}$."
    return _make_q(
        r, "17_moles_from_mass_and_molar_mass", 17, prompt, ans, sol, 2,
        ["multiplied_mass_by_molar_mass_instead_of_dividing"],
        [{"step": 1, "criterion": "Formula n = m / M", "marks": 1}, {"step": 2, "criterion": f"n = {_fmt(n_target)} mol", "marks": 1}],
        {"tier_1": "Use the formula n = m / M.", "tier_2": f"n = {_fmt(mass)} / {_fmt(mm)}.", "tier_3": ans},
    )


# 18. Mass from moles and molar mass
def build_18_mass_from_moles_and_molar_mass(r: random.Random) -> Dict[str, Any]:
    compound, mm = r.choice([
        ("magnesium oxide (MgO)", 40.3),
        ("sulfuric acid (H2SO4)", 98.1),
        ("copper(II) sulfate (CuSO4)", 159.6),
        ("ammonia (NH3)", 17.0),
    ])
    n = r.choice([0.15, 0.25, 0.4, 0.5, 1.2, 2.5])
    mass = round(n * mm, 2)
    prompt = (
        f"A reaction requires ${_fmt(n)}\\text{{ moles}}$ of {compound} (molar mass $M = {_fmt(mm)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"Calculate the mass in grams ($m = n \\times M$) that the chemist must weigh out on an electronic balance."
    )
    ans = f"{_fmt(mass)}\\text{{ g}}"
    sol = f"$m = n \\times M = {_fmt(n)} \\times {_fmt(mm)} = {_fmt(mass)}\\text{{ g}}$."
    return _make_q(
        r, "18_mass_from_moles_and_molar_mass", 18, prompt, ans, sol, 2,
        ["divided_moles_by_molar_mass_instead_of_multiplying"],
        [{"step": 1, "criterion": "Formula m = n * M", "marks": 1}, {"step": 2, "criterion": f"m = {_fmt(mass)} g", "marks": 1}],
        {"tier_1": "Rearrange n = m / M to solve for mass: m = n * M.", "tier_2": f"m = {_fmt(n)} * {_fmt(mm)}.", "tier_3": ans},
    )


# 19. Number of particles from moles Avogadro
def build_19_number_of_particles_from_moles_avogadro(r: random.Random) -> Dict[str, Any]:
    n = r.choice([0.2, 0.5, 1.5, 2.0, 2.5, 3.0, 5.0])
    n_particles = n * NA
    prompt = (
        f"Calculate the total number of molecules present in ${_fmt(n)}\\text{{ moles}}$ of methane gas ($\\text{{CH}}_4$).\n\n"
        f"Use Avogadro's constant $N_A = 6{{,}}02 \\times 10^{{23}}\\text{{ molecules}}\\cdot\\text{{mol}}^{{-1}}$."
    )
    ans = f"{_fmt_sci(n_particles)}\\text{{ molecules}}"
    sol = (
        f"$N = n \\times N_A = {_fmt(n)} \\times (6{{,}}02 \\times 10^{{23}}) = {_fmt_sci(n_particles)}\\text{{ molecules}}$."
    )
    return _make_q(
        r, "19_number_of_particles_from_moles_avogadro", 19, prompt, ans, sol, 2,
        ["divided_by_avogadro_number_when_finding_particle_count"],
        [{"step": 1, "criterion": "Formula N = n * NA", "marks": 1}, {"step": 2, "criterion": f"N = {_fmt_sci(n_particles)} molecules", "marks": 1}],
        {"tier_1": "Multiply the number of moles by Avogadro's constant (6,02 x 10^23).", "tier_2": f"{_fmt(n)} * 6,02e23.", "tier_3": ans},
    )


# 20. Moles and mass from number of particles
def build_20_moles_and_mass_from_number_of_particles(r: random.Random) -> Dict[str, Any]:
    compound, mm = r.choice([
        ("water (H2O)", 18.0),
        ("carbon dioxide (CO2)", 44.0),
        ("oxygen gas (O2)", 32.0),
    ])
    n = r.choice([0.5, 1.0, 2.0, 3.0])
    n_particles = n * NA
    mass = round(n * mm, 1)
    prompt = (
        f"A canister contains ${_fmt_sci(n_particles)}$ molecules of {compound} (molar mass $M = {_fmt(mm)}\\text{{ g/mol}}$).\n\n"
        f"1. Calculate the number of moles of {compound} present in the canister ($n = \\frac{{N}}{{N_A}}$).\n"
        f"2. Calculate the mass of the gas in grams ($m = n \\times M$)."
    )
    ans = f"n = {_fmt(n)}\\text{{ mol}},\\ m = {_fmt(mass)}\\text{{ g}}"
    sol = (
        f"1. $n = \\frac{{N}}{{N_A}} = \\frac{{{_fmt_sci(n_particles)}}}{{6{{,}}02 \\times 10^{{23}}}} = {_fmt(n)}\\text{{ mol}}$.\n"
        f"2. $m = n \\times M = {_fmt(n)} \\times {_fmt(mm)} = {_fmt(mass)}\\text{{ g}}$."
    )
    return _make_q(
        r, "20_moles_and_mass_from_number_of_particles", 20, prompt, ans, sol, 3,
        ["inverted_avogadro_division_N_over_NA"],
        [{"step": 1, "criterion": f"n = N / NA = {_fmt(n)} mol", "marks": 2}, {"step": 2, "criterion": f"m = n * M = {_fmt(mass)} g", "marks": 1}],
        {"tier_1": "Divide number of particles by 6,02 x 10^23 to find moles.", "tier_2": "Then multiply moles by molar mass to find grams.", "tier_3": ans},
    )


# 21. Count specific atoms in given mass of compound
def build_21_count_specific_atoms_in_given_mass_of_compound(r: random.Random) -> Dict[str, Any]:
    # In CaCO3 (M = 100.1): each formula unit has 3 oxygen atoms
    # Or in H2O (M = 18.0): each formula unit has 2 H atoms
    compound, formula, mm, target_elem, count_per_unit = r.choice([
        ("calcium carbonate", r"\text{CaCO}_3", 100.1, "oxygen (O)", 3),
        ("water", r"\text{H}_2\text{O}", 18.0, "hydrogen (H)", 2),
        ("sulfuric acid", r"\text{H}_2\text{SO}_4", 98.1, "oxygen (O)", 4),
        ("methane", r"\text{CH}_4", 16.0, "hydrogen (H)", 4),
    ])
    n = r.choice([0.5, 1.0, 1.5, 2.0])
    mass = round(n * mm, 1)
    n_atoms = n * count_per_unit * NA
    prompt = (
        f"A sample contains ${_fmt(mass)}\\text{{ g}}$ of {compound} (${formula}$, molar mass $M = {_fmt(mm)}\\text{{ g/mol}}$).\n\n"
        f"1. Calculate the number of moles of {compound}.\n"
        f"2. Calculate the total number of **{target_elem} atoms** in this sample."
    )
    ans = f"n = {_fmt(n)}\\text{{ mol}},\\ N_{{\\text{{atoms}}}} = {_fmt_sci(n_atoms)}"
    sol = (
        f"1. $n = \\frac{{m}}{{M}} = \\frac{{{_fmt(mass)}}}{{{_fmt(mm)}}} = {_fmt(n)}\\text{{ mol}}$.\n"
        f"2. Each molecule of ${formula}$ contains ${count_per_unit}$ atoms of {target_elem}.\n"
        f"   $\\text{{Total {target_elem} atoms}} = {count_per_unit} \\times n \\times N_A = {count_per_unit} \\times {_fmt(n)} \\times 6{{,}}02 \\times 10^{{23}} = {_fmt_sci(n_atoms)}$ atoms."
    )
    return _make_q(
        r, "21_count_specific_atoms_in_given_mass_of_compound", 21, prompt, ans, sol, 3,
        ["forgot_to_multiply_by_atom_count_subscript"],
        [{"step": 1, "criterion": f"n = {mass}/{mm} = {_fmt(n)} mol", "marks": 1}, {"step": 2, "criterion": f"Multiply by {count_per_unit} atoms per unit", "marks": 1}, {"step": 3, "criterion": f"N = {_fmt_sci(n_atoms)} atoms", "marks": 1}],
        {"tier_1": "Find moles of compound first, then multiply by the subscript of the element, then multiply by NA.", "tier_2": f"N = {count_per_unit} * n * 6,02e23.", "tier_3": ans},
    )


# 22. Percentage composition by mass of elements
def build_22_percentage_composition_by_mass_of_elements(r: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Carbon dioxide", r"\text{CO}_2", 12.0, 32.0, 44.0, "Carbon", "Oxygen", 27.27, 72.73),
        ("Water", r"\text{H}_2\text{O}", 2.0, 16.0, 18.0, "Hydrogen", "Oxygen", 11.11, 88.89),
        ("Methane", r"\text{CH}_4", 12.0, 4.0, 16.0, "Carbon", "Hydrogen", 75.0, 25.0),
        ("Sodium chloride", r"\text{NaCl}", 23.0, 35.5, 58.5, "Sodium", "Chlorine", 39.32, 60.68),
    ]
    name, formula, m1, m2, mm, e1, e2, pct1, pct2 = r.choice(compounds)
    prompt = (
        f"Calculate the **percentage composition by mass** of each element in **{name}** (${formula}$, molar mass $M = {_fmt(mm)}\\text{{ g/mol}}$).\n"
        f"Give each percentage rounded to two decimal places."
    )
    ans = f"\\%\\text{{{e1}}} = {_fmt(pct1)}\\%,\\ \\%\\text{{{e2}}} = {_fmt(pct2)}\\%"
    sol = (
        f"• $\\%\\text{{{e1}}} = \\frac{{{_fmt(m1)}}}{{{_fmt(mm)}}} \\times 100\\% = {_fmt(pct1)}\\%$\n"
        f"• $\\%\\text{{{e2}}} = \\frac{{{_fmt(m2)}}}{{{_fmt(mm)}}} \\times 100\\% = {_fmt(pct2)}\\%$\n"
        f"Check: ${_fmt(pct1)}\\% + {_fmt(pct2)}\\% = 100\\%$."
    )
    return _make_q(
        r, "22_percentage_composition_by_mass_of_elements", 22, prompt, ans, sol, 3,
        ["divided_by_individual_atomic_mass_instead_of_total_compound_molar_mass"],
        [{"step": 1, "criterion": f"%{e1} = ({m1}/{mm}) * 100 = {_fmt(pct1)}%", "marks": 1}, {"step": 2, "criterion": f"%{e2} = ({m2}/{mm}) * 100 = {_fmt(pct2)}%", "marks": 1}, {"step": 3, "criterion": "Sum to 100%", "marks": 1}],
        {"tier_1": "% of element = (total mass of that element in formula / molar mass) * 100%.", "tier_2": f"%{e1} = ({m1}/{mm}) * 100; %{e2} = ({m2}/{mm}) * 100.", "tier_3": ans},
    )


# 23. Percentage water of crystallisation in hydrated salt
def build_23_percentage_water_of_crystallisation_in_hydrated_salt(r: random.Random) -> Dict[str, Any]:
    salts = [
        ("Copper(II) sulfate pentahydrate", r"\text{CuSO}_4 \cdot 5\text{H}_2\text{O}", 159.6, 5, 90.0, 249.6, 36.06),
        ("Magnesium sulfate heptahydrate", r"\text{MgSO}_4 \cdot 7\text{H}_2\text{O}", 120.4, 7, 126.0, 246.4, 51.14),
        ("Sodium carbonate decahydrate", r"\text{Na}_2\text{CO}_3 \cdot 10\text{H}_2\text{O}", 106.0, 10, 180.0, 286.0, 62.94),
        ("Cobalt(II) chloride hexahydrate", r"\text{CoCl}_2 \cdot 6\text{H}_2\text{O}", 129.8, 6, 108.0, 237.8, 45.42),
    ]
    name, formula, m_anh, x, m_water, m_hyd, pct_w = r.choice(salts)
    prompt = (
        f"Calculate the **percentage by mass of water of crystallisation** in **{name}** (${formula}$).\n"
        f"Use the molar masses: Anhydrous salt = ${_fmt(m_anh)}\\text{{ g/mol}}$, and $\\text{{H}}_2\\text{{O}} = 18{{,}}0\\text{{ g/mol}}$."
    )
    ans = f"{_fmt(pct_w)}\\%"
    sol = (
        f"Molar mass of ${formula} = {_fmt(m_anh)} + ({x} \\times 18{{,}}0) = {_fmt(m_hyd)}\\text{{ g/mol}}$.\n"
        f"Mass of water in 1 mole $= {x} \\times 18{{,}}0 = {_fmt(m_water)}\\text{{ g}}$.\n"
        f"$\\text{{Percentage water}} = \\frac{{{_fmt(m_water)}}}{{{_fmt(m_hyd)}}} \\times 100\\% = {_fmt(pct_w)}\\%$."
    )
    return _make_q(
        r, "23_percentage_water_of_crystallisation_in_hydrated_salt", 23, prompt, ans, sol, 3,
        ["divided_by_anhydrous_mass_instead_of_hydrated_mass"],
        [{"step": 1, "criterion": f"Total hydrated molar mass = {_fmt(m_hyd)} g/mol", "marks": 1}, {"step": 2, "criterion": f"Mass of water = {x} * 18 = {_fmt(m_water)} g", "marks": 1}, {"step": 3, "criterion": f"% water = {_fmt(pct_w)}%", "marks": 1}],
        {"tier_1": "% water = (mass of x*H2O / total hydrated molar mass) * 100%.", "tier_2": f"({m_water} / {m_hyd}) * 100.", "tier_3": ans},
    )


# 24. Determine formula of hydrated salt x H2O from heating mass loss
def build_24_determine_formula_of_hydrated_salt_x_h2o(r: random.Random) -> Dict[str, Any]:
    salts = [
        ("copper(II) sulfate", r"\text{CuSO}_4 \cdot x\text{H}_2\text{O}", 159.6, 5, "CuSO4 . 5H2O"),
        ("magnesium sulfate", r"\text{MgSO}_4 \cdot x\text{H}_2\text{O}", 120.4, 7, "MgSO4 . 7H2O"),
        ("calcium chloride", r"\text{CaCl}_2 \cdot x\text{H}_2\text{O}", 111.1, 2, "CaCl2 . 2H2O"),
    ]
    name, formula, mm_anh, x_val, target_name = r.choice(salts)
    n_anh = r.choice([0.02, 0.03, 0.05])
    m_anh = round(n_anh * mm_anh, 2)
    m_water = round(n_anh * x_val * 18.0, 2)
    m_hyd = round(m_anh + m_water, 2)
    prompt = (
        f"A student heats a sample of ${_fmt(m_hyd)}\\text{{ g}}$ of hydrated {name} (${formula}$) in a crucible until all water of crystallisation is driven off.\n"
        f"The mass of the dry anhydrous salt remaining is ${_fmt(m_anh)}\\text{{ g}}$.\n"
        f"(Molar masses: Anhydrous salt = ${_fmt(mm_anh)}\\text{{ g/mol}}$, $\\text{{H}}_2\\text{{O}} = 18{{,}}0\\text{{ g/mol}}$).\n\n"
        f"1. Calculate the mass of water lost during heating.\n"
        f"2. Calculate the number of moles of anhydrous salt and the number of moles of water.\n"
        f"3. Determine the integer value of $x$ and state the formula of the hydrated salt."
    )
    ans = f"x = {x_val},\\ \\text{{Formula: }} {target_name}"
    sol = (
        f"1. $\\text{{Mass of water lost}} = {_fmt(m_hyd)} - {_fmt(m_anh)} = {_fmt(m_water)}\\text{{ g}}$.\n"
        f"2. $n(\\text{{anhydrous}}) = \\frac{{{_fmt(m_anh)}}}{{{_fmt(mm_anh)}}} = {_fmt(n_anh, 4)}\\text{{ mol}}$.\n"
        f"   $n(\\text{{H}}_2\\text{{O}}) = \\frac{{{_fmt(m_water)}}}{{18{{,}}0}} = {_fmt(n_anh * x_val, 4)}\\text{{ mol}}$.\n"
        f"3. Mole ratio $x = \\frac{{n(\\text{{H}}_2\\text{{O}})}}{{n(\\text{{anhydrous}})}} = \\frac{{{_fmt(n_anh * x_val, 4)}}}{{{_fmt(n_anh, 4)}}} = {x_val}$.\n"
        f"   Formula: **{target_name}**."
    )
    return _make_q(
        r, "24_determine_formula_of_hydrated_salt_x_h2o", 24, prompt, ans, sol, 4,
        ["inverted_mole_ratio_anhydrous_over_water"],
        [{"step": 1, "criterion": f"Mass of water = {_fmt(m_water)} g", "marks": 1}, {"step": 2, "criterion": "Moles of anhydrous and water", "marks": 1}, {"step": 3, "criterion": f"Ratio x = {x_val}", "marks": 1}, {"step": 4, "criterion": f"Formula {target_name}", "marks": 1}],
        {"tier_1": "Subtract dry mass from initial mass to get grams of water lost.", "tier_2": "Convert both masses to moles and divide moles of water by moles of anhydrous salt.", "tier_3": ans},
    )


# 25. Chemical change foundations diagnostic autopsy
def build_25_chemical_change_foundations_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    errors = [
        (
            "Balancing equations by altering subscripts",
            "A learner writes $H_2 + O_2 -> H_2O_2$ when attempting to balance the formation of water.",
            "Altering subscripts changes the chemical identity of the substance (H2O2 is hydrogen peroxide, not water). Only coefficients placed in front of formulas may be adjusted: 2H2 + O2 -> 2H2O."
        ),
        (
            "Molar mass using atomic number",
            "A learner calculates the molar mass of carbon dioxide (CO2) using atomic numbers: M = 6 + (2 * 8) = 22 g/mol.",
            "Molar mass requires the relative atomic mass (Ar from mass number), not the atomic number (Z): M = 12 + (2 * 16) = 44 g/mol."
        ),
        (
            "Avogadro's number multiplication error",
            "A learner calculates moles from 1,204 x 10^24 particles by multiplying by 6,02 x 10^23: n = 1,204 x 10^24 * 6,02 x 10^23 = 7,25 x 10^47 mol.",
            "To find moles from particle count, divide by Avogadro's constant: n = N / NA = (1,204 x 10^24) / (6,02 x 10^23) = 2 mol."
        ),
    ]
    err_title, err_desc, correction = r.choice(errors)
    prompt = (
        f"**Diagnostic Autopsy:** Review the following common learner error in quantitative chemistry:\n\n"
        f"**Error Description:** {err_desc}\n\n"
        f"1. Identify the fundamental misconception committed by the learner.\n"
        f"2. Provide the corrected calculation and state the underlying scientific rule violated."
    )
    ans = f"{correction}"
    sol = f"**Misconception Analysis:** {err_title}.\n\n**Scientific Correction:** {correction}"
    return _make_q(
        r, "25_chemical_change_foundations_diagnostic_autopsy", 25, prompt, ans, sol, 3,
        ["misconception_in_foundational_stoichiometry_concept"],
        [{"step": 1, "criterion": f"Identified error: {err_title}", "marks": 1}, {"step": 2, "criterion": "Underlying scientific rule explained", "marks": 1}, {"step": 3, "criterion": "Corrected calculation provided", "marks": 1}],
        {"tier_1": "Carefully compare what the learner did against standard chemical rules.", "tier_2": "Look at whether subscripts were changed, atomic numbers used, or formulas inverted.", "tier_3": ans},
    )


BUILDERS_01_25 = {
    "01_states_of_matter_kinetic_molecular_theory_properties": build_01_states_of_matter_kinetic_molecular_theory_properties,
    "02_temperature_and_average_kinetic_energy_kelvin_conversion": build_02_temperature_and_average_kinetic_energy_kelvin_conversion,
    "03_heating_curve_phase_changes_and_plateaus_svg": build_03_heating_curve_phase_changes_and_plateaus_svg,
    "04_cooling_curve_condensation_freezing_latent_heat_svg": build_04_cooling_curve_condensation_freezing_latent_heat_svg,
    "05_brownian_motion_and_diffusion_rates_particle_model": build_05_brownian_motion_and_diffusion_rates_particle_model,
    "06_physical_vs_chemical_change_classification": build_06_physical_vs_chemical_change_classification,
    "07_energy_changes_exothermic_vs_endothermic_reactions": build_07_energy_changes_exothermic_vs_endothermic_reactions,
    "08_conservation_of_mass_in_closed_reaction_system": build_08_conservation_of_mass_in_closed_reaction_system,
    "09_law_of_constant_composition_fixed_mass_proportions": build_09_law_of_constant_composition_fixed_mass_proportions,
    "10_microscopic_particle_model_atom_rearrangement_svg": build_10_microscopic_particle_model_atom_rearrangement_svg,
    "11_balancing_synthesis_reactions_with_state_symbols": build_11_balancing_synthesis_reactions_with_state_symbols,
    "12_balancing_decomposition_reactions_with_state_symbols": build_12_balancing_decomposition_reactions_with_state_symbols,
    "13_balancing_single_displacement_reactions": build_13_balancing_single_displacement_reactions,
    "14_balancing_double_displacement_precipitation_reactions": build_14_balancing_double_displacement_precipitation_reactions,
    "15_balancing_combustion_reactions_of_hydrocarbons": build_15_balancing_combustion_reactions_of_hydrocarbons,
    "16_molar_mass_calculation_of_elements_and_compounds": build_16_molar_mass_calculation_of_elements_and_compounds,
    "17_moles_from_mass_and_molar_mass": build_17_moles_from_mass_and_molar_mass,
    "18_mass_from_moles_and_molar_mass": build_18_mass_from_moles_and_molar_mass,
    "19_number_of_particles_from_moles_avogadro": build_19_number_of_particles_from_moles_avogadro,
    "20_moles_and_mass_from_number_of_particles": build_20_moles_and_mass_from_number_of_particles,
    "21_count_specific_atoms_in_given_mass_of_compound": build_21_count_specific_atoms_in_given_mass_of_compound,
    "22_percentage_composition_by_mass_of_elements": build_22_percentage_composition_by_mass_of_elements,
    "23_percentage_water_of_crystallisation_in_hydrated_salt": build_23_percentage_water_of_crystallisation_in_hydrated_salt,
    "24_determine_formula_of_hydrated_salt_x_h2o": build_24_determine_formula_of_hydrated_salt_x_h2o,
    "25_chemical_change_foundations_diagnostic_autopsy": build_25_chemical_change_foundations_diagnostic_autopsy,
}
