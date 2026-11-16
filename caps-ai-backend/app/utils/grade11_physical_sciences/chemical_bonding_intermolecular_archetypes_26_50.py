"""Grade 11 Physical Sciences — Macroscopic Properties, Water Chemistry & The Lithosphere (Subskills 26–50).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/03. Intermolecular forces.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 4/01. The lithosphere.md

Covers:
- Macroscopic physical properties driven by IMF: boiling points, vapour pressure, viscosity, capillarity, solubility
- Covalent network solids vs molecular solids vs ionic lattices
- Heating & cooling curves (kinetic vs potential energy plateaus)
- Unique chemistry of water: density anomaly of ice, high specific heat capacity, thermal expansion & conductivity
- Earth's concentric layers (crust, mantle, outer/inner core), lithosphere, geosphere, and rock cycle
- South African mineral chemistry (haematite, chalcocite, chalcopyrite, quartz), gold cyanidation, iron blast furnace,
  copper refining, phosphate fertilisers, ore grade stoichiometry, fossil fuels, and diagnostic misconception repair.

Zero-LLM: 100% deterministic Python with seed-varied parameters, South African comma decimals, and inline SVG diagrams.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from app.utils.grade11_physical_sciences.chemical_bonding_intermolecular_archetypes_01_25 import (
    _fmt_sa,
    _pillars,
    _svg_wrap,
)


# =========================================================================== #
# 26: Boiling Point Hydride Anomaly (Inline SVG)
# =========================================================================== #
def build_26_boiling_point_comparison_hydrides_anomaly(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        {"a": "H₂O", "bpa": 100, "b": "H₂S", "bpb": -60, "imf_a": "hydrogen bonding", "imf_b": "dipole-dipole forces"},
        {"a": "HF", "bpa": 20, "b": "HCl", "bpb": -85, "imf_a": "hydrogen bonding", "imf_b": "dipole-dipole forces"},
        {"a": "NH₃", "bpa": -33, "b": "PH₃", "bpb": -88, "imf_a": "hydrogen bonding", "imf_b": "dipole-dipole forces"},
    ]
    p = rng.choice(pairs)
    svg = _svg_wrap(
        f'<line x1="60" y1="30" x2="60" y2="180" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="120" x2="340" y2="120" stroke="#64748b" stroke-dasharray="3,2"/>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">BP (°C)</text>'
        f'<text x="45" y="124" font-family="sans-serif" font-size="10" fill="#64748b">0°</text>'
        f'<rect x="115" y="55" width="45" height="65" fill="#2563eb" opacity="0.85"/>'
        f'<text x="137" y="48" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">{p["bpa"]}°C</text>'
        f'<text x="137" y="195" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{p["a"]}</text>'
        f'<rect x="235" y="120" width="45" height="45" fill="#dc2626" opacity="0.85"/>'
        f'<text x="257" y="180" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#991b1b">{p["bpb"]}°C</text>'
        f'<text x="257" y="195" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{p["b"]}</text>',
        width=360,
        height=210,
    )
    prompt = (
        f"Refer to the boiling point comparison chart for $\\text{{{p['a']}}}$ ({p['bpa']} °C) and $\\text{{{p['b']}}}$ ({p['bpb']} °C).\n\n"
        f"1. Identify the dominant intermolecular force in $\\text{{{p['a']}}}$ and in $\\text{{{p['b']}}}$.\n"
        f"2. Fully explain why $\\text{{{p['a']}}}$ has a significantly higher boiling point than $\\text{{{p['b']}}}$ despite its lower molar mass."
    )
    ans = f"{p['a']}: {p['imf_a']}; {p['b']}: {p['imf_b']}; hydrogen bonds are stronger and require more energy to overcome"
    sample = (
        f"1. $\\text{{{p['a']}}}$ has **{p['imf_a']}** between molecules, whereas $\\text{{{p['b']}}}$ has weaker **{p['imf_b']}**.\n"
        f"2. Hydrogen bonds are significantly stronger than dipole-dipole forces, so far more thermal energy is required to overcome "
        f"the intermolecular forces in $\\text{{{p['a']}}}$ than in $\\text{{{p['b']}}}$, resulting in a much higher boiling point."
    )
    return _pillars(
        qid=f"ps11_26_{rng.randint(10000, 99999)}",
        subskill="26_boiling_point_comparison_hydrides_anomaly",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify {p['imf_a']} in {p['a']}", "marks": 1},
            {"id": "mp2", "desc": f"Identify {p['imf_b']} in {p['b']}", "marks": 1},
            {"id": "mp3", "desc": "Compare IMF strength and energy required to overcome forces", "marks": 2},
        ],
        hints={
            "1_nudge": "Check whether hydrogen is bonded to N, O, or F in each hydride.",
            "2_concept": "Stronger intermolecular forces require more energy to overcome during boiling.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_boiling_breaks_covalent_bonds", "attributing_higher_bp_to_molar_mass_only"],
        marks=4,
        duration=5,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Hydride boiling points ({p['a']} vs {p['b']})"},
    )


# =========================================================================== #
# 27: Vapour Pressure and Evaporation Rate vs IMF (Inline SVG)
# =========================================================================== #
def build_27_vapour_pressure_and_evaporation_rate_vs_imf(rng: random.Random) -> Dict[str, Any]:
    datasets = [
        {"x": "Ethanol", "vx": "5,9 kPa", "y": "Water", "vy": "3,2 kPa", "stronger": "Water", "weaker": "Ethanol", "temp": 20},
        {"x": "Acetone", "vx": "24,6 kPa", "y": "Ethanol", "vy": "5,9 kPa", "stronger": "Ethanol", "weaker": "Acetone", "temp": 20},
        {"x": "Diethyl ether", "vx": "58,9 kPa", "y": "Propanone", "vy": "24,6 kPa", "stronger": "Propanone", "weaker": "Diethyl ether", "temp": 20},
    ]
    d = rng.choice(datasets)
    svg = _svg_wrap(
        f'<rect x="30" y="25" width="300" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="180" y="52" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">Vapour Pressure at {d["temp"]} °C</text>'
        f'<text x="115" y="95" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{d["x"]}</text>'
        f'<text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#1e3a8a">{d["vx"]}</text>'
        f'<text x="245" y="95" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">{d["y"]}</text>'
        f'<text x="245" y="118" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#991b1b">{d["vy"]}</text>'
        f'<text x="180" y="155" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">Closed containers at thermal equilibrium</text>',
        width=360,
        height=195,
    )
    prompt = (
        f"Refer to the vapour pressure measurement panel for **{d['x']}** ({d['vx']}) and **{d['y']}** ({d['vy']}) at ${d['temp']}^\\circ\\text{{C}}$.\n\n"
        f"1. State which liquid has the **stronger** intermolecular forces.\n"
        f"2. State which liquid evaporates faster and has the **lower** boiling point, explaining in terms of intermolecular forces."
    )
    ans = f"Stronger IMF: {d['stronger']}; Faster evaporation & lower boiling point: {d['weaker']} (weaker IMF, escapes surface easily)"
    sample = (
        f"1. **{d['stronger']}** has stronger intermolecular forces because it exhibits the lower vapour pressure.\n"
        f"2. **{d['weaker']}** evaporates faster and has the lower boiling point: weaker intermolecular forces mean less energy is required "
        f"for surface molecules to escape into the vapour phase, creating a higher equilibrium vapour pressure."
    )
    return _pillars(
        qid=f"ps11_27_{rng.randint(10000, 99999)}",
        subskill="27_vapour_pressure_and_evaporation_rate_vs_imf",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Stronger IMF: {d['stronger']}", "marks": 1},
            {"id": "mp2", "desc": f"Faster evaporation & lower BP: {d['weaker']}", "marks": 1},
            {"id": "mp3", "desc": "Weaker IMF requires less energy to escape liquid phase -> higher vapour pressure", "marks": 2},
        ],
        hints={
            "1_nudge": "Vapour pressure and boiling point are inversely related: high vapour pressure means weak intermolecular forces.",
            "2_concept": "Molecules held weakly in the liquid escape easily into gas, raising vapour pressure.",
            "3_breakdown": sample,
        },
        misconception_tags=["equating_higher_vapour_pressure_with_stronger_IMF"],
        marks=4,
        duration=4,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Vapour pressure comparison ({d['x']} vs {d['y']})"},
    )


# =========================================================================== #
# 28: Viscosity and Chain Length (Motor Oils & Glycerine)
# =========================================================================== #
def build_28_viscosity_and_chain_length_motor_oils(rng: random.Random) -> Dict[str, Any]:
    comparisons = [
        {
            "liq_a": "SAE 50 monograde motor oil",
            "liq_b": "SAE 30 monograde motor oil",
            "visc": "SAE 50",
            "reason": "longer hydrocarbon chains create greater surface contact area and stronger induced dipole forces",
        },
        {
            "liq_a": "Glycerine (propane-1,2,3-triol)",
            "liq_b": "Water (H₂O)",
            "visc": "Glycerine",
            "reason": "three –OH groups per molecule form an extensive three-dimensional hydrogen-bonding network that resists flow",
        },
        {
            "liq_a": "Sunflower oil (long triglycerides)",
            "liq_b": "Methylated spirits (ethanol)",
            "visc": "Sunflower oil",
            "reason": "much larger molecular mass and tangled long chains yield stronger cumulative dispersion forces",
        },
    ]
    c = rng.choice(comparisons)
    prompt = (
        f"A metal sphere is dropped simultaneously into identical measuring cylinders containing **{c['liq_a']}** and **{c['liq_b']}** "
        f"at room temperature. The sphere falls much more slowly through **{c['visc']}**.\n\n"
        f"1. Define **viscosity**.\n"
        f"2. Explain at the molecular level why **{c['visc']}** has the higher viscosity."
    )
    ans = f"Resistance of a liquid to flow; {c['visc']} is more viscous because {c['reason']}"
    sample = (
        f"1. **Viscosity** is a measure of a fluid's resistance to flow.\n"
        f"2. {c['visc']} has stronger overall intermolecular forces because {c['reason']}, making it harder for molecules to slide past one another."
    )
    return _pillars(
        qid=f"ps11_28_{rng.randint(10000, 99999)}",
        subskill="28_viscosity_and_chain_length_motor_oils",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: resistance to flow", "marks": 1},
            {"id": "mp2", "desc": f"Molecular explanation: {c['reason']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Think about how easily liquid layers slide over one another when intermolecular forces are strong.",
            "2_concept": "Stronger IMF and longer tangled chains increase viscosity (resistance to flow).",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_viscosity_with_density"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 29: Surface Tension and Capillarity vs IMF
# =========================================================================== #
def build_29_surface_tension_and_capillarity_imf(rng: random.Random) -> Dict[str, Any]:
    liquids = [
        ("water", "acetone (nail polish remover)", "hydrogen bonding", "dipole-dipole forces"),
        ("water", "hexane", "hydrogen bonding", "induced dipole (London) forces"),
    ]
    l1, l2, f1, f2 = rng.choice(liquids)
    prompt = (
        f"In a capillarity investigation, narrow glass capillary tubes are placed vertically into dishes containing **{l1}** and **{l2}**.\n\n"
        f"1. Predict which liquid rises higher up the narrow glass tube and exhibits higher **surface tension**.\n"
        f"2. Explain your prediction by comparing the intermolecular forces in **{l1}** and **{l2}**."
    )
    ans = f"{l1} rises higher and has greater surface tension due to strong {f1} compared to weaker {f2} in {l2}"
    sample = (
        f"1. **{l1.capitalize()}** rises higher up the capillary tube and has much higher surface tension.\n"
        f"2. {l1.capitalize()} molecules are held together by strong **{f1}** (and adhere strongly to polar Si–O groups on glass), "
        f"whereas {l2} only has weaker **{f2}**."
    )
    return _pillars(
        qid=f"ps11_29_{rng.randint(10000, 99999)}",
        subskill="29_surface_tension_and_capillarity_imf",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Predict {l1} has greater surface tension and capillary rise", "marks": 1},
            {"id": "mp2", "desc": f"Compare {f1} in {l1} vs {f2} in {l2}", "marks": 2},
        ],
        hints={
            "1_nudge": "Surface tension pulls surface molecules inward; stronger IMF creates higher surface tension.",
            "2_concept": "Capillary rise is supported by strong intermolecular cohesion and adhesion to glass.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_less_viscous_liquid_rises_higher_in_capillary"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 30: Solubility ("Like Dissolves Like")
# =========================================================================== #
def build_30_solubility_like_dissolves_like_polarity(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "solute": "I₂(s) (iodine)",
            "sol_type": "non-polar molecular solid (induced dipole forces)",
            "solv1": "CCl₄(l) (tetrachloromethane, non-polar)",
            "solv2": "H₂O(l) (water, polar with hydrogen bonding)",
            "soluble_in": "CCl₄(l)",
        },
        {
            "solute": "KCl(s) (potassium chloride)",
            "sol_type": "ionic crystal lattice",
            "solv1": "H₂O(l) (water, polar solvent)",
            "solv2": "CCl₄(l) (tetrachloromethane, non-polar solvent)",
            "soluble_in": "H₂O(l)",
        },
        {
            "solute": "CH₃OH(l) (methanol)",
            "sol_type": "polar molecule with hydrogen bonding",
            "solv1": "H₂O(l) (water, polar with hydrogen bonding)",
            "solv2": "Hexane C₆H₁₄(l) (non-polar solvent)",
            "soluble_in": "H₂O(l)",
        },
    ]
    c = rng.choice(cases)
    prompt = (
        f"A learner attempts to dissolve **{c['solute']}** separately in two solvents: **{c['solv1']}** and **{c['solv2']}**.\n\n"
        f"1. State in which solvent **{c['solute']}** dissolves readily.\n"
        f"2. Explain this solubility observation in terms of intermolecular forces and polarity ('like dissolves like')."
    )
    ans = f"Dissolves readily in {c['soluble_in']} because both solute and solvent form comparable intermolecular forces"
    sample = (
        f"1. **{c['solute']}** dissolves readily in **{c['soluble_in']}**.\n"
        f"2. {c['solute']} is a {c['sol_type']}. According to 'like dissolves like', the new solute–solvent forces formed with "
        f"{c['soluble_in']} are comparable in strength to the original solute–solute and solvent–solvent forces."
    )
    return _pillars(
        qid=f"ps11_30_{rng.randint(10000, 99999)}",
        subskill="30_solubility_like_dissolves_like_polarity",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct solvent: {c['soluble_in']}", "marks": 1},
            {"id": "mp2", "desc": f"Identify solute nature ({c['sol_type']})", "marks": 1},
            {"id": "mp3", "desc": "Comparable solute-solvent IMF energy allows dissolution", "marks": 1},
        ],
        hints={
            "1_nudge": "Polar/ionic solutes dissolve in polar solvents; non-polar solutes dissolve in non-polar solvents.",
            "2_concept": "Dissolution occurs when solute-solvent attractions compensate for breaking solute-solute and solvent-solvent attractions.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_ionic_salts_dissolve_well_in_nonpolar_solvents"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 31: Covalent Network vs Molecular vs Ionic Melting Points
# =========================================================================== #
def build_31_covalent_network_vs_molecular_melting_points(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Diamond (C)", 3550, "Dry ice (CO₂)", -57, "giant covalent network of strong C–C covalent bonds", "weak induced dipole intermolecular forces"),
        ("Quartz (SiO₂)", 1710, "Iodine (I₂)", 114, "giant covalent network of strong Si–O covalent bonds", "weak induced dipole intermolecular forces"),
        ("Sodium chloride (NaCl)", 801, "Water ice (H₂O)", 0, "strong electrostatic ionic bonds in a 3D crystal lattice", "intermolecular hydrogen bonds between discrete molecules"),
    ]
    a, mpa, b, mpb, fa, fb = rng.choice(pairs)
    prompt = (
        f"Compare the melting points of **{a}** ($T_m = {mpa}^\\circ\\text{{C}}$) and **{b}** ($T_m = {mpb}^\\circ\\text{{C}}$).\n\n"
        f"Explain the vast difference in melting points by identifying the exact particles and forces broken when each solid melts."
    )
    ans = f"Melting {a} breaks {fa}, whereas melting {b} only overcomes {fb}"
    sample = (
        f"- **{a}** melts at {mpa} °C because melting requires breaking a **{fa}**, demanding huge thermal energy.\n"
        f"- **{b}** melts at {mpb} °C because only **{fb}** between discrete covalent molecules are overcome, requiring far less energy."
    )
    return _pillars(
        qid=f"ps11_31_{rng.randint(10000, 99999)}",
        subskill="31_covalent_network_vs_molecular_melting_points",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"{a}: {fa}", "marks": 2},
            {"id": "mp2", "desc": f"{b}: {fb}", "marks": 2},
        ],
        hints={
            "1_nudge": "Distinguish giant crystal networks (covalent or ionic) from discrete simple molecular solids.",
            "2_concept": "Covalent network solids break actual covalent bonds upon melting; molecular solids only overcome weak IMF.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_SiO2_is_molecular_solid", "claiming_diamond_has_strong_IMF"],
        marks=4,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 32: Heating & Cooling Curve Phase Plateaus (Inline SVG)
# =========================================================================== #
def build_32_heating_and_cooling_curve_phase_plateaus(rng: random.Random) -> Dict[str, Any]:
    substances = [
        {"name": "water", "mp": 0, "bp": 100, "start": -20, "end": 120},
        {"name": "ethanol", "mp": -114, "bp": 78, "start": -130, "end": 100},
        {"name": "acetic acid", "mp": 17, "bp": 118, "start": 0, "end": 135},
    ]
    s = rng.choice(substances)
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="185" x2="345" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="16" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">T (°C)</text>'
        f'<text x="275" y="203" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Time (min)</text>'
        f'<polyline points="55,170 95,140 155,140 220,75 290,75 330,35" fill="none" stroke="#2563eb" stroke-width="2.8"/>'
        f'<text x="125" y="133" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">BC ({s["mp"]}°C)</text>'
        f'<text x="255" y="68" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">DE ({s["bp"]}°C)</text>'
        f'<text x="72" y="160" font-family="sans-serif" font-size="10" fill="#475569">AB</text>'
        f'<text x="182" y="102" font-family="sans-serif" font-size="10" fill="#475569">CD</text>'
        f'<text x="195" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Heating Curve: {s["name"].capitalize()}</text>',
        width=360,
        height=215,
    )
    prompt = (
        f"Refer to the heating curve for pure **{s['name']}** heated uniformly from ${s['start']}^\\circ\\text{{C}}$ to ${s['end']}^\\circ\\text{{C}}$.\n\n"
        f"1. Name the phase change occurring along horizontal plateau **BC** ({s['mp']} °C) and along plateau **DE** ({s['bp']} °C).\n"
        f"2. Explain why the temperature remains constant along **DE** even though heat energy continues to be supplied."
    )
    ans = f"BC: melting ({s['mp']} °C); DE: boiling ({s['bp']} °C); added heat increases potential energy to overcome intermolecular forces rather than kinetic energy"
    sample = (
        f"1. **BC**: melting (solid + liquid in equilibrium at {s['mp']} °C). **DE**: boiling (liquid + gas in equilibrium at {s['bp']} °C).\n"
        f"2. Along **DE**, absorbed heat energy is used as latent heat (increasing potential energy) to overcome the intermolecular forces holding "
        f"liquid {s['name']} molecules together, while average kinetic energy (and therefore temperature) remains constant."
    )
    return _pillars(
        qid=f"ps11_32_{rng.randint(10000, 99999)}",
        subskill="32_heating_and_cooling_curve_phase_plateaus",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"BC = melting ({s['mp']} °C) and DE = boiling ({s['bp']} °C)", "marks": 2},
            {"id": "mp2", "desc": "Energy goes into potential energy to overcome IMF; average Ek constant", "marks": 2},
        ],
        hints={
            "1_nudge": "Temperature is proportional to the average kinetic energy of the particles.",
            "2_concept": "During a phase change plateau, supplied energy overcomes intermolecular forces (potential energy increases).",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_heat_stops_entering_at_plateau", "confusing_kinetic_with_potential_energy"],
        marks=4,
        duration=5,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Heating curve ({s['name']})"},
    )


# =========================================================================== #
# 33: Density Anomaly of Ice and Aquatic Survival
# =========================================================================== #
def build_33_density_anomaly_of_ice_and_aquatic_life(rng: random.Random) -> Dict[str, Any]:
    lake_depth = rng.choice([4, 6, 8, 12])
    prompt = (
        f"During severe winter frost, a freshwater lake of depth ${lake_depth}\\text{{ m}}$ freezes on its top surface, "
        f"forming a solid sheet of ice ($\\rho = 0{{,}}92\\text{{ g·cm}}^{{-3}}$) floating on liquid water ($\\rho = 1{{,}}00\\text{{ g·cm}}^{{-3}}$).\n\n"
        f"1. Explain in terms of **hydrogen bonding** why solid ice is less dense than liquid water.\n"
        f"2. Explain why this density anomaly is essential for aquatic organisms surviving winter."
    )
    ans = "Ice forms an open hexagonal hydrogen-bonded lattice with larger volume; floating ice insulates deeper liquid water"
    sample = (
        f"1. As water freezes, each $\\text{{H}}_2\\text{{O}}$ molecule forms four rigid directional **hydrogen bonds** arranged in an open hexagonal crystal lattice. "
        f"This leaves empty spaces between molecules, increasing volume for the same mass and lowering density ($\\rho = m/V$).\n"
        f"2. Because ice floats on top, it forms an insulating thermal blanket that prevents heat loss from the {lake_depth} m lake below, "
        f"allowing liquid water and aquatic life to survive underneath."
    )
    return _pillars(
        qid=f"ps11_33_{rng.randint(10000, 99999)}",
        subskill="33_density_anomaly_of_ice_and_aquatic_life",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Open crystal lattice formed by directional hydrogen bonds increases volume", "marks": 2},
            {"id": "mp2", "desc": "Floating ice insulates underlying liquid water so lakes do not freeze solid", "marks": 2},
        ],
        hints={
            "1_nudge": "Most substances contract when freezing, but water expands when hydrogen bonds lock molecules in place.",
            "2_concept": "Greater volume for a fixed mass decreases density (ρ = m/V).",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_ice_floats_because_air_bubbles_are_trapped"],
        marks=4,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 34: Water High Specific Heat Capacity & Climate Moderation
# =========================================================================== #
def build_34_water_high_specific_heat_capacity_climate(rng: random.Random) -> Dict[str, Any]:
    mass_kg = rng.choice([2, 3, 4, 5])
    dt = rng.choice([10, 15, 20])
    c_water = 4180  # J/(kg.K)
    q_kj = round((mass_kg * c_water * dt) / 1000, 1)
    city_pair = rng.choice([("Durban (coastal)", "Bloemfontein (inland)"), ("Cape Town (coastal)", "Kimberley (inland)")])
    prompt = (
        f"Water has an unusually high specific heat capacity ($c = 4\\,180\\text{{ J·kg}}^{{-1}}\\text{{·K}}^{{-1}}$) and high heat of vaporisation "
        f"($40{{,}}65\\text{{ kJ·mol}}^{{-1}}$).\n\n"
        f"1. Calculate the heat energy (in kJ) required to raise the temperature of ${mass_kg}\\text{{ kg}}$ of water by ${dt}^\\circ\\text{{C}}$ ($Q = mc\\Delta T$).\n"
        f"2. Explain in terms of hydrogen bonding why **{city_pair[0]}** experiences milder temperature fluctuations than **{city_pair[1]}**."
    )
    ans = f"Q = {_fmt_sa(q_kj, 1)} kJ; ocean water absorbs/releases large heat via hydrogen bonds with minimal temperature change"
    sample = (
        f"1. $Q = mc\\Delta T = ({mass_kg})(4\\,180)({dt}) = {mass_kg * c_water * dt}\\text{{ J}} = {_fmt_sa(q_kj, 1)}\\text{{ kJ}}$.\n"
        f"2. Much absorbed solar energy goes into disrupting strong intermolecular **hydrogen bonds** rather than increasing particle kinetic energy. "
        f"Thus, coastal oceans act as heat reservoirs that moderate temperature swings in {city_pair[0]}."
    )
    return _pillars(
        qid=f"ps11_34_{rng.randint(10000, 99999)}",
        subskill="34_water_high_specific_heat_capacity_climate",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Substitution into Q = mcΔT = {_fmt_sa(q_kj, 1)} kJ", "marks": 2},
            {"id": "mp2", "desc": "Explain via hydrogen bonds absorbing energy -> ocean heat reservoir", "marks": 2},
        ],
        hints={
            "1_nudge": "Use Q = mcΔT and convert joules to kilojoules by dividing by 1 000.",
            "2_concept": "Hydrogen bonding requires large energy input before water molecules gain translational kinetic energy.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_to_convert_J_to_kJ"],
        marks=4,
        duration=5,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 35: Thermal Expansion and Thermal Conductivity
# =========================================================================== #
def build_35_thermal_expansion_and_thermal_conductivity(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        {
            "ctx": "A copper rod and a solid paraffin wax rod have toothpicks attached to their ends with wax and are heated equally at the opposite end.",
            "q": "Which toothpick falls first and why is copper a superior thermal conductor?",
            "ans": "Copper rod toothpick falls first because copper has delocalised valence electrons that transfer kinetic energy rapidly",
        },
        {
            "ctx": "Builders leave small expansion gaps between ceramic floor tiles and engineers allow overhead power lines to sag slightly in summer.",
            "q": "Explain why solids and liquids expand upon heating at the particle level.",
            "ans": "Heating increases average kinetic energy so particles vibrate more vigorously and push further apart against intermolecular forces",
        },
    ]
    sc = rng.choice(scenarios)
    prompt = f"{sc['ctx']}\n\n{sc['q']}"
    sample = f"Explanation: {sc['ans']}."
    return _pillars(
        qid=f"ps11_35_{rng.randint(10000, 99999)}",
        subskill="35_thermal_expansion_and_thermal_conductivity",
        prompt=prompt,
        answer=sc["ans"],
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify particle kinetic energy / delocalised electron mechanism", "marks": 2},
            {"id": "mp2", "desc": "Link correctly to macroscopic observation", "marks": 1},
        ],
        hints={
            "1_nudge": "Consider how thermal energy moves through metallic vs molecular substances.",
            "2_concept": "Metals have mobile delocalised electrons; heating increases average particle vibration amplitude.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_atoms_themselves_swell_during_expansion"],
        marks=3,
        duration=3,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 36: Earth Concentric Layers & Lithosphere Definition (Inline SVG)
# =========================================================================== #
def build_36_earth_concentric_layers_crust_mantle_core(rng: random.Random) -> Dict[str, Any]:
    targets = [
        {"label": "Layer A", "name": "Crust", "desc": "outermost thin solid shell (continental and oceanic crust)"},
        {"label": "Layer B", "name": "Mantle", "desc": "thick semi-solid silicate magma layer (~2 900 km thick) beneath the crust"},
        {"label": "Layer C", "name": "Outer Core", "desc": "liquid iron–nickel layer surrounding the solid inner core"},
        {"label": "Layer D", "name": "Inner Core", "desc": "solid innermost sphere composed mainly of iron and nickel under extreme pressure"},
    ]
    t = rng.choice(targets)
    svg = _svg_wrap(
        f'<circle cx="180" cy="110" r="95" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>'
        f'<circle cx="180" cy="110" r="82" fill="#f97316" stroke="#7c2d12" stroke-width="1.5"/>'
        f'<circle cx="180" cy="110" r="48" fill="#facc15" stroke="#854d0e" stroke-width="1.5"/>'
        f'<circle cx="180" cy="110" r="22" fill="#fef08a" stroke="#713f12" stroke-width="1.5"/>'
        f'<text x="180" y="23" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ffffff">A</text>'
        f'<text x="180" y="47" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff">B</text>'
        f'<text x="180" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">C</text>'
        f'<text x="180" y="114" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">D</text>'
        f'<text x="315" y="195" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Focus: {t["label"]}</text>',
        width=370,
        height=220,
    )
    prompt = (
        f"Refer to the cross-sectional diagram of Earth's concentric internal structure (layers A, B, C, and D from outside to centre).\n\n"
        f"1. Identify **{t['label']}** and state its physical state.\n"
        f"2. Define the **lithosphere** in terms of Earth's structural layers."
    )
    ans = f"{t['label']} is the {t['name']} ({t['desc']}); the lithosphere comprises the crust plus the solid brittle upper mantle"
    sample = (
        f"1. **{t['label']}** is the **{t['name']}**: {t['desc']}.\n"
        f"2. The **lithosphere** consists of Earth's crust (oceanic and continental) together with the solid, brittle uppermost part of the mantle."
    )
    return _pillars(
        qid=f"ps11_36_{rng.randint(10000, 99999)}",
        subskill="36_earth_concentric_layers_crust_mantle_core",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify {t['label']} = {t['name']}", "marks": 1},
            {"id": "mp2", "desc": f"Correct state/description ({t['desc']})", "marks": 1},
            {"id": "mp3", "desc": "Lithosphere = crust + solid upper mantle", "marks": 2},
        ],
        hints={
            "1_nudge": "Read layers strictly from outside (A) towards the centre (D): Crust -> Mantle -> Outer Core -> Inner Core.",
            "2_concept": "Lithos means stone; the lithosphere is the rigid rocky outer shell of the geosphere.",
            "3_breakdown": sample,
        },
        misconception_tags=["swapping_solid_inner_and_liquid_outer_core", "equating_lithosphere_only_with_crust"],
        marks=4,
        duration=4,
        topic_label="The lithosphere",
        term=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Earth concentric cross-section ({t['label']})"},
    )


# =========================================================================== #
# 37: Rock Cycle Transformations (Inline SVG)
# =========================================================================== #
def build_37_rock_cycle_igneous_sedimentary_metamorphic(rng: random.Random) -> Dict[str, Any]:
    paths = [
        {"start": "Shale (sedimentary)", "proc": "intense heat and pressure deep underground", "end": "Slate (metamorphic)"},
        {"start": "Limestone (sedimentary)", "proc": "intense heat and pressure without melting", "end": "Marble (metamorphic)"},
        {"start": "Sandstone (sedimentary)", "proc": "heat and pressure metamorphism", "end": "Quartzite (metamorphic)"},
        {"start": "Magma (molten rock)", "proc": "cooling and crystallisation", "end": "Granite / Basalt (igneous)"},
        {"start": "Weathered sand particles", "proc": "deposition, compaction, and cementation", "end": "Sandstone (sedimentary)"},
    ]
    p = rng.choice(paths)
    svg = _svg_wrap(
        f'<rect x="20" y="70" width="110" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="75" y="99" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a">Igneous</text>'
        f'<rect x="230" y="70" width="110" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="285" y="99" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#92400e">Sedimentary</text>'
        f'<rect x="125" y="150" width="110" height="45" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="180" y="177" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#14532d">Metamorphic</text>'
        f'<line x1="130" y1="95" x2="230" y2="95" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="285" y1="120" x2="235" y2="165" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="125" y1="165" x2="75" y2="120" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="180" y="32" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Rock Cycle Transition: {p["start"]}</text>',
        width=360,
        height=210,
    )
    prompt = (
        f"Refer to the rock cycle diagram.\n\n"
        f"When **{p['start']}** undergoes **{p['proc']}**, identify the resulting rock type/example formed and describe one key physical change that occurs."
    )
    ans = f"{p['end']} formed via {p['proc']}"
    sample = (
        f"Resulting rock: **{p['end']}**.\n"
        f"Process: {p['proc']} alters crystal structure, texture, and density over geological time."
    )
    return _pillars(
        qid=f"ps11_37_{rng.randint(10000, 99999)}",
        subskill="37_rock_cycle_igneous_sedimentary_metamorphic",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct product: {p['end']}", "marks": 2},
            {"id": "mp2", "desc": "Accurate geological transformation explanation", "marks": 1},
        ],
        hints={
            "1_nudge": "Cooling magma -> igneous; compaction of sediments -> sedimentary; heat & pressure without melting -> metamorphic.",
            "2_concept": f"Pair {p['start']} with its metamorphic/rock-cycle product.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_metamorphism_with_complete_melting"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Rock cycle ({p['start']} -> {p['end']})"},
    )


# =========================================================================== #
# 38: Igneous Cooling Rate, Crystal Size & Pumice
# =========================================================================== #
def build_38_igneous_cooling_rate_crystal_size_and_pumice(rng: random.Random) -> Dict[str, Any]:
    rocks = [
        {"name": "Granite", "origin": "intrusive (deep underground)", "rate": "slow cooling", "crystals": "large visible interlocking crystals"},
        {"name": "Basalt", "origin": "extrusive (on Earth's surface)", "rate": "rapid cooling", "crystals": "very fine-grained microscopic crystals"},
        {"name": "Pumice", "origin": "extrusive volcanic eruption", "rate": "extremely rapid cooling", "crystals": "glassy porous texture with trapped gas cavities (floats on water)"},
    ]
    rk = rng.choice(rocks)
    prompt = (
        f"Geologists classify **{rk['name']}** as an igneous rock.\n\n"
        f"1. State whether **{rk['name']}** forms intrusively or extrusively and describe its magma/lava cooling rate.\n"
        f"2. Describe the crystal texture or physical structure of **{rk['name']}** resulting from this cooling rate."
    )
    ans = f"{rk['origin']}; {rk['rate']}; {rk['crystals']}"
    sample = (
        f"1. **{rk['name']}** is **{rk['origin']}**, formed by **{rk['rate']}**.\n"
        f"2. This cooling rate produces **{rk['crystals']}**."
    )
    return _pillars(
        qid=f"ps11_38_{rng.randint(10000, 99999)}",
        subskill="38_igneous_cooling_rate_crystal_size_and_pumice",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Origin: {rk['origin']}", "marks": 1},
            {"id": "mp2", "desc": f"Cooling rate: {rk['rate']}", "marks": 1},
            {"id": "mp3", "desc": f"Texture: {rk['crystals']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Slow cooling underground allows crystals plenty of time to grow large; rapid cooling at the surface gives small crystals or trapped gas.",
            "2_concept": "Intrusive = inside crust (slow); extrusive = surface lava (fast).",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_fast_cooling_produces_large_crystals"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 39: Sedimentary Rocks & Fossil Preservation
# =========================================================================== #
def build_39_sedimentary_rocks_and_fossil_preservation(rng: random.Random) -> Dict[str, Any]:
    fossils = ["ancient fern leaves", "trilobite marine shells", "Karoo vertebrate bones"]
    f = rng.choice(fossils)
    prompt = (
        f"Palaeontologists frequently discover preserved impressions of **{f}** inside sedimentary rock layers such as shale and limestone, "
        f"but almost never inside igneous rocks like granite or basalt.\n\n"
        f"Give TWO scientific reasons why fossils are preserved specifically in sedimentary rocks."
    )
    ans = "Low temperature/pressure during deposition preserves organic structures, and rapid burial by sediment prevents decay before mineralisation"
    sample = (
        f"1. Sedimentary rocks form at relatively **low temperatures and moderate pressures** (via compaction and cementation), "
        f"whereas molten magma in igneous rocks and intense heat/pressure in metamorphic rocks destroy organic remains.\n"
        f"2. Rapid burial of **{f}** beneath accumulating sand, mud, or silt protects hard parts from scavengers and oxygen decay, allowing gradual mineralisation."
    )
    return _pillars(
        qid=f"ps11_39_{rng.randint(10000, 99999)}",
        subskill="39_sedimentary_rocks_and_fossil_preservation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Low temperature/pressure compared to molten magma/metamorphism", "marks": 2},
            {"id": "mp2", "desc": "Rapid burial by sediment layers prevents decay/scavenging", "marks": 1},
        ],
        hints={
            "1_nudge": "Compare the heat of molten magma with cool river/ocean sediment deposition.",
            "2_concept": "Hard tissues are buried in sediment layers and slowly mineralised.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_fossils_form_inside_cooling_magma"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 40: Lithosphere Abundant Minerals and Chemical Formulas
# =========================================================================== #
def build_40_lithosphere_abundant_minerals_and_formulas(rng: random.Random) -> Dict[str, Any]:
    minerals = [
        {"name": "Haematite", "chem": "Iron(III) oxide", "formula": "Fe₂O₃", "use": "iron extraction for steel"},
        {"name": "Magnetite", "chem": "Triiron tetraoxide", "formula": "Fe₃O₄", "use": "magnetic iron ore"},
        {"name": "Quartz", "chem": "Silicon dioxide", "formula": "SiO₂", "use": "glass manufacturing and electronics"},
        {"name": "Chalcocite", "chem": "Copper(I) sulfide", "formula": "Cu₂S", "use": "copper metal extraction"},
        {"name": "Chalcopyrite", "chem": "Copper iron sulfide", "formula": "CuFeS₂", "use": "primary copper mineral ore"},
    ]
    m = rng.choice(minerals)
    prompt = (
        f"The lithosphere contains naturally occurring inorganic compounds known as minerals.\n\n"
        f"For the mineral **{m['name']}** ({m['chem']}):\n"
        f"1. Write down its chemical formula.\n"
        f"2. Identify the primary metal/non-metal elements present and state one major industrial use."
    )
    ans = f"Formula: {m['formula']}; Use: {m['use']}"
    sample = (
        f"1. Chemical formula of {m['name']}: **$\\text{{{m['formula']}}}$**.\n"
        f"2. It is a natural mineral source used industrially for {m['use']}."
    )
    return _pillars(
        qid=f"ps11_40_{rng.randint(10000, 99999)}",
        subskill="40_lithosphere_abundant_minerals_and_formulas",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct formula: {m['formula']}", "marks": 2},
            {"id": "mp2", "desc": f"Valid industrial use ({m['use']})", "marks": 1},
        ],
        hints={
            "1_nudge": f"Translate the chemical name '{m['chem']}' using ion valencies/oxidation numbers.",
            "2_concept": "Minerals are naturally occurring compounds with fixed chemical formulas.",
            "3_breakdown": sample,
        },
        misconception_tags=["wrong_valency_subscript_FeO_instead_of_Fe2O3"],
        marks=3,
        duration=3,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 41: South African Mineral Resources Distribution
# =========================================================================== #
def build_41_south_african_mineral_resources_distribution(rng: random.Random) -> Dict[str, Any]:
    reserves = [
        {"resource": "Iron ore (haematite)", "region": "Sishen (Northern Cape)", "use": "blast furnace reduction to iron and steel"},
        {"resource": "Gold", "region": "Witwatersrand Basin (Gauteng / Free State)", "use": "electrical contacts, jewellery, and monetary reserves"},
        {"resource": "Platinum & Chromium", "region": "Bushveld Igneous Complex (North West / Limpopo)", "use": "catalytic converters and stainless steel"},
        {"resource": "Phosphates", "region": "Phalaborwa (Limpopo)", "use": "superphosphate agricultural fertilisers"},
        {"resource": "Coal", "region": "Highveld / Mpumalanga coalfields", "use": "thermal electricity generation and synthetic fuels"},
    ]
    r = rng.choice(reserves)
    prompt = (
        f"South Africa's lithosphere hosts world-leading reserves of **{r['resource']}**.\n\n"
        f"1. Name the major geological region or town in South Africa associated with mining **{r['resource']}**.\n"
        f"2. State ONE major industrial or economic application of **{r['resource']}**."
    )
    ans = f"Region: {r['region']}; Application: {r['use']}"
    sample = (
        f"1. Major South African mining region: **{r['region']}**.\n"
        f"2. Industrial application: {r['use']}."
    )
    return _pillars(
        qid=f"ps11_41_{rng.randint(10000, 99999)}",
        subskill="41_south_african_mineral_resources_distribution",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct SA mining region: {r['region']}", "marks": 1},
            {"id": "mp2", "desc": f"Valid application: {r['use']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Connect each mineral resource to its primary South African geological basin.",
            "2_concept": "Mineral distribution reflects ancient igneous, sedimentary, and metamorphic basins.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_Sishen_iron_with_Phalaborwa_copper_phosphate"],
        marks=2,
        duration=3,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 42: Gold Mining Cyanidation Process Flowchart (Inline SVG)
# =========================================================================== #
def build_42_gold_mining_cyanidation_process_flowchart(rng: random.Random) -> Dict[str, Any]:
    steps = [
        {
            "focus": "Step A",
            "reactant": "sodium cyanide (NaCN) and oxygen (O₂)",
            "desc": "dissolves gold from crushed ore to form soluble sodium dicyanoaurate(I), NaAu(CN)₂",
        },
        {
            "focus": "Step B",
            "reactant": "powdered zinc (Zn)",
            "desc": "reduces Au⁺ ions in NaAu(CN)₂ back into solid gold precipitate while Zn oxidises",
        },
        {
            "focus": "Step C",
            "reactant": "smelting with acid/heat purification",
            "desc": "removes residual zinc and impurities to produce high-purity metallic gold bars",
        },
    ]
    st = rng.choice(steps)
    svg = _svg_wrap(
        f'<rect x="10" y="75" width="75" height="45" rx="5" fill="#f1f5f9" stroke="#334155"/>'
        f'<text x="47" y="101" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">Gold ore</text>'
        f'<line x1="85" y1="97" x2="108" y2="97" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="96" y="88" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">A</text>'
        f'<rect x="108" y="75" width="80" height="45" rx="5" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="148" y="101" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">NaAu(CN)₂</text>'
        f'<line x1="188" y1="97" x2="210" y2="97" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="199" y="88" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">B</text>'
        f'<rect x="210" y="75" width="75" height="45" rx="5" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="247" y="101" text-anchor="middle" font-family="sans-serif" font-size="9" font-weight="bold">Au precipitate</text>'
        f'<line x1="285" y1="97" x2="306" y2="97" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="295" y="88" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#16a34a">C</text>'
        f'<rect x="306" y="75" width="64" height="45" rx="5" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="338" y="101" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">Pure Au</text>'
        f'<text x="190" y="35" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Gold Extraction Flowchart ({st["focus"]})</text>',
        width=380,
        height=175,
    )
    prompt = (
        f"Refer to the industrial gold extraction flowchart above.\n\n"
        f"Focus on **{st['focus']}**:\n"
        f"1. Name the chemical reagent(s) or process applied in **{st['focus']}**.\n"
        f"2. Describe the chemical role of **{st['focus']}** in recovering pure gold from gold-bearing ore."
    )
    ans = f"{st['focus']} uses {st['reactant']} to {st['desc']}"
    sample = (
        f"1. Reagent/process in {st['focus']}: **{st['reactant']}**.\n"
        f"2. Role: It {st['desc']}."
    )
    return _pillars(
        qid=f"ps11_42_{rng.randint(10000, 99999)}",
        subskill="42_gold_mining_cyanidation_process_flowchart",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct reagent/process: {st['reactant']}", "marks": 1},
            {"id": "mp2", "desc": f"Role: {st['desc']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Gold recovery proceeds via: (A) cyanide leaching -> (B) zinc precipitation -> (C) smelting/purification.",
            "2_concept": "Gold is unreactive and must be complexed with cyanide before displacement by more reactive zinc.",
            "3_breakdown": sample,
        },
        misconception_tags=["swapping_cyanide_leaching_and_zinc_precipitation"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Gold cyanidation flowchart ({st['focus']})"},
    )


# =========================================================================== #
# 43: Gold Cyanidation Redox & Environmental Impact
# =========================================================================== #
def build_43_gold_cyanidation_redox_and_environmental_impact(rng: random.Random) -> Dict[str, Any]:
    aspects = [
        {
            "focus": "Redox recovery with zinc",
            "eq": "2NaAu(CN)₂(aq) + Zn(s) → 2Au(s) + Na₂Zn(CN)₄(aq)",
            "q": "Identify which species is reduced and which acts as the reducing agent.",
            "ans": "Au⁺ (in NaAu(CN)₂) is reduced to Au(s); Zn(s) is oxidised and acts as the reducing agent",
        },
        {
            "focus": "Environmental sustainability of gold mining",
            "eq": "4Au(s) + 8NaCN(aq) + O₂(g) + 2H₂O(l) → 4NaAu(CN)₂(aq) + 4NaOH(aq)",
            "q": "State TWO major environmental risks associated with gold cyanidation and mine tailings dumps.",
            "ans": "Toxic cyanide leakage contaminating groundwater/rivers and acid mine drainage from sulfide-rich mine tailings",
        },
    ]
    a = rng.choice(aspects)
    prompt = (
        f"Consider the gold mining reaction equation ({a['focus']}):\n"
        f"$${a['eq']}$$\n\n"
        f"{a['q']}"
    )
    sample = f"Answer: {a['ans']}."
    return _pillars(
        qid=f"ps11_43_{rng.randint(10000, 99999)}",
        subskill="43_gold_cyanidation_redox_and_environmental_impact",
        prompt=prompt,
        answer=a["ans"],
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Accurate chemical / environmental identification", "marks": 2},
            {"id": "mp2", "desc": "Clear justification / second environmental risk", "marks": 1},
        ],
        hints={
            "1_nudge": "Remember OIL RIG: oxidation is loss of electrons; reduction is gain of electrons.",
            "2_concept": "Mine tailings often contain toxic cyanide ions and pyrite (FeS₂) that oxidises to sulfuric acid.",
            "3_breakdown": sample,
        },
        misconception_tags=["calling_the_reduced_species_the_reducing_agent"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 44: Iron Extraction Blast Furnace Reactions (Inline SVG)
# =========================================================================== #
def build_44_iron_extraction_blast_furnace_reactions(rng: random.Random) -> Dict[str, Any]:
    zones = [
        {"mat": "Coke (C) + Hot air (O₂)", "eq": "C + O₂ → CO₂; CO₂ + C → 2CO", "role": "burns to generate heat and produces carbon monoxide (CO) reducing gas"},
        {"mat": "Haematite (Fe₂O₃) + Carbon monoxide (CO)", "eq": "Fe₂O₃(s) + 3CO(g) → 2Fe(l) + 3CO₂(g)", "role": "reduces iron(III) oxide ore to molten pig iron"},
        {"mat": "Limestone (CaCO₃) + Silica sand (SiO₂)", "eq": "CaO(s) + SiO₂(s) → CaSiO₃(l)", "role": "decomposes to CaO which reacts with acidic SiO₂ impurity to form molten slag"},
    ]
    z = rng.choice(zones)
    svg = _svg_wrap(
        f'<polygon points="130,30 230,30 265,175 95,175" fill="#fff7ed" stroke="#9a3412" stroke-width="2.5"/>'
        f'<text x="180" y="20" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Charge: Fe₂O₃ + C + CaCO₃</text>'
        f'<text x="180" y="95" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c2410c">Blast Furnace</text>'
        f'<text x="180" y="130" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#7c2d12">Hot air blast (O₂) →</text>'
        f'<text x="180" y="160" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Molten Fe &amp; Slag</text>'
        f'<text x="180" y="200" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2563eb">Focus: {z["mat"]}</text>',
        width=360,
        height=215,
    )
    prompt = (
        f"Refer to the schematic of an iron blast furnace extracting iron from haematite ($\\text{{Fe}}_2\\text{{O}}_3$).\n\n"
        f"For the reactants **{z['mat']}**:\n"
        f"1. Write the balanced chemical equation(s) occurring inside the blast furnace.\n"
        f"2. Explain the specific chemical function of this reaction in iron production."
    )
    ans = f"{z['eq']} — {z['role']}"
    sample = (
        f"1. Reaction equation(s): $${z['eq']}$$\n"
        f"2. Function: {z['role'].capitalize()}."
    )
    return _pillars(
        qid=f"ps11_44_{rng.randint(10000, 99999)}",
        subskill="44_iron_extraction_blast_furnace_reactions",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Balanced equation: {z['eq']}", "marks": 2},
            {"id": "mp2", "desc": f"Function: {z['role']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Three main raw materials enter the top of the blast furnace: haematite, coke, and limestone.",
            "2_concept": "CO reduces iron oxide; CaO from limestone removes silica impurities as calcium silicate slag.",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_limestone_reduces_iron_oxide"],
        marks=4,
        duration=5,
        topic_label="The lithosphere",
        term=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Iron blast furnace ({z['mat']})"},
    )


# =========================================================================== #
# 45: Copper Extraction from Sulfide Ores & Refining
# =========================================================================== #
def build_45_copper_extraction_and_electrolytic_refining(rng: random.Random) -> Dict[str, Any]:
    # Cu2S + O2 -> 2Cu + SO2
    moles_cu2s = rng.choice([2, 3, 4, 5])
    m_cu2s = round(moles_cu2s * 159.1, 1)  # M(Cu2S) = 2*63.55 + 32.0 = 159.1
    m_cu = round(moles_cu2s * 2 * 63.55, 1)
    prompt = (
        f"Copper is extracted from the lithosphere mineral chalcocite ($\\text{{Cu}}_2\\text{{S}}$, molar mass $159{{,}}1\\text{{ g·mol}}^{{-1}}$) "
        f"by controlled roasting in air:\n"
        f"$$\\text{{Cu}}_2\\text{{S}}(s) + \\text{{O}}_2(g) \\rightarrow 2\\text{{Cu}}(l) + \\text{{SO}}_2(g)$$\n\n"
        f"1. Calculate the maximum theoretical mass of copper ($M(\\text{{Cu}}) = 63{{,}}55\\text{{ g·mol}}^{{-1}}$) obtained from "
        f"${_fmt_sa(m_cu2s, 1)}\\text{{ g}}$ of pure $\\text{{Cu}}_2\\text{{S}}$.\n"
        f"2. Explain why the gaseous by-product $\\text{{SO}}_2(g)$ must be scrubbed rather than vented directly into the atmosphere."
    )
    ans = f"{_fmt_sa(m_cu, 1)} g Cu; SO₂ reacts with atmospheric moisture/oxygen to cause acid rain"
    sample = (
        f"1. $n(\\text{{Cu}}_2\\text{{S}}) = \\frac{{{_fmt_sa(m_cu2s, 1)}}}{{159{{,}}1}} = {moles_cu2s}\\text{{ mol}}$.\n"
        f"   Mole ratio $\\text{{Cu}}_2\\text{{S}} : \\text{{Cu}} = 1 : 2 \\implies n(\\text{{Cu}}) = {2 * moles_cu2s}\\text{{ mol}}$.\n"
        f"   $m(\\text{{Cu}}) = {2 * moles_cu2s} \\times 63{{,}}55 = {_fmt_sa(m_cu, 1)}\\text{{ g}}$.\n"
        f"2. $\\text{{SO}}_2$ dissolves in rainwater and oxidises to form sulfurous/sulfuric acid (**acid rain**), damaging ecosystems and infrastructure."
    )
    return _pillars(
        qid=f"ps11_45_{rng.randint(10000, 99999)}",
        subskill="45_copper_extraction_and_electrolytic_refining",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Calculate n(Cu2S) = {moles_cu2s} mol", "marks": 1},
            {"id": "mp2", "desc": f"Apply 1:2 mole ratio -> m(Cu) = {_fmt_sa(m_cu, 1)} g", "marks": 2},
            {"id": "mp3", "desc": "Identify SO2 causes acid rain", "marks": 1},
        ],
        hints={
            "1_nudge": "Find moles of Cu₂S using n = m / M first.",
            "2_concept": "Each 1 mole of Cu₂S produces 2 moles of pure copper.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_stoichiometric_factor_2_for_copper"],
        marks=4,
        duration=5,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 46: Phosphate Rock Mining & Fertilisers
# =========================================================================== #
def build_46_phosphate_rock_mining_and_fertilisers(rng: random.Random) -> Dict[str, Any]:
    nutrients = [
        ("phosphorus (P)", "Phalaborwa phosphate rock", "eutrophication (excessive algal blooms depleting dissolved O₂ in rivers)"),
        ("nitrogen & phosphorus (NPK)", "phosphate and nitrate mineral fertilisers", "eutrophication and leaching of nitrates into groundwater"),
    ]
    nut, src, env = rng.choice(nutrients)
    prompt = (
        f"In South Africa, **{src}** is mined and treated with sulfuric acid to convert insoluble calcium phosphate "
        f"($\\text{{Ca}}_3(\\text{{PO}}_4)_2$) into soluble superphosphate fertiliser.\n\n"
        f"1. Explain why raw crushed phosphate rock must be converted into soluble superphosphate before use in agriculture.\n"
        f"2. Explain the environmental consequence known as **eutrophication** if excess {nut} fertiliser washes off farmlands into dams."
    )
    ans = f"Plants can only absorb dissolved phosphate ions; excess runoff causes {env}"
    sample = (
        f"1. Plant roots can only absorb mineral nutrients such as phosphate ions when dissolved in soil water; "
        f"calcium phosphate rock is insoluble, whereas superphosphate is water-soluble.\n"
        f"2. Excess nutrient runoff causes rapid algal blooms (**eutrophication**). When the algae die and decompose, aerobic bacteria consume "
        f"dissolved oxygen in the water, suffocating fish and aquatic life."
    )
    return _pillars(
        qid=f"ps11_46_{rng.randint(10000, 99999)}",
        subskill="46_phosphate_rock_mining_and_fertilisers",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Insoluble rock converted to water-soluble form for root uptake", "marks": 1},
            {"id": "mp2", "desc": "Algal bloom -> decomposition by bacteria -> oxygen depletion", "marks": 2},
        ],
        hints={
            "1_nudge": "Ask: can plant roots absorb insoluble solid rocks directly?",
            "2_concept": "Eutrophication involves nutrient enrichment -> algal bloom -> oxygen depletion during bacterial decay.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_algae_directly_poison_fish_without_oxygen_depletion"],
        marks=3,
        duration=4,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 47: Ore Grade & Percentage Yield Stoichiometry
# =========================================================================== #
def build_47_ore_grade_percentage_yield_stoichiometry(rng: random.Random) -> Dict[str, Any]:
    # Haematite Fe2O3: M = 2(55.85) + 3(16.0) = 159.7 g/mol; Fe content = 111.7 / 159.7 ≈ 69.94%
    ore_tonnes = rng.choice([10, 20, 40, 50])
    purity_pct = rng.choice([60, 70, 80])
    pure_fe2o3 = ore_tonnes * (purity_pct / 100.0)
    fe_mass = round(pure_fe2o3 * (111.7 / 159.7), 2)
    prompt = (
        f"A mining shipment from Sishen contains ${ore_tonnes}\\text{{ tonnes}}$ of iron ore that is ${purity_pct}\\%$ pure haematite "
        f"($\\text{{Fe}}_2\\text{{O}}_3$ by mass).\n\n"
        f"Given $M(\\text{{Fe}}) = 55{{,}}85\\text{{ g·mol}}^{{-1}}$ and $M(\\text{{O}}) = 16{{,}}0\\text{{ g·mol}}^{{-1}}$:\n"
        f"1. Calculate the mass (in tonnes) of pure $\\text{{Fe}}_2\\text{{O}}_3$ present in the shipment.\n"
        f"2. Calculate the maximum mass of pure iron ($\\text{{Fe}}$) that can be extracted assuming $100\\%$ reduction efficiency."
    )
    ans = f"Pure Fe₂O₃ = {_fmt_sa(pure_fe2o3, 1)} t; Maximum Fe = {_fmt_sa(fe_mass, 2)} t"
    sample = (
        f"1. Mass of pure $\\text{{Fe}}_2\\text{{O}}_3 = {ore_tonnes} \\times \\frac{{{purity_pct}}}{{100}} = {_fmt_sa(pure_fe2o3, 1)}\\text{{ tonnes}}$.\n"
        f"2. $M(\\text{{Fe}}_2\\text{{O}}_3) = 2(55{{,}}85) + 3(16{{,}}0) = 159{{,}}7\\text{{ g·mol}}^{{-1}}$.\n"
        f"   Mass fraction of Fe = $\\frac{{111{{,}}7}}{{159{{,}}7}} \\approx 0{{,}}6994$.\n"
        f"   Max Fe = ${_fmt_sa(pure_fe2o3, 1)} \\times \\frac{{111{{,}}7}}{{159{{,}}7}} = {_fmt_sa(fe_mass, 2)}\\text{{ tonnes}}$."
    )
    return _pillars(
        qid=f"ps11_47_{rng.randint(10000, 99999)}",
        subskill="47_ore_grade_percentage_yield_stoichiometry",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Pure Fe2O3 = {_fmt_sa(pure_fe2o3, 1)} t", "marks": 1},
            {"id": "mp2", "desc": "Molar mass Fe2O3 = 159,7 g/mol", "marks": 1},
            {"id": "mp3", "desc": f"Extracted Fe = {_fmt_sa(fe_mass, 2)} t", "marks": 2},
        ],
        hints={
            "1_nudge": "First multiply total ore mass by percentage purity to obtain pure Fe₂O₃ mass.",
            "2_concept": "Multiply pure Fe₂O₃ mass by the mass fraction (2 × M(Fe)) / M(Fe₂O₃).",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_2_atoms_of_Fe_per_Fe2O3_formula_unit"],
        marks=4,
        duration=5,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 48: Fossil Fuels, Coal Formation & Atmospheric Emissions
# =========================================================================== #
def build_48_fossil_fuels_coal_formation_and_energy_resources(rng: random.Random) -> Dict[str, Any]:
    fuels = [
        ("Coal", "ancient terrestrial swamp plant remains compressed under heat and pressure in sedimentary basins", "CO₂ (greenhouse gas) and SO₂ (acid rain)"),
        ("Crude oil (petroleum)", "ancient marine plankton and microorganisms buried beneath ocean sediments", "CO₂, CO, and unburnt hydrocarbons / NOx"),
    ]
    f, origin, emissions = rng.choice(fuels)
    prompt = (
        f"**{f}** is a major non-renewable energy resource extracted from sedimentary strata in the lithosphere.\n\n"
        f"1. Briefly describe the geological origin of **{f}**.\n"
        f"2. Name TWO harmful combustion products released when **{f}** is burned in power stations or engines, and state their environmental impact."
    )
    ans = f"Formed from {origin}; combustion releases {emissions}"
    sample = (
        f"1. **{f}** formed over millions of years from **{origin}**.\n"
        f"2. Combustion releases **{emissions}**, contributing to enhanced global warming (climate change) and acid precipitation."
    )
    return _pillars(
        qid=f"ps11_48_{rng.randint(10000, 99999)}",
        subskill="48_fossil_fuels_coal_formation_and_energy_resources",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Geological origin: {origin}", "marks": 2},
            {"id": "mp2", "desc": f"Emissions and impact: {emissions}", "marks": 2},
        ],
        hints={
            "1_nudge": "Distinguish terrestrial plant origin (coal) from marine plankton origin (crude oil).",
            "2_concept": "Fossil fuels are rich in carbon and trace sulfur impurities.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_coal_forms_from_dinosaurs"],
        marks=4,
        duration=4,
        topic_label="The lithosphere",
        term=4,
    )


# =========================================================================== #
# 49: IMF vs Chemical Bonding Diagnostic Misconception Autopsy
# =========================================================================== #
def build_49_imf_vs_chemical_bonding_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    errors = [
        {
            "claim": "Water boils at a higher temperature than H₂S because the O–H covalent bond inside a water molecule is stronger than the S–H covalent bond.",
            "flaw": "confusing intramolecular covalent bonds with intermolecular forces",
            "repair": "Boiling overcomes intermolecular forces BETWEEN molecules (hydrogen bonding in H₂O vs weaker dipole-dipole in H₂S), NOT covalent bonds inside molecules.",
        },
        {
            "claim": "Carbon dioxide (CO₂) is a polar molecule because the electronegativity difference between C (2,5) and O (3,5) is 1,0.",
            "flaw": "assuming polar covalent bonds automatically produce a polar molecule",
            "repair": "Although each C=O bond is polar, CO₂ is linear and symmetrical so the two equal bond dipoles cancel out, making the overall molecule non-polar.",
        },
        {
            "claim": "Hydrogen sulfide (H₂S) forms hydrogen bonds because it contains hydrogen atoms.",
            "flaw": "assuming any hydrogen-containing molecule forms hydrogen bonds",
            "repair": "Hydrogen bonding only occurs when H is covalently bonded to small, highly electronegative N, O, or F atoms; H₂S only experiences dipole-dipole forces.",
        },
    ]
    err = rng.choice(errors)
    prompt = (
        f"**Diagnostic Error Analysis:** A learner wrote the following statement in a Chemistry test:\n\n"
        f"> *\"{err['claim']}\"*\n\n"
        f"1. Identify the fundamental conceptual misconception in the learner's reasoning.\n"
        f"2. Write the scientifically accurate correction."
    )
    ans = f"Misconception: {err['flaw']}. Correction: {err['repair']}"
    sample = f"1. **Conceptual flaw**: {err['flaw']}.\n2. **Scientific repair**: {err['repair']}"
    return _pillars(
        qid=f"ps11_49_{rng.randint(10000, 99999)}",
        subskill="49_imf_vs_chemical_bonding_diagnostic_autopsy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify flaw: {err['flaw']}", "marks": 1},
            {"id": "mp2", "desc": f"Accurate scientific repair: {err['repair']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Check carefully whether the statement mixes up intramolecular bonds, molecular symmetry, or H-bond criteria.",
            "2_concept": "Phase changes depend on intermolecular forces; overall polarity depends on both bond polarity and VSEPR symmetry.",
            "3_breakdown": sample,
        },
        misconception_tags=["intramolecular_vs_intermolecular_confusion", "polar_bond_equals_polar_molecule"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 50: Grade 11 Chemistry Comprehensive Multi-Step Synthesis
# =========================================================================== #
def build_50_grade11_chemistry_comprehensive_synthesis(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"a": "H₂O", "bpa": 100, "b": "CF₄", "bpb": -128, "salt": "NaCl", "shape_a": "bent / angular", "shape_b": "tetrahedral"},
        {"a": "NH₃", "bpa": -33, "b": "CH₄", "bpb": -164, "salt": "KCl", "shape_a": "trigonal pyramidal", "shape_b": "tetrahedral"},
    ]
    c = rng.choice(cases)
    prompt = (
        f"**Comprehensive Chemistry Synthesis:** Compare pure **{c['a']}** (boiling point ${c['bpa']}^\\circ\\text{{C}}$) and pure **{c['b']}** "
        f"(boiling point ${c['bpb']}^\\circ\\text{{C}}$):\n\n"
        f"1. State the VSEPR molecular shape and overall polarity of both **{c['a']}** and **{c['b']}**.\n"
        f"2. Identify the dominant intermolecular force in each substance and explain the boiling point difference.\n"
        f"3. Explain why ionic **{c['salt']}(s)** dissolves readily in liquid **{c['a']}** but is insoluble in liquid **{c['b']}**."
    )
    ans = (
        f"{c['a']}: {c['shape_a']}, polar, hydrogen bonding; {c['b']}: {c['shape_b']}, non-polar, induced dipole forces; "
        f"{c['salt']} forms strong ion-dipole forces with polar {c['a']}"
    )
    sample = (
        f"1. **{c['a']}** is {c['shape_a']} and **polar**; **{c['b']}** is {c['shape_b']} (symmetrical) and **non-polar**.\n"
        f"2. **{c['a']}** has strong **hydrogen bonding**, whereas **{c['b']}** has weak **induced dipole (London) forces**. "
        f"More energy is needed to overcome hydrogen bonds in {c['a']}, giving a much higher boiling point ({c['bpa']} °C vs {c['bpb']} °C).\n"
        f"3. Ionic {c['salt']} forms strong **ion-dipole forces** with polar {c['a']} molecules, overcoming its ionic lattice, "
        f"whereas non-polar {c['b']} can only form very weak ion-induced dipole interactions."
    )
    return _pillars(
        qid=f"ps11_50_{rng.randint(10000, 99999)}",
        subskill="50_grade11_chemistry_comprehensive_synthesis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"VSEPR shapes & polarities of {c['a']} and {c['b']}", "marks": 2},
            {"id": "mp2", "desc": "Identify H-bonding vs induced dipole and explain BP via energy", "marks": 2},
            {"id": "mp3", "desc": f"Ion-dipole dissolution in {c['a']} vs insolubility in non-polar {c['b']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Integrate VSEPR symmetry, IMF strength, boiling point energy, and ion-dipole solubility.",
            "2_concept": "Like dissolves like: ionic solids dissolve in polar solvents via ion-dipole forces.",
            "3_breakdown": sample,
        },
        misconception_tags=["vsepr_shape_confusion", "imf_classification_error", "confusing_ion_dipole_with_dipole_dipole"],
        marks=6,
        duration=8,
        topic_label="Intermolecular forces",
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_boiling_point_comparison_hydrides_anomaly": build_26_boiling_point_comparison_hydrides_anomaly,
    "27_vapour_pressure_and_evaporation_rate_vs_imf": build_27_vapour_pressure_and_evaporation_rate_vs_imf,
    "28_viscosity_and_chain_length_motor_oils": build_28_viscosity_and_chain_length_motor_oils,
    "29_surface_tension_and_capillarity_imf": build_29_surface_tension_and_capillarity_imf,
    "30_solubility_like_dissolves_like_polarity": build_30_solubility_like_dissolves_like_polarity,
    "31_covalent_network_vs_molecular_melting_points": build_31_covalent_network_vs_molecular_melting_points,
    "32_heating_and_cooling_curve_phase_plateaus": build_32_heating_and_cooling_curve_phase_plateaus,
    "33_density_anomaly_of_ice_and_aquatic_life": build_33_density_anomaly_of_ice_and_aquatic_life,
    "34_water_high_specific_heat_capacity_climate": build_34_water_high_specific_heat_capacity_climate,
    "35_thermal_expansion_and_thermal_conductivity": build_35_thermal_expansion_and_thermal_conductivity,
    "36_earth_concentric_layers_crust_mantle_core": build_36_earth_concentric_layers_crust_mantle_core,
    "37_rock_cycle_igneous_sedimentary_metamorphic": build_37_rock_cycle_igneous_sedimentary_metamorphic,
    "38_igneous_cooling_rate_crystal_size_and_pumice": build_38_igneous_cooling_rate_crystal_size_and_pumice,
    "39_sedimentary_rocks_and_fossil_preservation": build_39_sedimentary_rocks_and_fossil_preservation,
    "40_lithosphere_abundant_minerals_and_formulas": build_40_lithosphere_abundant_minerals_and_formulas,
    "41_south_african_mineral_resources_distribution": build_41_south_african_mineral_resources_distribution,
    "42_gold_mining_cyanidation_process_flowchart": build_42_gold_mining_cyanidation_process_flowchart,
    "43_gold_cyanidation_redox_and_environmental_impact": build_43_gold_cyanidation_redox_and_environmental_impact,
    "44_iron_extraction_blast_furnace_reactions": build_44_iron_extraction_blast_furnace_reactions,
    "45_copper_extraction_and_electrolytic_refining": build_45_copper_extraction_and_electrolytic_refining,
    "46_phosphate_rock_mining_and_fertilisers": build_46_phosphate_rock_mining_and_fertilisers,
    "47_ore_grade_percentage_yield_stoichiometry": build_47_ore_grade_percentage_yield_stoichiometry,
    "48_fossil_fuels_coal_formation_and_energy_resources": build_48_fossil_fuels_coal_formation_and_energy_resources,
    "49_imf_vs_chemical_bonding_diagnostic_autopsy": build_49_imf_vs_chemical_bonding_diagnostic_autopsy,
    "50_grade11_chemistry_comprehensive_synthesis": build_50_grade11_chemistry_comprehensive_synthesis,
}
