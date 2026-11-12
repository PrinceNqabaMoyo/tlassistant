"""Grade 9 Natural Sciences - Electric Cells as Energy Systems: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. Electric cells as energy systems.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


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
        "id": f"ns9_elc_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
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


def _svg_cell_vs_battery_symbols(rng: random.Random, n_cells: int, left_long: bool) -> Dict[str, Any]:
    """Parameterized circuit symbol diagram showing n_cells in series."""
    parts = []
    start_x = 120
    spacing = 36
    for i in range(n_cells):
        x1 = start_x + i * spacing
        x2 = x1 + 12
        long_x, short_x = (x1, x2) if left_long else (x2, x1)
        parts.append(
            f'<line x1="{long_x}" y1="64" x2="{long_x}" y2="128" stroke="#0f172a" stroke-width="3"/>'
            f'<line x1="{short_x}" y1="80" x2="{short_x}" y2="112" stroke="#0f172a" stroke-width="5"/>'
        )
        if i < n_cells - 1:
            parts.append(
                f'<line x1="{max(long_x, short_x)}" y1="96" x2="{start_x + (i + 1) * spacing}" y2="96" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2"/>'
            )
    end_wire_x = start_x + (n_cells - 1) * spacing + 12
    l_sign, r_sign = ("+", "-") if left_long else ("-", "+")
    svg = (
        f'<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="175" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="45" y1="96" x2="{start_x}" y2="96" stroke="#0f172a" stroke-width="2.5"/>'
        f'{"".join(parts)}'
        f'<line x1="{end_wire_x}" y1="96" x2="375" y2="96" stroke="#0f172a" stroke-width="2.5"/>'
        f'<text x="92" y="84" font-size="15" font-weight="bold" fill="#dc2626">{l_sign}</text>'
        f'<text x="{end_wire_x + 18}" y="84" font-size="15" font-weight="bold" fill="#2563eb">{r_sign}</text>'
        f'<text x="210" y="156" font-size="11" fill="#334155" text-anchor="middle">Circuit Symbol Component ({n_cells} unit/s)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_fruit_cell(rng: random.Random, fruit: str, electrode_a: str, electrode_b: str) -> Dict[str, Any]:
    """Parameterized citrus/potato fruit cell connected to an LED bulb."""
    tilt = rng.randint(-6, 6)
    fill_fruit = "#fde047" if "lemon" in fruit.lower() else ("#fdba74" if "orange" in fruit.lower() else "#d6d3d1")
    svg = (
        f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<ellipse cx="210" cy="{142 + tilt}" rx="78" ry="44" fill="{fill_fruit}" stroke="#854d0e" stroke-width="2"/>'
        f'<rect x="165" y="82" width="12" height="58" rx="2" fill="#94a3b8" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="243" y="82" width="12" height="58" rx="2" fill="#d97706" stroke="#78350f" stroke-width="1.5"/>'
        f'<path d="M 171 82 L 171 42 L 195 42" fill="none" stroke="#0f172a" stroke-width="2"/>'
        f'<path d="M 249 82 L 249 42 L 225 42" fill="none" stroke="#0f172a" stroke-width="2"/>'
        f'<circle cx="210" cy="42" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="210" y="46" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">LED</text>'
        f'<text x="128" y="96" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="end">{electrode_a}</text>'
        f'<text x="292" y="96" font-size="10.5" font-weight="bold" fill="#b45309" text-anchor="start">{electrode_b}</text>'
        f'<text x="210" y="204" font-size="11" fill="#0f172a" text-anchor="middle">{fruit} Electrochemical Cell</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_electric_cell_definition_chemical_energy_system(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["TV remote control", "LED pocket torch", "quartz wall clock", "scientific calculator"])
    prompt = (
        f"A **{app}** operates reliably using one or more electric cells without being plugged into the municipal wall mains.\n\n"
        "1. Define an **electric cell** as an energy system [2].\n"
        "2. State what triggers electric current flow when its terminals are joined in a closed circuit [1]."
    )
    correct = "An energy system in which chemical reactions take place internally to transfer stored chemical potential energy into electrical energy; The internal chemical reactions create a potential difference across the terminals pushing electrons through the external wire"
    sol = (
        "**Step 1:** An **electric cell** is an electrochemical system in which **chemical reactions** convert stored chemical energy directly into **electrical energy** [2].\n\n"
        "**Step 2:** These reactions build up a **potential difference** between the positive and negative terminals, driving electron flow around the closed circuit [1]."
    )
    return _q(
        rng, "01", "01_electric_cell_definition_chemical_energy_system", prompt, correct, sol, 3, "structured",
        ["thinking_cells_store_electricity_like_a_bucket_myth"],
        "Cells do NOT contain boxed electrons waiting like a bucket — internal chemical reactions push circuit electrons!",
        "System converting chemical energy -> electrical energy via chemical reactions.",
        correct,
    )


def arch_02_distinguishing_single_cell_vs_battery_of_cells(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([2, 3, 4])
    prompt = (
        f"A shop shelf sells individual **1,5 V AA cylindrical units**, while a learner places **{n}** of them end-to-end inside a portable radio.\n\n"
        "Clearly distinguish between an **electric cell** and a **battery** using this example [2]."
    )
    correct = f"One single 1,5 V AA unit is an electric cell; connecting {n} (two or more) cells together in a circuit forms a battery."
    sol = (
        "**Step 1:** In strict physics, a single self-contained AA unit (1,5 V) is one **electric cell**, NOT a battery [1].\n\n"
        f"**Step 2:** A **battery** consists of **two or more cells** connected together (so {n} linked AA cells form a battery) [1]."
    )
    return _q(
        rng, "02", "02_distinguishing_single_cell_vs_battery_of_cells", prompt, correct, sol, 2, "short_answer",
        ["calling_single_1_5v_aa_unit_a_battery_error"],
        "Think about the strict scientific terminology difference between 1 unit vs multiple connected units.",
        "Single unit = cell; 2+ connected units = battery.",
        correct,
    )


def arch_03_no_moving_parts_electrochemical_vs_generator_contrast(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["coal turbine generator at Medupi", "hydroelectric generator at Gariep Dam", "wind turbine dynamo"])
    prompt = (
        f"Compare electricity generation in a **{station}** against electricity production inside a small zinc–carbon torch cell.\n\n"
        "State how the energy generation mechanism inside a **cell** differs mechanically from a power-station generator [2]."
    )
    correct = "A generator relies on spinning turbines and moving coils/magnets (mechanical kinetic energy), whereas an electric cell has NO moving parts and generates electricity solely through chemical reactions."
    sol = (
        "**Step 1:** Power-station generators spin magnets past wire coils, needing **moving mechanical parts** (kinetic -> electrical) [1].\n\n"
        "**Step 2:** An **electric cell has zero moving parts** — silent **chemical reactions** inside electrolytes and electrodes drive electric current [1]."
    )
    return _q(
        rng, "03", "03_no_moving_parts_electrochemical_vs_generator_contrast", prompt, correct, sol, 2, "short_answer",
        ["thinking_batteries_have_mini_spinning_motors_myth"],
        "Recall whether a flashlight battery vibrates with spinning magnets inside.",
        "Generator = moving turbines/magnets; Cell = no moving parts (chemical reactions).",
        correct,
    )


def arch_04_circuit_symbol_cell_long_positive_short_negative_terminals(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([1, 2, 3, 4])
    left_long = rng.choice([True, False])
    spec = _svg_cell_vs_battery_symbols(rng, n_cells, left_long)
    kind = "a single electric cell" if n_cells == 1 else f"a battery of {n_cells} cells in series"
    pos_side = "left-hand long thin line (+)" if left_long else "right-hand long thin line (+)"
    neg_side = "right-hand short thick line (-)" if left_long else "left-hand short thick line (-)"
    prompt = (
        "Inspect the circuit diagram symbol component.\n\n"
        "1. State whether this symbol represents a **single electric cell** or a **battery** (and count how many cells are joined) [2].\n"
        "2. State the standard drawing convention for distinguishing the **positive (+)** terminal from the **negative (-)** terminal [2]."
    )
    correct = f"{kind} ({n_cells} cell/s); Long thin line = positive (+) terminal ({pos_side}), short thick line = negative (-) terminal ({neg_side})"
    sol = (
        f"**Step 1:** Counting long-short pairs gives **{n_cells} cell(s)** -> **{kind}** [2].\n\n"
        f"**Step 2:** Convention: **Long thin line = positive (+)** terminal; **short thick line = negative (-)** terminal [2]."
    )
    return _q(
        rng, "04", "04_circuit_symbol_cell_long_positive_short_negative_terminals", prompt, correct, sol, 4, "structured",
        ["reversing_long_and_short_battery_symbol_terminals"],
        "Count pairs of (1 long thin + 1 short thick) vertical bars. Longer line = Positive!",
        f"{n_cells} cell(s); Long thin = (+), Short thick = (-).",
        correct, diagram_spec=spec,
    )


def arch_05_energy_conversion_chemical_to_electrical_in_circuit(rng: random.Random) -> Dict[str, Any]:
    load = rng.choice([
        ("flashlight filament bulb", "light and thermal (heat) energy"),
        ("school electric buzzer", "sound (and slight thermal) energy"),
        ("toy car electric motor", "kinetic mechanical energy"),
    ])
    device, output = load
    prompt = (
        f"An electric cell powers a **{device}** when a switch is closed.\n\n"
        f"Trace the complete two-stage **energy conversion chain**: inside the cell first, then inside the {device} [2]."
    )
    correct = f"Chemical potential energy (cell) -> Electrical energy (in wires) -> {output} (in {device})"
    sol = (
        "**Step 1:** Inside cell: **Chemical potential energy $\\rightarrow$ Electrical energy** [1].\n\n"
        f"**Step 2:** Across external load ({device}): **Electrical energy $\\rightarrow$ {output}** [1]."
    )
    return _q(
        rng, "05", "05_energy_conversion_chemical_to_electrical_in_circuit", prompt, correct, sol, 2, "short_answer",
        ["omitting_chemical_energy_in_cell_chain_error"],
        "Start at energy stored inside cell chemicals, move through current, end at device output.",
        f"Chemical -> Electrical -> {output}.",
        correct,
    )


def arch_06_electron_flow_external_circuit_vs_conventional_current(rng: random.Random) -> Dict[str, Any]:
    q_mode = rng.choice(["electrons", "conventional"])
    if q_mode == "electrons":
        prompt = (
            "When a copper wire connects the negative (-) zinc terminal of a cell through a bulb back to the positive (+) terminal:\n\n"
            "In which direction do **free electrons** flow through the external copper connecting wire?"
        )
        correct = "From the negative (-) terminal around the external wire to the positive (+) terminal."
        distractors = [
            "From the positive (+) terminal around the wire to the negative (-) terminal.",
            "Electrons leave only the bulb filament and vanish inside the switch.",
            "Electrons stand still while energy teleports through empty air.",
        ]
    else:
        prompt = (
            "By international historical convention drawn on South African circuit diagrams, **conventional current** arrows are drawn pointing in which external direction around a closed loop?"
        )
        correct = "From the positive (+) terminal around the external circuit to the negative (-) terminal (opposite to electron motion)."
        distractors = [
            "From the negative (-) terminal directly to the positive (+) terminal.",
            "Only backwards inside the cell without entering wires.",
            "Randomly back and forth in a DC battery torch.",
        ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Negatively charged **electrons** are repelled out of the **(-)** terminal and attracted towards the **(+)** terminal externally.\n"
        "**Step 2:** **Conventional current** follows the older positive-charge convention from **(+)** externally to **(-)** [2]."
    )
    return _q(
        rng, "06", "06_electron_flow_external_circuit_vs_conventional_current", prompt, correct, sol, 2, "multiple_choice",
        ["reversing_electron_flow_vs_conventional_current"],
        "Electrons are negatively charged (repelled by negative -> positive); conventional current goes (+ -> -).",
        correct,
        correct, options=options,
    )


def arch_07_potential_difference_role_pushing_electrons_around_circuit(rng: random.Random) -> Dict[str, Any]:
    volt = rng.choice(["1,5 V", "3,0 V", "9,0 V"])
    prompt = (
        f"A voltmeter connected across the terminals of a cell reads **{volt}**.\n\n"
        "Explain what **potential difference (voltage)** means in terms of electrical energy and charges moving around a circuit, and name its SI unit [2]."
    )
    correct = f"Potential difference is the electrical energy transferred per unit charge (push driving electrons around the circuit); measured in volts (V), here {volt}."
    sol = (
        "**Step 1:** **Potential difference (voltage)** measures the work/energy supplied by the cell per unit charge to push electrons around the circuit [1].\n\n"
        f"**Step 2:** SI unit is the **volt (V)**; a **{volt}** cell supplies more energy per charge than a lower-voltage cell [1]."
    )
    return _q(
        rng, "07", "07_potential_difference_role_pushing_electrons_around_circuit", prompt, correct, sol, 2, "short_answer",
        ["confusing_voltage_and_current_definitions"],
        "Think of potential difference as electrical 'push' or energy per unit charge.",
        "Energy transferred per unit charge; measured in volts (V).",
        correct,
    )


def arch_08_closed_vs_open_switch_effect_on_cell_current(rng: random.Random) -> Dict[str, Any]:
    bulb_state = rng.choice([("switch is open", "0 A; Bulb is off — chemical reactions pause because no closed loop exists for electron transfer"), ("switch is closed", "steady current flows; Bulb lights up because a continuous closed loop permits continuous electron flow")])
    cond, outcome = bulb_state
    prompt = (
        f"An electric cell is wired in a simple circuit containing a switch and a torch bulb. Suppose the **{cond}**.\n\n"
        "State what happens to the ammeter current reading and to the chemical reaction inside the cell [2]."
    )
    correct = outcome
    sol = (
        "**Step 1:** Electric charges require an unbroken closed conducting pathway [1].\n\n"
        f"**Step 2:** When the {cond}, **{outcome}** [1]."
    )
    return _q(
        rng, "08", "08_closed_vs_open_switch_effect_on_cell_current", prompt, correct, sol, 2, "short_answer",
        ["thinking_cell_drains_at_full_speed_with_open_switch_myth"],
        "An open switch breaks the loop — electrons cannot accumulate indefinitely inside cut wire ends!",
        outcome,
        correct,
    )


def arch_09_short_circuit_hazard_overheating_across_cell_terminals(rng: random.Random) -> Dict[str, Any]:
    wire_type = rng.choice(["bare copper wire", "tin foil strip"])
    prompt = (
        f"A learner accidentally connects the **(+) and (-) terminals** of a fresh 1,5 V D-cell directly together using a short piece of **{wire_type}** with no bulb or resistor in between.\n\n"
        "1. What electrical fault has occurred? [1]\n"
        "2. Explain why both the cell and the wire become dangerously hot and the cell goes flat rapidly [2]."
    )
    correct = "A short circuit; Because resistance is nearly zero, a massive electric current surges through the loop, rapidly draining chemical energy into dangerous thermal energy (overheating/fire risk)"
    sol = (
        "**Step 1:** Connecting terminals directly with a low-resistance conductor creates a **short circuit** [1].\n\n"
        "**Step 2:** With almost zero external resistance, a **huge current flows**, heating the wire and cell dangerously fast while exhausting chemicals within minutes [2]."
    )
    return _q(
        rng, "09", "09_short_circuit_hazard_overheating_across_cell_terminals", prompt, correct, sol, 3, "structured",
        ["short_circuit_reduces_current_to_zero_myth"],
        "Remember low resistance + direct connection = HUGE surging current and heat!",
        "Short circuit -> nearly zero R -> massive current -> overheating and rapid depletion.",
        correct,
    )


def arch_10_dead_flat_cell_chemical_reactant_depletion_concept(rng: random.Random) -> Dict[str, Any]:
    months = rng.choice([4, 6, 8])
    prompt = (
        f"After {months} months of regular torch use, a non-rechargeable zinc–carbon cell goes **'flat' (dead)** and can no longer light the bulb.\n\n"
        "Which microscopic statement explains why a flat cell stops supplying electricity?"
    )
    correct = "The limiting chemical reactants inside the cell have been completely used up into products, so chemical reactions stop maintaining a potential difference."
    distractors = [
        "All copper wires inside the torch have run out of electrons.",
        "Every proton inside the zinc case dissolved into air.",
        "Gravity pulled all electric current out through the plastic bottom.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Wires ALWAYS still contain copper atoms and electrons.\n"
        "**Step 2:** A cell runs flat strictly because its **stored chemical reactants are exhausted**, ending potential difference generation [2]."
    )
    return _q(
        rng, "10", "10_dead_flat_cell_chemical_reactant_depletion_concept", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_wires_run_out_of_electrons_myth"],
        "Does a dead battery mean electrons disappeared from wires, or did cell chemistry finish?",
        "Chemical reactants inside the cell are depleted.",
        correct, options=options,
    )


def arch_11_internal_resistance_warmth_inside_hardworking_cell(rng: random.Random) -> Dict[str, Any]:
    device = rng.choice(["high-power RC motor", "portable bright spotlight", "handheld battery drill"])
    prompt = (
        f"When a battery pack runs a **{device}** continuously for 20 minutes, learners notice the battery casing itself feels slightly warm.\n\n"
        "Explain why a small fraction of chemical energy turns into heat inside the cell itself [2]."
    )
    correct = "Real electrolytes and electrodes inside a cell offer slight internal resistance to ion and electron motion, dissipating some energy as thermal energy (heat)."
    sol = (
        "**Step 1:** Nothing inside real chemical pastes or solutions has zero resistance [1].\n\n"
        "**Step 2:** Passing heavy current encounters **internal resistance** inside the electrolyte and electrodes, converting part of the chemical energy into wasted **heat** [1]."
    )
    return _q(
        rng, "11", "11_internal_resistance_warmth_inside_hardworking_cell", prompt, correct, sol, 2, "short_answer",
        ["ideal_zero_internal_resistance_cell_myth"],
        "Think about friction/collisions charges encounter moving inside cell liquids and plates.",
        "Internal resistance converts a portion of electrical energy into warmth.",
        correct,
    )


def arch_12_everyday_devices_using_cells_remote_torch_watch_car(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice([
        ("digital wristwatch", "Tiny lithium/silver-oxide button cell (~1,5–3 V)", "compact size and very low current draw for years"),
        ("starting engine of a petrol car", "12 V lead-acid battery (6 rechargeable cells in series)", "delivers massive brief cranking current and recharges while driving"),
        ("household solar garden lantern", "Rechargeable AA NiMH / LiFePO4 battery", "stores solar panel electricity by day for night lighting"),
    ])
    app, cell_t, reason = item
    prompt = (
        f"Match a **{app}** to a suitable cell/battery type (**{cell_t}**) and justify one practical design advantage [2]."
    )
    correct = f"{cell_t}; Chosen because of {reason}"
    sol = (
        f"**Step 1:** Appropriate power source: **{cell_t}** [1].\n\n"
        f"**Step 2:** Key engineering fit: **{reason}** [1]."
    )
    return _q(
        rng, "12", "12_everyday_devices_using_cells_remote_torch_watch_car", prompt, correct, sol, 2, "short_answer",
        ["using_car_battery_inside_watch_mismatch"],
        "Match voltage, physical size, current surge need, and rechargeability to the appliance.",
        f"{cell_t}: {reason}.",
        correct,
    )


def arch_13_electrode_definition_positive_cathode_vs_negative_anode(rng: random.Random) -> Dict[str, Any]:
    metal_pair = rng.choice([("zinc strip and copper plate", "Zinc is negative (-) and Copper is positive (+)"), ("magnesium strip and copper coin", "Magnesium is negative (-) and Copper is positive (+)")])
    pair_txt, pol = metal_pair
    prompt = (
        f"In an electrochemical experiment, **{pair_txt}** dip side-by-side into dilute sulfuric acid without touching.\n\n"
        "1. Define the term **electrode** [1].\n"
        f"2. Identify the terminal polarity expected between these two electrodes ({pair_txt}) [1]."
    )
    correct = f"A solid electrical conductor (metal plate/rod or carbon rod) inserted into an electrolyte where charge-transfer reactions take place; {pol}"
    sol = (
        "**Step 1:** An **electrode** is an electrical conductor dipping into an electrolyte through which electrons enter or leave the external circuit [1].\n\n"
        f"**Step 2:** Polarity: **{pol}** (the more reactive metal gives up electrons easier -> negative terminal) [1]."
    )
    return _q(
        rng, "13", "13_electrode_definition_positive_cathode_vs_negative_anode", prompt, correct, sol, 2, "short_answer",
        ["confusing_electrode_with_electrolyte_definition"],
        "Electrodes are solid conductors dipping into the conducting liquid (electrolyte).",
        f"Solid conductor in electrolyte; {pol}.",
        correct,
    )


def arch_14_electrolyte_definition_ionic_conducting_liquid_or_paste(rng: random.Random) -> Dict[str, Any]:
    cand = rng.choice([
        ("distilled sugar water vs salty lemon juice", "Salty lemon juice", "contains dissolved free mobile ions (H+ / Na+ / Cl- / citrate) whereas sugar dissolves as neutral uncharged molecules"),
        ("solid dry NaCl table salt crystals vs aqueous copper sulfate solution", "Aqueous copper sulfate solution", "free mobile Cu2+ and SO4(2-) ions move freely in water, whereas ions in dry solid crystal are locked in place"),
    ])
    pair, winner, exp = cand
    prompt = (
        "1. Define an **electrolyte** in an electric cell [1].\n"
        f"2. Comparing **{pair}**, state which serves as an effective electrolyte and explain why [2]."
    )
    correct = f"A liquid solution or moist ionic paste containing free moving ions that conducts electric current chemically; {winner} ({exp})"
    sol = (
        "**Step 1:** An **electrolyte** is an ionic liquid/solution or paste that conducts electricity via **mobile ions** [1].\n\n"
        f"**Step 2:** **{winner}** acts as an electrolyte because it **{exp}** [2]."
    )
    return _q(
        rng, "14", "14_electrolyte_definition_ionic_conducting_liquid_or_paste", prompt, correct, sol, 3, "structured",
        ["claiming_sugar_water_conducts_as_strong_electrolyte_myth"],
        "Electricity inside a liquid requires FREE MOBILE IONS — not neutral molecules like sugar or locked solid crystal grains.",
        f"{winner}: {exp}.",
        correct,
    )


def arch_15_requirement_for_two_dissimilar_metal_electrodes(rng: random.Random) -> Dict[str, Any]:
    same_metal = rng.choice(["two identical copper strips", "two identical shiny steel nails", "two identical zinc strips"])
    prompt = (
        f"A learner builds a lemon cell using **{same_metal}** connected to a sensitive voltmeter and gets **$0{{,}}00\\text{{ V}}$**!\n\n"
        "Explain why **two DIFFERENT metals** are essential to generate a potential difference in an electrochemical cell [2]."
    )
    correct = "Identical metals have equal reactivity/tendency to lose electrons, so both electrodes pull equally with zero net potential difference; two dissimilar metals create an electron-transfer imbalance (voltage)."
    sol = (
        "**Step 1:** Voltage arises from the **difference in chemical reactivity** (electron-losing tendency) between the two electrodes [1].\n\n"
        f"**Step 2:** With **{same_metal}**, identical reactions oppose equally -> **$0{{,}}00\\text{{ V}}$**; pairing two **different metals** (like Zn and Cu) generates a potential difference [1]."
    )
    return _q(
        rng, "15", "15_requirement_for_two_dissimilar_metal_electrodes", prompt, correct, sol, 2, "short_answer",
        ["thinking_any_two_identical_nails_power_fruit_cell_error"],
        "Like a tug-of-war between identical twins — no difference = zero push!",
        "Identical metals give 0 V; need two dissimilar metals with different reactivities.",
        correct,
    )


def arch_16_fruit_cell_lemon_juicing_without_tearing_peel(rng: random.Random) -> Dict[str, Any]:
    fruit = rng.choice(["a firm fresh lemon", "a firm naartjie"])
    prompt = (
        f"Step 1 of the textbook *Fruit Cell* practical directs learners to **gently roll and squeeze {fruit}** firmly on the desk **without bursting its outer skin** before inserting copper and zinc nails.\n\n"
        "Explain the scientific purpose of softening the inside of the fruit while keeping the peel unbroken [2]."
    )
    correct = "Rolling ruptures tiny internal juice sacs releasing liquid citric-acid electrolyte freely around the nails for ion flow, while keeping the peel intact prevents messy leakage and maintains electrolyte contact."
    sol = (
        "**Step 1:** Rolling breaks open small **juice pulp membranes** so acidic juice flows freely around both metal nails (**better electrolyte contact / lower resistance**) [1].\n\n"
        "**Step 2:** Keeping the **skin intact** holds the liquid electrolyte inside the cell without leaking onto the bench [1]."
    )
    return _q(
        rng, "16", "16_fruit_cell_lemon_juicing_without_tearing_peel", prompt, correct, sol, 2, "short_answer",
        ["thinking_lemon_peel_generates_electricity_myth"],
        "Remember: liquid juice = electrolyte! What holds the juice inside?",
        "Breaks internal juice sacs for free electrolyte ion flow while keeping peel sealed.",
        correct,
    )


def arch_17_lemon_vs_potato_fruit_electrolyte_composition(rng: random.Random) -> Dict[str, Any]:
    fruit_choice = rng.choice([("lemon juice", "citric acid"), ("raw potato moisture", "mildly acidic/ionic vegetable sap (phosphoric/mineral salts)")])
    f_src, chem = fruit_choice
    prompt = (
        "Both lemons and raw potatoes can build working simple fruit cells with zinc and copper electrodes — even though a potato does NOT taste strongly sour like a lemon.\n\n"
        f"Identify which chemical role **{f_src}** plays in the cell ({chem}) [2]."
    )
    correct = f"Both act as the liquid/moist electrolyte containing free dissolved ions ({chem}) permitting ionic charge transport between the electrodes."
    sol = (
        f"**Step 1:** Inside the cell, **{f_src}** ({chem}) contains dissolved charged **ions** [1].\n\n"
        "**Step 2:** Therefore, it performs the role of the **electrolyte** (electrical energy still comes from Zn + Cu metal reactions, NOT from fruit nutrition) [1]."
    )
    return _q(
        rng, "17", "17_lemon_vs_potato_fruit_electrolyte_composition", prompt, correct, sol, 2, "short_answer",
        ["thinking_fruit_food_energy_is_electricity_source_myth"],
        "Does electricity come from food calories in the potato, or from dissolved ions + two metals?",
        f"{f_src} supplies mobile ions -> serves as the electrolyte.",
        correct,
    )


def arch_18_preventing_electrodes_touching_inside_fruit_short_circuit(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice(["2 mm", "pushed right until tips touch inside"])
    prompt = (
        f"Step 3 of the fruit cell practical warns: *\"Push the zinc nail and copper coin deeply towards the centre of the lemon, **but make sure their tips do NOT touch inside ({dist})**.\"*\n\n"
        "State what happens to the **LED bulb brightness / voltmeter reading** if the zinc and copper touch inside the lemon, and name the fault [2]."
    )
    correct = "An internal short circuit occurs: electrons bypass the external LED/wire loop straight from zinc to copper inside the lemon, dropping external reading to 0 (LED goes out)."
    sol = (
        "**Step 1:** Metal-to-metal contact inside the lemon causes an **internal short circuit** [1].\n\n"
        "**Step 2:** Electrons travel directly at the touching interface instead of through the external wire loop, so the **LED goes out** (external current/voltage -> 0) [1]."
    )
    return _q(
        rng, "18", "18_preventing_electrodes_touching_inside_fruit_short_circuit", prompt, correct, sol, 2, "short_answer",
        ["thinking_touching_electrodes_doubles_lemon_voltage_myth"],
        "Electrons always take the lowest-resistance shortcut if metals touch inside!",
        "Internal short circuit -> electrons skip the LED loop -> LED stays off.",
        correct,
    )


def arch_19_fruit_cell_led_bulb_polarity_and_minimum_threshold_voltage(rng: random.Random) -> Dict[str, Any]:
    fruit = rng.choice(["Lemon", "Orange", "Potato"])
    elec_a, elec_b = rng.choice([("Zinc nail (-)", "Copper coin (+)"), ("Galvanised iron (-)", "Copper strip (+)")])
    spec = _svg_fruit_cell(rng, fruit, elec_a, elec_b)
    v_one = rng.choice([0.8, 0.9])
    v_led = 2.0
    n_needed = 3
    prompt = (
        f"Examine the {fruit.lower()} fruit cell connected to an LED bulb. A single **{fruit.lower()}–{elec_a.split()[0]}–Copper** cell produces **${_fmt_num(v_one)}\\text{{ V}}$**, whereas a standard red LED needs at least **${_fmt_num(v_led)}\\text{{ V}}$** to light visibly.\n\n"
        "1. Explain why one fruit cell fails to glow the LED even when wired properly [1].\n"
        f"2. Calculate the **minimum number of identical fruit cells connected in series** needed to glow the LED brightly [2]."
    )
    correct = f"One cell produces only {_fmt_num(v_one)} V which is below the {_fmt_num(v_led)} V threshold of the LED; Minimum {n_needed} fruit cells in series ({_fmt_num(3 * v_one)} V > 2,0 V)"
    sol = (
        f"**Step 1:** ${v_one:.1f}\\text{{ V}} < 2{{,}}0\\text{{ V}}$ threshold, so voltage is insufficient [1].\n\n"
        f"**Step 2:** Two cells give $2 \\times {_fmt_num(v_one)} = {_fmt_num(2 * v_one)}\\text{{ V}}$ (still below 2,0 V); **{n_needed} cells in series** yield **${_fmt_num(3 * v_one)}\\text{{ V}}$**, lighting the LED [2]."
    )
    return _q(
        rng, "19", "19_fruit_cell_led_bulb_polarity_and_minimum_threshold_voltage", prompt, correct, sol, 3, "structured",
        ["claiming_1_lemon_always_powers_household_bulb_error"],
        "Add single-cell voltages together in series until total >= 2,0 V!",
        f"{_fmt_num(v_one)} V x 3 = {_fmt_num(3 * v_one)} V >= 2,0 V -> need 3 cells.",
        correct, diagram_spec=spec,
    )


def arch_20_fruit_cell_ammeter_current_vs_voltmeter_potential_difference(rng: random.Random) -> Dict[str, Any]:
    tool = rng.choice(["ammeter (A)", "voltmeter (V)"])
    is_amm = "ammeter" in tool
    prompt = (
        f"A learner connects a **{tool}** to test a pair of series lemon cells.\n\n"
        "1. State the exact **physical quantity** measured by this meter (and its unit) [2].\n"
        f"2. State whether the {tool.split()[0]} is wired in **series** or in **parallel** across the cell terminals [1]."
    )
    if is_amm:
        correct = "Electric current (rate of charge/electron flow) in amperes (A / mA); Connected in series in the circuit loop"
    else:
        correct = "Potential difference (voltage) in volts (V); Connected in parallel directly across the (+) and (-) cell terminals"
    sol = (
        f"**Step 1:** Measures **{'electric current in amperes (A)' if is_amm else 'potential difference in volts (V)'}** [2].\n\n"
        f"**Step 2:** Connection topology: **{'in series' if is_amm else 'in parallel'}** [1]."
    )
    return _q(
        rng, "20", "20_fruit_cell_ammeter_current_vs_voltmeter_potential_difference", prompt, correct, sol, 3, "structured",
        ["wiring_ammeter_in_parallel_across_cell_error"],
        "Ammeter = flow rate (A, series); Voltmeter = push across two points (V, parallel).",
        correct,
        correct,
    )


def arch_21_alessandro_volta_1800_voltaic_pile_historical_cell(rng: random.Random) -> Dict[str, Any]:
    year = 1800
    stack = rng.choice(["zinc and copper discs separated by salty brine-soaked cardboard", "stacked zinc–copper discs with saltwater cloth"])
    prompt = (
        f"In **{year}**, the Italian physicist **Alessandro Volta** invented the **voltaic pile** — the world's first continuous electrical battery — using **{stack}**.\n\n"
        "1. Which SI electrical unit is named in honour of Alessandro Volta? [1]\n"
        "2. Explain what functional role the salty brine cloth performed inside his stacked pile [1]."
    )
    correct = "The volt (V) — unit of potential difference; The salty cloth served as the conducting electrolyte separating dissimilar metal discs"
    sol = (
        "**Step 1:** The **volt (V)** honours Alessandro Volta [1].\n\n"
        "**Step 2:** Saltwater provides mobile $Na^+$ and $Cl^-$ ions, functioning as the **electrolyte** between zinc and copper electrodes [1]."
    )
    return _q(
        rng, "21", "21_alessandro_volta_1800_voltaic_pile_historical_cell", prompt, correct, sol, 2, "short_answer",
        ["mixing_volta_with_ampere_or_watt_units"],
        "Notice 'Volta' -> 'volt', and brine cloth = conducting ionic medium.",
        "Volt (V); saltwater soaked cloth = electrolyte.",
        correct,
    )


def arch_22_why_identical_zinc_zinc_fruit_nails_give_zero_voltage(rng: random.Random) -> Dict[str, Any]:
    fruit = rng.choice(["lemon", "grapefruit", "potato"])
    prompt = (
        f"While assembling a **{fruit} cell**, a learner mistakenly pushes **two galvanised (zinc-coated) steel nails** into the fruit instead of one zinc nail and one copper coin.\n\n"
        "Predict the voltmeter reading across the two identical nails and explain your prediction [2]."
    )
    correct = "0,00 V; Both electrodes are coated in the exact same zinc metal, so neither has a stronger chemical tendency to push electrons toward the other."
    sol = (
        "**Step 1:** Voltmeter reads **$0{,}00\\text{{ V}}$** [1].\n\n"
        "**Step 2:** Equal half-cell chemical tendencies on two identical zinc nails cancel out completely -> zero net potential difference [1]."
    )
    return _q(
        rng, "22", "22_why_identical_zinc_zinc_fruit_nails_give_zero_voltage", prompt, correct, sol, 2, "short_answer",
        ["expecting_galvanised_nails_pair_to_generate_voltage_myth"],
        "Check if the two nail surfaces touching the juice are DIFFERENT metals or IDENTICAL zinc!",
        "0,00 V because both metals are zinc (identical chemical reactivity).",
        correct,
    )


def arch_23_varying_metal_pairs_mg_cu_vs_zn_cu_vs_fe_cu_voltage(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("Magnesium – Copper", "1,6 V", "Zinc – Copper (0,9 V) and Iron – Copper (0,4 V)", "largest difference in chemical reactivity between electrodes"),
        ("Magnesium – Zinc", "0,7 V", "Magnesium – Copper (1,6 V)", "copper and magnesium sit farther apart in reactivity than magnesium and zinc"),
    ])
    pair_a, v_a, comp, reason = case
    prompt = (
        "In a lemon electrolyte investigation, three electrode pairs record these open-circuit voltages:\n"
        "- Magnesium & Copper: $1{,}6\\text{ V}$\n"
        "- Zinc & Copper: $0{,}9\\text{ V}$\n"
        "- Iron & Copper: $0{,}4\\text{ V}$\n\n"
        f"Explain why **Magnesium–Copper** generates the highest voltage among all three pairs compared ({pair_a} = {v_a} vs {comp}) [2]."
    )
    correct = f"The wider the separation in chemical reactivity between the two metals, the higher the voltage produced ({reason})."
    sol = (
        "**Step 1:** Electrode potential difference depends on how strongly the two metals differ in reactivity (electron-donating strength) [1].\n\n"
        f"**Step 2:** Because **{reason}**, Magnesium–Copper achieves the largest voltage ($1{{,}}6\\text{{ V}}$) [1]."
    )
    return _q(
        rng, "23", "23_varying_metal_pairs_mg_cu_vs_zn_cu_vs_fe_cu_voltage", prompt, correct, sol, 2, "short_answer",
        ["thinking_larger_coin_size_changes_chemical_voltage_myth"],
        "Compare the positions of Mg, Zn, Fe, and Cu along the metal reactivity series!",
        "Greater reactivity gap between the two electrode metals -> higher cell voltage.",
        correct,
    )


def arch_24_increasing_fruit_cell_depth_or_surface_contact_area(rng: random.Random) -> Dict[str, Any]:
    change = rng.choice(["pushing the wide flat zinc and copper plates deeper into lemon pulp", "using thicker copper plates with larger submerged area"])
    prompt = (
        f"Compare two otherwise identical lemon–zinc–copper cells: Cell A has nails pushed only **3 mm** deep, whereas Cell B tries **{change}** (without touching).\n\n"
        "Explain why **Cell B delivers higher electric current (mA)** through an LED even though open-circuit voltage remains roughly the same [2]."
    )
    correct = "Greater submerged metal contact area lets faster chemical ion/electron reactions occur per second and lowers internal resistance, permitting larger electric current."
    sol = (
        "**Step 1:** Open-circuit voltage depends on electrode *identity* (still Zn vs Cu), so voltage stays around ~0,9 V [1].\n\n"
        "**Step 2:** **Larger wet contact surface area** increases chemical reaction rate per second and cuts internal resistance, boosting **electric current** [1]."
    )
    return _q(
        rng, "24", "24_increasing_fruit_cell_depth_or_surface_contact_area", prompt, correct, sol, 2, "short_answer",
        ["confusing_surface_area_current_boost_with_voltage_identity"],
        "Surface area speeds up reaction rate (more current!) while metal choice sets voltage!",
        "Larger submerged area -> lower internal resistance -> higher current (mA).",
        correct,
    )


def arch_25_fruit_cell_variables_controlled_vs_independent_design(rng: random.Random) -> Dict[str, Any]:
    test_type = rng.choice([
        ("testing lemon vs orange vs potato electrolytes using the same clean Zn and Cu electrodes at 3 cm spacing", "Fruit / electrolyte type", "Cell voltage / current", "Electrode metals (Zn & Cu), spacing (3 cm), submerged depth, temperature"),
        ("testing Mg, Zn, Fe, and Pb strips each paired against Copper inside identical lemons", "Metal electrode paired with copper", "Potential difference (V)", "Electrolyte (same lemon juice), copper electrode, distance between strips"),
    ])
    desc, ind, dep, ctrl = test_type
    prompt = (
        f"A Grade 9 learner designs a fair scientific test by **{desc}**.\n\n"
        "Identify:\n"
        "1. Independent variable [1]\n"
        "2. Dependent variable [1]\n"
        "3. **Two** controlled variables [2]"
    )
    correct = f"Independent: {ind}; Dependent: {dep}; Controlled: {ctrl}"
    sol = (
        f"**Step 1:** **Independent variable:** {ind} (deliberately varied) [1].\n\n"
        f"**Step 2:** **Dependent variable:** {dep} (measured outcome) [1].\n\n"
        f"**Step 3:** **Controlled variables:** {ctrl} [2]."
    )
    return _q(
        rng, "25", "25_fruit_cell_variables_controlled_vs_independent_design", prompt, correct, sol, 4, "structured",
        ["swapping_independent_and_dependent_cell_variables"],
        "What did the investigator change on purpose between trials vs what did the meter read?",
        f"Ind: {ind}; Dep: {dep}; Ctrl: {ctrl}.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_electric_cell_definition_chemical_energy_system": arch_01_electric_cell_definition_chemical_energy_system,
    "02_distinguishing_single_cell_vs_battery_of_cells": arch_02_distinguishing_single_cell_vs_battery_of_cells,
    "03_no_moving_parts_electrochemical_vs_generator_contrast": arch_03_no_moving_parts_electrochemical_vs_generator_contrast,
    "04_circuit_symbol_cell_long_positive_short_negative_terminals": arch_04_circuit_symbol_cell_long_positive_short_negative_terminals,
    "05_energy_conversion_chemical_to_electrical_in_circuit": arch_05_energy_conversion_chemical_to_electrical_in_circuit,
    "06_electron_flow_external_circuit_vs_conventional_current": arch_06_electron_flow_external_circuit_vs_conventional_current,
    "07_potential_difference_role_pushing_electrons_around_circuit": arch_07_potential_difference_role_pushing_electrons_around_circuit,
    "08_closed_vs_open_switch_effect_on_cell_current": arch_08_closed_vs_open_switch_effect_on_cell_current,
    "09_short_circuit_hazard_overheating_across_cell_terminals": arch_09_short_circuit_hazard_overheating_across_cell_terminals,
    "10_dead_flat_cell_chemical_reactant_depletion_concept": arch_10_dead_flat_cell_chemical_reactant_depletion_concept,
    "11_internal_resistance_warmth_inside_hardworking_cell": arch_11_internal_resistance_warmth_inside_hardworking_cell,
    "12_everyday_devices_using_cells_remote_torch_watch_car": arch_12_everyday_devices_using_cells_remote_torch_watch_car,
    "13_electrode_definition_positive_cathode_vs_negative_anode": arch_13_electrode_definition_positive_cathode_vs_negative_anode,
    "14_electrolyte_definition_ionic_conducting_liquid_or_paste": arch_14_electrolyte_definition_ionic_conducting_liquid_or_paste,
    "15_requirement_for_two_dissimilar_metal_electrodes": arch_15_requirement_for_two_dissimilar_metal_electrodes,
    "16_fruit_cell_lemon_juicing_without_tearing_peel": arch_16_fruit_cell_lemon_juicing_without_tearing_peel,
    "17_lemon_vs_potato_fruit_electrolyte_composition": arch_17_lemon_vs_potato_fruit_electrolyte_composition,
    "18_preventing_electrodes_touching_inside_fruit_short_circuit": arch_18_preventing_electrodes_touching_inside_fruit_short_circuit,
    "19_fruit_cell_led_bulb_polarity_and_minimum_threshold_voltage": arch_19_fruit_cell_led_bulb_polarity_and_minimum_threshold_voltage,
    "20_fruit_cell_ammeter_current_vs_voltmeter_potential_difference": arch_20_fruit_cell_ammeter_current_vs_voltmeter_potential_difference,
    "21_alessandro_volta_1800_voltaic_pile_historical_cell": arch_21_alessandro_volta_1800_voltaic_pile_historical_cell,
    "22_why_identical_zinc_zinc_fruit_nails_give_zero_voltage": arch_22_why_identical_zinc_zinc_fruit_nails_give_zero_voltage,
    "23_varying_metal_pairs_mg_cu_vs_zn_cu_vs_fe_cu_voltage": arch_23_varying_metal_pairs_mg_cu_vs_zn_cu_vs_fe_cu_voltage,
    "24_increasing_fruit_cell_depth_or_surface_contact_area": arch_24_increasing_fruit_cell_depth_or_surface_contact_area,
    "25_fruit_cell_variables_controlled_vs_independent_design": arch_25_fruit_cell_variables_controlled_vs_independent_design,
}
