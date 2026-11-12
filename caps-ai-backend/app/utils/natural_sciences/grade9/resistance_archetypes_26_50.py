"""Grade 9 Natural Sciences - Resistance: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Resistance.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


def _fmt_tex(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African KaTeX comma notation ({,})."""
    return f"{val:.{decimals}f}".replace(".", "{,}")


def _q(
    rng: random.Random,
    code: str,
    subskill: str,
    prompt: str,
    correct: str,
    sol: str,
    marks: int,
    qtype: str,
    tags: List[str],
    tier1: str,
    tier2: str,
    tier3: str,
    options: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    guide = f"Marking Guide ({marks} marks): Award credit for each verified scientific step shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_res_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": qtype,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": marks,
        "marking_schema": guide,
        "marking_guide": guide,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": tags,
    }
    if options is not None:
        item["options"] = options
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _svg_material_current_bars(rng: random.Random, cu_i: float, al_i: float, nic_i: float) -> Dict[str, Any]:
    """Parameterized bar graph comparing electric current for Copper, Aluminium, Nichrome wires."""
    bars = [("Copper", cu_i, "#ea580c"), ("Aluminium", al_i, "#64748b"), ("Nichrome", nic_i, "#2563eb")]
    cols = []
    for idx, (lbl, val, fill) in enumerate(bars):
        h = int((val / 3.0) * 120)
        x = 85 + idx * 105
        y = 165 - h
        cols.append(
            f'<rect x="{x}" y="{y}" width="54" height="{h}" fill="{fill}" stroke="#0f172a"/>'
            f'<text x="{x + 27}" y="{y - 6}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{_fmt_num(val)} A</text>'
            f'<text x="{x + 27}" y="184" font-size="11" fill="#0f172a" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="55" y1="30" x2="55" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="55" y1="165" x2="395" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="220" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Current Through Equal-Size Wires (3,0 V Battery)</text>'
        f'{"".join(cols)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_resistance_vs_length(rng: random.Random, r_per_m: int, max_l: int) -> Dict[str, Any]:
    """Parameterized linear Resistance vs Wire Length graph."""
    max_r = r_per_m * max_l
    svg = (
        f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="65" y1="28" x2="65" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="385" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="355" y2="45" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="210" cy="110" r="4" fill="#1d4ed8"/>'
        f'<circle cx="355" cy="45" r="4" fill="#1d4ed8"/>'
        f'<line x1="65" y1="45" x2="355" y2="45" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<line x1="355" y1="45" x2="355" y2="175" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<text x="56" y="49" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="end">{max_r}</text>'
        f'<text x="56" y="114" font-size="10.5" fill="#334155" text-anchor="end">{max_r // 2}</text>'
        f'<text x="355" y="191" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{max_l}</text>'
        f'<text x="210" y="191" font-size="10.5" fill="#334155" text-anchor="middle">{_fmt_num(max_l / 2.0)}</text>'
        f'<text x="225" y="208" font-size="11" fill="#0f172a" text-anchor="middle">Wire length (m)</text>'
        f'<text x="20" y="102" font-size="11" fill="#0f172a" transform="rotate(-90 20 102)" text-anchor="middle">Resistance (ohm)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_current_vs_resistance_curve(rng: random.Random, v_fix: int) -> Dict[str, Any]:
    """Parameterized inverse hyperbola graph of Current (I) vs Resistance (R) at constant voltage."""
    max_i = v_fix / 2.0

    def _px(r_val: float) -> int:
        return int(round(65 + (r_val / 12.0) * 300))

    def _py(i_val: float) -> int:
        return int(round(175 - (i_val / max_i) * 135))

    curve_rs = [1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.5, 9.0, 10.5, 12.0]
    pts = " ".join(f"{_px(rv)},{max(32, _py(v_fix / rv))}" for rv in curve_rs)
    i1, i2, i3 = v_fix / 2.0, v_fix / 4.0, v_fix / 6.0
    x1, y1 = _px(2.0), _py(i1)
    x2, y2 = _px(4.0), _py(i2)
    x3, y3 = _px(6.0), _py(i3)
    x4, y4 = _px(12.0), _py(v_fix / 12.0)
    svg = (
        f'<svg viewBox="0 0 430 225" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="225" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="225" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Current vs Resistance ({v_fix} V Constant Supply)</text>'
        f'<line x1="65" y1="32" x2="65" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="390" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<polyline points="{pts}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<line x1="65" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="175" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="65" y1="{y2}" x2="{x2}" y2="{y2}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="{x2}" y1="{y2}" x2="{x2}" y2="175" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="65" y1="{y3}" x2="{x3}" y2="{y3}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="{x3}" y1="{y3}" x2="{x3}" y2="175" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="{x4}" y1="{y4}" x2="{x4}" y2="175" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<circle cx="{x1}" cy="{y1}" r="4" fill="#dc2626"/>'
        f'<circle cx="{x2}" cy="{y2}" r="4" fill="#dc2626"/>'
        f'<circle cx="{x3}" cy="{y3}" r="4" fill="#dc2626"/>'
        f'<circle cx="{x4}" cy="{y4}" r="3.5" fill="#1d4ed8"/>'
        f'<text x="58" y="{y1 + 4}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="end">{_fmt_num(i1)}</text>'
        f'<text x="58" y="{y2 + 4}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="end">{_fmt_num(i2)}</text>'
        f'<text x="58" y="{y3 + 4}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="end">{_fmt_num(i3)}</text>'
        f'<text x="{x1}" y="191" font-size="10.5" fill="#0f172a" text-anchor="middle">2</text>'
        f'<text x="{x2}" y="191" font-size="10.5" fill="#0f172a" text-anchor="middle">4</text>'
        f'<text x="{x3}" y="191" font-size="10.5" fill="#0f172a" text-anchor="middle">6</text>'
        f'<text x="{x4}" y="191" font-size="10.5" fill="#0f172a" text-anchor="middle">12</text>'
        f'<text x="228" y="212" font-size="11" fill="#0f172a" text-anchor="middle">Resistance R (ohm)</text>'
        f'<text x="20" y="104" font-size="11" fill="#0f172a" transform="rotate(-90 20 104)" text-anchor="middle">Current I (A)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_factor1_type_of_material_copper_vs_nichrome_conductivity(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([("copper", "nichrome"), ("silver", "steel")])
    low_m, hi_m = pair
    prompt = (
        f"Equal lengths ($50\\text{{ cm}}$) and equal thicknesses ($1\\text{{ mm}}$ diameter) of **{low_m}** wire and **{hi_m}** wire are connected individually across a 3 V battery.\n\n"
        "State which wire conducts **larger electric current** and explain what intrinsic factor causes this difference [2]."
    )
    correct = f"{low_m.capitalize()} conducts larger current; Different conductor materials possess distinct intrinsic atomic resistivities/electron mobilities ({low_m} has much lower resistance than {hi_m})"
    sol = (
        f"**Step 1:** **{low_m.capitalize()}** allows a substantially larger current [1].\n\n"
        f"**Step 2:** Even with identical dimensions, **type of material** governs resistance: {low_m} offers lower resistance than {hi_m} [1]."
    )
    return _q(
        rng, "26", "26_factor1_type_of_material_copper_vs_nichrome_conductivity", prompt, correct, sol, 2, "short_answer",
        ["thinking_all_shiny_metals_have_identical_resistivity_myth"],
        "Even with exact same length and diameter, different elements/alloys hold electrons differently.",
        f"{low_m.capitalize()} conducts better (type of material factor).",
        correct,
    )


def arch_27_why_household_cords_use_copper_while_kettles_use_nichrome(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["bar heater", "electric toaster", "steam iron"])
    prompt = (
        f"A **{app}** requires two metallic paths: its heating element wire AND its internal power lead wires.\n\n"
        "Explain why engineers NEVER use copper for the heating coil and NEVER use thin nichrome for mains extension cables [2]."
    )
    correct = "Copper has very low resistance (ideal for cool, low-loss extension leads but won't heat effectively as an element); Nichrome has very high resistance (ideal for heating coils, but an extension cord made of nichrome would drop voltage and dangerously overheat)."
    sol = (
        "**Step 1:** **Mains leads** must have **very low resistance** (copper) so electricity arrives with minimal heat loss [1].\n\n"
        "**Step 2:** **Heating elements** need **high resistance** (nichrome) to convert electrical energy efficiently into heat right where needed [1]."
    )
    return _q(
        rng, "27", "27_why_household_cords_use_copper_while_kettles_use_nichrome", prompt, correct, sol, 2, "short_answer",
        ["swapping_copper_and_nichrome_circuit_roles"],
        "Think: cool supply wire (low R) vs glowing heater wire (high R).",
        "Copper = low R supply wires; Nichrome = high R heating coil.",
        correct,
    )


def arch_28_investigation_material_type_circuit_variables_design(rng: random.Random) -> Dict[str, Any]:
    length = rng.choice([20, 30, 40])
    prompt = (
        f"A class investigates how **metal material type** affects resistance using **{length} cm** strips of copper, aluminium, zinc, and nichrome connected into a 3 V series circuit with an ammeter.\n\n"
        "1. Identify the **independent variable** and **dependent variable** [2].\n"
        "2. Name **two variables that MUST be kept constant** for a fair test [2]."
    )
    correct = f"Independent: Type of metal wire; Dependent: Electric current (ammeter reading / calculated resistance); Controlled: Length ({length} cm), wire thickness/diameter, battery voltage (3 V), and temperature"
    sol = (
        "**Step 1:** **Independent:** Material of the conductor; **Dependent:** Ammeter current reading (indicating resistance) [2].\n\n"
        f"**Step 2:** **Controlled variables:** Conductor length ({length} cm), cross-sectional thickness/diameter, applied voltage, and initial temperature [2]."
    )
    return _q(
        rng, "28", "28_investigation_material_type_circuit_variables_design", prompt, correct, sol, 4, "structured",
        ["failing_to_control_wire_length_and_thickness_when_testing_material"],
        "If you change material, all other THREE resistance factors (length, thickness, temperature) + voltage must stay fixed!",
        f"Ind: material; Dep: current; Ctrl: {length} cm length, thickness, voltage, temperature.",
        correct,
    )


def arch_29_interpreting_material_test_bar_chart_of_current_readings(rng: random.Random) -> Dict[str, Any]:
    cu_i = rng.choice([2.4, 2.7, 3.0])
    al_i = round(cu_i * 0.6, 1)
    nic_i = round(cu_i * 0.15, 1)
    spec = _svg_material_current_bars(rng, cu_i, al_i, nic_i)
    prompt = (
        "Inspect the bar chart recording ammeter current through three identically sized wires (**Copper, Aluminium, Nichrome**) wired across the same 3,0 V battery.\n\n"
        "1. Which metal offered the **HIGHEST electrical resistance**, and how does the bar chart indicate this? [2]\n"
        f"2. Calculate the exact resistance of the **Copper** wire using $R = V/I$ ($V = 3{{,}}0\\text{{ V}}, I = {_fmt_tex(cu_i)}\\text{{ A}}$) [2]."
    )
    r_cu = _fmt_num(3.0 / cu_i, 2)
    r_cu_tex = _fmt_tex(3.0 / cu_i, 2)
    correct = f"Nichrome (allowed lowest current of {_fmt_num(nic_i)} A at equal voltage); Copper R = {r_cu} ohm"
    sol = (
        f"**Step 1:** **Nichrome** carries the **smallest current ({_fmt_num(nic_i)} A)** under identical voltage, proving it has the **highest resistance** [2].\n\n"
        f"**Step 2:** $R_{{\\text{{Cu}}}} = \\frac{{3{{,}}0\\text{{ V}}}}{{{_fmt_tex(cu_i)}\\text{{ A}}}} = \\mathbf{{{r_cu_tex}\\,\\Omega}}$ [2]."
    )
    return _q(
        rng, "29", "29_interpreting_material_test_bar_chart_of_current_readings", prompt, correct, sol, 4, "structured",
        ["thinking_lowest_current_bar_means_lowest_resistance_error"],
        "High current = LOW resistance; Lowest current bar = HIGHEST resistance!",
        f"Nichrome ({_fmt_num(nic_i)} A) highest R; Cu R = {r_cu} ohm.",
        correct, diagram_spec=spec,
    )


def arch_30_factor2_thickness_diameter_cross_sectional_area_rule(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([("thin nichrome strand (0,2 mm)", "thick nichrome rod (1,2 mm)"), ("thin copper strand", "thick battery cable")])
    thin_w, thick_w = pair
    prompt = (
        f"Compare two wires made of the exact same metal and length: a **{thin_w}** vs a **{thick_w}**.\n\n"
        "1. State which wire has **lower electrical resistance** [1].\n"
        "2. State the mathematical relationship between cross-sectional area (thickness) and resistance [1]."
    )
    correct = f"{thick_w.capitalize()}; Resistance is inversely proportional to cross-sectional area (thicker conductor -> lower resistance)"
    sol = (
        f"**Step 1:** The **thicker conductor ({thick_w})** has much **lower resistance** [1].\n\n"
        "**Step 2:** Wider area provides more parallel pathways for electrons, so **resistance is inversely proportional to cross-sectional area** ($R \\propto 1/A$) [1]."
    )
    return _q(
        rng, "30", "30_factor2_thickness_diameter_cross_sectional_area_rule", prompt, correct, sol, 2, "short_answer",
        ["claiming_thicker_wires_have_higher_resistance_myth"],
        "Think of wide multi-lane highway vs narrow single-lane alley!",
        "Thicker = larger area = lower resistance (inversely proportional).",
        correct,
    )


def arch_31_road_lanes_or_pipe_width_analogy_for_wire_thickness(rng: random.Random) -> Dict[str, Any]:
    analogy = rng.choice([("drinking straw vs wide garden hosepipe for flowing water", "wide garden hosepipe allows far higher flow per second (lower resistance)"), ("1-lane rural bridge vs 4-lane highway for cars", "4-lane highway passes far more cars per minute (lower resistance)")])
    scene, meaning = analogy
    prompt = (
        f"Explain how comparing a **{scene}** helps learners remember how conductor diameter controls electrical resistance [2]."
    )
    correct = f"The {meaning}, mirroring how a thicker metal wire offers wider cross-sectional area so more electrons flow easily with lower resistance."
    sol = (
        "**Step 1:** Wider cross-section cuts crowding and frictional bottlenecks [1].\n\n"
        f"**Step 2:** Just as the **{meaning}**, a **thicker wire has lower electrical resistance** [1]."
    )
    return _q(
        rng, "31", "31_road_lanes_or_pipe_width_analogy_for_wire_thickness", prompt, correct, sol, 2, "short_answer",
        ["reversing_pipe_width_analogy_for_resistance"],
        "Wider space = easier passage = smaller resistance!",
        meaning.capitalize(),
        correct,
    )


def arch_32_quantitative_resistance_ratio_when_cross_sectional_area_doubles(rng: random.Random) -> Dict[str, Any]:
    r_thin = rng.choice([12, 16, 24, 30])
    scale = rng.choice([2, 3])
    r_new = r_thin // scale
    prompt = (
        f"A uniform nichrome wire of cross-sectional area **$A$** has an electrical resistance of **${r_thin}\\,\\Omega$**.\n\n"
        f"What is the resistance of a wire of the same material, temperature, and length whose cross-sectional area is increased **{scale} times** to **${scale}A$**? [2]"
    )
    correct = f"{r_new} ohm"
    sol = (
        "**Step 1:** Because $R$ is **inversely proportional** to cross-sectional area ($R \\propto 1/A$), multiplying area by " + str(scale) + " divides resistance by " + str(scale) + " [1].\n\n"
        f"**Step 2:** $R_{{\\text{{new}}}} = \\frac{{{r_thin}}}{{{scale}}} = \\mathbf{{{r_new}\\,\\Omega}}$ [1]."
    )
    return _q(
        rng, "32", "32_quantitative_resistance_ratio_when_cross_sectional_area_doubles", prompt, correct, sol, 2, "short_answer",
        ["multiplying_resistance_when_area_increases_error"],
        "Remember INVERSE proportionality: bigger area -> SMALLER resistance!",
        f"{r_thin} / {scale} = {r_new} ohm.",
        correct,
    )


def arch_33_thick_jumper_cables_vs_thin_fuse_wire_thickness_application(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("car battery jumper cables", "must be super thick copper braids to offer minimal resistance when starting high ~200 A starter currents without melting"),
        ("filament of a thin safety fuse wire", "must be narrow/thin so excess fault current meets concentrated resistance, heats rapidly, and melts to break the circuit safely"),
    ])
    comp, exp = pair
    prompt = (
        f"Using conductor thickness principles, justify the design diameter chosen for **{comp}** [2]."
    )
    correct = exp.capitalize()
    sol = (
        "**Step 1:** Link wire diameter inversely to electrical resistance ($R \\propto 1/A$) [1].\n\n"
        f"**Step 2:** Therefore **{comp}** {exp} [1]."
    )
    return _q(
        rng, "33", "33_thick_jumper_cables_vs_thin_fuse_wire_thickness_application", prompt, correct, sol, 2, "short_answer",
        ["thinking_thick_car_starter_cables_are_used_for_high_resistance_myth"],
        "Does a jumper cable want ultra-low R (heavy current) or deliberate rapid heat melt (fuse)?",
        exp.capitalize(),
        correct,
    )


def arch_34_factor3_length_of_conductor_direct_proportionality_rule(rng: random.Random) -> Dict[str, Any]:
    l1, l2 = rng.choice([(20, 60), (25, 75), (30, 90)])
    prompt = (
        f"A learner measures current through a **{l1} cm** uniform nichrome wire across 3 V, then repeats using a **{l2} cm** piece of the identical wire spool.\n\n"
        "Predict how resistance and ammeter current change in the longer wire, stating the mathematical relationship between length and resistance [2]."
    )
    correct = "Longer wire has higher resistance so current decreases; Electrical resistance is directly proportional to conductor length (R proportional to L)."
    sol = (
        "**Step 1:** Electrons endure more lattice collisions traveling a longer wire path, so **resistance increases** and **current drops** [1].\n\n"
        "**Step 2:** Law: **Resistance is directly proportional to length** ($R \\propto L$) [1]."
    )
    return _q(
        rng, "34", "34_factor3_length_of_conductor_direct_proportionality_rule", prompt, correct, sol, 2, "short_answer",
        ["claiming_longer_wires_have_less_resistance_error"],
        "Longer path = more obstacles/collisions = higher resistance!",
        "Directly proportional: longer length -> higher R -> lower current.",
        correct,
    )


def arch_35_long_extension_cord_resistance_and_voltage_drop_hazard(rng: random.Random) -> Dict[str, Any]:
    len_m = rng.choice([30, 50])
    prompt = (
        f"On a building site, workers run a heavy concrete mixer off a tightly coiled **{len_m} m long** electrical extension drum.\n\n"
        "Why do electricians strictly instruct workers to **unwind** long extension reels completely and avoid chaining multiple thin cords together? [2]"
    )
    correct = f"A {len_m} m cord has significant total resistance that generates substantial heat; leaving the coil wound traps heat inside melted insulation (fire risk) and drops terminal voltage at the motor."
    sol = (
        f"**Step 1:** Greater wire length ({len_m} m) adds cumulative resistance ($R \\propto L$), warming the cable under heavy current [1].\n\n"
        "**Step 2:** Coiled turns trap thermal energy leading to **insulation melt/electrical fire**, and resistance reduces voltage reaching the tool [1]."
    )
    return _q(
        rng, "35", "35_long_extension_cord_resistance_and_voltage_drop_hazard", prompt, correct, sol, 2, "short_answer",
        ["thinking_coiled_extension_cords_cannot_overheat_myth"],
        "Remember $R \\propto L$: long cord heats up, and coiled layers cannot cool down!",
        "Resistance heat gets trapped inside wound reel -> melting/fire + voltage drop.",
        correct,
    )


def arch_36_quantitative_r_proportional_to_l_calculations(rng: random.Random) -> Dict[str, Any]:
    l1 = rng.choice([2, 3, 4])
    r_unit = rng.choice([3, 4, 5])
    r1 = l1 * r_unit
    factor = rng.choice([2, 3])
    l2 = l1 * factor
    r2 = r1 * factor
    prompt = (
        f"A **{l1} m** length of uniform alloy wire has a resistance of **${r1}\\,\\Omega$**.\n\n"
        f"Calculate the resistance of a **{l2} m** length cut from the exact same wire spool at the same temperature [2]."
    )
    correct = f"{r2} ohm"
    sol = (
        f"**Step 1:** Since $R \\propto L$, scaling length by ${l2}/{l1} = {factor}$ multiplies resistance by **{factor}** [1].\n\n"
        f"**Step 2:** $R_2 = {factor} \\times {r1}\\,\\Omega = \\mathbf{{{r2}\\,\\Omega}}$ [1]."
    )
    return _q(
        rng, "36", "36_quantitative_r_proportional_to_l_calculations", prompt, correct, sol, 2, "short_answer",
        ["dividing_resistance_when_wire_length_increases_error"],
        "Longer wire means proportional increase in resistance!",
        f"{r1} x {factor} = {r2} ohm.",
        correct,
    )


def arch_37_graphite_strip_current_vs_clip_length_graph_analysis(rng: random.Random) -> Dict[str, Any]:
    r_per_m = rng.choice([4, 6, 8])
    max_l = rng.choice([4, 6])
    max_r = r_per_m * max_l
    spec = _svg_resistance_vs_length(rng, r_per_m, max_l)
    half_l = _fmt_num(max_l / 2.0)
    half_l_tex = _fmt_tex(max_l / 2.0)
    half_r = max_r // 2
    prompt = (
        "Inspect the experimental graph plotting electrical resistance against wire length for a constant-diameter nichrome conductor.\n\n"
        "1. State the relationship revealed by the straight line passing through $(0, 0)$ [1].\n"
        f"2. Read or compute the wire's resistance at **{half_l} m** and resistance per metre [2]."
    )
    correct = f"Resistance is directly proportional to length; {half_r} ohm at {half_l} m ({r_per_m} ohm/m)"
    sol = (
        "**Step 1:** Straight line through origin confirms **resistance is directly proportional to length** ($R \\propto L$) [1].\n\n"
        f"**Step 2:** Gradient = ${max_r} / {max_l} = {r_per_m}\\,\\Omega/\\text{{m}}$; at ${half_l_tex}\\text{{ m}}$, $R = \\mathbf{{{half_r}\\,\\Omega}}$ [2]."
    )
    return _q(
        rng, "37", "37_graphite_strip_current_vs_clip_length_graph_analysis", prompt, correct, sol, 3, "structured",
        ["misreading_straight_line_through_origin_proportionality"],
        "Find gradient (max R / max L) to get ohm per metre, then evaluate at midpoint!",
        f"Directly proportional; {half_r} ohm at {half_l} m ({r_per_m} ohm/m).",
        correct, diagram_spec=spec,
    )


def arch_38_factor4_temperature_effect_on_metal_lattice_vibrations(rng: random.Random) -> Dict[str, Any]:
    metal = rng.choice(["copper coil", "iron filament", "nichrome wire"])
    prompt = (
        f"A learner heats a **{metal}** gently over a Bunsen burner while it stays wired in an ammeter circuit, and observes the current **dropping**.\n\n"
        "Explain microscopically why raising temperature increases the electrical resistance of a metal conductor [2]."
    )
    correct = "Heating gives fixed metal lattice ions more kinetic energy so they vibrate faster and with wider amplitude, colliding far more frequently with drifting electrons and obstructing current flow."
    sol = (
        "**Step 1:** Higher temperature increases thermal **vibration energy of the positive metal ions** in the lattice [1].\n\n"
        "**Step 2:** Wider vibrations present larger targets, increasing **collisions with flowing electrons** -> higher resistance & lower current [1]."
    )
    return _q(
        rng, "38", "38_factor4_temperature_effect_on_metal_lattice_vibrations", prompt, correct, sol, 2, "short_answer",
        ["thinking_hot_metals_conduct_better_myth"],
        "For normal METALS, hotter = atoms shake harder = MORE collisions with passing electrons!",
        "Faster metal ion vibrations increase collisions with drifting electrons -> higher R.",
        correct,
    )


def arch_39_comparing_cold_vs_glowing_hot_light_bulb_filament_resistance(rng: random.Random) -> Dict[str, Any]:
    r_cold = rng.choice([15, 20])
    r_hot = r_cold * rng.choice([10, 12])
    prompt = (
        f"A torch bulb tungsten filament measures **$R = {r_cold}\\,\\Omega$** when cold at room temperature ($20\\,^\\circ\\text{{C}}$), yet measures **$R = {r_hot}\\,\\Omega$** once glowing white-hot at $2500\\,^\\circ\\text{{C}}$.\n\n"
        "Which factor affecting resistance explains this ten-fold surge in resistance?"
    )
    correct = "Temperature — extreme thermal lattice vibrations in hot tungsten impede electron flow far more strongly than at room temperature."
    distractors = [
        "Length — the filament stretches out to ten times its physical length whenever plugged in.",
        "Material transmutation — tungsten turns into plastic when heated.",
        "Colour — white light pushes electrons backwards out of the socket.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Dimensions and material of the filament didn't suddenly change ten-fold — its **temperature** jumped from $20\\,^\\circ\\text{C}$ to $2500\\,^\\circ\\text{C}$.\n"
        f"**Step 2:** **Temperature** strongly increases metal resistance (**{r_cold} -> {r_hot} $\\Omega$**) [2]."
    )
    return _q(
        rng, "39", "39_comparing_cold_vs_glowing_hot_light_bulb_filament_resistance", prompt, correct, sol, 2, "multiple_choice",
        ["assuming_ohm_resistance_never_changes_with_temperature_myth"],
        "What changed dramatically between 20 °C off and 2500 °C glowing white-hot?",
        "Temperature!",
        correct, options=options,
    )


def arch_40_combined_four_factor_wire_ranking_high_vs_low_resistance(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["HIGHEST resistance (lowest current)", "LOWEST resistance (highest current)"])
    is_hi = "HIGHEST" in target
    prompt = (
        "Four wires are tested at equal battery voltage:\n"
        "- **Wire A:** Long ($100\\text{ cm}$), thin ($0{,}3\\text{ mm}$), nichrome, heated to $150\\,^\\circ\\text{C}$\n"
        "- **Wire B:** Short ($10\\text{ cm}$), thick ($2{,}0\\text{ mm}$), copper, cold at $15\\,^\\circ\\text{C}$\n"
        "- **Wire C:** Medium ($50\\text{ cm}$), medium ($1{,}0\\text{ mm}$), steel, $25\\,^\\circ\\text{C}$\n"
        "- **Wire D:** Short ($10\\text{ cm}$), thin ($0{,}3\\text{ mm}$), copper, $25\\,^\\circ\\text{C}$\n\n"
        f"Identify which wire exhibits the **{target}**, listing all **4 resistance factors** justifying your pick [3]."
    )
    if is_hi:
        correct = "Wire A; Combines all four resistance-raising features: high-resistivity nichrome material, longest length (100 cm), thinnest diameter (0,3 mm), and highest temperature (150 °C)"
    else:
        correct = "Wire B; Combines all four resistance-lowering features: low-resistivity copper material, shortest length (10 cm), thickest diameter (2,0 mm), and coldest temperature (15 °C)"
    sol = (
        "**Step 1:** Recall all four rules: Material (Cu low vs NiCr high), Length (short low vs long high), Thickness (thick low vs thin high), Temperature (cold low vs hot high) [1].\n\n"
        f"**Step 2:** Choice: **{correct}** [2]."
    )
    return _q(
        rng, "40", "40_combined_four_factor_wire_ranking_high_vs_low_resistance", prompt, correct, sol, 3, "structured",
        ["confusing_one_of_four_resistance_factors_in_wire_comparison"],
        "Check all 4 levers: Material, Length, Thickness, Temperature.",
        correct,
        correct,
    )


def arch_41_graphing_current_vs_resistance_inverse_relationship_curve(rng: random.Random) -> Dict[str, Any]:
    v_fix = rng.choice([6, 12, 24])
    i2 = v_fix / 4.0
    i4 = v_fix / 12.0
    spec = _svg_current_vs_resistance_curve(rng, v_fix)
    prompt = (
        f"Inspect the plotted **Current ($I$) vs Resistance ($R$)** graph recorded across a fixed **{v_fix} V** battery for resistors of $R = 2\\,\\Omega,\\; 4\\,\\Omega,\\; 6\\,\\Omega$, extended to $12\\,\\Omega$.\n\n"
        "1. State the mathematical relationship between $I$ and $R$ shown by this smooth downward-sloping hyperbola curve [1].\n"
        f"2. Verify from the plotted point at $R = 4\\,\\Omega$ ($I = {_fmt_num(i2)}\\text{{ A}}$) that $I \\times R = V$, and predict the current at $R = 12\\,\\Omega$ [2]."
    )
    correct = (
        f"Current is inversely proportional to resistance (I x R = constant = {v_fix} V); "
        f"At R = 4 ohm, {_fmt_num(i2)} A x 4 ohm = {v_fix} V, and at R = 12 ohm, I = {_fmt_num(i4)} A"
    )
    sol = (
        "**Step 1:** As $R$ doubles or triples, $I$ halves or drops to a third along the smooth downward-curving hyperbola -> **current is inversely proportional to resistance** ($I \\propto 1/R$) [1].\n\n"
        f"**Step 2:** $I \\times R = {_fmt_tex(i2)} \\times 4 = {v_fix}\\text{{ V}}$; therefore at $R = 12\\,\\Omega$, $I = \\frac{{{v_fix}}}{{12}} = \\mathbf{{{_fmt_tex(i4)}\\text{{ A}}}}$ [2]."
    )
    return _q(
        rng, "41", "41_graphing_current_vs_resistance_inverse_relationship_curve", prompt, correct, sol, 3, "structured",
        ["expecting_straight_line_through_origin_for_i_vs_r"],
        "Multiply I by R at each plotted point — if the product is constant, it is inverse proportionality (hyperbola)!",
        f"Inversely proportional (hyperbola); I x R = {v_fix} V; at 12 ohm, I = {_fmt_num(i4)} A.",
        correct, diagram_spec=spec,
    )


def arch_42_ohms_law_voltage_vs_current_gradient_determination(rng: random.Random) -> Dict[str, Any]:
    r_val = rng.choice([8, 12, 15, 20])
    i_max = rng.choice([0.5, 1.0, 1.5])
    v_max = r_val * i_max
    prompt = (
        f"On an Ohm's Law graph with **Potential Difference $V$ (y-axis)** plotted against **Current $I$ (x-axis)** for a metal resistor at constant temperature, the straight line passes through $(0; 0)$ and **$(I = {_fmt_tex(i_max)}\\text{{ A}},\\; V = {_fmt_tex(v_max)}\\text{{ V}})$**.\n\n"
        "Compute the **gradient** and state what electrical property it measures [2]."
    )
    correct = f"{r_val} ohm; The gradient (Delta V / Delta I) equals the constant electrical Resistance R"
    sol = (
        f"**Step 1:** $\\text{{Gradient}} = \\frac{{{_fmt_tex(v_max)} - 0}}{{{_fmt_tex(i_max)} - 0}} = \\mathbf{{{r_val}\\,\\Omega}}$ [1].\n\n"
        "**Step 2:** Gradient represents constant **electrical resistance ($R = V/I$)** [1]."
    )
    return _q(
        rng, "42", "42_ohms_law_voltage_vs_current_gradient_determination", prompt, correct, sol, 2, "short_answer",
        ["inverting_v_vs_i_slope_formula"],
        "Slope = rise (V) / run (I) = V / I = Resistance!",
        f"{r_val} ohm (Resistance R).",
        correct,
    )


def arch_43_reading_ammeter_and_voltmeter_table_to_deduce_r(rng: random.Random) -> Dict[str, Any]:
    r_ans = rng.choice([5, 10, 12])
    rows = [(i, i * r_ans) for i in (0.2, 0.4, 0.6)]
    tbl_lines = " | ".join(f"I={_fmt_num(i)} A, V={_fmt_num(v)} V" for i, v in rows)
    prompt = (
        f"A Grade 9 practical yields three meter data pairs across an unknown ceramic resistor:\n**{tbl_lines}**.\n\n"
        "Verify whether the resistor obeys Ohm's Law (constant $R$) and calculate its resistance value [3]."
    )
    correct = f"Yes, ratio V/I is constant across all trials; R = {r_ans} ohm"
    sol = (
        f"**Step 1:** Compute $V/I$ for every row: "
        f"${_fmt_tex(rows[0][1])}/{_fmt_tex(rows[0][0])} = {r_ans}$, "
        f"${_fmt_tex(rows[1][1])}/{_fmt_tex(rows[1][0])} = {r_ans}$, "
        f"${_fmt_tex(rows[2][1])}/{_fmt_tex(rows[2][0])} = {r_ans}$ [2].\n\n"
        f"**Step 2:** Because $V/I$ remains constant, it obeys Ohm's Law with **$R = {r_ans}\\,\\Omega$** [1]."
    )
    return _q(
        rng, "43", "43_reading_ammeter_and_voltmeter_table_to_deduce_r", prompt, correct, sol, 3, "short_answer",
        ["averaging_wrong_columns_for_resistance"],
        "Calculate V / I for each trial row separately to test constancy!",
        f"Constant ratio R = {r_ans} ohm.",
        correct,
    )


def arch_44_why_resistors_protect_leds_from_burning_out(rng: random.Random) -> Dict[str, Any]:
    v_supply = rng.choice([4.5, 6.0, 9.0])
    prompt = (
        f"When connecting a small red LED across a **{_fmt_num(v_supply)} V** battery pack, why is wiring a **220 $\\Omega$–470 $\\Omega$ resistor** in series mandatory, and does it matter whether the resistor sits on the positive side or negative side of the LED? [2]"
    )
    correct = "The resistor limits maximum series current so excess current does not overheat/destroy the delicate semiconductor junction; It works equally well on either side in a single series loop because current is identical throughout a series path."
    sol = (
        "**Step 1:** Series resistance caps circuit current safely (avoiding burnout) [1].\n\n"
        "**Step 2:** Because **current is the same everywhere in a series loop**, placing the protective resistor before OR after the LED protects it equally [1]."
    )
    return _q(
        rng, "44", "44_why_resistors_protect_leds_from_burning_out", prompt, correct, sol, 2, "short_answer",
        ["thinking_resistor_only_protects_if_placed_upstream_of_led"],
        "Does order along a single series wire change total resistance or current?",
        "Caps safe current; either side works identically in series.",
        correct,
    )


def arch_45_designing_fair_test_isolating_length_thickness_or_temperature(rng: random.Random) -> Dict[str, Any]:
    test_f = rng.choice(["wire length (L)", "wire diameter/thickness (A)"])
    if "length" in test_f:
        ctrl = "Wire material (e.g. only nichrome), wire thickness/diameter, voltage, and wire temperature"
    else:
        ctrl = "Wire material (e.g. only nichrome), wire length (e.g. 30 cm each), voltage, and temperature"
    prompt = (
        f"A learner wants to prove experimentally how **{test_f}** alone affects resistance.\n\n"
        "List the **three other physical/circuit factors** that MUST be controlled (held fixed) during all readings [3]."
    )
    correct = ctrl
    sol = (
        f"**Step 1:** To isolate **{test_f}** fairly, only that single variable may change between measurements [1].\n\n"
        f"**Step 2:** Hold constant: **{ctrl}** [2]."
    )
    return _q(
        rng, "45", "45_designing_fair_test_isolating_length_thickness_or_temperature", prompt, correct, sol, 3, "short_answer",
        ["changing_two_wire_properties_simultaneously_error"],
        "Recall all 4 resistance factors + supply voltage — change ONLY 1!",
        ctrl,
        correct,
    )


def arch_46_calculating_resistance_ratio_comparing_two_wires_length_and_area(rng: random.Random) -> Dict[str, Any]:
    r_a = rng.choice([8, 10, 12])
    l_mult = rng.choice([2, 3])
    a_mult = rng.choice([2, 4])
    # R_B = R_A * l_mult / a_mult -> keep whole numbers cleanly!
    r_a = a_mult * rng.choice([3, 4])
    r_b = int(r_a * l_mult / a_mult)
    prompt = (
        f"Wire A (same metal and temperature as Wire B) has length $L$, cross-sectional area $A$, and resistance **${r_a}\\,\\Omega$**.\n\n"
        f"Wire B has length **${l_mult}L$** and larger cross-sectional area **${a_mult}A$**. Calculate the resistance of Wire B [3]."
    )
    correct = f"{r_b} ohm"
    sol = (
        f"**Step 1:** $R \\propto \\frac{{L}}{{A}}$, so multiplying length by **{l_mult}** multiplies $R$ by **{l_mult}**, while widening area by **{a_mult}** divides $R$ by **{a_mult}** [2].\n\n"
        f"**Step 2:** $R_B = {r_a} \\times \\frac{{{l_mult}}}{{{a_mult}}} = \\mathbf{{{r_b}\\,\\Omega}}$ [1]."
    )
    return _q(
        rng, "46", "46_calculating_resistance_ratio_comparing_two_wires_length_and_area", prompt, correct, sol, 3, "short_answer",
        ["applying_both_length_and_area_scaling_backwards"],
        "Multiply by length factor (top) and divide by area factor (bottom)!",
        f"{r_a} x {l_mult} / {a_mult} = {r_b} ohm.",
        correct,
    )


def arch_47_choosing_best_heating_wire_from_material_diameter_length_table(rng: random.Random) -> Dict[str, Any]:
    task = rng.choice([
        ("maximum rapid heat generation for a toaster coil", "Long, very thin nichrome ribbon", "combines high-resistivity alloy, thin area, and long path for maximum resistance"),
        ("lowest-loss overhead Eskom long-distance cable core", "Thick aluminium-steel reinforced or copper conductor", "combines very low-resistivity metal and large thickness to cut line heating"),
    ])
    goal, spec_ans, why = task
    prompt = (
        f"An engineer must select wiring suited for **{goal}**.\n\n"
        "Specify the ideal **material** and **wire thickness** and explain scientifically using resistance factors [2]."
    )
    correct = f"{spec_ans}; {why}"
    sol = (
        f"**Step 1:** Recommended selection: **{spec_ans}** [1].\n\n"
        f"**Step 2:** Justification: it **{why}** [1]."
    )
    return _q(
        rng, "47", "47_choosing_best_heating_wire_from_material_diameter_length_table", prompt, correct, sol, 2, "short_answer",
        ["picking_thin_nichrome_for_power_transmission_lines_error"],
        "Heating device = wants high R; Power transmission = wants lowest R!",
        f"{spec_ans} ({why}).",
        correct,
    )


def arch_48_superconductors_and_zero_resistance_cooling_concept(rng: random.Random) -> Dict[str, Any]:
    temp_k = rng.choice(["-196 °C (liquid nitrogen)", "-269 °C (liquid helium)"])
    prompt = (
        f"In advanced MRI hospital scanners and particle accelerators, special conductors cooled to extremely cold temperatures near **{temp_k}** become **superconductors** whose electrical resistance drops identically to **zero ($0\\,\\Omega$)**.\n\n"
        "State **two major advantages** if electrical current flows through a circuit with literally zero resistance [2]."
    )
    correct = "Zero electrical energy is lost as unwanted heat (100% energy-efficient current flow), and huge currents can circulate continuously for ultra-strong electromagnets without overheating."
    sol = (
        "**Step 1:** If $R = 0\\,\\Omega$, electron–lattice resistance disappears -> **zero wasted heat energy** [1].\n\n"
        "**Step 2:** Massive continuous electric currents sustain powerful **MRI magnetic fields** indefinitely without melting coils [1]."
    )
    return _q(
        rng, "48", "48_superconductors_and_zero_resistance_cooling_concept", prompt, correct, sol, 2, "short_answer",
        ["thinking_superconductors_create_heat_faster_myth"],
        "If R drops to 0 ohm, what happens to collision heat loss?",
        "Zero wasted heat loss; supports huge lossless currents/MRI magnets.",
        correct,
    )


def arch_49_diagnosing_faulty_resistor_investigation_anomalies(rng: random.Random) -> Dict[str, Any]:
    anomaly = rng.choice([
        ("Group left the circuit switched on tightly for 5 continuous minutes while taking 10 readings, causing current to slowly drift downward", "Joule heating warmed the wire (increasing Temperature factor -> raising resistance -> dropping current); switch off briefly between measurements"),
        ("Group attached crocodile clips right onto plastic wire insulation instead of stripped bare metal ends", "Plastic is an insulator (essentially infinite resistance), causing 0 A reading; clamp tightly onto clean bare metal"),
    ])
    obs, diag = anomaly
    prompt = (
        "During a school practical investigating wire length vs resistance, one group records an unexpected error:\n"
        f"**Observation:** *{obs}.*\n\n"
        "Explain the **scientific cause** of this fault and state how to fix their method [2]."
    )
    correct = diag
    sol = (
        "**Step 1 & 2:** Experimental fault analysis & remedy:\n"
        f"{diag} [2]."
    )
    return _q(
        rng, "49", "49_diagnosing_faulty_resistor_investigation_anomalies", prompt, correct, sol, 2, "short_answer",
        ["ignoring_temperature_drift_during_long_wire_practicals"],
        "Think about both unintended heating over time AND accidental insulation contact!",
        diag,
        correct,
    )


def arch_50_resistance_term3_capstone_circuit_and_energy_synthesis(rng: random.Random) -> Dict[str, Any]:
    v = rng.choice([6, 12])
    r = rng.choice([3, 4, 6])
    i_calc = v // r
    prompt = (
        f"A nichrome heating wire of resistance **${r}\\,\\Omega$** is connected across a **${v}\\text{{ V}}$** battery.\n\n"
        f"1. Calculate the steady current drawn ($I = V/R$) [2].\n"
        "2. Now suppose the learner cuts the exact same wire to **half its original length** and reconnects it to the **same battery**. State the new resistance and predict the new current [2]."
    )
    r_half = _fmt_num(r / 2.0)
    r_half_tex = _fmt_tex(r / 2.0)
    i_new = i_calc * 2
    correct = f"Initial I = {i_calc} A; Half length halves resistance to {r_half} ohm, which doubles current to {i_new} A"
    sol = (
        f"**Step 1:** $I = \\frac{{{v}}}{{{r}}} = \\mathbf{{{i_calc}\\text{{ A}}}}$ [2].\n\n"
        f"**Step 2:** Since $R \\propto L$, halving length halves resistance to **${r_half_tex}\\,\\Omega$**, so current **doubles to ${i_new}\\text{{ A}}$** ($I = {v} / {r_half_tex}$) [2]."
    )
    return _q(
        rng, "50", "50_resistance_term3_capstone_circuit_and_energy_synthesis", prompt, correct, sol, 4, "structured",
        ["failing_to_link_halved_length_to_doubled_ohms_law_current"],
        "Combine $R \\propto L$ with $I = V/R$!",
        f"Initial {i_calc} A -> half length = {r_half} ohm -> {i_new} A.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_factor1_type_of_material_copper_vs_nichrome_conductivity": arch_26_factor1_type_of_material_copper_vs_nichrome_conductivity,
    "27_why_household_cords_use_copper_while_kettles_use_nichrome": arch_27_why_household_cords_use_copper_while_kettles_use_nichrome,
    "28_investigation_material_type_circuit_variables_design": arch_28_investigation_material_type_circuit_variables_design,
    "29_interpreting_material_test_bar_chart_of_current_readings": arch_29_interpreting_material_test_bar_chart_of_current_readings,
    "30_factor2_thickness_diameter_cross_sectional_area_rule": arch_30_factor2_thickness_diameter_cross_sectional_area_rule,
    "31_road_lanes_or_pipe_width_analogy_for_wire_thickness": arch_31_road_lanes_or_pipe_width_analogy_for_wire_thickness,
    "32_quantitative_resistance_ratio_when_cross_sectional_area_doubles": arch_32_quantitative_resistance_ratio_when_cross_sectional_area_doubles,
    "33_thick_jumper_cables_vs_thin_fuse_wire_thickness_application": arch_33_thick_jumper_cables_vs_thin_fuse_wire_thickness_application,
    "34_factor3_length_of_conductor_direct_proportionality_rule": arch_34_factor3_length_of_conductor_direct_proportionality_rule,
    "35_long_extension_cord_resistance_and_voltage_drop_hazard": arch_35_long_extension_cord_resistance_and_voltage_drop_hazard,
    "36_quantitative_r_proportional_to_l_calculations": arch_36_quantitative_r_proportional_to_l_calculations,
    "37_graphite_strip_current_vs_clip_length_graph_analysis": arch_37_graphite_strip_current_vs_clip_length_graph_analysis,
    "38_factor4_temperature_effect_on_metal_lattice_vibrations": arch_38_factor4_temperature_effect_on_metal_lattice_vibrations,
    "39_comparing_cold_vs_glowing_hot_light_bulb_filament_resistance": arch_39_comparing_cold_vs_glowing_hot_light_bulb_filament_resistance,
    "40_combined_four_factor_wire_ranking_high_vs_low_resistance": arch_40_combined_four_factor_wire_ranking_high_vs_low_resistance,
    "41_graphing_current_vs_resistance_inverse_relationship_curve": arch_41_graphing_current_vs_resistance_inverse_relationship_curve,
    "42_ohms_law_voltage_vs_current_gradient_determination": arch_42_ohms_law_voltage_vs_current_gradient_determination,
    "43_reading_ammeter_and_voltmeter_table_to_deduce_r": arch_43_reading_ammeter_and_voltmeter_table_to_deduce_r,
    "44_why_resistors_protect_leds_from_burning_out": arch_44_why_resistors_protect_leds_from_burning_out,
    "45_designing_fair_test_isolating_length_thickness_or_temperature": arch_45_designing_fair_test_isolating_length_thickness_or_temperature,
    "46_calculating_resistance_ratio_comparing_two_wires_length_and_area": arch_46_calculating_resistance_ratio_comparing_two_wires_length_and_area,
    "47_choosing_best_heating_wire_from_material_diameter_length_table": arch_47_choosing_best_heating_wire_from_material_diameter_length_table,
    "48_superconductors_and_zero_resistance_cooling_concept": arch_48_superconductors_and_zero_resistance_cooling_concept,
    "49_diagnosing_faulty_resistor_investigation_anomalies": arch_49_diagnosing_faulty_resistor_investigation_anomalies,
    "50_resistance_term3_capstone_circuit_and_energy_synthesis": arch_50_resistance_term3_capstone_circuit_and_energy_synthesis,
}
