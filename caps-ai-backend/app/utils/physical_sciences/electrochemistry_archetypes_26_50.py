"""Grade 11 Physical Sciences — Activation Energy, Activated Complex & Catalysis (Subskills 26–50).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/02. Energy and chemical change.md

Covers:
- Activation energy (Ea), activated complex (transition state), forward & reverse activation energies
- Exothermic and endothermic potential energy vs reaction coordinate profiles (with inline SVGs)
- Catalyst effects (alternative lower-Ea pathway, enzyme catalysis in cellular respiration, catalytic converters)
- Invariance of E_reactants, E_products, and ΔH under catalysis; inhibitors raising Ea
- Multi-step transition state profiles, Maxwell-Boltzmann kinetic thresholds, lab temperature-time profiles
- Coupled photosynthesis/respiration cycles, diagnostic misconception autopsy, and comprehensive exam synthesis.

Zero-LLM: 100% deterministic Python with seed-varied parameters, South African comma decimals, and inline SVG diagrams.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from app.utils.physical_sciences.electrochemistry_archetypes_01_25 import (
    _fmt_sa,
    _pillars,
    _svg_wrap,
)


def _pe_curve_svg(
    e_r: int,
    e_peak: int,
    e_p: int,
    title: str,
    cat_peak: int | None = None,
) -> str:
    """Draw a seeded exothermic or endothermic potential energy profile SVG."""
    is_exo = e_p < e_r
    y_r = 95 if is_exo else 145
    y_p = 155 if is_exo else 85
    y_peak = 35
    cat_markup = ""
    if cat_peak is not None:
        cat_markup = (
            f'<path d="M 55 {y_r} C 120 {y_r}, 140 65, 185 65 C 230 65, 250 {y_p}, 315 {y_p}" '
            f'fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="5,4"/>'
            f'<text x="185" y="79" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#15803d">Catalysed ({cat_peak} kJ)</text>'
        )
    return _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="185" x2="345" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="12" y="25" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Ep (kJ)</text>'
        f'<text x="275" y="202" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Course of reaction</text>'
        f'<line x1="50" y1="{y_r}" x2="95" y2="{y_r}" stroke="#334155" stroke-width="2.5"/>'
        f'<line x1="275" y1="{y_p}" x2="330" y2="{y_p}" stroke="#334155" stroke-width="2.5"/>'
        f'<path d="M 95 {y_r} C 135 {y_r}, 145 {y_peak}, 185 {y_peak} C 225 {y_peak}, 235 {y_p}, 275 {y_p}" '
        f'fill="none" stroke="#2563eb" stroke-width="2.8"/>'
        f'{cat_markup}'
        f'<circle cx="185" cy="{y_peak}" r="4" fill="#dc2626"/>'
        f'<text x="185" y="26" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Peak: {e_peak} kJ</text>'
        f'<text x="72" y="{y_r - 8}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">R ({e_r} kJ)</text>'
        f'<text x="302" y="{y_p - 8}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">P ({e_p} kJ)</text>'
        f'<text x="195" y="176" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#475569">{title}</text>',
        width=360,
        height=215,
    )


# =========================================================================== #
# 26: Activation Energy Definition & Ignition
# =========================================================================== #
def build_26_activation_energy_definition_and_ignition(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("striking a match on a rough matchbox strip", "friction supplies the initial kinetic/heat energy needed to reach activation energy"),
        ("igniting magnesium ribbon in air with a Bunsen burner", "initial heating supplies activation energy to break O=O bonds and start exothermic combustion"),
        ("igniting methane gas in a stove with a spark", "the spark supplies the minimum energy required to initiate bond breaking"),
    ]
    ex, mech = rng.choice(examples)
    prompt = (
        f"Even though **{ex}** triggers a strongly exothermic reaction ($\\Delta H < 0$), the reactants remain stable at room temperature until initiated.\n\n"
        f"1. Define **activation energy ($E_a$)**.\n"
        f"2. Explain why an exothermic reaction still requires this initial energy input to start."
    )
    ans = f"Minimum energy needed to start a chemical reaction; {mech} to form the activated complex"
    sample = (
        f"1. **Activation energy ($E_a$)** is the minimum amount of energy required to start a chemical reaction (to raise reactant energy to the activated complex).\n"
        f"2. Before new product bonds can form and release energy, reactant bonds must first begin breaking; {mech}."
    )
    return _pillars(
        qid=f"ps11_e26_{rng.randint(10000, 99999)}",
        subskill="26_activation_energy_definition_and_ignition",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: minimum energy needed to start a chemical reaction", "marks": 2},
            {"id": "mp2", "desc": "Initial energy required to stretch/break reactant bonds and form activated complex", "marks": 1},
        ],
        hints={
            "1_nudge": "Every chemical reaction begins by overcoming an energy barrier before products can form.",
            "2_concept": "Activation energy is the barrier between reactants and the activated complex.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_exothermic_reactions_have_zero_activation_energy"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 27: Activated Complex (Transition State) Properties
# =========================================================================== #
def build_27_activated_complex_transition_state_properties(rng: random.Random) -> Dict[str, Any]:
    rxns = [
        ("H₂(g) + F₂(g) → 2HF(g)", "[H···H···F···F]‡", "H–H and F–F bonds are partially breaking as H–F bonds form"),
        ("H₂(g) + Cl₂(g) → 2HCl(g)", "[H···H···Cl···Cl]‡", "H–H and Cl–Cl bonds are stretching while new H–Cl bonds begin forming"),
        ("CO(g) + NO₂(g) → CO₂(g) + NO(g)", "[O–C···O···N–O]‡", "N–O bond breaks simultaneously as the new C–O bond forms"),
    ]
    eq, ts, desc = rng.choice(rxns)
    prompt = (
        f"Consider the elementary reaction: $${eq}$$\n\n"
        f"1. Define the **activated complex** (represented provisionally as ${ts}$).\n"
        f"2. State where the activated complex is located on a potential energy graph and describe its lifetime and stability."
    )
    ans = f"Short-lived, unstable high-energy transition state at maximum potential energy where {desc}"
    sample = (
        f"1. The **activated complex** is the temporary, unstable transition state formed as reactant bonds are breaking simultaneously while product bonds are forming ({desc}).\n"
        f"2. It is located at the **maximum peak** of the potential energy profile and exists for only an extremely short time before collapsing to either products or reactants."
    )
    return _pillars(
        qid=f"ps11_e27_{rng.randint(10000, 99999)}",
        subskill="27_activated_complex_transition_state_properties",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "High-energy temporary transition state where bonds break and form simultaneously", "marks": 2},
            {"id": "mp2", "desc": "Located at maximum energy peak; unstable / short-lived", "marks": 2},
        ],
        hints={
            "1_nudge": "Look at the highest point of a potential energy curve.",
            "2_concept": "The activated complex is neither pure reactants nor pure products; it is an unstable intermediate configuration.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_activated_complex_with_final_product_or_catalyst"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 28: Reading Exothermic Potential Energy Profile (Inline SVG)
# =========================================================================== #
def build_28_exothermic_potential_energy_profile_reading(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([45, 55, 65, 75])
    e_p = e_r - rng.choice([25, 35, 40])
    e_peak = e_r + rng.choice([45, 58, 70])
    dh = e_p - e_r
    ea = e_peak - e_r
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Exothermic Profile (R={e_r}, P={e_p})")
    prompt = (
        f"Refer to the potential energy vs reaction coordinate graph (reactants $E_R = {e_r}\\text{{ kJ}}$, "
        f"activated complex peak $= {e_peak}\\text{{ kJ}}$, products $E_P = {e_p}\\text{{ kJ}}$).\n\n"
        f"1. Calculate the heat of reaction ($\\Delta H$) and state whether the reaction is exothermic or endothermic.\n"
        f"2. Calculate the activation energy ($E_a$) for this forward reaction."
    )
    ans = f"ΔH = {dh} kJ (exothermic); Ea = {ea} kJ"
    sample = (
        f"1. $\\Delta H = E_P - E_R = {e_p} - {e_r} = {dh}\\text{{ kJ}}$ (**exothermic**, since $\\Delta H < 0$).\n"
        f"2. $E_a = E_{{\\text{{peak}}}} - E_R = {e_peak} - {e_r} = {ea}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e28_{rng.randint(10000, 99999)}",
        subskill="28_exothermic_potential_energy_profile_reading",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"ΔH = {e_p} - {e_r} = {dh} kJ (exothermic)", "marks": 2},
            {"id": "mp2", "desc": f"Ea = {e_peak} - {e_r} = {ea} kJ", "marks": 2},
        ],
        hints={
            "1_nudge": "ΔH is the vertical distance from reactants to products (E_P - E_R); Ea is from reactants to peak.",
            "2_concept": "Always subtract reactant energy from peak energy for forward Ea.",
            "3_breakdown": sample,
        },
        misconception_tags=["reporting_Ea_as_peak_height_from_zero", "writing_positive_ΔH_for_exothermic"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Exothermic PE profile (R={e_r}, Peak={e_peak}, P={e_p})"},
    )


# =========================================================================== #
# 29: Reading Endothermic Potential Energy Profile (Inline SVG)
# =========================================================================== #
def build_29_endothermic_potential_energy_profile_reading(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([20, 30, 40])
    e_p = e_r + rng.choice([35, 50, 65])
    e_peak = e_p + rng.choice([25, 40, 55])
    dh = e_p - e_r
    ea = e_peak - e_r
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Endothermic Profile (R={e_r}, P={e_p})")
    prompt = (
        f"Refer to the potential energy profile (reactants $= {e_r}\\text{{ kJ}}$, products $= {e_p}\\text{{ kJ}}$, "
        f"transition peak $= {e_peak}\\text{{ kJ}}$).\n\n"
        f"1. Calculate $\\Delta H$ and classify the reaction as exothermic or endothermic.\n"
        f"2. Calculate the activation energy ($E_a$) of the forward reaction."
    )
    ans = f"ΔH = +{dh} kJ (endothermic); Ea = {ea} kJ"
    sample = (
        f"1. $\\Delta H = E_P - E_R = {e_p} - {e_r} = +{dh}\\text{{ kJ}}$ (**endothermic**, since $\\Delta H > 0$).\n"
        f"2. $E_a = E_{{\\text{{peak}}}} - E_R = {e_peak} - {e_r} = {ea}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e29_{rng.randint(10000, 99999)}",
        subskill="29_endothermic_potential_energy_profile_reading",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"ΔH = +{dh} kJ (endothermic)", "marks": 2},
            {"id": "mp2", "desc": f"Ea = {e_peak} - {e_r} = {ea} kJ", "marks": 2},
        ],
        hints={
            "1_nudge": "Products sit higher than reactants on an endothermic potential energy curve.",
            "2_concept": "Ea = E(activated complex) - E(reactants).",
            "3_breakdown": sample,
        },
        misconception_tags=["calculating_Ea_from_products_instead_of_reactants"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Endothermic PE profile (R={e_r}, Peak={e_peak}, P={e_p})"},
    )


# =========================================================================== #
# 30: Calculate Activated Complex Energy from Ea
# =========================================================================== #
def build_30_calculate_activated_complex_energy_from_Ea(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([35, 50, 75, 90])
    ea = rng.choice([40, 65, 85, 110])
    e_peak = e_r + ea
    prompt = (
        f"In a reaction coordinate study, the reactants possess a potential energy of ${e_r}\\text{{ kJ·mol}}^{{-1}}$ "
        f"and the forward activation energy barrier is $E_a = {ea}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"Calculate the potential energy of the **activated complex**."
    )
    ans = f"{e_peak} kJ/mol"
    sample = f"$E_{{\\text{{activated complex}}}} = E_{{\\text{{reactants}}}} + E_a = {e_r} + {ea} = {e_peak}\\text{{ kJ·mol}}^{{-1}}$."
    return _pillars(
        qid=f"ps11_e30_{rng.randint(10000, 99999)}",
        subskill="30_calculate_activated_complex_energy_from_Ea",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Formula E(activated complex) = E(reactants) + Ea", "marks": 1},
            {"id": "mp2", "desc": f"Result = {e_peak} kJ/mol", "marks": 2},
        ],
        hints={
            "1_nudge": "Start at the reactant energy level and climb up by Ea to reach the peak.",
            "2_concept": "E_peak = E_reactants + Ea.",
            "3_breakdown": sample,
        },
        misconception_tags=["subtracting_Ea_from_E_reactants"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 31: Calculate Product Energy from ΔH
# =========================================================================== #
def build_31_calculate_product_energy_from_deltaH(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([120, 150, 200])
    dh = rng.choice([-85, -55, 65, 95])
    e_p = e_r + dh
    sign_dh = f"+{dh}" if dh > 0 else str(dh)
    prompt = (
        f"For a chemical reaction, the reactants have potential energy ${e_r}\\text{{ kJ·mol}}^{{-1}}$ "
        f"and the enthalpy change is $\\Delta H = {sign_dh}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"Calculate the potential energy of the **products** ($E_{{\\text{{products}}}}$)."
    )
    ans = f"{e_p} kJ/mol"
    sample = f"$\\Delta H = E_{{\\text{{prod}}}} - E_{{\\text{{react}}}} \\implies E_{{\\text{{prod}}}} = {e_r} + ({sign_dh}) = {e_p}\\text{{ kJ·mol}}^{{-1}}$."
    return _pillars(
        qid=f"ps11_e31_{rng.randint(10000, 99999)}",
        subskill="31_calculate_product_energy_from_deltaH",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Rearrange ΔH = E_prod - E_react -> E_prod = E_react + ΔH", "marks": 1},
            {"id": "mp2", "desc": f"E_products = {e_p} kJ/mol", "marks": 2},
        ],
        hints={
            "1_nudge": "Substitute into ΔH = E_prod - E_react.",
            "2_concept": "Products are lower than reactants if ΔH < 0, and higher if ΔH > 0.",
            "3_breakdown": sample,
        },
        misconception_tags=["ignoring_sign_of_ΔH_when_finding_E_prod"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 32: Reverse Activation Energy — Exothermic Profile (Inline SVG)
# =========================================================================== #
def build_32_reverse_reaction_activation_energy_exothermic(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([70, 90, 110])
    e_p = e_r - rng.choice([30, 45])
    e_peak = e_r + rng.choice([40, 60])
    ea_fwd = e_peak - e_r
    ea_rev = e_peak - e_p
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Reverse Ea Exothermic (Peak={e_peak})")
    prompt = (
        f"Refer to the exothermic potential energy profile ($E_R = {e_r}\\text{{ kJ}}$, $E_{{\\text{{peak}}}} = {e_peak}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$).\n\n"
        f"1. Calculate the activation energy for the **forward** reaction ($E_{{a,\\text{{fwd}}}}$).\n"
        f"2. Calculate the activation energy for the **reverse** reaction ($E_{{a,\\text{{rev}}}}$) and compare the two barriers."
    )
    ans = f"Ea(fwd) = {ea_fwd} kJ; Ea(rev) = {ea_rev} kJ; Ea(rev) > Ea(fwd)"
    sample = (
        f"1. $E_{{a,\\text{{fwd}}}} = {e_peak} - {e_r} = {ea_fwd}\\text{{ kJ}}$.\n"
        f"2. $E_{{a,\\text{{rev}}}} = E_{{\\text{{peak}}}} - E_P = {e_peak} - {e_p} = {ea_rev}\\text{{ kJ}}$.\n"
        f"   Because the forward reaction is exothermic ($E_P < E_R$), the reverse reaction must climb a larger barrier ($E_{{a,\\text{{rev}}}} > E_{{a,\\text{{fwd}}}}$)."
    )
    return _pillars(
        qid=f"ps11_e32_{rng.randint(10000, 99999)}",
        subskill="32_reverse_reaction_activation_energy_exothermic",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Ea(fwd) = {ea_fwd} kJ", "marks": 1},
            {"id": "mp2", "desc": f"Ea(rev) = {e_peak} - {e_p} = {ea_rev} kJ", "marks": 2},
            {"id": "mp3", "desc": "Conclude Ea(rev) > Ea(fwd)", "marks": 1},
        ],
        hints={
            "1_nudge": "For the reverse reaction, the products P act as the starting level up to the same transition peak.",
            "2_concept": "Ea(rev) = E(activated complex) - E(products).",
            "3_breakdown": sample,
        },
        misconception_tags=["using_E_reactants_for_reverse_activation_energy"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Exothermic reverse Ea (R={e_r}, Peak={e_peak}, P={e_p})"},
    )


# =========================================================================== #
# 33: Reverse Activation Energy — Endothermic Profile (Inline SVG)
# =========================================================================== #
def build_33_reverse_reaction_activation_energy_endothermic(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([25, 40, 55])
    e_p = e_r + rng.choice([45, 60])
    e_peak = e_p + rng.choice([30, 50])
    ea_fwd = e_peak - e_r
    ea_rev = e_peak - e_p
    dh = e_p - e_r
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Reverse Ea Endothermic (Peak={e_peak})")
    prompt = (
        f"Refer to the endothermic potential energy diagram ($E_R = {e_r}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$, $E_{{\\text{{peak}}}} = {e_peak}\\text{{ kJ}}$).\n\n"
        f"1. Calculate the activation energy of the **reverse** reaction ($E_{{a,\\text{{rev}}}}$).\n"
        f"2. Calculate $\\Delta H$ for the reverse reaction and verify that $\\Delta H_{{\\text{{fwd}}}} = E_{{a,\\text{{fwd}}}} - E_{{a,\\text{{rev}}}}$."
    )
    ans = f"Ea(rev) = {ea_rev} kJ; ΔH(rev) = -{dh} kJ; {ea_fwd} - {ea_rev} = +{dh} kJ"
    sample = (
        f"1. $E_{{a,\\text{{rev}}}} = {e_peak} - {e_p} = {ea_rev}\\text{{ kJ}}$.\n"
        f"2. $\\Delta H_{{\\text{{rev}}}} = {e_r} - {e_p} = -{dh}\\text{{ kJ}}$.\n"
        f"   Check: $E_{{a,\\text{{fwd}}}} - E_{{a,\\text{{rev}}}} = {ea_fwd} - {ea_rev} = +{dh}\\text{{ kJ}} = \\Delta H_{{\\text{{fwd}}}}$."
    )
    return _pillars(
        qid=f"ps11_e33_{rng.randint(10000, 99999)}",
        subskill="33_reverse_reaction_activation_energy_endothermic",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Ea(rev) = {ea_rev} kJ", "marks": 2},
            {"id": "mp2", "desc": f"ΔH(rev) = -{dh} kJ and verify identity", "marks": 2},
        ],
        hints={
            "1_nudge": "Reverse reaction starts at P and ends at R via the same peak.",
            "2_concept": "ΔH(fwd) always equals Ea(fwd) - Ea(rev).",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_negative_sign_for_reverse_of_endothermic"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Endothermic reverse Ea (R={e_r}, Peak={e_peak}, P={e_p})"},
    )


# =========================================================================== #
# 34: Forward vs Reverse ΔH = Ea(fwd) - Ea(rev) Identity
# =========================================================================== #
def build_34_forward_vs_reverse_deltaH_symmetry(rng: random.Random) -> Dict[str, Any]:
    ea_fwd = rng.choice([55, 70, 95, 130])
    ea_rev = rng.choice([40, 85, 120])
    while ea_fwd == ea_rev:
        ea_rev += 25
    dh_fwd = ea_fwd - ea_rev
    kind = "exothermic" if dh_fwd < 0 else "endothermic"
    prompt = (
        f"For a reversible reaction $A + B \\rightleftharpoons C + D$, the forward activation energy is "
        f"$E_{{a,\\text{{fwd}}}} = {ea_fwd}\\text{{ kJ·mol}}^{{-1}}$ and the reverse activation energy is "
        f"$E_{{a,\\text{{rev}}}} = {ea_rev}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"1. Calculate $\\Delta H$ for the forward reaction.\n"
        f"2. State whether the forward reaction is exothermic or endothermic."
    )
    sign_s = f"+{dh_fwd}" if dh_fwd > 0 else str(dh_fwd)
    ans = f"ΔH = {sign_s} kJ/mol ({kind})"
    sample = (
        f"1. $\\Delta H_{{\\text{{fwd}}}} = E_{{a,\\text{{fwd}}}} - E_{{a,\\text{{rev}}}} = {ea_fwd} - {ea_rev} = {sign_s}\\text{{ kJ·mol}}^{{-1}}$.\n"
        f"2. Because $\\Delta H {'<' if dh_fwd < 0 else '>'} 0$, the forward reaction is **{kind}**."
    )
    return _pillars(
        qid=f"ps11_e34_{rng.randint(10000, 99999)}",
        subskill="34_forward_vs_reverse_deltaH_symmetry",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Apply ΔH = Ea(fwd) - Ea(rev) = {sign_s} kJ/mol", "marks": 2},
            {"id": "mp2", "desc": f"Classify as {kind}", "marks": 1},
        ],
        hints={
            "1_nudge": "Relate both activation energies to the common activated complex peak.",
            "2_concept": "ΔH(fwd) = Ea(fwd) - Ea(rev).",
            "3_breakdown": sample,
        },
        misconception_tags=["adding_Ea_fwd_and_Ea_rev"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 35: Matching Reaction Coordinate Curves (Inline SVG)
# =========================================================================== #
def build_35_sketching_and_identifying_reaction_coordinate_curves(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        {"rxn": "2NO₂(g) → N₂O₄(g)   (ΔH = -57 kJ·mol⁻¹)", "kind": "exothermic", "er": 90, "ep": 33, "peak": 125},
        {"rxn": "N₂(g) + O₂(g) → 2NO(g)   (ΔH = +181 kJ·mol⁻¹)", "kind": "endothermic", "er": 40, "ep": 221, "peak": 290},
    ]
    s = rng.choice(scenarios)
    svg = _pe_curve_svg(s["er"], s["peak"], s["ep"], f"{s['kind'].capitalize()} Curve ({s['rxn'].split('(')[0].strip()})")
    prompt = (
        f"Refer to the potential energy curve for the reaction $${s['rxn']}$$\n\n"
        f"1. Explain why the curve rises to a peak before reaching the final product energy level.\n"
        f"2. State whether $E_{{\\text{{products}}}}$ lies above or below $E_{{\\text{{reactants}}}}$ on this curve and justify."
    )
    pos = "below" if s["kind"] == "exothermic" else "above"
    ans = f"Peak represents activation energy / activated complex; E_products lies {pos} E_reactants ({s['kind']})"
    sample = (
        f"1. Reactants must first absorb **activation energy ($E_a$)** to reach the high-energy **activated complex** peak so bonds can rearrange.\n"
        f"2. Because the reaction is **{s['kind']}** ($\\Delta H {'<' if pos == 'below' else '>'} 0$), $E_{{\\text{{products}}}}$ lies **{pos}** $E_{{\\text{{reactants}}}}$."
    )
    return _pillars(
        qid=f"ps11_e35_{rng.randint(10000, 99999)}",
        subskill="35_sketching_and_identifying_reaction_coordinate_curves",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Curve rises to supply Ea and form activated complex", "marks": 2},
            {"id": "mp2", "desc": f"Products lie {pos} reactants ({s['kind']})", "marks": 1},
        ],
        hints={
            "1_nudge": "A straight line from R to P is incorrect because reactions have an activation energy barrier.",
            "2_concept": "Exothermic -> products lower than reactants; Endothermic -> products higher than reactants.",
            "3_breakdown": sample,
        },
        misconception_tags=["drawing_straight_line_without_activation_barrier"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Reaction coordinate curve ({s['kind']}, R={s['er']})"},
    )


# =========================================================================== #
# 36: Catalyst Effect on Activation Energy (Inline SVG)
# =========================================================================== #
def build_36_catalyst_effect_on_activation_energy(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([60, 80, 100])
    e_p = e_r - rng.choice([30, 40])
    e_peak = e_r + rng.choice([60, 75])
    cat_peak = e_peak - rng.choice([25, 35])
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Catalyst Pathway (Peak {e_peak} -> {cat_peak})", cat_peak=cat_peak)
    prompt = (
        f"Refer to the potential energy graph showing the uncatalysed reaction (peak ${e_peak}\\text{{ kJ}}$) and "
        f"the green dashed pathway with a suitable catalyst added (peak ${cat_peak}\\text{{ kJ}}$).\n\n"
        f"1. Define a **catalyst**.\n"
        f"2. Explain how the catalyst increases the rate of the reaction in terms of activation energy."
    )
    ans = f"Substance that increases reaction rate without being consumed by providing an alternative pathway with lower Ea ({cat_peak - e_r} kJ vs {e_peak - e_r} kJ)"
    sample = (
        f"1. A **catalyst** is a substance that increases the rate of a chemical reaction without undergoing a permanent chemical change itself.\n"
        f"2. It provides an **alternative reaction pathway with lower activation energy** (lowering $E_a$ from {e_peak - e_r} kJ to {cat_peak - e_r} kJ), "
        f"allowing more colliding particles to overcome the barrier per unit time."
    )
    return _pillars(
        qid=f"ps11_e36_{rng.randint(10000, 99999)}",
        subskill="36_catalyst_effect_on_activation_energy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: speeds up reaction without being permanently consumed", "marks": 2},
            {"id": "mp2", "desc": "Provides alternative pathway with lower activation energy", "marks": 2},
        ],
        hints={
            "1_nudge": "Compare the heights of the blue uncatalysed peak and green catalysed peak.",
            "2_concept": "Catalysts lower the activation energy barrier via an alternative mechanism.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_catalyst_gives_reactants_more_kinetic_energy"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Catalysed vs uncatalysed PE curve ({e_peak} vs {cat_peak})"},
    )


# =========================================================================== #
# 37: Catalyst Invariance of ΔH, Reactants & Products (Inline SVG)
# =========================================================================== #
def build_37_catalyst_invariance_of_deltaH_reactants_products(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([50, 70])
    e_p = e_r - 30
    e_peak = e_r + 65
    cat_peak = e_r + 35
    dh = e_p - e_r
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"ΔH Invariance ({dh} kJ)", cat_peak=cat_peak)
    prompt = (
        f"Refer to the potential energy diagram comparing uncatalysed and catalysed reaction pathways ($E_R = {e_r}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$).\n\n"
        f"1. State the value of $\\Delta H$ **before** and **after** adding the catalyst.\n"
        f"2. List THREE quantities on this energy profile that remain **unchanged** when a catalyst is added."
    )
    ans = f"ΔH = {dh} kJ both before and after; E_reactants, E_products, and ΔH remain unchanged"
    sample = (
        f"1. $\\Delta H = {e_p} - {e_r} = {dh}\\text{{ kJ}}$ both before and after adding the catalyst.\n"
        f"2. Unchanged quantities: (i) potential energy of reactants ($E_R$), (ii) potential energy of products ($E_P$), "
        f"and (iii) overall heat of reaction ($\\Delta H$)."
    )
    return _pillars(
        qid=f"ps11_e37_{rng.randint(10000, 99999)}",
        subskill="37_catalyst_invariance_of_deltaH_reactants_products",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"ΔH = {dh} kJ before and after", "marks": 1},
            {"id": "mp2", "desc": "Three unchanged quantities: E_reactants, E_products, ΔH", "marks": 3},
        ],
        hints={
            "1_nudge": "Does the catalyst change where the solid horizontal R and P lines start or end?",
            "2_concept": "Catalysts lower the peak (activated complex and Ea), leaving R, P, and ΔH strictly unchanged.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_catalyst_makes_ΔH_more_negative"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Catalyst ΔH invariance ({dh} kJ)"},
    )


# =========================================================================== #
# 38: Calculating Catalysed Forward & Reverse Ea (Inline SVG)
# =========================================================================== #
def build_38_calculating_catalyzed_Ea_and_reverse_Ea(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([80, 100, 120])
    e_p = e_r - rng.choice([30, 40])
    e_peak = e_r + rng.choice([70, 80])
    drop = rng.choice([25, 30])
    cat_peak = e_peak - drop
    ea_cat_fwd = cat_peak - e_r
    ea_cat_rev = cat_peak - e_p
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Catalysed drop = {drop} kJ", cat_peak=cat_peak)
    prompt = (
        f"Refer to the potential energy profile ($E_R = {e_r}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$, uncatalysed peak $= {e_peak}\\text{{ kJ}}$).\n"
        f"Adding a catalyst lowers the activation energy barrier by ${drop}\\text{{ kJ}}$.\n\n"
        f"1. Calculate the **catalysed forward activation energy** ($E_{{a,\\text{{fwd,cat}}}}$).\n"
        f"2. Calculate the **catalysed reverse activation energy** ($E_{{a,\\text{{rev,cat}}}}$)."
    )
    ans = f"Ea(fwd,cat) = {ea_cat_fwd} kJ; Ea(rev,cat) = {ea_cat_rev} kJ"
    sample = (
        f"1. New catalysed peak energy = ${e_peak} - {drop} = {cat_peak}\\text{{ kJ}}$.\n"
        f"   $E_{{a,\\text{{fwd,cat}}}} = {cat_peak} - {e_r} = {ea_cat_fwd}\\text{{ kJ}}$.\n"
        f"2. $E_{{a,\\text{{rev,cat}}}} = {cat_peak} - {e_p} = {ea_cat_rev}\\text{{ kJ}}$ (notice both forward and reverse barriers drop by {drop} kJ!)."
    )
    return _pillars(
        qid=f"ps11_e38_{rng.randint(10000, 99999)}",
        subskill="38_calculating_catalyzed_Ea_and_reverse_Ea",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Catalysed peak = {cat_peak} kJ", "marks": 1},
            {"id": "mp2", "desc": f"Ea(fwd,cat) = {ea_cat_fwd} kJ", "marks": 2},
            {"id": "mp3", "desc": f"Ea(rev,cat) = {ea_cat_rev} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "A catalyst lowers the transition state peak by the same amount for BOTH forward and reverse reactions.",
            "2_concept": "Subtract E_R from the catalysed peak for forward; subtract E_P for reverse.",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_catalyst_only_lowers_forward_Ea_not_reverse"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Catalysed forward/reverse Ea (drop={drop})"},
    )


# =========================================================================== #
# 39: Inhibitor (Negative Catalyst) Energy Barrier (Inline SVG)
# =========================================================================== #
def build_39_inhibitor_negative_catalyst_energy_profile(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([60, 80])
    e_p = e_r - 25
    e_peak = e_r + rng.choice([45, 55])
    inh_peak = e_peak + rng.choice([25, 35])
    svg = _pe_curve_svg(e_r, inh_peak, e_p, f"Inhibited peak = {inh_peak} kJ (Normal {e_peak} kJ)")
    prompt = (
        f"Refer to the reaction energy diagram where adding a chemical **inhibitor** (negative catalyst) shifts the transition peak "
        f"from ${e_peak}\\text{{ kJ}}$ up to ${inh_peak}\\text{{ kJ}}$ ($E_R = {e_r}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$).\n\n"
        f"1. Calculate the increase in activation energy caused by the inhibitor.\n"
        f"2. Explain what happens to the reaction rate and to $\\Delta H$ when the inhibitor is added."
    )
    ans = f"Ea increases by {inh_peak - e_peak} kJ (to {inh_peak - e_r} kJ); reaction rate decreases; ΔH remains {e_p - e_r} kJ"
    sample = (
        f"1. Uninhibited $E_a = {e_peak - e_r}\\text{{ kJ}}$; Inhibited $E_a = {inh_peak - e_r}\\text{{ kJ}}$ (increase of ${inh_peak - e_peak}\\text{{ kJ}}$).\n"
        f"2. Fewer colliding molecules possess enough energy to surmount the higher barrier, so **reaction rate decreases**, while $\\Delta H$ stays constant at ${e_p - e_r}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e39_{rng.randint(10000, 99999)}",
        subskill="39_inhibitor_negative_catalyst_energy_profile",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Increase in Ea = {inh_peak - e_peak} kJ", "marks": 1},
            {"id": "mp2", "desc": "Reaction rate decreases due to higher energy barrier", "marks": 1},
            {"id": "mp3", "desc": f"ΔH remains unchanged ({e_p - e_r} kJ)", "marks": 1},
        ],
        hints={
            "1_nudge": "An inhibitor works opposite to a catalyst by blocking the low-energy pathway.",
            "2_concept": "Higher Ea -> slower reaction rate; ΔH is unaffected.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_inhibitor_changes_final_product_energy"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Inhibitor energy barrier ({e_peak} -> {inh_peak})"},
    )


# =========================================================================== #
# 40: Comparing Ea and Reaction Feasibility at Room Temperature
# =========================================================================== #
def build_40_comparing_Ea_and_reaction_feasibility(rng: random.Random) -> Dict[str, Any]:
    ea_a = rng.choice([25, 35, 45])
    ea_b = rng.choice([180, 220, 260])
    prompt = (
        f"Two exothermic reactions take place at $25^\\circ\\text{{C}}$ with equal initial reactant concentrations:\n"
        f"- **Reaction A**: $E_a = {ea_a}\\text{{ kJ·mol}}^{{-1}}$, $\\Delta H = -90\\text{{ kJ·mol}}^{{-1}}$\n"
        f"- **Reaction B**: $E_a = {ea_b}\\text{{ kJ·mol}}^{{-1}}$, $\\Delta H = -450\\text{{ kJ·mol}}^{{-1}}$\n\n"
        f"Which reaction proceeds faster at $25^\\circ\\text{{C}}$ without external heating? Explain using activation energy."
    )
    ans = f"Reaction A proceeds faster because its activation energy ({ea_a} kJ/mol) is much lower than Reaction B ({ea_b} kJ/mol)"
    sample = (
        f"**Reaction A** proceeds much faster at $25^\\circ\\text{{C}}$ because its activation energy ($E_a = {ea_a}\\text{{ kJ·mol}}^{{-1}}$) is far smaller than that of Reaction B "
        f"($E_a = {ea_b}\\text{{ kJ·mol}}^{{-1}}$). Reaction rate depends on the height of the $E_a$ barrier, not the magnitude of $\\Delta H$."
    )
    return _pillars(
        qid=f"ps11_e40_{rng.randint(10000, 99999)}",
        subskill="40_comparing_Ea_and_reaction_feasibility",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Select Reaction A", "marks": 1},
            {"id": "mp2", "desc": "Smaller Ea allows more effective collisions at 25 °C; rate is independent of |ΔH|", "marks": 2},
        ],
        hints={
            "1_nudge": "Do not confuse how much heat a reaction releases (ΔH) with how fast it starts (Ea).",
            "2_concept": "Lower activation energy means a larger fraction of collisions can cross the barrier at 25 °C.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_more_negative_ΔH_always_means_faster_reaction"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 41: Collision Theory & Minimum Kinetic Energy Threshold
# =========================================================================== #
def build_41_maxwell_boltzmann_collision_energy_intro(rng: random.Random) -> Dict[str, Any]:
    temp_low = rng.choice([20, 25])
    temp_high = temp_low + rng.choice([20, 30])
    prompt = (
        f"A chemical reaction with activation energy $E_a = 75\\text{{ kJ·mol}}^{{-1}}$ is studied first at ${temp_low}^\\circ\\text{{C}}$ and then at ${temp_high}^\\circ\\text{{C}}$.\n\n"
        f"1. State the two conditions required for a collision between reactant particles to be **effective**.\n"
        f"2. Explain what happens to the **value of $E_a$** and to the **fraction of particles with $E_k \\ge E_a$** when temperature increases from ${temp_low}^\\circ\\text{{C}}$ to ${temp_high}^\\circ\\text{{C}}$."
    )
    ans = f"Minimum energy (>= Ea) + correct orientation; Ea remains unchanged while fraction of particles with Ek >= Ea increases"
    sample = (
        f"1. Colliding particles must have (i) **kinetic energy equal to or greater than $E_a$** and (ii) **correct spatial orientation**.\n"
        f"2. Raising the temperature does **not** change $E_a$ (still 75 kJ·mol⁻¹), but increases average kinetic energy so a much larger fraction of collisions have $E_k \\ge E_a$."
    )
    return _pillars(
        qid=f"ps11_e41_{rng.randint(10000, 99999)}",
        subskill="41_maxwell_boltzmann_collision_energy_intro",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Two conditions: Ek >= Ea and correct orientation", "marks": 2},
            {"id": "mp2", "desc": "Ea stays constant; fraction of particles >= Ea increases with temperature", "marks": 2},
        ],
        hints={
            "1_nudge": "Temperature shifts particle energies upward, NOT the activation energy barrier downward.",
            "2_concept": "Only a catalyst lowers Ea; heating helps more particles climb the same Ea.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_higher_temperature_lowers_activation_energy"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 42: Multi-Step Energy Diagram — Intermediate & Rate-Determining Step (Inline SVG)
# =========================================================================== #
def build_42_multi_step_energy_diagram_intermediate_and_rds(rng: random.Random) -> Dict[str, Any]:
    e_r = 40
    peak1 = rng.choice([110, 130])
    e_int = rng.choice([70, 80])
    peak2 = rng.choice([145, 165])
    e_p = 20
    ea1 = peak1 - e_r
    ea2 = peak2 - e_int
    rds = "Step 1" if ea1 > ea2 else "Step 2"
    svg = _svg_wrap(
        f'<line x1="45" y1="20" x2="45" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="45" y1="185" x2="345" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<path d="M 55 135 Q 95 45, 130 60 Q 160 110, 185 110 Q 210 110, 245 30 Q 280 160, 325 160" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="70" y="128" font-family="sans-serif" font-size="10" font-weight="bold">R ({e_r})</text>'
        f'<text x="125" y="45" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">TS1 ({peak1})</text>'
        f'<text x="185" y="126" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#059669">Int ({e_int})</text>'
        f'<text x="245" y="22" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">TS2 ({peak2})</text>'
        f'<text x="315" y="152" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">P ({e_p})</text>',
        width=360,
        height=205,
    )
    prompt = (
        f"Refer to the two-step reaction profile ($E_R = {e_r}\\text{{ kJ}}$, $\\text{{TS1}} = {peak1}\\text{{ kJ}}$, "
        f"Intermediate $= {e_int}\\text{{ kJ}}$, $\\text{{TS2}} = {peak2}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$).\n\n"
        f"1. Calculate the individual activation energies $E_{{a,1}}$ (Step 1) and $E_{{a,2}}$ (Step 2).\n"
        f"2. Identify the **rate-determining (slowest) step** and the **overall $\\Delta H$**."
    )
    ans = f"Ea1 = {ea1} kJ; Ea2 = {ea2} kJ; Rate-determining step = {rds}; Overall ΔH = {e_p - e_r} kJ"
    sample = (
        f"1. $E_{{a,1}} = {peak1} - {e_r} = {ea1}\\text{{ kJ}}$; $E_{{a,2}} = {peak2} - {e_int} = {ea2}\\text{{ kJ}}$.\n"
        f"2. **{rds}** has the larger activation energy barrier and is therefore the slowest (rate-determining) step.\n"
        f"   Overall $\\Delta H = E_P - E_R = {e_p} - {e_r} = {e_p - e_r}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e42_{rng.randint(10000, 99999)}",
        subskill="42_multi_step_energy_diagram_intermediate_and_rds",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Ea1 = {ea1} kJ and Ea2 = {ea2} kJ", "marks": 2},
            {"id": "mp2", "desc": f"Rate-determining step: {rds}", "marks": 1},
            {"id": "mp3", "desc": f"Overall ΔH = {e_p - e_r} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Step 2 starts from the intermediate valley, NOT from the initial reactants.",
            "2_concept": "The step with the largest individual Ea is the rate-determining step.",
            "3_breakdown": sample,
        },
        misconception_tags=["measuring_Ea2_from_initial_reactants_instead_of_intermediate"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Two-step PE profile (TS1={peak1}, TS2={peak2})"},
    )


# =========================================================================== #
# 43: Biological Enzyme Catalysis in Cellular Respiration
# =========================================================================== #
def build_43_enzyme_catalysis_human_respiration_profile(rng: random.Random) -> Dict[str, Any]:
    ea_uncat = rng.choice([120, 140])
    ea_enz = rng.choice([35, 45])
    prompt = (
        f"Inside human cells at $37^\\circ\\text{{C}}$, **cellular respiration** ($\text{{C}}_6\text{{H}}_{{12}}\text{{O}}_6 + 6\text{{O}}_2 \\to 6\text{{CO}}_2 + 6\text{{H}}_2\text{{O}}$) "
        f"is catalysed by biological **enzymes**, lowering the activation energy from ${ea_uncat}\\text{{ kJ·mol}}^{{-1}}$ to ${ea_enz}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"1. State why glucose does not spontaneously combust in air at $37^\\circ\\text{{C}}$ without enzymes.\n"
        f"2. Compare the total heat energy released per mole of glucose metabolised **with** vs **without** enzymes."
    )
    ans = f"Uncatalysed Ea ({ea_uncat} kJ/mol) is too high at 37 °C; total heat released (ΔH) is identical with or without enzymes"
    sample = (
        f"1. Without enzymes, the activation energy barrier (${ea_uncat}\\text{{ kJ·mol}}^{{-1}}$) is far too high for molecules to react rapidly at $37^\\circ\\text{{C}}$; "
        f"enzymes lower $E_a$ to ${ea_enz}\\text{{ kJ·mol}}^{{-1}}$.\n"
        f"2. The total enthalpy change ($\\Delta H$) released per mole of glucose is **identical** because catalysts/enzymes do not alter reactant or product energies."
    )
    return _pillars(
        qid=f"ps11_e43_{rng.randint(10000, 99999)}",
        subskill="43_enzyme_catalysis_human_respiration_profile",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "High uncatalysed Ea prevents rapid reaction at 37 °C; enzyme lowers Ea", "marks": 2},
            {"id": "mp2", "desc": "Total ΔH released remains identical", "marks": 1},
        ],
        hints={
            "1_nudge": "An enzyme is a biological protein catalyst.",
            "2_concept": "Catalysts increase reaction rate by lowering Ea without changing ΔH.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_enzymes_increase_total_energy_released_from_glucose"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 44: Catalytic Converter Activation Energy Application
# =========================================================================== #
def build_44_catalytic_converter_activation_energy_application(rng: random.Random) -> Dict[str, Any]:
    metals = rng.choice(["platinum and rhodium", "platinum and palladium"])
    prompt = (
        f"Modern car exhaust systems contain a **catalytic converter** coated with finely divided **{metals}** to convert toxic carbon monoxide "
        f"into carbon dioxide: $$2\\text{{CO}}(g) + \\text{{O}}_2(g) \\rightarrow 2\\text{{CO}}_2(g) \\quad \\Delta H < 0$$\n\n"
        f"1. Explain how the {metals} surface speeds up CO oxidation inside the exhaust.\n"
        f"2. Explain why the catalyst is coated onto a porous honeycomb structure rather than used as a solid lump."
    )
    ans = f"Lowers activation energy Ea via alternative surface pathway; honeycomb structure maximises surface area"
    sample = (
        f"1. The {metals} catalyst provides an alternative surface reaction pathway with a **lower activation energy ($E_a$)**.\n"
        f"2. A porous honeycomb dramatically increases **exposed reaction surface area**, maximising adsorption and effective collisions per second."
    )
    return _pillars(
        qid=f"ps11_e44_{rng.randint(10000, 99999)}",
        subskill="44_catalytic_converter_activation_energy_application",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Alternative pathway with lower activation energy Ea", "marks": 2},
            {"id": "mp2", "desc": "Honeycomb structure maximises catalyst surface area", "marks": 1},
        ],
        hints={
            "1_nudge": "Consider both the energy barrier (Ea) and contact area between gas molecules and solid metal.",
            "2_concept": "Heterogeneous catalysis depends on lower Ea and high surface area.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_catalyst_reacts_permanently_with_CO"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 45: Rocket Propellant H2 + F2 Energy Analysis
# =========================================================================== #
def build_45_rocket_propellant_H2_F2_energy_analysis(rng: random.Random) -> Dict[str, Any]:
    moles_h2 = rng.choice([2, 3, 4])
    # H2 + F2 -> 2HF, ΔH = -535 kJ/mol H2
    q_total = moles_h2 * 535
    prompt = (
        f"Hydrogen and fluorine react explosively in aerospace propellant studies:\n"
        f"$$\\text{{H}}_2(g) + \\text{{F}}_2(g) \\rightarrow 2\\text{{HF}}(g) \\quad \\Delta H = -535\\text{{ kJ·mol}}^{{-1}}$$\n\n"
        f"1. Compare the strength of the new $\\text{{H–F}}$ bonds formed to the $\\text{{H–H}}$ and $\\text{{F–F}}$ bonds broken.\n"
        f"2. Calculate the total heat released when ${moles_h2}\\text{{ mol}}$ of $\\text{{H}}_2(g)$ reacts completely with excess $\\text{{F}}_2(g)$."
    )
    ans = f"Energy released forming H–F bonds exceeds energy needed to break H–H and F–F bonds; {q_total} kJ released"
    sample = (
        f"1. More energy is released forming two strong $\\text{{H–F}}$ bonds than is absorbed breaking $\\text{{H–H}}$ and $\\text{{F–F}}$ bonds ($\\Delta H < 0$).\n"
        f"2. Total energy released = ${moles_h2} \\times 535 = {q_total}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e45_{rng.randint(10000, 99999)}",
        subskill="45_rocket_propellant_H2_F2_energy_analysis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Energy released forming 2 H–F bonds > energy absorbed breaking H–H and F–F", "marks": 2},
            {"id": "mp2", "desc": f"Total energy = {q_total} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Exothermic reactions form stronger/more stable product bonds than reactant bonds.",
            "2_concept": "Multiply moles of H₂ by 535 kJ/mol.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_HF_bonds_are_weaker_than_FF_bonds"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 46: Comparing Lab Temperature-Time Profiles (Inline SVG)
# =========================================================================== #
def build_46_citric_acid_bicarbonate_vs_steel_wool_comparison(rng: random.Random) -> Dict[str, Any]:
    t0 = rng.choice([20, 22])
    t_exo = t0 + rng.choice([7, 9])
    t_endo = t0 - rng.choice([6, 8])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="180" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="180" x2="340" y2="180" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="14" y="25" font-family="sans-serif" font-size="10" font-weight="bold">T (°C)</text>'
        f'<text x="275" y="198" font-family="sans-serif" font-size="10" font-weight="bold">Time (min)</text>'
        f'<polyline points="55,105 140,75 230,55 320,50" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<polyline points="55,105 140,135 230,152 320,158" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="245" y="42" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">Exp 1 ({t0}°C -> {t_exo}°C)</text>'
        f'<text x="245" y="148" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">Exp 2 ({t0}°C -> {t_endo}°C)</text>',
        width=360,
        height=210,
    )
    prompt = (
        f"Refer to the experimental temperature-time curves recorded in two covered polystyrene cups starting at ${t0}^\\circ\\text{{C}}$:\n"
        f"- **Experiment 1**: Vinegar-washed steel wool oxidising in air (reaches ${t_exo}^\\circ\\text{{C}}$).\n"
        f"- **Experiment 2**: Citric acid solution reacting with $\\text{{NaHCO}}_3$ (drops to ${t_endo}^\\circ\\text{{C}}$).\n\n"
        f"1. Identify which experiment is **exothermic** and which is **endothermic**.\n"
        f"2. State why covering both polystyrene cups with lids improves experimental validity."
    )
    ans = "Exp 1 (steel wool) is exothermic; Exp 2 (citric acid + NaHCO3) is endothermic; lids prevent heat exchange with room air"
    sample = (
        f"1. **Experiment 1** is **exothermic** (heat released raises cup temperature to {t_exo} °C); "
        f"**Experiment 2** is **endothermic** (heat absorbed lowers temperature to {t_endo} °C).\n"
        f"2. Covering the cups with lids minimises unwanted heat transfer (convection/evaporation) between the cup and surrounding air."
    )
    return _pillars(
        qid=f"ps11_e46_{rng.randint(10000, 99999)}",
        subskill="46_citric_acid_bicarbonate_vs_steel_wool_comparison",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Exp 1 exothermic; Exp 2 endothermic", "marks": 2},
            {"id": "mp2", "desc": "Lid reduces heat loss/gain with room air (improves insulation)", "marks": 1},
        ],
        hints={
            "1_nudge": "Observe which curve slopes upward (temperature rise) vs downward (temperature drop).",
            "2_concept": "Exothermic heats surroundings (+ΔT); endothermic cools surroundings (-ΔT).",
            "3_breakdown": sample,
        },
        misconception_tags=["reversing_exo_and_endo_on_temperature_time_graph"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Lab T-t curves (Exp1={t_exo}°C, Exp2={t_endo}°C)"},
    )


# =========================================================================== #
# 47: Coupled Photosynthesis & Respiration Energy Cycle (Inline SVG)
# =========================================================================== #
def build_47_coupled_photosynthesis_respiration_energy_cycle(rng: random.Random) -> Dict[str, Any]:
    e_low = rng.choice([100, 150])
    e_high = e_low + 2803
    e_peak = e_high + rng.choice([120, 180])
    svg = _pe_curve_svg(e_low, e_peak, e_high, f"Photosynthesis vs Respiration (Peak={e_peak})")
    prompt = (
        f"Refer to the potential energy diagram linking **photosynthesis** ($6\\text{{CO}}_2 + 6\\text{{H}}_2\\text{{O}} \\to \\text{{C}}_6\\text{{H}}_{{12}}\\text{{O}}_6 + 6\\text{{O}}_2$) "
        f"as the forward process ($E_R = {e_low}\\text{{ kJ}}$, $E_P = {e_high}\\text{{ kJ}}$, peak $= {e_peak}\\text{{ kJ}}$) "
        f"and **cellular respiration** as the reverse process.\n\n"
        f"1. State $\\Delta H$ for photosynthesis (forward) and for cellular respiration (reverse).\n"
        f"2. Calculate the activation energy for **cellular respiration** without enzymes."
    )
    ea_resp = e_peak - e_high
    ans = f"ΔH(photosynthesis) = +2 803 kJ/mol; ΔH(respiration) = -2 803 kJ/mol; Ea(respiration) = {ea_resp} kJ"
    sample = (
        f"1. $\\Delta H_{{\\text{{photo}}}} = {e_high} - {e_low} = +2\\,803\\text{{ kJ·mol}}^{{-1}}$ (endothermic); "
        f"$\\Delta H_{{\\text{{resp}}}} = -2\\,803\\text{{ kJ·mol}}^{{-1}}$ (exothermic).\n"
        f"2. Uncatalysed $E_a$ for respiration = ${e_peak} - {e_high} = {ea_resp}\\text{{ kJ·mol}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps11_e47_{rng.randint(10000, 99999)}",
        subskill="47_coupled_photosynthesis_respiration_energy_cycle",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "ΔH(photo) = +2803 kJ/mol and ΔH(resp) = -2803 kJ/mol", "marks": 2},
            {"id": "mp2", "desc": f"Ea(resp) = {e_peak} - {e_high} = {ea_resp} kJ", "marks": 2},
        ],
        hints={
            "1_nudge": "Cellular respiration is the exact reverse of photosynthesis.",
            "2_concept": "Start from the higher glucose+O₂ energy level to measure the reverse Ea to the peak.",
            "3_breakdown": sample,
        },
        misconception_tags=["using_CO2_H2O_level_for_respiration_Ea"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Coupled bioenergetics PE cycle (Peak={e_peak})"},
    )


# =========================================================================== #
# 48: Algebraic Reaction Profile Extraction (X, Y, Z Variables) (Inline SVG)
# =========================================================================== #
def build_48_energy_profile_variable_substitution_graph_algebra(rng: random.Random) -> Dict[str, Any]:
    exo = rng.choice([True, False])
    a_val = rng.choice([30, 50])
    b_val = rng.choice([80, 100]) if exo else rng.choice([140, 170])
    c_val = rng.choice([190, 220])
    if exo:
        y_r, y_p = 90, 150
        r_lbl, p_lbl = b_val, a_val
        ea_expr = "Z - Y"
        dh_expr = "X - Y"
        ea_num = c_val - b_val
        dh_num = a_val - b_val
    else:
        y_r, y_p = 145, 90
        r_lbl, p_lbl = a_val, b_val
        ea_expr = "Z - X"
        dh_expr = "Y - X"
        ea_num = c_val - a_val
        dh_num = b_val - a_val

    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="185" x2="340" y2="185" stroke="#0f172a" stroke-width="2"/>'
        f'<path d="M 55 {y_r} C 130 {y_r}, 140 30, 185 30 C 230 30, 240 {y_p}, 325 {y_p}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="72" y="{y_r - 8}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold">{"Y" if exo else "X"}={r_lbl}</text>'
        f'<text x="185" y="22" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Z={c_val}</text>'
        f'<text x="302" y="{y_p - 8}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold">{"X" if exo else "Y"}={p_lbl}</text>',
        width=360,
        height=205,
    )
    prompt = (
        f"Refer to the potential energy graph labelled with energies $X$, $Y$, and $Z$ ($X = {a_val}$, $Y = {b_val}$, $Z = {c_val}\\text{{ kJ}}$).\n\n"
        f"1. Express both the forward activation energy ($E_a$) and enthalpy change ($\\Delta H$) algebraically in terms of $X$, $Y$, and $Z$.\n"
        f"2. Calculate the numerical values of $E_a$ and $\\Delta H$."
    )
    ans = f"Ea = {ea_expr} = {ea_num} kJ; ΔH = {dh_expr} = {dh_num} kJ"
    sample = (
        f"1. $E_a = {ea_expr}$; $\\Delta H = {dh_expr}$.\n"
        f"2. $E_a = {ea_num}\\text{{ kJ}}$; $\\Delta H = {dh_num}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e48_{rng.randint(10000, 99999)}",
        subskill="48_energy_profile_variable_substitution_graph_algebra",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Algebraic expressions: Ea = {ea_expr}, ΔH = {dh_expr}", "marks": 2},
            {"id": "mp2", "desc": f"Numerical evaluation: Ea = {ea_num} kJ, ΔH = {dh_num} kJ", "marks": 2},
        ],
        hints={
            "1_nudge": "Identify which symbol marks reactants, products, and the peak first.",
            "2_concept": "Ea = Peak - Reactants; ΔH = Products - Reactants.",
            "3_breakdown": sample,
        },
        misconception_tags=["inverting_X_and_Y_in_exothermic_vs_endothermic_graphs"],
        marks=4,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Algebraic PE profile (X={a_val}, Y={b_val}, Z={c_val})"},
    )


# =========================================================================== #
# 49: Thermochemistry Diagnostic Misconception Autopsy
# =========================================================================== #
def build_49_thermochemistry_diagnostic_misconception_autopsy(rng: random.Random) -> Dict[str, Any]:
    errors = [
        {
            "claim": "Adding a catalyst lowers ΔH because it decreases the potential energy peak of the reaction.",
            "flaw": "confusing activation energy (Ea) with enthalpy change (ΔH)",
            "repair": "A catalyst lowers ONLY the activation energy (Ea) and activated complex energy; E_reactants, E_products, and ΔH remain strictly unchanged.",
        },
        {
            "claim": "From the energy graph (E_reactants = 45 kJ, Peak = 103 kJ), the activation energy is 103 kJ.",
            "flaw": "reading the absolute peak height from zero instead of the height above reactants",
            "repair": "Activation energy is the energy needed FROM the reactant level up to the peak: Ea = 103 - 45 = 58 kJ.",
        },
        {
            "claim": "Dissolving NH₄NO₃ in water is exothermic because the cold water absorbs heat to reach room temperature.",
            "flaw": "confusing heat flow between surroundings and chemical system",
            "repair": "The thermometer drops because the NH₄NO₃ dissolution (chemical system) absorbed heat FROM the water, making the process endothermic (ΔH > 0).",
        },
    ]
    e = rng.choice(errors)
    prompt = (
        f"**Diagnostic Error Analysis:** A learner wrote the following statement:\n\n"
        f"> *\"{e['claim']}\"*\n\n"
        f"1. Identify the conceptual error in the learner's reasoning.\n"
        f"2. Provide the correct scientific statement."
    )
    ans = f"Error: {e['flaw']}. Correction: {e['repair']}"
    sample = f"1. **Error**: {e['flaw']}.\n2. **Correction**: {e['repair']}"
    return _pillars(
        qid=f"ps11_e49_{rng.randint(10000, 99999)}",
        subskill="49_thermochemistry_diagnostic_misconception_autopsy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify flaw: {e['flaw']}", "marks": 1},
            {"id": "mp2", "desc": f"Correct statement: {e['repair']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Check definitions: Ea = E_peak - E_R, ΔH = E_P - E_R, and catalysts never alter ΔH.",
            "2_concept": "Always distinguish the chemical system from the surrounding solution/thermometer.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_Ea_with_peak_energy", "claiming_catalyst_changes_ΔH"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 50: Comprehensive Grade 11 Energy & Chemical Change Synthesis (Inline SVG)
# =========================================================================== #
def build_50_energy_and_chemical_change_comprehensive_synthesis(rng: random.Random) -> Dict[str, Any]:
    e_r = rng.choice([80, 100])
    dh_mag = rng.choice([40, 60])
    e_p = e_r - dh_mag
    e_peak = e_r + rng.choice([50, 70])
    cat_peak = e_peak - 20
    ea_fwd = e_peak - e_r
    ea_rev = e_peak - e_p
    ea_cat = cat_peak - e_r
    svg = _pe_curve_svg(e_r, e_peak, e_p, f"Synthesis Profile (R={e_r}, P={e_p})", cat_peak=cat_peak)
    prompt = (
        f"Refer to the potential energy profile for the catalysed and uncatalysed synthesis reaction "
        f"($E_R = {e_r}\\text{{ kJ}}$, $E_P = {e_p}\\text{{ kJ}}$, uncatalysed peak $= {e_peak}\\text{{ kJ}}$, "
        f"catalysed green dashed peak $= {cat_peak}\\text{{ kJ}}$).\n\n"
        f"1. State whether the forward reaction is exothermic or endothermic and calculate $\\Delta H$.\n"
        f"2. Calculate the uncatalysed forward activation energy ($E_{{a,\\text{{fwd}}}}$) and reverse activation energy ($E_{{a,\\text{{rev}}}}$).\n"
        f"3. State the catalysed forward activation energy and explain whether adding the catalyst alters $\\Delta H$."
    )
    ans = f"Exothermic (ΔH = -{dh_mag} kJ); Ea(fwd) = {ea_fwd} kJ, Ea(rev) = {ea_rev} kJ; Ea(cat) = {ea_cat} kJ, ΔH unchanged"
    sample = (
        f"1. **Exothermic**, because $E_P < E_R$: $\\Delta H = {e_p} - {e_r} = -{dh_mag}\\text{{ kJ}}$.\n"
        f"2. $E_{{a,\\text{{fwd}}}} = {e_peak} - {e_r} = {ea_fwd}\\text{{ kJ}}$; "
        f"$E_{{a,\\text{{rev}}}} = {e_peak} - {e_p} = {ea_rev}\\text{{ kJ}}$.\n"
        f"3. Catalysed $E_a = {cat_peak} - {e_r} = {ea_cat}\\text{{ kJ}}$. Adding the catalyst does **not** alter $\\Delta H$ (still $-{dh_mag}\\text{{ kJ}}$) "
        f"because $E_R$ and $E_P$ are unchanged."
    )
    return _pillars(
        qid=f"ps11_e50_{rng.randint(10000, 99999)}",
        subskill="50_energy_and_chemical_change_comprehensive_synthesis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Exothermic and ΔH = -{dh_mag} kJ", "marks": 2},
            {"id": "mp2", "desc": f"Ea(fwd) = {ea_fwd} kJ and Ea(rev) = {ea_rev} kJ", "marks": 2},
            {"id": "mp3", "desc": f"Ea(cat) = {ea_cat} kJ and ΔH unchanged with justification", "marks": 2},
        ],
        hints={
            "1_nudge": "Read all four energy levels from the graph: R, P, uncatalysed peak, catalysed peak.",
            "2_concept": "ΔH = E_P - E_R; Ea(fwd) = Peak - E_R; Ea(rev) = Peak - E_P.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_catalyst_changes_ΔH", "using_E_reactants_for_reverse_Ea"],
        marks=6,
        duration=7,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Comprehensive PE synthesis (R={e_r}, P={e_p}, Peak={e_peak})"},
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_activation_energy_definition_and_ignition": build_26_activation_energy_definition_and_ignition,
    "27_activated_complex_transition_state_properties": build_27_activated_complex_transition_state_properties,
    "28_exothermic_potential_energy_profile_reading": build_28_exothermic_potential_energy_profile_reading,
    "29_endothermic_potential_energy_profile_reading": build_29_endothermic_potential_energy_profile_reading,
    "30_calculate_activated_complex_energy_from_Ea": build_30_calculate_activated_complex_energy_from_Ea,
    "31_calculate_product_energy_from_deltaH": build_31_calculate_product_energy_from_deltaH,
    "32_reverse_reaction_activation_energy_exothermic": build_32_reverse_reaction_activation_energy_exothermic,
    "33_reverse_reaction_activation_energy_endothermic": build_33_reverse_reaction_activation_energy_endothermic,
    "34_forward_vs_reverse_deltaH_symmetry": build_34_forward_vs_reverse_deltaH_symmetry,
    "35_sketching_and_identifying_reaction_coordinate_curves": build_35_sketching_and_identifying_reaction_coordinate_curves,
    "36_catalyst_effect_on_activation_energy": build_36_catalyst_effect_on_activation_energy,
    "37_catalyst_invariance_of_deltaH_reactants_products": build_37_catalyst_invariance_of_deltaH_reactants_products,
    "38_calculating_catalyzed_Ea_and_reverse_Ea": build_38_calculating_catalyzed_Ea_and_reverse_Ea,
    "39_inhibitor_negative_catalyst_energy_profile": build_39_inhibitor_negative_catalyst_energy_profile,
    "40_comparing_Ea_and_reaction_feasibility": build_40_comparing_Ea_and_reaction_feasibility,
    "41_maxwell_boltzmann_collision_energy_intro": build_41_maxwell_boltzmann_collision_energy_intro,
    "42_multi_step_energy_diagram_intermediate_and_rds": build_42_multi_step_energy_diagram_intermediate_and_rds,
    "43_enzyme_catalysis_human_respiration_profile": build_43_enzyme_catalysis_human_respiration_profile,
    "44_catalytic_converter_activation_energy_application": build_44_catalytic_converter_activation_energy_application,
    "45_rocket_propellant_H2_F2_energy_analysis": build_45_rocket_propellant_H2_F2_energy_analysis,
    "46_citric_acid_bicarbonate_vs_steel_wool_comparison": build_46_citric_acid_bicarbonate_vs_steel_wool_comparison,
    "47_coupled_photosynthesis_respiration_energy_cycle": build_47_coupled_photosynthesis_respiration_energy_cycle,
    "48_energy_profile_variable_substitution_graph_algebra": build_48_energy_profile_variable_substitution_graph_algebra,
    "49_thermochemistry_diagnostic_misconception_autopsy": build_49_thermochemistry_diagnostic_misconception_autopsy,
    "50_energy_and_chemical_change_comprehensive_synthesis": build_50_energy_and_chemical_change_comprehensive_synthesis,
}
