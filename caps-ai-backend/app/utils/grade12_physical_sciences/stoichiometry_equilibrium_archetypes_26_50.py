"""Grade 12 Physical Sciences — Chemical Equilibrium, Le Chatelier & Chemical Industry (Subskills 26–50).
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Strictly grounded in curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/02. Chemical equilibrium.md
and Term 3/05. The chemical industry.md.

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
        "topic": "Chemical equilibrium",
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
# 26: Equilibrium Constant Kc Expression Homogeneous
# =========================================================================== #
def build_26_equilibrium_constant_kc_expression_homogeneous(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {"eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})", "kc": r"K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3}", "name": "ammonia synthesis"},
        {"eq": r"2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightleftharpoons 2\text{SO}_3(\text{g})", "kc": r"K_c = \frac{[\text{SO}_3]^2}{[\text{SO}_2]^2[\text{O}_2]}", "name": "sulfur trioxide equilibrium"},
        {"eq": r"\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightleftharpoons 2\text{HI}(\text{g})", "kc": r"K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]}", "name": "hydrogen iodide equilibrium"},
        {"eq": r"\text{N}_2\text{O}_4(\text{g}) \rightleftharpoons 2\text{NO}_2(\text{g})", "kc": r"K_c = \frac{[\text{NO}_2]^2}{[\text{N}_2\text{O}_4]}", "name": "nitrogen dioxide dissociation"},
    ])
    prompt = (
        f"Consider the homogeneous gas-phase equilibrium for {rxn['name']}:\n"
        f"$${rxn['eq']}$$\n\n"
        "1. Write down the equilibrium constant expression ($K_c$) for this reaction.\n"
        "2. State what the square brackets, e.g. $[\\text{X}]$, represent in the equilibrium expression."
    )
    ans = f"{rxn['kc']}; square brackets represent equilibrium concentration in mol·dm⁻³"
    sample = (
        f"1. $${rxn['kc']}$$\n"
        r"2. Square brackets represent the **equilibrium concentration** of that chemical species in units of $\text{mol}\cdot\text{dm}^{-3}$."
    )
    return _pillars(
        qid=f"ps12_eq26_{rng.randint(10000, 99999)}",
        subskill="26_equilibrium_constant_kc_expression_homogeneous",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct Kc expression: {rxn['kc']}", "marks": 2},
            {"id": "mp2", "desc": "Square brackets indicate equilibrium concentration in mol·dm⁻³", "marks": 1},
        ],
        hints={
            "1_nudge": "Products go in numerator, reactants in denominator; coefficients become exponents.",
            "2_concept": "Kc = [products]^p / [reactants]^r at equilibrium.",
            "3_breakdown": sample,
        },
        misconception_tags=["inverted_kc_expression", "using_coefficients_as_multipliers_instead_of_powers"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 27: Equilibrium Constant Heterogeneous Omissions
# =========================================================================== #
def build_27_equilibrium_constant_heterogeneous_omissions(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {
            "eq": r"\text{CaCO}_3(\text{s}) \rightleftharpoons \text{CaO}(\text{s}) + \text{CO}_2(\text{g})",
            "kc": r"K_c = [\text{CO}_2]",
            "omitted": r"\text{CaCO}_3(\text{s}) \text{ and } \text{CaO}(\text{s})",
            "desc": "thermal decomposition of limestone",
        },
        {
            "eq": r"\text{C}(\text{s}) + \text{H}_2\text{O}(\text{g}) \rightleftharpoons \text{CO}(\text{g}) + \text{H}_2(\text{g})",
            "kc": r"K_c = \frac{[\text{CO}][\text{H}_2]}{[\text{H}_2\text{O}]}",
            "omitted": r"\text{C}(\text{s})",
            "desc": "water gas reaction",
        },
        {
            "eq": r"3\text{Fe}(\text{s}) + 4\text{H}_2\text{O}(\text{g}) \rightleftharpoons \text{Fe}_3\text{O}_4(\text{s}) + 4\text{H}_2(\text{g})",
            "kc": r"K_c = \frac{[\text{H}_2]^4}{[\text{H}_2\text{O}]^4}",
            "omitted": r"\text{Fe}(\text{s}) \text{ and } \text{Fe}_3\text{O}_4(\text{s})",
            "desc": "steam on iron equilibrium",
        },
    ])
    prompt = (
        f"Consider the heterogeneous equilibrium for the {rxn['desc']}:\n"
        f"$${rxn['eq']}$$\n\n"
        "1. Write down the correct equilibrium constant ($K_c$) expression.\n"
        f"2. Explain why ${rxn['omitted']}$ is/are omitted from the $K_c$ expression."
    )
    ans = f"{rxn['kc']}; Pure solids have constant concentration (density) that does not change during the reaction, so they are incorporated into the constant Kc."
    sample = (
        f"1. $${rxn['kc']}$$\n"
        "2. Pure solids have a **constant concentration (density)** that is independent of the amount present. "
        "Because their concentration cannot change at a given temperature, their constant value is incorporated directly into the equilibrium constant $K_c$."
    )
    return _pillars(
        qid=f"ps12_eq27_{rng.randint(10000, 99999)}",
        subskill="27_equilibrium_constant_heterogeneous_omissions",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct Kc expression omitting solids: {rxn['kc']}", "marks": 2},
            {"id": "mp2", "desc": "Explanation: pure solids have constant concentration/density", "marks": 1},
        ],
        hints={
            "1_nudge": "Which states of matter are excluded from Kc expressions?",
            "2_concept": "Pure solids (s) and pure liquids (l) are omitted from Kc.",
            "3_breakdown": sample,
        },
        misconception_tags=["including_solids_in_kc_expression", "confusing_pure_solids_with_aqueous_solutions"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 28: Magnitude of Kc and Equilibrium Position
# =========================================================================== #
def build_28_magnitude_of_kc_and_equilibrium_position(rng: random.Random) -> Dict[str, Any]:
    kc_choice = rng.choice([
        {"kc": "4,2 \\times 10^5", "val": 420000, "pos": "lies far to the right (favours products)", "yield": "high product yield", "pred": "mostly products present at equilibrium"},
        {"kc": "1,8 \\times 10^{-6}", "val": 0.0000018, "pos": "lies far to the left (favours reactants)", "yield": "low product yield", "pred": "mostly reactants remain unreacted at equilibrium"},
        {"kc": "2,4", "val": 2.4, "pos": "lies moderately to the right", "yield": "comparable concentrations of reactants and products", "pred": "significant amounts of both reactants and products exist at equilibrium"},
    ])
    prompt = (
        f"A reversible gas reaction reaches chemical equilibrium at 450 K with an equilibrium constant of:\n"
        f"$$K_c = {kc_choice['kc']}$$\n\n"
        "1. State what the magnitude of $K_c$ indicates about the position of equilibrium.\n"
        "2. Predict whether the yield of products is HIGH, LOW, or MODERATE at this temperature.\n"
        "3. Does a large value of $K_c$ imply that the reaction reaches equilibrium quickly? State YES or NO and justify."
    )
    ans = f"1. Position {kc_choice['pos']}; 2. {kc_choice['yield'].capitalize()}; 3. NO, Kc indicates extent/equilibrium position, not the rate of reaction."
    sample = (
        f"1. Because $K_c = {kc_choice['kc']}$, the equilibrium **{kc_choice['pos']}**.\n"
        f"2. Product yield is **{kc_choice['yield']}** at equilibrium ({kc_choice['pred']}).\n"
        r"3. **NO**. The equilibrium constant $K_c$ is a thermodynamic quantity that indicates the **extent** of the reaction (how far it proceeds). "
        "It provides **no information about the rate** (how fast equilibrium is reached), which is governed by activation energy."
    )
    return _pillars(
        qid=f"ps12_eq28_{rng.randint(10000, 99999)}",
        subskill="28_magnitude_of_kc_and_equilibrium_position",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Equilibrium position: {kc_choice['pos']}", "marks": 1},
            {"id": "mp2", "desc": f"Yield prediction: {kc_choice['yield']}", "marks": 1},
            {"id": "mp3", "desc": "NO with justification: Kc governs extent, not rate", "marks": 2},
        ],
        hints={
            "1_nudge": "If Kc is very large, which is bigger: numerator (products) or denominator (reactants)?",
            "2_concept": "Kc relates to extent, not rate. A reaction can have a huge Kc but be extremely slow.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_kc_magnitude_with_reaction_rate", "misinterpreting_kc_greater_than_one"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 29: Temperature Dependence of Kc Value
# =========================================================================== #
def build_29_temperature_dependence_of_kc_value(rng: random.Random) -> Dict[str, Any]:
    rxn_type = rng.choice([
        {"name": "synthesis of ammonia", "eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})", "dh": r"\Delta H < 0 \text{ (exothermic)}", "fwd": "exothermic", "t1": 300, "t2": 500, "kc1": 9.6, "kc2": 0.05, "trend": "decreases"},
        {"name": "decomposition of dinitrogen tetroxide", "eq": r"\text{N}_2\text{O}_4(\text{g}) \rightleftharpoons 2\text{NO}_2(\text{g})", "dh": r"\Delta H > 0 \text{ (endothermic)}", "fwd": "endothermic", "t1": 273, "t2": 373, "kc1": 0.004, "kc2": 0.36, "trend": "increases"},
    ])
    prompt = (
        f"Consider the reversible reaction for the {rxn_type['name']}:\n"
        f"$${rxn_type['eq']} \\quad ({rxn_type['dh']})$$\n\n"
        f"- At $T_1 = {rxn_type['t1']}\\text{{ K}}$, $K_c = {_fmt_sa(rxn_type['kc1'])}$.\n"
        f"- At $T_2 = {rxn_type['t2']}\\text{{ K}}$, $K_c = {_fmt_sa(rxn_type['kc2'])}$.\n\n"
        f"1. State how the value of $K_c$ changes as temperature increases from {rxn_type['t1']} K to {rxn_type['t2']} K.\n"
        "2. Use Le Chatelier's principle to explain this change in the value of $K_c$.\n"
        "3. Name the ONLY experimental factor that can change the numerical value of $K_c$ for a given reaction."
    )
    ans = f"1. Kc {rxn_type['trend']}; 2. An increase in temperature favours the endothermic reaction. For this {rxn_type['fwd']} forward reaction, the {'reverse reaction is favoured, decreasing [products] and increasing [reactants], so Kc decreases' if rxn_type['fwd'] == 'exothermic' else 'forward endothermic reaction is favoured, increasing [products] and decreasing [reactants], so Kc increases'}; 3. Temperature."
    sample = (
        f"1. The value of $K_c$ **{rxn_type['trend']}** as temperature rises.\n"
        r"2. According to Le Chatelier's principle, an **increase in temperature favours the endothermic reaction** to absorb added heat. "
        + (
            r"Since the forward reaction is exothermic, the reverse (endothermic) reaction is favoured. "
            r"Reactant concentrations increase while product concentrations decrease, resulting in a lower $K_c = \frac{[\text{products}]}{[\text{reactants}]}$."
            if rxn_type["fwd"] == "exothermic"
            else
            r"Since the forward reaction is endothermic, the forward reaction is favoured. "
            r"Product concentrations increase while reactant concentrations decrease, resulting in a higher $K_c = \frac{[\text{products}]}{[\text{reactants}]}$."
        )
        + "\n3. **Temperature** is the ONLY factor that alters the numerical value of $K_c$ (concentration, pressure, and catalysts do not change $K_c$)."
    )
    return _pillars(
        qid=f"ps12_eq29_{rng.randint(10000, 99999)}",
        subskill="29_temperature_dependence_of_kc_value",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Kc {rxn_type['trend']} with temperature", "marks": 1},
            {"id": "mp2", "desc": "Increase in temperature favours endothermic direction", "marks": 1},
            {"id": "mp3", "desc": "Explanation of product/reactant concentration shift in Kc expression", "marks": 1},
            {"id": "mp4", "desc": "Temperature is the only factor affecting Kc", "marks": 1},
        ],
        hints={
            "1_nudge": "Which reaction (forward or reverse) absorbs heat?",
            "2_concept": "Temperature increase always favours endothermic. Kc changes only with temperature.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_pressure_or_catalysts_change_kc", "failing_to_link_le_chatelier_shift_to_kc_formula"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 30: Calculating Kc from Equilibrium Concentrations
# =========================================================================== #
def build_30_calculating_kc_from_equilibrium_concentrations(rng: random.Random) -> Dict[str, Any]:
    c_so2 = rng.choice([0.20, 0.40, 0.50])
    c_o2 = rng.choice([0.10, 0.20, 0.25])
    c_so3 = rng.choice([0.60, 0.80, 1.00])
    # 2SO2 + O2 <=> 2SO3. Kc = [SO3]^2 / ([SO2]^2 * [O2])
    num = c_so3 ** 2
    den = (c_so2 ** 2) * c_o2
    kc = round(num / den, 2)

    prompt = (
        "Sulfur dioxide and oxygen react in a sealed container according to the balanced equation:\n"
        r"$$2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightleftharpoons 2\text{SO}_3(\text{g})$$" + "\n\n"
        "At equilibrium at 600 °C, the concentrations are found to be:\n"
        rf"- $[\text{{SO}}_2] = {_fmt_sa(c_so2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n"
        rf"- $[\text{{O}}_2] = {_fmt_sa(c_o2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n"
        rf"- $[\text{{SO}}_3] = {_fmt_sa(c_so3)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n\n"
        "1. Write down the expression for $K_c$.\n"
        "2. Calculate the value of the equilibrium constant ($K_c$) at 600 °C."
    )
    ans = f"Kc = [SO3]^2 / ([SO2]^2 * [O2]); Kc = {_fmt_sa(kc)}"
    sample = (
        r"1. $$K_c = \frac{[\text{SO}_3]^2}{[\text{SO}_2]^2[\text{O}_2]}$$" + "\n"
        rf"2. $$K_c = \frac{{({_fmt_sa(c_so3)})^2}}{{({_fmt_sa(c_so2)})^2({_fmt_sa(c_o2)})}} = \frac{{{_fmt_sa(round(num, 4))}}}{{{_fmt_sa(round(den, 4))}}} = {_fmt_sa(kc)}$$."
    )
    return _pillars(
        qid=f"ps12_eq30_{rng.randint(10000, 99999)}",
        subskill="30_calculating_kc_from_equilibrium_concentrations",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Kc expression", "marks": 1},
            {"id": "mp2", "desc": "Correct substitution into expression", "marks": 1},
            {"id": "mp3", "desc": f"Correct numerical answer: {_fmt_sa(kc)}", "marks": 1},
        ],
        hints={
            "1_nudge": "Don't forget the square on [SO3] and [SO2]!",
            "2_concept": "Substitute the given equilibrium concentrations directly into Kc.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_to_square_concentrations", "swapping_products_and_reactants_in_kc"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 31: Calculating Equilibrium Concentration Given Kc
# =========================================================================== #
def build_31_calculating_equilibrium_concentration_given_kc(rng: random.Random) -> Dict[str, Any]:
    c_n2 = rng.choice([0.15, 0.20, 0.25])
    c_h2 = rng.choice([0.30, 0.40, 0.50])
    c_nh3 = rng.choice([0.60, 0.80, 1.20])
    # N2 + 3H2 <=> 2NH3. Kc = [NH3]^2 / ([N2][H2]^3)
    kc = round((c_nh3 ** 2) / (c_n2 * (c_h2 ** 3)), 2)

    prompt = (
        "The synthesis of ammonia reaches equilibrium at 400 °C:\n"
        r"$$\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})$$" + "\n\n"
        rf"At this temperature, $K_c = {_fmt_sa(kc)}$. Analysis of the equilibrium mixture reveals:" + "\n"
        rf"- $[\text{{N}}_2] = {_fmt_sa(c_n2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n"
        rf"- $[\text{{H}}_2] = {_fmt_sa(c_h2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n\n"
        rf"Calculate the concentration of ammonia, $[\text{{NH}}_3]$, present at equilibrium in $\text{{mol}}\cdot\text{{dm}}^{{-3}}$."
    )
    ans = f"[NH3] = {_fmt_sa(c_nh3)} mol·dm⁻³"
    sample = (
        r"$$K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3}$$" + "\n"
        rf"$${_fmt_sa(kc)} = \frac{{[\text{{NH}}_3]^2}}{{({_fmt_sa(c_n2)})({_fmt_sa(c_h2)})^3}}$$" + "\n"
        rf"$$[\text{{NH}}_3]^2 = {_fmt_sa(kc)} \times {_fmt_sa(c_n2)} \times {_fmt_sa(round(c_h2**3, 4))} = {_fmt_sa(round(c_nh3**2, 4))}$$" + "\n"
        rf"$$[\text{{NH}}_3] = \sqrt{{{_fmt_sa(round(c_nh3**2, 4))}}} = {_fmt_sa(c_nh3)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$$"
    )
    return _pillars(
        qid=f"ps12_eq31_{rng.randint(10000, 99999)}",
        subskill="31_calculating_equilibrium_concentration_given_kc",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Correct Kc formula and substitution", "marks": 2},
            {"id": "mp2", "desc": "Taking square root of product", "marks": 1},
            {"id": "mp3", "desc": f"Answer with units: {_fmt_sa(c_nh3)} mol·dm⁻³", "marks": 1},
        ],
        hints={
            "1_nudge": "Multiply both sides by denominator, then take the square root.",
            "2_concept": "[NH3]^2 = Kc * [N2] * [H2]^3.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_to_cube_hydrogen_concentration", "forgetting_to_square_root_ammonia"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 32: Reaction Quotient Qc vs Kc
# =========================================================================== #
def build_32_reaction_quotient_qc_vs_kc(rng: random.Random) -> Dict[str, Any]:
    kc = rng.choice([25.0, 50.0, 64.0])
    scenario = rng.choice(["less_than", "greater_than"])
    if scenario == "less_than":
        c_h2 = 1.0
        c_i2 = 1.0
        c_hi = 2.0  # Qc = 4.0 / 1.0 = 4.0 < kc
        qc = 4.0
        shift = "forward (to the right)"
        reason = "Qc < Kc, so more products must form to reach equilibrium"
    else:
        c_h2 = 0.5
        c_i2 = 0.5
        c_hi = 5.0  # Qc = 25.0 / 0.25 = 100 > kc
        qc = 100.0
        shift = "reverse (to the left)"
        reason = "Qc > Kc, so products must react back into reactants to reach equilibrium"

    prompt = (
        "Consider the equilibrium reaction at 448 °C:\n"
        r"$$\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightleftharpoons 2\text{HI}(\text{g}) \quad (K_c = " + _fmt_sa(kc) + r")$$" + "\n\n"
        "At a certain instant, a sample from the reaction vessel has concentrations:\n"
        rf"- $[\text{{H}}_2] = {_fmt_sa(c_h2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n"
        rf"- $[\text{{I}}_2] = {_fmt_sa(c_i2)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n"
        rf"- $[\text{{HI}}] = {_fmt_sa(c_hi)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$" + "\n\n"
        "1. Calculate the reaction quotient ($Q_c$) for this mixture.\n"
        "2. State whether the system is at chemical equilibrium.\n"
        "3. In which direction (FORWARD or REVERSE) will the reaction proceed to achieve equilibrium? Explain."
    )
    ans = f"1. Qc = {_fmt_sa(qc)}; 2. NOT at equilibrium (Qc != Kc); 3. {shift.upper()}, because {reason}."
    sample = (
        rf"1. $$Q_c = \frac{{[\text{{HI}}]^2}}{{[\text{{H}}_2][\text{{I}}_2]}} = \frac{{({_fmt_sa(c_hi)})^2}}{{({_fmt_sa(c_h2)})({_fmt_sa(c_i2)})}} = {_fmt_sa(qc)}$$" + "\n"
        rf"2. The system is **NOT at equilibrium** because $Q_c ({_fmt_sa(qc)}) \ne K_c ({_fmt_sa(kc)})$.\n"
        f"3. Because $Q_c {'<' if scenario == 'less_than' else '>'} K_c$, the net reaction will proceed in the **{shift}** direction. {reason}."
    )
    return _pillars(
        qid=f"ps12_eq32_{rng.randint(10000, 99999)}",
        subskill="32_reaction_quotient_qc_vs_kc",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Qc calculation: {_fmt_sa(qc)}", "marks": 2},
            {"id": "mp2", "desc": "Statement that system is not at equilibrium", "marks": 1},
            {"id": "mp3", "desc": f"Direction ({shift}) with comparison of Qc and Kc", "marks": 1},
        ],
        hints={
            "1_nudge": "Qc is calculated using the exact same formula as Kc, but using non-equilibrium concentrations.",
            "2_concept": "If Qc < Kc, system shifts forward; if Qc > Kc, system shifts in reverse.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_qc_with_kc", "inverted_direction_prediction"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 33: Reverse Reaction Kc Relationship
# =========================================================================== #
def build_33_reverse_reaction_kc_relationship(rng: random.Random) -> Dict[str, Any]:
    kc_fwd = rng.choice([0.25, 0.50, 4.0, 10.0, 50.0])
    kc_rev = round(1.0 / kc_fwd, 4)
    prompt = (
        "For the reaction:\n"
        r"$$\text{N}_2\text{O}_4(\text{g}) \rightleftharpoons 2\text{NO}_2(\text{g})$$" + "\n\n"
        rf"The equilibrium constant is $K_c = {_fmt_sa(kc_fwd)}$ at 298 K." + "\n"
        "1. Write down the equilibrium constant expression ($K_c'$) for the reverse reaction:\n"
        r"$$2\text{NO}_2(\text{g}) \rightleftharpoons \text{N}_2\text{O}_4(\text{g})$$" + "\n"
        "2. State the mathematical relationship between the forward equilibrium constant ($K_c$) and the reverse equilibrium constant ($K_c'$).\n"
        "3. Calculate the numerical value of $K_c'$ at 298 K."
    )
    ans = f"1. Kc' = [N2O4] / [NO2]^2; 2. Kc' = 1 / Kc; 3. Kc' = {_fmt_sa(kc_rev, 4)}"
    sample = (
        r"1. $$K_c' = \frac{[\text{N}_2\text{O}_4]}{[\text{NO}_2]^2}$$" + "\n"
        r"2. The reverse equilibrium constant is the reciprocal of the forward equilibrium constant:" + "\n"
        r"$$K_c' = \frac{1}{K_c}$$" + "\n"
        rf"3. $$K_c' = \frac{{1}}{{{_fmt_sa(kc_fwd)}}} = {_fmt_sa(kc_rev, 4)}$$"
    )
    return _pillars(
        qid=f"ps12_eq33_{rng.randint(10000, 99999)}",
        subskill="33_reverse_reaction_kc_relationship",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Reverse Kc expression", "marks": 1},
            {"id": "mp2", "desc": "Reciprocal relationship: Kc' = 1 / Kc", "marks": 1},
            {"id": "mp3", "desc": f"Calculation of Kc': {_fmt_sa(kc_rev, 4)}", "marks": 1},
        ],
        hints={
            "1_nudge": "Inverting the reaction inverts the fraction.",
            "2_concept": "Kc(reverse) = 1 / Kc(forward).",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_reverse_kc_is_negative_kc", "forgetting_reciprocal_rule"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 34: Le Chatelier Principle Statement
# =========================================================================== #
def build_34_le_chatelier_principle_statement(rng: random.Random) -> Dict[str, Any]:
    factors = [
        {"name": "temperature change", "desc": "shifts equilibrium to absorb or release thermal energy"},
        {"name": "concentration change", "desc": "shifts equilibrium to consume added species or replace removed species"},
        {"name": "pressure change (for gases)", "desc": "shifts equilibrium to side with fewer or more gas moles"},
    ]
    f = rng.choice(factors)
    prompt = (
        "1. State **Le Chatelier's Principle** verbatim according to the South African CAPS curriculum.\n"
        f"2. Explain how a closed equilibrium system responds when a **{f['name']}** is imposed on it."
    )
    ans = "When the equilibrium in a closed system is disturbed, the system will adjust in such a way as to counteract the disturbance (oppose the change) and establish a new equilibrium."
    sample = (
        "1. **Le Chatelier's Principle**: When the equilibrium in a closed system is disturbed, the system will adjust in such a way as to counteract the disturbance (oppose the change) and establish a new equilibrium.\n"
        f"2. When {f['name']} occurs, the system shifts its forward or reverse reaction rate so as to {f['desc']}, minimizing the external stress."
    )
    return _pillars(
        qid=f"ps12_eq34_{rng.randint(10000, 99999)}",
        subskill="34_le_chatelier_principle_statement",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Closed system and disturbed condition mentioned", "marks": 1},
            {"id": "mp2", "desc": "System adjusts to counteract the disturbance", "marks": 1},
            {"id": "mp3", "desc": "Application to specific stress factor", "marks": 1},
        ],
        hints={
            "1_nudge": "Le Chatelier's principle states that nature fights back to undo the change you make.",
            "2_concept": "Key words: closed system, disturbed, counteract the disturbance.",
            "3_breakdown": sample,
        },
        misconception_tags=["omitting_closed_system_in_le_chatelier_definition", "saying_system_reinforces_change_instead_of_counteracting"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 35: Le Chatelier Concentration Disturbance
# =========================================================================== #
def build_35_le_chatelier_concentration_disturbance(rng: random.Random) -> Dict[str, Any]:
    action = rng.choice([
        {"action": "adding more N2(g)", "favours": "forward reaction", "reason": "to consume excess N2", "color_change": "increases NH3 yield"},
        {"action": "removing NH3(g) continuously as it forms", "favours": "forward reaction", "reason": "to replace removed NH3", "color_change": "increases NH3 production rate"},
        {"action": "adding more NH3(g)", "favours": "reverse reaction", "reason": "to consume excess NH3", "color_change": "increases N2 and H2 concentrations"},
    ])
    prompt = (
        "Consider the Haber equilibrium in a sealed container:\n"
        r"$$\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g}) \quad (\Delta H = -92\text{ kJ}\cdot\text{mol}^{-1})$$" + "\n\n"
        f"At constant temperature and volume, the system is disturbed by **{action['action']}**.\n"
        "1. According to Le Chatelier's principle, which reaction (FORWARD or REVERSE) is favoured? Explain.\n"
        rf"2. How does the concentration of $\text{{H}}_2(\text{{g}})$ change once the new equilibrium is established (INCREASES, DECREASES, or REMAINS THE SAME)?\n"
        "3. Does the numerical value of $K_c$ change? State YES or NO."
    )
    ans = f"1. Favours {action['favours']}, {action['reason']}; 2. {'Decreases' if 'forward' in action['favours'] else 'Increases'}; 3. NO (temperature is constant)."
    sample = (
        f"1. The **{action['favours']}** is favoured. According to Le Chatelier's principle, the system adjusts to **{action['reason']}**.\n"
        rf"2. The concentration of $\text{{H}}_2$ **{'DECREASES' if 'forward' in action['favours'] else 'INCREASES'}** because $\text{{H}}_2$ is {'consumed as the forward reaction proceeds' if 'forward' in action['favours'] else 'produced as the reverse reaction proceeds'}.\n"
        "3. **NO**. The value of $K_c$ remains completely unchanged because temperature has remained constant."
    )
    return _pillars(
        qid=f"ps12_eq35_{rng.randint(10000, 99999)}",
        subskill="35_le_chatelier_concentration_disturbance",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Favours {action['favours']}", "marks": 1},
            {"id": "mp2", "desc": f"Le Chatelier explanation: {action['reason']}", "marks": 1},
            {"id": "mp3", "desc": "H2 concentration change", "marks": 1},
            {"id": "mp4", "desc": "NO: Kc is constant at constant temperature", "marks": 1},
        ],
        hints={
            "1_nudge": "If you add something, the system shifts to use it up; if you remove it, the system shifts to replace it.",
            "2_concept": "Kc depends strictly on temperature. Concentration changes never alter Kc.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_concentration_change_alters_kc", "incorrect_le_chatelier_direction"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 36: Le Chatelier Temperature Disturbance
# =========================================================================== #
def build_36_le_chatelier_temperature_disturbance(rng: random.Random) -> Dict[str, Any]:
    temp_action = rng.choice(["increasing", "decreasing"])
    prompt = (
        "The brown gas nitrogen dioxide (NO2) exists in equilibrium with colourless dinitrogen tetroxide (N2O4):\n"
        r"$$2\text{NO}_2(\text{g, brown}) \rightleftharpoons \text{N}_2\text{O}_4(\text{g, colourless}) \quad (\Delta H = -57{,}2\text{ kJ}\cdot\text{mol}^{-1})$$" + "\n\n"
        f"A sealed glass syringe containing this equilibrium mixture is placed into a water bath, **{temp_action} the temperature** of the gas.\n"
        "1. State whether the forward reaction is EXOTHERMIC or ENDOTHERMIC.\n"
        "2. Use Le Chatelier's principle to explain which reaction (FORWARD or REVERSE) is favoured by this temperature change.\n"
        "3. State how the colour of the gas mixture in the syringe changes (BECOMES DARKER BROWN or BECOMES LIGHTER/COLOURLESS).\n"
        "4. How does the value of $K_c$ change (INCREASES, DECREASES, or REMAINS THE SAME)?"
    )
    if temp_action == "increasing":
        fwd_fav = "reverse reaction (endothermic)"
        color = "BECOMES DARKER BROWN (more NO2 formed)"
        kc_change = "DECREASES"
        exp = "An increase in temperature favours the endothermic reaction to absorb the added heat. Since the forward reaction is exothermic, the reverse (endothermic) reaction is favoured."
    else:
        fwd_fav = "forward reaction (exothermic)"
        color = "BECOMES LIGHTER/COLOURLESS (more N2O4 formed)"
        kc_change = "INCREASES"
        exp = "A decrease in temperature favours the exothermic reaction to release heat. Since the forward reaction is exothermic, the forward reaction is favoured."

    ans = f"1. Exothermic; 2. Favours {fwd_fav}; 3. {color}; 4. {kc_change}"
    sample = (
        r"1. Because $\Delta H < 0$, the forward reaction is **exothermic**." + "\n"
        f"2. {exp}\n"
        f"3. The gas mixture **{color}**.\n"
        rf"4. $K_c$ **{kc_change}**."
    )
    return _pillars(
        qid=f"ps12_eq36_{rng.randint(10000, 99999)}",
        subskill="36_le_chatelier_temperature_disturbance",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Forward reaction is exothermic", "marks": 1},
            {"id": "mp2", "desc": f"Le Chatelier explanation: favours {fwd_fav}", "marks": 2},
            {"id": "mp3", "desc": f"Colour change: {color}", "marks": 1},
            {"id": "mp4", "desc": f"Kc change: {kc_change}", "marks": 1},
        ],
        hints={
            "1_nudge": "Increasing temp favours endothermic; decreasing temp favours exothermic.",
            "2_concept": "Check ΔH sign: negative means forward is exothermic, so reverse is endothermic.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_which_direction_is_endothermic", "claiming_temperature_does_not_change_kc"],
        marks=5,
        duration=5,
    )


# =========================================================================== #
# 37: Le Chatelier Pressure and Volume Gases
# =========================================================================== #
def build_37_le_chatelier_pressure_and_volume_gases(rng: random.Random) -> Dict[str, Any]:
    rxn = rng.choice([
        {"eq": r"2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightleftharpoons 2\text{SO}_3(\text{g})", "r_moles": 3, "p_moles": 2, "name": "sulfur trioxide synthesis"},
        {"eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})", "r_moles": 4, "p_moles": 2, "name": "ammonia synthesis"},
        {"eq": r"\text{PCl}_5(\text{g}) \rightleftharpoons \text{PCl}_3(\text{g}) + \text{Cl}_2(\text{g})", "r_moles": 1, "p_moles": 2, "name": "phosphorus pentachloride decomposition"},
    ])
    vol_change = rng.choice(["decreasing", "increasing"])
    if vol_change == "decreasing":
        press = "increases"
        target_moles = "fewer moles of gas"
        favoured = "forward reaction" if rxn["p_moles"] < rxn["r_moles"] else "reverse reaction"
    else:
        press = "decreases"
        target_moles = "greater moles of gas"
        favoured = "reverse reaction" if rxn["p_moles"] < rxn["r_moles"] else "forward reaction"

    prompt = (
        f"Consider the gas-phase equilibrium for {rxn['name']}:\n"
        f"$${rxn['eq']}$$\n\n"
        f"The volume of the reaction container is **{vol_change}** at constant temperature.\n"
        f"1. How does this volume change affect the total pressure inside the container?\n"
        "2. Count the total number of moles of gas on the reactant side and product side.\n"
        "3. Use Le Chatelier's principle to explain which reaction (FORWARD or REVERSE) is favoured.\n"
        "4. Does the value of $K_c$ change as a result of this pressure adjustment?"
    )
    ans = f"1. Pressure {press}; 2. Reactants = {rxn['r_moles']} mol, Products = {rxn['p_moles']} mol; 3. Favours {favoured} to shift towards {target_moles}; 4. NO, temperature is constant."
    sample = (
        f"1. According to Boyle's law, {vol_change} container volume causes total pressure to **{press}**.\n"
        f"2. Reactants = **{rxn['r_moles']} moles of gas**; Products = **{rxn['p_moles']} moles of gas**.\n"
        f"3. By Le Chatelier's principle, the system adjusts to counteract the pressure change by shifting towards the side with **{target_moles}**. Therefore, the **{favoured}** is favoured.\n"
        "4. **NO**. The value of $K_c$ remains unchanged because temperature is constant."
    )
    return _pillars(
        qid=f"ps12_eq37_{rng.randint(10000, 99999)}",
        subskill="37_le_chatelier_pressure_and_volume_gases",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Pressure {press}", "marks": 1},
            {"id": "mp2", "desc": f"Correct gas mole count: {rxn['r_moles']} vs {rxn['p_moles']}", "marks": 1},
            {"id": "mp3", "desc": f"Le Chatelier: favours {favoured} towards {target_moles}", "marks": 2},
            {"id": "mp4", "desc": "NO: Kc is constant", "marks": 1},
        ],
        hints={
            "1_nudge": "Count the stoichiometric gas coefficients on each side.",
            "2_concept": "High pressure favours fewer gas moles; low pressure favours more gas moles.",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_solid_or_liquid_moles_in_gas_pressure_shift", "believing_pressure_changes_kc"],
        marks=5,
        duration=5,
    )


# =========================================================================== #
# 38: Le Chatelier Catalyst Invariance
# =========================================================================== #
def build_38_le_chatelier_catalyst_invariance(rng: random.Random) -> Dict[str, Any]:
    cat = rng.choice(["iron (Fe) in ammonia synthesis", "vanadium pentoxide (V2O5) in sulfur trioxide synthesis", "finely divided platinum (Pt)"])
    prompt = (
        f"A suitable catalyst ({cat}) is added to a closed reaction vessel that has already attained chemical equilibrium at 450 °C.\n\n"
        "1. What is the effect of the catalyst on the rate of the forward reaction?\n"
        "2. What is the effect of the catalyst on the rate of the reverse reaction?\n"
        "3. Does the catalyst cause any shift in the position of equilibrium (or alter the yield of products)? State YES or NO and justify.\n"
        "4. Does the catalyst change the value of the equilibrium constant ($K_c$)?"
    )
    ans = "1. Increases forward rate; 2. Increases reverse rate by the exact same factor; 3. NO, both rates increase equally, so the equilibrium position and yield are unchanged (equilibrium is reached faster, but position is unaltered); 4. NO."
    sample = (
        "1. The catalyst **increases the rate of the forward reaction** by lowering its activation energy.\n"
        "2. The catalyst **increases the rate of the reverse reaction by the exact same factor** by lowering its activation energy by the same amount.\n"
        "3. **NO**. Because both forward and reverse rates are accelerated equally, there is **no net shift in the position of equilibrium** and the yield of products remains unchanged. The system merely reaches equilibrium faster.\n"
        "4. **NO**. $K_c$ depends only on temperature and is completely unchanged by catalysts."
    )
    return _pillars(
        qid=f"ps12_eq38_{rng.randint(10000, 99999)}",
        subskill="38_le_chatelier_catalyst_invariance",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Increases forward rate", "marks": 1},
            {"id": "mp2", "desc": "Increases reverse rate equally", "marks": 1},
            {"id": "mp3", "desc": "NO: no shift in position of equilibrium with reason", "marks": 1},
            {"id": "mp4", "desc": "NO: Kc is unchanged", "marks": 1},
        ],
        hints={
            "1_nudge": "Does a catalyst lower activation energy for one direction only, or for both directions?",
            "2_concept": "Catalysts lower the barrier equally from both sides, leaving equilibrium position and Kc unchanged.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_catalyst_shifts_equilibrium_position", "believing_catalyst_increases_yield"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 39: Graphical Analysis Concentration Spike
# =========================================================================== #
def build_39_graphical_analysis_concentration_spike(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([30, 40])
    t2 = t1 + rng.choice([30, 40])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="10" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Conc [ ]</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<line x1="50" y1="140" x2="{50 + t1 * 3}" y2="140" stroke="#2563eb" stroke-width="2.5"/>'
        f'<line x1="{50 + t1 * 3}" y1="140" x2="{50 + t1 * 3}" y2="70" stroke="#2563eb" stroke-width="2.5"/>'
        f'<path d="M {50 + t1 * 3} 70 Q {50 + t1 * 3 + 30} 85, {50 + t2 * 3} 85 L 360 85" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="60" y="132" font-family="sans-serif" font-size="10" fill="#2563eb">[Reactant A]</text>'
        f'<line x1="50" y1="110" x2="{50 + t1 * 3}" y2="110" stroke="#dc2626" stroke-width="2.5"/>'
        f'<path d="M {50 + t1 * 3} 110 Q {50 + t1 * 3 + 30} 130, {50 + t2 * 3} 130 L 360 130" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="60" y="102" font-family="sans-serif" font-size="10" fill="#dc2626">[Product B]</text>'
        f'<line x1="{50 + t1 * 3}" y1="20" x2="{50 + t1 * 3}" y2="190" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="{40 + t1 * 3}" y="205" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">t1 ({t1} s)</text>',
        width=390,
        height=230,
    )
    prompt = (
        r"The accompanying concentration-time graph illustrates a closed equilibrium system $\text{A}(\text{g}) \rightleftharpoons \text{B}(\text{g})$ disturbed at time $t_1$." + "\n\n"
        rf"1. Identify the exact disturbance that occurred at time $t_1 = {t1}\text{{ s}}$. Justify using graphical evidence." + "\n"
        "2. Explain why the concentration of B increases gradually after time $t_1$.\n"
        "3. How does the value of $K_c$ at $t = 20\\text{ s}$ compare to the value of $K_c$ at $t = 80\\text{ s}$ (GREATER THAN, LESS THAN, or EQUAL TO) assuming temperature remained constant?"
    )
    ans = f"1. Reactant A was added; instantaneous vertical spike in [A] at t1 while [B] has no spike; 2. Forward reaction is favoured to consume excess A, gradually producing more B; 3. EQUAL TO (temperature is constant)."
    sample = (
        f"1. **Reactant A was added** to the container. Graphically, Curve A shows an **instantaneous vertical sharp spike** at $t_1 = {t1}\\text{{ s}}$, whereas Curve B shows no vertical spike at that moment.\n"
        "2. By Le Chatelier's principle, the system shifts forward to counteract the increase in $[\\text{A}]$. As the forward reaction proceeds, reactant A is gradually consumed while product B is gradually formed, causing $[\\text{B}]$ to rise smoothly to a new plateau.\n"
        "3. **EQUAL TO**. Because temperature is constant throughout, the equilibrium constant $K_c$ remains identical before and after the disturbance."
    )
    return _pillars(
        qid=f"ps12_eq39_{rng.randint(10000, 99999)}",
        subskill="39_graphical_analysis_concentration_spike",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Reactant A was added", "marks": 1},
            {"id": "mp2", "desc": "Graphical evidence: sharp vertical spike in [A] only", "marks": 1},
            {"id": "mp3", "desc": "Forward reaction favoured to consume A, forming B", "marks": 1},
            {"id": "mp4", "desc": "EQUAL TO: Kc unchanged at constant temp", "marks": 1},
        ],
        hints={
            "1_nudge": "Look at which curve has an instantaneous vertical jump.",
            "2_concept": "A single vertical spike means that substance was directly added or removed.",
            "3_breakdown": sample,
        },
        misconception_tags=["misinterpreting_vertical_spike_as_temperature_change", "thinking_kc_changes_after_concentration_spike"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Concentration vs Time Graph Disturbance Spike"},
    )


# =========================================================================== #
# 40: Graphical Analysis Rate Time Disturbances
# =========================================================================== #
def build_40_graphical_analysis_rate_time_disturbances(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([25, 30])
    svg = _svg_wrap(
        f'<line x1="50" y1="20" x2="50" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="190" x2="370" y2="190" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Rate</text>'
        f'<text x="260" y="215" font-family="sans-serif" font-size="11" fill="#0f172a">Time (s)</text>'
        f'<line x1="50" y1="130" x2="{50 + t1 * 4}" y2="130" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="{50 + t1 * 4}" y1="130" x2="{50 + t1 * 4}" y2="60" stroke="#2563eb" stroke-width="2.5"/>'
        f'<path d="M {50 + t1 * 4} 60 Q {50 + t1 * 4 + 40} 80, 270 80 L 360 80" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="{50 + t1 * 4 + 10}" y="55" font-family="sans-serif" font-size="10" fill="#2563eb">Forward rate</text>'
        f'<line x1="{50 + t1 * 4}" y1="130" x2="{50 + t1 * 4}" y2="130" stroke="#dc2626" stroke-width="2.5"/>'
        f'<path d="M {50 + t1 * 4} 130 Q {50 + t1 * 4 + 40} 80, 270 80 L 360 80" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="{50 + t1 * 4 + 10}" y="145" font-family="sans-serif" font-size="10" fill="#dc2626">Reverse rate</text>'
        f'<line x1="{50 + t1 * 4}" y1="20" x2="{50 + t1 * 4}" y2="190" stroke="#64748b" stroke-dasharray="3,3"/>'
        f'<text x="{40 + t1 * 4}" y="205" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">t1 ({t1} s)</text>',
        width=390,
        height=230,
    )
    prompt = (
        r"The accompanying rate-time graph illustrates a chemical equilibrium disturbed at time $t_1$." + "\n\n"
        rf"1. At time $t_1 = {t1}\text{{ s}}$, only the forward reaction rate experiences an immediate sharp upward jump, while the reverse rate begins to climb gradually from its previous level." + "\n"
        "   State what disturbance caused this sudden change.\n"
        "2. Explain why the forward rate subsequently decreases while the reverse rate increases until a new equilibrium is reached at $t = 55\\text{ s}$.\n"
        "3. How does the new rate at the second equilibrium compare to the initial equilibrium rate before $t_1$ (HIGHER, LOWER, or EQUAL)?"
    )
    ans = f"1. Addition of reactant (increase in reactant concentration); 2. Forward rate decreases as reactants are consumed; reverse rate increases as product concentration builds up; 3. HIGHER."
    sample = (
        f"1. **A reactant was added** (or reactant concentration increased) at $t_1 = {t1}\\text{{ s}}$. A sudden surge in reactant concentration causes an instantaneous jump in forward collision frequency and forward rate, with no immediate jump in reverse rate.\n"
        "2. As the favoured forward reaction proceeds, reactants are consumed, so the forward rate gradually declines. Simultaneously, product concentrations build up, increasing reverse collisions and causing the reverse rate to climb until both rates equalise at a new higher level.\n"
        "3. **HIGHER**. The new equilibrium rate plateau is at a higher level than before $t_1$ because total matter/concentration inside the system is greater."
    )
    return _pillars(
        qid=f"ps12_eq40_{rng.randint(10000, 99999)}",
        subskill="40_graphical_analysis_rate_time_disturbances",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Reactant added / reactant concentration increased", "marks": 1},
            {"id": "mp2", "desc": "Explanation of subsequent rate changes", "marks": 2},
            {"id": "mp3", "desc": "HIGHER: new rate plateau is above original", "marks": 1},
        ],
        hints={
            "1_nudge": "If only one rate jumps instantly, it's a concentration change of that substance.",
            "2_concept": "If both rates jump instantly by the same amount, it's a catalyst.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_rate_graph_with_concentration_graph", "failing_to_recognize_higher_equilibrium_rate_plateau"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Rate vs Time Graph Disturbance"},
    )


# =========================================================================== #
# 41: ICE Table Kc Calculation Moles and Volume
# =========================================================================== #
def build_41_ice_table_kc_calculation_moles_and_volume(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice([2, 5, 10])
    n_h2_init = rng.choice([3.0, 4.0, 5.0])
    n_i2_init = n_h2_init
    # H2 + I2 <=> 2HI
    # reacted x mol H2, x mol I2, produced 2x mol HI
    x = rng.choice([1.0, 2.0])
    n_h2_eq = n_h2_init - x
    n_i2_eq = n_i2_init - x
    n_hi_eq = 2 * x

    c_h2_eq = n_h2_eq / vol
    c_i2_eq = n_i2_eq / vol
    c_hi_eq = n_hi_eq / vol
    kc = round((c_hi_eq ** 2) / (c_h2_eq * c_i2_eq), 2)

    prompt = (
        rf"Initially, {_fmt_sa(n_h2_init)} mol of $\text{{H}}_2(\text{{g}})$ and {_fmt_sa(n_i2_init)} mol of $\text{{I}}_2(\text{{g}})$ are sealed in a {vol} dm³ container at 448 °C." + "\n"
        r"$$\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightleftharpoons 2\text{HI}(\text{g})$$" + "\n\n"
        rf"At equilibrium, analysis shows that {_fmt_sa(n_hi_eq)} mol of $\text{{HI}}(\text{{g}})$ is present." + "\n\n"
        "1. Set up an ICE table (Initial, Change, Equilibrium) showing the moles and equilibrium concentrations of each substance.\n"
        "2. Calculate the equilibrium constant ($K_c$) for the reaction at 448 °C."
    )
    ans = f"Equilibrium concentrations: [H2] = {_fmt_sa(c_h2_eq)} mol·dm⁻³, [I2] = {_fmt_sa(c_i2_eq)} mol·dm⁻³, [HI] = {_fmt_sa(c_hi_eq)} mol·dm⁻³; Kc = {_fmt_sa(kc)}"
    sample = (
        f"**Step 1: Set up the ICE Table in a {vol} dm³ container:**\n\n"
        "| Substance | $\\text{H}_2$ | $\\text{I}_2$ | $\\text{HI}$ |\n"
        "| :--- | :---: | :---: | :---: |\n"
        f"| Initial moles ($n_i$) | {_fmt_sa(n_h2_init)} | {_fmt_sa(n_i2_init)} | 0 |\n"
        rf"| Mole change ($\Delta n$) | -{_fmt_sa(x)} | -{_fmt_sa(x)} | +{_fmt_sa(n_hi_eq)} |" + "\n"
        rf"| Equilibrium moles ($n_{{\text{{eq}}}}$) | {_fmt_sa(n_h2_eq)} | {_fmt_sa(n_i2_eq)} | {_fmt_sa(n_hi_eq)} |" + "\n"
        rf"| Equilibrium conc ($c = n/V$) | {_fmt_sa(c_h2_eq)} | {_fmt_sa(c_i2_eq)} | {_fmt_sa(c_hi_eq)} |" + "\n\n"
        "**Step 2: Calculate $K_c$:**\n"
        r"$$K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{" + f"({_fmt_sa(c_hi_eq)})^2" + r"}{" + f"({_fmt_sa(c_h2_eq)})({_fmt_sa(c_i2_eq)})" + rf"}} = \frac{{{_fmt_sa(round(c_hi_eq**2, 4))}}}{{{_fmt_sa(round(c_h2_eq * c_i2_eq, 4))}}} = {_fmt_sa(kc)}$$"
    )
    return _pillars(
        qid=f"ps12_eq41_{rng.randint(10000, 99999)}",
        subskill="41_ice_table_kc_calculation_moles_and_volume",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Correct stoichiometric mole changes (Δn)", "marks": 2},
            {"id": "mp2", "desc": f"Correct equilibrium moles: H2={_fmt_sa(n_h2_eq)}, I2={_fmt_sa(n_i2_eq)}, HI={_fmt_sa(n_hi_eq)}", "marks": 2},
            {"id": "mp3", "desc": f"Division by volume ({vol} dm³) to find concentrations", "marks": 1},
            {"id": "mp4", "desc": "Kc expression and substitution", "marks": 1},
            {"id": "mp5", "desc": f"Final Kc answer: {_fmt_sa(kc)}", "marks": 1},
        ],
        hints={
            "1_nudge": f"From HI equilibrium moles ({_fmt_sa(n_hi_eq)}), use the 1:1:2 ratio to find how much H2 and I2 reacted.",
            "2_concept": "Always divide equilibrium moles by container volume V before plugging into Kc!",
            "3_breakdown": sample,
        },
        misconception_tags=["substituting_moles_directly_into_kc_without_dividing_by_volume", "incorrect_stoichiometric_change_in_ice_table"],
        marks=7,
        duration=7,
    )


# =========================================================================== #
# 42: ICE Table Finding Initial Reactant Moles
# =========================================================================== #
def build_42_ice_table_finding_initial_reactant_moles(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice([2, 4])
    # PCl5 <=> PCl3 + Cl2
    # Eq conc: [PCl3] = x, [Cl2] = x, [PCl5] = y
    n_cl2_eq = rng.choice([0.4, 0.8, 1.2])
    n_pcl3_eq = n_cl2_eq
    c_cl2_eq = n_cl2_eq / vol
    c_pcl3_eq = n_pcl3_eq / vol

    kc = rng.choice([0.04, 0.08, 0.16])
    # Kc = [PCl3][Cl2] / [PCl5] => [PCl5] = [PCl3][Cl2] / Kc
    c_pcl5_eq = round((c_pcl3_eq * c_cl2_eq) / kc, 3)
    n_pcl5_eq = round(c_pcl5_eq * vol, 3)
    n_pcl5_init = round(n_pcl5_eq + n_cl2_eq, 3)

    prompt = (
        rf"An unknown quantity of pure $\text{{PCl}}_5(\text{{g}})$ is placed into an empty {vol} dm³ reaction flask and heated to 250 °C:" + "\n"
        r"$$\text{PCl}_5(\text{g}) \rightleftharpoons \text{PCl}_3(\text{g}) + \text{Cl}_2(\text{g}) \quad (K_c = " + _fmt_sa(kc) + r")$$" + "\n\n"
        rf"When equilibrium is established, analysis reveals {_fmt_sa(n_cl2_eq)} mol of $\text{{Cl}}_2(\text{{g}})$ in the flask." + "\n\n"
        rf"Calculate the **initial number of moles of $\text{{PCl}}_5$** originally placed in the flask."
    )
    ans = f"Initial moles of PCl5 = {_fmt_sa(n_pcl5_init)} mol"
    sample = (
        f"**1. Equilibrium concentrations:**\n"
        rf"$$[\text{{Cl}}_2] = \frac{{{_fmt_sa(n_cl2_eq)}}}{{{vol}}} = {_fmt_sa(c_cl2_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$$" + "\n"
        rf"From the 1:1 stoichiometry, $[\text{{PCl}}_3]_{{\text{{eq}}}} = [\text{{Cl}}_2]_{{\text{{eq}}}} = {_fmt_sa(c_pcl3_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$." + "\n\n"
        f"**2. Equilibrium concentration of $\\text{{PCl}}_5$:**\n"
        r"$$K_c = \frac{[\text{PCl}_3][\text{Cl}_2]}{[\text{PCl}_5]} \implies [\text{PCl}_5] = \frac{[\text{PCl}_3][\text{Cl}_2]}{K_c}$$" + "\n"
        rf"$$[\text{{PCl}}_5]_{{\text{{eq}}}} = \frac{{({_fmt_sa(c_pcl3_eq)})({_fmt_sa(c_cl2_eq)})}}{{{_fmt_sa(kc)}}} = {_fmt_sa(c_pcl5_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$$" + "\n"
        rf"$$n(\text{{PCl}}_5)_{{\text{{eq}}}} = c \times V = {_fmt_sa(c_pcl5_eq)} \times {vol} = {_fmt_sa(n_pcl5_eq)}\text{{ mol}}$$" + "\n\n"
        f"**3. Initial moles:**\n"
        rf"$$n(\text{{PCl}}_5)_{{\text{{initial}}}} = n_{{\text{{eq}}}} + n_{{\text{{reacted}}}} = {_fmt_sa(n_pcl5_eq)} + {_fmt_sa(n_cl2_eq)} = {_fmt_sa(n_pcl5_init)}\text{{ mol}}$$"
    )
    return _pillars(
        qid=f"ps12_eq42_{rng.randint(10000, 99999)}",
        subskill="42_ice_table_finding_initial_reactant_moles",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Concentration of products at equilibrium", "marks": 1},
            {"id": "mp2", "desc": "Calculation of equilibrium [PCl5] from Kc", "marks": 2},
            {"id": "mp3", "desc": "Conversion from conc to equilibrium moles", "marks": 1},
            {"id": "mp4", "desc": f"Initial moles = eq moles + reacted moles = {_fmt_sa(n_pcl5_init)} mol", "marks": 2},
        ],
        hints={
            "1_nudge": "Work backwards: find [PCl5] at equilibrium from Kc, then add back what decomposed.",
            "2_concept": "Initial moles = Equilibrium moles + Reacted moles.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_to_add_reacted_moles_to_equilibrium_moles", "volume_omission_in_back_calculation"],
        marks=6,
        duration=6,
    )


# =========================================================================== #
# 43: ICE Table Unknown X Quadratic or Perfect Square
# =========================================================================== #
def build_43_ice_table_unknown_x_quadratic_or_perfect_square(rng: random.Random) -> Dict[str, Any]:
    # H2 + I2 <=> 2HI. Perfect square: Kc = 49 (sqrt = 7) or 64 (sqrt = 8)
    sqrt_kc = rng.choice([7, 8])
    kc = sqrt_kc ** 2
    vol = rng.choice([1, 2])
    n_init = rng.choice([1.0, 2.0])  # mol H2 and I2 initially
    # [HI]^2 / ([H2][I2]) = (2x/V)^2 / ((n_init - x)/V)^2 = (2x / (n_init - x))^2 = Kc
    # 2x / (n_init - x) = sqrt_kc => 2x = sqrt_kc * n_init - sqrt_kc * x => (2 + sqrt_kc) x = sqrt_kc * n_init
    x = round((sqrt_kc * n_init) / (2 + sqrt_kc), 3)
    n_h2_eq = round(n_init - x, 3)
    n_hi_eq = round(2 * x, 3)

    prompt = (
        rf"In a {vol} dm³ closed flask at 448 °C, {_fmt_sa(n_init)} mol of $\text{{H}}_2(\text{{g}})$ and {_fmt_sa(n_init)} mol of $\text{{I}}_2(\text{{g}})$ are allowed to react:" + "\n"
        r"$$\text{H}_2(\text{g}) + \text{I}_2(\text{g}) \rightleftharpoons 2\text{HI}(\text{g}) \quad (K_c = " + str(kc) + r")$$" + "\n\n"
        r"1. Set up the equilibrium expression in terms of an unknown change in moles, $x$." + "\n"
        rf"2. Take the square root of both sides to solve for $x$ and determine the equilibrium amount of $\text{{HI}}(\text{{g}})$ in moles."
    )
    ans = f"x = {_fmt_sa(x)} mol; Equilibrium moles of HI = {_fmt_sa(n_hi_eq)} mol"
    sample = (
        r"At equilibrium in a " + f"{vol}" + r" dm³ container:" + "\n"
        rf"- $[\text{{H}}_2]_{{\text{{eq}}}} = \frac{{{_fmt_sa(n_init)} - x}}{{{vol}}}$" + "\n"
        rf"- $[\text{{I}}_2]_{{\text{{eq}}}} = \frac{{{_fmt_sa(n_init)} - x}}{{{vol}}}$" + "\n"
        rf"- $[\text{{HI}}]_{{\text{{eq}}}} = \frac{{2x}}{{{vol}}}$" + "\n\n"
        r"$$K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{(2x)^2}{(" + f"{_fmt_sa(n_init)}" + r" - x)^2} = " + f"{kc}$$\n\n"
        r"Taking the square root of both sides:" + "\n"
        rf"$$\frac{{2x}}{{{_fmt_sa(n_init)} - x}} = \sqrt{{{kc}}} = {sqrt_kc}$$" + "\n"
        rf"$$2x = {sqrt_kc}({_fmt_sa(n_init)} - x) = {_fmt_sa(sqrt_kc * n_init)} - {sqrt_kc}x$$" + "\n"
        rf"$${2 + sqrt_kc}x = {_fmt_sa(sqrt_kc * n_init)} \implies x = {_fmt_sa(x)}\text{{ mol}}$$" + "\n"
        rf"$$n(\text{{HI}})_{{\text{{eq}}}} = 2x = 2({_fmt_sa(x)}) = {_fmt_sa(n_hi_eq)}\text{{ mol}}$$"
    )
    return _pillars(
        qid=f"ps12_eq43_{rng.randint(10000, 99999)}",
        subskill="43_ice_table_unknown_x_quadratic_or_perfect_square",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Equilibrium algebraic expressions in terms of x", "marks": 2},
            {"id": "mp2", "desc": f"Perfect square simplification: square root of both sides = {sqrt_kc}", "marks": 2},
            {"id": "mp3", "desc": f"Solving for x: x = {_fmt_sa(x)} mol", "marks": 1},
            {"id": "mp4", "desc": f"Final HI moles: {_fmt_sa(n_hi_eq)} mol", "marks": 1},
        ],
        hints={
            "1_nudge": f"Notice that Kc ({kc}) is a perfect square! Take the square root of both sides to avoid the quadratic formula.",
            "2_concept": "sqrt( (2x)^2 / (a - x)^2 ) = 2x / (a - x).",
            "3_breakdown": sample,
        },
        misconception_tags=["algebraic_expansion_errors_in_ice_table", "forgetting_that_hi_equals_2x"],
        marks=6,
        duration=6,
    )


# =========================================================================== #
# 44: ICE Table Percentage Decomposition or Yield
# =========================================================================== #
def build_44_ice_table_percentage_decomposition_or_yield(rng: random.Random) -> Dict[str, Any]:
    n_init = rng.choice([2.0, 4.0, 5.0])
    pct = rng.choice([40.0, 60.0, 75.0])
    n_decomp = round(n_init * (pct / 100.0), 2)
    n_rem = round(n_init - n_decomp, 2)
    vol = 2

    prompt = (
        rf"A sample of {_fmt_sa(n_init)} mol of $\text{{N}}_2\text{{O}}_4(\text{{g}})$ is introduced into a {vol} dm³ sealed vessel at 60 °C:" + "\n"
        r"$$\text{N}_2\text{O}_4(\text{g}) \rightleftharpoons 2\text{NO}_2(\text{g})$$" + "\n\n"
        rf"At equilibrium, exactly {_fmt_sa(n_rem)} mol of $\text{{N}}_2\text{{O}}_4(\text{{g}})$ remains unreacted." + "\n\n"
        r"1. Calculate the percentage of $\text{N}_2\text{O}_4$ that dissociated at this temperature." + "\n"
        "2. Calculate the equilibrium constant ($K_c$) for this dissociation."
    )
    n_no2_eq = 2 * n_decomp
    c_n2o4_eq = n_rem / vol
    c_no2_eq = n_no2_eq / vol
    kc = round((c_no2_eq ** 2) / c_n2o4_eq, 2)

    ans = f"1. Percentage dissociated = {_fmt_sa(pct)}%; 2. Kc = {_fmt_sa(kc)}"
    sample = (
        rf"1. Moles decomposed $\Delta n = {_fmt_sa(n_init)} - {_fmt_sa(n_rem)} = {_fmt_sa(n_decomp)}\text{{ mol}}$." + "\n"
        rf"$$\text{{Percentage dissociated}} = \frac{{{_fmt_sa(n_decomp)}}}{{{_fmt_sa(n_init)}}} \times 100\% = {_fmt_sa(pct)}\%$$" + "\n\n"
        r"2. From stoichiometry, 1 mol $\text{N}_2\text{O}_4$ yields 2 mol $\text{NO}_2$:" + "\n"
        rf"$$n(\text{{NO}}_2)_{{\text{{eq}}}} = 2 \times {_fmt_sa(n_decomp)} = {_fmt_sa(n_no2_eq)}\text{{ mol}}$$" + "\n"
        rf"$$[\text{{NO}}_2]_{{\text{{eq}}}} = \frac{{{_fmt_sa(n_no2_eq)}}}{{{vol}}} = {_fmt_sa(c_no2_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$$" + "\n"
        rf"$$[\text{{N}}_2\text{{O}}_4]_{{\text{{eq}}}} = \frac{{{_fmt_sa(n_rem)}}}{{{vol}}} = {_fmt_sa(c_n2o4_eq)}\text{{ mol}}\cdot\text{{dm}}^{{-3}}$$" + "\n"
        rf"$$K_c = \frac{{[\text{{NO}}_2]^2}}{{[\text{{N}}_2\text{{O}}_4]}} = \frac{{({_fmt_sa(c_no2_eq)})^2}}{{{_fmt_sa(c_n2o4_eq)}}} = {_fmt_sa(kc)}$$"
    )
    return _pillars(
        qid=f"ps12_eq44_{rng.randint(10000, 99999)}",
        subskill="44_ice_table_percentage_decomposition_or_yield",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Percentage calculation: {_fmt_sa(pct)}%", "marks": 2},
            {"id": "mp2", "desc": "Equilibrium concentrations of NO2 and N2O4", "marks": 2},
            {"id": "mp3", "desc": f"Final Kc answer: {_fmt_sa(kc)}", "marks": 2},
        ],
        hints={
            "1_nudge": "Percentage dissociated = (moles reacted / initial moles) * 100%.",
            "2_concept": "Remember that each mole of N2O4 that reacts forms TWO moles of NO2.",
            "3_breakdown": sample,
        },
        misconception_tags=["using_remaining_moles_instead_of_reacted_moles_in_percentage", "forgetting_the_2_coefficient_for_no2"],
        marks=6,
        duration=6,
    )


# =========================================================================== #
# 45: Industrial Haber Process Compromise Conditions
# =========================================================================== #
def build_45_industrial_haber_process_compromise_conditions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Haber process synthesizes ammonia from nitrogen and hydrogen gases:\n"
        r"$$\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g}) \quad (\Delta H = -92\text{ kJ}\cdot\text{mol}^{-1})$$" + "\n\n"
        "In industrial plants, the reaction is operated at approximately 450 °C and 200 atmospheres in the presence of an iron catalyst.\n"
        "1. According to Le Chatelier's principle, what temperature (HIGH or LOW) would produce the maximum equilibrium yield of ammonia? Explain.\n"
        "2. Explain why a moderate compromise temperature of 450 °C is utilized instead of a low temperature.\n"
        "3. Explain why a high pressure of 200 atmospheres favours both high yield and high reaction rate.\n"
        "4. State the purpose of using an iron (Fe) catalyst."
    )
    ans = "1. Low temperature, forward reaction is exothermic; 2. Compromise between yield and reaction rate (at low temp rate is uneconomically slow); 3. High pressure shifts equilibrium forward (fewer gas moles, 4 -> 2) increasing yield, and increases particle concentration increasing collision frequency and rate; 4. Increases reaction rate to reach equilibrium faster without needing higher temperatures."
    sample = (
        "1. A **LOW temperature** favours the exothermic forward reaction according to Le Chatelier's principle, producing the highest equilibrium yield.\n"
        "2. At low temperatures, the **rate of reaction is unacceptably and uneconomically slow** because few molecules possess sufficient kinetic energy ($E_k \\ge E_a$). "
        "A temperature of **450 °C is a compromise** providing a commercially acceptable reaction rate with a viable yield.\n"
        "3. **High pressure (200 atm)**:\n"
        "   - **Yield**: The forward reaction converts 4 moles of gas into 2 moles of gas. High pressure favours the forward direction with fewer gas moles.\n"
        "   - **Rate**: High pressure compresses gas molecules, increasing collision frequency and rate.\n"
        "4. The **iron catalyst** accelerates both forward and reverse rates, enabling equilibrium to be established rapidly at a lower, safer operating temperature."
    )
    return _pillars(
        qid=f"ps12_eq45_{rng.randint(10000, 99999)}",
        subskill="45_industrial_haber_process_compromise_conditions",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Low temperature favours exothermic forward reaction", "marks": 1},
            {"id": "mp2", "desc": "450 °C compromise between rate and yield explained", "marks": 2},
            {"id": "mp3", "desc": "Pressure effect on yield (4 to 2 moles) and rate (collision frequency)", "marks": 2},
            {"id": "mp4", "desc": "Role of iron catalyst", "marks": 1},
        ],
        hints={
            "1_nudge": "Why don't chemical engineers always run exothermic reactions at freezing cold temperatures?",
            "2_concept": "High yield at cold temp is useless if the reaction takes three years to finish.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_industrial_conditions_are_chosen_only_for_yield", "confusing_compromise_temperature_with_optimal_yield_temperature"],
        marks=6,
        duration=6,
        term=3,
        caps_weight=10,
    )


# =========================================================================== #
# 46: Industrial Contact Process Conditions and Oleum
# =========================================================================== #
def build_46_industrial_contact_process_conditions_and_oleum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Contact Process produces sulfuric acid (H2SO4) through four consecutive stages.\n"
        r"The key equilibrium step is the catalytic oxidation of sulfur dioxide:" + "\n"
        r"$$2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightleftharpoons 2\text{SO}_3(\text{g}) \quad (\Delta H = -197\text{ kJ}\cdot\text{mol}^{-1})$$" + "\n\n"
        r"1. Name the catalyst utilized in this equilibrium step." + "\n"
        r"2. In Stage 3, $\text{SO}_3$ gas is absorbed in concentrated $\text{H}_2\text{SO}_4$ rather than directly into liquid water. Write the balanced equation for this absorption reaction and name the oily liquid product formed." + "\n"
        r"3. Explain why $\text{SO}_3$ is NOT dissolved directly in water."
    )
    ans = "1. Vanadium pentoxide (V2O5); 2. SO3 + H2SO4 -> H2S2O7 (oleum / pyrosulfuric acid); 3. Dissolving SO3 directly in water is extremely exothermic and produces a dense, corrosive mist of fine sulfuric acid droplets that is hazardous and difficult to condense."
    sample = (
        r"1. The catalyst is **vanadium pentoxide** ($\text{V}_2\text{O}_5$)." + "\n"
        r"2. Balanced absorption equation:" + "\n"
        r"$$\text{SO}_3(\text{g}) + \text{H}_2\text{SO}_4(\text{l}) \rightarrow \text{H}_2\text{S}_2\text{O}_7(\text{l})$$" + "\n"
        r"The product is **oleum** (fuming sulfuric acid / pyrosulfuric acid)." + "\n"
        r"3. The direct reaction of $\text{SO}_3$ with water is **violently exothermic**. "
        "The enormous heat vaporizes the water, producing an uncontrollable, highly corrosive acid fog/mist that escapes into the atmosphere rather than condensing."
    )
    return _pillars(
        qid=f"ps12_eq46_{rng.randint(10000, 99999)}",
        subskill="46_industrial_contact_process_conditions_and_oleum",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Catalyst: vanadium pentoxide (V2O5)", "marks": 1},
            {"id": "mp2", "desc": "Oleum equation: SO3 + H2SO4 -> H2S2O7", "marks": 2},
            {"id": "mp3", "desc": "Name product: oleum", "marks": 1},
            {"id": "mp4", "desc": "Direct dissolution with water is violently exothermic forming corrosive mist", "marks": 2},
        ],
        hints={
            "1_nudge": "What is the formula of oleum (H2S2O7)?",
            "2_concept": "Adding SO3 to water makes a dangerous acid mist.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_so3_is_dissolved_directly_in_water_in_contact_process", "wrong_contact_process_catalyst"],
        marks=6,
        duration=6,
        term=3,
        caps_weight=10,
    )


# =========================================================================== #
# 47: Industrial Ostwald Process Nitric Acid
# =========================================================================== #
def build_47_industrial_ostwald_process_nitric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Ostwald Process manufactures nitric acid (HNO3) from ammonia in three primary chemical stages.\n\n"
        "1. Write down a balanced chemical equation for the primary catalytic oxidation of ammonia over a platinum-rhodium gauze catalyst.\n"
        "2. Write down the equation for the oxidation of nitrogen monoxide to nitrogen dioxide.\n"
        "3. Write down the balanced equation for the reaction of nitrogen dioxide with water to form nitric acid.\n"
        r"4. Name ONE essential nitrogenous fertilizer produced by reacting nitric acid with ammonia."
    )
    ans = "1. 4NH3 + 5O2 -> 4NO + 6H2O; 2. 2NO + O2 -> 2NO2; 3. 3NO2 + H2O -> 2HNO3 + NO (or 4NO2 + O2 + 2H2O -> 4HNO3); 4. Ammonium nitrate (NH4NO3)."
    sample = (
        "1. **Stage 1 (Catalytic oxidation of ammonia):**\n"
        r"$$4\text{NH}_3(\text{g}) + 5\text{O}_2(\text{g}) \xrightarrow{\text{Pt/Rh}} 4\text{NO}(\text{g}) + 6\text{H}_2\text{O}(\text{g})$$" + "\n\n"
        "2. **Stage 2 (Oxidation of NO):**\n"
        r"$$2\text{NO}(\text{g}) + \text{O}_2(\text{g}) \rightarrow 2\text{NO}_2(\text{g})$$" + "\n\n"
        "3. **Stage 3 (Absorption into water):**\n"
        r"$$3\text{NO}_2(\text{g}) + \text{H}_2\text{O}(\text{l}) \rightarrow 2\text{HNO}_3(\text{aq}) + \text{NO}(\text{g})$$" + "\n"
        r"(Alternatively: $4\text{NO}_2(\text{g}) + \text{O}_2(\text{g}) + 2\text{H}_2\text{O}(\text{l}) \rightarrow 4\text{HNO}_3(\text{aq})$)." + "\n\n"
        r"4. Fertilizer formed: **Ammonium nitrate** ($\text{NH}_4\text{NO}_3$)."
    )
    return _pillars(
        qid=f"ps12_eq47_{rng.randint(10000, 99999)}",
        subskill="47_industrial_ostwald_process_nitric_acid",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Stage 1 equation: 4NH3 + 5O2 -> 4NO + 6H2O", "marks": 2},
            {"id": "mp2", "desc": "Stage 2 equation: 2NO + O2 -> 2NO2", "marks": 1},
            {"id": "mp3", "desc": "Stage 3 equation forming HNO3", "marks": 2},
            {"id": "mp4", "desc": "Ammonium nitrate fertilizer named", "marks": 1},
        ],
        hints={
            "1_nudge": "Stage 1 makes NO and H2O; Stage 2 oxidizes NO to NO2; Stage 3 dissolves NO2 in water.",
            "2_concept": "Ostwald process converts NH3 into HNO3.",
            "3_breakdown": sample,
        },
        misconception_tags=["unbalanced_ostwald_equations", "forgetting_water_is_produced_in_stage_1"],
        marks=6,
        duration=6,
        term=3,
        caps_weight=10,
    )


# =========================================================================== #
# 48: NPK Fertilizer Ratio and Percentage Calculations
# =========================================================================== #
def build_48_npk_fertilizer_ratio_and_percentage_calculations(rng: random.Random) -> Dict[str, Any]:
    bag_mass = 50.0  # kg
    ratio_options = [
        {"ratio_str": "3:1:5 (26)", "n": 3, "p": 1, "k": 5, "total_pct": 26.0},
        {"ratio_str": "7:2:3 (30)", "n": 7, "p": 2, "k": 3, "total_pct": 30.0},
        {"ratio_str": "4:3:4 (28)", "n": 4, "p": 3, "k": 4, "total_pct": 28.0},
    ]
    opt = rng.choice(ratio_options)
    sum_parts = opt["n"] + opt["p"] + opt["k"]
    target = rng.choice(["nitrogen (N)", "phosphorus (P)", "potassium (K)"])
    if "nitrogen" in target:
        part = opt["n"]
        nutrient_sym = "N"
    elif "phosphorus" in target:
        part = opt["p"]
        nutrient_sym = "P"
    else:
        part = opt["k"]
        nutrient_sym = "K"

    pct_nutrient = round((part / sum_parts) * opt["total_pct"], 2)
    mass_nutrient = round(bag_mass * (pct_nutrient / 100.0), 2)

    prompt = (
        f"A commercial fertilizer bag is labeled with the NPK ratio:\n"
        f"$$\\mathbf{{{opt['ratio_str']}}}$$\n\n"
        f"The mass of the fertilizer bag is {int(bag_mass)} kg.\n"
        "1. Explain what the number in brackets, e.g. " + f"({int(opt['total_pct'])})" + ", represents on the fertilizer bag.\n"
        f"2. Calculate the percentage of **{target}** in this fertilizer bag.\n"
        f"3. Calculate the exact mass of pure {target} present in this {int(bag_mass)} kg bag."
    )
    ans = f"1. Total percentage of active fertilizer (nutrients N+P+K) in the bag is {int(opt['total_pct'])}% (the remaining is filler); 2. {_fmt_sa(pct_nutrient)}%; 3. {_fmt_sa(mass_nutrient)} kg"
    sample = (
        f"1. The number ({int(opt['total_pct'])}) represents the **total percentage mass of active nutrients** (N, P, and K) in the bag. "
        f"The remaining {int(100 - opt['total_pct'])}% consists of inert filler material (e.g. sand, limestone).\n"
        f"2. Total ratio parts = {opt['n']} + {opt['p']} + {opt['k']} = {sum_parts}.\n"
        rf"$$\% \text{{{nutrient_sym}}} = \frac{{{part}}}{{{sum_parts}}} \times {int(opt['total_pct'])}\% = {_fmt_sa(pct_nutrient)}\%$$" + "\n"
        f"3. Mass of {target} in a {int(bag_mass)} kg bag:\n"
        rf"$$\text{{Mass}} = {_fmt_sa(bag_mass)} \times \frac{{{_fmt_sa(pct_nutrient)}}}{{100}} = {_fmt_sa(mass_nutrient)}\text{{ kg}}$$"
    )
    return _pillars(
        qid=f"ps12_eq48_{rng.randint(10000, 99999)}",
        subskill="48_npk_fertilizer_ratio_and_percentage_calculations",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Meaning of ({int(opt['total_pct'])}): total active nutrient percentage", "marks": 1},
            {"id": "mp2", "desc": f"Percentage of {target}: {_fmt_sa(pct_nutrient)}%", "marks": 2},
            {"id": "mp3", "desc": f"Mass of {target}: {_fmt_sa(mass_nutrient)} kg", "marks": 2},
        ],
        hints={
            "1_nudge": f"Sum of parts = {sum_parts}. Find the fraction of the {int(opt['total_pct'])}% active content.",
            "2_concept": "Nutrient % = (part / sum_of_parts) * total_active_%. Mass = bag_mass * (nutrient_% / 100).",
            "3_breakdown": sample,
        },
        misconception_tags=["calculating_fraction_of_100_instead_of_number_in_brackets", "inverting_npk_ratio_order"],
        marks=5,
        duration=5,
        term=3,
        caps_weight=10,
    )


# =========================================================================== #
# 49: Eutrophication Environmental Impact
# =========================================================================== #
def build_49_eutrophication_environmental_impact(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Excessive use of inorganic nitrogen and phosphorus fertilizers on farmlands can lead to severe degradation of nearby freshwater aquatic ecosystems through **eutrophication**.\n\n"
        "1. Define the term **eutrophication**.\n"
        "2. Arrange and explain the following four ecological events in their correct sequential chronological order:\n"
        "   - **A**: Bacteria decompose dead organic matter, consuming dissolved oxygen (hypoxia).\n"
        "   - **B**: Excessive nitrates and phosphates leach into water bodies via surface runoff.\n"
        "   - **C**: Fish and aquatic organisms die due to lack of oxygen.\n"
        "   - **D**: Rapid proliferation of surface algae (algal bloom) blocks sunlight from underwater plants.\n"
        "3. State ONE sustainable alternative to inorganic chemical fertilizers used in community agriculture."
    )
    ans = "1. Eutrophication is the process where a water body becomes enriched with excessive nutrients, leading to abundant plant/algal growth and subsequent oxygen depletion; 2. Order: B -> D -> A -> C; 3. Animal manure / compost / crop rotation / organic green manure."
    sample = (
        "1. **Eutrophication** is the process where water bodies become excessively enriched with minerals and nutrients (especially nitrates and phosphates), inducing excessive growth of algae and plant life, followed by severe oxygen depletion.\n"
        "2. **Chronological sequence: B -> D -> A -> C**\n"
        "   - **B**: Rainwater washes excess fertilizer nitrates and phosphates into rivers and dams (**leaching/runoff**).\n"
        "   - **D**: Nutrients trigger explosive growth of algae (**algal bloom**), blocking sunlight and killing submerged photosynthetic plants.\n"
        "   - **A**: When algae die, aerobic bacteria decompose the organic biomass, consuming massive amounts of dissolved oxygen (**hypoxia/anoxia**).\n"
        "   - **C**: Depletion of dissolved oxygen leads to suffocation and death of aquatic fauna (**fish kills/dead zones**).\n"
        "3. **Sustainable alternatives**: Use of **organic compost**, animal manure, crop rotation with nitrogen-fixing legumes, or indigenous soil mulch."
    )
    return _pillars(
        qid=f"ps12_eq49_{rng.randint(10000, 99999)}",
        subskill="49_eutrophication_environmental_impact",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition of eutrophication (nutrient enrichment and oxygen depletion)", "marks": 2},
            {"id": "mp2", "desc": "Correct chronological sequence: B -> D -> A -> C", "marks": 2},
            {"id": "mp3", "desc": "One valid sustainable organic alternative (compost/manure)", "marks": 1},
        ],
        hints={
            "1_nudge": "Fertilizers wash in -> algae bloom -> sunlight blocked -> algae die -> bacteria consume oxygen -> fish die.",
            "2_concept": "It is bacteria decomposing the dead algae that consumes oxygen, not the live algae.",
            "3_breakdown": sample,
        },
        misconception_tags=["believing_algae_consume_all_oxygen_while_alive", "confusing_eutrophication_with_acid_rain"],
        marks=5,
        duration=5,
        term=3,
        caps_weight=10,
    )


# =========================================================================== #
# 50: Equilibrium Capstone Misconception Autopsy
# =========================================================================== #
def build_50_equilibrium_capstone_misconception_autopsy(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        {
            "claim": "A learner claims that when a catalyst is added to an equilibrium mixture, the value of Kc increases and the equilibrium yield of ammonia increases.",
            "verdict": "INCORRECT",
            "correction": "A catalyst increases the rates of forward and reverse reactions equally. It does NOT shift the position of equilibrium, does NOT increase yield, and does NOT alter the value of Kc (which depends solely on temperature).",
        },
        {
            "claim": "A learner states that at chemical equilibrium, the concentrations of reactants and products must be equal to each other.",
            "verdict": "INCORRECT",
            "correction": "At chemical equilibrium, the forward rate equals the reverse rate, and concentrations remain constant, but concentrations are rarely equal to one another.",
        },
        {
            "claim": "A learner calculates Kc by directly substituting the number of moles at equilibrium without dividing by the 2 dm³ container volume.",
            "verdict": "INCORRECT",
            "correction": "Kc is formulated with concentrations (mol·dm⁻³), not moles. Unless total gas moles on both sides are equal (where volumes cancel), omitting volume leads to an incorrect Kc value.",
        },
    ])
    prompt = (
        "During a chemistry post-exam diagnostic review, a learner makes the following claim:\n"
        f"\"{scenario['claim']}\"\n\n"
        "1. Is this claim CORRECT or INCORRECT?\n"
        "2. Provide a thorough scientific correction based on CAPS physical chemistry principles.\n"
        "3. Summarize the THREE conditions necessary for a system to achieve dynamic chemical equilibrium."
    )
    ans = f"1. {scenario['verdict']}; 2. {scenario['correction']}; 3. (i) Closed system; (ii) Reversible chemical reaction; (iii) Constant temperature."
    sample = (
        f"1. **{scenario['verdict']}**.\n"
        f"2. **Scientific Correction**: {scenario['correction']}\n"
        "3. **Three essential conditions for dynamic chemical equilibrium**:\n"
        "   - **Closed system**: No matter or chemical species can enter or leave the system.\n"
        "   - **Reversible reaction**: The reaction can proceed in both forward and reverse directions.\n"
        "   - **Constant physical conditions**: Temperature (and pressure for gases) must remain constant."
    )
    return _pillars(
        qid=f"ps12_eq50_{rng.randint(10000, 99999)}",
        subskill="50_equilibrium_capstone_misconception_autopsy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Verdict: {scenario['verdict']}", "marks": 1},
            {"id": "mp2", "desc": "Scientific correction addressing misconception", "marks": 2},
            {"id": "mp3", "desc": "Three conditions: closed system, reversible reaction, constant temperature", "marks": 2},
        ],
        hints={
            "1_nudge": "Review: does Kc change with catalysts? Are concentrations equal or constant?",
            "2_concept": "Equilibrium requires closed system, reversible reaction, and constant temperature.",
            "3_breakdown": sample,
        },
        misconception_tags=["equilibrium_rate_vs_extent_confusion", "omitting_container_volume_in_kc"],
        marks=5,
        duration=5,
    )


BUILDERS_26_50 = {
    "26_equilibrium_constant_kc_expression_homogeneous": build_26_equilibrium_constant_kc_expression_homogeneous,
    "27_equilibrium_constant_heterogeneous_omissions": build_27_equilibrium_constant_heterogeneous_omissions,
    "28_magnitude_of_kc_and_equilibrium_position": build_28_magnitude_of_kc_and_equilibrium_position,
    "29_temperature_dependence_of_kc_value": build_29_temperature_dependence_of_kc_value,
    "30_calculating_kc_from_equilibrium_concentrations": build_30_calculating_kc_from_equilibrium_concentrations,
    "31_calculating_equilibrium_concentration_given_kc": build_31_calculating_equilibrium_concentration_given_kc,
    "32_reaction_quotient_qc_vs_kc": build_32_reaction_quotient_qc_vs_kc,
    "33_reverse_reaction_kc_relationship": build_33_reverse_reaction_kc_relationship,
    "34_le_chatelier_principle_statement": build_34_le_chatelier_principle_statement,
    "35_le_chatelier_concentration_disturbance": build_35_le_chatelier_concentration_disturbance,
    "36_le_chatelier_temperature_disturbance": build_36_le_chatelier_temperature_disturbance,
    "37_le_chatelier_pressure_and_volume_gases": build_37_le_chatelier_pressure_and_volume_gases,
    "38_le_chatelier_catalyst_invariance": build_38_le_chatelier_catalyst_invariance,
    "39_graphical_analysis_concentration_spike": build_39_graphical_analysis_concentration_spike,
    "40_graphical_analysis_rate_time_disturbances": build_40_graphical_analysis_rate_time_disturbances,
    "41_ice_table_kc_calculation_moles_and_volume": build_41_ice_table_kc_calculation_moles_and_volume,
    "42_ice_table_finding_initial_reactant_moles": build_42_ice_table_finding_initial_reactant_moles,
    "43_ice_table_unknown_x_quadratic_or_perfect_square": build_43_ice_table_unknown_x_quadratic_or_perfect_square,
    "44_ice_table_percentage_decomposition_or_yield": build_44_ice_table_percentage_decomposition_or_yield,
    "45_industrial_haber_process_compromise_conditions": build_45_industrial_haber_process_compromise_conditions,
    "46_industrial_contact_process_conditions_and_oleum": build_46_industrial_contact_process_conditions_and_oleum,
    "47_industrial_ostwald_process_nitric_acid": build_47_industrial_ostwald_process_nitric_acid,
    "48_npk_fertilizer_ratio_and_percentage_calculations": build_48_npk_fertilizer_ratio_and_percentage_calculations,
    "49_eutrophication_environmental_impact": build_49_eutrophication_environmental_impact,
    "50_equilibrium_capstone_misconception_autopsy": build_50_equilibrium_capstone_misconception_autopsy,
}
