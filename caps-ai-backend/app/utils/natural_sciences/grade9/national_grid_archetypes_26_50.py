"""Grade 9 Natural Sciences - Energy and the National Electricity Grid: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Energy and the national electricity grid.md.
Focus: Atomic structure & radioactive decay, nuclear fission vs fusion, Koeberg Nuclear Power Station,
reactor vessel/fuel rods/control rods/coolant, coal vs nuclear comparison, nuclear energy density,
Vaalputs & spent fuel waste storage, Chernobyl & Fukushima meltdowns, global nuclear % data, nuclear debate,
national electricity grid system & 4 stages, pylons & Al-steel cables, step-up & step-down transformers,
230 V domestic mains, P = VI current reduction, Joule heating P_loss = I^2*R, power surges, grid overloads,
sensitive circuit protection, and end-to-end grid synthesis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal number using South African comma notation."""
    if decimals == 0:
        return str(int(round(val)))
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
        "id": f"ns9_grid_{code}_{rng.randint(100000, 999999)}",
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


def _svg_atom_model(rng: random.Random, target_part: str, z_label: int) -> Dict[str, Any]:
    """Parameterized atomic structure diagram with callouts P, Q, R, S."""
    shift = rng.randint(-4, 4)
    svg = (
        f'<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Atomic Structure Model (Atomic Number Z = {z_label})</text>'
        f'<circle cx="210" cy="{110 + shift}" r="68" fill="#eff6ff" stroke="#93c5fd" stroke-dasharray="4,3" stroke-width="1.5"/>'
        f'<circle cx="210" cy="{110 + shift}" r="22" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>'
        f'<circle cx="202" cy="{104 + shift}" r="6" fill="#dc2626"/>'
        f'<text x="202" y="{107 + shift}" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>'
        f'<circle cx="218" cy="{106 + shift}" r="6" fill="#64748b"/>'
        f'<circle cx="210" cy="{119 + shift}" r="6" fill="#dc2626"/>'
        f'<text x="210" y="{122 + shift}" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>'
        f'<circle cx="152" cy="{82 + shift}" r="6" fill="#2563eb"/>'
        f'<text x="152" y="{85 + shift}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>'
        f'<circle cx="268" cy="{138 + shift}" r="6" fill="#2563eb"/>'
        f'<text x="268" y="{141 + shift}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>'
        f'<line x1="152" y1="{76 + shift}" x2="96" y2="52" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="86" y="54" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="end">P</text>'
        f'<line x1="202" y1="{98 + shift}" x2="112" y2="152" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="102" y="156" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="end">Q</text>'
        f'<line x1="218" y1="{106 + shift}" x2="316" y2="62" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="326" y="65" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="start">R</text>'
        f'<line x1="232" y1="{118 + shift}" x2="316" y2="162" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="326" y="166" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="start">S (Central Core)</text>'
        f'<text x="210" y="198" font-size="9.5" fill="#475569" text-anchor="middle">Identify particle/region {target_part}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_nuclear_fission(rng: random.Random, neutrons_out: int) -> Dict[str, Any]:
    """Parameterized nuclear fission reaction schematic for Uranium-235."""
    e_mev = rng.choice([200, 202, 205])
    svg = (
        f'<svg viewBox="0 0 435 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Induced Nuclear Reaction (~{e_mev} MeV Energy Released)</text>'
        f'<circle cx="48" cy="100" r="7" fill="#475569"/>'
        f'<text x="48" y="84" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Neutron</text>'
        f'<line x1="58" y1="100" x2="96" y2="100" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="96,100 88,96 88,104" fill="#0f172a"/>'
        f'<circle cx="132" cy="100" r="28" fill="#fca5a5" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="132" y="104" font-size="10.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">U-235</text>'
        f'<line x1="168" y1="100" x2="220" y2="100" stroke="#ea580c" stroke-width="2.5"/>'
        f'<polygon points="220,100 212,95 212,105" fill="#ea580c"/>'
        f'<circle cx="268" cy="64" r="18" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="268" y="68" font-size="9" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Ba</text>'
        f'<circle cx="268" cy="136" r="16" fill="#86efac" stroke="#15803d" stroke-width="2"/>'
        f'<text x="268" y="140" font-size="9" font-weight="bold" fill="#14532d" text-anchor="middle">Kr</text>'
        f'<text x="360" y="96" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">+ {neutrons_out} neutrons</text>'
        f'<text x="360" y="114" font-size="10" font-weight="bold" fill="#ea580c" text-anchor="middle">+ Heat &amp; Radiation</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_nuclear_plant(rng: random.Random, masked_part: str, mw: int) -> Dict[str, Any]:
    """Parameterized nuclear power station schematic with one masked component X."""
    lbl_ctrl = "Component X" if masked_part == "control_rods" else "Control Rods"
    lbl_sg = "Component X" if masked_part == "steam_gen" else "Steam Generator"
    lbl_dome = "Component X" if masked_part == "containment" else "Containment Dome"
    lbl_fuel = "Component X" if masked_part == "fuel_rods" else "Uranium Fuel Rods"
    svg = (
        f'<svg viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="220" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Nuclear Power Station Loop ({mw} MW)</text>'
        f'<path d="M 28 175 L 28 72 A 80 42 0 0 1 188 72 L 188 175 Z" fill="#f1f5f9" stroke="#475569" stroke-width="2.5"/>'
        f'<text x="108" y="46" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">{lbl_dome}</text>'
        f'<rect x="44" y="88" width="52" height="72" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<line x1="56" y1="74" x2="56" y2="122" stroke="#0f172a" stroke-width="3"/>'
        f'<line x1="70" y1="74" x2="70" y2="122" stroke="#0f172a" stroke-width="3"/>'
        f'<text x="70" y="148" font-size="7.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">{lbl_fuel}</text>'
        f'<text x="64" y="68" font-size="7.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl_ctrl}</text>'
        f'<rect x="118" y="88" width="54" height="72" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="145" y="128" font-size="8" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{lbl_sg}</text>'
        f'<line x1="172" y1="98" x2="245" y2="98" stroke="#0284c7" stroke-width="3"/>'
        f'<rect x="245" y="78" width="66" height="44" rx="4" fill="#e0f2fe" stroke="#0369a1" stroke-width="2"/>'
        f'<text x="278" y="104" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Turbine</text>'
        f'<line x1="311" y1="100" x2="342" y2="100" stroke="#0f172a" stroke-width="3"/>'
        f'<rect x="342" y="78" width="76" height="44" rx="4" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>'
        f'<text x="380" y="104" font-size="9.5" font-weight="bold" fill="#14532d" text-anchor="middle">Generator</text>'
        f'<text x="330" y="168" font-size="9" fill="#0369a1" text-anchor="middle">Condenser Cooling Water</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_nuclear_share_bars(rng: random.Random, target_country: str, year_tag: int) -> Dict[str, Any]:
    """Parameterized bar graph comparing nuclear electricity % share across selected nations."""
    data = [
        ("France", 75, "#2563eb"),
        ("Ukraine", 44, "#0ea5e9"),
        ("USA", 19, "#6366f1"),
        ("UK", 18, "#8b5cf6"),
        ("SA", 5, "#16a34a"),
    ]
    bars = []
    for i, (cntry, pct, fill) in enumerate(data):
        h = max(8, int((pct / 80.0) * 112))
        x = 68 + i * 70
        y = 162 - h
        bars.append(
            f'<rect x="{x}" y="{y}" width="40" height="{h}" fill="{fill}" stroke="#0f172a"/>'
            f'<text x="{x + 20}" y="{y - 5}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{pct}%</text>'
            f'<text x="{x + 20}" y="180" font-size="9.5" fill="#0f172a" text-anchor="middle">{cntry}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Nuclear Share of Electricity ({year_tag} Reference): Focus {target_country}</text>'
        f'<line x1="48" y1="36" x2="48" y2="162" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="48" y1="162" x2="405" y2="162" stroke="#0f172a" stroke-width="2"/>'
        f'{"".join(bars)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_grid_four_stages(rng: random.Random, labels: List[str], v_trans: int) -> Dict[str, Any]:
    """Parameterized 4-stage national electricity grid diagram."""
    names = ["Power Station", "Transmission Lines", "Substation", "Homes & Shops"]
    fills = ["#fee2e2", "#fef9c3", "#dbeafe", "#dcfce7"]
    elems = []
    for i in range(4):
        x = 18 + i * 105
        elems.append(
            f'<rect x="{x}" y="68" width="84" height="58" rx="6" fill="{fills[i]}" stroke="#0f172a" stroke-width="1.8"/>'
            f'<text x="{x + 42}" y="88" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{labels[i]}</text>'
            f'<text x="{x + 42}" y="108" font-size="8.5" fill="#334155" text-anchor="middle">{names[i]}</text>'
        )
        if i < 3:
            elems.append(
                f'<line x1="{x + 84}" y1="97" x2="{x + 105}" y2="97" stroke="#0f172a" stroke-width="2"/>'
                f'<polygon points="{x + 105},97 {x + 98},93 {x + 98},101" fill="#0f172a"/>'
            )
    svg = (
        f'<svg viewBox="0 0 435 170" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="170" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="24" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">National Electricity Grid Stages ({v_trans} kV Grid)</text>'
        f'{"".join(elems)}'
        f'<text x="217" y="150" font-size="9.5" fill="#475569" text-anchor="middle">Match Generation, Transmission, Distribution, and Consumers to {labels[0]}-{labels[3]}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_transformer_stage(rng: random.Random, is_step_up: bool, v1: str, v2: str, i1: str, i2: str) -> Dict[str, Any]:
    """Parameterized transformer block schematic showing input and output voltage/current."""
    col = "#dc2626" if is_step_up else "#2563eb"
    tag = "Grid Substation Transformer"
    svg = (
        f'<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="175" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{tag}</text>'
        f'<rect x="30" y="64" width="110" height="58" rx="5" fill="#f8fafc" stroke="#64748b"/>'
        f'<text x="85" y="88" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Input: {v1}</text>'
        f'<text x="85" y="106" font-size="9.5" fill="#334155" text-anchor="middle">Current: {i1}</text>'
        f'<line x1="140" y1="93" x2="165" y2="93" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="165" y="54" width="90" height="78" rx="6" fill="#fef3c7" stroke="{col}" stroke-width="2.5"/>'
        f'<text x="210" y="96" font-size="10.5" font-weight="bold" fill="{col}" text-anchor="middle">Transformer</text>'
        f'<line x1="255" y1="93" x2="280" y2="93" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="280" y="64" width="110" height="58" rx="5" fill="#f8fafc" stroke="#64748b"/>'
        f'<text x="335" y="88" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Output: {v2}</text>'
        f'<text x="335" y="106" font-size="9.5" fill="#334155" text-anchor="middle">Current: {i2}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_joule_scaling_bars(rng: random.Random, p_old_kw: int, k_factor: int) -> Dict[str, Any]:
    """Parameterized comparison bar chart for resistive heating loss before vs after current reduction."""
    p_new_kw = p_old_kw / float(k_factor * k_factor)
    h_old = 110
    h_new = max(5, int((p_new_kw / float(p_old_kw)) * 110))
    svg = (
        f'<svg viewBox="0 0 420 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Line Heat Loss Comparison (Current Reduced {k_factor}x)</text>'
        f'<line x1="60" y1="36" x2="60" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="165" x2="380" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="115" y="{165 - h_old}" width="64" height="{h_old}" fill="#ef4444" stroke="#0f172a"/>'
        f'<text x="147" y="{158 - h_old}" font-size="10" font-weight="bold" fill="#991b1b" text-anchor="middle">{p_old_kw} kW</text>'
        f'<text x="147" y="183" font-size="9.5" fill="#0f172a" text-anchor="middle">Low-V (I)</text>'
        f'<rect x="245" y="{165 - h_new}" width="64" height="{h_new}" fill="#22c55e" stroke="#0f172a"/>'
        f'<text x="277" y="{154 - h_new}" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">? kW</text>'
        f'<text x="277" y="183" font-size="9.5" fill="#0f172a" text-anchor="middle">High-V (I/{k_factor})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_end_to_end_grid(rng: random.Random, station: str, v_gen_kv: int, v_trans_kv: int, line_r: int) -> Dict[str, Any]:
    """Parameterized end-to-end national grid architecture for synthesis problem."""
    svg = (
        f'<svg viewBox="0 0 440 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="220" y="20" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{station} -&gt; National Grid -&gt; Domestic Consumer (230 V)</text>'
        f'<rect x="14" y="68" width="76" height="52" rx="4" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="52" y="91" font-size="8.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">{station}</text>'
        f'<text x="52" y="106" font-size="8.5" fill="#0f172a" text-anchor="middle">{v_gen_kv} kV</text>'
        f'<line x1="90" y1="94" x2="110" y2="94" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="110" y="68" width="76" height="52" rx="4" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="148" y="91" font-size="8.5" font-weight="bold" fill="#92400e" text-anchor="middle">Step-Up</text>'
        f'<text x="148" y="106" font-size="8.5" fill="#0f172a" text-anchor="middle">{v_trans_kv} kV</text>'
        f'<line x1="186" y1="94" x2="254" y2="94" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="5,3"/>'
        f'<text x="220" y="84" font-size="8.5" font-weight="bold" fill="#dc2626" text-anchor="middle">R = {line_r} ohm</text>'
        f'<rect x="254" y="68" width="78" height="52" rx="4" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="293" y="91" font-size="8.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Substation</text>'
        f'<text x="293" y="106" font-size="8.5" fill="#0f172a" text-anchor="middle">Step-Down</text>'
        f'<line x1="332" y1="94" x2="352" y2="94" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="352" y="68" width="74" height="52" rx="4" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="389" y="91" font-size="8.5" font-weight="bold" fill="#14532d" text-anchor="middle">Home</text>'
        f'<text x="389" y="106" font-size="8.5" fill="#0f172a" text-anchor="middle">230 V</text>'
        f'<text x="220" y="156" font-size="9" fill="#475569" text-anchor="middle">Transmission at {v_trans_kv} kV cuts I^2 R line heating before 230 V delivery</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_atomic_structure_nucleus_protons_neutrons_electrons(rng: random.Random) -> Dict[str, Any]:
    part_map = [
        ("P", "electron (negatively charged)", "surrounds the central nucleus in a diffuse electron cloud and carries a negative (-) charge"),
        ("Q", "proton (positively charged)", "resides inside the dense central nucleus and carries a positive (+) charge"),
        ("R", "neutron (uncharged)", "resides inside the dense central nucleus alongside protons and carries zero electrical charge"),
        ("S", "nucleus", "is the dense central core containing tightly packed protons and neutrons"),
    ]
    lbl, name, desc = rng.choice(part_map)
    z_val = rng.choice([6, 12, 92])
    spec = _svg_atom_model(rng, lbl, z_val)
    prompt = (
        f"Examine the atomic structure model (for an element with atomic number $Z = {z_val}$).\n\n"
        f"1. Identify subatomic feature **{lbl}** [1].\n"
        f"2. State its electrical charge and location within the atom [2]."
    )
    correct = f"{name.capitalize()}; It {desc}"
    sol = (
        f"**Step 1:** Label **{lbl}** points to the **{name}** [1].\n\n"
        f"**Step 2:** It {desc} [2]."
    )
    return _q(
        rng, "26", "26_atomic_structure_nucleus_protons_neutrons_electrons", prompt, correct, sol, 3, "short_answer",
        ["reversing_proton_and_electron_positions_in_atom"],
        "Remember: protons (+) and neutrons (0) sit in the dense nucleus; electrons (-) orbit outside.",
        f"{lbl} = {name}.",
        correct, diagram_spec=spec,
    )


def arch_27_unstable_nuclei_radioactivity_and_spontaneous_decay(rng: random.Random) -> Dict[str, Any]:
    elem = rng.choice(["Uranium", "Radium", "Thorium"])
    prompt = (
        f"Heavy elements such as **{elem}** have unstable atomic nuclei that spontaneously break down over time.\n\n"
        "What is meant by **radioactive decay**, and why does uranium make a reliable nuclear reactor fuel?"
    )
    correct = "An unstable nucleus spontaneously emits particles/radiation and transforms into another element of different mass; uranium undergoes radioactive decay slowly and sustains controlled energy release"
    distractors = [
        "Stable nuclei freeze into solid crystals and absorb all incoming sunlight.",
        "Electrons boil off copper atoms when heated by burning coal.",
        "Atoms multiply continuously into heavier elements with zero radiation emitted.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** **Radioactive** nuclei are unstable and spontaneously emit radiation particles, decaying into different atoms with altered mass.\n"
        f"**Step 2:** **{elem}** decays very slowly naturally yet undergoes controlled induced fission inside reactors [2]."
    )
    return _q(
        rng, "27", "27_unstable_nuclei_radioactivity_and_spontaneous_decay", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_radioactive_decay_is_chemical_burning"],
        "Focus on unstable nuclei emitting particles and changing into a different atom.",
        "Spontaneous particle/radiation emission by unstable nuclei; slow natural decay of uranium.",
        correct, options=options,
    )


def arch_28_nuclear_fission_splitting_heavy_uranium_nuclei(rng: random.Random) -> Dict[str, Any]:
    neutrons = rng.choice([2, 3])
    spec = _svg_nuclear_fission(rng, neutrons)
    prompt = (
        f"Study the nuclear reaction schematic producing **{neutrons} free neutrons**.\n\n"
        "1. Name the nuclear reaction shown when a neutron strikes a heavy Uranium-235 nucleus [1].\n"
        "2. Describe what happens to the uranium nucleus and state the two main forms of energy/output released besides daughter nuclei and neutrons [2]."
    )
    correct = f"Nuclear fission; The heavy Uranium-235 nucleus splits into two smaller nuclei, releasing huge thermal (heat) energy and dangerous nuclear radiation alongside {neutrons} neutrons"
    sol = (
        "**Step 1:** The reaction is **nuclear fission** [1].\n\n"
        f"**Step 2:** A neutron triggers the heavy U-235 nucleus to **split into two smaller nuclei** (e.g., Ba and Kr) plus {neutrons} neutrons, liberating vast amounts of **heat and radiation** [2]."
    )
    return _q(
        rng, "28", "28_nuclear_fission_splitting_heavy_uranium_nuclei", prompt, correct, sol, 3, "short_answer",
        ["confusing_nuclear_fission_splitting_with_fusion_joining"],
        "Look at whether one heavy nucleus is SPLITTING apart or two light nuclei are JOINING.",
        "Nuclear fission: splits heavy nucleus into smaller nuclei + huge heat and radiation.",
        correct, diagram_spec=spec,
    )


def arch_29_nuclear_fusion_vs_nuclear_fission_comparison(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["nuclear fusion", "nuclear fission"])
    is_fus = focus == "nuclear fusion"
    prompt = (
        "Commercial power stations and stars both release nuclear energy from atomic nuclei, yet through opposite processes.\n\n"
        f"Which statement accurately describes **{focus}**?"
    )
    fus_desc = "Two small light atomic nuclei are joined together at extreme temperature and pressure to form a larger nucleus, releasing enormous energy (as inside the Sun)."
    fis_desc = "A large unstable atomic nucleus (such as uranium) is split into two smaller nuclei, releasing huge amounts of heat and radiation inside nuclear power reactors."
    correct = fus_desc if is_fus else fis_desc
    other = fis_desc if is_fus else fus_desc
    options = [
        correct,
        other,
        "Burning pulverised fossil coal chemically with atmospheric oxygen inside a boiler.",
        "Passing high electric current through copper cables so electrons melt the wire.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** **Fusion** = fusing/joining light nuclei together; **Fission** = splitting a heavy nucleus apart.\n"
        f"**Step 2:** Therefore **{focus}** is: {correct} [2]."
    )
    return _q(
        rng, "29", "29_nuclear_fusion_vs_nuclear_fission_comparison", prompt, correct, sol, 2, "multiple_choice",
        ["swapping_definitions_of_nuclear_fission_and_fusion"],
        "Fission = split (like fissure); Fusion = fuse/join together.",
        correct, correct, options=options,
    )


def arch_30_koeberg_nuclear_power_station_location_and_cooling(rng: random.Random) -> Dict[str, Any]:
    cap_mw = rng.choice([900, 930, 1860])
    prompt = (
        f"South Africa operates only one commercial nuclear power station (generating up to **{cap_mw} MW** depending on active units) to supply electricity to the national grid.\n\n"
        "1. Name this nuclear power station and state its exact city/province location [2].\n"
        "2. State the primary cooling water source used by its condensers and explain why coastal siting is essential [1]."
    )
    correct = "Koeberg Nuclear Power Station, situated near Cape Town in the Western Cape; Cold Atlantic Ocean seawater cools the condenser steam loop continuously without depleting inland freshwater dams"
    sol = (
        "**Step 1:** **Koeberg Power Station**, located at Duynefontein just north of **Cape Town, Western Cape** [2].\n\n"
        "**Step 2:** Koeberg pumps cold **Atlantic Ocean seawater** through heat-exchanger condensers to cool secondary steam back into liquid water [1]."
    )
    return _q(
        rng, "30", "30_koeberg_nuclear_power_station_location_and_cooling", prompt, correct, sol, 3, "short_answer",
        ["locating_koeberg_in_mpumalanga_or_gauteng"],
        "Remember the only nuclear plant on the African continent sits on the Western Cape coast.",
        "Koeberg Nuclear Power Station, Cape Town (Western Cape); cooled by Atlantic Ocean seawater.",
        correct,
    )


def arch_31_nuclear_reactor_components_fuel_rods_control_rods_water(rng: random.Random) -> Dict[str, Any]:
    masked = rng.choice(["control_rods", "steam_gen", "containment", "fuel_rods"])
    mw = rng.choice([900, 930, 1800])
    info = {
        "control_rods": ("Control Rods", "absorb excess neutrons to regulate the speed of the nuclear fission chain reaction and shut down the core safely"),
        "steam_gen": ("Steam Generator (Heat Exchanger)", "transfers heat from pressurised primary reactor water to clean secondary water, boiling it into steam without mixing radioactive water into the turbine"),
        "containment": ("Containment Dome / Structure", "is a thick reinforced concrete and steel barrier that traps radioactive material inside if a pipe leak or accident occurs"),
        "fuel_rods": ("Uranium Fuel Rods", "hold uranium pellets inside the reactor core where controlled nuclear fission releases thermal energy"),
    }
    name, role = info[masked]
    spec = _svg_nuclear_plant(rng, masked, mw)
    prompt = (
        f"Inspect the pressurised water nuclear power station loop (**{mw} MW**).\n\n"
        "1. Identify **Component X** [1].\n"
        "2. Explain the safety or energy-transfer role performed by **Component X** [2]."
    )
    correct = f"{name}; {role.capitalize()}"
    sol = (
        f"**Step 1:** **Component X** represents the **{name}** [1].\n\n"
        f"**Step 2:** Function: it {role} [2]."
    )
    return _q(
        rng, "31", "31_nuclear_reactor_components_fuel_rods_control_rods_water", prompt, correct, sol, 3, "structured",
        ["thinking_radioactive_reactor_water_contacts_steam_turbine_directly"],
        "Check where Component X sits inside the reactor containment loop!",
        f"{name}: {role}.",
        correct, diagram_spec=spec,
    )


def arch_32_control_rods_and_coolant_preventing_reactor_meltdown(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("control rods are dropped all the way down between the uranium fuel rods", "control rods absorb neutrons rapidly, slowing and halting the nuclear fission chain reaction"),
        ("cooling water circulation around the uranium fuel bundle fails completely", "heat from continuing fission and decay cannot escape, causing fuel rods to overheat and undergo a partial or full meltdown"),
    ])
    event, consequence = scenario
    prompt = (
        "Inside a nuclear reactor core, bundles of uranium fuel pellet rods are submerged in water alongside movable **control rods**.\n\n"
        f"Explain physically what happens inside the reactor core if **{event}** [3]."
    )
    correct = f"{consequence.capitalize()} (preventing or risking catastrophic radiation release depending on heat removal)"
    sol = (
        "**Step 1:** Water removes intense fission heat and prevents fuel pellets from overheating; control rods govern neutron population [1].\n\n"
        f"**Step 2:** Therefore, if {event}, **{consequence}** [2]."
    )
    return _q(
        rng, "32", "32_control_rods_and_coolant_preventing_reactor_meltdown", prompt, correct, sol, 3, "short_answer",
        ["confusing_control_rods_with_uranium_fuel_rods"],
        "Think about the roles of circulating coolant water (heat removal) vs control rods (neutron absorption).",
        consequence.capitalize(),
        correct,
    )


def arch_33_coal_vs_nuclear_power_station_similarities_and_differences(rng: random.Random) -> Dict[str, Any]:
    coal_st = rng.choice(["Duvha", "Arnot", "Matimba", "Lethabo"])
    prompt = (
        f"Compare **{coal_st} Coal-Fired Power Station** with **Koeberg Nuclear Power Station**.\n\n"
        "1. State **one major mechanical similarity** in how both stations convert steam into electricity [1].\n"
        "2. Contrast their **heat sources** and **atmospheric greenhouse gas emissions** [3]."
    )
    correct = "Similarity: both heat water to make high-pressure steam that spins a turbine connected to an electromagnetic generator; Differences: coal stations burn fossil coal releasing CO2 and acid-rain gases, whereas nuclear reactors split uranium atoms via fission with zero CO2 emission during operation (though producing radioactive waste)"
    sol = (
        "**Step 1 (Similarity):** Both stations boil water into steam to drive a **steam turbine coupled to an electrical generator** [1].\n\n"
        f"**Step 2 (Differences):** {coal_st} burns **chemical coal**, emitting massive **$\\text{{CO}}_2$** and $\\text{{SO}}_2$ [1.5]; Koeberg uses **nuclear fission of uranium** to heat water with **zero greenhouse gas emissions** during generation, instead producing radioactive waste [1.5]."
    )
    return _q(
        rng, "33", "33_coal_vs_nuclear_power_station_similarities_and_differences", prompt, correct, sol, 4, "structured",
        ["claiming_nuclear_power_stations_burn_coal_or_emit_co2_from_cooling_towers"],
        "Both boil water -> steam -> turbine -> generator! Only HOW water is heated and the waste produced differ.",
        correct, correct,
    )


def arch_34_nuclear_energy_density_fuel_mass_comparison(rng: random.Random) -> Dict[str, Any]:
    uranium_kg = rng.choice([2, 3, 5, 8, 12])
    eq_coal_kg = uranium_kg * 1_000_000
    eq_coal_tonnes = eq_coal_kg // 1000
    prompt = (
        f"Nuclear fission releases approximately **1 000 000 times** as much energy per kilogram of fuel as burning fossil coal.\n\n"
        f"Calculate how many **tonnes of coal** ($1\\text{{ tonne}} = 1\\,000\\text{{ kg}}$) would have to be burned to release roughly the same energy as **{uranium_kg} kg** of nuclear uranium fuel [3]."
    )
    correct = f"{eq_coal_tonnes} tonnes"
    sol = (
        f"**Step 1:** Equivalent coal mass in kg: ${uranium_kg}\\text{{ kg}} \\times 1\\,000\\,000 = {eq_coal_kg}\\text{{ kg}}$ [2].\n\n"
        f"**Step 2:** Convert kg to tonnes: $\\frac{{{eq_coal_kg}}}{{1\\,000}} = \\mathbf{{{eq_coal_tonnes}\\text{{ tonnes}}}}$ [1]."
    )
    return _q(
        rng, "34", "34_nuclear_energy_density_fuel_mass_comparison", prompt, correct, sol, 3, "calculation",
        ["forgetting_to_convert_kilograms_to_tonnes"],
        "Multiply uranium mass in kg by 1 000 000, then divide by 1 000 kg per tonne.",
        f"{eq_coal_tonnes} tonnes of coal.",
        correct,
    )


def arch_35_radioactive_waste_disposal_vaalputs_and_spent_fuel_pools(rng: random.Random) -> Dict[str, Any]:
    waste_lvl = rng.choice([
        ("low- and intermediate-level radioactive waste (contaminated protective gear and tools)", "sealed inside steel-lined concrete drums and buried at Vaalputs National Radioactive Waste Disposal Facility in the arid Northern Cape"),
        ("high-level spent uranium fuel rods removed from the reactor core", "submerged deep underwater in on-site spent-fuel cooling pools for decades before transfer to sealed dry steel/concrete storage casks, guarded for thousands of years"),
    ])
    w_type, disposal = waste_lvl
    prompt = (
        "Unlike coal ash, radioactive waste from nuclear reactors cannot be dumped at municipal landfills because radioactivity decays safely only over thousands of years.\n\n"
        f"1. Describe South Africa's safe containment method for **{w_type}** [2].\n"
        "2. Give one security or cost concern linked to long-term radioactive waste storage [1]."
    )
    correct = f"{disposal.capitalize()}; Must be guarded indefinitely against environmental leakage and diversion to nuclear weapons manufacturing, adding major long-term cost"
    sol = (
        f"**Step 1:** Handling of {w_type}: **{disposal}** [2].\n\n"
        "**Step 2:** Requires multi-thousand-year geological isolation, continuous monitoring, and strict security so fissile material cannot reach weapons proliferators, driving up overall nuclear electricity costs [1]."
    )
    return _q(
        rng, "35", "35_radioactive_waste_disposal_vaalputs_and_spent_fuel_pools", prompt, correct, sol, 3, "structured",
        ["thinking_spent_nuclear_fuel_is_disposed_in_ordinary_municipal_landfills"],
        "Distinguish Vaalputs (Northern Cape low/intermediate waste) from on-site water pools & dry casks (high-level spent fuel).",
        disposal.capitalize(),
        correct,
    )


def arch_36_nuclear_meltdown_case_studies_chernobyl_and_fukushima(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        (
            "Chernobyl (1986, Ukraine)",
            "a reactor exploded, releasing 50 tonnes of radioactive material across forests and forcing 30 000 residents to evacuate while causing thousands of radiation-linked cancers",
        ),
        (
            "Fukushima-Daiichi (March 2011, Japan)",
            "a powerful earthquake and tsunami caused cooling water to leak from the reactors, leading to extreme overheating and a partial nuclear meltdown",
        ),
    ])
    event, cause_effect = case
    prompt = (
        "Critics of nuclear energy warn that reactor accidents carry catastrophic human and ecological consequences.\n\n"
        f"Which description accurately summarises the **{event}** nuclear disaster?"
    )
    correct = f"{cause_effect.capitalize()}."
    distractors = [
        "Hyperbolic cooling towers released harmless pure water vapour that briefly blocked local sunlight.",
        "Coal conveyor belts froze during winter snowstorms without emitting any radiation.",
        "A hydroelectric dam burst after heavy rain with zero radioactive substances involved.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** **{event}**: {cause_effect}.\n"
        "**Step 2:** Ionising radiation damages living animal and plant cells and contaminates surrounding land for decades [2]."
    )
    return _q(
        rng, "36", "36_nuclear_meltdown_case_studies_chernobyl_and_fukushima", prompt, correct, sol, 2, "multiple_choice",
        ["confusing_nuclear_meltdown_radiation_with_coal_smoke"],
        "Recall Chernobyl (1986 explosion) vs Fukushima (2011 earthquake/tsunami loss of cooling water).",
        correct, correct, options=options,
    )


def arch_37_global_nuclear_electricity_share_bar_chart_analysis(rng: random.Random) -> Dict[str, Any]:
    country, pct = rng.choice([("France", 75), ("Ukraine", 44), ("USA", 19), ("UK", 18)])
    year_tag = rng.choice([2013, 2018, 2022])
    diff = pct - 5
    spec = _svg_nuclear_share_bars(rng, country, year_tag)
    prompt = (
        f"Study the bar graph comparing nuclear electricity percentages across nations ({year_tag} reference).\n\n"
        f"1. Read South Africa's nuclear share and **{country}**'s nuclear share from the bars [2].\n"
        f"2. Calculate how many percentage points higher **{country}**'s nuclear share is than South Africa's [1]."
    )
    correct = f"SA: 5%, {country}: {pct}%; Difference = {diff} percentage points"
    sol = (
        f"**Step 1:** South Africa = **5%**; **{country}** = **{pct}%** [2].\n\n"
        f"**Step 2:** Difference: ${pct}\\% - 5\\% = \\mathbf{{{diff}\\text{{ percentage points}}}}$ [1]."
    )
    return _q(
        rng, "37", "37_global_nuclear_electricity_share_bar_chart_analysis", prompt, correct, sol, 3, "calculation",
        ["misreading_bar_heights_on_nuclear_share_chart"],
        f"Read the height above SA (5%) and {country} ({pct}%) and subtract.",
        f"SA = 5%, {country} = {pct}%, difference = {diff} percentage points.",
        correct, diagram_spec=spec,
    )


def arch_38_nuclear_energy_debate_advantages_vs_disadvantages(rng: random.Random) -> Dict[str, Any]:
    stance = rng.choice(["in favour of expanding", "opposed to expanding"])
    prompt = (
        f"South Africa faces an ongoing electricity supply challenge. In a formal science debate, your team argues **{stance}** nuclear power generation.\n\n"
        "1. Present **two verified scientific advantages** of nuclear power [2].\n"
        "2. Present **two verified disadvantages or risks** that critics raise [2]."
    )
    correct = "Advantages: zero greenhouse gas (CO2) emissions during operation and ultra-high fuel energy density (~1 million times coal per kg, independent of coal/oil prices); Disadvantages: dangerous high-level radioactive waste lasting thousands of years plus catastrophic meltdown risk and high storage/security costs"
    sol = (
        "**Step 1 (Advantages):** (1) Zero $\\text{CO}_2$ emissions during generation (no enhanced greenhouse effect); (2) enormous energy output from a tiny mass of uranium fuel [2].\n\n"
        "**Step 2 (Disadvantages):** (1) Produces long-lived radioactive waste requiring secure multi-millennia containment; (2) severe meltdown/radiation hazards and high capital/disposal costs [2]."
    )
    return _q(
        rng, "38", "38_nuclear_energy_debate_advantages_vs_disadvantages", prompt, correct, sol, 4, "structured",
        ["claiming_nuclear_energy_has_no_environmental_waste_problem"],
        "Include both atmospheric cleanliness/efficiency AND radioactive waste/meltdown risk.",
        "Pros: zero CO2 + huge energy density; Cons: long-lived radioactive waste + meltdown/cost risk.",
        correct,
    )


def arch_39_national_electricity_grid_as_an_interacting_system(rng: random.Random) -> Dict[str, Any]:
    event = rng.choice([
        "two large generating units in Mpumalanga suddenly trip offline",
        "a major 400 kV transmission corridor trips during a veld fire",
        "a regional substation suffers an abrupt grid overload",
    ])
    prompt = (
        f"Suppose **{event}**.\n\n"
        "Explain why South Africa's national electricity supply is classified as a **system (grid)**, and describe how a failure in one component affects the rest of the network [3]."
    )
    correct = "The national grid is a single closed, interconnected network of interacting power stations, transformers, transmission lines, substations, and consumers; A fault, drop in supply, or surge in one part alters current and voltage across the entire connected network, potentially causing widespread blackouts or load-shedding"
    sol = (
        "**Step 1:** A **system** consists of interconnected parts working together toward a single outcome — here delivering continuous power nationwide [1].\n\n"
        f"**Step 2:** Because all power lines form an interconnected closed grid, when {event}, voltage/frequency imbalances propagate across other links and can force protective cut-offs elsewhere [2]."
    )
    return _q(
        rng, "39", "39_national_electricity_grid_as_an_interacting_system", prompt, correct, sol, 3, "short_answer",
        ["treating_each_province_power_lines_as_isolated_from_national_grid"],
        "Ask: why do engineers call it a 'grid' instead of separate isolated lines?",
        "Interconnected interacting parts forming one closed system; a change in one part affects the whole network.",
        correct,
    )


def arch_40_four_stages_of_national_electricity_grid_schematic(rng: random.Random) -> Dict[str, Any]:
    labels = ["A", "B", "C", "D"]
    rng.shuffle(labels)
    v_trans = rng.choice([400, 765])
    spec = _svg_grid_four_stages(rng, labels, v_trans)
    prompt = (
        f"Inspect the national electricity grid schematic (**{v_trans} kV** transmission network).\n\n"
        "Match the four curriculum stages — **Generation**, **Transmission**, **Distribution**, and **Consumers** — to the letters **A, B, C, and D** in correct order from the power station to homes [4]."
    )
    correct = f"{labels[0]} = Generation; {labels[1]} = Transmission; {labels[2]} = Distribution; {labels[3]} = Consumers"
    sol = (
        f"**Step 1:** Power Station = **{labels[0]} (Generation)** [1].\n"
        f"**Step 2:** High-voltage pylons = **{labels[1]} (Transmission)** [1].\n"
        f"**Step 3:** Local Substation = **{labels[2]} (Distribution)** [1].\n"
        f"**Step 4:** Homes & Shops = **{labels[3]} (Consumers)** [1]."
    )
    return _q(
        rng, "40", "40_four_stages_of_national_electricity_grid_schematic", prompt, correct, sol, 4, "short_answer",
        ["swapping_transmission_and_distribution_stages_in_grid"],
        "Follow electricity outward: Power Station -> Long-distance lines -> Substation -> Homes.",
        correct, correct, diagram_spec=spec,
    )


def arch_41_transmission_lines_pylons_and_aluminium_steel_core_cables(rng: random.Random) -> Dict[str, Any]:
    kv = rng.choice([400, 765])
    prompt = (
        f"Overhead **{kv} kV** transmission lines spanning South Africa are held high above the ground by steel lattice **pylons**, using conductors built from **aluminium strands wrapped around a steel core** rather than solid copper.\n\n"
        "Why do grid engineers select aluminium with a steel core instead of solid copper?"
    )
    correct = "Aluminium is much lighter and cheaper than copper (reducing cable sag between distant pylons), while the central steel core adds high tensile strength so lines do not snap under wind or tension"
    distractors = [
        "Aluminium is an electrical insulator that blocks all current from flowing through pylons.",
        "Steel melts at room temperature to absorb lightning strikes before electricity flows.",
        "Copper is magnetic and sticks permanently to wooden utility poles.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Solid copper across hundreds of kilometres would be prohibitively heavy and expensive.\n"
        "**Step 2:** **Aluminium** provides low mass + good conductivity, while the **steel core** supplies mechanical tensile strength across wide pylon spans [2]."
    )
    return _q(
        rng, "41", "41_transmission_lines_pylons_and_aluminium_steel_core_cables", prompt, correct, sol, 2, "multiple_choice",
        ["claiming_transmission_cables_are_solid_copper_or_insulators"],
        "Think about weight (sagging between towers), cost, and mechanical strength against wind.",
        "Lightweight & cost-effective aluminium + high tensile strength steel core.",
        correct, options=options,
    )


def arch_42_step_up_vs_step_down_transformer_voltage_current_effect(rng: random.Random) -> Dict[str, Any]:
    is_up = rng.choice([True, False])
    if is_up:
        v1, v2, i1, i2 = "20 kV", "400 kV", "2 000 A", "100 A"
        kind = "step-up transformer"
        desc = "increases voltage from 20 kV to 400 kV while proportionally decreasing current from 2 000 A to 100 A"
    else:
        v1, v2, i1, i2 = "11 kV", "230 V", "10 A", "478 A"
        kind = "step-down transformer"
        desc = "decreases voltage from 11 kV down to 230 V while proportionally increasing available current"
    spec = _svg_transformer_stage(rng, is_up, v1, v2, i1, i2)
    prompt = (
        f"Examine the transformer stage changing **{v1}** ({i1}) at the input to **{v2}** ({i2}) at the output.\n\n"
        "Identify the type of transformer and describe its effect on voltage and current."
    )
    correct = f"A {kind}; it {desc}"
    other = "step-down transformer" if is_up else "step-up transformer"
    options = [
        correct,
        f"A {other}; it creates extra electrical energy from nothing inside iron coils.",
        "A direct-current chemical battery that converts steam into water.",
        "A mechanical fuse that permanently disconnects both voltage and current.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Comparing {v1} input vs {v2} output shows voltage {'increases' if is_up else 'decreases'}, so this is a **{kind}**.\n"
        f"**Step 2:** By $P = V \\cdot I$, stepping voltage {'up lowers' if is_up else 'down raises'} current proportionally [2]."
    )
    return _q(
        rng, "42", "42_step_up_vs_step_down_transformer_voltage_current_effect", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_step_up_transformer_increases_both_voltage_and_current"],
        "Check whether output voltage is higher (step-up) or lower (step-down) than input voltage!",
        correct, correct, options=options, diagram_spec=spec,
    )


def arch_43_grid_voltage_levels_generation_transmission_domestic_230v(rng: random.Random) -> Dict[str, Any]:
    line_kv = rng.choice([132, 400, 765])
    prompt = (
        f"Electricity flows along South African transmission lines at **{line_kv} kV** ({line_kv * 1000} V), yet appliances plugged into household wall sockets require only **220–240 V (standard 230 V)**.\n\n"
        "1. Explain how the grid safely lowers transmission voltage before it enters a suburban home [2].\n"
        f"2. State two dangerous consequences if **{line_kv} kV** were connected directly into a domestic wall socket [2]."
    )
    correct = f"Step-down transformers at municipal substations and local neighbourhood transformers lower voltage progressively down to 230 V; Direct {line_kv} kV would arc violently across air gaps, destroy/burn out appliance wiring, ignite electrical fires, and cause instant fatal electrocution"
    sol = (
        "**Step 1:** **Step-down transformers** at regional substations and local street/pole transformers reduce high voltage in stages to **230 V** [2].\n\n"
        f"**Step 2:** Direct {line_kv} kV would puncture household insulation, cause violent **electrical arcing / fires**, melt appliances, and deliver **fatal shock** [2]."
    )
    return _q(
        rng, "43", "43_grid_voltage_levels_generation_transmission_domestic_230v", prompt, correct, sol, 4, "short_answer",
        ["assuming_household_plugs_carry_400_kv_directly"],
        "Which transformer lowers voltage? And what happens when insulation fails under extreme voltage?",
        "Substation/local step-down transformers reduce to 230 V; direct kV causes arcing, fires, and fatal shock.",
        correct,
    )


def arch_44_power_equation_p_equals_vi_current_reduction_at_high_voltage(rng: random.Random) -> Dict[str, Any]:
    p_kw = rng.choice([400, 800, 1200, 2000])
    v_low = rng.choice([20, 25])
    v_high = rng.choice([200, 400])
    i_low = p_kw / float(v_low)
    i_high = p_kw / float(v_high)
    prompt = (
        f"A regional power line must transmit **{p_kw} kW** ($P = {p_kw * 1000}\\text{{ W}}$) of electrical power across the Karoo.\n\n"
        f"Using $I = \\frac{{P}}{{V}}$, calculate the transmission current at:\n"
        f"1. Generator voltage $V_1 = {v_low}\\text{{ kV}}$ ($V_1 = {v_low * 1000}\\text{{ V}}$) [2].\n"
        f"2. Stepped-up transmission voltage $V_2 = {v_high}\\text{{ kV}}$ ($V_2 = {v_high * 1000}\\text{{ V}}$) [2]."
    )
    correct = f"At {v_low} kV: {_fmt_num(i_low, 1)} A; At {v_high} kV: {_fmt_num(i_high, 1)} A"
    sol = (
        f"**Step 1:** At {v_low} kV: $I_1 = \\frac{{{p_kw * 1000}}}{{{v_low * 1000}}} = \\mathbf{{{_fmt_num(i_low, 1)}\\text{{ A}}}}$ [2].\n\n"
        f"**Step 2:** At {v_high} kV: $I_2 = \\frac{{{p_kw * 1000}}}{{{v_high * 1000}}} = \\mathbf{{{_fmt_num(i_high, 1)}\\text{{ A}}}}$ [2].\n\n"
        "Raising voltage dramatically lowers line current for the same transmitted power."
    )
    return _q(
        rng, "44", "44_power_equation_p_equals_vi_current_reduction_at_high_voltage", prompt, correct, sol, 4, "calculation",
        ["multiplying_p_and_v_instead_of_dividing_p_over_v"],
        "Rearrange P = V x I to get I = P / V (using watts and volts, or kW and kV consistently).",
        correct, correct,
    )


def arch_45_joule_heating_power_loss_formula_i_squared_r(rng: random.Random) -> Dict[str, Any]:
    r_ohm = rng.choice([4, 6, 8, 10])
    i_amp = rng.choice([50, 80, 100, 120])
    p_loss_w = (i_amp ** 2) * r_ohm
    p_loss_kw = p_loss_w / 1000.0
    prompt = (
        f"An overland transmission cable has a total resistance of **$R = {r_ohm}\\,\\Omega$** and carries an alternating current of **$I = {i_amp}\\text{{ A}}$**.\n\n"
        "1. Calculate the rate of electrical energy wasted as heat in the cable using $P_{\\text{loss}} = I^2 R$, giving your answer in **kilowatts (kW)** [3].\n"
        "2. Explain why engineers must minimise current $I$ along long transmission cables [1]."
    )
    correct = f"{_fmt_num(p_loss_kw, 1)} kW ({p_loss_w} W); Heating waste rises with the square of current (I^2), so lower current prevents large thermal energy waste"
    sol = (
        f"**Step 1:** $P_{{\\text{{loss}}}} = I^2 \\cdot R = ({i_amp})^2 \\times {r_ohm} = {p_loss_w}\\text{{ W}}$ [2].\n\n"
        f"**Step 2:** Convert to kW: $\\frac{{{p_loss_w}}}{{1\\,000}} = \\mathbf{{{_fmt_num(p_loss_kw, 1)}\\text{{ kW}}}}$ [1].\n\n"
        "**Step 3:** Because heat dissipation scales with $I^2$, lowering current saves vast electrical energy [1]."
    )
    return _q(
        rng, "45", "45_joule_heating_power_loss_formula_i_squared_r", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_square_current_in_i_squared_r"],
        "Square the current FIRST (I x I), then multiply by R, then divide by 1 000 for kW.",
        f"{_fmt_num(p_loss_kw, 1)} kW lost as heat.",
        correct,
    )


def arch_46_quadratic_current_scaling_effect_on_line_heating_losses(rng: random.Random) -> Dict[str, Any]:
    k_factor = rng.choice([2, 4, 5, 10])
    p_old = rng.choice([400, 800, 1000, 1200])
    p_new = p_old / float(k_factor * k_factor)
    spec = _svg_joule_scaling_bars(rng, p_old, k_factor)
    prompt = (
        f"Study the line heat loss bar comparison. When transmitted at low voltage, a cable loses **{p_old} kW** as resistive heat. "
        f"A step-up transformer increases voltage by a factor of **{k_factor}**, reducing current by a factor of **{k_factor}**.\n\n"
        f"1. By what factor does the resistive heat loss ($P_{{\\text{{loss}}}} = I^2 R$) decrease? [1]\n"
        f"2. Calculate the new heat loss **? kW** at high voltage [2]."
    )
    correct = f"Decreases by a factor of {k_factor ** 2}; New heat loss = {_fmt_num(p_new, 1)} kW"
    sol = (
        f"**Step 1:** Since $P_{{\\text{{loss}}}} \\propto I^2$, reducing current by a factor of {k_factor} lowers heat loss by $({k_factor})^2 = \\mathbf{{{k_factor ** 2}}}$ [1].\n\n"
        f"**Step 2:** $P_{{\\text{{new}}}} = \\frac{{{p_old}\\text{{ kW}}}}{{{k_factor ** 2}}} = \\mathbf{{{_fmt_num(p_new, 1)}\\text{{ kW}}}}$ [2]."
    )
    return _q(
        rng, "46", "46_quadratic_current_scaling_effect_on_line_heating_losses", prompt, correct, sol, 3, "calculation",
        ["dividing_line_loss_by_k_instead_of_k_squared"],
        "Remember P_loss depends on I SQUARED! Square the reduction factor before dividing.",
        f"Factor of {k_factor ** 2} reduction -> {_fmt_num(p_new, 1)} kW.",
        correct, diagram_spec=spec,
    )


def arch_47_power_surge_definition_and_causes_in_national_grid(rng: random.Random) -> Dict[str, Any]:
    cause_case = rng.choice([
        "a high-energy lightning strike near an overhead transmission line",
        "faulty household or substation wiring creating a brief short circuit",
        "massive industrial motors or heavy equipment switching on and off suddenly",
    ])
    prompt = (
        f"During an electrical event involving **{cause_case}**, a sudden **power surge** enters the distribution line.\n\n"
        "What happens electrically during a **power surge**?"
    )
    correct = "A sudden, brief spike in electrical voltage produces a sharp surge in electric current strength capable of damaging circuit wiring and components"
    distractors = [
        "Voltage smoothly falls to 0 V while water evaporates inside the copper cables.",
        "Coal pulverisers reverse spin and send raw coal dust into wall sockets.",
        "Transmission pylons turn into permanent magnets and stop alternating current forever.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** A **power surge** is a sudden jump in voltage somewhere in a circuit, driving a dangerous burst of high electric current.\n"
        f"**Step 2:** Common triggers include **{cause_case}** [2]."
    )
    return _q(
        rng, "47", "47_power_surge_definition_and_causes_in_national_grid", prompt, correct, sol, 2, "multiple_choice",
        ["confusing_power_surge_spike_with_voltage_blackout_drop"],
        "Think about what 'surge' means for voltage and resulting current strength.",
        correct, correct, options=options,
    )


def arch_48_grid_overload_cascading_blackout_and_protection_cutoffs(rng: random.Random) -> Dict[str, Any]:
    trigger = rng.choice([
        "excessive peak consumer heater demand exceeding substation transformer capacity",
        "a lightning-induced voltage surge sweeping down a 132 kV feeder line",
    ])
    prompt = (
        f"National grid monitoring points continuously scan for faults such as **{trigger}**.\n\n"
        "1. What automated protective action do grid circuit breakers take the moment a severe surge or grid overload is detected? [1]\n"
        "2. Explain why cutting off that local area prevents a broader national grid blackout [2]."
    )
    correct = "Automated circuit breakers immediately trip and disconnect electricity supply to the affected sector; Isolating the fault stops extreme currents and overloads from burning out expensive transformers and cascading across interconnected transmission lines"
    sol = (
        "**Step 1:** Grid protection switches **trip and cut off power** to the affected branch immediately [1].\n\n"
        "**Step 2:** Isolating the overloaded or surged zone shields substation transformers from catastrophic failure and stops a **domino/cascading blackout** across the interconnected grid [2]."
    )
    return _q(
        rng, "48", "48_grid_overload_cascading_blackout_and_protection_cutoffs", prompt, correct, sol, 3, "short_answer",
        ["assuming_grid_cutoffs_are_intended_to_destroy_appliances"],
        "Why isolate one overloaded link in an interconnected network? Think domino effect!",
        "Sensors cut supply to the faulted zone, protecting transformers and stopping cascading blackouts.",
        correct,
    )


def arch_49_protecting_sensitive_household_electronics_from_surges(rng: random.Random) -> Dict[str, Any]:
    device = rng.choice(["desktop computer", "smart television", "Wi-Fi fibre router", "gaming console"])
    prompt = (
        f"During thunderstorms or grid restoration after load-shedding, homeowners are advised to protect sensitive devices such as a **{device}**.\n\n"
        f"1. Explain scientifically why a **power surge** easily ruins a **{device}** [2].\n"
        "2. State two practical safety measures a household can apply to protect delicate electronics [2]."
    )
    correct = f"Sensitive microchip circuits inside a {device} are engineered for tiny currents; a power surge drives a sudden excessive current spike that overheats and melts delicate pathways; Use a certified surge-protector plug/adapter and unplug sensitive electronics during lightning storms or outages"
    sol = (
        f"**Step 1:** Delicate circuits in a **{device}** require very small currents; a surge pushes a massive current through thin microchip tracks, melting or shorting them out [2].\n\n"
        "**Step 2:** Connect devices through a **surge-protector multi-plug** (which diverts excess spike energy) or **unplug** equipment from wall sockets during electrical storms and before power switches back on [2]."
    )
    return _q(
        rng, "49", "49_protecting_sensitive_household_electronics_from_surges", prompt, correct, sol, 4, "short_answer",
        ["thinking_ordinary_extension_lead_stops_lightning_power_surges"],
        "Ask: why do microchips fail under high current, and what affordable plug-in or unplugging habit prevents damage?",
        "Tiny circuits melt under surge currents; use surge protectors or unplug during storms.",
        correct,
    )


def arch_50_national_grid_end_to_end_diagnostic_synthesis(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Koeberg Nuclear", "Duvha Coal", "Ingula Hydro"])
    v_gen = rng.choice([11, 20, 22])
    v_trans = rng.choice([400, 765])
    line_r = rng.choice([5, 8, 12])
    spec = _svg_end_to_end_grid(rng, station, v_gen, v_trans, line_r)
    prompt = (
        f"Analyse the end-to-end national electricity delivery chain starting from **{station} Power Station** (**{v_gen} kV**) across **{v_trans} kV** transmission cables (resistance **{line_r} $\\Omega$**) to a **230 V** household.\n\n"
        "1. State the exact energy conversion occurring inside the generator at the station [1].\n"
        f"2. Explain why a step-up transformer raises voltage from **{v_gen} kV** to **{v_trans} kV** before long-distance transmission [2].\n"
        "3. Explain the dual role of the neighbourhood substation and household surge protection at the **230 V** end [2]."
    )
    correct = f"Mechanical kinetic energy -> Electrical energy via electromagnetic induction; Raising voltage from {v_gen} kV to {v_trans} kV slashes transmission current (I = P/V), drastically reducing I^2 R resistive heat losses across the {line_r} ohm cables; The substation steps voltage down safely to 230 V for homes while surge protectors shield delicate appliances from voltage spikes"
    sol = (
        f"**Step 1:** Inside **{station}**'s generator, **mechanical kinetic energy** converts into **electrical energy** via electromagnetic induction [1].\n\n"
        f"**Step 2:** Stepping voltage up to **{v_trans} kV** reduces current $I = P/V$, which quadratically cuts Joule heat losses ($P_{{\\text{{loss}}}} = I^2 R$) across the {line_r} $\\Omega$ cables [2].\n\n"
        "**Step 3:** Substations step voltage down to **230 V** so household wiring/appliances do not arc or burn out, while surge protectors defend micro-electronics against lightning or switching voltage spikes [2]."
    )
    return _q(
        rng, "50", "50_national_grid_end_to_end_diagnostic_synthesis", prompt, correct, sol, 5, "structured",
        ["omitting_step_up_current_reduction_in_end_to_end_grid_explanation"],
        "Link all three parts: Generator induction -> Step-Up (I^2R loss saving) -> Step-Down to 230 V + surge protection.",
        correct, correct, diagram_spec=spec,
    )


BUILDERS_26_50 = {
    "26_atomic_structure_nucleus_protons_neutrons_electrons": arch_26_atomic_structure_nucleus_protons_neutrons_electrons,
    "27_unstable_nuclei_radioactivity_and_spontaneous_decay": arch_27_unstable_nuclei_radioactivity_and_spontaneous_decay,
    "28_nuclear_fission_splitting_heavy_uranium_nuclei": arch_28_nuclear_fission_splitting_heavy_uranium_nuclei,
    "29_nuclear_fusion_vs_nuclear_fission_comparison": arch_29_nuclear_fusion_vs_nuclear_fission_comparison,
    "30_koeberg_nuclear_power_station_location_and_cooling": arch_30_koeberg_nuclear_power_station_location_and_cooling,
    "31_nuclear_reactor_components_fuel_rods_control_rods_water": arch_31_nuclear_reactor_components_fuel_rods_control_rods_water,
    "32_control_rods_and_coolant_preventing_reactor_meltdown": arch_32_control_rods_and_coolant_preventing_reactor_meltdown,
    "33_coal_vs_nuclear_power_station_similarities_and_differences": arch_33_coal_vs_nuclear_power_station_similarities_and_differences,
    "34_nuclear_energy_density_fuel_mass_comparison": arch_34_nuclear_energy_density_fuel_mass_comparison,
    "35_radioactive_waste_disposal_vaalputs_and_spent_fuel_pools": arch_35_radioactive_waste_disposal_vaalputs_and_spent_fuel_pools,
    "36_nuclear_meltdown_case_studies_chernobyl_and_fukushima": arch_36_nuclear_meltdown_case_studies_chernobyl_and_fukushima,
    "37_global_nuclear_electricity_share_bar_chart_analysis": arch_37_global_nuclear_electricity_share_bar_chart_analysis,
    "38_nuclear_energy_debate_advantages_vs_disadvantages": arch_38_nuclear_energy_debate_advantages_vs_disadvantages,
    "39_national_electricity_grid_as_an_interacting_system": arch_39_national_electricity_grid_as_an_interacting_system,
    "40_four_stages_of_national_electricity_grid_schematic": arch_40_four_stages_of_national_electricity_grid_schematic,
    "41_transmission_lines_pylons_and_aluminium_steel_core_cables": arch_41_transmission_lines_pylons_and_aluminium_steel_core_cables,
    "42_step_up_vs_step_down_transformer_voltage_current_effect": arch_42_step_up_vs_step_down_transformer_voltage_current_effect,
    "43_grid_voltage_levels_generation_transmission_domestic_230v": arch_43_grid_voltage_levels_generation_transmission_domestic_230v,
    "44_power_equation_p_equals_vi_current_reduction_at_high_voltage": arch_44_power_equation_p_equals_vi_current_reduction_at_high_voltage,
    "45_joule_heating_power_loss_formula_i_squared_r": arch_45_joule_heating_power_loss_formula_i_squared_r,
    "46_quadratic_current_scaling_effect_on_line_heating_losses": arch_46_quadratic_current_scaling_effect_on_line_heating_losses,
    "47_power_surge_definition_and_causes_in_national_grid": arch_47_power_surge_definition_and_causes_in_national_grid,
    "48_grid_overload_cascading_blackout_and_protection_cutoffs": arch_48_grid_overload_cascading_blackout_and_protection_cutoffs,
    "49_protecting_sensitive_household_electronics_from_surges": arch_49_protecting_sensitive_household_electronics_from_surges,
    "50_national_grid_end_to_end_diagnostic_synthesis": arch_50_national_grid_end_to_end_diagnostic_synthesis,
}
