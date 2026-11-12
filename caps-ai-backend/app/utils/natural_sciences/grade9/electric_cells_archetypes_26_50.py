"""Grade 9 Natural Sciences - Electric Cells as Energy Systems: Archetypes 26 to 50.
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


def _svg_zn_cu_salt_bridge_cell(rng: random.Random, meter_lbl: str, reading_txt: str) -> Dict[str, Any]:
    """Parameterized two-beaker Zn/Cu electrochemical cell with U-tube salt bridge and external meter."""
    shift = rng.randint(-5, 5)
    svg = (
        f'<svg viewBox="0 0 430 230" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="230" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="45" y="105" width="110" height="90" rx="5" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="48" y="135" width="104" height="57" fill="#e2e8f0" opacity="0.8"/>'
        f'<rect x="275" y="105" width="110" height="90" rx="5" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="278" y="135" width="104" height="57" fill="#93c5fd" opacity="0.8"/>'
        f'<rect x="75" y="88" width="14" height="90" fill="#64748b" stroke="#0f172a" stroke-width="1.5"/>'
        f'<rect x="341" y="88" width="14" height="90" fill="#d97706" stroke="#78350f" stroke-width="1.5"/>'
        f'<path d="M 128 158 L 128 {78 + shift} L 302 {78 + shift} L 302 158" fill="none" stroke="#cbd5e1" stroke-width="14" stroke-linejoin="round"/>'
        f'<path d="M 128 158 L 128 {78 + shift} L 302 {78 + shift} L 302 158" fill="none" stroke="#475569" stroke-width="2" stroke-linejoin="round"/>'
        f'<path d="M 82 88 L 82 36 L 195 36" fill="none" stroke="#0f172a" stroke-width="2"/>'
        f'<path d="M 348 88 L 348 36 L 235 36" fill="none" stroke="#0f172a" stroke-width="2"/>'
        f'<circle cx="215" cy="36" r="18" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="215" y="40" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{meter_lbl}</text>'
        f'<text x="215" y="68" font-size="10.5" fill="#334155" text-anchor="middle">Salt bridge (B) | {reading_txt}</text>'
        f'<text x="100" y="212" font-size="10.5" fill="#0f172a" text-anchor="middle">Zn in ZnSO4</text>'
        f'<text x="330" y="212" font-size="10.5" fill="#0f172a" text-anchor="middle">Cu in CuSO4</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_electrode_mass_chart(rng: random.Random, zn_i: float, zn_f: float, cu_i: float, cu_f: float) -> Dict[str, Any]:
    """Parameterized before vs after plate masses in a Zn-Cu electrochemical cell."""
    svg = (
        f'<svg viewBox="0 0 420 195" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="195" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="24" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Electrode Mass Before vs After 40 min Operation</text>'
        f'<rect x="65" y="55" width="46" height="90" fill="#94a3b8" stroke="#334155"/>'
        f'<rect x="122" y="{145 - int(90 * (zn_f / zn_i))}" width="46" height="{int(90 * (zn_f / zn_i))}" fill="#475569" stroke="#0f172a"/>'
        f'<rect x="245" y="55" width="46" height="90" fill="#fb923c" stroke="#9a3412"/>'
        f'<rect x="302" y="{145 - int(90 * (cu_f / cu_i))}" width="46" height="{int(90 * (cu_f / cu_i))}" fill="#c2410c" stroke="#431407"/>'
        f'<text x="88" y="48" font-size="10" fill="#0f172a" text-anchor="middle">{_fmt_num(zn_i)} g</text>'
        f'<text x="145" y="{138 - int(90 * (zn_f / zn_i))}" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">{_fmt_num(zn_f)} g</text>'
        f'<text x="268" y="48" font-size="10" fill="#0f172a" text-anchor="middle">{_fmt_num(cu_i)} g</text>'
        f'<text x="325" y="{138 - int(90 * (cu_f / cu_i))}" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">{_fmt_num(cu_f)} g</text>'
        f'<text x="116" y="170" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Zinc Plate (Before / After)</text>'
        f'<text x="296" y="170" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Copper Plate (Before / After)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_reversed_series_battery(rng: random.Random, v_cell: float, n_forward: int, n_rev: int) -> Dict[str, Any]:
    """Parameterized battery of n_forward+n_rev cells where n_rev faces backwards."""
    total = n_forward + n_rev
    rev_idx = rng.randint(1, total - 1) if n_rev == 1 else total - 1
    cells = []
    start_x = 85
    for i in range(total):
        x = start_x + i * 56
        is_rev = (i == rev_idx)
        l_x, s_x = (x + 22, x + 8) if is_rev else (x + 8, x + 22)
        col = "#dc2626" if is_rev else "#0f172a"
        cells.append(
            f'<line x1="{l_x}" y1="62" x2="{l_x}" y2="122" stroke="{col}" stroke-width="3"/>'
            f'<line x1="{s_x}" y1="77" x2="{s_x}" y2="107" stroke="{col}" stroke-width="5"/>'
            f'<text x="{x + 15}" y="142" font-size="10" fill="{col}" text-anchor="middle">{_fmt_num(v_cell)} V {"(rev)" if is_rev else ""}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="175" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="40" y1="92" x2="380" y2="92" stroke="#94a3b8" stroke-dasharray="3,2"/>'
        f'{"".join(cells)}'
        f'<text x="210" y="28" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{total} Series Cells ({n_rev} reversed)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_half_cell_definition_zinc_half_vs_copper_half_cell(rng: random.Random) -> Dict[str, Any]:
    half_target = rng.choice([("zinc half-cell", "zinc metal strip dipped in aqueous zinc sulfate (ZnSO4)"), ("copper half-cell", "copper plate dipped in aqueous copper(II) sulfate (CuSO4)")])
    h_name, comp = half_target
    prompt = (
        f"A two-beaker Daniell electrochemical cell splits the chemistry into two separate **half-cells**, one of which is the **{h_name}**.\n\n"
        f"1. State the exact metal and electrolyte composition inside the **{h_name}** [1].\n"
        "2. Explain what a **half-cell** represents inside a full electrochemical system [1]."
    )
    correct = f"{comp.capitalize()}; Each half-cell holds one metal electrode submerged in its own electrolyte where either oxidation or reduction occurs, needing connection to the partner half-cell to work"
    sol = (
        f"**Step 1:** Composition of the {h_name}: **{comp}** [1].\n\n"
        "**Step 2:** A **half-cell** is one electrode–electrolyte compartment of the complete cell; on its own no continuous loop completes until paired with a second half-cell [1]."
    )
    return _q(
        rng, "26", "26_half_cell_definition_zinc_half_vs_copper_half_cell", prompt, correct, sol, 2, "short_answer",
        ["thinking_half_cell_works_alone_without_partner_myth"],
        "Remember: Zinc strip sits in ZnSO4; Copper plate sits in CuSO4!",
        f"{comp}; one half of the full redox cell.",
        correct,
    )


def arch_27_salt_bridge_u_tube_purpose_ion_migration_closing_circuit(rng: random.Random) -> Dict[str, Any]:
    meter = rng.choice(["V", "A"])
    read_txt = "1,1 V" if meter == "V" else "0,4 A"
    spec = _svg_zn_cu_salt_bridge_cell(rng, meter, read_txt)
    prompt = (
        "Inspect the zinc–copper electrochemical cell diagram featuring the inverted U-tube labelled **Salt bridge (B)** bridging the two beakers.\n\n"
        "State **two vital functions** of the salt bridge in keeping this cell operating continuously [2]."
    )
    correct = "1. Completes the internal electrical circuit between both beakers; 2. Allows ions to migrate between half-cells so solutions stay electrically neutral as reactions proceed."
    sol = (
        "**Step 1:** Without the U-tube, wires only connect the tops — the salt bridge **completes the closed electrical circuit** between the two solutions [1].\n\n"
        "**Step 2:** It permits **ion migration** so positive and negative charges stay balanced in both beakers as zinc dissolves and copper plates out [1]."
    )
    return _q(
        rng, "27", "27_salt_bridge_u_tube_purpose_ion_migration_closing_circuit", prompt, correct, sol, 2, "short_answer",
        ["claiming_electrons_swim_through_salt_bridge_myth"],
        "Does the salt bridge pass solid wires' electrons, or dissolved IONS to close the circuit and keep charge neutral?",
        "1. Completes closed circuit; 2. Permits ion flow maintaining electrical neutrality.",
        correct, diagram_spec=spec,
    )


def arch_28_effect_of_lifting_out_salt_bridge_reading_drops_to_zero(rng: random.Random) -> Dict[str, Any]:
    meter = rng.choice(["voltmeter reading (initially 1,10 V)", "ammeter current (initially 0,35 A)"])
    prompt = (
        f"While the zinc–copper cell operates steadily with a **{meter}**, a learner lifts the U-tube salt bridge completely out of both beakers into mid-air.\n\n"
        "State the immediate change observed on the meter and explain why [2]."
    )
    correct = "The reading drops immediately to 0; lifting the salt bridge opens/breaks the internal electrical circuit and stops ion balance between half-cells."
    sol = (
        "**Step 1:** The meter reading drops instantaneously to **zero (0)** [1].\n\n"
        "**Step 2:** Removing the salt bridge creates an **open circuit**, stopping ion migration and halting external electron flow [1]."
    )
    return _q(
        rng, "28", "28_effect_of_lifting_out_salt_bridge_reading_drops_to_zero", prompt, correct, sol, 2, "short_answer",
        ["thinking_zinc_copper_cell_runs_with_salt_bridge_removed_myth"],
        "What happens to any circuit when you cut a wire or remove the connecting bridge?",
        "Breaks internal circuit -> reading drops instantly to 0.",
        correct,
    )


def arch_29_zinc_electrode_dissolving_oxidation_into_znso4_solution(rng: random.Random) -> Dict[str, Any]:
    mins = rng.choice([30, 45, 60])
    prompt = (
        f"After connecting a zinc–copper cell to a load for **{mins} minutes**, learners examine the **zinc electrode** in its $\\text{{ZnSO}}_4$ beaker.\n\n"
        "Describe what happens to the solid zinc atoms at this electrode, explaining which way electrons move into the external wire [2]."
    )
    correct = "Zinc metal atoms lose electrons (oxidise) and dissolve into the zinc sulfate solution as Zn2+ ions, sending excess electrons up into the external wire towards copper."
    sol = (
        "**Step 1:** Solid zinc atoms go into the aqueous solution as **zinc ions ($Zn^{2+}$)** [1].\n\n"
        "**Step 2:** Each atom leaves two electrons behind on the zinc strip, feeding electrons out through the external wire (**negative terminal**) [1]."
    )
    return _q(
        rng, "29", "29_zinc_electrode_dissolving_oxidation_into_znso4_solution", prompt, correct, sol, 2, "short_answer",
        ["thinking_zinc_plate_gains_mass_during_discharge_error"],
        "Remember textbook observation: zinc plate dissolves/shrinks while releasing electrons!",
        "Zn atoms dissolve as Zn2+ ions into solution, leaving electrons to enter external circuit.",
        correct,
    )


def arch_30_copper_electrode_plating_deposition_from_cuso4_solution(rng: random.Random) -> Dict[str, Any]:
    duration = rng.choice([25, 40, 50])
    prompt = (
        f"During **{duration} minutes** of operation in a zinc–copper cell, electrons arrive along the external wire at the **copper electrode** dipping into blue $\\text{{CuSO}}_4$ solution.\n\n"
        "Explain what occurs at the copper electrode surface and why reddish-brown solid copper builds up there [2]."
    )
    correct = "Dissolved copper ions (Cu2+) from the CuSO4 solution gain arriving electrons at the electrode and deposit (plate out) onto the plate as solid metallic copper atoms."
    sol = (
        "**Step 1:** Arriving electrons from the wire meet dissolved **$Cu^{2+}$ ions** in $\\text{CuSO}_4$ solution [1].\n\n"
        "**Step 2:** Copper ions gain electrons and **deposit onto the copper strip** as freshly plated solid copper atoms [1]."
    )
    return _q(
        rng, "30", "30_copper_electrode_plating_deposition_from_cuso4_solution", prompt, correct, sol, 2, "short_answer",
        ["thinking_copper_plate_dissolves_in_daniell_cell_error"],
        "Opposite of zinc: copper ions in solution GAIN electrons and turn into solid metallic copper!",
        "Cu2+ ions plate onto the copper electrode as solid copper.",
        correct,
    )


def arch_31_electrode_mass_change_zn_decreases_cu_increases_data(rng: random.Random) -> Dict[str, Any]:
    zn_i = rng.choice([20.0, 24.0])
    dm = rng.choice([1.6, 2.2, 2.8])
    zn_f = zn_i - dm
    cu_i = rng.choice([20.0, 24.0])
    cu_f = cu_i + dm
    spec = _svg_electrode_mass_chart(rng, zn_i, zn_f, cu_i, cu_f)
    prompt = (
        "Inspect the laboratory mass measurements recorded before and after running the zinc–copper electrochemical cell.\n\n"
        f"1. State the exact change in mass (in grams) of BOTH electrodes: Zinc ({_fmt_num(zn_i)} g -> {_fmt_num(zn_f)} g) and Copper ({_fmt_num(cu_i)} g -> {_fmt_num(cu_f)} g) [2].\n"
        "2. Explain chemically why one plate lost mass while the other gained mass [2]."
    )
    correct = f"Zinc lost {_fmt_num(dm)} g; Copper gained {_fmt_num(dm)} g; Solid Zn dissolved into ZnSO4 solution as Zn2+ ions while dissolved Cu2+ ions plated onto the Cu electrode as solid copper"
    sol = (
        f"**Step 1:** $\\Delta m_{{\\text{{Zn}}}} = {_fmt_num(zn_f)} - {_fmt_num(zn_i)} = -{_fmt_num(dm)}\\text{{ g}}$ (**decreased**); $\\Delta m_{{\\text{{Cu}}}} = {_fmt_num(cu_f)} - {_fmt_num(cu_i)} = +{_fmt_num(dm)}\\text{{ g}}$ (**increased**) [2].\n\n"
        "**Step 2:** Solid zinc oxidised into solution as ions, whereas aqueous $Cu^{2+}$ deposited as solid copper metal [2]."
    )
    return _q(
        rng, "31", "31_electrode_mass_change_zn_decreases_cu_increases_data", prompt, correct, sol, 4, "structured",
        ["predicting_both_electrodes_keep_constant_mass_myth"],
        "Compare the grey zinc bars before/after vs orange copper bars before/after.",
        f"Zn decreases by {_fmt_num(dm)} g (dissolves); Cu increases by {_fmt_num(dm)} g (deposits).",
        correct, diagram_spec=spec,
    )


def arch_32_solution_colour_fading_in_blue_copper_sulfate_half_cell(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([3, 4, 5])
    prompt = (
        f"A Grade 9 teacher leaves a zinc–copper half-cell running continuously through a small motor for **{hours} hours**. Learners observe that the rich bright **blue colour** of the $\\text{{CuSO}}_4$ beaker noticeably turns **paler blue**.\n\n"
        "Give the chemical explanation for why the copper(II) sulfate solution loses its deep blue colour over time [2]."
    )
    correct = "The blue colour is caused by dissolved Cu2+ ions; as Cu2+ ions accept electrons and plate out onto the copper electrode, their concentration in solution drops, fading the blue tint."
    sol = (
        "**Step 1:** Aqueous **copper(II) ions ($Cu^{2+}$)** give $\\text{CuSO}_4$ its characteristic blue colour [1].\n\n"
        "**Step 2:** As reaction proceeds, **$Cu^{2+}$ ions leave solution** to form metallic copper on the plate, lowering concentration and paling the liquid [1]."
    )
    return _q(
        rng, "32", "32_solution_colour_fading_in_blue_copper_sulfate_half_cell", prompt, correct, sol, 2, "short_answer",
        ["thinking_blue_colour_leaks_up_salt_bridge_myth"],
        "Which particle in CuSO4(aq) produces the blue colour — SO4(2-) or Cu2+?",
        "Blue Cu2+ ions get used up plating onto the copper strip -> blue colour fades.",
        correct,
    )


def arch_33_why_electrons_never_swim_through_electrolyte_ions_carry_charge(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice(["external copper wire vs salt bridge / aqueous electrolyte", "wire loop vs liquid beaker solutions"])
    prompt = (
        f"Compare the **charge carriers** moving inside the **{part}** of an active electrochemical cell.\n\n"
        "State accurately which mobile particles carry charge in the **metal wires** vs inside the **electrolytes & salt bridge** [2]."
    )
    correct = "Free electrons carry electric charge through the external metal wires and plates; dissolved positive and negative IONS (never free electrons) migrate to carry charge through the electrolytes and salt bridge."
    sol = (
        "**Step 1:** Through solid metal wires/plates: **delocalised electrons** move [1].\n\n"
        "**Step 2:** Through aqueous solutions and the U-tube salt bridge: **dissolved cations and anions (ions)** move — free electrons do not swim through water [1]."
    )
    return _q(
        rng, "33", "33_why_electrons_never_swim_through_electrolyte_ions_carry_charge", prompt, correct, sol, 2, "short_answer",
        ["electrons_flow_through_liquid_electrolyte_myth"],
        "Metals pass electrons; solutions and salt bridges pass IONS!",
        "Wires = electrons; Electrolytes & salt bridge = mobile ions.",
        correct,
    )


def arch_34_labeling_complete_zn_cu_salt_bridge_cell_diagram(rng: random.Random) -> Dict[str, Any]:
    ask = rng.choice([
        ("Left beaker solution containing Zn strip", "Zinc sulfate solution (ZnSO4)"),
        ("Right beaker solution containing Cu plate", "Copper(II) sulfate solution (CuSO4)"),
        ("Inverted glass U-tube connecting both beakers", "Salt bridge"),
    ])
    clue, ans = ask
    prompt = (
        "In revision Question 5 (*Electric cells as energy systems*), marks are awarded for essential labels and apparatus rules of a zinc–copper cell.\n\n"
        f"1. State the exact chemical/apparatus label for the **{clue}** [1].\n"
        "2. Why must both open ends of the U-tube be completely submerged below the liquid surfaces? [1]"
    )
    correct = f"{ans}; Submerging both ends keeps the ionic bridge continuous so ions migrate freely and close the circuit"
    sol = (
        f"**Step 1:** Correct label: **{ans}** [1].\n\n"
        "**Step 2:** An air gap at either tip breaks ion contact, acting like an open switch (circuit broken, current = 0) [1]."
    )
    return _q(
        rng, "34", "34_labeling_complete_zn_cu_salt_bridge_cell_diagram", prompt, correct, sol, 2, "short_answer",
        ["submerging_only_one_salt_bridge_end_error"],
        "Check half-cell matching rules (metal sits in its own salt) + air gap = open circuit.",
        f"{ans}; both tips submerged keep ionic circuit closed.",
        correct,
    )


def arch_35_comparing_fruit_cell_vs_beaker_zn_cu_salt_bridge_cell(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice(["electrolyte placement", "steady voltage longevity"])
    prompt = (
        "Compare a **single-lemon fruit cell (Zn + Cu nails)** with a **two-beaker Zn–Cu half-cell apparatus**.\n\n"
        "State **one structural similarity** and **one practical difference** (e.g. steady current or separate half-cell separation) between them [2]."
    )
    correct = "Similarity: Both use dissimilar Zn and Cu electrodes and ionic electrolytes to convert chemical into electrical energy; Difference: The two-beaker cell separates electrodes into individual half-cells bridged by a salt bridge and delivers steadier, stronger voltage/current (~1,1 V)."
    sol = (
        "**Step 1 (Similarity):** Both pair reactive Zn vs unreactive Cu across an ionic **electrolyte** [1].\n\n"
        "**Step 2 (Difference):** The two-beaker cell isolates separate half-cell electrolytes connected by a **salt bridge**, yielding cleaner reactions and steadier output [1]."
    )
    return _q(
        rng, "35", "35_comparing_fruit_cell_vs_beaker_zn_cu_salt_bridge_cell", prompt, correct, sol, 2, "short_answer",
        ["thinking_fruit_cells_outpower_beaker_cells_myth"],
        "Contrast what stays the same (two metals + electrolyte) vs separation via salt bridge.",
        "Same Zn/Cu chemistry; two-beaker cell isolates half-cells with salt bridge for steadier current.",
        correct,
    )


def arch_36_ammeter_and_voltmeter_placement_on_zn_cu_cell(rng: random.Random) -> Dict[str, Any]:
    instr = rng.choice([("voltmeter (+ red lead)", "copper electrode (+)", "zinc electrode (-)"), ("ammeter in the wire loop", "measures electron flow rate directly in amperes", "connected in series with external circuit")])
    part, a, b = instr
    if "voltmeter" in part:
        prompt = (
            "When hooking a digital DC **voltmeter** across a zinc–copper cell to obtain a clean positive reading (+1,1 V instead of -1,1 V):\n\n"
            "Which electrode (Zn or Cu) connects to the voltmeter's **positive (+ red)** terminal, and which connects to the **negative (- black)** terminal? [2]"
        )
        correct = f"Positive (+ red) lead -> {a}; Negative (- black) lead -> {b}"
    else:
        prompt = (
            "If you replace the LED bulb in a cell test with a low-resistance **ammeter (A)**:\n\n"
            "1. What does a non-zero ammeter reading confirm about electrons? [1]\n"
            "2. Why must an ammeter ALWAYS be connected in series with a load (never bare across terminals of a commercial 9 V battery)? [1]"
        )
        correct = "Confirms electrons are moving as electric current around the closed external circuit; An ammeter has nearly zero resistance so wiring it directly across a strong battery creates a damaging short circuit"
    sol = (
        "**Step 1 & 2:** Apply correct polarity and safety topology:\n"
        f"{correct} [2]."
    )
    return _q(
        rng, "36", "36_ammeter_and_voltmeter_placement_on_zn_cu_cell", prompt, correct, sol, 2, "short_answer",
        ["wiring_bare_ammeter_across_battery_terminals_error"],
        "Remember: Zn gives off electrons (-), Cu attracts them (+); Ammeters have very low R!",
        correct,
        correct,
    )


def arch_37_salt_bridge_suitable_electrolyte_kcl_or_na2so4_not_sugar(rng: random.Random) -> Dict[str, Any]:
    cand = rng.choice([
        ("potassium nitrate (KNO3) solution", "distilled sucrose (sugar) solution", "KNO3(aq)"),
        ("sodium sulfate (Na2SO4) paste", "pure cooking oil", "Na2SO4 paste"),
    ])
    good, bad, winner = cand
    prompt = (
        f"When cotton wool soaked in liquid fills a U-tube salt bridge, a learner compares **{good}** against **{bad}**.\n\n"
        "State which liquid will make the cell work and explain why the other causes **$0\\text{{ V}}$ / $0\\text{{ A}}$** [2]."
    )
    correct = f"{winner} works because it dissociates into free mobile ions to conduct internally; {bad} has zero mobile ions (acts as an electrical insulator breaking the circuit)"
    sol = (
        f"**Step 1:** Choose **{winner}** because ionic salts split into free charged ions in water [1].\n\n"
        f"**Step 2:** **{bad.capitalize()}** lacks mobile ions and acts like an open gap [1]."
    )
    return _q(
        rng, "37", "37_salt_bridge_suitable_electrolyte_kcl_or_na2so4_not_sugar", prompt, correct, sol, 2, "short_answer",
        ["claiming_oil_or_sugar_conducts_salt_bridge_error"],
        "Salt bridges MUST contain soluble ionic salts (electrolytes), NOT oil or sugar.",
        f"{winner} supplies mobile ions; {bad} is non-conductive.",
        correct,
    )


def arch_38_identifying_terminal_polarity_of_zinc_vs_copper_electrodes(rng: random.Random) -> Dict[str, Any]:
    metal_hi = rng.choice(["Zinc (Zn)", "Magnesium (Mg)", "Iron (Fe)"])
    prompt = (
        f"When **{metal_hi}** is paired with **Copper (Cu)** in an acidic or sulfate electrochemical cell, {metal_hi.split()[0]} reacts much more strongly than copper, pushing electrons into the wire.\n\n"
        f"1. State which metal acts as the **negative (-)** terminal and which acts as the **positive (+)** terminal [2].\n"
        "2. State the direction electrons move through the external wire between the two metals [1]."
    )
    correct = f"Negative (-) = {metal_hi}; Positive (+) = Copper (Cu); Electrons travel externally from {metal_hi.split()[0]} to Copper"
    sol = (
        f"**Step 1:** The more reactive metal (**{metal_hi}**) oxidises to release electrons -> **negative (-) terminal**; unreactive **Copper** receives them -> **positive (+) terminal** [2].\n\n"
        f"**Step 2:** Electrons flow through the external wire from **{metal_hi.split()[0]} $\\rightarrow$ Copper** [1]."
    )
    return _q(
        rng, "38", "38_identifying_terminal_polarity_of_zinc_vs_copper_electrodes", prompt, correct, sol, 3, "structured",
        ["reversing_zn_and_cu_polarity_in_cell_error"],
        "More reactive metal loses electrons (source of negative electrons = negative terminal!).",
        f"(-) = {metal_hi}, (+) = Copper; e- go {metal_hi.split()[0]} -> Cu.",
        correct,
    )


def arch_39_cells_in_series_total_voltage_sum_vtotal_formula(rng: random.Random) -> Dict[str, Any]:
    v_each = rng.choice([1.5, 1.2, 2.0])
    n_cells = rng.choice([3, 4, 5, 6])
    v_tot = n_cells * v_each
    prompt = (
        f"A Grade 9 camp lantern connects **{n_cells} identical electric cells in series**, each rated at **${_fmt_num(v_each)}\\text{{ V}}$**, all facing the same correct orientation (+ to -).\n\n"
        "Calculate the **total potential difference ($V_{\\text{total}}$)** supplied by this battery [2]."
    )
    correct = f"{_fmt_num(v_tot)} V"
    sol = (
        "**Step 1:** For cells connected in series with matching polarity, individual voltages add directly: $V_{\\text{total}} = V_1 + V_2 + \\dots$ [1].\n\n"
        f"**Step 2:** $V_{{\\text{{total}}}} = {n_cells} \\times {_fmt_num(v_each)}\\text{{ V}} = \\mathbf{{{_fmt_num(v_tot)}\\text{{ V}}}}$ [1]."
    )
    return _q(
        rng, "39", "39_cells_in_series_total_voltage_sum_vtotal_formula", prompt, correct, sol, 2, "short_answer",
        ["assuming_series_cells_stay_at_single_cell_voltage_error"],
        "In series, add the voltages: V_total = n x V_cell.",
        f"{n_cells} x {_fmt_num(v_each)} = {_fmt_num(v_tot)} V.",
        correct,
    )


def arch_40_calculating_single_cell_voltage_from_battery_total(rng: random.Random) -> Dict[str, Any]:
    v_cell = rng.choice([1.5, 2.0, 3.0])
    n_cells = rng.choice([4, 6])
    v_tot = v_cell * n_cells
    prompt = (
        f"A sealed battery pack marked **${_fmt_num(v_tot)}\\text{{ V}}$** contains **{n_cells} identical electric cells** wired end-to-end in series.\n\n"
        "Determine the voltage of **each individual cell** inside the pack [2]."
    )
    correct = f"{_fmt_num(v_cell)} V"
    sol = (
        f"**Step 1:** Since series voltages sum equally, $V_{{\\text{{cell}}}} = \\frac{{V_{{\\text{{total}}}}}}{{n}}$ [1].\n\n"
        f"**Step 2:** $V_{{\\text{{cell}}}} = \\frac{{{_fmt_num(v_tot)}\\text{{ V}}}}{{{n_cells}}} = \\mathbf{{{_fmt_num(v_cell)}\\text{{ V}}}}$ [1]."
    )
    return _q(
        rng, "40", "40_calculating_single_cell_voltage_from_battery_total", prompt, correct, sol, 2, "short_answer",
        ["multiplying_total_voltage_by_cell_count_error"],
        "Divide the total series voltage by the number of identical cells.",
        f"{_fmt_num(v_tot)} / {n_cells} = {_fmt_num(v_cell)} V.",
        correct,
    )


def arch_41_effect_of_one_reversed_backwards_cell_in_series_battery(rng: random.Random) -> Dict[str, Any]:
    v_cell = rng.choice([1.5, 2.0])
    n_forward = rng.choice([2, 3])
    n_rev = 1
    net_v = (n_forward - n_rev) * v_cell
    spec = _svg_reversed_series_battery(rng, v_cell, n_forward, n_rev)
    prompt = (
        f"Inspect the battery circuit where **one {_fmt_num(v_cell)} V cell is accidentally inserted backwards** (reversed polarity) among {n_forward + n_rev} identical series cells.\n\n"
        "Calculate the resulting **net battery potential difference** across the battery [3]."
    )
    correct = f"{_fmt_num(net_v)} V"
    sol = (
        f"**Step 1:** {n_forward} forward cells add **${n_forward} \\times {_fmt_num(v_cell)} = +{_fmt_num(n_forward * v_cell)}\\text{{ V}}$**, while the **1 reversed cell** pushes opposite (**$-{_fmt_num(v_cell)}\\text{{ V}}$**) cancelling one forward cell [2].\n\n"
        f"**Step 2:** $V_{{\\text{{net}}}} = {_fmt_num(n_forward * v_cell)} - {_fmt_num(v_cell)} = \\mathbf{{{_fmt_num(net_v)}\\text{{ V}}}}$ [1]."
    )
    return _q(
        rng, "41", "41_effect_of_one_reversed_backwards_cell_in_series_battery", prompt, correct, sol, 3, "short_answer",
        ["adding_reversed_cell_voltage_as_positive_error"],
        "Notice one red backwards cell cancels ONE forward cell of equal voltage!",
        f"{_fmt_num(n_forward * v_cell)} - {_fmt_num(v_cell)} = {_fmt_num(net_v)} V.",
        correct, diagram_spec=spec,
    )


def arch_42_cells_in_parallel_same_voltage_longer_battery_life(rng: random.Random) -> Dict[str, Any]:
    v_cell = rng.choice([1.5, 3.0])
    n_cells = rng.choice([2, 3])
    prompt = (
        f"Suppose **{n_cells} identical ${_fmt_num(v_cell)}\\text{{ V}}$ cells** are wired in **parallel** (+ to +, - to -) rather than in series across a single torch bulb.\n\n"
        f"1. State the total potential difference across the parallel battery bank [1].\n"
        "2. State the main operational advantage of connecting cells in parallel [1]."
    )
    correct = f"{_fmt_num(v_cell)} V (stays equal to a single cell); Cells share the current load so the battery bank lasts much longer before running flat"
    sol = (
        f"**Step 1:** Connecting identical cells in **parallel** preserves single-cell voltage: **${_fmt_num(v_cell)}\\text{{ V}}$** [1].\n\n"
        f"**Step 2:** Each cell only supplies $1/{n_cells}$ of total current, extending **battery lifespan ({n_cells}x longer)** [1]."
    )
    return _q(
        rng, "42", "42_cells_in_parallel_same_voltage_longer_battery_life", prompt, correct, sol, 2, "short_answer",
        ["multiplying_voltage_for_cells_in_parallel_error"],
        "Series adds VOLTAGE; Parallel keeps voltage the same and extends CAPACITY / DURATION!",
        f"{_fmt_num(v_cell)} V; lasts longer.",
        correct,
    )


def arch_43_bulb_brightness_adding_lemon_or_aa_cells_in_series(rng: random.Random) -> Dict[str, Any]:
    start_n = rng.choice([1, 2])
    end_n = start_n + rng.choice([1, 2])
    prompt = (
        f"A learner places **{start_n} cell(s)** in series with a 6 V torch filament bulb (glowing dim orange) and then adds more cells in series to total **{end_n} identical cells**.\n\n"
        "Describe how BOTH **bulb brightness** and **circuit current (ammeter reading)** change, explaining why [2]."
    )
    correct = "Both circuit current and bulb brightness increase noticeably, because higher total series voltage pushes more electrical energy per charge (larger current) through the bulb per second."
    sol = (
        f"**Step 1:** Stepping from {start_n} to {end_n} series cells increases **total potential difference ($V$)** [1].\n\n"
        "**Step 2:** Higher voltage drives a **larger electric current ($I$)**, delivering more electrical energy per second -> **brighter glow** [1]."
    )
    return _q(
        rng, "43", "43_bulb_brightness_adding_lemon_or_aa_cells_in_series", prompt, correct, sol, 2, "short_answer",
        ["thinking_more_series_cells_makes_bulb_dimmer_error"],
        "More cells in series -> more voltage -> larger current -> brighter bulb.",
        "Both current and bulb brightness increase.",
        correct,
    )


def arch_44_primary_single_use_cells_zinc_carbon_vs_alkaline(rng: random.Random) -> Dict[str, Any]:
    chem = rng.choice(["zinc–carbon dry cell", "alkaline manganese cell"])
    prompt = (
        f"An ordinary supermarket **{chem}** is classified as a **primary electric cell**.\n\n"
        "1. What defines a **primary cell**? [1]\n"
        "2. Why is attempting to force current backwards into a primary dry cell in a wall charger unsafe? [1]"
    )
    correct = "A single-use non-rechargeable cell whose internal chemical reactions are irreversible; Recharging creates gas pressure buildup, leakage of corrosive paste, overheating, or bursting"
    sol = (
        "**Step 1:** A **primary cell** uses **irreversible chemical reactions**, so once reactants run out it cannot be restored [1].\n\n"
        "**Step 2:** Forcing reverse charging heats the sealed can and builds **gas pressure**, risking **chemical leaks or explosion** [1]."
    )
    return _q(
        rng, "44", "44_primary_single_use_cells_zinc_carbon_vs_alkaline", prompt, correct, sol, 2, "short_answer",
        ["recharging_primary_zinc_carbon_batteries_in_charger_error"],
        "Primary = single-use irreversible chemistry; NOT rechargeable!",
        "Irreversible reactions (non-rechargeable); reverse charging risks gas buildup/rupture.",
        correct,
    )


def arch_45_secondary_rechargeable_cells_nicd_nimh_lithium_ion(rng: random.Random) -> Dict[str, Any]:
    cell_t = rng.choice(["Nickel-Cadmium (NiCd)", "Nickel-Metal Hydride (NiMH)", "Lithium-ion (Li-ion)"])
    prompt = (
        f"Modern mobile phones, laptops, and solar power banks use **{cell_t}** batteries classified as **secondary cells**.\n\n"
        "State what distinguishes a **secondary cell** from a primary cell, and name one environmental advantage of secondary cells [2]."
    )
    correct = "A secondary cell relies on REVERSIBLE chemical reactions so it can be recharged hundreds of times; Generates far less long-term battery landfill waste per unit of energy used."
    sol = (
        "**Step 1:** **Secondary cells** perform **reversible electrochemical reactions**, letting electrical chargers regenerate original reactants repeatedly [1].\n\n"
        "**Step 2:** Environmental benefit: one secondary cell replaces hundreds of thrown-away primary cells, drastically **cutting solid and heavy-metal waste** [1]."
    )
    return _q(
        rng, "45", "45_secondary_rechargeable_cells_nicd_nimh_lithium_ion", prompt, correct, sol, 2, "short_answer",
        ["confusing_primary_and_secondary_battery_classifications"],
        "Primary = once-off; Secondary = reversible/rechargeable (e.g. NiCd, NiMH, Li-ion).",
        "Reversible chemistry (rechargeable); cuts disposable battery waste.",
        correct,
    )


def arch_46_lead_acid_car_battery_reversible_discharge_and_alternator(rng: random.Random) -> Dict[str, Any]:
    n_cells = 6
    v_each = 2.0
    v_tot = 12.0
    prompt = (
        f"A typical South African petrol vehicle uses a **12 V lead-acid battery** built from **{n_cells} secondary cells** wired in series (**{_fmt_num(v_each)} V** each).\n\n"
        "1. Which liquid acid serves as the electrolyte inside a lead-acid car battery? [1]\n"
        "2. How does the vehicle avoid going flat permanently after starting the starter motor every morning? [1]"
    )
    correct = "Dilute sulfuric acid (H2SO4); While the engine runs, the alternator generates electricity to recharge the battery backwards (electrical -> chemical energy)"
    sol = (
        "**Step 1:** Electrolyte inside lead-acid batteries: **dilute sulfuric acid ($\\text{H}_2\\text{SO}_4$)** [1].\n\n"
        "**Step 2:** The engine-driven **alternator** pumps current back in reverse, converting **electrical energy $\\rightarrow$ stored chemical energy** [1]."
    )
    return _q(
        rng, "46", "46_lead_acid_car_battery_reversible_discharge_and_alternator", prompt, correct, sol, 2, "short_answer",
        ["thinking_car_alternator_consumes_fuel_for_battery_without_recharging"],
        "Recall what strong acid fills car batteries and which car part recharges it on the highway.",
        "Dilute H2SO4; engine alternator recharges it continuously.",
        correct,
    )


def arch_47_recharging_electrical_energy_back_into_chemical_energy(rng: random.Random) -> Dict[str, Any]:
    phase = rng.choice(["Discharging (powering a smartphone screen)", "Recharging (plugged into a 5 V wall charger)"])
    is_dis = "Discharging" in phase
    prompt = (
        f"Consider the energy conversion direction occurring inside a lithium-ion cell during **{phase}**.\n\n"
        "State the exact energy transformation taking place inside the battery cell during this phase [2]."
    )
    if is_dis:
        correct = "Chemical potential energy -> Electrical energy (delivered out to power the phone circuit)"
    else:
        correct = "Electrical energy (from wall charger) -> Chemical potential energy (restored inside electrode materials)"
    sol = (
        f"**Step 1:** {'Discharging releases stored chemical fuel as current' if is_dis else 'Recharging drives chemical reactions in reverse using external electricity'} [1].\n\n"
        f"**Step 2:** Energy change: **{correct}** [1]."
    )
    return _q(
        rng, "47", "47_recharging_electrical_energy_back_into_chemical_energy", prompt, correct, sol, 2, "short_answer",
        ["swapping_charge_and_discharge_energy_directions"],
        "Discharge = Chemical -> Electrical; Recharge = Electrical -> Chemical.",
        correct,
        correct,
    )


def arch_48_heavy_metal_environmental_toxicity_lead_cadmium_mercury(rng: random.Random) -> Dict[str, Any]:
    metal = rng.choice(["lead (from car batteries)", "cadmium (from NiCd packs)", "mercury / zinc–acid pastes"])
    prompt = (
        f"Old discarded batteries contain toxic **heavy metals** such as **{metal}** along with corrosive acids or alkalis.\n\n"
        "Explain **two environmental hazards** if used batteries are dumped illegally into household bins or rivers [2]."
    )
    correct = f"1. Metal casings rust open so toxic heavy metals ({metal.split()[0]}) and corrosive acids leach into soil and groundwater/rivers; 2. Heavy metals poison plants, aquatic life, and accumulate up human food chains."
    sol = (
        f"**Step 1:** Corroded casings release **acidic/alkaline chemicals and {metal}** directly into soil and drinking groundwater [1].\n\n"
        "**Step 2:** Persistent heavy metals cause severe neurological/organ poisoning across aquatic ecosystems and **bioaccumulate** in food chains [1]."
    )
    return _q(
        rng, "48", "48_heavy_metal_environmental_toxicity_lead_cadmium_mercury", prompt, correct, sol, 2, "short_answer",
        ["thinking_flat_batteries_are_biodegradable_household_trash_myth"],
        "Think about what happens when battery metal cans rust inside damp landfill rain!",
        "Leaks corrosive chemicals + toxic heavy metals into groundwater and food chains.",
        correct,
    )


def arch_49_safe_battery_recycling_and_disposal_in_south_africa(rng: random.Random) -> Dict[str, Any]:
    drop_site = rng.choice(["supermarket e-waste/battery drop-off bin", "municipal hazardous waste depot", "automotive battery scrap recycler"])
    prompt = (
        f"Instead of throwing spent batteries onto open rubbish tips or burning them on fires, South African municipalities encourage returning dead cells to a **{drop_site}**.\n\n"
        "State **one safety hazard** of burning old batteries on a rubbish fire and **one benefit** of formal battery recycling [2]."
    )
    correct = "Burning explodes sealed cans and releases poisonous heavy-metal fumes into air; Recycling safely neutralises acids and recovers valuable lead, zinc, nickel, and lithium for new products without pollution."
    sol = (
        "**Step 1:** Heating/burning closed battery cells causes **violent explosions and toxic heavy-metal vapour clouds** [1].\n\n"
        f"**Step 2:** Dropping dead cells at a **{drop_site}** enables **metal recovery (circular economy)** and keeps heavy metals out of dams and farms [1]."
    )
    return _q(
        rng, "49", "49_safe_battery_recycling_and_disposal_in_south_africa", prompt, correct, sol, 2, "short_answer",
        ["thinking_burning_old_batteries_safely_destroys_toxins_myth"],
        "Never burn sealed cells! Recover valuable metals and protect water supplies.",
        "Explodes/toxic fumes if burned; recycling recovers metals cleanly and protects water.",
        correct,
    )


def arch_50_electric_cell_troubleshooting_and_term3_synthesis(rng: random.Random) -> Dict[str, Any]:
    fault = rng.choice([
        ("Learner connects two copper nails instead of Zn + Cu inside an orange", "Zero voltage (0 V): identical electrodes generate no potential difference; replace one copper nail with a zinc/galvanised strip"),
        ("Learner builds Zn-Cu cell but forgets to dip the U-tube salt bridge into the ZnSO4 beaker", "Zero voltage/current (0): open internal circuit; push U-tube tip cleanly below liquid level in both beakers"),
        ("Learner loads 3 AA cells (1,5 V each) in a torch with 1 cell reversed backwards", "Total voltage drops to 1,5 V instead of 4,5 V (dim bulb); flip the reversed cell so all + face the same direction"),
    ])
    obs, fix = fault
    prompt = (
        "During a Grade 9 practical test, an electrochemical setup fails to operate properly:\n"
        f"**Symptom / Error:** *{obs}.*\n\n"
        "Diagnose the scientific flaw and state the exact step needed to restore proper cell output [3]."
    )
    correct = fix
    sol = (
        "**Step 1:** Identify whether the failure stems from identical electrode chemistry, an open electrolyte circuit, or reversed series polarity [1].\n\n"
        f"**Step 2:** Diagnosis & remedy: **{fix}** [2]."
    )
    return _q(
        rng, "50", "50_electric_cell_troubleshooting_and_term3_synthesis", prompt, correct, sol, 3, "short_answer",
        ["failing_systematic_cell_fault_diagnosis"],
        "Check the 3 golden rules of working cells: (1) dissimilar metals, (2) closed electrolyte/salt bridge, (3) aligned + to - polarity.",
        fix,
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_half_cell_definition_zinc_half_vs_copper_half_cell": arch_26_half_cell_definition_zinc_half_vs_copper_half_cell,
    "27_salt_bridge_u_tube_purpose_ion_migration_closing_circuit": arch_27_salt_bridge_u_tube_purpose_ion_migration_closing_circuit,
    "28_effect_of_lifting_out_salt_bridge_reading_drops_to_zero": arch_28_effect_of_lifting_out_salt_bridge_reading_drops_to_zero,
    "29_zinc_electrode_dissolving_oxidation_into_znso4_solution": arch_29_zinc_electrode_dissolving_oxidation_into_znso4_solution,
    "30_copper_electrode_plating_deposition_from_cuso4_solution": arch_30_copper_electrode_plating_deposition_from_cuso4_solution,
    "31_electrode_mass_change_zn_decreases_cu_increases_data": arch_31_electrode_mass_change_zn_decreases_cu_increases_data,
    "32_solution_colour_fading_in_blue_copper_sulfate_half_cell": arch_32_solution_colour_fading_in_blue_copper_sulfate_half_cell,
    "33_why_electrons_never_swim_through_electrolyte_ions_carry_charge": arch_33_why_electrons_never_swim_through_electrolyte_ions_carry_charge,
    "34_labeling_complete_zn_cu_salt_bridge_cell_diagram": arch_34_labeling_complete_zn_cu_salt_bridge_cell_diagram,
    "35_comparing_fruit_cell_vs_beaker_zn_cu_salt_bridge_cell": arch_35_comparing_fruit_cell_vs_beaker_zn_cu_salt_bridge_cell,
    "36_ammeter_and_voltmeter_placement_on_zn_cu_cell": arch_36_ammeter_and_voltmeter_placement_on_zn_cu_cell,
    "37_salt_bridge_suitable_electrolyte_kcl_or_na2so4_not_sugar": arch_37_salt_bridge_suitable_electrolyte_kcl_or_na2so4_not_sugar,
    "38_identifying_terminal_polarity_of_zinc_vs_copper_electrodes": arch_38_identifying_terminal_polarity_of_zinc_vs_copper_electrodes,
    "39_cells_in_series_total_voltage_sum_vtotal_formula": arch_39_cells_in_series_total_voltage_sum_vtotal_formula,
    "40_calculating_single_cell_voltage_from_battery_total": arch_40_calculating_single_cell_voltage_from_battery_total,
    "41_effect_of_one_reversed_backwards_cell_in_series_battery": arch_41_effect_of_one_reversed_backwards_cell_in_series_battery,
    "42_cells_in_parallel_same_voltage_longer_battery_life": arch_42_cells_in_parallel_same_voltage_longer_battery_life,
    "43_bulb_brightness_adding_lemon_or_aa_cells_in_series": arch_43_bulb_brightness_adding_lemon_or_aa_cells_in_series,
    "44_primary_single_use_cells_zinc_carbon_vs_alkaline": arch_44_primary_single_use_cells_zinc_carbon_vs_alkaline,
    "45_secondary_rechargeable_cells_nicd_nimh_lithium_ion": arch_45_secondary_rechargeable_cells_nicd_nimh_lithium_ion,
    "46_lead_acid_car_battery_reversible_discharge_and_alternator": arch_46_lead_acid_car_battery_reversible_discharge_and_alternator,
    "47_recharging_electrical_energy_back_into_chemical_energy": arch_47_recharging_electrical_energy_back_into_chemical_energy,
    "48_heavy_metal_environmental_toxicity_lead_cadmium_mercury": arch_48_heavy_metal_environmental_toxicity_lead_cadmium_mercury,
    "49_safe_battery_recycling_and_disposal_in_south_africa": arch_49_safe_battery_recycling_and_disposal_in_south_africa,
    "50_electric_cell_troubleshooting_and_term3_synthesis": arch_50_electric_cell_troubleshooting_and_term3_synthesis,
}
