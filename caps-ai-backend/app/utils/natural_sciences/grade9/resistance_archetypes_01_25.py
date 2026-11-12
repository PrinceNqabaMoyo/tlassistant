"""Grade 9 Natural Sciences - Resistance: Archetypes 01 to 25.
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


def _svg_resistor_symbols(rng: random.Random, sym_kind: str, oh_val: int, comp_label: str = "X") -> Dict[str, Any]:
    """Parameterized circuit symbol for fixed resistor vs variable rheostat."""
    w = 96 + rng.randint(-6, 6)
    x0 = 210 - w // 2
    is_var = "rheostat" in sym_kind
    arrow = (
        f'<line x1="{x0 + 10}" y1="125" x2="{x0 + w - 10}" y2="52" stroke="#dc2626" stroke-width="2.5"/>'
        f'<polygon points="{x0 + w - 10},52 {x0 + w - 21},55 {x0 + w - 14},64" fill="#dc2626"/>'
        if is_var
        else ""
    )
    cap_txt = f"Component {comp_label} (0–{oh_val} ohm)" if is_var else f"Component {comp_label} ({oh_val} ohm)"
    svg = (
        f'<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="175" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="65" y1="88" x2="{x0}" y2="88" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="{x0}" y="70" width="{w}" height="36" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="{x0 + w}" y1="88" x2="355" y2="88" stroke="#0f172a" stroke-width="2.5"/>'
        f'{arrow}'
        f'<text x="210" y="148" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{cap_txt}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_graphite_rheostat(rng: random.Random, length_cm: int, max_len: int) -> Dict[str, Any]:
    """Parameterized pencil-graphite variable resistor with sliding crocodile clip."""
    clip_x = 85 + int((length_cm / float(max_len)) * 240)
    svg = (
        f'<svg viewBox="0 0 430 195" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="195" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="85" y="96" width="250" height="14" rx="4" fill="#334155" stroke="#0f172a"/>'
        f'<circle cx="85" cy="103" r="6" fill="#dc2626"/>'
        f'<circle cx="{clip_x}" cy="103" r="6" fill="#2563eb"/>'
        f'<line x1="85" y1="103" x2="85" y2="42" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="{clip_x}" y1="103" x2="{clip_x}" y2="42" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="85" y1="42" x2="{clip_x}" y2="42" stroke="#0f172a" stroke-width="2"/>'
        f'<circle cx="{(85 + clip_x) // 2}" cy="42" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="{(85 + clip_x) // 2}" y="46" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">Bulb</text>'
        f'<text x="210" y="138" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Graphite path active length = {length_cm} cm (of {max_len} cm)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_sankey_lamp(rng: random.Random, e_in: int, e_light: int, lamp_name: str) -> Dict[str, Any]:
    """Parameterized Sankey energy flow diagram comparing useful light vs wasted heat."""
    e_heat = e_in - e_light
    h_light = max(14, int(90 * (e_light / float(e_in))))
    h_heat = max(14, 90 - h_light)
    svg = (
        f'<svg viewBox="0 0 430 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="22" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Energy Flow Sankey: {lamp_name}</text>'
        f'<rect x="35" y="65" width="140" height="90" fill="#93c5fd" stroke="#1d4ed8"/>'
        f'<text x="105" y="114" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Input: {e_in} J</text>'
        f'<rect x="175" y="65" width="175" height="{h_light}" fill="#fde047" stroke="#ca8a04"/>'
        f'<text x="262" y="{65 + h_light // 2 + 4}" font-size="10.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Light: {e_light} J</text>'
        f'<rect x="175" y="{65 + h_light + 6}" width="175" height="{h_heat}" fill="#fca5a5" stroke="#dc2626"/>'
        f'<text x="262" y="{65 + h_light + 6 + h_heat // 2 + 4}" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Heat: {e_heat} J</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_resistance_definition_opposition_to_electron_flow(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice(["a thin nichrome filament", "a carbon film resistor", "a long coiled stove element"])
    prompt = (
        f"Inside an active circuit containing **{comp}**, mobile electrons are pushed by the battery yet encounter resistance.\n\n"
        "1. Define **electrical resistance** accurately [2].\n"
        "2. State how increasing circuit resistance (for the same battery voltage) affects electric current strength [1]."
    )
    correct = "The property of a material or component that opposes/restricts the flow of electric charge (electrons); Higher resistance decreases the electric current strength"
    sol = (
        "**Step 1:** **Electrical resistance** is the opposition offered by a conductor or component to the flow of electric charge (electrons) through it [2].\n\n"
        "**Step 2:** For a constant battery voltage, **higher resistance lowers electric current** ($I = V/R$) [1]."
    )
    return _q(
        rng, "01", "01_resistance_definition_opposition_to_electron_flow", prompt, correct, sol, 3, "structured",
        ["thinking_resistance_speeds_up_electrons_myth"],
        "Resistance acts like narrow traffic lanes opposing charge flow!",
        "Opposition to electron/charge flow; higher R -> lower current I.",
        correct,
    )


def arch_02_school_corridor_and_doorway_analogy_for_resistance(rng: random.Random) -> Dict[str, Any]:
    zone = rng.choice([
        ("wide open grassy school sports field", "very low resistance (good copper conductor) — wide open space with minimal collisions"),
        ("tight narrow doorway squeezing only one learner through at a time", "very high resistance (resistor / thin nichrome wire) — severe crowding and collisions limiting flow rate"),
    ])
    place, match = zone
    prompt = (
        "In the textbook *Movement Analogy* for electricity at a South African high school, learners moving from class to break pass through an open field, a busy corridor, and a narrow doorway.\n\n"
        f"Explain which part of an electrical circuit the **{place}** models [2]."
    )
    correct = match.capitalize()
    sol = (
        "**Step 1:** Moving learners correspond to **delocalised electrons**; crowding/bottlenecks mirror **resistance** [1].\n\n"
        f"**Step 2:** Therefore, **{place}** models **{match}** [1]."
    )
    return _q(
        rng, "02", "02_school_corridor_and_doorway_analogy_for_resistance", prompt, correct, sol, 2, "short_answer",
        ["reversing_field_and_doorway_analogy_for_resistance"],
        "Compare free unimpeded movement (low resistance) vs crowded bottleneck (high resistance).",
        match.capitalize(),
        correct,
    )


def arch_03_metallic_lattice_and_delocalised_sea_of_electrons(rng: random.Random) -> Dict[str, Any]:
    metal = rng.choice(["copper wire", "aluminium cable", "silver contact"])
    prompt = (
        f"Metals such as **{metal}** conduct electric current far better than glass or wood because of their unique metallic atomic bonding.\n\n"
        "Describe the **positive ion lattice and 'sea' of delocalised electrons** inside a metal, explaining why free electrons can drift under battery voltage [3]."
    )
    correct = "Metal atoms sit fixed in a regular lattice of positive metal kernels surrounded by a mobile 'sea' of outer delocalised electrons not bound to any single atom; applying voltage makes these free electrons drift steadily towards the positive terminal."
    sol = (
        "**Step 1:** Positive metal ions vibrate in fixed positions forming a **metal lattice** [1].\n\n"
        "**Step 2:** Outer valence electrons break free as **delocalised electrons** shared across the entire metal crystal [1].\n\n"
        "**Step 3:** When connected to a battery, this mobile electron sea drifts uniformly towards the positive (+) terminal, creating electric current [1]."
    )
    return _q(
        rng, "03", "03_metallic_lattice_and_delocalised_sea_of_electrons", prompt, correct, sol, 3, "short_answer",
        ["claiming_positive_metal_ions_flow_down_copper_wires_myth"],
        "Which particles stay locked in fixed lattice positions and which roam freely as a 'sea'?",
        "Fixed positive metal lattice + mobile delocalised electron sea.",
        correct,
    )


def arch_04_electron_lattice_collisions_causing_thermal_heating(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["toaster element", "electric kettle coil", "hairdryer wire"])
    prompt = (
        f"When current passes through a high-resistance **{app}**, the metal wire rapidly grows glowing hot.\n\n"
        "Explain microscopically — in terms of **electron collisions** — why electrical energy turns into heat inside a resistor [2]."
    )
    correct = "Moving electrons collide repeatedly with vibrating positive metal lattice ions, transferring kinetic energy to the ions so they vibrate faster (heating the conductor)."
    sol = (
        "**Step 1:** Drifting electrons bump continuously into fixed **vibrating metal lattice atoms/ions** [1].\n\n"
        "**Step 2:** Each collision transfers kinetic energy into stronger atomic vibrations, which we observe macroscopically as **heat (thermal energy)** [1]."
    )
    return _q(
        rng, "04", "04_electron_lattice_collisions_causing_thermal_heating", prompt, correct, sol, 2, "short_answer",
        ["thinking_heat_comes_from_electrons_burning_oxygen_myth"],
        "Think of bumper cars: drifting electrons bumping fixed lattice atoms make the lattice jiggle faster!",
        "Electron collisions with positive metal lattice ions transfer energy into faster lattice vibrations (heat).",
        correct,
    )


def arch_05_si_unit_ohm_omega_symbol_and_georg_ohm(rng: random.Random) -> Dict[str, Any]:
    r_val = rng.choice([12, 47, 100, 220])
    prompt = (
        f"A circuit component label is stamped **$R = {r_val}\\,\\Omega$**.\n\n"
        "1. Read aloud the full name of the SI unit represented by $\\Omega$ [1].\n"
        "2. Name the German physicist honoured by this unit [1]."
    )
    correct = f"The ohm ({r_val} ohms); Georg Simon Ohm"
    sol = (
        f"**Step 1:** The Greek letter omega (**$\\Omega$**) denotes the **ohm** — the SI unit of electrical resistance [1].\n\n"
        "**Step 2:** Named after German physicist **Georg Simon Ohm**, who formulated Ohm's Law [1]."
    )
    return _q(
        rng, "05", "05_si_unit_ohm_omega_symbol_and_georg_ohm", prompt, correct, sol, 2, "short_answer",
        ["confusing_ohm_omega_with_ampere_or_watt"],
        "Omega symbol = resistance unit named after Ohm.",
        f"{r_val} ohms; Georg Simon Ohm.",
        correct,
    )


def arch_06_electrical_conductors_vs_resistors_definition_and_roles(rng: random.Random) -> Dict[str, Any]:
    role = rng.choice(["conductor wire", "discrete circuit resistor"])
    is_cond = "conductor" in role
    prompt = (
        "All metals offer at least tiny resistance, yet engineers distinguish between **electrical conductors** and **resistors**.\n\n"
        f"Define the role of **{role}** in an electric circuit and name a suitable metal/material [2]."
    )
    if is_cond:
        correct = "An electrical conductor allows current to pass easily with minimal energy loss (e.g. copper connecting wire)."
    else:
        correct = "A resistor is a component deliberately designed to add specific opposition to control current or convert electrical energy to heat/light (e.g. nichrome wire or carbon resistor)."
    sol = (
        "**Step 1:** Compare whether low-loss transport or deliberate opposition is wanted [1].\n\n"
        f"**Step 2:** {correct} [1]."
    )
    return _q(
        rng, "06", "06_electrical_conductors_vs_resistors_definition_and_roles", prompt, correct, sol, 2, "short_answer",
        ["thinking_resistors_are_total_insulators_like_plastic_myth"],
        "Does a resistor stop all current like rubber insulation, or control/oppose current carefully?",
        correct,
        correct,
    )


def arch_07_circuit_symbols_fixed_resistor_vs_variable_rheostat(rng: random.Random) -> Dict[str, Any]:
    sym_kind = rng.choice(["fixed resistor", "variable resistor (rheostat)"])
    oh_val = rng.choice([50, 100, 250, 500])
    comp_label = rng.choice(["X", "Y", "Z"])
    spec = _svg_resistor_symbols(rng, sym_kind, oh_val, comp_label)
    is_var = "rheostat" in sym_kind
    prompt = (
        f"Examine the electronic circuit component **Component {comp_label}** ({oh_val} $\\Omega$ rating) in the diagram.\n\n"
        f"1. Identify whether Component {comp_label} is a **fixed resistor** or a **variable resistor (rheostat)** [1].\n"
        "2. Explain the feature of the symbol that distinguishes the two [1]."
    )
    correct = (
        f"Variable resistor (rheostat); Diagonal arrow across the rectangle indicates adjustable resistance (0 to {oh_val} ohm)"
        if is_var
        else f"Fixed resistor; Plain rectangle with no diagonal adjustment arrow represents constant fixed resistance ({oh_val} ohm)"
    )
    sol = (
        f"**Step 1:** Component {comp_label} is a **{sym_kind}** [1].\n\n"
        f"**Step 2:** {'A diagonal sliding arrow crossing the resistor box denotes adjustability' if is_var else 'A plain unadorned rectangular box (without arrow) denotes fixed resistance'} [1]."
    )
    return _q(
        rng, "07", "07_circuit_symbols_fixed_resistor_vs_variable_rheostat", prompt, correct, sol, 2, "short_answer",
        ["confusing_rheostat_symbol_with_diode_or_fuse"],
        "Look for whether a diagonal adjustment arrow slashes across the rectangle.",
        correct,
        correct, diagram_spec=spec,
    )


def arch_08_resistor_colour_band_purpose_identifying_resistance_value(rng: random.Random) -> Dict[str, Any]:
    band_desc = rng.choice(["red–red–brown–gold", "brown–black–orange–gold", "yellow–violet–brown–gold"])
    prompt = (
        f"Small electronics resistors printed with coloured stripes (such as **{band_desc}**) are mounted inside radios and school circuit boards.\n\n"
        "What is the practical engineering purpose of those **coloured bands**?"
    )
    correct = "They serve as an international colour code telling technicians the exact resistance value in ohms and its manufacturing tolerance."
    distractors = [
        "They are purely aesthetic paint stripes showing which country sold the wire.",
        "They indicate which liquid acid is sealed inside the glass resistor.",
        "They change colour automatically like litmus paper whenever current flows.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Tiny resistors have too little surface area for readable printed digits.\n"
        "**Step 2:** Coloured stripes encode the **numerical resistance in ohms ($\\Omega$)** and percentage tolerance [2]."
    )
    return _q(
        rng, "08", "08_resistor_colour_band_purpose_identifying_resistance_value", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_resistor_stripes_are_decorative_myth"],
        "Think about reading tiny numbers on a component smaller than a grain of rice!",
        "Standardised colour code indicating resistance value in ohms + tolerance.",
        correct, options=options,
    )


def arch_09_voltage_current_resistance_qualitative_control_relationship(rng: random.Random) -> Dict[str, Any]:
    change = rng.choice([("doubling total circuit resistance at constant voltage", "halves the circuit current"), ("reducing resistance while keeping battery voltage fixed", "increases circuit current")])
    cond, outcome = change
    prompt = (
        "An LED strip inside a science project burns out if current is too high, so a learner adds a series resistor.\n\n"
        f"State the effect of **{cond}** on circuit current [2]."
    )
    correct = f"{outcome.capitalize()} because current is inversely proportional to total resistance at fixed voltage"
    sol = (
        "**Step 1:** Voltage pushes charges while resistance opposes motion [1].\n\n"
        f"**Step 2:** Therefore **{cond}** cleanly **{outcome}** [1]."
    )
    return _q(
        rng, "09", "09_voltage_current_resistance_qualitative_control_relationship", prompt, correct, sol, 2, "short_answer",
        ["thinking_adding_resistor_increases_current_myth"],
        "Higher resistance = harder to push -> smaller current.",
        outcome.capitalize(),
        correct,
    )


def arch_10_current_is_not_consumed_inside_a_resistor(rng: random.Random) -> Dict[str, Any]:
    curr = _fmt_num(rng.choice([0.4, 0.6, 0.8]))
    prompt = (
        f"An ammeter wired just **before** a hot 20 $\\Omega$ resistor reads **{curr} A**.\n\n"
        "What does an identical ammeter wired immediately **after** the resistor in the same single series branch read?"
    )
    correct = f"{curr} A — identical! Electrical energy is transferred to heat, NOT electric current/electrons; current entering equals current leaving."
    distractors = [
        "0,0 A — the resistor absorbs and destroys every electron.",
        "Half the current — 50% of the electrons evaporate into heat.",
        "Double the current — electrons speed up after dropping off energy.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Charge is conserved: electrons are NOT eaten inside a resistor — they transfer *energy*, then continue back towards the battery.\n"
        f"**Step 2:** Both ammeters before and after read exactly **{curr} A** [2]."
    )
    return _q(
        rng, "10", "10_current_is_not_consumed_inside_a_resistor", prompt, correct, sol, 2, "multiple_choice",
        ["resistors_consume_current_electrons_myth"],
        "Ask: Are electrons consumed like petrol, or do they stay in the closed circuit loop just dropping off energy?",
        f"Same {curr} A everywhere in series!",
        correct, options=options,
    )


def arch_11_ohms_law_calculating_resistance_r_equals_v_over_i(rng: random.Random) -> Dict[str, Any]:
    i_val = rng.choice([0.5, 1.5, 2.0, 3.0])
    r_val = rng.choice([4, 6, 8, 12])
    v_val = i_val * r_val
    prompt = (
        f"A resistor connected across a **{_fmt_num(v_val)} V** DC supply draws a steady current of **{_fmt_num(i_val)} A**.\n\n"
        "Calculate the resistance **$R$** using Ohm's Law ($R = \\frac{V}{I}$), showing formula, substitution, and unit [3]."
    )
    correct = f"{r_val} ohm"
    sol = (
        "**Step 1:** Formula: **$R = \\frac{V}{I}$** [1].\n\n"
        f"**Step 2:** $R = \\frac{{{_fmt_tex(v_val)}\\text{{ V}}}}{{{_fmt_tex(i_val)}\\text{{ A}}}} = \\mathbf{{{r_val}\\,\\Omega}}$ [2]."
    )
    return _q(
        rng, "11", "11_ohms_law_calculating_resistance_r_equals_v_over_i", prompt, correct, sol, 3, "short_answer",
        ["inverting_ohms_law_as_i_over_v_error"],
        "Ohm's Law: R = V / I.",
        f"{_fmt_num(v_val)} / {_fmt_num(i_val)} = {r_val} ohm.",
        correct,
    )


def arch_12_calculating_current_or_voltage_using_ohms_law_rearrangement(rng: random.Random) -> Dict[str, Any]:
    find_v = rng.choice([True, False])
    r_val = rng.choice([5, 10, 15, 20])
    i_val = rng.choice([0.4, 0.6, 1.2, 1.5])
    v_val = r_val * i_val
    if find_v:
        prompt = (
            f"A steady current of **{_fmt_num(i_val)} A** passes through a **{r_val} $\\Omega$** heating resistor.\n\n"
            "Calculate the potential difference **$V$** across the resistor ($V = I \\cdot R$) [3]."
        )
        correct = f"{_fmt_num(v_val)} V"
        sol = f"**Step 1:** $V = I \\times R$ [1].\n\n**Step 2:** $V = {_fmt_tex(i_val)} \\times {r_val} = \\mathbf{{{_fmt_tex(v_val)}\\text{{ V}}}}$ [2]."
    else:
        prompt = (
            f"A **{r_val} $\\Omega$** resistor is connected directly across a **{_fmt_num(v_val)} V** battery.\n\n"
            "Calculate the current **$I$** flowing through the resistor ($I = \\frac{V}{R}$) [3]."
        )
        correct = f"{_fmt_num(i_val)} A"
        sol = f"**Step 1:** $I = \\frac{{V}}{{R}}$ [1].\n\n**Step 2:** $I = \\frac{{{_fmt_tex(v_val)}}}{{{r_val}}} = \\mathbf{{{_fmt_tex(i_val)}\\text{{ A}}}}$ [2]."
    return _q(
        rng, "12", "12_calculating_current_or_voltage_using_ohms_law_rearrangement", prompt, correct, sol, 3, "short_answer",
        ["rearranging_v_equals_i_r_algebra_error"],
        "Use the Ohm triangle: V on top, I and R on the bottom.",
        correct,
        correct,
    )


def arch_13_useful_resistance_converting_electrical_to_heat_light(rng: random.Random) -> Dict[str, Any]:
    device, output = rng.choice([
        ("electric geyser heating element", "thermal energy to heat household bath water"),
        ("filament desk lamp", "light energy (and thermal energy)"),
        ("bar heater wire coil", "radiant and thermal heat for warming rooms"),
    ])
    prompt = (
        f"Although engineers minimise resistance in transmission power lines, high electrical resistance is **deliberately useful** inside a **{device}**.\n\n"
        "State the intended energy conversion performed by the resistor in this appliance [2]."
    )
    correct = f"Electrical energy -> {output}"
    sol = (
        "**Step 1:** High resistance triggers intense electron–atom collisions converting electrical work purposefully [1].\n\n"
        f"**Step 2:** Conversion in {device}: **Electrical energy $\\rightarrow$ {output}** [1]."
    )
    return _q(
        rng, "13", "13_useful_resistance_converting_electrical_to_heat_light", prompt, correct, sol, 2, "short_answer",
        ["thinking_resistance_is_always_unwanted_waste_myth"],
        "Remember heating appliances NEED high-resistance elements to convert electricity into heat/light!",
        correct,
        correct,
    )


def arch_14_electric_kettle_and_geyser_nichrome_heating_element(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["electric kettle base", "domestic hot-water geyser"])
    prompt = (
        f"Look inside the element tube of an **{app}**: the heating coil is made of **nichrome** (nickel–chromium alloy), whereas its flexible wall cord is pure **copper**.\n\n"
        "1. Explain why **nichrome** is selected for the heating coil while **copper** is used in the plug cord [2].\n"
        "2. What dangerous fault occurs if a copper cord offered high resistance like nichrome? [1]"
    )
    correct = "Nichrome has high resistance (so current generates intense thermal energy safely without melting or oxidising quickly), while copper has very low resistance to deliver current to the kettle without cord heating; A high-resistance supply cord would overheat, melt insulation, and ignite a house fire"
    sol = (
        "**Step 1:** **Nichrome** resists current strongly and resists oxidation at glowing temperatures, heating water rapidly; **copper** conducts cleanly with minimal heat loss [2].\n\n"
        "**Step 2:** A hot plug cord would melt PVC insulation causing shock or fire [1]."
    )
    return _q(
        rng, "14", "14_electric_kettle_and_geyser_nichrome_heating_element", prompt, correct, sol, 3, "structured",
        ["claiming_kettle_elements_are_made_of_copper_error"],
        "Match high-resistance alloy to heating element and low-resistance metal to supply cable.",
        "Nichrome heats water (high R); Copper delivers power safely (low R).",
        correct,
    )


def arch_15_incandescent_bulb_tungsten_filament_light_and_wasted_heat(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([2500, 2800, 3000])
    prompt = (
        f"Inside an older **incandescent filament bulb**, electric current heats a super-thin coiled **tungsten** filament to **~{temp} °C**, glowing white-hot inside an inert **argon** gas bulb.\n\n"
        "1. State why tungsten metal is chosen over copper for the filament [1].\n"
        "2. Why is the glass bulb filled with inert **argon** instead of ordinary oxygen air? [1]"
    )
    correct = f"Tungsten has a very high resistance (thin wire) and an extremely high melting point (~3420 °C) so it glows white-hot without melting; Argon prevents the white-hot filament from oxidising (burning away) rapidly in oxygen"
    sol = (
        f"**Step 1:** Fine **tungsten** provides high resistance plus the highest metal melting point (~3420 °C), surviving **{temp} °C** glowing heat [1].\n\n"
        "**Step 2:** Replacing air with unreactive **argon** prevents oxygen combustion of the hot filament [1]."
    )
    return _q(
        rng, "15", "15_incandescent_bulb_tungsten_filament_light_and_wasted_heat", prompt, correct, sol, 2, "short_answer",
        ["claiming_argon_in_bulbs_fuels_combustion_myth"],
        "Think melting point (~3420 °C) and inert gas blocking oxidation!",
        "Tungsten = high melting point & thin high-R coil; Argon = blocks oxygen burning.",
        correct,
    )


def arch_16_electric_toaster_glowing_high_resistance_elements(rng: random.Random) -> Dict[str, Any]:
    watt = rng.choice([700, 850, 1000])
    prompt = (
        f"When a **{watt} W electric toaster** switches on, internal nichrome ribbon wires glow bright orange-red within seconds.\n\n"
        "Explain why ONLY the thin nichrome toaster ribbons glow orange-red while the thicker copper wall cable stays cool to the touch, even though **exact same current** passes through both [2]."
    )
    correct = "The narrow nichrome element has much higher electrical resistance than the thick copper cord, so far more electrical energy per second converts to intense thermal radiation/heat inside the toaster element."
    sol = (
        "**Step 1:** Same current enters the copper cord and nichrome ribbons in series [1].\n\n"
        "**Step 2:** Because nichrome has **orders of magnitude higher resistance** than thick copper, intense collision heating happens right inside the element ribbons [1]."
    )
    return _q(
        rng, "16", "16_electric_toaster_glowing_high_resistance_elements", prompt, correct, sol, 2, "short_answer",
        ["thinking_more_current_enters_toaster_than_cord_myth"],
        "Remember current is identical in series — compare RESISTANCE of thick Cu wire vs thin nichrome ribbon!",
        "Higher R of thin nichrome concentrates heating inside the toaster coil.",
        correct,
    )


def arch_17_rheostat_definition_sliding_contact_variable_resistance(rng: random.Random) -> Dict[str, Any]:
    dir_move = rng.choice([("increases effective wire length in the circuit", "increases resistance and decreases current"), ("shortens the resistive path inside the rheostat", "decreases resistance and increases current")])
    move_desc, res = dir_move
    prompt = (
        "1. Define a **rheostat (variable resistor)** [1].\n"
        f"2. If sliding a rheostat wiper **{move_desc}**, predict what happens to BOTH total resistance and circuit current [2]."
    )
    correct = f"A variable resistor whose sliding contact alters the resistive path length to adjust resistance continuously; {res.capitalize()}"
    sol = (
        "**Step 1:** A **rheostat** is a variable resistor that changes circuit resistance continuously by moving a wiper along a resistive coil/track [1].\n\n"
        f"**Step 2:** Sliding to where it {move_desc} **{res}** [2]."
    )
    return _q(
        rng, "17", "17_rheostat_definition_sliding_contact_variable_resistance", prompt, correct, sol, 3, "structured",
        ["confusing_rheostat_with_open_switch"],
        "Longer resistive wire inside path = MORE resistance = LESS current.",
        f"Variable resistor; {res}.",
        correct,
    )


def arch_18_practical_rheostat_apps_dimmer_switches_and_radio_volume(rng: random.Random) -> Dict[str, Any]:
    apps = rng.choice([
        ("dimmer switch for lounge ceiling lights", "varying resistance lowers/raises bulb current smoothly to adjust room brightness"),
        ("rotary volume knob on an older hi-fi radio", "adjusts signal current flowing into loudspeaker coils smoothly"),
        ("speed controller dial on a fan or sewing machine pedal", "modulates motor current smoothly from slow to fast"),
    ])
    device, how = apps
    prompt = (
        f"Give the electrical explanation for how a variable resistor (rheostat) performs inside a **{device}** [2]."
    )
    correct = f"By {how}."
    sol = (
        f"**Step 1:** A variable resistor adjusts total resistance smoothly without opening the switch [1].\n\n"
        f"**Step 2:** In a {device}, **{how}** [1]."
    )
    return _q(
        rng, "18", "18_practical_rheostat_apps_dimmer_switches_and_radio_volume", prompt, correct, sol, 2, "short_answer",
        ["thinking_dimmer_switches_add_extra_batteries_myth"],
        "Variable resistors tune CURRENT smoothly without simply turning fully ON or OFF.",
        how.capitalize(),
        correct,
    )


def arch_19_graphite_pencil_lead_variable_resistor_practical(rng: random.Random) -> Dict[str, Any]:
    max_len = rng.choice([12, 14, 16])
    cur_len = rng.choice([3, 8, 10])
    spec = _svg_graphite_rheostat(rng, cur_len, max_len)
    prompt = (
        "Inspect the DIY graphite resistor setup made from a split pencil lead (HB graphite core) connected with movable crocodile clips.\n\n"
        "1. Does graphite (carbon non-metal) conduct electricity? [1]\n"
        f"2. If the learner slides the right-hand blue clip away from **{cur_len} cm** towards the full **{max_len} cm** mark, predict what happens to bulb brightness and justify [2]."
    )
    correct = f"Yes, graphite conducts electricity moderately despite being a non-metal (resistance device); Moving from {cur_len} cm to {max_len} cm increases resistor path length, raising total resistance, reducing current, and making the bulb dimmer"
    sol = (
        "**Step 1:** **Yes!** Pencil 'lead' is **graphite** (carbon with delocalised electrons between layers), acting as an electrical resistor [1].\n\n"
        f"**Step 2:** Increasing active graphite length from {cur_len} cm to {max_len} cm **increases resistance**, **reducing current** so the bulb glows **dimmer** [2]."
    )
    return _q(
        rng, "19", "19_graphite_pencil_lead_variable_resistor_practical", prompt, correct, sol, 3, "structured",
        ["thinking_graphite_pencil_core_is_lead_metal_or_insulator_myth"],
        "Remember: longer resistive graphite path = greater resistance = dimmer lamp.",
        "Graphite conducts (non-metal); longer path -> higher R -> dimmer bulb.",
        correct, diagram_spec=spec,
    )


def arch_20_diode_one_way_current_valve_definition_and_symbol(rng: random.Random) -> Dict[str, Any]:
    dir_txt = rng.choice(["forward-biased (arrow aligned with conventional current + -> -)", "reverse-biased (arrow pointing opposite to conventional current)"])
    is_fwd = "forward" in dir_txt
    prompt = (
        "A **diode** acts as a one-way electronic valve inside circuit boards.\n\n"
        f"Describe what happens to electric current when a diode is wired **{dir_txt}** [2]."
    )
    if is_fwd:
        correct = "Current flows freely in the direction of the diode's triangle symbol (conventional current + -> -)."
    else:
        correct = "Current is completely blocked (almost zero current flows) because the diode prevents reverse conduction."
    sol = (
        "**Step 1:** A diode is an asymmetric semiconductor component conducting charge in **one direction only** [1].\n\n"
        f"**Step 2:** When **{dir_txt}**, **{correct}** [1]."
    )
    return _q(
        rng, "20", "20_diode_one_way_current_valve_definition_and_symbol", prompt, correct, sol, 2, "short_answer",
        ["thinking_diodes_allow_bidirectional_current_like_resistors_myth"],
        "Compare a diode to a one-way turnstile or heart valve!",
        correct,
        correct,
    )


def arch_21_led_light_emitting_diode_forward_bias_polarity_and_apps(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["traffic lights", "cellphone indicator lights", "solar LED household lanterns"])
    prompt = (
        f"Modern South African cities rely on **LEDs (Light-Emitting Diodes)** for {app}.\n\n"
        "1. State what **LED** stands for [1].\n"
        "2. Suppose a learner wires an LED into a working battery circuit and it stays completely dark — reversing its two wire legs suddenly makes it glow! Explain why [2]."
    )
    correct = "Light-Emitting Diode; An LED is a diode that only conducts and emits light when connected with correct polarity (long positive anode leg towards +, short negative cathode leg towards -)."
    sol = (
        "**Step 1:** **LED** stands for **Light-Emitting Diode** [1].\n\n"
        "**Step 2:** Because an LED only passes current one way (forward bias), wiring it backwards blocked all current until its legs were swapped [2]."
    )
    return _q(
        rng, "21", "21_led_light_emitting_diode_forward_bias_polarity_and_apps", prompt, correct, sol, 3, "structured",
        ["assuming_leds_light_up_either_way_round_like_filament_bulbs"],
        "Does an incandescent filament bulb care about + / - leg polarity vs an LED?",
        "Light-Emitting Diode; LEDs require correct one-way polarity.",
        correct,
    )


def arch_22_led_vs_incandescent_bulb_efficiency_comparison(rng: random.Random) -> Dict[str, Any]:
    w_inc, w_led = rng.choice([(60, 8), (100, 12)])
    prompt = (
        f"An **{w_led} W LED lamp** produces the exact same room brightness (lumens) as an older **{w_inc} W incandescent filament bulb**.\n\n"
        "Explain why the LED bulb uses far fewer watts of electrical power to achieve identical light output [2]."
    )
    correct = "Incandescent bulbs waste ~90% of input electrical energy heating an incandescent tungsten wire, whereas LEDs convert a far higher proportion directly into visible light with minimal wasted heat."
    sol = (
        "**Step 1:** Filament bulbs rely on white-hot thermal glow (~2800 °C), wasting ~90% of energy as unwanted **heat** [1].\n\n"
        f"**Step 2:** **LEDs** emit light efficiently with very little thermal waste, achieving the same light using just **{w_led} W instead of {w_inc} W** [1]."
    )
    return _q(
        rng, "22", "22_led_vs_incandescent_bulb_efficiency_comparison", prompt, correct, sol, 2, "short_answer",
        ["thinking_brighter_wattage_always_means_more_light_not_heat"],
        "Remember: Eskom power saving replaces 60 W incandescent bulbs with ~8 W LEDs because of HEAT waste!",
        "LED wastes very little energy as heat; filament bulb wastes ~90% as heat.",
        correct,
    )


def arch_23_sankey_diagram_interpreting_useful_vs_wasted_energy_arrows(rng: random.Random) -> Dict[str, Any]:
    lamp, e_in, e_light = rng.choice([
        ("Incandescent Filament Bulb", 100, 10),
        ("Modern LED Bulb", 100, 80),
        ("Compact Fluorescent (CFL)", 100, 45),
        ("Incandescent Floodlight", 200, 20),
    ])
    e_heat = e_in - e_light
    spec = _svg_sankey_lamp(rng, e_in, e_light, lamp)
    prompt = (
        f"Study the **Sankey energy diagram** plotted for **{lamp}** receiving {e_in} J of electrical energy per second.\n\n"
        "1. State the exact numerical value of **wasted thermal (heat) energy** transferred per second [1].\n"
        "2. State what the **width** of each Sankey arrow represents and verify conservation of energy [2]."
    )
    correct = f"{e_heat} J/s wasted heat; Arrow width is directly proportional to the amount of energy transferred; {e_light} J + {e_heat} J = {e_in} J (energy conserved)"
    sol = (
        f"**Step 1:** Wasted heat = ${e_in} - {e_light} = \\mathbf{{{e_heat}\\text{{ J}}}}$ per second [1].\n\n"
        f"**Step 2:** In a Sankey diagram, **arrow thickness (width)** represents quantity of energy, and useful + wasted outputs sum identically to input (${e_light} + {e_heat} = {e_in}\\text{{ J}}$) [2]."
    )
    return _q(
        rng, "23", "23_sankey_diagram_interpreting_useful_vs_wasted_energy_arrows", prompt, correct, sol, 3, "structured",
        ["thinking_arrow_length_not_width_shows_sankey_energy"],
        "In a Sankey diagram, WIDTH represents energy magnitude, and all output widths sum back to input!",
        f"Wasted heat = {e_heat} J; width proportional to energy.",
        correct, diagram_spec=spec,
    )


def arch_24_calculating_percentage_efficiency_from_sankey_values(rng: random.Random) -> Dict[str, Any]:
    e_in, e_use, device = rng.choice([
        (200, 160, "high-efficiency LED fixture"),
        (250, 50, "old halogen spotlight"),
        (500, 425, "insulated electric kettle"),
    ])
    eff = int(round((e_use / float(e_in)) * 100))
    prompt = (
        f"An appliance (**{device}**) draws **{e_in} J** of electrical energy each second and delivers **{e_use} J** of useful output energy.\n\n"
        "Calculate its **percentage energy efficiency** ($\\eta = \\frac{\\text{Useful output}}{\\text{Total input}} \\times 100\\%$) [2]."
    )
    correct = f"{eff}%"
    sol = (
        "**Step 1:** $\\text{Efficiency} = \\frac{\\text{Useful Energy Out}}{\\text{Total Energy In}} \\times 100\\%$ [1].\n\n"
        f"**Step 2:** $\\text{{Efficiency}} = \\frac{{{e_use}}}{{{e_in}}} \\times 100\\% = \\mathbf{{{eff}\\%}}$ [1]."
    )
    return _q(
        rng, "24", "24_calculating_percentage_efficiency_from_sankey_values", prompt, correct, sol, 2, "short_answer",
        ["dividing_wasted_energy_by_input_and_calling_it_efficiency"],
        "Put USEFUL output on top, TOTAL input on the bottom, multiply by 100%.",
        f"({e_use} / {e_in}) x 100% = {eff}%.",
        correct,
    )


def arch_25_comparing_resistor_current_vs_lamp_filament_protection(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([6, 9])
    v_led = 2
    prompt = (
        f"An electronics learner hooks a tiny 2 V indicator LED straight across a fresh **{v_bat} V** battery with no resistor in the circuit, and the LED flashes once before burning out permanently.\n\n"
        f"Explain why electronics kits ALWAYS include a **current-limiting resistor** in series with an LED on a {v_bat} V supply [2]."
    )
    correct = f"Without a series resistor, resistance of the forward-biased LED is tiny, so {v_bat} V pushes excessive damaging current through it; adding a series resistor limits current to safe ~20 mA and drops excess voltage."
    sol = (
        "**Step 1:** Forward-biased LEDs have near-zero internal resistance once lit [1].\n\n"
        f"**Step 2:** A series resistor shares the **{v_bat} V** drop and restricts circuit current safely so the LED glows continuously without overheating [1]."
    )
    return _q(
        rng, "25", "25_comparing_resistor_current_vs_lamp_filament_protection", prompt, correct, sol, 2, "short_answer",
        ["wiring_bare_led_across_9v_battery_without_resistor"],
        "Remember: LEDs don't restrict current once conducting forward — you need a protective resistor!",
        "Series resistor restricts excessive current and protects the LED from burnout.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_resistance_definition_opposition_to_electron_flow": arch_01_resistance_definition_opposition_to_electron_flow,
    "02_school_corridor_and_doorway_analogy_for_resistance": arch_02_school_corridor_and_doorway_analogy_for_resistance,
    "03_metallic_lattice_and_delocalised_sea_of_electrons": arch_03_metallic_lattice_and_delocalised_sea_of_electrons,
    "04_electron_lattice_collisions_causing_thermal_heating": arch_04_electron_lattice_collisions_causing_thermal_heating,
    "05_si_unit_ohm_omega_symbol_and_georg_ohm": arch_05_si_unit_ohm_omega_symbol_and_georg_ohm,
    "06_electrical_conductors_vs_resistors_definition_and_roles": arch_06_electrical_conductors_vs_resistors_definition_and_roles,
    "07_circuit_symbols_fixed_resistor_vs_variable_rheostat": arch_07_circuit_symbols_fixed_resistor_vs_variable_rheostat,
    "08_resistor_colour_band_purpose_identifying_resistance_value": arch_08_resistor_colour_band_purpose_identifying_resistance_value,
    "09_voltage_current_resistance_qualitative_control_relationship": arch_09_voltage_current_resistance_qualitative_control_relationship,
    "10_current_is_not_consumed_inside_a_resistor": arch_10_current_is_not_consumed_inside_a_resistor,
    "11_ohms_law_calculating_resistance_r_equals_v_over_i": arch_11_ohms_law_calculating_resistance_r_equals_v_over_i,
    "12_calculating_current_or_voltage_using_ohms_law_rearrangement": arch_12_calculating_current_or_voltage_using_ohms_law_rearrangement,
    "13_useful_resistance_converting_electrical_to_heat_light": arch_13_useful_resistance_converting_electrical_to_heat_light,
    "14_electric_kettle_and_geyser_nichrome_heating_element": arch_14_electric_kettle_and_geyser_nichrome_heating_element,
    "15_incandescent_bulb_tungsten_filament_light_and_wasted_heat": arch_15_incandescent_bulb_tungsten_filament_light_and_wasted_heat,
    "16_electric_toaster_glowing_high_resistance_elements": arch_16_electric_toaster_glowing_high_resistance_elements,
    "17_rheostat_definition_sliding_contact_variable_resistance": arch_17_rheostat_definition_sliding_contact_variable_resistance,
    "18_practical_rheostat_apps_dimmer_switches_and_radio_volume": arch_18_practical_rheostat_apps_dimmer_switches_and_radio_volume,
    "19_graphite_pencil_lead_variable_resistor_practical": arch_19_graphite_pencil_lead_variable_resistor_practical,
    "20_diode_one_way_current_valve_definition_and_symbol": arch_20_diode_one_way_current_valve_definition_and_symbol,
    "21_led_light_emitting_diode_forward_bias_polarity_and_apps": arch_21_led_light_emitting_diode_forward_bias_polarity_and_apps,
    "22_led_vs_incandescent_bulb_efficiency_comparison": arch_22_led_vs_incandescent_bulb_efficiency_comparison,
    "23_sankey_diagram_interpreting_useful_vs_wasted_energy_arrows": arch_23_sankey_diagram_interpreting_useful_vs_wasted_energy_arrows,
    "24_calculating_percentage_efficiency_from_sankey_values": arch_24_calculating_percentage_efficiency_from_sankey_values,
    "25_comparing_resistor_current_vs_lamp_filament_protection": arch_25_comparing_resistor_current_vs_lamp_filament_protection,
}
