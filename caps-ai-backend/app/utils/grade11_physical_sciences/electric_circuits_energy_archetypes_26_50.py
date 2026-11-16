"""Grade 11 Physical Sciences — Term 3: Electric Circuits (Archetypes 26–50).
Deterministic 6-pillar generators grounded in South African National Curriculum Standards:
- Subskills 26–35: Internal resistance with composite loads, terminal potential difference vs current
  graphical analysis, switch toggling effects on terminal PD, electrical power (P = VI = I^2R = V^2/R),
  electrical work/energy in joules (W = VIt), and bulb brightness in series vs parallel networks.
- Subskills 36–50: Household 230 V parallel circuits, fuse selection, kilowatt-hour (kWh) conversions,
  single and multi-appliance electricity cost calculations, South African municipal inclining block
  tariffs, LED & geyser energy-saving audits, prepaid vouchers, kettle thermal efficiency, backup
  battery Ah capacity, proportional scaling, capstone synthesis, and diagnostic misconception repair.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

from app.utils.grade11_physical_sciences.electric_circuits_energy_archetypes_01_25 import (
    _svg_composite_circuit,
    fmt_sa,
    make_payload,
    rng,
)


def _svg_v_terminal_vs_i(emf: float, r_int: float) -> str:
    i_short = round(emf / r_int, 1)
    i_mid = round(i_short / 2, 1)
    v_mid = round(emf / 2, 1)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 280">'
        f'<rect width="420" height="280" fill="#ffffff"/>'
        f'<text x="215" y="24" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e293b">'
        f'Terminal Potential Difference (V) vs Current (I)</text>'
        f'<line x1="65" y1="230" x2="375" y2="230" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="230" x2="65" y2="40" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="55" x2="345" y2="230" stroke="#dc2626" stroke-width="3"/>'
        f'<line x1="205" y1="230" x2="205" y2="142" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<line x1="65" y1="142" x2="205" y2="142" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>'
        f'<circle cx="65" cy="55" r="4.5" fill="#b91c1c"/>'
        f'<circle cx="205" cy="142" r="4" fill="#b91c1c"/>'
        f'<circle cx="345" cy="230" r="4.5" fill="#b91c1c"/>'
        f'<text x="55" y="59" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="bold" fill="#334155">{emf}</text>'
        f'<text x="55" y="146" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">{v_mid}</text>'
        f'<text x="60" y="246" text-anchor="end" font-family="sans-serif" font-size="11" fill="#334155">0</text>'
        f'<text x="205" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">{i_mid}</text>'
        f'<text x="345" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#334155">{i_short}</text>'
        f'<text x="220" y="270" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Current I (A)</text>'
        f'<text x="18" y="135" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" transform="rotate(-90 18 135)">Terminal PD V (V)</text>'
        f'</svg>'
    )


# ---------------------------------------------------------------------------
# Subskill 26: Internal resistance with series-parallel load
# ---------------------------------------------------------------------------
def arch_26_internal_resistance_with_series_parallel_load(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([2, 3, 4, 5])
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5)])
    rp = int((r1 * r2) // (r1 + r2))
    r_ext = rs + rp
    r_int = r.choice([0.5, 1.0, 1.5, 2.0])
    i_tot = r.choice([1.5, 2.0, 2.5, 3.0])
    emf = round(i_tot * (r_ext + r_int), 2)
    v_term = round(i_tot * r_ext, 2)
    v_lost = round(i_tot * r_int, 2)

    prompt = (
        f"A battery with emf **$\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$** and internal resistance **$r = {fmt_sa(r_int)}\\ \\Omega$** "
        f"is connected to an external circuit consisting of a series resistor **$R_s = {rs}\\ \\Omega$** and a parallel bank "
        f"of **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n\n"
        f"1. Calculate the total external resistance ($R_{{\\text{{ext}}}}$) of the circuit.\n"
        f"2. Calculate the main-branch current ($I$) drawn from the battery.\n"
        f"3. Calculate the terminal potential difference ($V_{{\\text{{terminal}}}}$) across the battery and the 'lost volts' ($V_{{\\text{{internal}}}}$)."
    )

    ans_latex = rf"R_{{\text{{ext}}}} = {r_ext}\ \Omega, \ I = {fmt_sa(i_tot)}\text{{ A}}, \ V_{{\text{{term}}}} = {fmt_sa(v_term)}\text{{ V}}, \ V_{{\text{{lost}}}} = {fmt_sa(v_lost)}\text{{ V}}"
    sample_answer = (
        f"1. $$R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {rp}\\ \\Omega \\implies R_{{\\text{{ext}}}} = R_s + R_p = {rs} + {rp} = {r_ext}\\ \\Omega$$\n\n"
        f"2. $$\\mathcal{{E}} = I(R_{{\\text{{ext}}}} + r) \\implies I = \\frac{{{fmt_sa(emf)}}}{{{r_ext} + {fmt_sa(r_int)}}} = {fmt_sa(i_tot)}\\text{{ A}}$$\n\n"
        f"3. $$V_{{\\text{{terminal}}}} = I \\cdot R_{{\\text{{ext}}}} = {fmt_sa(i_tot)} \\times {r_ext} = {fmt_sa(v_term)}\\text{{ V}}$$\n"
        f"   $$V_{{\\text{{internal}}}} = I \\cdot r = {fmt_sa(i_tot)} \\times {fmt_sa(r_int)} = {fmt_sa(v_lost)}\\text{{ V}}$$"
    )

    return make_payload(
        "26_internal_resistance_with_series_parallel_load",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate Rp = {rp} Ohm and R_ext = {r_ext} Ohm", 2),
            (f"Calculate current I = {fmt_sa(i_tot)} A using E = I(R_ext + r)", 2),
            (f"Calculate V_terminal = {fmt_sa(v_term)} V and V_internal = {fmt_sa(v_lost)} V", 2),
        ],
        [
            "Find the total external resistance $R_{\\text{ext}} = R_s + R_p$ first, then add internal resistance $r$.",
            f"Use $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{ext}}}} + r}} = \\frac{{{fmt_sa(emf)}}}{{{fmt_sa(r_ext + r_int)}}}$.",
            f"$R_{{\\text{{ext}}}} = {r_ext}\\ \\Omega$, $I = {fmt_sa(i_tot)}\\text{{ A}}$, $V_{{\\text{{term}}}} = {fmt_sa(v_term)}\\text{{ V}}$, $V_{{\\text{{lost}}}} = {fmt_sa(v_lost)}\\text{{ V}}$.",
        ],
        ["forgetting_internal_resistance_when_finding_main_current", "using_emf_as_parallel_voltage"],
        ["internal resistance", "composite load", "terminal voltage"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 27: Terminal voltage vs current graph analysis (with inline SVG)
# ---------------------------------------------------------------------------
def arch_27_terminal_voltage_vs_current_graph_analysis(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    emf, r_int = r.choice([
        (12.0, 1.5),
        (12.0, 2.0),
        (15.0, 2.5),
        (18.0, 1.5),
        (18.0, 3.0),
        (24.0, 2.0),
        (9.0, 1.5),
    ])
    i_short = round(emf / r_int, 2)
    svg = _svg_v_terminal_vs_i(emf, r_int)

    prompt = (
        f"During an experiment to determine the emf ($\\mathcal{{E}}$) and internal resistance ($r$) of a battery, "
        f"a learner plots terminal potential difference ($V$) on the vertical axis against current ($I$) on the horizontal axis.\n"
        f"The straight line intersects the vertical axis at **$(0\\text{{ A}}; {fmt_sa(emf)}\\text{{ V}})$** and the horizontal axis at **$( {fmt_sa(i_short)}\\text{{ A}}; 0\\text{{ V}})$**.\n\n"
        f"1. Write down the equation of the straight line in the form $V = mI + c$ in terms of $\\mathcal{{E}}$, $r$, and $I$.\n"
        f"2. Write down the value of the **emf** ($\\mathcal{{E}}$) from the vertical intercept.\n"
        f"3. Calculate the gradient of the line and hence state the **internal resistance** ($r$) of the battery.\n"
        f"4. State the physical meaning of the horizontal intercept ($I = {fmt_sa(i_short)}\\text{{ A}}$)."
    )

    ans_latex = rf"\mathcal{{E}} = {fmt_sa(emf)}\text{{ V}}, \ r = {fmt_sa(r_int)}\ \Omega, \ I_{{\text{{short}}}} = {fmt_sa(i_short)}\text{{ A}}"
    sample_answer = (
        f"1. Since $\\mathcal{{E}} = V + Ir$, rearranging into straight-line form gives:\n"
        f"   $$V = -rI + \\mathcal{{E}}$$\n\n"
        f"2. Vertical intercept ($I = 0\\text{{ A}}$): **$\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$**.\n\n"
        f"3. $$\\text{{Gradient}} = \\frac{{0 - {fmt_sa(emf)}}}{{{fmt_sa(i_short)} - 0}} = -{fmt_sa(r_int)}\\ \\Omega$$\n"
        f"   Since $\\text{{gradient}} = -r$, the internal resistance is **$r = {fmt_sa(r_int)}\\ \\Omega$**.\n\n"
        f"4. The horizontal intercept ($V = 0\\text{{ V}}, I = {fmt_sa(i_short)}\\text{{ A}}$) represents the **maximum (short-circuit) current** "
        f"when the external resistance is zero ($R_{{\\text{{ext}}}} = 0\\ \\Omega$)."
    )

    return make_payload(
        "27_terminal_voltage_vs_current_graph_analysis",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Write equation V = -rI + E", 1),
            (f"Identify emf E = {fmt_sa(emf)} V from y-intercept", 1),
            (f"Calculate gradient = -{fmt_sa(r_int)} and internal resistance r = {fmt_sa(r_int)} Ohm", 2),
            ("Explain x-intercept as maximum / short-circuit current when R_ext = 0", 2),
        ],
        [
            "Rearrange $\\mathcal{E} = V + Ir$ to make $V$ the subject: $V = -rI + \\mathcal{E}$.",
            f"The y-intercept is $\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$ and the magnitude of the gradient is $r = \\frac{{{fmt_sa(emf)}}}{{{fmt_sa(i_short)}}}$.",
            f"$\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$, $r = {fmt_sa(r_int)}\\ \\Omega$, short-circuit current $= {fmt_sa(i_short)}\\text{{ A}}$.",
        ],
        ["reporting_negative_value_for_internal_resistance", "confusing_x_intercept_with_operating_current"],
        ["V vs I intercept", "internal resistance gradient", "short-circuit current"],
        difficulty="medium",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 28: Switch effect on terminal potential difference of a real battery
# ---------------------------------------------------------------------------
def arch_28_switch_effect_on_terminal_potential_difference(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    action = r.choice(["closed", "opened"])
    emf = r.choice([12.0, 15.0, 18.0, 24.0])
    r_int = r.choice([1.0, 1.5, 2.0])
    r1 = r.choice([6.0, 8.0, 12.0])

    if action == "closed":
        r_ext_Change = "DECREASES"
        i_change = "INCREASES"
        vlost_change = "INCREASES"
        vterm_change = "DECREASES"
    else:
        r_ext_Change = "INCREASES"
        i_change = "DECREASES"
        vlost_change = "DECREASES"
        vterm_change = "INCREASES"

    prompt = (
        f"A battery of emf $\\mathcal{{E}} = {fmt_sa(emf)}\\text{{ V}}$ and significant internal resistance $r = {fmt_sa(r_int)}\\ \\Omega$ "
        f"is connected across two parallel branches: branch 1 has resistor $R_1 = {fmt_sa(r1)}\\ \\Omega$, and branch 2 has resistor $R_2 = {fmt_sa(r1)}\\ \\Omega$ with switch $S$.\n"
        f"A voltmeter $V$ is connected across the terminals of the battery.\n\n"
        f"Switch $S$ is now **{action}**.\n"
        f"1. State whether the reading on voltmeter $V$ **increases, decreases, or remains the same**.\n"
        f"2. Provide a step-by-step causal explanation referring to $R_{{\\text{{ext}}}}$, main current $I$, internal 'lost volts' ($V_{{\\text{{internal}}}} = Ir$), and $\\mathcal{{E}}$."
    )

    ans_latex = rf"V_{{\text{{terminal}}}} \text{{ {vterm_change} }} (\Delta R_{{\text{{ext}}}} \to \Delta I \to \Delta V_{{\text{{lost}}}} \to \Delta V_{{\text{{term}}}})"
    sample_answer = (
        f"1. The reading on voltmeter $V$ **{vterm_change}**.\n\n"
        f"2. **Step-by-step explanation:**\n"
        f"   - When switch $S$ is {action}, the total external resistance $R_{{\\text{{ext}}}}$ **{r_ext_Change.lower()}**.\n"
        f"   - Since $\\mathcal{{E}}$ and $r$ are constant and $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{ext}}}} + r}}$, the total current $I$ in the circuit **{i_change.lower()}**.\n"
        f"   - The 'lost volts' across the internal resistance ($V_{{\\text{{internal}}}} = I \\cdot r$) therefore **{vlost_change.lower()}**.\n"
        f"   - Since $V_{{\\text{{terminal}}}} = \\mathcal{{E}} - V_{{\\text{{internal}}}}$ and $\\mathcal{{E}}$ is constant, $V_{{\\text{{terminal}}}}$ **{vterm_change.lower()}**."
    )

    return make_payload(
        "28_switch_effect_on_terminal_potential_difference",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"State V_terminal {vterm_change}", 1),
            (f"State R_ext {r_ext_Change.lower()} when parallel switch is {action}", 1),
            (f"State total current I {i_change.lower()}", 1),
            (f"State lost volts Ir {vlost_change.lower()} and conclude V_term = E - Ir {vterm_change.lower()}", 2),
        ],
        [
            "Use the 4-step chain: $R_{\\text{ext}} \\to I_{\\text{main}} \\to V_{\\text{lost}} (= Ir) \\to V_{\\text{terminal}} (= \\mathcal{E} - V_{\\text{lost}})$.",
            f"When $S$ is {action}, $R_{{\\text{{ext}}}}$ {r_ext_Change.lower()}, so $I$ {i_change.lower()}, so $Ir$ {vlost_change.lower()}.",
            f"Voltmeter reading {vterm_change.lower()} because $V_{{\\text{{terminal}}}} = \\mathcal{{E}} - Ir$.",
        ],
        ["assuming_terminal_voltage_is_constant_like_ideal_battery", "claiming_emf_changes_when_switch_toggled"],
        ["terminal potential difference", "switch reasoning chain", "lost volts"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 29: Electrical power definition and P = V * I
# ---------------------------------------------------------------------------
def arch_29_electrical_power_definition_and_vi(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_val = r.choice([12, 24, 110, 230])
    i_val = r.choice([0.5, 1.5, 2.0, 4.0, 5.0, 8.0, 10.0])
    p_val = round(v_val * i_val, 1)
    t_sec = r.choice([30, 60, 120, 300])
    w_val = round(p_val * t_sec, 1)

    prompt = (
        f"An electrical device operates at a potential difference of **${v_val}\\text{{ V}}$** and draws a current of **${fmt_sa(i_val)}\\text{{ A}}$**.\n\n"
        f"1. Define **electrical power** in words.\n"
        f"2. Calculate the electrical power ($P$) dissipated in the device.\n"
        f"3. Calculate the electrical energy ($W$) converted by the device in **${t_sec}\\text{{ s}}$**."
    )

    ans_latex = rf"P = {fmt_sa(p_val)}\text{{ W}}; \quad W = {fmt_sa(w_val)}\text{{ J}}"
    sample_answer = (
        f"1. **Definition:** Electrical power is the **rate at which electrical energy is converted** (or electrical work is done) in an electric circuit ($P = \\frac{{W}}{{\\Delta t}}$).\n\n"
        f"2. $$P = V \\cdot I = {v_val} \\times {fmt_sa(i_val)} = {fmt_sa(p_val)}\\text{{ W}}$$\n\n"
        f"3. $$W = P \\cdot \\Delta t = {fmt_sa(p_val)} \\times {t_sec} = {fmt_sa(w_val)}\\text{{ J}}$$"
    )

    return make_payload(
        "29_electrical_power_definition_and_vi",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Correct definition of electrical power (rate of electrical energy conversion)", 2),
            (f"Formula P = V * I and calculation P = {fmt_sa(p_val)} W", 2),
            (f"Calculate energy W = P * dt = {fmt_sa(w_val)} J", 2),
        ],
        [
            "Power is the rate of energy transfer, measured in watts ($\\text{W} = \\text{J}\\cdot\\text{s}^{-1}$).",
            f"Multiply $V = {v_val}\\text{{ V}}$ by $I = {fmt_sa(i_val)}\\text{{ A}}$ to get $P$, then multiply by ${t_sec}\\text{{ s}}$ for $W$.",
            f"$P = {fmt_sa(p_val)}\\text{{ W}}$ and $W = {fmt_sa(w_val)}\\text{{ J}}$.",
        ],
        ["omitting_rate_in_power_definition", "confusing_power_watts_with_energy_joules"],
        ["electrical power", "watt", "P = VI", "energy transfer"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 30: Power dissipation P = I^2 * R in series circuits
# ---------------------------------------------------------------------------
def arch_30_power_dissipation_i_squared_r(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r1 = r.choice([3, 4, 5, 6])
    r2 = r1 * r.choice([2, 3])
    i_curr = r.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    p1 = round((i_curr ** 2) * r1, 2)
    p2 = round((i_curr ** 2) * r2, 2)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**, are connected in **series** and carry a current of **${fmt_sa(i_curr)}\\text{{ A}}$**.\n\n"
        f"1. Calculate the power ($P_1$) dissipated in resistor $R_1$ and the power ($P_2$) dissipated in resistor $R_2$.\n"
        f"2. Which resistor dissipates more thermal power per second? Explain why using the formula $P = I^2 R$."
    )

    ans_latex = rf"P_1 = {fmt_sa(p1)}\text{{ W}}, \ P_2 = {fmt_sa(p2)}\text{{ W}} \ (R_2 \text{{ dissipates more power since }} P \propto R \text{{ at constant }} I)"
    sample_answer = (
        f"1. Using $P = I^2 R$:\n"
        f"   $$P_1 = ({fmt_sa(i_curr)})^2 \\times {r1} = {fmt_sa(p1)}\\text{{ W}}$$\n"
        f"   $$P_2 = ({fmt_sa(i_curr)})^2 \\times {r2} = {fmt_sa(p2)}\\text{{ W}}$$\n\n"
        f"2. **$R_2$ ({r2} $\\Omega$)** dissipates more power. Since the resistors are in series, they carry the **same current $I$**. "
        f"According to $P = I^2 R$, power is **directly proportional to resistance** ($P \\propto R$) when $I$ is constant."
    )

    return make_payload(
        "30_power_dissipation_i_squared_r",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Formula P = I^2 * R", 1),
            (f"Calculate P1 = {fmt_sa(p1)} W and P2 = {fmt_sa(p2)} W", 2),
            ("Explain that I is constant in series so P is directly proportional to R", 2),
        ],
        [
            "In a series connection, current $I$ is identical in both resistors, so use $P = I^2 R$.",
            f"Square the current $I^2 = ({fmt_sa(i_curr)})^2 = {fmt_sa(i_curr ** 2)}$ and multiply by $R_1$ and $R_2$.",
            f"$P_1 = {fmt_sa(p1)}\\text{{ W}}$, $P_2 = {fmt_sa(p2)}\\text{{ W}}$; $P \\propto R$ in series.",
        ],
        ["forgetting_to_square_current_in_i2r", "using_inverse_proportionality_in_series"],
        ["P = I^2R", "series power dissipation", "Joule heating"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 31: Power dissipation P = V^2 / R in parallel circuits
# ---------------------------------------------------------------------------
def arch_31_power_dissipation_v_squared_over_r(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_par = r.choice([12, 18, 24, 30, 36])
    r1, r2 = r.choice([(4, 12), (6, 12), (6, 18), (8, 24), (9, 18)])
    p1 = round((v_par ** 2) / r1, 2)
    p2 = round((v_par ** 2) / r2, 2)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**, are connected in **parallel** across a constant **${v_par}\\text{{ V}}$** source.\n\n"
        f"1. Calculate the electrical power ($P_1$) dissipated in $R_1$ and ($P_2$) dissipated in $R_2$.\n"
        f"2. Which resistor dissipates greater power when connected in parallel? Explain using $P = \\frac{{V^2}}{{R}}$."
    )

    ans_latex = rf"P_1 = {fmt_sa(p1)}\text{{ W}}, \ P_2 = {fmt_sa(p2)}\text{{ W}} \ (R_1 \text{{ dissipates more power since }} P \propto \frac{{1}}{{R}} \text{{ at constant }} V)"
    sample_answer = (
        f"1. Using $P = \\frac{{V^2}}{{R}}$:\n"
        f"   $$P_1 = \\frac{{{v_par}^2}}{{{r1}}} = \\frac{{{v_par ** 2}}}{{{r1}}} = {fmt_sa(p1)}\\text{{ W}}$$\n"
        f"   $$P_2 = \\frac{{{v_par}^2}}{{{r2}}} = \\frac{{{v_par ** 2}}}{{{r2}}} = {fmt_sa(p2)}\\text{{ W}}$$\n\n"
        f"2. **$R_1$ ({r1} $\\Omega$, the smaller resistor)** dissipates greater power. In parallel, the **potential difference $V$ is the same** across both branches, "
        f"so $P = \\frac{{V^2}}{{R}}$ implies $P$ is **inversely proportional to $R$** ($P \\propto \\frac{{1}}{{R}}$)."
    )

    return make_payload(
        "31_power_dissipation_v_squared_over_r",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Formula P = V^2 / R", 1),
            (f"Calculate P1 = {fmt_sa(p1)} W and P2 = {fmt_sa(p2)} W", 2),
            ("Explain that V is constant in parallel so P is inversely proportional to R (smaller R -> larger P)", 2),
        ],
        [
            "In parallel branches, the potential difference $V$ is identical across each resistor, so $P = \\frac{V^2}{R}$ is the most direct formula.",
            f"Compute $V^2 = {v_par}^2 = {v_par ** 2}$, then divide by $R_1 = {r1}\\ \\Omega$ and $R_2 = {r2}\\ \\Omega$.",
            f"$P_1 = {fmt_sa(p1)}\\text{{ W}}$, $P_2 = {fmt_sa(p2)}\\text{{ W}}$; smaller resistor $R_1$ dissipates more power.",
        ],
        ["claiming_larger_resistor_always_dissipates_more_power_in_parallel", "forgetting_to_square_voltage"],
        ["P = V^2/R", "parallel power dissipation", "inverse proportionality"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 32: Solving for resistance or current from appliance power rating
# ---------------------------------------------------------------------------
def arch_32_solving_for_resistance_or_current_from_power(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_mains = 230
    p_rating = r.choice([1150, 1840, 2070, 2300, 2530, 2760])
    i_op = round(p_rating / v_mains, 2)
    r_elem = round((v_mains ** 2) / p_rating, 2)

    prompt = (
        f"A South African household electric kettle carries a specification plate rated at **${p_rating}\\text{{ W}},\\ {v_mains}\\text{{ V}}$**.\n\n"
        f"1. State what the rating '${p_rating}\\text{{ W}},\\ {v_mains}\\text{{ V}}$' means.\n"
        f"2. Calculate the operating current ($I$) drawn by the kettle when connected to a ${v_mains}\\text{{ V}}$ supply.\n"
        f"3. Calculate the operating resistance ($R$) of the kettle's heating element."
    )

    ans_latex = rf"I = {fmt_sa(i_op)}\text{{ A}}; \quad R = {fmt_sa(r_elem)}\ \Omega"
    sample_answer = (
        f"1. When connected to a **${v_mains}\\text{{ V}}$** potential difference, the kettle converts electrical energy into thermal energy at a rate of **${p_rating}\\text{{ J per second}}$**.\n\n"
        f"2. $$P = V \\cdot I \\implies I = \\frac{{P}}{{V}} = \\frac{{{p_rating}}}{{{v_mains}}} = {fmt_sa(i_op)}\\text{{ A}}$$\n\n"
        f"3. $$P = \\frac{{V^2}}{{R}} \\implies R = \\frac{{V^2}}{{P}} = \\frac{{{v_mains}^2}}{{{p_rating}}} = {fmt_sa(r_elem)}\\ \\Omega$$"
    )

    return make_payload(
        "32_solving_for_resistance_or_current_from_power",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Explain rating: {p_rating} J/s converted when connected to {v_mains} V", 1),
            (f"Calculate operating current I = {fmt_sa(i_op)} A", 2),
            (f"Calculate resistance R = {fmt_sa(r_elem)} Ohm", 2),
        ],
        [
            "Use $I = \\frac{P}{V}$ to find the operating current and $R = \\frac{V^2}{P}$ (or $R = \\frac{V}{I}$) to find the resistance.",
            f"Divide $P = {p_rating}\\text{{ W}}$ by $V = {v_mains}\\text{{ V}}$ for $I$.",
            f"$I = {fmt_sa(i_op)}\\text{{ A}}$ and $R = {fmt_sa(r_elem)}\\ \\Omega$.",
        ],
        ["dividing_v_by_p_for_current", "forgetting_to_square_v_in_r_equals_v2_over_p"],
        ["appliance rating", "operating current", "heating element resistance"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 33: Electrical energy in joules (W = V * I * dt)
# ---------------------------------------------------------------------------
def arch_33_electrical_energy_joules_w_vit(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_val = r.choice([10, 12, 15, 20, 25])
    i_val = r.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    t_mins = r.choice([3, 5, 8, 10, 15])
    t_secs = t_mins * 60
    v_val = round(i_val * r_val, 2)
    w_joules = round((i_val ** 2) * r_val * t_secs, 1)
    w_kj = round(w_joules / 1000.0, 3)

    prompt = (
        f"A heating coil of resistance **$R = {r_val}\\ \\Omega$** carries a constant current of **$I = {fmt_sa(i_val)}\\text{{ A}}$** "
        f"for **${t_mins}\\text{{ minutes}}$**.\n\n"
        f"1. Calculate the potential difference ($V$) across the heating coil.\n"
        f"2. Calculate the total thermal energy ($W$) dissipated by the coil in **joules ($\\text{{J}}$)** and in **kilojoules ($\\text{{kJ}}$)**."
    )

    ans_latex = rf"V = {fmt_sa(v_val)}\text{{ V}}; \quad W = {fmt_sa(w_joules)}\text{{ J}} = {fmt_sa(w_kj, 3)}\text{{ kJ}}"
    sample_answer = (
        f"1. $$V = I \\cdot R = {fmt_sa(i_val)} \\times {r_val} = {fmt_sa(v_val)}\\text{{ V}}$$\n\n"
        f"2. Convert time to seconds: $\\Delta t = {t_mins} \\times 60 = {t_secs}\\text{{ s}}$.\n"
        f"   $$W = I^2 R \\Delta t = ({fmt_sa(i_val)})^2 \\times {r_val} \\times {t_secs} = {fmt_sa(w_joules)}\\text{{ J}} = {fmt_sa(w_kj, 3)}\\text{{ kJ}}$$"
    )

    return make_payload(
        "33_electrical_energy_joules_w_vit",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate V = I * R = {fmt_sa(v_val)} V", 1),
            (f"Convert {t_mins} minutes to {t_secs} seconds", 1),
            (f"Formula W = I^2 * R * dt (or V * I * dt) and W = {fmt_sa(w_joules)} J ({fmt_sa(w_kj, 3)} kJ)", 3),
        ],
        [
            "Energy in joules requires time $\\Delta t$ in **seconds** ($1\\text{ minute} = 60\\text{ s}$).",
            f"Use $W = I^2 R \\Delta t = ({fmt_sa(i_val)})^2 \\times {r_val} \\times {t_secs}$.",
            f"$V = {fmt_sa(v_val)}\\text{{ V}}$ and $W = {fmt_sa(w_joules)}\\text{{ J}}$ (${fmt_sa(w_kj, 3)}\\text{{ kJ}}$).",
        ],
        ["leaving_time_in_minutes_when_calculating_joules", "forgetting_to_square_current_in_w_i2rt"],
        ["electrical work", "joules", "kilojoules", "W = I^2Rt"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 34: Power comparison of bulbs in series vs parallel
# ---------------------------------------------------------------------------
def arch_34_power_comparison_series_vs_parallel_bulbs(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    ra, rb = r.choice([(6, 12), (4, 8), (5, 15), (8, 16), (10, 20)])
    v_supply = r.choice([12, 24, 30, 36])
    i_ser = round(v_supply / (ra + rb), 2)
    pa_ser = round((i_ser ** 2) * ra, 2)
    pb_ser = round((i_ser ** 2) * rb, 2)
    pa_par = round((v_supply ** 2) / ra, 2)
    pb_par = round((v_supply ** 2) / rb, 2)

    prompt = (
        f"Two light bulbs have constant filament resistances of **$R_A = {ra}\\ \\Omega$** and **$R_B = {rb}\\ \\Omega$**.\n\n"
        f"1. First, Bulbs A and B are connected in **series** across a **${v_supply}\\text{{ V}}$** battery. "
        f"Calculate the power dissipated in each bulb and state which bulb glows brighter in series.\n"
        f"2. Next, Bulbs A and B are connected in **parallel** across the same **${v_supply}\\text{{ V}}$** battery. "
        f"Calculate the power dissipated in each bulb and state which bulb glows brighter in parallel."
    )

    ans_latex = rf"\text{{Series: }} P_B ({fmt_sa(pb_ser)}\text{{ W}}) > P_A ({fmt_sa(pa_ser)}\text{{ W}}); \quad \text{{Parallel: }} P_A ({fmt_sa(pa_par)}\text{{ W}}) > P_B ({fmt_sa(pb_par)}\text{{ W}})"
    sample_answer = (
        f"1. **In series:** $I = \\frac{{{v_supply}}}{{{ra} + {rb}}} = {fmt_sa(i_ser)}\\text{{ A}}$.\n"
        f"   $$P_A = I^2 R_A = ({fmt_sa(i_ser)})^2({ra}) = {fmt_sa(pa_ser)}\\text{{ W}}$$\n"
        f"   $$P_B = I^2 R_B = ({fmt_sa(i_ser)})^2({rb}) = {fmt_sa(pb_ser)}\\text{{ W}}$$\n"
        f"   **Bulb B** (larger resistance) glows brighter in series because $P \\propto R$ at constant $I$.\n\n"
        f"2. **In parallel:** $V_A = V_B = {v_supply}\\text{{ V}}$.\n"
        f"   $$P_A = \\frac{{V^2}}{{R_A}} = \\frac{{{v_supply}^2}}{{{ra}}} = {fmt_sa(pa_par)}\\text{{ W}}$$\n"
        f"   $$P_B = \\frac{{V^2}}{{R_B}} = \\frac{{{v_supply}^2}}{{{rb}}} = {fmt_sa(pb_par)}\\text{{ W}}$$\n"
        f"   **Bulb A** (smaller resistance) glows brighter in parallel because $P \\propto \\frac{{1}}{{R}}$ at constant $V$."
    )

    return make_payload(
        "34_power_comparison_series_vs_parallel_bulbs",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate series powers P_A = {fmt_sa(pa_ser)} W and P_B = {fmt_sa(pb_ser)} W", 2),
            ("Identify Bulb B as brighter in series", 1),
            (f"Calculate parallel powers P_A = {fmt_sa(pa_par)} W and P_B = {fmt_sa(pb_par)} W", 2),
            ("Identify Bulb A as brighter in parallel", 1),
        ],
        [
            "Bulb brightness is determined by the electrical power dissipated ($P$) in the bulb.",
            "In series ($I$ same), $P = I^2 R$ so larger $R$ is brighter. In parallel ($V$ same), $P = V^2/R$ so smaller $R$ is brighter.",
            f"Series: Bulb B brighter (${fmt_sa(pb_ser)}\\text{{ W}} > {fmt_sa(pa_ser)}\\text{{ W}}$). Parallel: Bulb A brighter (${fmt_sa(pa_par)}\\text{{ W}} > {fmt_sa(pb_par)}\\text{{ W}}$).",
        ],
        ["assuming_same_bulb_is_brighter_in_both_series_and_parallel", "equating_brightness_to_resistance_alone"],
        ["bulb brightness", "series vs parallel power", "P = I^2R", "P = V^2/R"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 35: Bulb brightness changes when a switch is toggled
# ---------------------------------------------------------------------------
def arch_35_bulb_brightness_changes_when_switch_toggled(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    r_bulb = r.choice([6, 8, 12])
    v_bat = r.choice([12, 18, 24])
    p_open = round((v_bat / (2 * r_bulb)) ** 2 * r_bulb, 2)
    rp_closed = r_bulb / 2.0
    r_tot_closed = r_bulb + rp_closed
    i_main_closed = round(v_bat / r_tot_closed, 2)
    p_main_closed = round((i_main_closed ** 2) * r_bulb, 2)

    prompt = (
        f"Three identical light bulbs (**$L_1, L_2, L_3$**), each of constant resistance **$R = {r_bulb}\\ \\Omega$**, are connected to a **${v_bat}\\text{{ V}}$** battery of negligible internal resistance.\n"
        f"Bulb $L_1$ is in the main branch in series with the battery, while $L_2$ and $L_3$ are in two parallel branches (with switch **$S$** in the $L_3$ branch).\n\n"
        f"1. Calculate the power dissipated in $L_1$ when switch $S$ is **open**.\n"
        f"2. Switch $S$ is now **closed**. Calculate the new power dissipated in $L_1$.\n"
        f"3. State how the brightness of **$L_1$** and the brightness of **$L_2$** change when switch $S$ is closed. Explain briefly."
    )

    ans_latex = rf"P_{{L_1,\text{{open}}}} = {fmt_sa(p_open)}\text{{ W}}, \ P_{{L_1,\text{{closed}}}} = {fmt_sa(p_main_closed)}\text{{ W}}; \ L_1 \text{{ brighter, }} L_2 \text{{ dimmer}}"
    sample_answer = (
        f"1. With $S$ open, $L_1$ and $L_2$ are in series ($R_{{\\text{{tot}}}} = 2R = {2 * r_bulb}\\ \\Omega$, $I = \\frac{{{v_bat}}}{{{2 * r_bulb}}} = {fmt_sa(v_bat / (2 * r_bulb))}\\text{{ A}}$):\n"
        f"   $$P_{{L_1,\\text{{open}}}} = I^2 R = {fmt_sa(p_open)}\\text{{ W}}$$\n\n"
        f"2. With $S$ closed, $L_2 \\parallel L_3$ gives $R_p = \\frac{{{r_bulb}}}{{2}} = {fmt_sa(rp_closed)}\\ \\Omega$, so $R_{{\\text{{tot}}}} = {r_bulb} + {fmt_sa(rp_closed)} = {fmt_sa(r_tot_closed)}\\ \\Omega$:\n"
        f"   $$I_{{\\text{{main}}}} = \\frac{{{v_bat}}}{{{fmt_sa(r_tot_closed)}}} = {fmt_sa(i_main_closed)}\\text{{ A}} \\implies P_{{L_1,\\text{{closed}}}} = ({fmt_sa(i_main_closed)})^2({r_bulb}) = {fmt_sa(p_main_closed)}\\text{{ W}}$$\n\n"
        f"3. - **$L_1$ becomes brighter** because total resistance decreases, main current $I_{{\\text{{main}}}}$ increases, so $P_{{L_1}} = I_{{\\text{{main}}}}^2 R$ increases.\n"
        f"   - **$L_2$ becomes dimmer** because $V_{{L_1}}$ increases, leaving a smaller parallel potential difference $V_p = V_{{\\text{{bat}}}} - V_{{L_1}}$ across $L_2$ ($P_{{L_2}} = V_p^2 / R$ decreases)."
    )

    return make_payload(
        "35_bulb_brightness_changes_when_switch_toggled",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate P_L1(open) = {fmt_sa(p_open)} W", 2),
            (f"Calculate P_L1(closed) = {fmt_sa(p_main_closed)} W", 2),
            ("State L1 gets brighter and L2 gets dimmer with valid power/voltage reasoning", 2),
        ],
        [
            "Compare the main-branch current $I_{\\text{main}}$ before and after closing switch $S$.",
            "When $L_3$ is added in parallel, $R_{\\text{total}}$ drops from $2R$ to $1{,}5R$, so $I_{\\text{main}}$ through $L_1$ increases.",
            f"$P_{{L_1}}$ rises from ${fmt_sa(p_open)}\\text{{ W}}$ to ${fmt_sa(p_main_closed)}\\text{{ W}}$ ($L_1$ brighter, $L_2$ dimmer).",
        ],
        ["assuming_parallel_bulb_l2_brightness_never_changes_with_series_bulb_present", "wrong_equivalent_resistance_for_three_bulbs"],
        ["bulb brightness", "switch closed", "power redistribution"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 36: Appliance power ratings and fuse selection
# ---------------------------------------------------------------------------
def arch_36_appliance_power_ratings_and_fuse_selection(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    app = r.choice([
        {"name": "microwave oven", "p": 1380, "i": 6.0, "fuse": "10 A"},
        {"name": "hair dryer", "p": 1840, "i": 8.0, "fuse": "10 A"},
        {"name": "toaster", "p": 920, "i": 4.0, "fuse": "5 A"},
        {"name": "iron", "p": 2530, "i": 11.0, "fuse": "13 A or 15 A"},
        {"name": "oil heater", "p": 2070, "i": 9.0, "fuse": "10 A"},
        {"name": "washing machine", "p": 2760, "i": 12.0, "fuse": "15 A"},
    ])
    v_mains = 230

    prompt = (
        f"A household **{app['name']}** is rated at **${app['p']}\\text{{ W}}$** for use on the standard South African **${v_mains}\\text{{ V}}$** mains supply.\n"
        f"Available fuses have ratings of **$3\\text{{ A}}$**, **$5\\text{{ A}}$**, **$10\\text{{ A}}$**, and **$15\\text{{ A}}$**.\n\n"
        f"1. State the safety function of a **fuse** in an electrical appliance.\n"
        f"2. Calculate the normal operating current drawn by the {app['name']}.\n"
        f"3. Select the most suitable fuse rating from the list and explain why a much smaller or much larger fuse is unsuitable."
    )

    ans_latex = rf"I = {fmt_sa(app['i'])}\text{{ A}}; \quad \text{{Recommended fuse: {app['fuse']}}}"
    sample_answer = (
        f"1. A **fuse** contains a thin wire that melts and breaks the circuit if the current exceeds a safe value, protecting the appliance and wiring from overheating and electrical fires.\n\n"
        f"2. $$I = \\frac{{P}}{{V}} = \\frac{{{app['p']}}}{{{v_mains}}} = {fmt_sa(app['i'])}\\text{{ A}}$$\n\n"
        f"3. **Recommended fuse: {app['fuse']}** (just above the normal operating current of ${fmt_sa(app['i'])}\\text{{ A}}$).\n"
        f"   - A fuse rated below ${fmt_sa(app['i'])}\\text{{ A}}$ would blow immediately during normal use.\n"
        f"   - A fuse rated far too high would allow dangerous fault currents to flow without melting."
    )

    return make_payload(
        "36_appliance_power_ratings_and_fuse_selection",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("State safety function of fuse (melts to break circuit on overcurrent)", 1),
            (f"Calculate normal operating current I = {fmt_sa(app['i'])} A", 2),
            (f"Select {app['fuse']} fuse and explain why (slightly above operating current)", 2),
        ],
        [
            "Calculate the normal operating current using $I = \\frac{P}{V}$.",
            "Choose the standard fuse rating that is **just higher** than the normal operating current.",
            f"$I = {fmt_sa(app['i'])}\\text{{ A}}$; choose the **{app['fuse']}** fuse.",
        ],
        ["choosing_fuse_smaller_than_operating_current", "choosing_exact_or_excessively_large_fuse"],
        ["fuse selection", "overcurrent protection", "mains supply"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 37: Multi-appliance parallel household circuit & breaker limit
# ---------------------------------------------------------------------------
def arch_37_multi_appliance_parallel_household_circuit(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_mains = 230
    p1 = r.choice([1840, 2070, 2300])  # kettle
    p2 = r.choice([1150, 1380, 1610])  # microwave
    p3 = r.choice([920, 1150, 1840])   # toaster/iron
    p_tot = p1 + p2 + p3
    i_tot = round(p_tot / v_mains, 2)
    breaker = 20
    trips = "YES" if i_tot > breaker else "NO"

    prompt = (
        f"In a kitchen wired in parallel to a **${v_mains}\\text{{ V}}$** distribution board protected by a **${breaker}\\text{{ A}}$** circuit breaker, "
        f"three appliances are switched on simultaneously:\n"
        f"- Electric kettle: **${p1}\\text{{ W}}$**\n"
        f"- Microwave oven: **${p2}\\text{{ W}}$**\n"
        f"- Electric toaster/iron: **${p3}\\text{{ W}}$**\n\n"
        f"1. Give two reasons why household appliances are connected in **parallel** rather than in series.\n"
        f"2. Calculate the total electrical power ($P_{{\\text{{total}}}}$) drawn when all three appliances operate simultaneously.\n"
        f"3. Calculate the total main current ($I_{{\\text{{total}}}}$) and determine whether the **${breaker}\\text{{ A}}$** circuit breaker will trip."
    )

    ans_latex = rf"P_{{\text{{tot}}}} = {p_tot}\text{{ W}}, \ I_{{\text{{tot}}}} = {fmt_sa(i_tot)}\text{{ A}} \ (\text{{Trips: {trips}}})"
    sample_answer = (
        f"1. **Reasons for parallel household wiring:**\n"
        f"   - Every appliance receives the full **${v_mains}\\text{{ V}}$** mains potential difference.\n"
        f"   - Appliances can be switched on and off **independently** without breaking the circuit for other devices.\n\n"
        f"2. $$P_{{\\text{{total}}}} = {p1} + {p2} + {p3} = {p_tot}\\text{{ W}}$$\n\n"
        f"3. $$I_{{\\text{{total}}}} = \\frac{{P_{{\\text{{total}}}}}}{{V}} = \\frac{{{p_tot}}}{{{v_mains}}} = {fmt_sa(i_tot)}\\text{{ A}}$$\n"
        f"   Since ${fmt_sa(i_tot)}\\text{{ A}} {'>' if i_tot > breaker else '<'} {breaker}\\text{{ A}}$, the circuit breaker **{'WILL trip' if trips == 'YES' else 'will NOT trip'}**."
    )

    return make_payload(
        "37_multi_appliance_parallel_household_circuit",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Two valid reasons for parallel household wiring (full 230 V each; independent operation)", 2),
            (f"Calculate total power P_total = {p_tot} W", 1),
            (f"Calculate total current I_total = {fmt_sa(i_tot)} A and conclude breaker trips: {trips}", 2),
        ],
        [
            "Total power dissipated in a parallel circuit is the sum of the individual powers: $P_{\\text{total}} = P_1 + P_2 + P_3$.",
            f"Divide $P_{{\\text{{total}}}} = {p_tot}\\text{{ W}}$ by $230\\text{{ V}}$ and compare with the ${breaker}\\text{{ A}}$ limit.",
            f"$I_{{\\text{{total}}}} = {fmt_sa(i_tot)}\\text{{ A}}$; breaker trips: {trips}.",
        ],
        ["calculating_series_current_for_household_appliances", "failing_to_sum_parallel_appliance_currents"],
        ["household circuit", "circuit breaker", "parallel wiring", "overload"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 38: Watt to kilowatt and kWh definition & Joule conversion
# ---------------------------------------------------------------------------
def arch_38_watt_to_kilowatt_and_kwh_definition(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    p_watts = r.choice([450, 750, 1200, 1500, 2200, 2800, 3500])
    p_kw = p_watts / 1000.0
    n_kwh = r.choice([2, 3, 4, 5, 8, 10])
    j_total = round(n_kwh * 3.6, 2)

    prompt = (
        f"Municipal electricity meters measure household energy consumption in **kilowatt-hours ($\\text{{kWh}}$)**.\n\n"
        f"1. Define the **kilowatt-hour ($\\text{{kWh}}$)** and state which physical quantity it measures (power or energy).\n"
        f"2. Convert a power rating of **${p_watts}\\text{{ W}}$** into kilowatts ($\\text{{kW}}$).\n"
        f"3. Show by calculation that **$1\\text{{ kWh}} = 3{{,}}6 \\times 10^6\\text{{ J}}$**, and hence convert **${n_kwh}\\text{{ kWh}}$** into joules."
    )

    ans_latex = rf"P = {fmt_sa(p_kw, 3)}\text{{ kW}}; \quad {n_kwh}\text{{ kWh}} = {fmt_sa(j_total)} \times 10^6\text{{ J}}"
    sample_answer = (
        f"1. One **kilowatt-hour ($\\text{{kWh}}$)** is the **electrical energy** consumed by a $1\\text{{ kW}}$ ($1000\\text{{ W}}$) appliance operating continuously for $1\\text{{ hour}}$. It is a unit of **energy** (not power).\n\n"
        f"2. $$P = \\frac{{{p_watts}}}{{1000}} = {fmt_sa(p_kw, 3)}\\text{{ kW}}$$\n\n"
        f"3. $$1\\text{{ kWh}} = (1000\\text{{ J}}\\cdot\\text{{s}}^{{-1}}) \\times (3600\\text{{ s}}) = 3{{,}}6 \\times 10^6\\text{{ J}}$$\n"
        f"   Therefore, ${n_kwh}\\text{{ kWh}} = {n_kwh} \\times 3{{,}}6 \\times 10^6 = {fmt_sa(j_total)} \\times 10^6\\text{{ J}}$."
    )

    return make_payload(
        "38_watt_to_kilowatt_and_kwh_definition",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Define 1 kWh and state it measures electrical energy", 2),
            (f"Convert {p_watts} W to {fmt_sa(p_kw, 3)} kW", 1),
            (f"Show 1 kWh = 3,6 x 10^6 J and convert {n_kwh} kWh = {fmt_sa(j_total)} x 10^6 J", 2),
        ],
        [
            "Since $E = P \\times t$, multiplying kilowatts (power) by hours (time) gives energy.",
            "Divide watts by $1000$ to get kilowatts; multiply $1000\\text{ W}$ by $3600\\text{ s}$ to convert $1\\text{ kWh}$ to joules.",
            f"${p_watts}\\text{{ W}} = {fmt_sa(p_kw, 3)}\\text{{ kW}}$ and ${n_kwh}\\text{{ kWh}} = {fmt_sa(j_total)} \\times 10^6\\text{{ J}}$.",
        ],
        ["confusing_kwh_as_a_unit_of_power", "multiplying_by_1000_instead_of_dividing_for_kw"],
        ["kilowatt-hour", "kWh", "joules conversion", "electrical energy"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 39: Kilowatt-hour energy consumption calculation
# ---------------------------------------------------------------------------
def arch_39_kilowatt_hour_energy_consumption_calculation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    app = r.choice([
        {"name": "convection oven", "w": 2200, "mins": 45},
        {"name": "clothes dryer", "w": 2500, "mins": 30},
        {"name": "pool pump", "w": 1100, "mins": 150},
        {"name": "air fryer", "w": 1800, "mins": 20},
        {"name": "dishwasher", "w": 1500, "mins": 90},
    ])
    days = r.choice([14, 20, 30])
    p_kw = app["w"] / 1000.0
    h_day = round(app["mins"] / 60.0, 2)
    e_day = round(p_kw * h_day, 3)
    e_month = round(e_day * days, 2)

    prompt = (
        f"A household **{app['name']}** rated at **${app['w']}\\text{{ W}}$** is used for **${app['mins']}\\text{{ minutes}}$** every day.\n\n"
        f"1. Convert the power rating to kilowatts ($\\text{{kW}}$) and the daily operating time to hours ($\\text{{h}}$).\n"
        f"2. Calculate the electrical energy (in $\\text{{kWh}}$) consumed by the {app['name']} in **one day**.\n"
        f"3. Calculate the total electrical energy (in $\\text{{kWh}}$) consumed over **${days}\\text{{ days}}$**."
    )

    ans_latex = rf"E_{{\text{{day}}}} = {fmt_sa(e_day, 3)}\text{{ kWh}}; \quad E_{{{days}\text{{ days}}}} = {fmt_sa(e_month)}\text{{ kWh}}"
    sample_answer = (
        f"1. $$P = \\frac{{{app['w']}}}{{1000}} = {fmt_sa(p_kw, 2)}\\text{{ kW}}, \\quad t = \\frac{{{app['mins']}}}{{60}} = {fmt_sa(h_day)}\\text{{ hours/day}}$$\n\n"
        f"2. $$E_{{\\text{{day}}}} = P(\\text{{kW}}) \\times t(\\text{{h}}) = {fmt_sa(p_kw, 2)} \\times {fmt_sa(h_day)} = {fmt_sa(e_day, 3)}\\text{{ kWh}}$$\n\n"
        f"3. $$E_{{{days}\\text{{ days}}}} = {fmt_sa(e_day, 3)} \\times {days} = {fmt_sa(e_month)}\\text{{ kWh}}$$"
    )

    return make_payload(
        "39_kilowatt_hour_energy_consumption_calculation",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Convert {app['w']} W to {fmt_sa(p_kw, 2)} kW and {app['mins']} min to {fmt_sa(h_day)} h", 2),
            (f"Calculate daily energy = {fmt_sa(e_day, 3)} kWh", 1),
            (f"Calculate {days}-day energy = {fmt_sa(e_month)} kWh", 1),
        ],
        [
            "In $E(\\text{kWh}) = P(\\text{kW}) \\times t(\\text{h})$, convert watts to kilowatts ($\\div 1000$) and minutes to hours ($\\div 60$).",
            f"Here $P = {fmt_sa(p_kw, 2)}\\text{{ kW}}$ and $t = {fmt_sa(h_day)}\\text{{ h}}$ per day.",
            f"$E_{{\\text{{day}}}} = {fmt_sa(e_day, 3)}\\text{{ kWh}}$ and $E_{{{days}}} = {fmt_sa(e_month)}\\text{{ kWh}}$.",
        ],
        ["forgetting_minutes_to_hours_conversion_in_kwh", "forgetting_watts_to_kw_conversion"],
        ["kWh calculation", "daily energy consumption", "time conversion"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 40: Single appliance monthly electricity cost
# ---------------------------------------------------------------------------
def arch_40_single_appliance_monthly_electricity_cost(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    app = r.choice([
        {"name": "electric geyser", "w": 3000, "h": 3.5},
        {"name": "air conditioner", "w": 1800, "h": 5.0},
        {"name": "space heater", "w": 2000, "h": 4.0},
        {"name": "electric stove plate", "w": 1500, "h": 2.0},
        {"name": "chest freezer", "w": 400, "h": 12.0},
    ])
    days = r.choice([30, 31])
    tariff = r.choice([2.45, 2.75, 2.90, 3.15, 3.40])
    p_kw = app["w"] / 1000.0
    tot_h = app["h"] * days
    e_kwh = round(p_kw * tot_h, 2)
    cost = round(e_kwh * tariff, 2)

    prompt = (
        f"A family operates an **{app['name']}** rated at **${app['w']}\\text{{ W}}$** for an average of "
        f"**${fmt_sa(app['h'])}\\text{{ hours per day}}$** over a **${days}\\text{{-day}}$** month.\n"
        f"The municipal electricity tariff is **$\\text{{R}}{fmt_sa(tariff)}\\text{{ per kWh}}$**.\n\n"
        f"1. Calculate the total electrical energy (in $\\text{{kWh}}$) consumed by the {app['name']} during the ${days}$-day month.\n"
        f"2. Calculate the monthly cost (in Rands) of operating this appliance."
    )

    ans_latex = rf"E = {fmt_sa(e_kwh)}\text{{ kWh}}; \quad \text{{Cost}} = \text{{R}}{fmt_sa(cost)}"
    sample_answer = (
        f"1. $$P = \\frac{{{app['w']}}}{{1000}} = {fmt_sa(p_kw)}\\text{{ kW}}, \\quad t_{{\\text{{total}}}} = {fmt_sa(app['h'])} \\times {days} = {fmt_sa(tot_h)}\\text{{ h}}$$\n"
        f"   $$E = P \\times t_{{\\text{{total}}}} = {fmt_sa(p_kw)} \\times {fmt_sa(tot_h)} = {fmt_sa(e_kwh)}\\text{{ kWh}}$$\n\n"
        f"2. $$\\text{{Cost}} = E(\\text{{kWh}}) \\times \\text{{tariff}} = {fmt_sa(e_kwh)} \\times \\text{{R}}{fmt_sa(tariff)} = \\text{{R}}{fmt_sa(cost)}$$"
    )

    return make_payload(
        "40_single_appliance_monthly_electricity_cost",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Convert power to {fmt_sa(p_kw)} kW and total time to {fmt_sa(tot_h)} h", 1),
            (f"Calculate monthly energy E = {fmt_sa(e_kwh)} kWh", 1),
            (f"Calculate monthly cost = R{fmt_sa(cost)}", 2),
        ],
        [
            "Use $\\text{Cost} = P(\\text{kW}) \\times t_{\\text{total}}(\\text{hours}) \\times \\text{tariff (R/kWh)}$.",
            f"Multiply ${fmt_sa(p_kw)}\\text{{ kW}} \\times {fmt_sa(tot_h)}\\text{{ h}} = {fmt_sa(e_kwh)}\\text{{ kWh}}$, then multiply by $\\text{{R}}{fmt_sa(tariff)}$.",
            f"$E = {fmt_sa(e_kwh)}\\text{{ kWh}}$ and $\\text{{Cost}} = \\text{{R}}{fmt_sa(cost)}$.",
        ],
        ["forgot_converting_watts_to_kw", "forgot_multiplying_by_days_in_month"],
        ["electricity cost", "monthly tariff", "kWh"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 41: Multi-appliance household audit bill
# ---------------------------------------------------------------------------
def arch_41_multi_appliance_household_audit_bill(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    geyser_h = r.choice([2.5, 3.0, 4.0])
    lights_n = r.choice([6, 8, 10])
    tv_h = r.choice([4.0, 5.0, 6.0])
    tariff = r.choice([2.50, 2.80, 3.00, 3.20])
    days = 30

    # Daily kWh:
    # Geyser: 3.0 kW * geyser_h
    e_geyser_d = round(3.0 * geyser_h, 3)
    # LED lamps: lights_n * 0.010 kW * 5 h
    e_lights_d = round(lights_n * 0.010 * 5.0, 3)
    # TV: 0.15 kW * tv_h
    e_tv_d = round(0.15 * tv_h, 3)
    e_day_tot = round(e_geyser_d + e_lights_d + e_tv_d, 3)
    e_month_tot = round(e_day_tot * days, 2)
    bill = round(e_month_tot * tariff, 2)

    prompt = (
        f"A learner conducts a daily electrical energy audit for three household systems over a **${days}\\text{{-day}}$** month:\n"
        f"- **1 Electric geyser** ($3000\\text{{ W}}$) operating for **${fmt_sa(geyser_h)}\\text{{ hours/day}}$**\n"
        f"- **${lights_n}$ LED lamps** ($10\\text{{ W}}$ each) operating for **$5\\text{{ hours/day}}$**\n"
        f"- **1 Television** ($150\\text{{ W}}$) operating for **${fmt_sa(tv_h)}\\text{{ hours/day}}$**\n\n"
        f"The electricity tariff is **$\\text{{R}}{fmt_sa(tariff)}\\text{{ per kWh}}$**.\n"
        f"1. Calculate the daily energy consumption (in $\\text{{kWh}}$) of each of the three systems.\n"
        f"2. Calculate the total monthly energy consumption (in $\\text{{kWh}}$) over ${days}$ days.\n"
        f"3. Calculate the total monthly electricity bill for these items."
    )

    ans_latex = rf"E_{{\text{{month}}}} = {fmt_sa(e_month_tot)}\text{{ kWh}}; \quad \text{{Total Bill}} = \text{{R}}{fmt_sa(bill)}"
    sample_answer = (
        f"1. **Daily consumption:**\n"
        f"   - Geyser: $3{{,}}0\\text{{ kW}} \\times {fmt_sa(geyser_h)}\\text{{ h}} = {fmt_sa(e_geyser_d, 3)}\\text{{ kWh}}$\n"
        f"   - ${lights_n}$ LED lamps: ${lights_n} \\times 0{{,}}010\\text{{ kW}} \\times 5\\text{{ h}} = {fmt_sa(e_lights_d, 3)}\\text{{ kWh}}$\n"
        f"   - Television: $0{{,}}150\\text{{ kW}} \\times {fmt_sa(tv_h)}\\text{{ h}} = {fmt_sa(e_tv_d, 3)}\\text{{ kWh}}$\n\n"
        f"2. $$E_{{\\text{{day,total}}}} = {fmt_sa(e_geyser_d, 3)} + {fmt_sa(e_lights_d, 3)} + {fmt_sa(e_tv_d, 3)} = {fmt_sa(e_day_tot, 3)}\\text{{ kWh/day}}$$\n"
        f"   $$E_{{\\text{{month}}}} = {fmt_sa(e_day_tot, 3)} \\times {days} = {fmt_sa(e_month_tot)}\\text{{ kWh}}$$\n\n"
        f"3. $$\\text{{Bill}} = {fmt_sa(e_month_tot)} \\times \\text{{R}}{fmt_sa(tariff)} = \\text{{R}}{fmt_sa(bill)}$$"
    )

    return make_payload(
        "41_multi_appliance_household_audit_bill",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate daily kWh for geyser ({fmt_sa(e_geyser_d, 3)}), LEDs ({fmt_sa(e_lights_d, 3)}), and TV ({fmt_sa(e_tv_d, 3)})", 3),
            (f"Calculate total monthly energy = {fmt_sa(e_month_tot)} kWh", 1),
            (f"Calculate total monthly bill = R{fmt_sa(bill)}", 1),
        ],
        [
            "Remember to multiply the single LED lamp power ($10\\text{ W} = 0{,}010\\text{ kW}$) by the number of lamps (${lights_n}$).",
            f"Sum the daily $\\text{{kWh}}$ values (${fmt_sa(e_day_tot, 3)}\\text{{ kWh}}$), multiply by ${days}\\text{{ days}}$, then multiply by $\\text{{R}}{fmt_sa(tariff)}$.",
            f"$E_{{\\text{{month}}}} = {fmt_sa(e_month_tot)}\\text{{ kWh}}$, $\\text{{Bill}} = \\text{{R}}{fmt_sa(bill)}$.",
        ],
        ["forgetting_to_multiply_by_number_of_bulbs", "watts_to_kw_decimal_shift_error"],
        ["household energy audit", "multi-appliance bill", "kWh"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 42: Stepped inclining block tariff calculation
# ---------------------------------------------------------------------------
def arch_42_stepped_inclining_block_tariff_calculation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    total_kwh = r.choice([450, 500, 550, 600, 650])
    block1_limit = 350
    t1 = r.choice([2.10, 2.20, 2.40])
    t2 = r.choice([3.00, 3.20, 3.50])
    b1_kwh = block1_limit
    b2_kwh = total_kwh - block1_limit
    cost1 = round(b1_kwh * t1, 2)
    cost2 = round(b2_kwh * t2, 2)
    sub_tot = round(cost1 + cost2, 2)
    vat_tot = round(sub_tot * 1.15, 2)

    prompt = (
        f"A South African municipality uses an **inclining block tariff** (excluding $15\\%$ VAT) for domestic electricity:\n"
        f"- **Block 1 ($0\\text{{--}}{block1_limit}\\text{{ kWh}}$):** $\\text{{R}}{fmt_sa(t1)}\\text{{ per kWh}}$\n"
        f"- **Block 2 ($> {block1_limit}\\text{{ kWh}}$):** $\\text{{R}}{fmt_sa(t2)}\\text{{ per kWh}}$\n\n"
        f"A household consumes **${total_kwh}\\text{{ kWh}}$** during a month.\n"
        f"1. Calculate the cost of the electricity consumed in Block 1 and in Block 2 (excluding VAT).\n"
        f"2. Calculate the total monthly electricity cost **including $15\\%$ VAT**.\n"
        f"3. State one socio-economic or environmental reason why municipalities use inclining block tariffs."
    )

    ans_latex = rf"\text{{Excl. VAT}} = \text{{R}}{fmt_sa(sub_tot)}; \quad \text{{Incl. 15\% VAT}} = \text{{R}}{fmt_sa(vat_tot)}"
    sample_answer = (
        f"1. - **Block 1 ($350\\text{{ kWh}}$):** $350 \\times \\text{{R}}{fmt_sa(t1)} = \\text{{R}}{fmt_sa(cost1)}$\n"
        f"   - **Block 2 (${total_kwh} - 350 = {b2_kwh}\\text{{ kWh}}$):** ${b2_kwh} \\times \\text{{R}}{fmt_sa(t2)} = \\text{{R}}{fmt_sa(cost2)}$\n"
        f"   - **Total (excl. VAT):** $\\text{{R}}{fmt_sa(cost1)} + \\text{{R}}{fmt_sa(cost2)} = \\text{{R}}{fmt_sa(sub_tot)}$\n\n"
        f"2. $$\\text{{Total (incl. 15\\% VAT)}} = \\text{{R}}{fmt_sa(sub_tot)} \\times 1{{,}}15 = \\text{{R}}{fmt_sa(vat_tot)}$$\n\n"
        f"3. It keeps basic electricity affordable for low-income households while discouraging excessive electricity consumption and reducing strain on the national grid."
    )

    return make_payload(
        "42_stepped_inclining_block_tariff_calculation",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate Block 1 cost = R{fmt_sa(cost1)} and Block 2 ({b2_kwh} kWh) cost = R{fmt_sa(cost2)}", 2),
            (f"Calculate subtotal = R{fmt_sa(sub_tot)} and VAT-inclusive total = R{fmt_sa(vat_tot)}", 2),
            ("Valid reason for stepped tariff (energy conservation / affordability for low-usage households)", 1),
        ],
        [
            f"Only the units **above** ${block1_limit}\\text{{ kWh}}$ (${b2_kwh}\\text{{ kWh}}$) are charged at the Block 2 rate!",
            f"Add $\\text{{R}}{fmt_sa(cost1)} + \\text{{R}}{fmt_sa(cost2)} = \\text{{R}}{fmt_sa(sub_tot)}$, then multiply by $1{{,}}15$ for $15\\%$ VAT.",
            f"Excl. VAT: $\\text{{R}}{fmt_sa(sub_tot)}$; Incl. VAT: $\\text{{R}}{fmt_sa(vat_tot)}$.",
        ],
        ["applying_block2_rate_to_all_units_instead_of_excess_units", "forgetting_15_percent_vat"],
        ["inclining block tariff", "stepped tariff", "VAT", "municipal bill"],
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Subskill 43: Energy saving LED vs incandescent bulb comparison
# ---------------------------------------------------------------------------
def arch_43_energy_saving_led_vs_incandescent_comparison(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    n_bulbs = r.choice([5, 8, 10, 12])
    p_inc = r.choice([60, 75, 100])
    p_led = r.choice([9, 10, 12])
    h_day = r.choice([5, 6, 8])
    days = 30
    tariff = r.choice([2.50, 2.80, 3.00])

    kw_saved = ((p_inc - p_led) * n_bulbs) / 1000.0
    kwh_saved = round(kw_saved * h_day * days, 2)
    rand_saved = round(kwh_saved * tariff, 2)

    prompt = (
        f"A household replaces **${n_bulbs}$ incandescent light bulbs** rated at **${p_inc}\\text{{ W}}$** each with "
        f"**${n_bulbs}$ LED bulbs** rated at **${p_led}\\text{{ W}}$** each (providing equivalent light output).\n"
        f"All ${n_bulbs}$ bulbs are switched on for **${h_day}\\text{{ hours per day}}$** over a **${days}\\text{{-day}}$** month at a tariff of **$\\text{{R}}{fmt_sa(tariff)}\\text{{ per kWh}}$**.\n\n"
        f"1. Calculate the total electrical power (in $\\text{{kW}}$) saved when all ${n_bulbs}$ bulbs are operating.\n"
        f"2. Calculate the monthly electrical energy saved (in $\\text{{kWh}}$).\n"
        f"3. Calculate the monthly financial savings (in Rands)."
    )

    ans_latex = rf"\Delta P = {fmt_sa(kw_saved, 3)}\text{{ kW}}, \ \Delta E = {fmt_sa(kwh_saved)}\text{{ kWh}}, \ \text{{Savings}} = \text{{R}}{fmt_sa(rand_saved)}"
    sample_answer = (
        f"1. Power saved per bulb $= {p_inc} - {p_led} = {p_inc - p_led}\\text{{ W}}$.\n"
        f"   For ${n_bulbs}$ bulbs: $\\Delta P = \\frac{{{n_bulbs} \\times {p_inc - p_led}}}{{1000}} = {fmt_sa(kw_saved, 3)}\\text{{ kW}}$.\n\n"
        f"2. $$\\Delta E = \\Delta P \\times t_{{\\text{{month}}}} = {fmt_sa(kw_saved, 3)} \\times ({h_day} \\times {days}) = {fmt_sa(kwh_saved)}\\text{{ kWh}}$$\n\n"
        f"3. $$\\text{{Monthly savings}} = {fmt_sa(kwh_saved)} \\times \\text{{R}}{fmt_sa(tariff)} = \\text{{R}}{fmt_sa(rand_saved)}$$"
    )

    return make_payload(
        "43_energy_saving_led_vs_incandescent_comparison",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate total power saved = {fmt_sa(kw_saved, 3)} kW", 2),
            (f"Calculate monthly energy saved = {fmt_sa(kwh_saved)} kWh", 1),
            (f"Calculate monthly money saved = R{fmt_sa(rand_saved)}", 2),
        ],
        [
            f"Find the power difference for all ${n_bulbs}$ bulbs: ${n_bulbs} \\times ({p_inc} - {p_led})\\text{{ W}}$, then convert to $\\text{{kW}}$.",
            f"Multiply $\\Delta P = {fmt_sa(kw_saved, 3)}\\text{{ kW}}$ by total monthly hours (${h_day * days}\\text{{ h}}$) and tariff $\\text{{R}}{fmt_sa(tariff)}$.",
            f"$\\Delta E = {fmt_sa(kwh_saved)}\\text{{ kWh}}$ and $\\text{{Savings}} = \\text{{R}}{fmt_sa(rand_saved)}$.",
        ],
        ["calculating_savings_for_only_one_bulb", "forgetting_watts_to_kw_conversion"],
        ["LED energy saving", "incandescent comparison", "cost reduction"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 44: Geyser timer and insulation cost savings
# ---------------------------------------------------------------------------
def arch_44_geyser_timer_and_insulation_cost_savings(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    p_kw = r.choice([2.5, 3.0, 4.0])
    h_before = r.choice([5.0, 6.0])
    h_after = r.choice([2.5, 3.0])
    days = 30
    tariff = r.choice([2.60, 2.85, 3.10, 3.25])

    dh = h_before - h_after
    kwh_saved = round(p_kw * dh * days, 2)
    rand_saved = round(kwh_saved * tariff, 2)

    prompt = (
        f"An electric geyser with a **${fmt_sa(p_kw)}\\text{{ kW}}$** heating element previously operated for **${fmt_sa(h_before)}\\text{{ hours per day}}$**.\n"
        f"After installing a thermal geyser blanket and an automatic timer switch, the heating element operates for only **${fmt_sa(h_after)}\\text{{ hours per day}}$**.\n"
        f"Assume a **${days}\\text{{-day}}$** month and a municipal tariff of **$\\text{{R}}{fmt_sa(tariff)}\\text{{ per kWh}}$**.\n\n"
        f"1. Calculate the daily reduction in operating time and daily $\\text{{kWh}}$ saved.\n"
        f"2. Calculate the total $\\text{{kWh}}$ saved over the ${days}$-day month.\n"
        f"3. Calculate the monthly cost saving in Rands."
    )

    ans_latex = rf"\Delta E_{{\text{{month}}}} = {fmt_sa(kwh_saved)}\text{{ kWh}}; \quad \text{{Monthly Saving}} = \text{{R}}{fmt_sa(rand_saved)}"
    sample_answer = (
        f"1. Time saved per day: $\\Delta t = {fmt_sa(h_before)} - {fmt_sa(h_after)} = {fmt_sa(dh)}\\text{{ h/day}}$.\n"
        f"   Daily energy saved: $\\Delta E_{{\\text{{day}}}} = {fmt_sa(p_kw)} \\times {fmt_sa(dh)} = {fmt_sa(p_kw * dh)}\\text{{ kWh/day}}$.\n\n"
        f"2. $$\\Delta E_{{\\text{{month}}}} = {fmt_sa(p_kw * dh)} \\times {days} = {fmt_sa(kwh_saved)}\\text{{ kWh}}$$\n\n"
        f"3. $$\\text{{Saving}} = {fmt_sa(kwh_saved)} \\times \\text{{R}}{fmt_sa(tariff)} = \\text{{R}}{fmt_sa(rand_saved)}$$"
    )

    return make_payload(
        "44_geyser_timer_and_insulation_cost_savings",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate daily time saved ({fmt_sa(dh)} h) and daily energy saved ({fmt_sa(p_kw * dh)} kWh)", 2),
            (f"Calculate monthly energy saved = {fmt_sa(kwh_saved)} kWh", 1),
            (f"Calculate monthly Rand saving = R{fmt_sa(rand_saved)}", 2),
        ],
        [
            "Note that the power rating is already given in kilowatts ($\\text{kW}$), so do not divide by $1000$ again.",
            f"Multiply ${fmt_sa(p_kw)}\\text{{ kW}}$ by the hours saved per day (${fmt_sa(dh)}\\text{{ h}}$) and by ${days}\\text{{ days}}$.",
            f"$\\Delta E_{{\\text{{month}}}} = {fmt_sa(kwh_saved)}\\text{{ kWh}}$; saving $= \\text{{R}}{fmt_sa(rand_saved)}$.",
        ],
        ["dividing_kw_by_1000_again", "calculating_after_cost_instead_of_cost_difference"],
        ["geyser timer", "thermal insulation", "electricity saving"],
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# Subskill 45: Prepaid electricity voucher units and operating duration
# ---------------------------------------------------------------------------
def arch_45_prepaid_electricity_voucher_units_and_duration(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    voucher_rands = r.choice([300, 450, 500, 600, 750])
    tariff = r.choice([2.50, 3.00])
    units_kwh = round(voucher_rands / tariff, 1)
    daily_kwh = r.choice([8.0, 10.0, 12.0, 15.0])
    days_last = round(units_kwh / daily_kwh, 2)

    prompt = (
        f"A student buys a prepaid electricity voucher for **$\\text{{R}}{voucher_rands}$** at a flat tariff of **$\\text{{R}}{fmt_sa(tariff)}\\text{{ per kWh}}$**.\n"
        f"The student's apartment consumes an average of **${fmt_sa(daily_kwh)}\\text{{ kWh per day}}$**.\n\n"
        f"1. Calculate the number of electricity units (in $\\text{{kWh}}$) loaded onto the prepaid meter.\n"
        f"2. Calculate how many days this prepaid voucher will last at an average consumption of ${fmt_sa(daily_kwh)}\\text{{ kWh/day}}$.\n"
        f"3. If the student also runs a $2000\\text{{ W}}$ heater for $2\\text{{ hours}}$ every evening, calculate the new daily consumption and new number of days the voucher will last."
    )

    new_daily = daily_kwh + 4.0
    new_days = round(units_kwh / new_daily, 2)
    ans_latex = rf"\text{{Units}} = {fmt_sa(units_kwh)}\text{{ kWh}}, \ t_1 = {fmt_sa(days_last)}\text{{ days}}, \ t_2 = {fmt_sa(new_days)}\text{{ days}}"
    sample_answer = (
        f"1. $$\\text{{Units}} = \\frac{{\\text{{Voucher amount}}}}{{\\text{{Tariff}}}} = \\frac{{\\text{{R}}{voucher_rands}}}{{\\text{{R}}{fmt_sa(tariff)}}} = {fmt_sa(units_kwh)}\\text{{ kWh}}$$\n\n"
        f"2. $$\\text{{Days}} = \\frac{{{fmt_sa(units_kwh)}\\text{{ kWh}}}}{{{fmt_sa(daily_kwh)}\\text{{ kWh/day}}}} = {fmt_sa(days_last)}\\text{{ days}}$$\n\n"
        f"3. Extra heater energy per day $= 2{{,}}0\\text{{ kW}} \\times 2\\text{{ h}} = 4{{,}}0\\text{{ kWh/day}}$.\n"
        f"   New daily usage $= {fmt_sa(daily_kwh)} + 4{{,}}0 = {fmt_sa(new_daily)}\\text{{ kWh/day}}$.\n"
        f"   $$\\text{{New duration}} = \\frac{{{fmt_sa(units_kwh)}}}{{{fmt_sa(new_daily)}}} = {fmt_sa(new_days)}\\text{{ days}}$$"
    )

    return make_payload(
        "45_prepaid_electricity_voucher_units_and_duration",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate units = {fmt_sa(units_kwh)} kWh", 1),
            (f"Calculate initial duration = {fmt_sa(days_last)} days", 2),
            (f"Calculate heater addition (+4 kWh/day) and new duration = {fmt_sa(new_days)} days", 2),
        ],
        [
            "Divide the Rand amount by the tariff ($\\text{R/kWh}$) to find the total $\\text{kWh}$ units purchased.",
            f"Divide total units (${fmt_sa(units_kwh)}\\text{{ kWh}}$) by the daily $\\text{{kWh}}$ usage.",
            f"Units $= {fmt_sa(units_kwh)}\\text{{ kWh}}$, initial duration $= {fmt_sa(days_last)}\\text{{ days}}$, with heater $= {fmt_sa(new_days)}\\text{{ days}}$.",
        ],
        ["multiplying_rands_by_tariff_for_units", "adding_watts_directly_to_kwh"],
        ["prepaid electricity", "voucher units", "consumption rate"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 46: Heating water kettle thermal efficiency
# ---------------------------------------------------------------------------
def arch_46_heating_water_kettle_thermal_efficiency(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    p_kettle = r.choice([2000, 2200, 2400])
    t_sec = r.choice([150, 180, 200, 240])
    e_in = p_kettle * t_sec
    eff_pct = r.choice([80, 84, 85, 88, 90])
    e_useful = round(e_in * (eff_pct / 100.0), 1)
    e_wasted = round(e_in - e_useful, 1)

    prompt = (
        f"An electric kettle rated at **${p_kettle}\\text{{ W}}$** operates for **${t_sec}\\text{{ s}}$** to heat water to boiling point.\n"
        f"During this interval, the water absorbs **${fmt_sa(e_useful)}\\text{{ J}}$** of thermal energy.\n\n"
        f"1. Calculate the total electrical energy ($E_{{\\text{{input}}}}$) supplied to the kettle in ${t_sec}\\text{{ s}}$.\n"
        f"2. Calculate the percentage efficiency ($\\eta$) of the kettle.\n"
        f"3. Calculate the amount of energy wasted and state where this wasted energy goes."
    )

    ans_latex = rf"E_{{\text{{in}}}} = {e_in}\text{{ J}}, \ \eta = {eff_pct}\%, \ E_{{\text{{wasted}}}} = {fmt_sa(e_wasted)}\text{{ J}}"
    sample_answer = (
        f"1. $$E_{{\\text{{input}}}} = P \\cdot \\Delta t = {p_kettle} \\times {t_sec} = {e_in}\\text{{ J}}$$\n\n"
        f"2. $$\\eta = \\frac{{E_{{\\text{{useful}}}}}}{{E_{{\\text{{input}}}}}} \\times 100\\% = \\frac{{{fmt_sa(e_useful)}}}{{{e_in}}} \\times 100\\% = {eff_pct}\\%$$\n\n"
        f"3. $$E_{{\\text{{wasted}}}} = E_{{\\text{{input}}}} - E_{{\\text{{useful}}}} = {e_in} - {fmt_sa(e_useful)} = {fmt_sa(e_wasted)}\\text{{ J}}$$\n"
        f"   This energy is dissipated as heat to the body of the kettle and the surrounding air."
    )

    return make_payload(
        "46_heating_water_kettle_thermal_efficiency",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate electrical input energy E_input = {e_in} J", 2),
            (f"Calculate percentage efficiency = {eff_pct}%", 2),
            (f"Calculate wasted energy = {fmt_sa(e_wasted)} J and state lost as heat to surroundings", 2),
        ],
        [
            "First calculate the total electrical energy supplied: $E_{\\text{input}} = P \\Delta t$.",
            f"Use $\\text{{Efficiency}} = \\frac{{E_{{\\text{{useful}}}}}}{{E_{{\\text{{input}}}}}} \\times 100\\%$.",
            f"$E_{{\\text{{in}}}} = {e_in}\\text{{ J}}$, $\\eta = {eff_pct}\\%$, $E_{{\\text{{wasted}}}} = {fmt_sa(e_wasted)}\\text{{ J}}$.",
        ],
        ["inverting_efficiency_ratio_over_100_percent", "dividing_power_by_time_for_energy"],
        ["efficiency", "kettle heating", "useful energy", "energy conservation"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 47: Battery capacity in amp-hours (Ah) and stored energy
# ---------------------------------------------------------------------------
def arch_47_battery_capacity_amp_hours_and_energy(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    v_bat = r.choice([12, 24])
    ah_cap = r.choice([50, 100, 150, 200])
    q_coul = ah_cap * 3600
    e_wh = v_bat * ah_cap
    e_kwh = round(e_wh / 1000.0, 2)
    load_w = r.choice([150, 200, 240, 300])
    hours_run = round(e_wh / load_w, 2)

    prompt = (
        f"A household load-shedding inverter system uses a **${v_bat}\\text{{ V}}$** lithium backup battery rated at **${ah_cap}\\text{{ Ah}}$** (ampere-hours).\n\n"
        f"1. Calculate the total electric charge ($Q$, in coulombs) that the fully charged battery can deliver ($1\\text{{ h}} = 3600\\text{{ s}}$).\n"
        f"2. Calculate the total energy stored in the battery in **watt-hours ($\\text{{Wh}}$)** and in **kilowatt-hours ($\\text{{kWh}}$)**.\n"
        f"3. Calculate how many hours the battery can power a **${load_w}\\text{{ W}}$** load (assuming $100\\%$ inverter efficiency)."
    )

    ans_latex = rf"Q = {q_coul}\text{{ C}}, \ E = {fmt_sa(e_kwh)}\text{{ kWh}}, \ t = {fmt_sa(hours_run)}\text{{ h}}"
    sample_answer = (
        f"1. $$Q = I \\cdot \\Delta t = ({ah_cap}\\text{{ A}}) \\times (3600\\text{{ s}}) = {q_coul}\\text{{ C}}$$\n\n"
        f"2. $$E(\\text{{Wh}}) = V \\times (\\text{{Ah}}) = {v_bat} \\times {ah_cap} = {e_wh}\\text{{ Wh}} = {fmt_sa(e_kwh)}\\text{{ kWh}}$$\n\n"
        f"3. $$t = \\frac{{E(\\text{{Wh}})}}{{P(\\text{{W}})}} = \\frac{{{e_wh}}}{{{load_w}}} = {fmt_sa(hours_run)}\\text{{ hours}}$$"
    )

    return make_payload(
        "47_battery_capacity_amp_hours_and_energy",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate total charge Q = {q_coul} C", 2),
            (f"Calculate stored energy = {e_wh} Wh = {fmt_sa(e_kwh)} kWh", 2),
            (f"Calculate backup runtime = {fmt_sa(hours_run)} hours", 1),
        ],
        [
            "$1\\text{ Ah} = 1\\text{ A} \\times 3600\\text{ s} = 3600\\text{ C}$.",
            f"Multiply battery voltage (${v_bat}\\text{{ V}}$) by capacity (${ah_cap}\\text{{ Ah}}$) to get energy in $\\text{{Wh}}$.",
            f"$Q = {q_coul}\\text{{ C}}$, $E = {fmt_sa(e_kwh)}\\text{{ kWh}}$, $t = {fmt_sa(hours_run)}\\text{{ h}}$.",
        ],
        ["confusing_amp_hours_with_watt_hours", "forgetting_3600_seconds_per_hour"],
        ["ampere-hour", "battery capacity", "load-shedding inverter", "kWh storage"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 48: Proportional scaling of power when voltage or resistance changes
# ---------------------------------------------------------------------------
def arch_48_proportional_scaling_power_voltage_changes(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    p_init = r.choice([20, 30, 36, 40, 48, 60, 80])
    factor_name, v_mult, r_mult = r.choice([
        ("doubled while its resistance remains constant", 2.0, 1.0),
        ("tripled while its resistance remains constant", 3.0, 1.0),
        ("halved while its resistance remains constant", 0.5, 1.0),
        ("doubled while its resistance is also doubled", 2.0, 2.0),
        ("kept constant while its resistance is halved", 1.0, 0.5),
    ])
    p_factor = (v_mult ** 2) / r_mult
    p_new = round(p_init * p_factor, 2)

    prompt = (
        f"An ohmic resistor dissipates a power of **$P = {p_init}\\text{{ W}}$** when connected to a power supply.\n\n"
        f"The potential difference across the resistor is now **{factor_name}**.\n"
        f"1. Write down the formula relating power ($P$), potential difference ($V$), and resistance ($R$).\n"
        f"2. Use proportional reasoning to determine the factor by which the power changes.\n"
        f"3. Calculate the new power ($P_{{\\text{{new}}}}$) dissipated in the resistor."
    )

    ans_latex = rf"P_{{\text{{new}}}} = {fmt_sa(p_factor)} P = {fmt_sa(p_new)}\text{{ W}}"
    sample_answer = (
        f"1. $$P = \\frac{{V^2}}{{R}}$$\n\n"
        f"2. Substituting $V_{{\\text{{new}}}} = {fmt_sa(v_mult)}V$ and $R_{{\\text{{new}}}} = {fmt_sa(r_mult)}R$:\n"
        f"   $$P_{{\\text{{new}}}} = \\frac{{({fmt_sa(v_mult)}V)^2}}{{{fmt_sa(r_mult)}R}} = \\frac{{{fmt_sa(v_mult ** 2)}}}{{{fmt_sa(r_mult)}}} \\left(\\frac{{V^2}}{{R}}\\right) = {fmt_sa(p_factor)} P$$\n\n"
        f"3. $$P_{{\\text{{new}}}} = {fmt_sa(p_factor)} \\times {p_init} = {fmt_sa(p_new)}\\text{{ W}}$$"
    )

    return make_payload(
        "48_proportional_scaling_power_voltage_changes",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Formula P = V^2 / R", 1),
            (f"Determine scaling factor = {fmt_sa(p_factor)}", 2),
            (f"Calculate P_new = {fmt_sa(p_new)} W", 2),
        ],
        [
            "Use $P = \\frac{V^2}{R}$ so that both $V$ and $R$ appear explicitly in the equation.",
            f"Note that $V$ is **squared** in $P = \\frac{{V^2}}{{R}}$, so multiplying $V$ by ${fmt_sa(v_mult)}$ multiplies $V^2$ by ${fmt_sa(v_mult ** 2)}$.",
            f"Scaling factor $= {fmt_sa(p_factor)}$; $P_{{\\text{{new}}}} = {fmt_sa(p_new)}\\text{{ W}}$.",
        ],
        ["linear_scaling_forgetting_v_squared_in_power", "using_p_vi_assuming_current_is_constant_when_v_changes"],
        ["proportional reasoning", "power scaling", "P = V^2/R"],
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Subskill 49: Comprehensive circuit network and power synthesis (with SVG)
# ---------------------------------------------------------------------------
def arch_49_comprehensive_circuit_network_and_power_synthesis(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    rs = r.choice([2, 3, 4, 5])
    r1, r2 = r.choice([(6, 3), (12, 4), (12, 6), (20, 5)])
    rp = int((r1 * r2) // (r1 + r2))
    r_ext = rs + rp
    i_tot = r.choice([2.0, 2.5, 3.0, 4.0])
    v_tot = round(i_tot * r_ext, 1)
    v_p = round(i_tot * rp, 2)
    i1 = round(v_p / r1, 2)
    p_rs = round((i_tot ** 2) * rs, 2)
    p_r1 = round((v_p ** 2) / r1, 2)

    svg = _svg_composite_circuit(v_tot, rs, r1, r2)

    prompt = (
        f"A composite circuit has a **${fmt_sa(v_tot)}\\text{{ V}}$** battery of negligible internal resistance connected to a series resistor "
        f"**$R_s = {rs}\\ \\Omega$** and a parallel bank of **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel bank and the total circuit resistance ($R_{{\\text{{total}}}}$).\n"
        f"2. Calculate the main-branch current ($I_{{\\text{{total}}}}$) and the potential difference ($V_p$) across the parallel bank.\n"
        f"3. Calculate the electrical power dissipated in **$R_s$** and the electrical power dissipated in **$R_1$**."
    )

    ans_latex = rf"R_{{\text{{tot}}}} = {r_ext}\ \Omega, \ I_{{\text{{tot}}}} = {fmt_sa(i_tot)}\text{{ A}}, \ V_p = {fmt_sa(v_p)}\text{{ V}}, \ P_{{R_s}} = {fmt_sa(p_rs)}\text{{ W}}, \ P_{{R_1}} = {fmt_sa(p_r1)}\text{{ W}}"
    sample_answer = (
        f"1. $$R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = {rp}\\ \\Omega \\implies R_{{\\text{{total}}}} = {rs} + {rp} = {r_ext}\\ \\Omega$$\n\n"
        f"2. $$I_{{\\text{{total}}}} = \\frac{{{fmt_sa(v_tot)}}}{{{r_ext}}} = {fmt_sa(i_tot)}\\text{{ A}}, \\quad V_p = I_{{\\text{{total}}}} \\cdot R_p = {fmt_sa(i_tot)} \\times {rp} = {fmt_sa(v_p)}\\text{{ V}}$$\n\n"
        f"3. $$P_{{R_s}} = I_{{\\text{{total}}}}^2 R_s = ({fmt_sa(i_tot)})^2 \\times {rs} = {fmt_sa(p_rs)}\\text{{ W}}$$\n"
        f"   $$P_{{R_1}} = \\frac{{V_p^2}}{{R_1}} = \\frac{{{fmt_sa(v_p)}^2}}{{{r1}}} = {fmt_sa(p_r1)}\\text{{ W}}$$"
    )

    return make_payload(
        "49_comprehensive_circuit_network_and_power_synthesis",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            (f"Calculate Rp = {rp} Ohm and R_total = {r_ext} Ohm", 2),
            (f"Calculate I_total = {fmt_sa(i_tot)} A and V_p = {fmt_sa(v_p)} V", 2),
            (f"Calculate power in Rs = {fmt_sa(p_rs)} W and power in R1 = {fmt_sa(p_r1)} W", 3),
        ],
        [
            "Solve the circuit sequentially: $R_p \\to R_{\\text{total}} \\to I_{\\text{total}} \\to V_p$.",
            f"Use $P_{{R_s}} = I_{{\\text{{total}}}}^2 R_s$ for the series resistor and $P_{{R_1}} = \\frac{{V_p^2}}{{R_1}}$ for branch 1.",
            f"$R_{{\\text{{tot}}}} = {r_ext}\\ \\Omega$, $I_{{\\text{{tot}}}} = {fmt_sa(i_tot)}\\text{{ A}}$, $P_{{R_s}} = {fmt_sa(p_rs)}\\text{{ W}}$, $P_{{R_1}} = {fmt_sa(p_r1)}\\text{{ W}}$.",
        ],
        ["using_main_current_in_parallel_branch_power_formula", "using_battery_voltage_for_single_component_power"],
        ["circuit synthesis", "series-parallel power", "Ohm's Law"],
        difficulty="hard",
        diagram_spec={"kind": "inline_svg", "diagram_role": "context", "svg": svg},
    )


# ---------------------------------------------------------------------------
# Subskill 50: Circuit diagnostic autopsy and misconception repair
# ---------------------------------------------------------------------------
def arch_50_circuit_diagnostic_autopsy_and_misconception_repair(seed: Optional[int] = None) -> Dict[str, Any]:
    r = rng(seed)
    case = r.choice([
        {
            "desc": "Two resistors of $R_1 = 6\\ \\Omega$ and $R_2 = 12\\ \\Omega$ are connected in parallel across a $12\\text{ V}$ battery.",
            "wrong_work": "$\\frac{1}{R_p} = \\frac{1}{6} + \\frac{1}{12} = \\frac{3}{12} = 0{,}25\\ \\Omega$, so $I = \\frac{12}{0{,}25} = 48\\text{ A}$.",
            "flaw": "The learner forgot to take the reciprocal (invert $\\frac{1}{R_p} = \\frac{3}{12}$) to find $R_p = 4\\ \\Omega$.",
            "correct": "$R_p = \\frac{12}{3} = 4\\ \\Omega$ and $I = \\frac{12}{4} = 3\\text{ A}$.",
        },
        {
            "desc": "A $4\\ \\Omega$ series resistor is connected to a parallel combination ($R_p = 2\\ \\Omega$) across an $18\\text{ V}$ battery. A learner calculates the power in the $4\\ \\Omega$ resistor.",
            "wrong_work": "$P_{4\\Omega} = \\frac{V^2}{R} = \\frac{18^2}{4} = 81\\text{ W}$.",
            "flaw": "The learner substituted the total battery voltage ($18\\text{ V}$) instead of the potential difference across the $4\\ \\Omega$ resistor alone ($V_{4\\Omega} = I \\times 4 = 3 \\times 4 = 12\\text{ V}$).",
            "correct": "$I = \\frac{18}{4 + 2} = 3\\text{ A}$, so $P_{4\\Omega} = I^2 R = 3^2 \\times 4 = 36\\text{ W}$.",
        },
        {
            "desc": "A $2000\\text{ W}$ heater is used for $30\\text{ minutes}$ at a tariff of $\\text{R}2{,}50\\text{/kWh}$.",
            "wrong_work": "$\\text{Cost} = 2000 \\times 30 \\times 2{,}50 = \\text{R}150\\ 000$.",
            "flaw": "The learner failed to convert power from watts to kilowatts ($2000\\text{ W} = 2\\text{ kW}$) and failed to convert time from minutes to hours ($30\\text{ min} = 0{,}5\\text{ h}$).",
            "correct": "$E = 2\\text{ kW} \\times 0{,}5\\text{ h} = 1{,}0\\text{ kWh}$, so $\\text{Cost} = 1{,}0 \\times \\text{R}2{,}50 = \\text{R}2{,}50$.",
        },
    ])

    prompt = (
        f"**Diagnostic Error Analysis:**\n"
        f"Problem statement: *{case['desc']}*\n"
        f"Learner's flawed attempt: *{case['wrong_work']}*\n\n"
        f"1. Identify the specific conceptual or mathematical error in the learner's working.\n"
        f"2. Write out the fully corrected calculation and final answer."
    )

    ans_latex = rf"\text{{Corrected: }} {case['correct']}"
    sample_answer = (
        f"1. **Identified Misconception / Error:**\n"
        f"   {case['flaw']}\n\n"
        f"2. **Corrected Solution:**\n"
        f"   {case['correct']}"
    )

    return make_payload(
        "50_circuit_diagnostic_autopsy_and_misconception_repair",
        seed,
        prompt,
        ans_latex,
        sample_answer,
        [
            ("Accurately diagnose the conceptual/unit error in the learner's attempt", 2),
            ("Provide the complete, valid step-by-step calculation and final answer", 3),
        ],
        [
            "Check each formula substitution for unit consistency ($\\text{kW}$, hours) and component-specific values ($V_i$ vs $V_{\\text{total}}$, $R_p$ vs $1/R_p$).",
            case["flaw"],
            case["correct"],
        ],
        ["forgetting_to_invert_1_over_rp", "forgot_converting_watts_to_kw"],
        ["diagnostic autopsy", "misconception repair", "circuit error analysis"],
        difficulty="hard",
    )


BUILDERS_26_50: Dict[str, Callable[[Optional[int]], Dict[str, Any]]] = {
    "26_internal_resistance_with_series_parallel_load": arch_26_internal_resistance_with_series_parallel_load,
    "27_terminal_voltage_vs_current_graph_analysis": arch_27_terminal_voltage_vs_current_graph_analysis,
    "28_switch_effect_on_terminal_potential_difference": arch_28_switch_effect_on_terminal_potential_difference,
    "29_electrical_power_definition_and_vi": arch_29_electrical_power_definition_and_vi,
    "30_power_dissipation_i_squared_r": arch_30_power_dissipation_i_squared_r,
    "31_power_dissipation_v_squared_over_r": arch_31_power_dissipation_v_squared_over_r,
    "32_solving_for_resistance_or_current_from_power": arch_32_solving_for_resistance_or_current_from_power,
    "33_electrical_energy_joules_w_vit": arch_33_electrical_energy_joules_w_vit,
    "34_power_comparison_series_vs_parallel_bulbs": arch_34_power_comparison_series_vs_parallel_bulbs,
    "35_bulb_brightness_changes_when_switch_toggled": arch_35_bulb_brightness_changes_when_switch_toggled,
    "36_appliance_power_ratings_and_fuse_selection": arch_36_appliance_power_ratings_and_fuse_selection,
    "37_multi_appliance_parallel_household_circuit": arch_37_multi_appliance_parallel_household_circuit,
    "38_watt_to_kilowatt_and_kwh_definition": arch_38_watt_to_kilowatt_and_kwh_definition,
    "39_kilowatt_hour_energy_consumption_calculation": arch_39_kilowatt_hour_energy_consumption_calculation,
    "40_single_appliance_monthly_electricity_cost": arch_40_single_appliance_monthly_electricity_cost,
    "41_multi_appliance_household_audit_bill": arch_41_multi_appliance_household_audit_bill,
    "42_stepped_inclining_block_tariff_calculation": arch_42_stepped_inclining_block_tariff_calculation,
    "43_energy_saving_led_vs_incandescent_comparison": arch_43_energy_saving_led_vs_incandescent_comparison,
    "44_geyser_timer_and_insulation_cost_savings": arch_44_geyser_timer_and_insulation_cost_savings,
    "45_prepaid_electricity_voucher_units_and_duration": arch_45_prepaid_electricity_voucher_units_and_duration,
    "46_heating_water_kettle_thermal_efficiency": arch_46_heating_water_kettle_thermal_efficiency,
    "47_battery_capacity_amp_hours_and_energy": arch_47_battery_capacity_amp_hours_and_energy,
    "48_proportional_scaling_power_voltage_changes": arch_48_proportional_scaling_power_voltage_changes,
    "49_comprehensive_circuit_network_and_power_synthesis": arch_49_comprehensive_circuit_network_and_power_synthesis,
    "50_circuit_diagnostic_autopsy_and_misconception_repair": arch_50_circuit_diagnostic_autopsy_and_misconception_repair,
}
