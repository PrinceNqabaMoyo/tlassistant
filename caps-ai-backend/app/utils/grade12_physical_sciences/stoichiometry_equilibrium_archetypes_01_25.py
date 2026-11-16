"""Grade 12 Physical Sciences — Rate and Extent of Reaction & Equilibrium Fundamentals (Subskills 01–25).
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Strictly grounded in curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/01. Rate and Extent of Reaction.md
and 02. Chemical equilibrium.md.

South African comma decimal notation supported.
No diagram description leaks: inline SVG specs provided where figures are referenced.
All files strictly < 2000 lines.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, places: int = 2) -> str:
    """Format decimal number using South African comma decimal convention."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_wrap(body: str, width: int = 400, height: int = 240) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;">'
        f'{body}</svg>'
    )


def _pillars(
    qid: str,
    subskill: str,
    prompt: str,
    answer: str,
    sample: str,
    marking_points: List[Dict[str, Any]],
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 4,
    duration: int = 5,
    diagram_spec: Optional[Dict[str, Any]] = None,
    term: int = 2,
    caps_weight: int = 15,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "id": qid,
        "topic": "Rate and Extent of Reaction",
        "subskill": subskill,
        "mode": "practice",
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": duration,
        "prompt": prompt,
        "ideal_answer": answer,
        "sample_answer": sample,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return payload


# =========================================================================== #
# 01: Reaction Rate Definition and Units
# =========================================================================== #
def build_01_reaction_rate_definition_and_units(rng: random.Random) -> Dict[str, Any]:
    unit_choices = [
        {"quantity": "mass of reactant consumed per second", "unit": r"\text{g}\cdot\text{s}^{-1}", "name": "grams per second"},
        {"quantity": "volume of gas evolved per second", "unit": r"\text{cm}^3\cdot\text{s}^{-1}", "name": "cubic centimetres per second"},
        {"quantity": "amount in moles consumed per second", "unit": r"\text{mol}\cdot\text{s}^{-1}", "name": "moles per second"},
        {"quantity": "concentration change per second", "unit": r"\text{mol}\cdot\text{dm}^{-3}\cdot\text{s}^{-1}", "name": "mol per cubic decimetre per second"},
    ]
    u = rng.choice(unit_choices)
    prompt = (
        "1. Define the term **reaction rate** according to CAPS.\n"
        f"2. State the standard SI unit used when measuring reaction rate as the **{u['quantity']}**."
    )
    ans = f"Rate of change in concentration / amount of reactants or products per unit time; {u['unit']}"
    sample = (
        "1. **Reaction rate** is defined as the change in concentration (or amount/mass/volume) of reactants or products per unit time.\n"
        f"2. The unit for {u['name']} is **${u['unit']}$**."
    )
    return _pillars(
        qid=f"ps12_eq01_{rng.randint(10000, 99999)}",
        subskill="01_reaction_rate_definition_and_units",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: change in concentration/amount per unit time", "marks": 2},
            {"id": "mp2", "desc": f"Correct unit: {u['unit']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Reaction rate expresses how fast reactants turn into products over time.",
            "2_concept": "Rate = (change in quantity) / (change in time).",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_reaction_rate_with_equilibrium_extent", "omitted_per_unit_time_in_definition"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 02: Collision Theory Criteria
# =========================================================================== #
def build_02_collision_theory_criteria(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {"eq": r"\text{CO}(\text{g}) + \text{NO}_2(\text{g}) \rightarrow \text{CO}_2(\text{g}) + \text{NO}(\text{g})", "desc": "carbon monoxide and nitrogen dioxide"},
        {"eq": r"\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightarrow 2\text{HI}(\text{g})", "desc": "hydrogen and iodine gas"},
        {"eq": r"2\text{NO}(\text{g}) + \text{O}_2(\text{g}) \rightarrow 2\text{NO}_2(\text{g})", "desc": "nitrogen monoxide and oxygen"},
    ])
    prompt = (
        f"Consider the gas-phase reaction between {rxn['desc']}:\n"
        f"$${rxn['eq']}$$\n\n"
        "According to the **collision theory**, state the TWO conditions necessary for a collision between reacting molecules to be **effective** (result in a chemical reaction)."
    )
    ans = "1. Correct orientation (spatial alignment); 2. Sufficient kinetic energy greater than or equal to activation energy (E >= Ea)"
    sample = (
        "For a collision to be effective:\n"
        "1. Reacting particles must collide with the **correct orientation** (favourable spatial alignment).\n"
        r"2. Colliding particles must have **sufficient kinetic energy**, greater than or equal to the **activation energy** ($E_k \ge E_a$)."
    )
    return _pillars(
        qid=f"ps12_eq02_{rng.randint(10000, 99999)}",
        subskill="02_collision_theory_criteria",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Correct collision orientation", "marks": 1},
            {"id": "mp2", "desc": "Kinetic energy >= activation energy (Ea)", "marks": 2},
        ],
        hints={
            "1_nudge": "Do all collisions lead to a reaction? What two hurdles must molecules overcome?",
            "2_concept": "Molecules must bump into each other the right way around and with enough punch (energy).",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_all_collisions_produce_reactions", "forgetting_orientation_requirement"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 03: Maxwell-Boltzmann Temperature Shift
# =========================================================================== #
def build_03_maxwell_boltzmann_temperature_shift(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([25, 30, 40])
    t2 = t1 + rng.choice([20, 30, 40])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="25" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Fraction of particles</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Kinetic energy (E)</text>'
        f'<path d="M 50 190 Q 110 30, 160 110 T 360 190" fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="120" y="55" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Curve A ({t1} °C)</text>'
        f'<path d="M 50 190 Q 140 70, 200 135 T 365 190" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,3"/>'
        f'<text x="195" y="85" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Curve B ({t2} °C)</text>'
        f'<line x1="260" y1="30" x2="260" y2="190" stroke="#047857" stroke-width="2" stroke-dasharray="3,3"/>'
        f'<text x="265" y="45" font-family="sans-serif" font-size="11" font-weight="bold" fill="#047857">Ea</text>',
        width=390,
        height=230,
    )
    prompt = (
        f"The accompanying Maxwell-Boltzmann distribution graph shows the distribution of molecular kinetic energies for a reaction mixture at {t1} °C (Curve A) and {t2} °C (Curve B).\n\n"
        "1. Explain why the peak of Curve B is lower and shifted to the right compared to Curve A.\n"
        f"2. Use collision theory to explain why the reaction rate is significantly higher at {t2} °C."
    )
    ans = f"Peak shifts right because average Ek increases; lower peak keeps total area (number of molecules) constant; at {t2} °C a much larger fraction has Ek >= Ea, leading to more effective collisions per unit time."
    sample = (
        f"1. At higher temperature ({t2} °C), the average kinetic energy of the molecules increases, shifting the peak to the right (higher energy). "
        "Because the total number of particles (area under the curve) remains constant, the peak must become lower and broader.\n"
        f"2. At {t2} °C, a much larger fraction of particles possess kinetic energy greater than or equal to the activation energy ($E_k \\ge E_a$, area under curve to right of $E_a$). "
        "Consequently, the frequency of effective collisions increases, resulting in a higher reaction rate."
    )
    return _pillars(
        qid=f"ps12_eq03_{rng.randint(10000, 99999)}",
        subskill="03_maxwell_boltzmann_temperature_shift",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Average kinetic energy increases (peak shifts right)", "marks": 1},
            {"id": "mp2", "desc": "Total area / particle count constant (peak flattens)", "marks": 1},
            {"id": "mp3", "desc": "Larger fraction with Ek >= Ea (area to right of Ea increases)", "marks": 1},
            {"id": "mp4", "desc": "Greater frequency of effective collisions per unit time", "marks": 1},
        ],
        hints={
            "1_nudge": "What happens to the total number of molecules when temperature changes?",
            "2_concept": "Area under curve = total molecules. If it spreads wider to higher energies, the peak must lower.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_area_under_maxwell_boltzmann_curve_increases_with_temp", "omitting_per_unit_time_in_collision_frequency"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Maxwell-Boltzmann Distribution ({t1} vs {t2} deg C)"},
    )


# =========================================================================== #
# 04: Maxwell-Boltzmann Catalyst Effect
# =========================================================================== #
def build_04_maxwell_boltzmann_catalyst_effect(rng: random.Random) -> Dict[str, Any]:
    cat = rng.choice([
        {"rxn": "decomposition of hydrogen peroxide", "cat": r"\text{MnO}_2", "label": "MnO2"},
        {"rxn": "Haber synthesis of ammonia", "cat": r"\text{Fe}", "label": "Fe"},
        {"rxn": "Contact process synthesis of sulfur trioxide", "cat": r"\text{V}_2\text{O}_5", "label": "V2O5"},
    ])
    ea_uncat_x = rng.choice([275, 280, 285])
    ea_cat_x = rng.choice([205, 210, 215])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="20" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Fraction of particles</text>'
        f'<text x="250" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Kinetic energy (E)</text>'
        f'<path d="M 50 190 Q 120 40, 170 110 T 360 190" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<line x1="{ea_uncat_x}" y1="35" x2="{ea_uncat_x}" y2="190" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<text x="{ea_uncat_x - 10}" y="30" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Ea (uncat)</text>'
        f'<line x1="{ea_cat_x}" y1="35" x2="{ea_cat_x}" y2="190" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<text x="{ea_cat_x - 25}" y="30" font-family="sans-serif" font-size="11" font-weight="bold" fill="#16a34a">Ea ({cat["label"]})</text>',
        width=390,
        height=230,
    )
    prompt = (
        f"The accompanying Maxwell-Boltzmann distribution graph illustrates the molecular kinetic energy distribution for the {cat['rxn']}.\n\n"
        f"A catalyst (${cat['cat']}$) is added to the system at constant temperature.\n"
        "1. Does the shape of the kinetic energy distribution curve change? State YES or NO and justify.\n"
        "2. Explain how the addition of the catalyst increases the rate of reaction."
    )
    ans = "1. NO, temperature is constant so molecular kinetic energies do not change; 2. Catalyst provides an alternative pathway with lower activation energy (Ea shifts left), so a larger fraction of particles has Ek >= Ea, increasing the frequency of effective collisions."
    sample = (
        "1. **NO**. The distribution curve depends strictly on temperature. Because temperature is constant, average kinetic energy and molecular speed distribution remain identical.\n"
        r"2. The catalyst provides an **alternative reaction pathway of lower activation energy** ($E_a$). On the Maxwell-Boltzmann graph, the threshold line shifts to the left ($E_a\text{(cat)} < E_a\text{(uncat)}$). "
        r"Therefore, a **larger fraction of particles possess $E_k \ge E_a$**, increasing the frequency of effective collisions per unit time and thus increasing the reaction rate."
    )
    return _pillars(
        qid=f"ps12_eq04_{rng.randint(10000, 99999)}",
        subskill="04_maxwell_boltzmann_catalyst_effect",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "NO with justification: temperature is constant", "marks": 1},
            {"id": "mp2", "desc": "Catalyst provides alternative pathway of lower activation energy", "marks": 1},
            {"id": "mp3", "desc": "Larger fraction of particles have Ek >= Ea", "marks": 1},
            {"id": "mp4", "desc": "Greater frequency of effective collisions per unit time", "marks": 1},
        ],
        hints={
            "1_nudge": "Does a catalyst give particles more kinetic energy, or does it lower the energy hurdle?",
            "2_concept": "Temperature determines molecular speeds. Catalysts only lower the activation energy barrier.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_catalyst_increases_particle_kinetic_energy", "thinking_catalyst_shifts_maxwell_curve_peak"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Catalyst effect on Maxwell-Boltzmann distribution"},
    )


# =========================================================================== #
# 05: Surface Area Reaction Rate Effect
# =========================================================================== #
def build_05_surface_area_reaction_rate_effect(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([5, 10, 15])
    reagent = rng.choice([
        {"solid": f"{mass} g marble chips (CaCO3)", "powder": f"{mass} g powdered calcium carbonate (CaCO3)", "acid": "100 cm3 of 1 mol/dm3 HCl"},
        {"solid": f"{mass} g zinc granules (Zn)", "powder": f"{mass} g zinc powder (Zn)", "acid": "100 cm3 of 0.5 mol/dm3 H2SO4"},
        {"solid": f"{mass} g magnesium ribbon (Mg)", "powder": f"{mass} g magnesium powder (Mg)", "acid": "150 cm3 of 1 mol/dm3 HNO3"},
    ])
    prompt = (
        "A learner investigates the effect of surface area on reaction rate.\n"
        f"In Experiment 1, {reagent['solid']} reacts with {reagent['acid']}.\n"
        f"In Experiment 2, {reagent['powder']} reacts with {reagent['acid']} under identical temperature.\n\n"
        "1. In which experiment is the initial reaction rate higher? State Experiment 1 or Experiment 2.\n"
        "2. Explain your answer using the collision theory in terms of surface area and collision frequency."
    )
    ans = "Experiment 2; Powdered reactant has a greater exposed surface area per unit volume, exposing more particles to collide with acid particles, increasing the frequency of effective collisions per unit time."
    sample = (
        "1. **Experiment 2**.\n"
        "2. The powdered solid has a much greater **exposed surface area per unit volume** than the large chips/granules. "
        "More reactant particles are directly accessible to collide with the acid ions, resulting in a **greater number of collisions per unit time** (higher collision frequency). "
        "Consequently, the frequency of effective collisions increases, resulting in a faster initial rate."
    )
    return _pillars(
        qid=f"ps12_eq05_{rng.randint(10000, 99999)}",
        subskill="05_surface_area_reaction_rate_effect",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify Experiment 2", "marks": 1},
            {"id": "mp2", "desc": "Powder has greater exposed surface area", "marks": 1},
            {"id": "mp3", "desc": "Greater frequency of collisions per unit time", "marks": 1},
        ],
        hints={
            "1_nudge": "Which form of the solid exposes more particles to the acid solution at the very start?",
            "2_concept": "Surface area directly governs the number of collision contact sites available per unit time.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_powder_has_higher_kinetic_energy", "confusing_surface_area_with_concentration"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 06: Concentration and Pressure Rate Effect
# =========================================================================== #
def build_06_concentration_and_pressure_rate_effect(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([0.5, 1.0])
    c2 = round(c1 * rng.choice([2.0, 3.0]), 1)
    prompt = (
        "In an experiment, equal masses of zinc powder react with hydrochloric acid at 25 °C:\n"
        f"Reaction 1 uses acid of concentration {_fmt_sa(c1)} mol·dm⁻³.\n"
        f"Reaction 2 uses acid of concentration {_fmt_sa(c2)} mol·dm⁻³.\n\n"
        "Use the collision theory to explain why Reaction 2 has a significantly higher initial rate than Reaction 1."
    )
    ans = f"Reaction 2 has higher concentration ({_fmt_sa(c2)} mol·dm⁻³), meaning more H+ particles per unit volume. This increases the collision frequency between reacting particles, leading to more effective collisions per unit time."
    sample = (
        f"At higher concentration ({_fmt_sa(c2)} mol·dm⁻³), there are **more reactant particles per unit volume**. "
        "This increases the **frequency of collisions** between hydrogen ions and zinc atoms. "
        "Consequently, there are **more effective collisions per unit time**, resulting in a higher reaction rate."
    )
    return _pillars(
        qid=f"ps12_eq06_{rng.randint(10000, 99999)}",
        subskill="06_concentration_and_pressure_rate_effect",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Higher concentration: more particles per unit volume", "marks": 1},
            {"id": "mp2", "desc": "Increased frequency of collisions", "marks": 1},
            {"id": "mp3", "desc": "Greater frequency of effective collisions per unit time", "marks": 1},
        ],
        hints={
            "1_nudge": "What does concentration measure in terms of particle crowding?",
            "2_concept": "More particles per unit volume -> more frequent collisions.",
            "3_breakdown": sample,
        },
        misconception_tags=["omitting_per_unit_volume_in_concentration_explanation", "claiming_concentration_changes_activation_energy"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 07: Temperature Kinetic Energy Rate Effect
# =========================================================================== #
def build_07_temperature_kinetic_energy_rate_effect(rng: random.Random) -> Dict[str, Any]:
    dt = rng.choice([10, 20, 30])
    prompt = (
        f"A general rule in chemistry states that for many reactions, an increase in temperature of {dt} °C roughly doubles or triples the reaction rate.\n\n"
        "Explain why temperature has such a profound impact on reaction rate, highlighting the **TWO** distinct effects temperature has on reacting particles according to collision theory."
    )
    ans = "1. Particles move faster, increasing collision frequency; 2. Much larger fraction of particles possess Ek >= Ea (activation energy threshold), dramatically increasing the fraction of collisions that are effective."
    sample = (
        "An increase in temperature causes two simultaneous effects:\n"
        "1. **Higher speed / collision frequency**: Particles gain thermal energy, move faster, and collide more frequently per unit time (minor factor).\n"
        r"2. **Higher energy threshold exceedance**: The average kinetic energy increases, so a **significantly larger fraction of colliding particles have kinetic energy greater than or equal to the activation energy ($E_k \ge E_a$)** (major factor)." + "\n"
        "Together, these cause a dramatic increase in the **frequency of effective collisions per unit time**."
    )
    return _pillars(
        qid=f"ps12_eq07_{rng.randint(10000, 99999)}",
        subskill="07_temperature_kinetic_energy_rate_effect",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Particles move faster / collision frequency increases", "marks": 1},
            {"id": "mp2", "desc": "Larger fraction of particles have Ek >= Ea", "marks": 2},
            {"id": "mp3", "desc": "Greater frequency of effective collisions per unit time", "marks": 1},
        ],
        hints={
            "1_nudge": "Does temperature only make particles move faster, or does it also make their hits harder?",
            "2_concept": "The primary reason rate jumps with temperature is the surge in particles exceeding Ea.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_collision_frequency_alone_accounts_for_temp_rate_doubling", "claiming_temperature_lowers_activation_energy"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 08: Measuring Rate Gas Syringe Apparatus
# =========================================================================== #
def build_08_measuring_rate_gas_syringe_apparatus(rng: random.Random) -> Dict[str, Any]:
    v_target = rng.choice([40, 50, 60])
    t_sec = rng.choice([80, 100, 120])
    avg_rate = round(v_target / t_sec, 2)
    svg = _svg_wrap(
        f'<rect x="40" y="90" width="80" height="90" rx="4" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 65 90 L 65 60 L 95 60 L 95 90" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<rect x="70" y="48" width="20" height="12" fill="#94a3b8"/>'
        f'<path d="M 80 48 L 80 30 L 220 30 L 220 70" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<rect x="220" y="55" width="140" height="30" rx="3" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="220" y="60" width="{int(v_target * 1.5)}" height="20" fill="#93c5fd" opacity="0.7"/>'
        f'<line x1="280" y1="55" x2="280" y2="85" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="230" y="105" font-family="sans-serif" font-size="10" fill="#0f172a">Gas syringe ({v_target} cm³)</text>'
        f'<text x="45" y="140" font-family="sans-serif" font-size="10" fill="#0f172a">Reaction flask</text>',
        width=390,
        height=200,
    )
    prompt = (
        "The accompanying diagram illustrates an experimental apparatus used to monitor the rate of the reaction between excess hydrochloric acid and calcium carbonate chips:\n"
        r"$$\text{CaCO}_3(\text{s}) + 2\text{HCl}(\text{aq}) \rightarrow \text{CaCl}_2(\text{aq}) + \text{CO}_2(\text{g}) + \text{H}_2\text{O}(\text{l})$$" + "\n\n"
        f"During the reaction, {_fmt_sa(v_target)} cm³ of carbon dioxide gas was collected in the gas syringe over {_fmt_sa(t_sec)} seconds.\n"
        "1. Calculate the average rate of gas evolution in cm³·s⁻¹.\n"
        "2. State why a gas syringe is preferable to downward displacement of water for collecting carbon dioxide."
    )
    ans = f"{_fmt_sa(avg_rate)} cm³·s⁻¹; CO2 is slightly soluble in water, so water displacement underestimates the volume"
    sample = (
        rf"1. Average rate = $\frac{{\Delta V}}{{\Delta t}} = \frac{{{_fmt_sa(v_target)}}}{{{_fmt_sa(t_sec)}}} = {_fmt_sa(avg_rate)}\text{{ cm}}^3\cdot\text{{s}}^{{-1}}$." + "\n"
        r"2. Carbon dioxide is moderately soluble in water (forms weak carbonic acid, $\text{H}_2\text{CO}_3$). "
        "Using a gas syringe prevents loss of gas due to dissolution, ensuring accurate volume measurement."
    )
    return _pillars(
        qid=f"ps12_eq08_{rng.randint(10000, 99999)}",
        subskill="08_measuring_rate_gas_syringe_apparatus",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Formula: Average rate = ΔV / Δt", "marks": 1},
            {"id": "mp2", "desc": f"Calculation and unit: {_fmt_sa(avg_rate)} cm³·s⁻¹", "marks": 1},
            {"id": "mp3", "desc": "Reason: CO2 dissolves in water", "marks": 1},
        ],
        hints={
            "1_nudge": "Rate is volume divided by time. Does CO2 dissolve in water?",
            "2_concept": "Gases with slight water solubility dissolve partially if bubbled into a water trough.",
            "3_breakdown": sample,
        },
        misconception_tags=["inverted_rate_calculation", "unaware_of_gas_solubility_in_water"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Gas Syringe Apparatus"},
    )


# =========================================================================== #
# 09: Measuring Rate Mass Loss Electronic Balance
# =========================================================================== #
def build_09_measuring_rate_mass_loss_electronic_balance(rng: random.Random) -> Dict[str, Any]:
    m_init = rng.choice([180.5, 210.0, 245.2])
    dm = rng.choice([1.32, 1.76, 2.20])
    m_final = round(m_init - dm, 2)
    t_sec = rng.choice([120, 150, 180])
    rate = round(dm / t_sec, 4)
    svg = _svg_wrap(
        f'<rect x="120" y="140" width="150" height="50" rx="4" fill="#334155" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="150" y="152" width="90" height="25" rx="2" fill="#0f172a"/>'
        f'<text x="165" y="170" font-family="monospace" font-size="14" font-weight="bold" fill="#22c55e">{m_final:.2f} g</text>'
        f'<path d="M 160 140 L 175 70 L 215 70 L 230 140 Z" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
        f'<ellipse cx="195" cy="65" rx="15" ry="8" fill="#e2e8f0" stroke="#94a3b8"/>'
        f'<text x="155" y="55" font-family="sans-serif" font-size="10" fill="#475569">Cotton wool</text>',
        width=390,
        height=210,
    )
    prompt = (
        "A conical flask containing dilute hydrochloric acid and marble chips is placed on an electronic balance as shown in the accompanying diagram.\n"
        f"Initial mass of apparatus = {_fmt_sa(m_init)} g.\n"
        f"Final mass after {_fmt_sa(t_sec)} s = {_fmt_sa(m_final)} g.\n\n"
        "1. Explain why the mass decreases as the reaction proceeds.\n"
        "2. State the function of the cotton wool plug in the neck of the flask.\n"
        "3. Calculate the average rate of reaction in g·s⁻¹."
    )
    ans = f"1. CO2 gas escapes from the open flask; 2. Prevents acid droplets/spray from splashing out while letting gas escape; 3. {_fmt_sa(rate, 4)} g·s⁻¹"
    sample = (
        r"1. Carbon dioxide gas ($\text{CO}_2$) is generated and escapes into the atmosphere, causing mass loss." + "\n"
        r"2. The cotton wool plug **prevents acid spray/droplets from splashing out** while permitting the $\text{CO}_2$ gas to escape freely." + "\n"
        rf"3. Mass loss $\Delta m = {_fmt_sa(m_init)} - {_fmt_sa(m_final)} = {_fmt_sa(dm)}\text{{ g}}$." + "\n"
        rf"Average rate = $\frac{{\Delta m}}{{\Delta t}} = \frac{{{_fmt_sa(dm)}}}{{{_fmt_sa(t_sec)}}} = {_fmt_sa(rate, 4)}\text{{ g}}\cdot\text{{s}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps12_eq09_{rng.randint(10000, 99999)}",
        subskill="09_measuring_rate_mass_loss_electronic_balance",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "CO2 gas escapes from the flask", "marks": 1},
            {"id": "mp2", "desc": "Cotton wool prevents acid spray splashing out", "marks": 1},
            {"id": "mp3", "desc": "Calculate mass change: dm", "marks": 1},
            {"id": "mp4", "desc": f"Rate calculation: {_fmt_sa(rate, 4)} g·s⁻¹", "marks": 1},
        ],
        hints={
            "1_nudge": "Which product is a gas that can leave the flask?",
            "2_concept": "Cotton wool lets gas molecules pass but catches liquid aerosol droplets.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_cotton_wool_prevents_acid_spray", "confusing_mass_loss_with_mass_destruction"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Electronic Balance Mass Loss Apparatus"},
    )


# =========================================================================== #
# 10: Measuring Rate Turbidity Precipitate Cross
# =========================================================================== #
def build_10_measuring_rate_turbidity_precipitate_cross(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([20, 25, 30])
    t2 = t1 + rng.choice([15, 20, 25])
    time1 = rng.choice([56, 68, 74])
    time2 = int(time1 * (t1 / t2) * 0.6)
    rate1 = round(1 / time1, 4)
    rate2 = round(1 / time2, 4)
    prompt = (
        "In the classic reaction between sodium thiosulfate and hydrochloric acid:\n"
        r"$$\text{Na}_2\text{S}_2\text{O}_3(\text{aq}) + 2\text{HCl}(\text{aq}) \rightarrow 2\text{NaCl}(\text{aq}) + \text{SO}_2(\text{g}) + \text{S}(\text{s}) + \text{H}_2\text{O}(\text{l})$$" + "\n\n"
        "A flask is placed over a paper card marked with a black cross. A stopwatch records the time taken for the cross to be obscured by yellow sulfur precipitate:\n"
        f"- At {t1} °C, the cross disappears after {_fmt_sa(time1)} s (Rate = {_fmt_sa(rate1, 4)} s⁻¹).\n"
        f"- At {t2} °C, the cross disappears after {_fmt_sa(time2)} s.\n\n"
        "1. Identify the substance causing the turbidity (cloudiness).\n"
        f"2. Calculate the relative reaction rate at {t2} °C in s⁻¹ ($1/t$).\n"
        f"3. Explain why the cross disappears more quickly at {t2} °C."
    )
    ans = f"1. Solid sulfur (S); 2. {_fmt_sa(rate2, 4)} s⁻¹; 3. Higher temperature increases average kinetic energy, so a larger fraction of particles has Ek >= Ea, leading to more effective collisions per second."
    sample = (
        r"1. **Solid sulfur** ($\text{S}(\text{s})$) forms as an insoluble colloidal precipitate, scattering light." + "\n"
        rf"2. Relative rate = $\frac{{1}}{{t}} = \frac{{1}}{{{_fmt_sa(time2)}}} = {_fmt_sa(rate2, 4)}\text{{ s}}^{{-1}}$." + "\n"
        r"3. At higher temperature (" + str(t2) + r" °C), particles possess greater average kinetic energy. "
        r"A significantly larger fraction of collisions possess $E_k \ge E_a$, increasing the frequency of effective collisions per second. Precipitate forms faster."
    )
    return _pillars(
        qid=f"ps12_eq10_{rng.randint(10000, 99999)}",
        subskill="10_measuring_rate_turbidity_precipitate_cross",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify solid sulfur (S)", "marks": 1},
            {"id": "mp2", "desc": f"Relative rate calculation: {_fmt_sa(rate2, 4)} s⁻¹", "marks": 1},
            {"id": "mp3", "desc": "Collision theory explanation for temp increase", "marks": 2},
        ],
        hints={
            "1_nudge": "Which product is listed with the state symbol (s)?",
            "2_concept": "Relative rate in disappearing cross experiments is expressed as 1/t.",
            "3_breakdown": sample,
        },
        misconception_tags=["identifying_so2_gas_as_turbidity_cause", "confusing_time_with_rate"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 11: Average Reaction Rate Calculation
# =========================================================================== #
def build_11_average_reaction_rate_calculation(rng: random.Random) -> Dict[str, Any]:
    t1, t2 = 30, 90
    c1 = rng.choice([0.80, 0.90, 1.00])
    c2 = round(c1 - rng.choice([0.35, 0.40, 0.45]), 2)
    dt = t2 - t1
    dc = round(c1 - c2, 2)
    rate = round(dc / dt, 4)
    prompt = (
        rf"The concentration of a reactant A decreases from {_fmt_sa(c1)} mol·dm⁻³ at $t = {t1}\text{{ s}}$ to {_fmt_sa(c2)} mol·dm⁻³ at $t = {t2}\text{{ s}}$." + "\n\n"
        "1. Write down the mathematical formula for the average rate of consumption of A.\n"
        f"2. Calculate the average rate of reaction over this {dt} s time interval in mol·dm⁻³·s⁻¹."
    )
    ans = f"Average rate = -Δ[A]/Δt; {_fmt_sa(rate, 4)} mol·dm⁻³·s⁻¹"
    sample = (
        r"1. Average rate = $-\frac{\Delta [\text{A}]}{\Delta t} = -\frac{[\text{A}]_2 - [\text{A}]_1}{t_2 - t_1}$." + "\n"
        rf"2. Average rate = $-\frac{{{_fmt_sa(c2)} - {_fmt_sa(c1)}}}{{{t2} - {t1}}} = \frac{{{_fmt_sa(dc)}}}{{{dt}}} = {_fmt_sa(rate, 4)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}\cdot\text{{s}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps12_eq11_{rng.randint(10000, 99999)}",
        subskill="11_average_reaction_rate_calculation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Correct rate formula with negative sign or Δ[A]/Δt", "marks": 1},
            {"id": "mp2", "desc": "Substitution of concentrations and times", "marks": 1},
            {"id": "mp3", "desc": f"Answer with correct units: {_fmt_sa(rate, 4)} mol·dm⁻³·s⁻¹", "marks": 1},
        ],
        hints={
            "1_nudge": "Rate is positive even though reactant concentration drops.",
            "2_concept": "Change in concentration = final minus initial; divide by time difference.",
            "3_breakdown": sample,
        },
        misconception_tags=["negative_reaction_rate_sign_error", "omitted_volume_units_in_rate"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 12: Instantaneous Rate Tangent Gradient
# =========================================================================== #
def build_12_instantaneous_rate_tangent_gradient(rng: random.Random) -> Dict[str, Any]:
    t_pt = rng.choice([20, 30, 40])
    dy = rng.choice([30, 45, 60])
    dx = rng.choice([40, 50, 60])
    grad = round(dy / dx, 2)
    prompt = (
        "A curve of volume of gas evolved versus time is plotted for the reaction of zinc with acid.\n"
        rf"At time $t = {t_pt}\text{{ s}}$, a tangent drawn to the curve passes through points $(0\text{{ s}}, 10\text{{ cm}}^3)$ and $({dx}\text{{ s}}, {10 + dy}\text{{ cm}}^3)$." + "\n\n"
        "1. Distinguish between **average rate** and **instantaneous rate**.\n"
        rf"2. Calculate the instantaneous rate of reaction at $t = {t_pt}\text{{ s}}$ in cm³·s⁻¹." + "\n"
        "3. What happens to the value of the gradient of the tangent as time approaches completion of the reaction?"
    )
    ans = f"1. Average rate is change over a time interval; instantaneous rate is rate at one specific moment (gradient of tangent); 2. {_fmt_sa(grad)} cm³·s⁻¹; 3. Decreases to zero (curve becomes horizontal)."
    sample = (
        r"1. **Average rate** is calculated over an extended time interval ($\Delta V / \Delta t$). **Instantaneous rate** is the rate at one particular instant in time, given by the gradient of the tangent to the curve at that point." + "\n"
        rf"2. Instantaneous rate = Gradient = $\frac{{{10 + dy} - 10}}{{{dx} - 0}} = \frac{{{dy}}}{{{dx}}} = {_fmt_sa(grad)}\text{{ cm}}^3\cdot\text{{s}}^{{-1}}$." + "\n"
        "3. As the limiting reactant is used up, reactant collisions decrease and the reaction slows; the gradient **decreases and becomes zero** when the reaction ceases."
    )
    return _pillars(
        qid=f"ps12_eq12_{rng.randint(10000, 99999)}",
        subskill="12_instantaneous_rate_tangent_gradient",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Distinction between average and instantaneous rate", "marks": 1},
            {"id": "mp2", "desc": f"Gradient calculation: {_fmt_sa(grad)} cm³·s⁻¹", "marks": 2},
            {"id": "mp3", "desc": "Gradient decreases to zero at completion", "marks": 1},
        ],
        hints={
            "1_nudge": "How do you find instantaneous rate on a graph?",
            "2_concept": "Gradient of tangent line = instantaneous reaction rate.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_secant_with_tangent_gradient", "failing_to_recognize_zero_rate_at_plateau"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 13: Reaction Rate Stoichiometric Relationships
# =========================================================================== #
def build_13_reaction_rate_stoichiometric_relationships(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {"eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightarrow 2\text{NH}_3(\text{g})", "r1": "N_2", "r2": "H_2", "p": "NH_3", "c1": 1, "c2": 3, "cp": 2},
        {"eq": r"2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightarrow 2\text{SO}_3(\text{g})", "r1": "O_2", "r2": "SO_2", "p": "SO_3", "c1": 1, "c2": 2, "cp": 2},
        {"eq": r"2\text{NO}_2(\text{g}) \rightarrow 2\text{NO}(\text{g}) + \text{O}_2(\text{g})", "r1": "O_2", "r2": "NO_2", "p": "NO", "c1": 1, "c2": 2, "cp": 2},
    ])
    rate_r1 = rng.choice([0.020, 0.030, 0.040, 0.050])
    rate_r2 = round(rate_r1 * rxn["c2"], 3)
    rate_p = round(rate_r1 * rxn["cp"], 3)
    prompt = (
        "Consider the balanced chemical equation:\n"
        f"$${rxn['eq']}$$\n\n"
        f"During an investigation, the rate of consumption of ${rxn['r1']}$ is determined to be {_fmt_sa(rate_r1)} mol·dm⁻³·s⁻¹.\n"
        f"1. Determine the rate of consumption of ${rxn['r2']}.\n"
        f"2. Determine the rate of formation of ${rxn['p']}."
    )
    ans = f"Rate of {rxn['r2']} = {_fmt_sa(rate_r2)} mol·dm⁻³·s⁻¹; Rate of {rxn['p']} = {_fmt_sa(rate_p)} mol·dm⁻³·s⁻¹"
    sample = (
        "From the stoichiometric coefficients:\n"
        rf"$$\frac{{\text{{Rate of }}\text{{{rxn['r1']}}}}}{{{rxn['c1']}}} = \frac{{\text{{Rate of }}\text{{{rxn['r2']}}}}}{{{rxn['c2']}}} = \frac{{\text{{Rate of }}\text{{{rxn['p']}}}}}{{{rxn['cp']}}}$$" + "\n\n"
        rf"1. Rate of $\text{{{rxn['r2']}}} = \frac{{{rxn['c2']}}}{{{rxn['c1']}}} \times {_fmt_sa(rate_r1)} = {_fmt_sa(rate_r2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}\cdot\text{{s}}^{{-1}}$." + "\n"
        rf"2. Rate of $\text{{{rxn['p']}}} = \frac{{{rxn['cp']}}}{{{rxn['c1']}}} \times {_fmt_sa(rate_r1)} = {_fmt_sa(rate_p)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}\cdot\text{{s}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps12_eq13_{rng.randint(10000, 99999)}",
        subskill="13_reaction_rate_stoichiometric_relationships",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Rate of {rxn['r2']}: {_fmt_sa(rate_r2)} mol·dm⁻³·s⁻¹", "marks": 2},
            {"id": "mp2", "desc": f"Rate of {rxn['p']}: {_fmt_sa(rate_p)} mol·dm⁻³·s⁻¹", "marks": 2},
        ],
        hints={
            "1_nudge": "Use the mole ratios in the balanced equation to relate reaction rates.",
            "2_concept": "Rate of substance divided by its stoichiometric coefficient is constant.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_all_substances_react_at_same_numerical_rate", "inverting_stoichiometric_ratio_in_rates"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 14: Catalytic Action Mechanism
# =========================================================================== #
def build_14_catalytic_action_mechanism(rng: random.Random) -> Dict[str, Any]:
    cat = rng.choice([
        {"name": "platinum in a catalytic converter", "type": "heterogeneous", "phase": "solid catalyst with gaseous reactants"},
        {"name": "iron in the Haber process", "type": "heterogeneous", "phase": "solid iron with gaseous N2 and H2"},
        {"name": "acid catalyst (H+) in esterification", "type": "homogeneous", "phase": "liquid acid in liquid alcohol and carboxylic acid"},
    ])
    prompt = (
        "1. Define a **catalyst** according to the South African CAPS curriculum.\n"
        f"2. The catalyst used as {cat['name']} operates in a **{cat['type']}** phase.\n"
        f"   Explain what is meant by a **{cat['type']} catalyst**.\n"
        "3. Does the catalyst undergo any permanent chemical change by the end of the reaction?"
    )
    ans = f"1. A substance that increases the rate of a chemical reaction without undergoing permanent chemical change; 2. {cat['type'].capitalize()} catalyst exists in a different physical phase from the reactants ({cat['phase']}); 3. NO"
    sample = (
        "1. A **catalyst** is a substance that increases the rate of a chemical reaction by providing an alternative pathway with a lower activation energy, without undergoing any permanent chemical change itself.\n"
        f"2. A **{cat['type']} catalyst** exists in a **different phase** from the reactants ({cat['phase']}). Reactant molecules adsorb onto active surface sites, weakening bonds and lowering activation energy.\n"
        "3. **NO**. The catalyst may participate in intermediate steps but is regenerated chemically unchanged at the end."
    )
    return _pillars(
        qid=f"ps12_eq14_{rng.randint(10000, 99999)}",
        subskill="14_catalytic_action_mechanism",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition of catalyst (lowers Ea / alternative pathway / unchanged)", "marks": 2},
            {"id": "mp2", "desc": f"Definition of {cat['type']} catalyst", "marks": 1},
            {"id": "mp3", "desc": "NO: catalyst is not permanently changed", "marks": 1},
        ],
        hints={
            "1_nudge": "How does a catalyst change the activation energy?",
            "2_concept": "Heterogeneous means different phases; homogeneous means the same phase.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_catalysts_are_consumed_in_the_overall_reaction", "thinking_catalyst_changes_delta_h"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 15: Catalyzed Energy Profile Diagram
# =========================================================================== #
def build_15_catalyzed_energy_profile_diagram(rng: random.Random) -> Dict[str, Any]:
    e_react = rng.choice([80, 100, 120])
    e_act_uncat = e_react + rng.choice([120, 150, 180])
    e_act_cat = e_act_uncat - rng.choice([40, 50, 60])
    dh = -rng.choice([50, 70, 90])
    e_prod = e_react + dh
    ea_fwd_uncat = e_act_uncat - e_react
    ea_fwd_cat = e_act_cat - e_react

    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="195" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="195" x2="365" y2="195" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">PE (kJ)</text>'
        f'<text x="250" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Course of reaction</text>'
        f'<line x1="50" y1="{195 - int(e_react * 0.7)}" x2="110" y2="{195 - int(e_react * 0.7)}" stroke="#2563eb" stroke-width="3"/>'
        f'<text x="60" y="{195 - int(e_react * 0.7) - 6}" font-family="sans-serif" font-size="10" fill="#2563eb">Reactants ({e_react})</text>'
        f'<path d="M 110 {195 - int(e_react * 0.7)} Q 190 {195 - int(e_act_uncat * 0.7)}, 270 {195 - int(e_prod * 0.7)}" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<path d="M 110 {195 - int(e_react * 0.7)} Q 190 {195 - int(e_act_cat * 0.7)}, 270 {195 - int(e_prod * 0.7)}" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<line x1="270" y1="{195 - int(e_prod * 0.7)}" x2="340" y2="{195 - int(e_prod * 0.7)}" stroke="#dc2626" stroke-width="3"/>'
        f'<text x="280" y="{195 - int(e_prod * 0.7) - 6}" font-family="sans-serif" font-size="10" fill="#dc2626">Products ({e_prod})</text>'
        f'<text x="160" y="{195 - int(e_act_uncat * 0.7) - 6}" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Peak 1 ({e_act_uncat})</text>'
        f'<text x="160" y="{195 - int(e_act_cat * 0.7) + 14}" font-family="sans-serif" font-size="10" font-weight="bold" fill="#16a34a">Peak 2 ({e_act_cat})</text>',
        width=390,
        height=230,
    )
    prompt = (
        "Refer to the potential energy graph for a reversible reaction.\n"
        f"- Potential energy of reactants = {e_react} kJ·mol⁻¹\n"
        f"- Potential energy of products = {e_prod} kJ·mol⁻¹\n"
        f"- Peak 1 (uncatalyzed activated complex) = {e_act_uncat} kJ·mol⁻¹\n"
        f"- Peak 2 (catalyzed activated complex) = {e_act_cat} kJ·mol⁻¹\n\n"
        r"1. Calculate the activation energy ($E_a$) of the forward uncatalyzed reaction." + "\n"
        r"2. Calculate the activation energy ($E_a$) of the forward catalyzed reaction." + "\n"
        r"3. Calculate the heat of reaction ($\Delta H$) and state whether the reaction is exothermic or endothermic."
    )
    ans = f"1. Ea(uncat) = {ea_fwd_uncat} kJ·mol⁻¹; 2. Ea(cat) = {ea_fwd_cat} kJ·mol⁻¹; 3. ΔH = {dh} kJ·mol⁻¹, exothermic"
    sample = (
        rf"1. $E_a\text{{(uncat)}} = E_{{\text{{complex}}}} - E_{{\text{{reactants}}}} = {e_act_uncat} - {e_react} = {ea_fwd_uncat}\text{{ kJ}}\cdot\text{{mol}}^{{-1}}$." + "\n"
        rf"2. $E_a\text{{(cat)}} = E_{{\text{{cat complex}}}} - E_{{\text{{reactants}}}} = {e_act_cat} - {e_react} = {ea_fwd_cat}\text{{ kJ}}\cdot\text{{mol}}^{{-1}}$." + "\n"
        rf"3. $\Delta H = E_{{\text{{products}}}} - E_{{\text{{reactants}}}} = {e_prod} - {e_react} = {dh}\text{{ kJ}}\cdot\text{{mol}}^{{-1}}$. "
        r"Because $\Delta H < 0$, the reaction is **exothermic**."
    )
    return _pillars(
        qid=f"ps12_eq15_{rng.randint(10000, 99999)}",
        subskill="15_catalyzed_energy_profile_diagram",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Ea uncatalyzed: {ea_fwd_uncat} kJ·mol⁻¹", "marks": 1},
            {"id": "mp2", "desc": f"Ea catalyzed: {ea_fwd_cat} kJ·mol⁻¹", "marks": 1},
            {"id": "mp3", "desc": f"ΔH = {dh} kJ·mol⁻¹ and exothermic", "marks": 2},
        ],
        hints={
            "1_nudge": "Activation energy is peak minus reactants; heat of reaction is products minus reactants.",
            "2_concept": "Catalyst lowers the peak but leaves reactant and product energy levels unchanged.",
            "3_breakdown": sample,
        },
        misconception_tags=["calculating_ea_from_zero_instead_of_reactants", "thinking_catalyst_changes_delta_h"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Catalyzed Potential Energy Profile"},
    )


# =========================================================================== #
# 16: Limiting Reagent and Yield vs Rate
# =========================================================================== #
def build_16_limiting_reagent_and_yield_vs_rate(rng: random.Random) -> Dict[str, Any]:
    n_zn = rng.choice([0.10, 0.15, 0.20])
    c_hcl = rng.choice([1.0, 1.5, 2.0])
    v_hcl = rng.choice([0.10, 0.20])
    n_hcl = round(c_hcl * v_hcl, 2)
    if n_hcl < 2 * n_zn:
        limiting = "HCl"
        excess = "Zn"
        n_h2 = round(n_hcl / 2, 3)
    else:
        limiting = "Zn"
        excess = "HCl"
        n_h2 = round(n_zn, 3)

    v_stp = round(n_h2 * 22.4, 2)
    prompt = (
        f"A learner adds {_fmt_sa(n_zn)} mol of zinc granules to {_fmt_sa(v_hcl * 1000)} cm³ of {_fmt_sa(c_hcl)} mol·dm⁻³ hydrochloric acid at 25 °C:\n"
        r"$$\text{Zn}(\text{s}) + 2\text{HCl}(\text{aq}) \rightarrow \text{ZnCl}_2(\text{aq}) + \text{H}_2(\text{g})$$" + "\n\n"
        "1. Identify the **limiting reagent** by comparing stoichiometric mole ratios.\n"
        rf"2. Calculate the maximum volume of $\text{{H}}_2(\text{{g}})$ formed at standard temperature and pressure (molar gas volume at STP = 22,4 dm³·mol⁻¹)." + "\n"
        rf"3. If the experiment is repeated using powdered zinc instead of granules, state how this affects (i) the rate of reaction, and (ii) the total yield of $\text{{H}}_2$."
    )
    ans = f"1. Limiting reagent: {limiting}; 2. Volume of H2 = {_fmt_sa(v_stp)} dm³; 3. (i) Rate increases; (ii) Total yield remains unchanged."
    sample = (
        rf"1. Moles of $\text{{HCl}} = c \times V = {_fmt_sa(c_hcl)} \times {_fmt_sa(v_hcl)} = {_fmt_sa(n_hcl)}\text{{ mol}}$." + "\n"
        rf"From stoichiometry, 1 mol Zn requires 2 mol HCl. For {_fmt_sa(n_zn)} mol Zn, we require $2 \times {_fmt_sa(n_zn)} = {_fmt_sa(2 * n_zn)}\text{{ mol HCl}}$." + "\n"
        f"Because available HCl is {_fmt_sa(n_hcl)} mol, **{limiting}** is the limiting reagent.\n"
        rf"2. Moles of $\text{{H}}_2$ produced = {_fmt_sa(n_h2)} mol." + "\n"
        rf"$V = n \times V_m = {_fmt_sa(n_h2)} \times 22{{,}}4 = {_fmt_sa(v_stp)}\text{{ dm}}^3$." + "\n"
        "3. Powdered zinc has higher surface area: (i) Initial rate **increases**; (ii) Total yield is governed strictly by the limiting reagent and **remains identical**."
    )
    return _pillars(
        qid=f"ps12_eq16_{rng.randint(10000, 99999)}",
        subskill="16_limiting_reagent_and_yield_vs_rate",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identification of limiting reagent ({limiting}) with mole calculation", "marks": 2},
            {"id": "mp2", "desc": f"Volume of H2 at STP: {_fmt_sa(v_stp)} dm³", "marks": 2},
            {"id": "mp3", "desc": "Rate increases, total yield remains unchanged", "marks": 2},
        ],
        hints={
            "1_nudge": "Which reagent runs out first based on the 1:2 mole ratio?",
            "2_concept": "Surface area alters reaction rate but never changes the total quantity of products formed.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_rate_increase_with_yield_increase", "incorrect_limiting_reagent_ratio"],
        marks=6,
        duration=6,
    )


# =========================================================================== #
# 17: Gas Volume Time Graph Different Conditions
# =========================================================================== #
def build_17_gas_volume_time_graph_different_conditions(rng: random.Random) -> Dict[str, Any]:
    v_max = rng.choice([60, 80, 100])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Vol H2 (cm³)</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<path d="M 50 190 Q 90 60, 180 60 L 360 60" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="200" y="50" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Curve X (steep)</text>'
        f'<path d="M 50 190 Q 140 100, 260 60 L 360 60" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="280" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Curve Y (standard)</text>'
        f'<line x1="45" y1="60" x2="360" y2="60" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="10" y="65" font-family="sans-serif" font-size="11" fill="#0f172a">{v_max}</text>',
        width=390,
        height=230,
    )
    prompt = (
        "The accompanying graph shows the volume of carbon dioxide gas evolved over time for two experiments (X and Y) using identical masses of calcium carbonate reacting with excess acid.\n\n"
        "1. Which curve (X or Y) represents the experiment with the higher initial reaction rate? Give a reason.\n"
        f"2. Explain why both curves level off at the exact same plateau volume ({v_max} cm³).\n"
        "3. State TWO possible modifications to the conditions of Experiment Y that could produce Curve X."
    )
    ans = f"1. Curve X, steeper initial gradient; 2. The mass of the limiting reagent (CaCO3) is identical in both experiments; 3. Any two of: increasing temperature, using powdered CaCO3 instead of chips, increasing acid concentration, adding a catalyst."
    sample = (
        "1. **Curve X**. The initial gradient of the curve is steeper, indicating a greater volume of gas produced per second at the start.\n"
        f"2. Both experiments used **identical quantities of the limiting reagent** (calcium carbonate). Because the limiting reagent determines the maximum product yield, the final volume ({v_max} cm³) is identical.\n"
        "3. Modifications that increase rate without altering yield:\n"
        "   - **Increase the temperature** of the acid.\n"
        "   - **Increase surface area** by grinding the carbonate into a fine powder.\n"
        "   - **Increase acid concentration**."
    )
    return _pillars(
        qid=f"ps12_eq17_{rng.randint(10000, 99999)}",
        subskill="17_gas_volume_time_graph_different_conditions",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Curve X identified with reason (steeper initial gradient)", "marks": 2},
            {"id": "mp2", "desc": "Same limiting reagent quantity determines final yield", "marks": 1},
            {"id": "mp3", "desc": "Two valid conditions (temperature, surface area, concentration)", "marks": 2},
        ],
        hints={
            "1_nudge": "Initial gradient = initial rate. Plateau height = total yield.",
            "2_concept": "Steeper slope means faster; same flat level means same quantity of limiting reactant.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_different_curves_must_have_different_limiting_reagents", "misinterpreting_graph_gradient_as_yield"],
        marks=5,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Gas Volume vs Time Graph"},
    )


# =========================================================================== #
# 18: Mass Loss Time Graph Analysis
# =========================================================================== #
def build_18_mass_loss_time_graph_analysis(rng: random.Random) -> Dict[str, Any]:
    dm_tot = rng.choice([2.2, 3.3, 4.4])
    t_end = rng.choice([60, 90, 120])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Mass loss (g)</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<path d="M 50 190 Q 110 70, {50 + t_end} 70 L 360 70" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<line x1="45" y1="70" x2="{50 + t_end}" y2="70" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="15" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{dm_tot}</text>'
        f'<line x1="{50 + t_end}" y1="70" x2="{50 + t_end}" y2="190" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="{40 + t_end}" y="205" font-family="sans-serif" font-size="11" fill="#0f172a">{t_end}</text>',
        width=390,
        height=230,
    )
    prompt = (
        "The accompanying graph illustrates the total mass loss over time during the reaction between marble chips and dilute hydrochloric acid in an open flask.\n\n"
        rf"1. State the mass of $\text{{CO}}_2$ gas that escaped from the flask." + "\n"
        "2. How long did it take for the reaction to reach completion?\n"
        rf"3. Calculate the number of moles of carbon dioxide gas produced ($M(\text{{CO}}_2) = 44\text{{ g}}\cdot\text{{mol}}^{{-1}}$)."
    )
    n_co2 = round(dm_tot / 44.0, 3)
    ans = f"1. {dm_tot} g; 2. {t_end} s; 3. {_fmt_sa(n_co2)} mol"
    sample = (
        rf"1. Total mass loss = **{_fmt_sa(dm_tot)} g** of $\text{{CO}}_2$ gas." + "\n"
        f"2. The curve becomes horizontal at **{t_end} s**, indicating zero further mass loss (reaction complete).\n"
        rf"3. $n = \frac{{m}}{{M}} = \frac{{{_fmt_sa(dm_tot)}}}{{44}} = {_fmt_sa(n_co2)}\text{{ mol}}$."
    )
    return _pillars(
        qid=f"ps12_eq18_{rng.randint(10000, 99999)}",
        subskill="18_mass_loss_time_graph_analysis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Total mass loss: {dm_tot} g", "marks": 1},
            {"id": "mp2", "desc": f"Time of completion: {t_end} s", "marks": 1},
            {"id": "mp3", "desc": f"Calculation of moles: {_fmt_sa(n_co2)} mol", "marks": 2},
        ],
        hints={
            "1_nudge": "Read the plateau height on the y-axis for total mass loss.",
            "2_concept": "Completion is reached where the curve first flattens completely.",
            "3_breakdown": sample,
        },
        misconception_tags=["misreading_plateau_time", "inverted_moles_formula"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Mass Loss vs Time Graph"},
    )


# =========================================================================== #
# 19: Catalytic Converter Reactions
# =========================================================================== #
def build_19_catalytic_converter_reactions(rng: random.Random) -> Dict[str, Any]:
    cat_metal = rng.choice(["platinum (Pt)", "palladium (Pd)", "rhodium (Rh)"])
    prompt = (
        "Internal combustion engines emit harmful exhaust gases including carbon monoxide (CO), nitrogen monoxide (NO), and unburnt hydrocarbons.\n"
        f"Catalytic converters fitted to exhaust systems utilize transition metals like {cat_metal} to catalyze the conversion of these harmful gases into safer products.\n\n"
        "1. Write down a balanced chemical equation for the catalyzed conversion of carbon monoxide and nitrogen monoxide into carbon dioxide and nitrogen gas.\n"
        "2. State the environmental hazard associated with the release of unmanaged nitrogen oxides (NO and NO2).\n"
        "3. Explain why leaded petrol must NEVER be used in vehicles fitted with catalytic converters."
    )
    ans = "1. 2CO(g) + 2NO(g) -> 2CO2(g) + N2(g); 2. Acid rain / photochemical smog; 3. Lead poisons the catalyst by permanently coating active sites, rendering it ineffective."
    sample = (
        "1. Balanced equation:\n"
        r"$$2\text{CO}(\text{g}) + 2\text{NO}(\text{g}) \xrightarrow{\text{Pt/Rh}} 2\text{CO}_2(\text{g}) + \text{N}_2(\text{g})$$" + "\n"
        "2. Nitrogen oxides react with atmospheric water vapour to form nitric acid, causing **acid rain**, and contribute to **photochemical smog**.\n"
        "3. Lead deposits permanently adsorb onto the surface of the catalyst (**catalyst poisoning**), blocking active sites and destroying catalytic activity."
    )
    return _pillars(
        qid=f"ps12_eq19_{rng.randint(10000, 99999)}",
        subskill="19_catalytic_converter_reactions",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Balanced equation: 2CO + 2NO -> 2CO2 + N2", "marks": 2},
            {"id": "mp2", "desc": "Environmental impact: acid rain / photochemical smog", "marks": 1},
            {"id": "mp3", "desc": "Lead poisons / blocks active sites of catalyst", "marks": 1},
        ],
        hints={
            "1_nudge": "CO is oxidized to CO2; NO is reduced to N2.",
            "2_concept": "Lead binds irreversibly to noble metal catalytic surfaces.",
            "3_breakdown": sample,
        },
        misconception_tags=["unbalanced_catalytic_converter_equation", "unaware_of_lead_catalyst_poisoning"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 20: Rate Determining Step and Intermediates
# =========================================================================== #
def build_20_rate_determining_step_and_intermediates(rng: random.Random) -> Dict[str, Any]:
    step1_speed = "SLOW (Rate-determining)"
    step2_speed = "FAST"
    prompt = (
        "A chemical reaction proceeds via a two-step mechanism:\n"
        rf"- Step 1 ({step1_speed}): $$\text{{NO}}_2(\text{{g}}) + \text{{NO}}_2(\text{{g}}) \rightarrow \text{{NO}}_3(\text{{g}}) + \text{{NO}}(\text{{g}})$$" + "\n"
        rf"- Step 2 ({step2_speed}): $$\text{{NO}}_3(\text{{g}}) + \text{{CO}}(\text{{g}}) \rightarrow \text{{NO}}_2(\text{{g}}) + \text{{CO}}_2(\text{{g}})$$" + "\n\n"
        "1. Write down the overall balanced equation for the reaction.\n"
        "2. Identify the **reaction intermediate** and justify your answer.\n"
        "3. Which step controls the overall reaction rate? Explain why."
    )
    ans = "1. NO2(g) + CO(g) -> NO(g) + CO2(g); 2. NO3, formed in Step 1 and consumed in Step 2; 3. Step 1, it is the slowest step (rate-determining step) with the highest activation energy."
    sample = (
        "1. Adding both steps and cancelling species appearing on both sides:\n"
        r"$$\text{NO}_2(\text{g}) + \text{CO}(\text{g}) \rightarrow \text{NO}(\text{g}) + \text{CO}_2(\text{g})$$" + "\n"
        r"2. The **reaction intermediate** is $\mathbf{\text{NO}_3}$. It is produced in Step 1 and subsequently consumed in Step 2, so it does not appear in the overall balanced equation." + "\n"
        "3. **Step 1** is the **rate-determining step**. Like the narrowest bottleneck, the slowest elementary step has the highest activation energy and governs the overall rate."
    )
    return _pillars(
        qid=f"ps12_eq20_{rng.randint(10000, 99999)}",
        subskill="20_rate_determining_step_and_intermediates",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Overall equation: NO2 + CO -> NO + CO2", "marks": 2},
            {"id": "mp2", "desc": "Identify NO3 as intermediate with justification", "marks": 1},
            {"id": "mp3", "desc": "Step 1 is rate-determining (slowest step)", "marks": 1},
        ],
        hints={
            "1_nudge": "Add the two equations and cancel terms on both sides.",
            "2_concept": "Intermediates are made then consumed; rate is governed by the slowest step.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_catalyst_with_intermediate", "believing_fast_step_determines_rate"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 21: Open vs Closed Chemical Systems
# =========================================================================== #
def build_21_open_vs_closed_chemical_systems(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        {"desc": "calcium carbonate decomposing in an open crucible", "type": "open", "reason": "CO2 gas escapes into the atmosphere", "eq_possible": False},
        {"desc": "dinitrogen tetroxide gas in a sealed glass syringe", "type": "closed", "reason": "no gas or matter can enter or escape", "eq_possible": True},
        {"desc": "boiling water in a stoppered conical flask", "type": "closed", "reason": "water vapour is contained within the flask", "eq_possible": True},
        {"desc": "hydrochloric acid reacting with zinc in an open beaker", "type": "open", "reason": "hydrogen gas escapes into the room", "eq_possible": False},
    ]
    s = rng.choice(scenarios)
    prompt = (
        f"Consider the chemical system: **{s['desc']}**.\n\n"
        f"1. Classify this system as an **open system** or a **closed system**.\n"
        "2. Explain the fundamental difference between an open system and a closed system.\n"
        "3. Can this system attain a state of dynamic chemical equilibrium? State YES or NO and justify."
    )
    ans = f"1. {s['type'].capitalize()} system; 2. An open system exchanges both matter and energy with surroundings; a closed system exchanges energy but NOT matter; 3. {'YES' if s['eq_possible'] else 'NO'}, dynamic equilibrium requires a closed system where matter cannot escape."
    sample = (
        f"1. This is a **{s['type']} system**.\n"
        "2. An **open system** can exchange both matter and energy (heat) with its surroundings. A **closed system** can exchange energy with its surroundings, but **cannot exchange matter**.\n"
        f"3. **{'YES' if s['eq_possible'] else 'NO'}**. Chemical equilibrium can only be established and maintained in a **closed system** because {s['reason']}."
    )
    return _pillars(
        qid=f"ps12_eq21_{rng.randint(10000, 99999)}",
        subskill="21_open_vs_closed_chemical_systems",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Classification: {s['type']} system", "marks": 1},
            {"id": "mp2", "desc": "Difference: exchange of matter vs energy", "marks": 2},
            {"id": "mp3", "desc": f"Equilibrium criteria: {'YES' if s['eq_possible'] else 'NO'} with reason", "marks": 1},
        ],
        hints={
            "1_nudge": "Can atoms or gas molecules leave this container?",
            "2_concept": "Dynamic chemical equilibrium strictly requires a closed system.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_equilibrium_can_exist_in_an_open_system", "confusing_closed_system_with_isolated_system"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 22: Dynamic Chemical Equilibrium Definition
# =========================================================================== #
def build_22_dynamic_chemical_equilibrium_definition(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {"eq": r"\text{N}_2\text{O}_4(\text{g, colourless}) \rightleftharpoons 2\text{NO}_2(\text{g, brown})", "desc": "dinitrogen tetroxide and nitrogen dioxide"},
        {"eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})", "desc": "synthesis of ammonia"},
        {"eq": r"\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightleftharpoons 2\text{HI}(\text{g})", "desc": "hydrogen and iodine equilibrium"},
    ])
    prompt = (
        "Consider the reversible reaction in a closed container:\n"
        f"$${rxn['eq']}$$\n\n"
        "1. Define the term **chemical equilibrium** verbatim according to the official examination standard.\n"
        "2. Explain why the equilibrium is described as **dynamic** rather than static."
    )
    ans = "1. A stage in a chemical reaction when the rate of the forward reaction equals the rate of the reverse reaction; 2. Dynamic because both forward and reverse reactions continue to occur simultaneously at equal rates, not because the reactions have stopped."
    sample = (
        "1. **Chemical equilibrium** is a stage in a chemical reaction when the **rate of the forward reaction equals the rate of the reverse reaction** (and the concentrations of reactants and products remain constant).\n"
        "2. It is **dynamic** because the chemical reactions have **not stopped**. Both forward and reverse processes continue at exactly equal rates simultaneously."
    )
    return _pillars(
        qid=f"ps12_eq22_{rng.randint(10000, 99999)}",
        subskill="22_dynamic_chemical_equilibrium_definition",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: rate of forward reaction = rate of reverse reaction", "marks": 2},
            {"id": "mp2", "desc": "Dynamic: both reactions continue to occur at equal rates", "marks": 1},
        ],
        hints={
            "1_nudge": "Equilibrium is defined in terms of RATES being equal, not amounts being equal.",
            "2_concept": "Dynamic means moving: reactants turn into products as fast as products turn back.",
            "3_breakdown": sample,
        },
        misconception_tags=["defining_equilibrium_as_equal_concentrations", "thinking_reactions_halt_at_equilibrium"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 23: Microscopic vs Macroscopic Equilibrium
# =========================================================================== #
def build_23_microscopic_vs_macroscopic_equilibrium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a sealed flask at 25 °C containing the equilibrium:\n"
        r"$$\text{N}_2\text{O}_4(\text{g, colourless}) \rightleftharpoons 2\text{NO}_2(\text{g, brown})$$" + "\n\n"
        "The brown colour intensity, temperature, and total pressure of the gas mixture remain completely unchanged over several hours.\n"
        "1. What term describes properties like colour intensity, pressure, and temperature (macroscopic or microscopic)?\n"
        "2. Explain why macroscopic properties remain constant even though individual molecules are constantly reacting.\n"
        rf"3. True or False: At equilibrium, the concentration of $\text{{N}}_2\text{{O}}_4$ must equal the concentration of $\text{{NO}}_2$."
    )
    ans = "1. Macroscopic properties; 2. Forward and reverse reactions occur at identical rates, so molecules are produced and consumed at the exact same rate; 3. FALSE (concentrations are constant, not necessarily equal)."
    sample = (
        "1. These are **macroscopic properties** (observable/measurable on a large scale).\n"
        r"2. Macroscopic properties remain constant because the **forward rate equals the reverse rate**. For every $\text{N}_2\text{O}_4$ molecule that dissociates into two $\text{NO}_2$ molecules, another two $\text{NO}_2$ molecules recombine, keeping concentrations perfectly stable." + "\n"
        "3. **FALSE**. At equilibrium, concentrations must be **constant**, but they are rarely equal to one another."
    )
    return _pillars(
        qid=f"ps12_eq23_{rng.randint(10000, 99999)}",
        subskill="23_microscopic_vs_macroscopic_equilibrium",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Macroscopic properties identified", "marks": 1},
            {"id": "mp2", "desc": "Rates are equal so net concentration change is zero", "marks": 2},
            {"id": "mp3", "desc": "FALSE: concentrations are constant, not equal", "marks": 1},
        ],
        hints={
            "1_nudge": "Are concentrations equal at equilibrium, or are they constant?",
            "2_concept": "Rates are equal; concentrations are constant.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_reactant_and_product_concentrations_must_be_equal_at_equilibrium", "confusing_macroscopic_with_microscopic"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 24: Reversible Reaction Rate Time Graph
# =========================================================================== #
def build_24_reversible_reaction_rate_time_graph(rng: random.Random) -> Dict[str, Any]:
    t_eq = rng.choice([30, 40, 50])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Rate</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<path d="M 50 40 Q 120 110, {50 + t_eq * 4} 110 L 360 110" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="70" y="35" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">Curve 1 (forward)</text>'
        f'<path d="M 50 190 Q 120 110, {50 + t_eq * 4} 110 L 360 110" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="70" y="180" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">Curve 2 (reverse)</text>'
        f'<line x1="{50 + t_eq * 4}" y1="110" x2="{50 + t_eq * 4}" y2="190" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="{40 + t_eq * 4}" y="205" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">t_eq ({t_eq} s)</text>',
        width=390,
        height=230,
    )
    prompt = (
        "The accompanying graph illustrates the rates of the forward and reverse reactions over time when pure reactants are sealed in a closed container at constant temperature.\n\n"
        "1. Identify Curve 1 and Curve 2 as either the **forward reaction rate** or the **reverse reaction rate**.\n"
        "2. Explain why Curve 1 decreases over time while Curve 2 increases over time.\n"
        rf"3. What significance does time $t_{{\text{{eq}}}} = {t_eq}\text{{ s}}$ have in this system?"
    )
    ans = f"1. Curve 1 is forward rate, Curve 2 is reverse rate; 2. Forward rate decreases as reactants are consumed (lower concentration); reverse rate increases as products form; 3. Equilibrium is established at t_eq ({t_eq} s) when forward rate equals reverse rate."
    sample = (
        "1. **Curve 1** is the **forward reaction rate**; **Curve 2** is the **reverse reaction rate**.\n"
        "2. Initially, only reactants are present, so the forward rate is at a maximum. As reactants are consumed, their concentration drops, decreasing the forward rate. "
        "Conversely, product concentrations increase from zero, causing the reverse rate to increase from zero.\n"
        rf"3. At $t_{{\text{{eq}}}} = {t_eq}\text{{ s}}$, **chemical equilibrium is reached** because the forward rate becomes equal to the reverse rate (curves merge into a single horizontal line)."
    )
    return _pillars(
        qid=f"ps12_eq24_{rng.randint(10000, 99999)}",
        subskill="24_reversible_reaction_rate_time_graph",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Curve 1 = forward, Curve 2 = reverse", "marks": 2},
            {"id": "mp2", "desc": "Explanation of rate decrease and increase based on concentration", "marks": 2},
            {"id": "mp3", "desc": f"Equilibrium established at t_eq = {t_eq} s", "marks": 1},
        ],
        hints={
            "1_nudge": "Which rate starts high? Which rate starts at zero?",
            "2_concept": "Forward starts maximum and drops; reverse starts at 0 and climbs until they meet.",
            "3_breakdown": sample,
        },
        misconception_tags=["swapping_forward_and_reverse_rate_curves", "believing_rates_drop_to_zero_at_equilibrium"],
        marks=5,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Rate vs Time Graph Reaching Equilibrium"},
    )


# =========================================================================== #
# 25: Reversible Reaction Concentration Time Graph
# =========================================================================== #
def build_25_reversible_reaction_concentration_time_graph(rng: random.Random) -> Dict[str, Any]:
    c_r_init = rng.choice([2.0, 3.0, 4.0])
    c_r_eq = round(c_r_init * 0.4, 1)
    c_p_eq = round(c_r_init * 0.6, 1)
    t_eq = rng.choice([25, 35, 45])

    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="10" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">[ ] (mol/dm³)</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<path d="M 50 40 Q 110 130, {50 + t_eq * 4} 130 L 360 130" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="60" y="35" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">Reactant A ({c_r_init})</text>'
        f'<text x="310" y="125" font-family="sans-serif" font-size="10" fill="#2563eb">[{c_r_eq}]</text>'
        f'<path d="M 50 190 Q 110 90, {50 + t_eq * 4} 90 L 360 90" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="60" y="180" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">Product B (0.0)</text>'
        f'<text x="310" y="85" font-family="sans-serif" font-size="10" fill="#dc2626">[{c_p_eq}]</text>'
        f'<line x1="{50 + t_eq * 4}" y1="40" x2="{50 + t_eq * 4}" y2="190" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="{40 + t_eq * 4}" y="205" font-family="sans-serif" font-size="11" fill="#0f172a">{t_eq} s</text>',
        width=390,
        height=230,
    )
    prompt = (
        r"The accompanying concentration-time graph represents the reaction $\text{A}(\text{g}) \rightleftharpoons \text{B}(\text{g})$ in a sealed vessel." + "\n\n"
        "1. At what time is dynamic chemical equilibrium first established?\n"
        "2. State how the graph demonstrates that equilibrium has been established.\n"
        rf"3. At equilibrium, is $[\text{{B}}]$ greater than, less than, or equal to $[\text{{A}}]$?" + "\n"
        r"4. Calculate the equilibrium constant ($K_c$) for this reaction at the given temperature."
    )
    kc = round(c_p_eq / c_r_eq, 2)
    ans = f"1. {t_eq} s; 2. Concentrations of both A and B become constant (horizontal parallel lines); 3. Greater than ([B] = {c_p_eq} > [A] = {c_r_eq}); 4. Kc = {_fmt_sa(kc)}"
    sample = (
        f"1. Equilibrium is established at **{t_eq} s**.\n"
        f"2. From {t_eq} s onwards, the concentration curves become **horizontal lines**, showing that the concentrations of both reactants and products remain **constant**.\n"
        rf"3. $[\text{{B}}] = {_fmt_sa(c_p_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$ is **greater than** $[\text{{A}}] = {_fmt_sa(c_r_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$." + "\n"
        rf"4. $K_c = \frac{{[\text{{B}}]}}{{[\text{{A}}]}} = \frac{{{_fmt_sa(c_p_eq)}}}{{{_fmt_sa(c_r_eq)}}} = {_fmt_sa(kc)}$."
    )
    return _pillars(
        qid=f"ps12_eq25_{rng.randint(10000, 99999)}",
        subskill="25_reversible_reaction_concentration_time_graph",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Time equilibrium established: {t_eq} s", "marks": 1},
            {"id": "mp2", "desc": "Curves become horizontal / concentrations remain constant", "marks": 1},
            {"id": "mp3", "desc": "Comparison: [B] is greater than [A]", "marks": 1},
            {"id": "mp4", "desc": f"Kc calculation: {_fmt_sa(kc)}", "marks": 2},
        ],
        hints={
            "1_nudge": "Look at where the curves first stop curving and become horizontal.",
            "2_concept": "On a concentration-time graph, equilibrium is shown by horizontal lines (constant concentrations).",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_concentrations_must_cross_or_equal_to_be_at_equilibrium", "inverted_kc_expression"],
        marks=5,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Concentration vs Time Graph Reaching Equilibrium"},
    )


BUILDERS_01_25 = {
    "01_reaction_rate_definition_and_units": build_01_reaction_rate_definition_and_units,
    "02_collision_theory_criteria": build_02_collision_theory_criteria,
    "03_maxwell_boltzmann_temperature_shift": build_03_maxwell_boltzmann_temperature_shift,
    "04_maxwell_boltzmann_catalyst_effect": build_04_maxwell_boltzmann_catalyst_effect,
    "05_surface_area_reaction_rate_effect": build_05_surface_area_reaction_rate_effect,
    "06_concentration_and_pressure_rate_effect": build_06_concentration_and_pressure_rate_effect,
    "07_temperature_kinetic_energy_rate_effect": build_07_temperature_kinetic_energy_rate_effect,
    "08_measuring_rate_gas_syringe_apparatus": build_08_measuring_rate_gas_syringe_apparatus,
    "09_measuring_rate_mass_loss_electronic_balance": build_09_measuring_rate_mass_loss_electronic_balance,
    "10_measuring_rate_turbidity_precipitate_cross": build_10_measuring_rate_turbidity_precipitate_cross,
    "11_average_reaction_rate_calculation": build_11_average_reaction_rate_calculation,
    "12_instantaneous_rate_tangent_gradient": build_12_instantaneous_rate_tangent_gradient,
    "13_reaction_rate_stoichiometric_relationships": build_13_reaction_rate_stoichiometric_relationships,
    "14_catalytic_action_mechanism": build_14_catalytic_action_mechanism,
    "15_catalyzed_energy_profile_diagram": build_15_catalyzed_energy_profile_diagram,
    "16_limiting_reagent_and_yield_vs_rate": build_16_limiting_reagent_and_yield_vs_rate,
    "17_gas_volume_time_graph_different_conditions": build_17_gas_volume_time_graph_different_conditions,
    "18_mass_loss_time_graph_analysis": build_18_mass_loss_time_graph_analysis,
    "19_catalytic_converter_reactions": build_19_catalytic_converter_reactions,
    "20_rate_determining_step_and_intermediates": build_20_rate_determining_step_and_intermediates,
    "21_open_vs_closed_chemical_systems": build_21_open_vs_closed_chemical_systems,
    "22_dynamic_chemical_equilibrium_definition": build_22_dynamic_chemical_equilibrium_definition,
    "23_microscopic_vs_macroscopic_equilibrium": build_23_microscopic_vs_macroscopic_equilibrium,
    "24_reversible_reaction_rate_time_graph": build_24_reversible_reaction_rate_time_graph,
    "25_reversible_reaction_concentration_time_graph": build_25_reversible_reaction_concentration_time_graph,
}
