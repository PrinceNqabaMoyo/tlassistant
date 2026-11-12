"""Grade 9 Natural Sciences - Forces: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md.
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
        "id": f"ns9_frc_{code}_{rng.randint(100000, 999999)}",
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


def _svg_mass_weight_graph(rng: random.Random, m_top: int, g_val: float, planet: str) -> Dict[str, Any]:
    """Parameterized linear graph of Weight (N) vs Mass (kg)."""
    w_top = m_top * g_val
    svg = (
        f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="65" y1="28" x2="65" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="385" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="355" y2="45" stroke="#2563eb" stroke-width="3"/>'
        f'<line x1="65" y1="45" x2="355" y2="45" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<line x1="355" y1="45" x2="355" y2="175" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<circle cx="355" cy="45" r="4.5" fill="#1d4ed8"/>'
        f'<text x="56" y="49" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="end">{_fmt_num(w_top)}</text>'
        f'<text x="355" y="191" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{m_top}</text>'
        f'<text x="56" y="178" font-size="11" fill="#334155" text-anchor="end">0</text>'
        f'<text x="220" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Mass vs Weight on {planet}</text>'
        f'<text x="225" y="208" font-size="11" fill="#0f172a" text-anchor="middle">Mass (kg)</text>'
        f'<text x="20" y="100" font-size="11" fill="#0f172a" transform="rotate(-90 20 100)" text-anchor="middle">Weight (N)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_bar_magnet_field(rng: random.Random, flip: bool) -> Dict[str, Any]:
    """Parameterized bar magnet with directional magnetic field lines (N -> S)."""
    left_p, right_p = ("S", "N") if flip else ("N", "S")
    arr_dir = -1 if flip else 1
    mid_x = 215 + rng.randint(-6, 6)
    ax1 = mid_x + arr_dir * 6
    ax2 = mid_x - arr_dir * 6
    svg = (
        f'<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<path d="M 155 88 Q {mid_x} 24 275 88" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M 155 122 Q {mid_x} 186 275 122" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M 145 96 Q {mid_x} 52 285 96" fill="none" stroke="#475569" stroke-width="1.5"/>'
        f'<path d="M 145 114 Q {mid_x} 158 285 114" fill="none" stroke="#475569" stroke-width="1.5"/>'
        f'<polygon points="{ax1},56 {ax2},51 {ax2},61" fill="#2563eb"/>'
        f'<polygon points="{ax1},154 {ax2},149 {ax2},159" fill="#2563eb"/>'
        f'<rect x="135" y="88" width="80" height="34" fill="{"#2563eb" if flip else "#dc2626"}" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="215" y="88" width="80" height="34" fill="{"#dc2626" if flip else "#2563eb"}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="175" y="110" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">{left_p}</text>'
        f'<text x="255" y="110" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">{right_p}</text>'
        f'<text x="215" y="198" font-size="11" fill="#334155" text-anchor="middle">Bar Magnet Field Pattern ({left_p}-{right_p})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_like_poles_repel(rng: random.Random, pole: str) -> Dict[str, Any]:
    """Parameterized two facing like magnetic poles (N-N or S-S) showing neutral null point."""
    gap = rng.randint(58, 76)
    col = "#dc2626" if pole == "N" else "#2563eb"
    lx_end = 215 - gap // 2
    rx_start = 215 + gap // 2
    svg = (
        f'<svg viewBox="0 0 430 195" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="195" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="{lx_end - 80}" y="80" width="80" height="34" fill="{col}" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="{rx_start}" y="80" width="80" height="34" fill="{col}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="{lx_end - 22}" y="102" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">{pole}</text>'
        f'<text x="{rx_start + 22}" y="102" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">{pole}</text>'
        f'<path d="M {lx_end} 86 Q {lx_end + 16} 55 {lx_end - 18} 32" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M {lx_end} 108 Q {lx_end + 16} 139 {lx_end - 18} 162" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M {rx_start} 86 Q {rx_start - 16} 55 {rx_start + 18} 32" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<path d="M {rx_start} 108 Q {rx_start - 16} 139 {rx_start + 18} 162" fill="none" stroke="#475569" stroke-width="2"/>'
        f'<circle cx="215" cy="97" r="4" fill="#0f172a"/>'
        f'<text x="215" y="180" font-size="11" fill="#0f172a" text-anchor="middle">Centre gap {gap} mm (Point X at centre)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_electroscope(rng: random.Random, charge_sign: str, spread_deg: int) -> Dict[str, Any]:
    """Parameterized gold-leaf electroscope diverging due to like charge repulsion."""
    dx = spread_deg
    svg = (
        f'<svg viewBox="0 0 380 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="125" y="78" width="130" height="115" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<ellipse cx="190" cy="40" rx="34" ry="8" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<line x1="190" y1="48" x2="190" y2="128" stroke="#475569" stroke-width="4"/>'
        f'<line x1="190" y1="128" x2="{190 - dx}" y2="172" stroke="#eab308" stroke-width="3"/>'
        f'<line x1="190" y1="128" x2="{190 + dx}" y2="172" stroke="#eab308" stroke-width="3"/>'
        f'<text x="165" y="38" font-size="13" font-weight="bold" fill="#dc2626">{charge_sign}</text>'
        f'<text x="208" y="38" font-size="13" font-weight="bold" fill="#dc2626">{charge_sign}</text>'
        f'<text x="{182 - dx}" y="168" font-size="11" font-weight="bold" fill="#dc2626">{charge_sign}</text>'
        f'<text x="{194 + dx}" y="168" font-size="11" font-weight="bold" fill="#dc2626">{charge_sign}</text>'
        f'<text x="190" y="207" font-size="10.5" fill="#0f172a" text-anchor="middle">Charged Electroscope (spread {dx} px)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_mass_vs_weight_linear_graph_gradient_analysis(rng: random.Random) -> Dict[str, Any]:
    planet, g_val = rng.choice([("Planet Alpha", 9.8), ("Moon", 1.6), ("Mars", 3.7), ("Planet Beta", 12.0)])
    m_top = rng.choice([10, 15, 20])
    w_top = m_top * g_val
    spec = _svg_mass_weight_graph(rng, m_top, g_val, planet)
    prompt = (
        f"Study the Weight vs Mass graph plotted from experiments conducted on **{planet}**.\n\n"
        f"1. Calculate the **gradient (slope)** of the straight line using the coordinate $(m={m_top}\\text{{ kg}},\\; W={_fmt_num(w_top)}\\text{{ N}})$ [2].\n"
        "2. State what physical quantity this gradient represents, with units [2]."
    )
    correct = f"Gradient = {_fmt_num(g_val)} N/kg; Gravitational acceleration / field strength (g) on {planet}"
    sol = (
        f"**Step 1:** $\\text{{Gradient}} = \\frac{{\\Delta W}}{{\\Delta m}} = \\frac{{{_fmt_num(w_top)} - 0}}{{{m_top} - 0}} = \\mathbf{{{_fmt_num(g_val)}\\text{{ N/kg}}}}$ [2].\n\n"
        f"**Step 2:** Since $W = g \\cdot m$, the slope equals **{planet}'s gravitational field strength ($g$)** in **N/kg** [2]."
    )
    return _q(
        rng, "26", "26_mass_vs_weight_linear_graph_gradient_analysis", prompt, correct, sol, 4, "structured",
        ["inverting_slope_as_mass_divided_by_weight_error"],
        "Gradient = rise (Weight on y-axis) divided by run (Mass on x-axis).",
        f"{_fmt_num(w_top)} / {m_top} = {_fmt_num(g_val)} N/kg = g.",
        correct, diagram_spec=spec,
    )


def arch_27_apparent_weightlessness_in_orbit_free_fall_explained(rng: random.Random) -> Dict[str, Any]:
    alt = rng.choice([400, 420])
    prompt = (
        f"Astronauts aboard the International Space Station orbiting at **{alt} km** altitude float effortlessly inside the cabin, yet Earth's gravity there is still nearly **89%** as strong as on the ground!\n\n"
        "Explain why orbiting astronauts experience **apparent weightlessness** even though Earth's gravitational pull is NOT zero [2]."
    )
    correct = "Both the space station and astronauts are falling continuously around Earth together in free fall at matching horizontal orbital speeds, leaving zero normal support force against the cabin floor."
    sol = (
        "**Step 1:** Gravity is still strong at 400 km altitude (around $8{,}7\\text{ N/kg}$), bending their orbit [1].\n\n"
        "**Step 2:** Because the astronauts and spacecraft accelerate downward together in perpetual **free fall**, the astronauts press with **zero normal contact force** against scales or floors, creating apparent weightlessness [1]."
    )
    return _q(
        rng, "27", "27_apparent_weightlessness_in_orbit_free_fall_explained", prompt, correct, sol, 2, "short_answer",
        ["astronauts_float_because_zero_gravity_exists_at_iss_myth"],
        "If gravity truly dropped to zero 400 km up, what would happen to the orbiting ISS and the Moon?",
        "Continuous free fall around Earth leaves zero normal support force.",
        correct,
    )


def arch_28_ferromagnetic_metals_iron_nickel_cobalt_and_steel(rng: random.Random) -> Dict[str, Any]:
    items = rng.choice([
        (["iron nail", "stainless steel paperclip", "nickel coin"], "cobalt bolt"),
        (["mild steel screw", "cobalt rod", "iron filings"], "pure nickel wire"),
    ])
    trio, fourth = items
    prompt = (
        f"A Grade 9 learner tests which elements are **ferromagnetic** (strongly attracted to a permanent magnet): {', '.join(trio)}, and {fourth}.\n\n"
        "Name the **three primary ferromagnetic elements** on the Periodic Table and explain why steel is strongly magnetic [2]."
    )
    correct = "Iron (Fe), Nickel (Ni), and Cobalt (Co); Steel is an alloy composed predominantly of iron"
    sol = (
        "**Step 1:** Only three metallic elements at room temperature are strongly ferromagnetic: **Iron (Fe), Nickel (Ni), and Cobalt (Co)** [1].\n\n"
        "**Step 2:** Steel is strongly attracted because it is an alloy made overwhelmingly (~98%) of **iron** [1]."
    )
    return _q(
        rng, "28", "28_ferromagnetic_metals_iron_nickel_cobalt_and_steel", prompt, correct, sol, 2, "short_answer",
        ["claiming_all_metals_are_magnetic_myth"],
        "Think of the 'Fe-Co-Ni' magnetic triad — copper, aluminium, and gold are NOT among them!",
        "Iron, Nickel, Cobalt (and iron alloys like steel).",
        correct,
    )


def arch_29_non_magnetic_metals_copper_aluminium_brass_and_plastics(rng: random.Random) -> Dict[str, Any]:
    nonmag = rng.choice(["solid aluminium cooldrink can", "pure copper electrical cable", "brass door key", "gold ring"])
    prompt = (
        f"A recycling plant passes a strong electromagnet conveyor belt above mixed scrap containing **steel tins**, **{nonmag}**, and **plastic bottles**.\n\n"
        f"State what happens to the **{nonmag}** and explain why [2]."
    )
    correct = f"The {nonmag} stays on the belt (is NOT lifted by the magnet) because {nonmag.split()[1]} is a non-magnetic metal, unlike steel/iron."
    sol = (
        "**Step 1:** Magnetism does NOT attract every shiny metal [1].\n\n"
        f"**Step 2:** Since aluminium, copper, brass, and gold are **non-magnetic**, the **{nonmag}** remains unaffected on the belt while magnetic steel cans are pulled out [1]."
    )
    return _q(
        rng, "29", "29_non_magnetic_metals_copper_aluminium_brass_and_plastics", prompt, correct, sol, 2, "short_answer",
        ["thinking_aluminium_cans_stick_to_magnets_myth"],
        "Does an aluminium cooldrink tin stick to a fridge magnet?",
        f"Only iron, nickel, cobalt, and steel are attracted; {nonmag} is non-magnetic.",
        correct,
    )


def arch_30_magnetic_poles_north_south_and_law_of_attraction_repulsion(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("North pole of Magnet 1 faces North pole of Magnet 2", "Repel each other (push apart)"),
        ("South pole of Magnet 1 faces South pole of Magnet 2", "Repel each other (push apart)"),
        ("North pole of Magnet 1 faces South pole of Magnet 2", "Attract each other (pull together)"),
    ])
    setup, effect = pair
    prompt = (
        f"Two bar magnets hang freely on strings so that **{setup}**.\n\n"
        "State the interaction observed and the **Law of Magnetic Poles** explaining it [2]."
    )
    correct = f"{effect}; Like poles repel each other while opposite (unlike) poles attract each other"
    sol = (
        f"**Step 1:** Result: **{effect}** [1].\n\n"
        "**Step 2:** **Law of Magnetic Poles:** Like poles (N–N or S–S) repel; unlike poles (N–S) attract [1]."
    )
    return _q(
        rng, "30", "30_magnetic_poles_north_south_and_law_of_attraction_repulsion", prompt, correct, sol, 2, "short_answer",
        ["mixing_magnetic_attraction_and_repulsion_rules"],
        "Same poles push apart; opposite poles pull together.",
        f"{effect}.",
        correct,
    )


def arch_31_broken_bar_magnet_always_forms_new_north_south_dipoles(rng: random.Random) -> Dict[str, Any]:
    pieces = rng.choice(["two halves", "three smaller pieces"])
    prompt = (
        f"A bar magnet originally labelled **N** on its left tip and **S** on its right tip is accidentally snapped cleanly into **{pieces}**.\n\n"
        "Will the piece carrying the old **N** end exist as an isolated 'North-only monopole magnet'?"
    )
    correct = "No; every broken piece immediately behaves as a complete magnet with BOTH a North pole and a South pole at opposite ends."
    distractors = [
        "Yes; you get one pure North magnet and one pure South magnet.",
        "No; breaking a magnet destroys all magnetism instantly across every piece.",
        "Only the middle piece remains magnetic while both end pieces become copper.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Magnetic poles always exist in **North–South dipoles**.\n"
        "**Step 2:** Snapping a bar magnet creates new opposite poles right at every break face — magnetic monopoles do not form [2]."
    )
    return _q(
        rng, "31", "31_broken_bar_magnet_always_forms_new_north_south_dipoles", prompt, correct, sol, 2, "multiple_choice",
        ["magnetic_monopole_isolation_myth"],
        "Remember each tiny magnetic domain inside iron acts as a mini N–S magnet.",
        "Every broken fragment has BOTH an N pole and an S pole.",
        correct, options=options,
    )


def arch_32_magnetic_field_acting_through_non_magnetic_materials(rng: random.Random) -> Dict[str, Any]:
    barrier = rng.choice(["a thin sheet of cardboard", "a pane of window glass", "a wooden desk top", "a plastic Perspex ruler"])
    prompt = (
        f"A learner holds a strong magnet underneath **{barrier}** and moves a steel paperclip sitting on the top surface effortlessly.\n\n"
        "1. What does this demonstration prove about magnetic field forces? [2]\n"
        "2. What happens instead if a thick **soft iron plate** is placed between the magnet and the paperclip? [1]"
    )
    correct = f"Magnetic fields penetrate/act through non-magnetic barriers (like {barrier}) across a distance without physical contact; A thick iron plate shields/redirects magnetic field lines so the paperclip weakens/drops"
    sol = (
        f"**Step 1:** Magnetic forces are **field forces** that act across space and pass unhindered through **non-magnetic materials** such as {barrier} [2].\n\n"
        "**Step 2:** A ferromagnetic **iron plate** absorbs/redirects magnetic flux inside itself (magnetic shielding), blocking pull above it [1]."
    )
    return _q(
        rng, "32", "32_magnetic_field_acting_through_non_magnetic_materials", prompt, correct, sol, 3, "structured",
        ["thinking_paper_or_glass_blocks_magnetic_fields_myth"],
        "Compare non-magnetic barriers (glass/wood/plastic) vs magnetic iron shielding.",
        f"Passes cleanly through {barrier}; blocked/shielded by ferromagnetic iron.",
        correct,
    )


def arch_33_visualising_magnetic_field_lines_with_iron_filings(rng: random.Random) -> Dict[str, Any]:
    tool = rng.choice(["fine iron filings sprinkled gently onto white cardboard", "several miniature plotting compasses placed around the magnet"])
    prompt = (
        f"To map an invisible magnetic field around a bar magnet, a learner uses **{tool}**.\n\n"
        "1. Define a **magnetic field** [1].\n"
        "2. Where are field lines **most densely packed**, and what does higher line density signify? [2]"
    )
    correct = "A region in space around a magnet where another magnet or ferromagnetic material experiences a non-contact magnetic force; Packed closest at the North and South poles, where magnetic field strength is greatest"
    sol = (
        "**Step 1:** A **magnetic field** is the invisible 3D region around a magnet where magnetic forces are experienced [1].\n\n"
        "**Step 2:** Lines crowd **closest together at the N and S poles**, showing **strongest magnetic field intensity** there [2]."
    )
    return _q(
        rng, "33", "33_visualising_magnetic_field_lines_with_iron_filings", prompt, correct, sol, 3, "structured",
        ["claiming_magnetic_field_is_strongest_at_bar_middle_myth"],
        "Where do most paperclips cluster onto a bar magnet — the centre or the two ends?",
        "Densest lines = poles = strongest field.",
        correct,
    )


def arch_34_magnetic_field_line_direction_north_to_south_flux_density(rng: random.Random) -> Dict[str, Any]:
    flip = rng.choice([True, False])
    spec = _svg_bar_magnet_field(rng, flip)
    arrow_dir_txt = "from right (N) to left (S)" if flip else "from left (N) to right (S)"
    prompt = (
        "Examine the magnetic field line diagram surrounding a single bar magnet.\n\n"
        "1. State the standard physics convention for the direction of magnetic field lines **outside** a magnet [1].\n"
        "2. State whether any two magnetic field lines can ever cross each other, giving a brief reason [2]."
    )
    correct = f"From North pole out towards South pole ({arrow_dir_txt} here); Field lines NEVER cross because field direction at any point in space must be unique"
    sol = (
        f"**Step 1:** Outside a magnet, magnetic field arrows always point from **North (N) to South (S)** ({arrow_dir_txt}) [1].\n\n"
        "**Step 2:** Magnetic field lines **never intersect**, because a tiny compass needle placed at any point can only point in **one unique direction** [2]."
    )
    return _q(
        rng, "34", "34_magnetic_field_line_direction_north_to_south_flux_density", prompt, correct, sol, 3, "structured",
        ["drawing_external_field_lines_south_to_north_error"],
        "Follow a tiny plotting compass N-pointer: pushed away from N and pulled towards S!",
        "N -> S outside magnet; lines never cross.",
        correct, diagram_spec=spec,
    )


def arch_35_magnetic_field_pattern_unlike_poles_attracting(rng: random.Random) -> Dict[str, Any]:
    gap = rng.choice([2, 3, 4])
    prompt = (
        f"Two bar magnets lie collinearly **{gap} cm apart** with the **North pole** of Magnet A facing the **South pole** of Magnet B.\n\n"
        "Describe how iron filings arrange inside the gap between the facing opposite poles [2]."
    )
    correct = "Filings form smooth, continuous straight/curved bridges connecting directly out of Magnet A's North pole into Magnet B's South pole, demonstrating magnetic attraction."
    sol = (
        "**Step 1:** Between opposite poles (N facing S), field lines leave N and enter directly into S without turning away [1].\n\n"
        "**Step 2:** Iron filings form **continuous connecting lines bridging straight across the gap**, visually indicating **attraction** [1]."
    )
    return _q(
        rng, "35", "35_magnetic_field_pattern_unlike_poles_attracting", prompt, correct, sol, 2, "short_answer",
        ["drawing_repulsion_pattern_for_unlike_poles_error"],
        "N -> S connects smoothly across the gap!",
        "Continuous field lines bridge directly from N to S.",
        correct,
    )


def arch_36_magnetic_field_pattern_like_poles_repelling_neutral_point(rng: random.Random) -> Dict[str, Any]:
    pole = rng.choice(["N", "S"])
    spec = _svg_like_poles_repel(rng, pole)
    prompt = (
        "Inspect the magnetic field diagram where two magnets face each other closely.\n\n"
        f"1. State why field lines bend sharply sideways away from **Point X** in the middle gap between both **{pole}** poles [2].\n"
        "2. What would you observe at exact **Point X** if fine iron filings were sprinkled there? [1]"
    )
    correct = f"Both facing poles are identical ({pole}-{pole}), so like poles repel and deflect flux lines outward; Very few or zero iron filings settle right at the empty neutral null point X"
    sol = (
        f"**Step 1:** Because both facing ends are **{pole} poles**, the magnets **repel**, forcing field lines to curve sharply away from one another [2].\n\n"
        "**Step 2:** Opposing magnetic fields cancel at **Point X (neutral point)**, leaving a clear blank spot almost **free of iron filings** [1]."
    )
    return _q(
        rng, "36", "36_magnetic_field_pattern_like_poles_repelling_neutral_point", prompt, correct, sol, 3, "structured",
        ["expecting_dense_iron_filings_at_neutral_repulsion_gap_myth"],
        "Notice the field curves bending outward and leaving Point X empty in the centre.",
        "Like poles repel -> neutral null spot at X.",
        correct, diagram_spec=spec,
    )


def arch_37_earth_magnetic_field_geographic_north_and_compass_navigation(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Cape Town", "Durban", "Gqeberha", "Polokwane"])
    prompt = (
        f"A hiker near **{city}** checks a magnetic pocket compass, and its red **North-seeking pointer needle** turns to point toward geographic North.\n\n"
        "Explain the surprising polarity fact inside Earth's core responsible for attracting the compass needle's North pole northward [2]."
    )
    correct = "Since unlike magnetic poles attract, the region near Earth's geographic North Pole actually acts like a Magnetic SOUTH pole (attracting the compass needle's North pole)."
    sol = (
        "**Step 1:** Recall that **opposite poles attract** [1].\n\n"
        "**Step 2:** Because the **North pole** of a compass needle points towards Earth's geographic North, Earth's geographic North hemisphere behaves magnetically as a **Magnetic South Pole** [1]."
    )
    return _q(
        rng, "37", "37_earth_magnetic_field_geographic_north_and_compass_navigation", prompt, correct, sol, 2, "short_answer",
        ["claiming_geographic_north_is_magnetic_north_pole_myth"],
        "Wait: If a compass's N-tip is ATTRACTED northward, what magnetic pole must sit up there?",
        "Geographic North = Magnetic South pole (N attracts S!).",
        correct,
    )


def arch_38_earth_magnetosphere_protection_against_solar_wind_aurora(rng: random.Random) -> Dict[str, Any]:
    pole_light = rng.choice(["Aurora Australis (Southern Lights)", "Aurora Borealis (Northern Lights)"])
    prompt = (
        "The Sun continuously streams high-speed electrically charged particles called the **solar wind** towards Earth.\n\n"
        f"Explain how Earth's magnetic field (**magnetosphere**) protects life on Earth's surface and creates the glowing **{pole_light}** near the poles [2]."
    )
    correct = "Earth's magnetosphere deflects most dangerous charged solar-wind particles around our planet, funneling a fraction down polar field lines to excite upper-atmosphere gases into glowing auroras."
    sol = (
        "**Step 1:** Moving electric charges feel magnetic forces, so Earth's **magnetosphere** deflects dangerous solar radiation away from the equator and biosphere [1].\n\n"
        f"**Step 2:** Guided down polar magnetic field lines, particles collide with atmospheric oxygen/nitrogen to emit colourful **{pole_light}** [1]."
    )
    return _q(
        rng, "38", "38_earth_magnetosphere_protection_against_solar_wind_aurora", prompt, correct, sol, 2, "short_answer",
        ["ozone_layer_and_magnetosphere_exact_same_thing_myth"],
        "Magnetosphere deflects CHARGED solar particles (whereas ozone absorbs UV light).",
        "Deflects solar wind + funnels particles to poles -> auroras.",
        correct,
    )


def arch_39_electrostatic_charging_by_friction_electron_transfer(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("a polythene PVC ruler", "a dry woollen cloth", "negatively", "gains electrons from the cloth"),
        ("a Perspex rod", "a silk scarf", "positively", "loses electrons onto the silk scarf"),
    ])
    rod, cloth, sign, action = pair
    prompt = (
        f"A learner briskly rubs **{rod}** with **{cloth}**, leaving the rod **{sign} charged**.\n\n"
        "Explain microscopically how rubbing caused this static electric charge on the rod [2]."
    )
    correct = f"Friction transferred outer negatively charged electrons between the materials: the rod {action}, while protons remained locked inside atomic nuclei."
    sol = (
        f"**Step 1:** Rubbing supplies mechanical energy enabling mobile outer **electrons** to move across touching surfaces ({rod} {action}) [1].\n\n"
        "**Step 2:** **Protons** are locked tightly inside atomic nuclei and **never transfer** during friction charging [1]."
    )
    return _q(
        rng, "39", "39_electrostatic_charging_by_friction_electron_transfer", prompt, correct, sol, 2, "short_answer",
        ["protons_move_during_friction_charging_myth"],
        "ONLY outer electrons move during rubbing — positive protons stay fixed in the nucleus!",
        f"Friction transfers electrons: rod {action}.",
        correct,
    )


def arch_40_protons_fixed_in_nucleus_vs_mobile_outer_electrons_rule(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("an initially neutral glass rod acquires a +3 microcoulomb charge", "lost electrons"),
        ("an initially neutral rubber balloon acquires a negative charge", "gained extra electrons"),
    ])
    event, truth = scenario
    prompt = (
        f"Suppose **{event}** after rubbing against dry hair.\n\n"
        "Which subatomic statement accurately explains this charge state?"
    )
    correct = f"The object {truth}; positive protons remained completely stationary inside atomic nuclei."
    distractors = [
        "Positive protons jumped out of atomic nuclei onto the hair.",
        "Neutrons split inside the surface to create positive and negative charges from nothing.",
        "Charge is generated solely from air humidity freezing onto the surface.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Becoming positive means **losing electrons** (excess protons remain); becoming negative means **gaining electrons**.\n"
        f"**Step 2:** Therefore the object **{truth}** while nuclear protons never moved [2]."
    )
    return _q(
        rng, "40", "40_protons_fixed_in_nucleus_vs_mobile_outer_electrons_rule", prompt, correct, sol, 2, "multiple_choice",
        ["positive_charge_means_gaining_protons_myth"],
        "Positive object = deficit of electrons (electrons moved away!), NOT extra protons gained!",
        f"{truth}; protons stay locked in nucleus.",
        correct, options=options,
    )


def arch_41_triboelectric_pairs_perspex_silk_vs_polythene_wool(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("PVC/polythene rod + wool cloth", "PVC gains electrons (-) and wool becomes positive (+)"),
        ("Perspex/glass rod + silk cloth", "Perspex loses electrons (+) and silk becomes negative (-)"),
    ])
    combo, outcome = case
    prompt = (
        f"In standard Grade 9 triboelectric experiments, **{combo}** are rubbed vigorously together.\n\n"
        "1. Identify the resulting electric charge sign produced on BOTH objects after rubbing [2].\n"
        "2. State whether total combined charge across the isolated rod–cloth pair stayed zero (Law of Conservation of Charge) [1]."
    )
    correct = f"{outcome}; Yes — total net charge remains zero because equal and opposite charges are separated by electron transfer"
    sol = (
        f"**Step 1:** Resulting signs: **{outcome}** [2].\n\n"
        "**Step 2:** By **conservation of electric charge**, electrons are merely transferred (not created), so total net charge across both items together stays zero [1]."
    )
    return _q(
        rng, "41", "41_triboelectric_pairs_perspex_silk_vs_polythene_wool", prompt, correct, sol, 3, "structured",
        ["both_rubbed_objects_get_same_charge_sign_myth"],
        "Where do lost electrons go? Onto the partner object! So both end up with EQUAL and OPPOSITE charges.",
        f"{outcome}; total charge conserved.",
        correct,
    )


def arch_42_calculating_net_charge_from_proton_and_electron_counts(rng: random.Random) -> Dict[str, Any]:
    p_cnt = rng.randint(12, 22)
    diff = rng.choice([-4, -3, -2, 2, 3, 5])
    e_cnt = p_cnt - diff
    charge_val = f"+{diff}" if diff > 0 else f"{diff}"
    nature = "Positively charged" if diff > 0 else "Negatively charged"
    prompt = (
        f"A simplified particle diagram of an object counts **{p_cnt} protons** (+1 each) and **{e_cnt} electrons** (-1 each).\n\n"
        "Calculate the **net unit charge** of this object and classify it as positive, negative, or neutral [2]."
    )
    correct = f"Net charge = {charge_val}; {nature}"
    sol = (
        f"**Step 1:** $\\text{{Net charge}} = (+{p_cnt}) + (-{e_cnt}) = \\mathbf{{{charge_val}}}$ [1].\n\n"
        f"**Step 2:** Because there are {'more protons than electrons' if diff > 0 else 'more electrons than protons'}, the object is **{nature.lower()}** [1]."
    )
    return _q(
        rng, "42", "42_calculating_net_charge_from_proton_and_electron_counts", prompt, correct, sol, 2, "short_answer",
        ["subtracting_protons_from_electrons_sign_error"],
        "Add (+ protons) and (- electrons).",
        f"({p_cnt}) - ({e_cnt}) = {charge_val} -> {nature}.",
        correct,
    )


def arch_43_attraction_and_repulsion_between_charged_rods_and_balloons(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("two negatively charged Perspex/PVC balloons", "repel each other", "like charges"),
        ("a positively charged Perspex rod and a negatively charged ebonite rod", "attract each other", "opposite charges"),
        ("two positively charged glass rods", "repel each other", "like charges"),
    ])
    pair, result, rule = case
    prompt = (
        f"Two suspended insulated objects — **{pair}** — are brought close without touching.\n\n"
        "State whether they attract or repel and quote the **Electrostatic Charge Law** [2]."
    )
    correct = f"They {result}; Like charges repel and opposite (unlike) charges attract"
    sol = (
        f"**Step 1:** Because they carry **{rule}**, they **{result}** [1].\n\n"
        "**Step 2:** Fundamental electrostatic law: **Like charges repel; opposite charges attract** [1]."
    )
    return _q(
        rng, "43", "43_attraction_and_repulsion_between_charged_rods_and_balloons", prompt, correct, sol, 2, "short_answer",
        ["claiming_unlike_electric_charges_repel_error"],
        "Check whether the signs are the same (repel) or opposite (attract).",
        f"They {result}.",
        correct,
    )


def arch_44_electrostatic_induction_polarisation_of_neutral_paper_bits(rng: random.Random) -> Dict[str, Any]:
    rod = rng.choice(["negatively charged PVC comb", "positively charged Perspex ruler"])
    is_neg = "negatively" in rod
    prompt = (
        f"A **{rod}** is held 2 cm above tiny, electrically **neutral** torn paper confetti resting on a desk, causing the paper bits to jump upward and cling.\n\n"
        "Explain via **polarisation (charge separation)** why a charged rod attracts completely neutral paper bits [3]."
    )
    shift_desc = (
        "repels paper electrons slightly away toward the far edges, leaving the near paper surface positively polarised"
        if is_neg
        else "attracts mobile electrons slightly closer toward the near surface, leaving it negatively polarised"
    )
    correct = f"The {rod} induces polarisation in neutral paper: it {shift_desc}. Because the closer opposite-charge edge feels a stronger attractive pull than the farther like-charge edge feels repulsion, net upward electrostatic attraction lifts the paper."
    sol = (
        f"**Step 1:** Although the paper bits have equal + and - overall (neutral), the {rod} **{shift_desc}** [2].\n\n"
        "**Step 2:** Since opposite charges sit closer to the rod than like charges, attraction dominates over repulsion, pulling the light paper upward [1]."
    )
    return _q(
        rng, "44", "44_electrostatic_induction_polarisation_of_neutral_paper_bits", prompt, correct, sol, 3, "short_answer",
        ["thinking_paper_must_be_pre_charged_to_attract_myth"],
        "Remember charge separation (polarisation) puts the opposite charge closer to the charged rod!",
        f"Induced polarisation makes near surface attract strongly -> paper jumps up.",
        correct,
    )


def arch_45_gold_leaf_electroscope_detection_of_static_charge(rng: random.Random) -> Dict[str, Any]:
    sign = rng.choice(["-", "+"])
    spread = rng.randint(14, 24)
    spec = _svg_electroscope(rng, sign, spread)
    prompt = (
        "Inspect the gold-leaf electroscope diagram after a charged rod touches the metal cap.\n\n"
        "1. Explain why the thin gold leaves at the bottom swing outward and **diverge** apart [2].\n"
        "2. What happens to the diverged leaves if you touch the metal cap briefly with a bare finger? [1]"
    )
    ch_name = "negative (-)" if sign == "-" else "positive (+)"
    correct = f"Both leaves acquire the exact same {ch_name} charge and repel each other apart (like charges repel); The leaves collapse back together because your body earths/neutralises the excess charge"
    sol = (
        f"**Step 1:** Charge conducts down the brass stem into both leaves so both acquire identical **{ch_name} charge**; **like charges repel**, spreading the light leaves apart [2].\n\n"
        "**Step 2:** Touching the cap **earths** the electroscope through your body, neutralising excess charge so the leaves **collapse downward** [1]."
    )
    return _q(
        rng, "45", "45_gold_leaf_electroscope_detection_of_static_charge", prompt, correct, sol, 3, "structured",
        ["thinking_electroscope_leaves_repel_from_air_currents_myth"],
        "Both leaves get the SAME sign of charge conducted down the metal rod.",
        "Same charge on both leaves -> repel apart; earthing with finger -> collapses.",
        correct, diagram_spec=spec,
    )


def arch_46_earthing_grounding_path_neutralising_excess_static_charge(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("Aviation fuel tankers connect a thick copper earthing cable to the ground before refuelling aircraft at OR Tambo Airport.", "Equalises charge safely to Earth before a static spark could ignite fuel vapour."),
        ("Touching a metal staircase handrail after walking across synthetic carpet gives a sharp static zap.", "Excess charge stored on your body flows rapidly through a spark into the grounded metal to neutralise."),
    ])
    scene, exp = scenario
    prompt = (
        f"**Context:** *{scene}*\n\n"
        "Explain the physics of **earthing (grounding)** in this situation [2]."
    )
    correct = exp
    sol = (
        "**Step 1:** **Earthing** provides a conductive pathway connecting a charged object to Earth's huge reservoir [1].\n\n"
        f"**Step 2:** {exp} [1]."
    )
    return _q(
        rng, "46", "46_earthing_grounding_path_neutralising_excess_static_charge", prompt, correct, sol, 2, "short_answer",
        ["thinking_earthing_destroys_electric_charge_myth"],
        "Earth accepts or supplies electrons seamlessly to make any conductor electrically neutral.",
        exp,
        correct,
    )


def arch_47_van_de_graaff_generator_dome_charge_and_standing_hair(rng: random.Random) -> Dict[str, Any]:
    sign_note = rng.choice(["positive static charge", "high-voltage static charge"])
    prompt = (
        f"During a science demonstration, an insulated learner stands on a dry rubber mat with one hand resting on a **Van de Graaff generator** dome accumulating strong **{sign_note}**. Almost immediately, individual strands of the learner's dry hair stand straight outward!"
        "\n\nExplain why the hair strands spread apart in every direction, and why standing on the **rubber mat** is essential for the demo [3]."
    )
    correct = "Each hair strand acquires the same electric charge sign from the dome and repels every neighbouring strand apart; The insulating rubber mat prevents charge from leaking away to the ground (earthing)"
    sol = (
        "**Step 1:** Charge spreads over the learner's body and into every hair strand; because **all hair strands carry the same charge sign**, **like charges repel** violently outward [2].\n\n"
        "**Step 2:** The **rubber mat acts as an electrical insulator**, stopping static charge from draining directly down into the floor [1]."
    )
    return _q(
        rng, "47", "47_van_de_graaff_generator_dome_charge_and_standing_hair", prompt, correct, sol, 3, "structured",
        ["forgetting_why_insulator_stool_is_used_with_van_de_graaff"],
        "Two parts: (1) Why hair stands up (like charges), (2) Why stand on rubber/plastic instead of bare tile.",
        "Same charge makes hair strands repel; rubber insulates body from Earth.",
        correct,
    )


def arch_48_thundercloud_charge_separation_and_lightning_discharge_mechanism(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Johannesburg Highveld", "Pretoria", "Free State plains"])
    prompt = (
        f"Summer afternoon thunderstorms on the **{region}** produce dramatic flashes of **lightning**.\n\n"
        "Outline in 3 steps how static charges build up inside a storm cloud and finally discharge as a lightning bolt [3]."
    )
    correct = "1. Strong updrafts and friction between ice crystals/hailstones strip electrons separating positive upper cloud from negative lower cloud base; 2. Negative cloud base induces positive charge on Earth's ground below; 3. When electric attraction becomes extreme, air breaks down and giant electron discharge jumps between cloud and ground (or within clouds)."
    sol = (
        "**Step 1 (Charging by friction):** Rising warm winds collide hail and ice crystals inside cumulonimbus clouds, making cloud bottoms strongly **negative** and tops **positive** [1].\n\n"
        "**Step 2 (Ground induction):** The negative cloud base repels ground electrons, leaving ground objects beneath **positively** charged [1].\n\n"
        "**Step 3 (Electrostatic discharge):** Once voltage exceeds air's insulation, massive charge jumps across the air gap heating air violently (**lightning** + **thunder** shockwave) [1]."
    )
    return _q(
        rng, "48", "48_thundercloud_charge_separation_and_lightning_discharge_mechanism", prompt, correct, sol, 3, "structured",
        ["thinking_lightning_is_magnetic_force_myth"],
        "Trace friction (ice collisions) -> induction (ground below) -> sudden electrostatic spark discharge.",
        "Ice/water friction -> negative base induces positive ground -> giant spark discharge.",
        correct,
    )


def arch_49_lightning_conductor_earthing_protection_on_sa_buildings(rng: random.Random) -> Dict[str, Any]:
    building = rng.choice(["highveld thatched lodge", "rural school classroom block", "tall apartment tower"])
    prompt = (
        f"A tall **lightning conductor (lightning rod)** made of thick copper is mounted above a **{building}** and wired straight down into an underground metal plate.\n\n"
        "Explain how this metal rod protects the building and people inside from fire or fatal shock during a storm [2]."
    )
    correct = "Because copper is an excellent conductor reaching highest above the roof, lightning strikes the pointed rod first and flows safely down the thick cable directly into Earth without passing through walls or thatch."
    sol = (
        "**Step 1:** Its elevated pointed metal tip concentrates induced charge, intercepting the lightning channel before it hits flammable roofing [1].\n\n"
        "**Step 2:** Thick **copper** offers a low-resistance **earthing pathway**, guiding huge electric current harmlessly into soil instead of through wiring or occupants [1]."
    )
    return _q(
        rng, "49", "49_lightning_conductor_earthing_protection_on_sa_buildings", prompt, correct, sol, 2, "short_answer",
        ["thinking_lightning_rods_repel_lightning_away_into_space_myth"],
        "Does a lightning rod repel lightning away, or give it the safest conductive shortcut to Earth?",
        "Copper rod intercepts lightning and conducts current safely straight into the ground.",
        correct,
    )


def arch_50_thunderstorm_safety_precautions_south_african_highveld_rules(rng: random.Random) -> Dict[str, Any]:
    place = rng.choice(["standing under a lone tall acacia tree in an open veld", "holding a metal golf club on an open fairway", "swimming in an outdoor pool"])
    prompt = (
        f"While watching a fast-approaching South African thunderstorm, why is **{place}** extremely dangerous, and what is the **safest alternative shelter**? [2]"
    )
    correct = f"{place.capitalize()} makes you part of a tall/conductive strike or ground-current target; Shelter inside a solid enclosed brick/concrete building (away from plumbing/wired appliances) or an enclosed metal-roofed car (Faraday cage)."
    sol = (
        f"**Step 1:** **{place.capitalize()}** exposes you to direct strikes, side-flashes off tall trees, or dangerous ground voltage ripples [1].\n\n"
        "**Step 2:** Immediately move inside a **solid enclosed building** (avoid taps/landlines) or stay inside an **enclosed hard-top vehicle** with windows shut [1]."
    )
    return _q(
        rng, "50", "50_thunderstorm_safety_precautions_south_african_highveld_rules", prompt, correct, sol, 2, "short_answer",
        ["sheltering_under_tall_isolated_tree_in_storm_error"],
        "Never shelter under tall lone trees or water; choose enclosed buildings or enclosed metal cars!",
        "Avoid lone trees/water; shelter inside enclosed building or hard-top car.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_mass_vs_weight_linear_graph_gradient_analysis": arch_26_mass_vs_weight_linear_graph_gradient_analysis,
    "27_apparent_weightlessness_in_orbit_free_fall_explained": arch_27_apparent_weightlessness_in_orbit_free_fall_explained,
    "28_ferromagnetic_metals_iron_nickel_cobalt_and_steel": arch_28_ferromagnetic_metals_iron_nickel_cobalt_and_steel,
    "29_non_magnetic_metals_copper_aluminium_brass_and_plastics": arch_29_non_magnetic_metals_copper_aluminium_brass_and_plastics,
    "30_magnetic_poles_north_south_and_law_of_attraction_repulsion": arch_30_magnetic_poles_north_south_and_law_of_attraction_repulsion,
    "31_broken_bar_magnet_always_forms_new_north_south_dipoles": arch_31_broken_bar_magnet_always_forms_new_north_south_dipoles,
    "32_magnetic_field_acting_through_non_magnetic_materials": arch_32_magnetic_field_acting_through_non_magnetic_materials,
    "33_visualising_magnetic_field_lines_with_iron_filings": arch_33_visualising_magnetic_field_lines_with_iron_filings,
    "34_magnetic_field_line_direction_north_to_south_flux_density": arch_34_magnetic_field_line_direction_north_to_south_flux_density,
    "35_magnetic_field_pattern_unlike_poles_attracting": arch_35_magnetic_field_pattern_unlike_poles_attracting,
    "36_magnetic_field_pattern_like_poles_repelling_neutral_point": arch_36_magnetic_field_pattern_like_poles_repelling_neutral_point,
    "37_earth_magnetic_field_geographic_north_and_compass_navigation": arch_37_earth_magnetic_field_geographic_north_and_compass_navigation,
    "38_earth_magnetosphere_protection_against_solar_wind_aurora": arch_38_earth_magnetosphere_protection_against_solar_wind_aurora,
    "39_electrostatic_charging_by_friction_electron_transfer": arch_39_electrostatic_charging_by_friction_electron_transfer,
    "40_protons_fixed_in_nucleus_vs_mobile_outer_electrons_rule": arch_40_protons_fixed_in_nucleus_vs_mobile_outer_electrons_rule,
    "41_triboelectric_pairs_perspex_silk_vs_polythene_wool": arch_41_triboelectric_pairs_perspex_silk_vs_polythene_wool,
    "42_calculating_net_charge_from_proton_and_electron_counts": arch_42_calculating_net_charge_from_proton_and_electron_counts,
    "43_attraction_and_repulsion_between_charged_rods_and_balloons": arch_43_attraction_and_repulsion_between_charged_rods_and_balloons,
    "44_electrostatic_induction_polarisation_of_neutral_paper_bits": arch_44_electrostatic_induction_polarisation_of_neutral_paper_bits,
    "45_gold_leaf_electroscope_detection_of_static_charge": arch_45_gold_leaf_electroscope_detection_of_static_charge,
    "46_earthing_grounding_path_neutralising_excess_static_charge": arch_46_earthing_grounding_path_neutralising_excess_static_charge,
    "47_van_de_graaff_generator_dome_charge_and_standing_hair": arch_47_van_de_graaff_generator_dome_charge_and_standing_hair,
    "48_thundercloud_charge_separation_and_lightning_discharge_mechanism": arch_48_thundercloud_charge_separation_and_lightning_discharge_mechanism,
    "49_lightning_conductor_earthing_protection_on_sa_buildings": arch_49_lightning_conductor_earthing_protection_on_sa_buildings,
    "50_thunderstorm_safety_precautions_south_african_highveld_rules": arch_50_thunderstorm_safety_precautions_south_african_highveld_rules,
}
