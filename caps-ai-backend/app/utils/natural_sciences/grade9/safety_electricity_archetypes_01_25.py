"""Grade 9 Natural Sciences - Safety with Electricity: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Safety with electricity.md and Syllabus.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt(val: float, decimals: int = 1) -> str:
    """Format a number using South African comma decimal notation."""
    if float(val).is_integer() and decimals == 0:
        return str(int(val))
    s = f"{val:.{decimals}f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".") if decimals > 1 else s
    return s.replace(".", ",")


def _q(
    rng: random.Random,
    code: str,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    sol: str,
    marks: int,
    qtype: str,
    tags: List[str],
    tier1: str,
    tier2: str,
    tier3: str,
    marking_points: Optional[List[Dict[str, Any]]] = None,
    options: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    pts = marking_points or [{"id": "mp_1", "desc": "Verified scientific concept and answer", "marks": marks, "editable": True}]
    schema = {
        "total_marks": marks,
        "marking_points": pts,
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    guide_lines = [f"- {p['desc']} [{p['marks']} mark(s)]" for p in pts]
    guide = "\n".join(guide_lines) + f"\n**Total: {marks} marks**"
    item: Dict[str, Any] = {
        "id": f"ns9_sfe_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
        "question_family_id": subskill,
        "title": title,
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
        "marking_schema": schema,
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


def _svg_parallel_house_branches(rng: random.Random, voltage: int, branches: List[tuple]) -> Dict[str, Any]:
    """Parameterized parallel house circuit with multiple branch appliances."""
    total_i = sum(b[1] for b in branches)
    row_svg = []
    for idx, (name, amps) in enumerate(branches):
        y = 52 + idx * 46
        row_svg.append(
            f'<line x1="75" y1="{y}" x2="155" y2="{y}" stroke="#0f172a" stroke-width="2"/>'
            f'<circle cx="163" cy="{y}" r="3.5" fill="#0f172a"/>'
            f'<line x1="166" y1="{y}" x2="188" y2="{y - 8}" stroke="#0f172a" stroke-width="2"/>'
            f'<circle cx="192" cy="{y}" r="3.5" fill="#0f172a"/>'
            f'<line x1="195" y1="{y}" x2="230" y2="{y}" stroke="#0f172a" stroke-width="2"/>'
            f'<rect x="230" y="{y - 14}" width="118" height="28" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>'
            f'<text x="289" y="{y + 4}" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{name} ({_fmt(amps, 1)} A)</text>'
            f'<line x1="348" y1="{y}" x2="395" y2="{y}" stroke="#0f172a" stroke-width="2"/>'
        )
    y_bot = 52 + (len(branches) - 1) * 46
    svg = (
        f'<svg viewBox="0 0 440 {y_bot + 50}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="{y_bot + 50}" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<line x1="75" y1="30" x2="75" y2="{y_bot}" stroke="#dc2626" stroke-width="2.5"/>'
        f'<line x1="395" y1="30" x2="395" y2="{y_bot}" stroke="#2563eb" stroke-width="2.5"/>'
        f'<rect x="18" y="65" width="44" height="44" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>'
        f'<text x="40" y="84" font-size="10" font-weight="bold" fill="#991b1b" text-anchor="middle">{voltage} V</text>'
        f'<text x="40" y="99" font-size="9.5" fill="#991b1b" text-anchor="middle">Mains</text>'
        f'<line x1="62" y1="87" x2="75" y2="87" stroke="#dc2626" stroke-width="2.5"/>'
        f'{"".join(row_svg)}'
        f'<text x="235" y="{y_bot + 34}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Parallel House Circuit | Total I = {_fmt(total_i, 1)} A</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_overloaded_multiplug(rng: random.Random, apps: List[tuple], total_i: float, limit_a: int) -> Dict[str, Any]:
    """Parameterized overloaded wall socket with multi-plug adapter."""
    y_base = 42
    lines = []
    for idx, (label, amps) in enumerate(apps):
        y = 35 + idx * 42
        lines.append(
            f'<line x1="175" y1="95" x2="230" y2="{y}" stroke="#dc2626" stroke-width="2.2"/>'
            f'<rect x="230" y="{y - 14}" width="175" height="28" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>'
            f'<text x="317" y="{y + 4}" font-size="10.5" font-weight="bold" fill="#9a3412" text-anchor="middle">{label}: {_fmt(amps, 1)} A</text>'
        )
    h = max(195, 45 + len(apps) * 44)
    svg = (
        f'<svg viewBox="0 0 430 {h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="{h}" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="20" y="65" width="75" height="60" rx="5" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
        f'<text x="57" y="92" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Wall Socket</text>'
        f'<text x="57" y="108" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">Max {limit_a} A</text>'
        f'<rect x="115" y="74" width="60" height="42" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="145" y="93" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Multi-plug</text>'
        f'<text x="145" y="107" font-size="9.5" fill="#991b1b" text-anchor="middle">{_fmt(total_i, 1)} A</text>'
        f'<line x1="95" y1="95" x2="115" y2="95" stroke="#0f172a" stroke-width="3"/>'
        f'{"".join(lines)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_short_circuit_bypass(rng: random.Random, volt: int, r_load: int, fault_label: str) -> Dict[str, Any]:
    """Circuit showing normal load bypassed by an accidental low-resistance path."""
    svg = (
        f'<svg viewBox="0 0 430 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="205" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="45" y="40" width="320" height="125" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="25" y="82" width="42" height="40" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="46" y="106" font-size="11" font-weight="bold" fill="#78350f" text-anchor="middle">{volt} V</text>'
        f'<rect x="160" y="25" width="90" height="30" rx="4" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="205" y="44" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Load ({r_load} Ω)</text>'
        f'<path d="M 140 40 L 140 105 L 270 105 L 270 40" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,3"/>'
        f'<circle cx="140" cy="40" r="4" fill="#dc2626"/>'
        f'<circle cx="270" cy="40" r="4" fill="#dc2626"/>'
        f'<text x="205" y="124" font-size="10.5" font-weight="bold" fill="#dc2626" text-anchor="middle">{fault_label}</text>'
        f'<text x="205" y="186" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Bypass Resistance ≈ 0,1 Ω (Short Circuit)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_house_wiring_plan(rng: random.Random, rooms: List[str], fuse_a: int) -> Dict[str, Any]:
    """Parallel house lighting plan with room switches, kitchen main switch, and main fuse."""
    room_boxes = []
    coords = [(30, 30, 175, 78), (225, 30, 175, 78), (30, 128, 175, 78), (225, 128, 175, 78)]
    for idx, rname in enumerate(rooms[:4]):
        x, y, w, h = coords[idx]
        bx, by = x + w // 2, y + 48
        room_boxes.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f8fafc" stroke="#64748b" stroke-width="1.8"/>'
            f'<text x="{x + 10}" y="{y + 18}" font-size="10.5" font-weight="bold" fill="#0f172a">{rname}</text>'
            f'<circle cx="{bx}" cy="{by}" r="11" fill="#fef08a" stroke="#ca8a04" stroke-width="1.8"/>'
            f'<line x1="{bx - 7}" y1="{by - 7}" x2="{bx + 7}" y2="{by + 7}" stroke="#854d0e" stroke-width="1.5"/>'
            f'<line x1="{bx + 7}" y1="{by - 7}" x2="{bx - 7}" y2="{by + 7}" stroke="#854d0e" stroke-width="1.5"/>'
            f'<text x="{bx + 26}" y="{by + 4}" font-size="9.5" fill="#334155">S{idx + 1}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 235" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="235" fill="#ffffff" stroke="#cbd5e1"/>'
        f'{"".join(room_boxes)}'
        f'<rect x="130" y="210" width="170" height="20" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="215" y="224" font-size="10" font-weight="bold" fill="#991b1b" text-anchor="middle">Main Switch + {fuse_a} A Fuse (Mains)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_steel_wool_fuse_rig(rng: random.Random, n_cells: int, r_val: float, current_a: float, status: str) -> Dict[str, Any]:
    """CAPS Making Your Own Fuse experimental setup circuit."""
    v_tot = _fmt(n_cells * 1.5, 1)
    sw_col = "#ef4444" if "melt" in status.lower() else "#475569"
    svg = (
        f'<svg viewBox="0 0 440 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="215" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="55" y="38" width="330" height="135" fill="none" stroke="#0f172a" stroke-width="2.2"/>'
        f'<rect x="170" y="22" width="100" height="32" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>'
        f'<text x="220" y="42" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">{n_cells} cells ({v_tot} V)</text>'
        f'<circle cx="55" cy="105" r="17" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="55" y="109" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">A</text>'
        f'<text x="82" y="109" font-size="10" font-weight="bold" fill="#1e40af">{_fmt(current_a, 1)} A</text>'
        f'<circle cx="385" cy="105" r="16" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="385" y="109" font-size="9.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Bulb</text>'
        f'<rect x="85" y="158" width="110" height="28" rx="3" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>'
        f'<text x="140" y="176" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Rheostat ({_fmt(r_val, 1)} Ω)</text>'
        f'<rect x="240" y="152" width="115" height="42" rx="3" fill="#e2e8f0" stroke="#64748b" stroke-width="1.6"/>'
        f'<line x1="252" y1="173" x2="343" y2="173" stroke="{sw_col}" stroke-width="3" stroke-dasharray="4,2"/>'
        f'<text x="297" y="189" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Steel wool on mat ({status})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_fuse_placement(rng: random.Random, is_parallel: bool, fuse_branch: str, fuse_a: int) -> Dict[str, Any]:
    """Series or parallel bulb circuit with fuse placed in main line or branch."""
    if not is_parallel:
        svg = (
            f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="430" height="190" fill="#ffffff" stroke="#cbd5e1"/>'
            f'<rect x="55" y="38" width="320" height="110" fill="none" stroke="#0f172a" stroke-width="2.2"/>'
            f'<rect x="175" y="24" width="80" height="26" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>'
            f'<text x="215" y="41" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">Battery (3 V)</text>'
            f'<rect x="33" y="75" width="44" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
            f'<text x="55" y="94" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Fuse {fuse_a}A</text>'
            f'<circle cx="145" cy="148" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
            f'<text x="145" y="152" font-size="9.5" font-weight="bold" fill="#854d0e" text-anchor="middle">B1</text>'
            f'<circle cx="285" cy="148" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
            f'<text x="285" y="152" font-size="9.5" font-weight="bold" fill="#854d0e" text-anchor="middle">B2</text>'
            f'<text x="215" y="176" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Series Circuit: {fuse_a} A Fuse in Main Path</text>'
            f'</svg>'
        )
    else:
        fx, fy = (130, 96) if "Branch 1" in fuse_branch else (130, 152)
        svg = (
            f'<svg viewBox="0 0 430 205" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="430" height="205" fill="#ffffff" stroke="#cbd5e1"/>'
            f'<rect x="65" y="34" width="300" height="120" fill="none" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="65" y1="96" x2="365" y2="96" stroke="#0f172a" stroke-width="2"/>'
            f'<rect x="175" y="21" width="80" height="25" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>'
            f'<text x="215" y="38" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Cell (1,5 V)</text>'
            f'<circle cx="255" cy="96" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
            f'<text x="255" y="100" font-size="9.5" font-weight="bold" fill="#854d0e" text-anchor="middle">B1</text>'
            f'<circle cx="255" cy="154" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
            f'<text x="255" y="158" font-size="9.5" font-weight="bold" fill="#854d0e" text-anchor="middle">B2</text>'
            f'<rect x="{fx - 26}" y="{fy - 12}" width="52" height="24" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
            f'<text x="{fx}" y="{fy + 4}" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Fuse {fuse_a}A</text>'
            f'<text x="215" y="190" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Parallel Circuit: {fuse_a} A Fuse in {fuse_branch}</text>'
            f'</svg>'
        )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_circuit_breaker_internal(rng: random.Random, rated_a: int, state: str) -> Dict[str, Any]:
    """Internal components of an electromagnetic circuit breaker (MCB)."""
    svg = (
        f'<svg viewBox="0 0 430 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="215" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="35" y="25" width="360" height="160" rx="8" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<text x="215" y="45" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Electromagnetic Circuit Breaker ({rated_a} A | {state})</text>'
        f'<rect x="60" y="88" width="60" height="34" rx="3" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.8"/>'
        f'<text x="90" y="109" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Contacts (A)</text>'
        f'<rect x="165" y="85" width="75" height="40" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>'
        f'<text x="202" y="109" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Electromagnet (B)</text>'
        f'<rect x="275" y="65" width="80" height="28" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>'
        f'<text x="315" y="83" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Iron Catch (C)</text>'
        f'<rect x="275" y="122" width="80" height="28" rx="3" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>'
        f'<text x="315" y="140" font-size="9.5" font-weight="bold" fill="#166534" text-anchor="middle">Spring (D)</text>'
        f'<line x1="120" y1="105" x2="165" y2="105" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="240" y1="95" x2="275" y2="79" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3,2"/>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_parallel_house_wiring_independent_appliances(rng: random.Random) -> Dict[str, Any]:
    room_a, room_b = rng.choice([
        ("kitchen fluorescent tube", "bedroom ceiling light"),
        ("lounge television socket", "bathroom heater light"),
        ("study desk lamp", "hallway passage light"),
        ("dining room chandelier", "garage workshop light"),
    ])
    prompt = (
        f"In a typical South African home, the **{room_a}** stops working when its filament burns out, "
        f"yet the **{room_b}** continues to shine brightly.\n\n"
        "How are domestic house circuits wired, and why does one broken appliance not switch off the rest of the home?"
    )
    correct = "Houses are wired in parallel circuits; each appliance sits on its own independent branch so breaking one branch leaves complete closed paths for all other branches."
    options = [
        correct,
        "Houses are wired in a single series loop so electricity jumps across empty air gaps when one bulb blows.",
        "Each room contains its own underground coal generator disconnected from the mains supply.",
        "Parallel circuits increase total circuit resistance until zero current enters the remaining bulbs.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Household lighting and wall socket circuits are connected in **parallel**.\n\n"
        f"**Step 2:** Because the {room_a} and {room_b} are on separate branches, an open switch or blown bulb in one branch only interrupts current in that branch; the remaining parallel branches stay closed and powered."
    )
    return _q(
        rng, "01", "01_parallel_house_wiring_independent_appliances",
        "Domestic Parallel Circuit Independence",
        prompt, correct, sol, 2, "mcq",
        ["thinking_house_wiring_is_series"],
        "Think about whether lights in different rooms depend on one single wire loop.",
        "Houses use parallel branches so each branch operates independently.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Identify parallel house wiring", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Explain independent current paths in other branches", "marks": 1, "editable": True},
        ],
        options=options,
    )


def arch_02_parallel_circuits_resistance_and_current_increase(rng: random.Random) -> Dict[str, Any]:
    voltage = rng.choice([220, 230, 240])
    i1 = round(rng.uniform(2.0, 5.0), 1)
    i2 = round(rng.uniform(3.0, 7.0), 1)
    i3 = round(rng.uniform(1.5, 4.5), 1)
    branches = [("Kettle", i1), ("Iron", i2), ("Toaster", i3)]
    rng.shuffle(branches)
    total_i = round(i1 + i2 + i3, 1)
    spec = _svg_parallel_house_branches(rng, voltage, branches)
    prompt = (
        f"Refer to the parallel house circuit schematic powered at **{voltage} V**.\n\n"
        f"1. State what happens to the **total resistance** and **total mains current** when more parallel appliances are switched on [2].\n"
        f"2. Calculate the **total current** drawn from the mains supply when all three branches operate simultaneously [2]."
    )
    correct = f"Total resistance decreases and total current increases; Total current = {_fmt(total_i, 1)} A"
    sol = (
        "**Step 1:** Adding resistors (appliances) in **parallel** creates extra paths for charge, so **total resistance decreases** and **total mains current increases** [2].\n\n"
        f"**Step 2:** $I_{{\\text{{total}}}} = I_1 + I_2 + I_3 = {_fmt(i1, 1)} + {_fmt(i2, 1)} + {_fmt(i3, 1)} = {_fmt(total_i, 1)}\\text{{ A}}$ [2]."
    )
    return _q(
        rng, "02", "02_parallel_circuits_resistance_and_current_increase",
        "Parallel Branches: Total Resistance & Current",
        prompt, correct, sol, 4, "calculation",
        ["thinking_adding_parallel_branches_increases_resistance"],
        "More parallel paths reduce overall opposition to flow; add branch currents.",
        f"Total R decreases; I_total = {_fmt(i1, 1)} + {_fmt(i2, 1)} + {_fmt(i3, 1)}.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Total resistance decreases & current increases", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Correct sum I_total = {_fmt(total_i, 1)} A", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_03_overloading_multiplug_adapter_fire_hazard(rng: random.Random) -> Dict[str, Any]:
    limit_a = 16
    apps = rng.sample([
        ("Electric Kettle", 9.0),
        ("Steam Iron", 6.5),
        ("Fan Heater", 8.5),
        ("Microwave", 5.5),
        ("Toaster", 4.5),
    ], 3)
    total_i = round(sum(a[1] for a in apps), 1)
    spec = _svg_overloaded_multiplug(rng, apps, total_i, limit_a)
    prompt = (
        f"Inspect the multi-plug adapter plugged into a single **{limit_a} A** bedroom wall socket.\n\n"
        f"1. Define **electrical overloading** [1].\n"
        f"2. Calculate the combined current drawn ({_fmt(total_i, 1)} A vs {limit_a} A limit) and explain how this leads to a **building fire** [3]."
    )
    correct = f"Adding too many parallel branches causes excessive current ({_fmt(total_i, 1)} A > {limit_a} A); wires overheat, melting plastic insulation and igniting nearby materials."
    sol = (
        "**Step 1:** **Overloading** occurs when too many high-power parallel appliances are connected to one socket or circuit branch [1].\n\n"
        f"**Step 2:** Combined current is ${_fmt(apps[0][1], 1)} + {_fmt(apps[1][1], 1)} + {_fmt(apps[2][1], 1)} = {_fmt(total_i, 1)}\\text{{ A}}$, which exceeds the **{limit_a} A** wall socket limit [1].\n\n"
        "**Step 3:** Excessive current generates intense **heat** inside the copper conductors, melting wire insulation and igniting a fire [2]."
    )
    return _q(
        rng, "03", "03_overloading_multiplug_adapter_fire_hazard",
        "Multi-Plug Overloading & Thermal Fire Risk",
        prompt, correct, sol, 4, "structured",
        ["multiplug_overloading_harmless_myth"],
        "Sum all branch currents and compare to 16 A; remember electric current produces heat.",
        f"Total = {_fmt(total_i, 1)} A > {limit_a} A -> wire heating -> melted insulation -> fire.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Definition of overloading (too many parallel branches)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total current ({_fmt(total_i, 1)} A) exceeds {limit_a} A limit", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Excessive heating melts insulation and starts fire", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_04_overloading_total_current_calculation_threshold(rng: random.Random) -> Dict[str, Any]:
    limit_a = rng.choice([15, 16, 20])
    i_a = round(rng.uniform(4.2, 7.8), 1)
    i_b = round(rng.uniform(5.0, 8.6), 1)
    i_c = round(rng.uniform(4.0, 6.5), 1)
    tot = round(i_a + i_b + i_c, 1)
    excess = round(tot - limit_a, 1)
    prompt = (
        f"A kitchen plug circuit protected at **{limit_a} A** supplies three appliances in parallel: "
        f"an urn drawing **{_fmt(i_a, 1)} A**, a toaster drawing **{_fmt(i_b, 1)} A**, and a waffle maker drawing **{_fmt(i_c, 1)} A**.\n\n"
        "Calculate the **total current** in the main cable and determine by how many amperes it **exceeds** the safe circuit limit [3]."
    )
    correct = f"{_fmt(tot, 1)} A total; exceeds the {limit_a} A limit by {_fmt(excess, 1)} A (overloaded)"
    sol = (
        f"**Step 1:** Sum parallel branch currents: $I_{{\\text{{total}}}} = {_fmt(i_a, 1)} + {_fmt(i_b, 1)} + {_fmt(i_c, 1)} = {_fmt(tot, 1)}\\text{{ A}}$ [2].\n\n"
        f"**Step 2:** Excess above safe limit: ${_fmt(tot, 1)} - {limit_a} = {_fmt(excess, 1)}\\text{{ A}}$ [1]. Because {_fmt(tot, 1)} A > {limit_a} A, the circuit is **overloaded**."
    )
    return _q(
        rng, "04", "04_overloading_total_current_calculation_threshold",
        "Overload Current Threshold Calculation",
        prompt, correct, sol, 3, "calculation",
        ["dividing_instead_of_adding_parallel_currents"],
        "In a parallel circuit, branch currents add together in the main cable.",
        f"I_total = {_fmt(i_a, 1)} + {_fmt(i_b, 1)} + {_fmt(i_c, 1)}; subtract {limit_a} A.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Total current = {_fmt(tot, 1)} A", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Exceeds limit by {_fmt(excess, 1)} A", "marks": 1, "editable": True},
        ],
    )


def arch_05_short_circuit_definition_and_unintended_low_resistance_path(rng: random.Random) -> Dict[str, Any]:
    cause = rng.choice([
        "frayed insulation lets bare live and neutral copper conductors touch inside a lamp cord",
        "a metal screwdriver bridges across two bare battery terminals",
        "water seeps across exposed plug terminals creating a direct bypass",
        "a chewed cable in a ceiling lets bare wires touch directly",
    ])
    prompt = (
        f"Suppose {cause}.\n\n"
        "Which scientific definition accurately describes a **short circuit**?"
    )
    correct = "An unintended electrical pathway of very low or almost zero resistance that bypasses the normal load, resulting in an excessive surge of electric current."
    options = [
        correct,
        "A very long extension cord that has too much resistance and dims a light bulb completely.",
        "An open switch that increases circuit resistance to infinity so zero electrons move.",
        "A normal household parallel circuit operating below 1 ampere.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** A **short circuit** is an accidental bypass path in an electric circuit with **very low resistance**.\n\n"
        "**Step 2:** Because resistance along the bypass approaches zero, current surges dangerously high."
    )
    return _q(
        rng, "05", "05_short_circuit_definition_and_unintended_low_resistance_path",
        "Short Circuit Definition & Low-Resistance Bypass",
        prompt, correct, sol, 2, "mcq",
        ["thinking_short_circuit_means_short_wire_length"],
        "'Short' refers to bypassing the load via a low-resistance path, not physical cord length.",
        "Unintended low-resistance pathway causing massive current surge.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Identify unintended low-resistance bypass pathway causing excessive current", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_06_short_circuit_current_surge_via_ohms_law(rng: random.Random) -> Dict[str, Any]:
    volt = rng.choice([12, 24, 230])
    r_load = rng.choice([12, 20, 46])
    r_fault = 0.1
    i_norm = round(volt / r_load, 2)
    i_fault = int(round(volt / r_fault))
    fault_label = rng.choice(["Bare wire bypass", "Accidental copper contact", "Damaged insulation bridge"])
    spec = _svg_short_circuit_bypass(rng, volt, r_load, fault_label)
    prompt = (
        f"Inspect the circuit schematic powered by a **{volt} V** source driving a **{r_load} Ω** load. "
        f"A fault ({fault_label}) creates a bypass path with resistance **$0{{,}}1\\ \\Omega$**.\n\n"
        f"Use Ohm's Law ($I = \\frac{{V}}{{R}}$) to calculate both the **normal operating current** and the **short-circuit fault current** [4]."
    )
    correct = f"Normal current = {_fmt(i_norm, 2)} A; Short-circuit current = {i_fault} A"
    sol = (
        f"**Step 1 (Normal Operation):** $I_{{\\text{{normal}}}} = \\frac{{{volt}}}{{{r_load}}} = {_fmt(i_norm, 2)}\\text{{ A}}$ [2].\n\n"
        f"**Step 2 (Short Circuit Fault):** $I_{{\\text{{fault}}}} = \\frac{{{volt}}}{{0{{,}}1}} = {i_fault}\\text{{ A}}$ [2].\n\n"
        f"Because resistance dropped drastically to $0{{,}}1\\ \\Omega$, current spiked to **{i_fault} A**."
    )
    return _q(
        rng, "06", "06_short_circuit_current_surge_via_ohms_law",
        "Short-Circuit Current Surge via Ohm's Law",
        prompt, correct, sol, 4, "calculation",
        ["thinking_short_circuit_reduces_current"],
        "Apply I = V / R separately for R_load and for R_bypass = 0,1 Ω.",
        f"I_norm = {volt} / {r_load}; I_fault = {volt} / 0,1.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Normal current = {_fmt(i_norm, 2)} A", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Short-circuit current = {i_fault} A", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_07_short_circuit_dangers_overheating_sparks_and_fire(rng: random.Random) -> Dict[str, Any]:
    appliance = rng.choice(["electric kettle base", "classroom extension reel", "cellphone charger cable", "hairdryer cord"])
    prompt = (
        f"An internal short circuit occurs inside a **{appliance}** while plugged into the wall socket.\n\n"
        "State **two major physical dangers** caused by the sudden extreme current surge during a short circuit [2]."
    )
    correct = "1) Rapid overheating of conductors melts plastic insulation and ignites fires; 2) Intense sparks/arcing can burn users or damage the appliance and supply wiring."
    sol = (
        "**Step 1:** The huge current surge rapidly converts electrical energy into **thermal energy (heat)** in the wires, melting insulation and starting an **electrical fire** [1].\n\n"
        "**Step 2:** Sudden electrical **sparks/arcing** can severely burn nearby people or destroy sensitive components [1]."
    )
    return _q(
        rng, "07", "07_short_circuit_dangers_overheating_sparks_and_fire",
        "Physical Dangers of Short Circuits",
        prompt, correct, sol, 2, "short_answer",
        ["underestimating_short_circuit_fire_risk"],
        "Consider what intense current does to wire temperature and bare contact points.",
        "Overheating / melted insulation / electrical fire and sparks / component damage.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Overheating / melting insulation / fire hazard", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Sparks / appliance damage / burn risk", "marks": 1, "editable": True},
        ],
    )


def arch_08_house_wiring_plan_design_independent_switches_and_mains(rng: random.Random) -> Dict[str, Any]:
    rooms = rng.choice([
        ["Bedroom 1", "Bedroom 2", "Lounge", "Kitchen"],
        ["Main Bedroom", "Bathroom", "Lounge", "Kitchen"],
        ["Study", "Guest Room", "Dining", "Kitchen"],
        ["Bedroom 1", "Bathroom", "Passage", "Kitchen"],
    ])
    fuse_a = rng.choice([5, 10, 15])
    spec = _svg_house_wiring_plan(rng, rooms, fuse_a)
    prompt = (
        f"Refer to the four-room house lighting layout ({', '.join(rooms)}) protected by a **{fuse_a} A** main fuse.\n\n"
        "1. Explain why each room switch (**S1–S4**) must be wired **in series with its own bulb** inside **parallel branches** [2].\n"
        "2. Explain where the **main switch** and **{fuse_a} A fuse** must be positioned in the circuit so they protect and isolate the entire house [2]."
    )
    correct = f"Each room bulb is on a parallel branch with its switch in series on that branch so rooms switch independently; the main switch and {fuse_a} A fuse sit in the main supply line before branches split."
    sol = (
        "**Step 1:** Parallel room branches allow independent lighting; placing switch S1–S4 in series within each room branch controls only that room's bulb [2].\n\n"
        f"**Step 2:** Placing the **main switch** and **{fuse_a} A fuse** on the single main supply trunk (in the Kitchen) ensures opening the main switch or blowing the fuse cuts power to all four rooms [2]."
    )
    return _q(
        rng, "08", "08_house_wiring_plan_design_independent_switches_and_mains",
        "House Wiring Design: Room Switches & Mains Fuse",
        prompt, correct, sol, 4, "structured",
        ["placing_room_switch_in_main_trunk_error"],
        "Individual control = switch inside branch; total house protection = device on main line.",
        f"Parallel room branches with individual branch switches; main switch + {fuse_a} A fuse in main trunk.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Parallel branches with series branch switches for independence", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Main switch & fuse on main trunk before branch split", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_09_main_switch_isolation_before_circuit_maintenance(rng: random.Random) -> Dict[str, Any]:
    task = rng.choice([
        "replacing a cracked ceiling light fitting",
        "tightening a loose wall-socket faceplate screw",
        "installing a new stove isolator switch",
        "replacing a damaged wall dimmer switch",
    ])
    prompt = (
        f"An electrician arrives at a house to begin **{task}**.\n\n"
        "What is the mandatory first action at the household distribution board before touching any conductors, and why?"
    )
    correct = "Switch OFF the Main Switch on the distribution board to completely isolate all live wires from the 230 V grid supply before working."
    options = [
        correct,
        "Switch ON every kettle in the house so voltage drops to zero volts.",
        "Wrap wet cloths around the ceiling bulb while leaving power turned on.",
        "Remove the wall meter box glass with a bare steel crowbar while live.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Always turn **OFF the Main Switch** on the distribution board (DB) before repairing house wiring.\n\n"
        "**Step 2:** Isolating the main supply disconnects the 230 V Live feed across all branches, preventing fatal electric shock."
    )
    return _q(
        rng, "09", "09_main_switch_isolation_before_circuit_maintenance",
        "Mains Isolation Before Electrical Maintenance",
        prompt, correct, sol, 2, "mcq",
        ["working_on_live_circuits_myth"],
        "How do you guarantee no voltage reaches any room wire before touching copper?",
        "Turn OFF the Main Switch on the distribution board.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Switch off Main Switch to isolate 230 V live supply", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_10_household_branch_fault_isolation_diagnosis(rng: random.Random) -> Dict[str, Any]:
    faulty = rng.choice(["Kitchen Plugs (20 A)", "Geyser Circuit (20 A)", "Bedroom Plugs (16 A)", "Garage Sockets (16 A)"])
    working = rng.choice(["Ceiling Lights (10 A)", "Passage Lights (10 A)"])
    i1 = rng.choice([10, 16, 20])
    spec = _svg_parallel_house_branches(rng, 230, [(faulty.split(" (")[0], 21.5), (working.split(" (")[0], 4.2)])
    prompt = (
        f"Refer to the two parallel household supply branches on the distribution board.\n\n"
        f"Suddenly, power to **{faulty}** stops working, yet **{working}** stay completely lit. "
        "Explain how separate parallel sub-circuits on a distribution board produce this selective isolation [3]."
    )
    correct = f"The distribution board feeds '{faulty}' and '{working}' via separate parallel sub-circuits with individual breakers; when the '{faulty}' breaker trips due to a fault, the '{working}' parallel branch stays energized."
    sol = (
        f"**Step 1:** Domestic distribution boards divide the home into distinct **parallel sub-circuits** (e.g. lights vs plugs vs geyser) [1].\n\n"
        f"**Step 2:** An overload or fault on **{faulty}** trips only its dedicated breaker, leaving **{working}** powered [2]."
    )
    return _q(
        rng, "10", "10_household_branch_fault_isolation_diagnosis",
        "Distribution Board Selective Branch Fault Isolation",
        prompt, correct, sol, 3, "structured",
        ["thinking_one_tripped_breaker_always_kills_whole_house"],
        "Consider why lights and plug sockets are wired on separate DB breakers.",
        "Separate parallel sub-circuits allow faulty branch isolation while others keep running.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Separate parallel DB sub-circuits", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Fault trips only that sub-circuit breaker while others remain live", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_11_fuse_definition_thin_low_melting_point_wire(rng: random.Random) -> Dict[str, Any]:
    alloy = rng.choice(["tin-lead alloy", "thin low-melting-point wire", "calibrated zinc-alloy strip", "thin fusible element"])
    prompt = (
        f"A cartridge safety device inside an older appliance contains a **{alloy}** enclosed in a glass or ceramic tube.\n\n"
        "Which statement accurately describes how a **fuse** protects a circuit?"
    )
    correct = "It contains a thin low-melting-point wire that heats up, melts, and breaks the circuit whenever current exceeds its safe rated limit."
    options = [
        correct,
        "It stores spare electrical charge like a battery to boost lamp brightness during power cuts.",
        "It consists of a thick iron bar that increases voltage whenever a short circuit begins.",
        "It can be flipped back ON with a toggle switch infinitely without replacing anything.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** A **fuse** is a one-time safety device containing a **thin wire with a low melting point**.\n\n"
        "**Step 2:** If current exceeds the fuse's rating, the thin wire heats up and **melts ('blows')**, opening the circuit to prevent fire."
    )
    return _q(
        rng, "11", "11_fuse_definition_thin_low_melting_point_wire",
        "Fuse Construction & Melting Mechanism",
        prompt, correct, sol, 2, "mcq",
        ["confusing_fuse_and_switch_reset"],
        "Remember what happens physically to the thin wire inside a fuse when excess current flows.",
        "Thin low-melting-point wire melts and breaks the circuit when current exceeds safe rating.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Identify melting mechanism breaking circuit on overcurrent", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_12_fuse_heating_effect_steel_wool_experiment_setup(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    r_val = rng.choice([10.0, 12.0, 15.0])
    curr = round((n_cells * 1.5) / r_val, 1)
    spec = _svg_steel_wool_fuse_rig(rng, n_cells, r_val, curr, "Intact")
    prompt = (
        f"Inspect the classroom 'Making Your Own Fuse' circuit setup powered by **{n_cells} cells** in series.\n\n"
        "State the specific **experimental role** of:\n"
        "1. The **ammeter** [1]\n"
        "2. The **torch light bulb** [1]\n"
        "3. The **variable resistor (rheostat)** [1]\n"
        "4. The thin strands of **steel wool** [1]"
    )
    correct = "1) Ammeter: measures exact current in amperes; 2) Bulb: visual indicator showing current flow; 3) Rheostat: varies resistance to control current; 4) Steel wool: acts as a model fuse that melts under excessive current."
    sol = (
        "**Step 1:** **Ammeter** measures exact circuit current ($I$) in amperes, even when current is too small to light the bulb [1].\n"
        "**Step 2:** **Light bulb** gives visual evidence of current flow via brightness [1].\n"
        "**Step 3:** **Variable resistor** adjusts total resistance to step current up or down [1].\n"
        "**Step 4:** **Steel wool** acts as a thin **model fuse** demonstrating heating and melting [1]."
    )
    return _q(
        rng, "12", "12_fuse_heating_effect_steel_wool_experiment_setup",
        "Model Steel-Wool Fuse Experiment Components",
        prompt, correct, sol, 4, "structured",
        ["confusing_ammeter_and_rheostat_roles"],
        "Think what each piece lets you measure, see, adjust, or melt.",
        "Ammeter = measure A; Bulb = visual glow; Rheostat = adjust R/I; Steel wool = melting fuse.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Ammeter role (measures current)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Bulb role (visual current indicator)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Variable resistor role (controls resistance/current)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Steel wool role (model fuse melting at high current)", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_13_steel_wool_fuse_variable_resistor_current_control(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([3, 4])
    v_tot = n_cells * 1.5
    r_high = rng.choice([15.0, 18.0, 20.0])
    r_low = rng.choice([1.5, 2.0, 3.0])
    i_high_r = round(v_tot / r_high, 2)
    i_low_r = round(v_tot / r_low, 1)
    spec = _svg_steel_wool_fuse_rig(rng, n_cells, r_low, i_low_r, "Glowing")
    prompt = (
        f"Refer to the steel-wool fuse investigation powered at **{_fmt(v_tot, 1)} V**. A learner slides the variable resistor from **{_fmt(r_high, 1)} Ω** down to **{_fmt(r_low, 1)} Ω**.\n\n"
        "1. Calculate how the current changes using $I = \\frac{{V}}{{R}}$ [2].\n"
        "2. Describe what is observed on the **ammeter**, **torch bulb**, and **steel wool strands** [2]."
    )
    correct = f"Current increases from {_fmt(i_high_r, 2)} A to {_fmt(i_low_r, 1)} A; ammeter reading rises, bulb glows brighter, and steel wool heats red-hot and melts."
    sol = (
        f"**Step 1:** At $R = {_fmt(r_high, 1)}\\ \\Omega$: $I = \\frac{{{_fmt(v_tot, 1)}}}{{{_fmt(r_high, 1)}}} = {_fmt(i_high_r, 2)}\\text{{ A}}$. "
        f"At $R = {_fmt(r_low, 1)}\\ \\Omega$: $I = \\frac{{{_fmt(v_tot, 1)}}}{{{_fmt(r_low, 1)}}} = {_fmt(i_low_r, 1)}\\text{{ A}}$ [2].\n\n"
        "**Step 2:** Decreasing resistance **increases current**, so the **ammeter reading rises**, the **bulb shines brighter**, and intense heating causes the **steel wool to glow and burn/melt through** [2]."
    )
    return _q(
        rng, "13", "13_steel_wool_fuse_variable_resistor_current_control",
        "Rheostat Resistance vs Heating Effect in Fuse",
        prompt, correct, sol, 4, "calculation",
        ["thinking_decreasing_resistance_decreases_current"],
        "Use I = V / R; remember current and resistance are inversely proportional at constant voltage.",
        f"I rises from {_fmt(i_high_r, 2)} A to {_fmt(i_low_r, 1)} A; steel wool melts.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Correct Ohm's Law calculation showing current increase", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Correct observations (ammeter rises, brighter bulb, wool melts)", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_14_fuse_post_melt_open_circuit_current_zero(rng: random.Random) -> Dict[str, Any]:
    device = rng.choice(["steel wool strand", "3 A glass cartridge fuse", "5 A plug fuse", "2 A instrument fuse"])
    prompt = (
        f"After excessive current flows through a series circuit, the **{device}** glows brightly, snaps, and melts.\n\n"
        "State what happens immediately to the **ammeter reading** and explain **why** in terms of circuit continuity [2]."
    )
    correct = "The ammeter reading drops immediately to 0 A because melting breaks the conductor, creating an open circuit with no continuous pathway for charge to flow."
    sol = (
        "**Step 1:** The ammeter reading drops to **0 A** (and any series bulb turns OFF) [1].\n\n"
        "**Step 2:** Melting creates an air gap (**open circuit**), removing the continuous conducting loop required for electrons to flow [1]."
    )
    return _q(
        rng, "14", "14_fuse_post_melt_open_circuit_current_zero",
        "Post-Melt Open Circuit & Zero Current",
        prompt, correct, sol, 2, "short_answer",
        ["thinking_current_still_flows_to_open_gap"],
        "Can electrons cross an air gap when the wire melts apart?",
        "Reading becomes 0 A because the circuit is broken (open circuit).",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Current drops to 0 A", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Open circuit / broken continuous conducting path", "marks": 1, "editable": True},
        ],
    )


def arch_15_fuse_safety_precautions_heat_resistant_mat_and_screen(rng: random.Random) -> Dict[str, Any]:
    hazard = rng.choice(["hot molten iron droplets and sparks", "incandescent glowing fragments", "brief flame bursts"])
    prompt = (
        f"During the steel-wool fuse demonstration, the thin iron strands can emit **{hazard}** as they burn apart.\n\n"
        "Which pair of laboratory precautions is essential when performing this demonstration?"
    )
    correct = "Place a heat-resistant ceramic tile or wooden block beneath the steel wool and position a protective safety screen between the wool and learners."
    options = [
        correct,
        "Hold the steel wool bare-handed over open paper notebooks to catch sparks.",
        "Soak the wooden bench in paraffin so the wool burns faster.",
        "Connect the steel wool directly into a 230 V wall socket without any rheostat.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Always rest the steel wool on a **heat-resistant mat** (ceramic tile or solid wood block) so hot embers do not scorch the bench.\n\n"
        "**Step 2:** Use a **protective safety screen** (and safety goggles) to shield learners from flying sparks."
    )
    return _q(
        rng, "15", "15_fuse_safety_precautions_heat_resistant_mat_and_screen",
        "Laboratory Precautions for Steel-Wool Fuse Test",
        prompt, correct, sol, 2, "mcq",
        ["ignoring_spark_and_heat_mat_precautions"],
        "How do we protect both the desk surface and learners' eyes from sparks?",
        "Heat-resistant tile/wood block underneath + safety screen.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Heat-resistant surface and protective safety screen", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_16_fuse_current_rating_selection_for_appliances(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("electric fan heater", 8.0, [3, 5, 10, 30], 10),
        ("electric kettle", 9.5, [3, 5, 13, 30], 13),
        ("television set", 0.8, [1, 3, 10, 13], 3),
        ("microwave oven", 5.4, [3, 5, 10, 20], 10),
        ("steam iron", 6.2, [3, 5, 10, 30], 10),
    ]
    app, amps, avail, best = rng.choice(cases)
    avail_str = ", ".join(f"{f} A" for f in avail)
    prompt = (
        f"A household **{app}** normally draws a steady operating current of **{_fmt(amps, 1)} A**.\n\n"
        f"Available cartridge fuses are: **{avail_str}**.\n"
        f"Select the **most suitable fuse rating** and justify why it must exceed **{_fmt(amps, 1)} A** without being excessively large [3]."
    )
    correct = f"{best} A; it is the smallest standard rating safely above {_fmt(amps, 1)} A, so normal current will not blow it, yet an overcurrent fault will melt it quickly."
    sol = (
        f"**Step 1:** Select **{best} A** [1].\n\n"
        f"**Step 2:** A fuse must be rated **just higher** than the normal **{_fmt(amps, 1)} A** running current so it survives normal use [1], "
        "yet blows promptly during a dangerous fault before wires overheat [1]."
    )
    return _q(
        rng, "16", "16_fuse_current_rating_selection_for_appliances",
        "Selecting Correct Appliance Fuse Rating",
        prompt, correct, sol, 3, "calculation",
        ["choosing_fuse_below_operating_current"],
        "Pick the first available fuse rating just above the operating current.",
        f"Next rating above {_fmt(amps, 1)} A is {best} A.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Select {best} A", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Justify exceeding operating current without huge headroom", "marks": 2, "editable": True},
        ],
    )


def arch_17_undersized_fuse_nuisance_blowing_analysis(rng: random.Random) -> Dict[str, Any]:
    app, run_a, small_a = rng.choice([
        ("electric fan heater", 8, 3),
        ("electric kettle", 9, 5),
        ("radiant heater", 10, 3),
        ("hairdryer", 6, 2),
    ])
    prompt = (
        f"A learner fits a **{small_a} A** fuse into a **{app}** that requires **{run_a} A** to operate normally.\n\n"
        f"Predict what will happen the moment the {app} is switched on, and explain why [2]."
    )
    correct = f"The {small_a} A fuse will melt ('blow') immediately and cut power because the normal {run_a} A operating current already exceeds the {small_a} A fuse limit."
    sol = (
        f"**Step 1:** The **{small_a} A** fuse melts immediately when switched on, so the {app} stops working [1].\n\n"
        f"**Step 2:** Because normal running current ($I = {run_a}\\text{{ A}}$) exceeds the fuse's ${small_a}\\text{{ A}}$ threshold, the thin wire overheats and breaks the circuit [1]."
    )
    return _q(
        rng, "17", "17_undersized_fuse_nuisance_blowing_analysis",
        "Consequence of Fitting an Undersized Fuse",
        prompt, correct, sol, 2, "short_answer",
        ["thinking_smaller_fuse_reduces_appliance_current"],
        f"Compare {run_a} A required by the appliance against the {small_a} A melt limit.",
        f"{run_a} A > {small_a} A -> fuse melts immediately.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Fuse blows/melts immediately", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Operating current ({run_a} A) exceeds {small_a} A limit", "marks": 1, "editable": True},
        ],
    )


def arch_18_oversized_fuse_or_nail_bypass_fire_hazard(rng: random.Random) -> Dict[str, Any]:
    sub = rng.choice([
        "a thick copper wire / steel nail",
        "a 30 A fuse in a 3 A lamp circuit",
        "a strip of aluminium foil wrapped over a blown glass fuse",
        "a heavy iron bolt bridging the fuse holder",
    ])
    prompt = (
        f"After a lamp fuse blows repeatedly, someone replaces it with **{sub}** so the lamp stays on.\n\n"
        "Why is this practice extremely dangerous?"
    )
    correct = "A huge fault current can flow without melting the oversized bypass, allowing the appliance cable to overheat, melt its insulation, and ignite a fire."
    options = [
        correct,
        "It reverses current direction so electrons flow backward into the wall socket.",
        "It makes the lamp consume zero electrical energy while glowing brighter.",
        "It raises resistance so high that electricity stops reaching the room.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Replacing a calibrated fuse with **{sub}** removes overcurrent protection.\n\n"
        "**Step 2:** During a fault, dangerously high current continues flowing through thin household flex without disconnecting, overheating cables and causing fires."
    )
    return _q(
        rng, "18", "18_oversized_fuse_or_nail_bypass_fire_hazard",
        "Hazard of Oversized Fuse or Metal Bypass",
        prompt, correct, sol, 2, "mcq",
        ["replacing_fuse_with_thick_wire_myth"],
        "Think what happens to the house flex wires if the fuse fails to melt during a fault.",
        "Excess current keeps flowing unstopped, overheating cables and starting fires.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Fault current not cut -> cable overheating & fire hazard", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_19_fuse_placement_series_main_branch_controls_all(rng: random.Random) -> Dict[str, Any]:
    fuse_a = rng.choice([2, 3, 5])
    spec = _svg_fuse_placement(rng, is_parallel=False, fuse_branch="Main", fuse_a=fuse_a)
    prompt = (
        f"Refer to the series circuit containing a 3 V battery, two bulbs (**B1** and **B2**), and a **{fuse_a} A** fuse placed in the main path.\n\n"
        "1. Predict what happens to **both** bulbs B1 and B2 if a current surge melts this fuse [1].\n"
        "2. Explain why placing a fuse in the **main path** of any circuit protects every downstream branch or component [2]."
    )
    correct = "Both B1 and B2 switch OFF immediately because all circuit current passes through the main path; breaking it cuts supply to the entire circuit."
    sol = (
        "**Step 1:** Both **B1 and B2** extinguish immediately [1].\n\n"
        "**Step 2:** In a series circuit (or the main feed trunk before parallel branches), 100% of the current flows through the fuse; melting it opens the entire circuit [2]."
    )
    return _q(
        rng, "19", "19_fuse_placement_series_main_branch_controls_all",
        "Main-Path Fuse Placement in Series Circuits",
        prompt, correct, sol, 3, "structured",
        ["thinking_one_series_bulb_stays_lit_after_fuse_blows"],
        "Trace the single path from the battery through the fuse to B1 and B2.",
        "Both bulbs go OFF because the main path is broken.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Both B1 and B2 turn off", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "All current passes through main path so breaking it isolates everything", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_20_fuse_placement_parallel_individual_branch_isolation(rng: random.Random) -> Dict[str, Any]:
    fuse_branch = rng.choice(["Branch 1 (B1)", "Branch 2 (B2)"])
    lit_bulb = "B2" if "Branch 1" in fuse_branch else "B1"
    off_bulb = "B1" if "Branch 1" in fuse_branch else "B2"
    fuse_a = rng.choice([3, 5])
    spec = _svg_fuse_placement(rng, is_parallel=True, fuse_branch=fuse_branch, fuse_a=fuse_a)
    prompt = (
        f"Inspect the parallel circuit where a **{fuse_a} A** fuse is installed specifically inside **{fuse_branch}**.\n\n"
        f"1. State which bulb turns **OFF** and which bulb stays **ON** if this fuse melts [2].\n"
        f"2. Explain how this differs from placing the fuse in the main battery wire [1]."
    )
    correct = f"{off_bulb} switches OFF while {lit_bulb} stays ON; a branch fuse isolates only its own parallel branch, whereas a main-wire fuse shuts off the entire circuit."
    sol = (
        f"**Step 1:** **{off_bulb}** goes **OFF** because its branch is broken, while **{lit_bulb}** stays **ON** because its parallel path remains closed to the cell [2].\n\n"
        "**Step 2:** Placing the fuse in the main wire before the junction would disconnect both bulbs simultaneously [1]."
    )
    return _q(
        rng, "20", "20_fuse_placement_parallel_individual_branch_isolation",
        "Branch-Specific Fuse Placement in Parallel Circuits",
        prompt, correct, sol, 3, "structured",
        ["thinking_branch_fuse_cuts_all_parallel_branches"],
        "Trace whether the other parallel branch still forms a complete loop with the cell.",
        f"{off_bulb} OFF, {lit_bulb} ON; branch fuse isolates only that branch.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"{off_bulb} OFF and {lit_bulb} ON", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Contrast with main-wire placement shutting off all bulbs", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_21_fuse_vs_circuit_breaker_reusability_and_convenience(rng: random.Random) -> Dict[str, Any]:
    setting = rng.choice(["modern home distribution board", "school science block DB", "apartment electricity panel", "clinic sub-board"])
    prompt = (
        f"A **{setting}** uses miniature circuit breakers (MCBs) instead of older glass or porcelain fuses.\n\n"
        "What is the main operational advantage of a **circuit breaker** over a traditional **fuse**?"
    )
    correct = "A fuse melts and is destroyed after one fault so it must be replaced, whereas a circuit breaker trips open like a switch and can simply be reset once the fault is repaired."
    options = [
        correct,
        "A circuit breaker uses no moving parts and melts into liquid copper every week.",
        "A fuse automatically resets itself within two seconds without cutting current.",
        "A circuit breaker eliminates the need for insulation on household wires.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** When a **fuse** blows, its internal metal wire melts and must be discarded and replaced.\n\n"
        "**Step 2:** A **circuit breaker** is a reusable magnetic/thermal switch that trips open during an overload and can be **reset** back on once the fault is fixed."
    )
    return _q(
        rng, "21", "21_fuse_vs_circuit_breaker_reusability_and_convenience",
        "Fuses vs Circuit Breakers: Reusability",
        prompt, correct, sol, 2, "mcq",
        ["thinking_fuses_can_be_reset_without_replacement"],
        "Think about what happens after a fault: which device is thrown away vs flipped back on?",
        "Fuses melt and need replacement; circuit breakers can be reset.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Contrast single-use melting fuse vs resettable breaker", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_22_fault_diagnosis_before_replacing_fuse_or_resetting(rng: random.Random) -> Dict[str, Any]:
    event = rng.choice([
        "plugging in an old electric iron",
        "switching on a damp outdoor floodlight",
        "turning on a kettle with a frayed cord",
        "plugging in a damaged microwave oven",
    ])
    prompt = (
        f"A household fuse blows (or circuit breaker trips) immediately upon **{event}**.\n\n"
        "Why must the underlying electrical fault be identified and repaired **before** replacing the fuse or resetting the breaker [2]?"
    )
    correct = "If the fault remains, the excessive fault current will recur immediately—blowing the new fuse or tripping the breaker again—and creates a severe fire and electric shock risk."
    sol = (
        "**Step 1:** Safety devices react to a symptom (overcurrent or short circuit); resetting does not fix a damaged wire or faulty appliance [1].\n\n"
        "**Step 2:** Restoring power while the fault persists immediately triggers another hazardous current surge, risking electric shock, sparks, or fire [1]."
    )
    return _q(
        rng, "22", "22_fault_diagnosis_before_replacing_fuse_or_resetting",
        "Fixing Faults Before Resetting Breakers or Fuses",
        prompt, correct, sol, 2, "short_answer",
        ["resetting_breaker_fixes_appliance_myth"],
        "Does replacing a fuse repair a broken cord inside an appliance?",
        "Unfixed fault causes immediate re-trip/re-blow and poses shock/fire danger.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "New fuse/breaker will immediately trip/blow again", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Risk of electric shock, overheating, or fire", "marks": 1, "editable": True},
        ],
    )


def arch_23_electromagnet_principle_in_circuit_breaker(rng: random.Random) -> Dict[str, Any]:
    trip_a = rng.choice([15, 20, 25, 30])
    prompt = (
        f"Inside a **{trip_a} A** circuit breaker, mains current passes through a coil wrapped around an iron core.\n\n"
        "How does the magnetic force inside this **electromagnet** respond as circuit current rises sharply above normal limits?"
    )
    correct = f"Magnetic strength is directly proportional to current; when current surges past {trip_a} A, the electromagnet grows strong enough to pull the iron catch open and break the circuit."
    options = [
        correct,
        "Higher current turns off magnetism completely so gravity drops the switch closed.",
        "Electromagnet strength stays permanently constant regardless of how many amperes flow.",
        "Excess current turns the plastic casing into a permanent magnet that attracts lightning.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** An **electromagnet** is formed when electric current flows around a metal core; its magnetic strength increases as current increases.\n\n"
        f"**Step 2:** Above **{trip_a} A**, the amplified magnetic pull overcomes the latch force, tripping the switch open."
    )
    return _q(
        rng, "23", "23_electromagnet_principle_in_circuit_breaker",
        "Electromagnet Strength vs Current in Breakers",
        prompt, correct, sol, 2, "mcq",
        ["thinking_electromagnet_strength_is_independent_of_current"],
        "Recall the relationship between current magnitude and electromagnet strength.",
        f"Higher current = stronger magnet -> pulls catch at {trip_a} A.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Proportional magnetic strength with current triggering trip", "marks": 2, "editable": True},
        ],
        options=options,
    )


def arch_24_circuit_breaker_internal_components_identification(rng: random.Random) -> Dict[str, Any]:
    rated_a = rng.choice([10, 16, 20, 32])
    target_role = rng.choice([
        ("Contacts (A)", "provide the physical metal touch points where current passes when closed and separates when tripped"),
        ("Electromagnet (B)", "produces a magnetic field proportional to current that pulls the latch during an overload"),
        ("Iron Catch (C)", "holds the moving contact closed during normal current and releases when pulled by the electromagnet"),
        ("Spring (D)", "pulls the contacts rapidly apart to break the circuit once the iron catch releases"),
    ])
    comp_name, role_desc = target_role
    spec = _svg_circuit_breaker_internal(rng, rated_a, "Closed / Normal")
    prompt = (
        f"Inspect the internal schematic of the **{rated_a} A electromagnetic circuit breaker** labelled **A, B, C, D**.\n\n"
        f"1. State the exact function of **{comp_name}** inside this circuit breaker [2].\n"
        "2. Name the external part a user presses after clearing a fault to reconnect the contacts [1]."
    )
    correct = f"{comp_name}: {role_desc}; External part: Reset button / toggle lever"
    sol = (
        f"**Step 1:** **{comp_name}** functions to **{role_desc}** [2].\n\n"
        "**Step 2:** Pushing or flipping the **reset button / toggle switch** forces the moving and stationary contacts back together and re-engages the iron catch [1]."
    )
    return _q(
        rng, "24", "24_circuit_breaker_internal_components_identification",
        "Internal Structure of an Electromagnetic Circuit Breaker",
        prompt, correct, sol, 3, "structured",
        ["confusing_spring_and_iron_catch_roles"],
        "Match each labeled part (A–D) to sensing current, latching, separating, or conducting.",
        f"{comp_name} -> {role_desc}; Reset button restores contact.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Accurate function of {comp_name}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Identify reset button/switch", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_25_circuit_breaker_tripping_and_reset_sequence(rng: random.Random) -> Dict[str, Any]:
    limit_a = rng.choice([16, 20, 25])
    surge_a = limit_a + rng.choice([12, 18, 24])
    prompt = (
        f"During an appliance fault, current through a **{limit_a} A** circuit breaker suddenly spikes to **{surge_a} A**.\n\n"
        "Write a clear **4-step sequence** explaining how the electromagnet, iron catch, spring, and contacts work together to shut off power, and how power is safely restored afterwards [4]."
    )
    correct = f"1) High {surge_a} A current makes the electromagnet very strong; 2) It pulls and releases the iron catch; 3) The spring pulls the contacts apart, breaking the circuit; 4) After fixing the fault, pressing the reset button re-engages the catch and closes contacts."
    sol = (
        f"**Step 1:** Surge current (**{surge_a} A > {limit_a} A**) strongly magnetizes the **electromagnet coil** [1].\n"
        "**Step 2:** Magnetic attraction pulls the **iron catch** away, releasing the latch [1].\n"
        "**Step 3:** The **spring** snaps the moving contact away from the stationary contact, breaking the circuit [1].\n"
        "**Step 4:** Once the fault is repaired, pushing the **reset switch** closes the contacts and re-engages the iron catch [1]."
    )
    return _q(
        rng, "25", "25_circuit_breaker_tripping_and_reset_sequence",
        "Circuit Breaker Tripping & Reset Sequence",
        prompt, correct, sol, 4, "structured",
        ["reversing_electromagnet_and_spring_action"],
        "Order the chain: Excess current -> Electromagnet -> Iron catch -> Spring/Contacts -> Fix fault -> Reset.",
        "Electromagnet strengthens -> catch releases -> spring separates contacts -> fix fault & reset.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Excess current strengthens electromagnet", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Iron catch released", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Spring separates contacts to open circuit", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Fix fault before pressing reset button", "marks": 1, "editable": True},
        ],
    )


BUILDERS_01_25 = {
    "01_parallel_house_wiring_independent_appliances": arch_01_parallel_house_wiring_independent_appliances,
    "02_parallel_circuits_resistance_and_current_increase": arch_02_parallel_circuits_resistance_and_current_increase,
    "03_overloading_multiplug_adapter_fire_hazard": arch_03_overloading_multiplug_adapter_fire_hazard,
    "04_overloading_total_current_calculation_threshold": arch_04_overloading_total_current_calculation_threshold,
    "05_short_circuit_definition_and_unintended_low_resistance_path": arch_05_short_circuit_definition_and_unintended_low_resistance_path,
    "06_short_circuit_current_surge_via_ohms_law": arch_06_short_circuit_current_surge_via_ohms_law,
    "07_short_circuit_dangers_overheating_sparks_and_fire": arch_07_short_circuit_dangers_overheating_sparks_and_fire,
    "08_house_wiring_plan_design_independent_switches_and_mains": arch_08_house_wiring_plan_design_independent_switches_and_mains,
    "09_main_switch_isolation_before_circuit_maintenance": arch_09_main_switch_isolation_before_circuit_maintenance,
    "10_household_branch_fault_isolation_diagnosis": arch_10_household_branch_fault_isolation_diagnosis,
    "11_fuse_definition_thin_low_melting_point_wire": arch_11_fuse_definition_thin_low_melting_point_wire,
    "12_fuse_heating_effect_steel_wool_experiment_setup": arch_12_fuse_heating_effect_steel_wool_experiment_setup,
    "13_steel_wool_fuse_variable_resistor_current_control": arch_13_steel_wool_fuse_variable_resistor_current_control,
    "14_fuse_post_melt_open_circuit_current_zero": arch_14_fuse_post_melt_open_circuit_current_zero,
    "15_fuse_safety_precautions_heat_resistant_mat_and_screen": arch_15_fuse_safety_precautions_heat_resistant_mat_and_screen,
    "16_fuse_current_rating_selection_for_appliances": arch_16_fuse_current_rating_selection_for_appliances,
    "17_undersized_fuse_nuisance_blowing_analysis": arch_17_undersized_fuse_nuisance_blowing_analysis,
    "18_oversized_fuse_or_nail_bypass_fire_hazard": arch_18_oversized_fuse_or_nail_bypass_fire_hazard,
    "19_fuse_placement_series_main_branch_controls_all": arch_19_fuse_placement_series_main_branch_controls_all,
    "20_fuse_placement_parallel_individual_branch_isolation": arch_20_fuse_placement_parallel_individual_branch_isolation,
    "21_fuse_vs_circuit_breaker_reusability_and_convenience": arch_21_fuse_vs_circuit_breaker_reusability_and_convenience,
    "22_fault_diagnosis_before_replacing_fuse_or_resetting": arch_22_fault_diagnosis_before_replacing_fuse_or_resetting,
    "23_electromagnet_principle_in_circuit_breaker": arch_23_electromagnet_principle_in_circuit_breaker,
    "24_circuit_breaker_internal_components_identification": arch_24_circuit_breaker_internal_components_identification,
    "25_circuit_breaker_tripping_and_reset_sequence": arch_25_circuit_breaker_tripping_and_reset_sequence,
}
