"""Grade 9 Natural Sciences - Safety with Electricity: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Safety with electricity.md and Syllabus.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .safety_electricity_archetypes_01_25 import _fmt, _q


def _svg_three_pin_plug_open(rng: random.Random, appliance: str, fault_mode: str = "correct") -> Dict[str, Any]:
    """Opened South African Type M 3-pin plug (cord grip at bottom, pins facing away)."""
    if fault_mode == "correct":
        l_col, n_col, e_col = "#92400e", "#2563eb", "#16a34a"
        l_lbl, n_lbl, e_lbl = "L", "N", "E"
        status_txt = f"Opened 3-Pin Plug ({appliance}) - View from Back"
        extra = ""
    elif fault_mode == "live_earth_swap":
        l_col, n_col, e_col = "#16a34a", "#2563eb", "#92400e"
        l_lbl, n_lbl, e_lbl = "L (Green/Yellow!)", "N (Blue)", "E (Brown!)"
        status_txt = f"Faulty Plug ({appliance}): Live & Earth Swapped"
        extra = '<text x="215" y="34" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">FAULT: Brown connected to Earth!</text>'
    elif fault_mode == "stray_strand":
        l_col, n_col, e_col = "#92400e", "#2563eb", "#16a34a"
        l_lbl, n_lbl, e_lbl = "L (Brown)", "N (Blue)", "E (Green/Yellow)"
        status_txt = f"Faulty Plug ({appliance}): Loose Copper Strand"
        extra = (
            '<line x1="138" y1="128" x2="292" y2="128" stroke="#d97706" stroke-width="2" stroke-dasharray="3,2"/>'
            '<text x="215" y="118" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Stray copper touching N</text>'
        )
    else:  # loose_grip
        l_col, n_col, e_col = "#92400e", "#2563eb", "#16a34a"
        l_lbl, n_lbl, e_lbl = "L (Brown)", "N (Blue)", "E (Green/Yellow)"
        status_txt = f"Faulty Plug ({appliance}): Cord Grip Unclamped"
        extra = '<text x="215" y="198" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Cord grip loose - inner wire strained</text>'

    svg = (
        f'<svg viewBox="0 0 430 230" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="230" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<polygon points="215,42 335,148 295,182 135,182 95,148" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="215" cy="70" r="13" fill="#e2e8f0" stroke="{e_col}" stroke-width="3"/>'
        f'<text x="215" y="74" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{e_lbl}</text>'
        f'<circle cx="138" cy="136" r="12" fill="#e2e8f0" stroke="{l_col}" stroke-width="3"/>'
        f'<text x="138" y="140" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{l_lbl}</text>'
        f'<circle cx="292" cy="136" r="12" fill="#e2e8f0" stroke="{n_col}" stroke-width="3"/>'
        f'<text x="292" y="140" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{n_lbl}</text>'
        f'<path d="M 215 178 L 215 83" fill="none" stroke="{e_col}" stroke-width="4"/>'
        f'<path d="M 205 178 L 138 148" fill="none" stroke="{l_col}" stroke-width="4"/>'
        f'<path d="M 225 178 L 292 148" fill="none" stroke="{n_col}" stroke-width="4"/>'
        f'<rect x="182" y="170" width="66" height="14" rx="2" fill="#cbd5e1" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="215" y="180" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Cord Grip</text>'
        f'{extra}'
        f'<text x="215" y="218" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{status_txt}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_three_pin_plug_profile(rng: random.Random, rating_a: int, e_mm: int, ln_mm: int) -> Dict[str, Any]:
    """Side profile comparing longer thicker Earth pin against Live/Neutral pins."""
    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="45" y="38" width="80" height="106" rx="5" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>'
        f'<text x="85" y="92" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{rating_a} A Plug</text>'
        f'<rect x="125" y="48" width="145" height="18" rx="3" fill="#94a3b8" stroke="#1e293b" stroke-width="1.5"/>'
        f'<text x="200" y="61" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Earth Pin ({e_mm} mm)</text>'
        f'<rect x="125" y="108" width="110" height="13" rx="3" fill="#cbd5e1" stroke="#1e293b" stroke-width="1.5"/>'
        f'<text x="180" y="118" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Live &amp; Neutral ({ln_mm} mm)</text>'
        f'<rect x="305" y="36" width="85" height="110" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.8"/>'
        f'<text x="347" y="92" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">Wall Socket</text>'
        f'<text x="347" y="106" font-size="9" fill="#dc2626" text-anchor="middle">Safety Shutters</text>'
        f'<text x="215" y="174" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Earth Pin Longer ({e_mm} mm vs {ln_mm} mm) &amp; Thicker</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_cord_stripping_guide(rng: random.Random, outer_cm: float, inner_cm: float) -> Dict[str, Any]:
    """3-core cable stripping schematic showing outer jacket and inner copper lengths."""
    svg = (
        f'<svg viewBox="0 0 430 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="175" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="35" y="62" width="150" height="44" rx="4" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<text x="110" y="88" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Outer Sheath</text>'
        f'<line x1="185" y1="68" x2="295" y2="52" stroke="#16a34a" stroke-width="6"/>'
        f'<line x1="185" y1="84" x2="295" y2="84" stroke="#92400e" stroke-width="6"/>'
        f'<line x1="185" y1="100" x2="295" y2="116" stroke="#2563eb" stroke-width="6"/>'
        f'<line x1="295" y1="52" x2="350" y2="52" stroke="#d97706" stroke-width="3"/>'
        f'<line x1="295" y1="84" x2="350" y2="84" stroke="#d97706" stroke-width="3"/>'
        f'<line x1="295" y1="116" x2="350" y2="116" stroke="#d97706" stroke-width="3"/>'
        f'<text x="240" y="34" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Outer cut: {_fmt(outer_cm, 1)} cm</text>'
        f'<text x="322" y="34" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">Copper: {_fmt(inner_cm, 1)} cm</text>'
        f'<text x="215" y="156" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Prepare Cord: Strip {_fmt(outer_cm, 1)} cm outer &amp; {_fmt(inner_cm, 1)} cm inner</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_double_insulation_symbol(rng: random.Random, appliance: str, watts: int) -> Dict[str, Any]:
    """Double insulation square-inside-square nameplate symbol with 2-pin plug."""
    svg = (
        f'<svg viewBox="0 0 430 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="185" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="35" y="34" width="175" height="115" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<text x="122" y="56" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{appliance}</text>'
        f'<text x="122" y="74" font-size="10" fill="#334155" text-anchor="middle">{watts} W | 230 V</text>'
        f'<rect x="102" y="88" width="40" height="40" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="112" y="98" width="20" height="20" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="255" y="50" width="135" height="82" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.8"/>'
        f'<text x="322" y="76" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">2-Pin Plug Only</text>'
        f'<text x="322" y="96" font-size="9.5" fill="#92400e" font-weight="bold" text-anchor="middle">Brown (Live)</text>'
        f'<text x="322" y="114" font-size="9.5" fill="#2563eb" font-weight="bold" text-anchor="middle">Blue (Neutral)</text>'
        f'<text x="215" y="170" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Class II Appliance Safety Symbol</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_earthed_appliance_fault(rng: random.Random, appliance: str, fuse_a: int, r_earth: float) -> Dict[str, Any]:
    """Metal-cased appliance with Live-to-chassis fault diverted via low-R Earth wire."""
    svg = (
        f'<svg viewBox="0 0 430 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="215" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="165" y="34" width="210" height="125" rx="6" fill="#e2e8f0" stroke="#0f172a" stroke-width="2.5"/>'
        f'<text x="270" y="55" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Metal Casing: {appliance}</text>'
        f'<line x1="25" y1="80" x2="195" y2="80" stroke="#92400e" stroke-width="3"/>'
        f'<rect x="65" y="68" width="52" height="24" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>'
        f'<text x="91" y="84" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Fuse {fuse_a} A</text>'
        f'<circle cx="195" cy="80" r="5" fill="#dc2626"/>'
        f'<text x="270" y="84" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">FAULT: Live touches casing!</text>'
        f'<line x1="25" y1="120" x2="215" y2="120" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="120" y="114" font-size="9" font-weight="bold" fill="#2563eb" text-anchor="middle">Neutral</text>'
        f'<polyline points="165,146 85,146 85,182" fill="none" stroke="#16a34a" stroke-width="3.5"/>'
        f'<line x1="65" y1="182" x2="105" y2="182" stroke="#16a34a" stroke-width="2.5"/>'
        f'<line x1="73" y1="189" x2="97" y2="189" stroke="#16a34a" stroke-width="2.5"/>'
        f'<line x1="80" y1="196" x2="90" y2="196" stroke="#16a34a" stroke-width="2.5"/>'
        f'<text x="225" y="182" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">Earth Wire (R ≈ {_fmt(r_earth, 1)} Ω) to Ground</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_earth_leakage_comparator(rng: random.Random, i_live: float, i_neut: float, leak_ma: int) -> Dict[str, Any]:
    """Earth Leakage (ELCB/RCD) differential current comparator schematic."""
    svg = (
        f'<svg viewBox="0 0 430 195" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="195" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="135" y="34" width="150" height="110" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="210" y="56" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Earth Leakage Unit</text>'
        f'<line x1="25" y1="78" x2="330" y2="78" stroke="#92400e" stroke-width="3"/>'
        f'<text x="78" y="70" font-size="10" font-weight="bold" fill="#92400e" text-anchor="middle">Live: {_fmt(i_live, 3)} A</text>'
        f'<line x1="25" y1="116" x2="330" y2="116" stroke="#2563eb" stroke-width="3"/>'
        f'<text x="78" y="132" font-size="10" font-weight="bold" fill="#2563eb" text-anchor="middle">Neutral: {_fmt(i_neut, 3)} A</text>'
        f'<rect x="330" y="64" width="75" height="68" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>'
        f'<text x="367" y="96" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Appliance</text>'
        f'<text x="367" y="112" font-size="9.5" fill="#dc2626" text-anchor="middle">Leak: {leak_ma} mA</text>'
        f'<text x="215" y="176" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Imbalance ΔI = {leak_ma} mA to Earth</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_lightning_rod_house(rng: random.Random, bldg: str, height_m: int) -> Dict[str, Any]:
    """House/school roof lightning spike and deep earth burial conductor."""
    svg = (
        f'<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="210" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<polygon points="105,105 215,50 325,105" fill="#fecaca" stroke="#7f1d1d" stroke-width="2"/>'
        f'<rect x="125" y="105" width="180" height="68" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
        f'<text x="215" y="142" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{bldg} ({height_m} m)</text>'
        f'<line x1="215" y1="20" x2="215" y2="50" stroke="#0f172a" stroke-width="4"/>'
        f'<text x="262" y="34" font-size="10" font-weight="bold" fill="#dc2626">Lightning Spike</text>'
        f'<polyline points="215,50 335,105 335,186" fill="none" stroke="#b45309" stroke-width="3"/>'
        f'<line x1="318" y1="186" x2="352" y2="186" stroke="#15803d" stroke-width="3"/>'
        f'<text x="365" y="150" font-size="9.5" font-weight="bold" fill="#b45309" text-anchor="middle">Copper</text>'
        f'<text x="215" y="198" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">Deep Ground Earth Rod</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_shock_current_scale(rng: random.Random, curr_ma: int, band_label: str) -> Dict[str, Any]:
    """Physiological electric shock severity scale in mA."""
    x_pos = min(375, max(55, 55 + int(curr_ma * 2.5)))
    svg = (
        f'<svg viewBox="0 0 430 165" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="165" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="40" y="65" width="80" height="28" fill="#dcfce7" stroke="#16a34a"/>'
        f'<rect x="120" y="65" width="90" height="28" fill="#fef08a" stroke="#ca8a04"/>'
        f'<rect x="210" y="65" width="90" height="28" fill="#fed7aa" stroke="#ea580c"/>'
        f'<rect x="300" y="65" width="90" height="28" fill="#fecaca" stroke="#dc2626"/>'
        f'<text x="80" y="83" font-size="9" font-weight="bold" fill="#166534" text-anchor="middle">1–5 mA</text>'
        f'<text x="165" y="83" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">10–20 mA</text>'
        f'<text x="255" y="83" font-size="9" font-weight="bold" fill="#9a3412" text-anchor="middle">30–75 mA</text>'
        f'<text x="345" y="83" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">100+ mA</text>'
        f'<polygon points="{x_pos},62 {x_pos - 6},46 {x_pos + 6},46" fill="#0f172a"/>'
        f'<text x="{x_pos}" y="38" font-size="10.5" font-weight="bold" fill="#dc2626" text-anchor="middle">{curr_ma} mA</text>'
        f'<text x="215" y="132" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Body Current Effect Scale ({band_label})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_distribution_board(rng: random.Random, tripped: str, elcb_ma: int, lights_a: int, plugs_a: int) -> Dict[str, Any]:
    """Domestic distribution board showing Main Switch, ELCB, Lights MCB, Plugs MCB."""
    def _col(name: str) -> str:
        return "#fee2e2" if name in tripped else "#dcfce7"
    def _st(name: str) -> str:
        return "TRIPPED" if name in tripped else "ON"

    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<rect x="25" y="25" width="380" height="140" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<text x="215" y="45" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Household Distribution Board (DB)</text>'
        f'<rect x="42" y="60" width="76" height="82" rx="4" fill="{_col("Main")}" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="80" y="90" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Main 60 A</text>'
        f'<text x="80" y="114" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">{_st("Main")}</text>'
        f'<rect x="132" y="60" width="82" height="82" rx="4" fill="{_col("ELCB")}" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="173" y="90" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">ELCB {elcb_ma}mA</text>'
        f'<text x="173" y="114" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">{_st("ELCB")}</text>'
        f'<rect x="228" y="60" width="76" height="82" rx="4" fill="{_col("Lights")}" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="266" y="90" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Lights {lights_a}A</text>'
        f'<text x="266" y="114" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">{_st("Lights")}</text>'
        f'<rect x="318" y="60" width="72" height="82" rx="4" fill="{_col("Plugs")}" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="354" y="90" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Plugs {plugs_a}A</text>'
        f'<text x="354" y="114" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">{_st("Plugs")}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_three_pin_plug_wire_colour_codes_identification(rng: random.Random) -> Dict[str, Any]:
    wire = rng.choice([
        ("Live wire", "Brown", "Blue", "Green and yellow striped", "Black and white"),
        ("Neutral wire", "Blue", "Brown", "Green and yellow striped", "Red"),
        ("Earth wire", "Green and yellow striped", "Brown", "Blue", "Orange"),
    ])
    w_name, col_ok, d1, d2, d3 = wire
    prompt = (
        f"When inspecting the internal cord of a standard South African 3-pin plug, three colour-coded insulated conductors appear.\n\n"
        f"Which standard insulation colour identifies the **{w_name}**?"
    )
    options = [col_ok, d1, d2, d3]
    rng.shuffle(options)
    sol = (
        "**Standard Three-Wire Colour Code:**\n"
        "- **Live wire:** Brown\n"
        "- **Neutral wire:** Blue\n"
        "- **Earth wire:** Green and yellow striped (occasionally solid green or yellow)\n\n"
        f"**Answer:** **{w_name}** = **{col_ok}**."
    )
    return _q(
        rng, "26", "26_three_pin_plug_wire_colour_codes_identification",
        "3-Pin Plug Wire Colour Codes",
        prompt, col_ok, sol, 2, "mcq",
        ["confusing_live_brown_and_neutral_blue"],
        "Remember: Brown = Live, Blue = Neutral, Green/Yellow = Earth.",
        f"{w_name} -> {col_ok}.",
        col_ok,
        marking_points=[{"id": "mp_1", "desc": f"Correct colour ({col_ok}) for {w_name}", "marks": 2, "editable": True}],
        options=options,
    )


def arch_27_live_neutral_earth_wire_electrical_functions(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["washing machine", "electric kettle", "microwave oven", "fridge-freezer"])
    prompt = (
        f"A **{app}** connects to the mains supply through a three-wire power cord (Live, Neutral, and Earth).\n\n"
        "State the specific electrical **function** of each wire:\n"
        "1. **Live wire** [1]\n"
        "2. **Neutral wire** [1]\n"
        "3. **Earth wire** [1]"
    )
    correct = "Live wire brings high-potential current into the appliance; Neutral wire completes the return circuit away from the appliance; Earth wire provides a low-resistance safety path to ground during faults."
    sol = (
        "**Step 1 (Live wire - Brown):** Supplies high potential difference (230 V) and carries current into the appliance [1].\n"
        "**Step 2 (Neutral wire - Blue):** Carries return current away from the appliance to complete the circuit [1].\n"
        "**Step 3 (Earth wire - Green/Yellow):** Normally carries zero current; provides a very low-resistance safety path to the ground if a fault energizes the metal casing [1]."
    )
    return _q(
        rng, "27", "27_live_neutral_earth_wire_electrical_functions",
        "Functions of Live, Neutral & Earth Wires",
        prompt, correct, sol, 3, "structured",
        ["thinking_earth_wire_carries_normal_load_current"],
        "Distinguish supply (Live), return path (Neutral), and fault safety path (Earth).",
        "Live = brings 230 V in; Neutral = return loop; Earth = safety fault path to ground.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Live wire supplies high-potential current", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Neutral wire completes circuit", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Earth wire safety path to ground during fault", "marks": 1, "editable": True},
        ],
    )


def arch_28_three_pin_plug_terminal_pin_positions_opened_view(rng: random.Random) -> Dict[str, Any]:
    appliance = rng.choice(["Electric Kettle", "Steam Iron", "Microwave", "Toaster"])
    spec = _svg_three_pin_plug_open(rng, appliance, "correct")
    prompt = (
        f"Inspect the opened South African 3-pin plug for a **{appliance}** viewed from the back with the cord grip at the bottom.\n\n"
        "Complete the pin assignment by matching each terminal (**E, L, N**) to its position (Top, Left, Right) and wire colour [3]."
    )
    correct = "Top pin (E): Green and yellow striped Earth wire; Left terminal (L): Brown Live wire; Right terminal (N): Blue Neutral wire."
    sol = (
        "**Opened 3-Pin Plug Orientation (pins pointing away, cord at bottom):**\n"
        "- **Top pin (E):** **Green and yellow striped** (Earth)\n"
        "- **Left pin (L):** **Brown** (Live)\n"
        "- **Right pin (N):** **Blue** (Neutral)"
    )
    return _q(
        rng, "28", "28_three_pin_plug_terminal_pin_positions_opened_view",
        "Opened 3-Pin Plug Pin Positions & Colours",
        prompt, correct, sol, 3, "structured",
        ["swapping_left_and_right_pins_in_opened_plug"],
        "Remember: 'bLue = Right (or bLue = Left in socket, Right inside open plug)'; 'bRown = Left inside open plug' — wait: check L (Left) and N (Right) labels!",
        "Top E = Green/Yellow; Left L = Brown; Right N = Blue.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "E top = Green/Yellow", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "L left = Brown", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "N right = Blue", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_29_fuse_mandatory_placement_on_live_wire(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["toaster", "kettle", "electric heater", "bench grinder"])
    prompt = (
        f"Inside the mains plug or internal supply of a 230 V **{app}**, engineers always fit the fuse or single-pole switch on the **Live wire** rather than the Neutral wire.\n\n"
        "Why is placing the fuse on the **Live wire** essential for human safety?"
    )
    correct = "When the fuse blows on the Live wire, it disconnects the high 230 V supply before current reaches the appliance, leaving internal parts at 0 V instead of live."
    options = [
        correct,
        "The Neutral wire has zero copper and cannot hold a screw clamp.",
        "Fuses only melt if wrapped in brown plastic insulation.",
        "Placing a fuse on the Neutral wire doubles the voltage inside the plug.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** The **Live wire** is at 230 V relative to earth; the Neutral wire sits near 0 V.\n\n"
        "**Step 2:** When a Live-side fuse blows, the entire appliance is completely isolated from high voltage. "
        "If placed only on the Neutral wire, a blown fuse would stop the motor yet leave internal components live at 230 V."
    )
    return _q(
        rng, "29", "29_fuse_mandatory_placement_on_live_wire",
        "Why Fuses & Switches Belong on the Live Wire",
        prompt, correct, sol, 2, "mcq",
        ["placing_fuse_on_neutral_wire_hazard"],
        "Consider which wire carries 230 V relative to ground if a fuse opens.",
        "Fuse on Live wire isolates 230 V from the appliance when blown.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Isolates high 230 V potential from appliance", "marks": 2, "editable": True}],
        options=options,
    )


def arch_30_longer_thicker_earth_pin_safety_engineering(rng: random.Random) -> Dict[str, Any]:
    e_mm = rng.choice([28, 29])
    ln_mm = rng.choice([21, 22])
    rating_a = rng.choice([15, 16])
    spec = _svg_three_pin_plug_profile(rng, rating_a, e_mm, ln_mm)
    prompt = (
        f"Refer to the side profile of a standard **{rating_a} A** 3-pin plug where the **Earth pin** ({e_mm} mm) is longer and thicker than the Live and Neutral pins ({ln_mm} mm).\n\n"
        "Explain **two safety reasons** for making the Earth pin longer and thicker [2]."
    )
    correct = "1) The longer Earth pin connects first before Live/Neutral make contact (and disconnects last on removal), earthing the casing before power arrives; 2) It pushes open the spring-loaded safety shutters over Live/Neutral socket holes and prevents wrong-way insertion."
    sol = (
        "**Step 1 (First-make, last-break):** Because the Earth pin is longer, the appliance metal casing is earthed **before** the Live pin reaches 230 V (and stays earthed until after Live disconnects) [1].\n\n"
        "**Step 2 (Safety shutters & keying):** The longer/thicker Earth pin opens child-safety shutters inside the wall socket and physically prevents inserting the plug upside down [1]."
    )
    return _q(
        rng, "30", "30_longer_thicker_earth_pin_safety_engineering",
        "Engineering Purpose of Longer, Thicker Earth Pin",
        prompt, correct, sol, 2, "short_answer",
        ["thinking_longer_earth_pin_only_saves_metal"],
        "Think about contact order during insertion and wall-socket child shutters.",
        "Earths appliance before Live touches + opens wall socket safety shutters.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Connects Earth before Live/Neutral", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Opens wall socket safety shutters / prevents mis-insertion", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_31_three_pin_plug_cord_stripping_and_strand_twisting(rng: random.Random) -> Dict[str, Any]:
    outer_cm = rng.choice([2.0, 2.5])
    inner_cm = rng.choice([0.5, 0.6])
    spec = _svg_cord_stripping_guide(rng, outer_cm, inner_cm)
    prompt = (
        f"Refer to the cord preparation guide showing **{_fmt(outer_cm, 1)} cm** of outer sheath removed and **{_fmt(inner_cm, 1)} cm** of inner insulation stripped.\n\n"
        "Why must the copper wire strands be **gently twisted tightly** together without nicking any strands before inserting them into the brass pin holes?"
    )
    correct = "Twisting keeps all fine copper strands together so no loose stray strand bridges to an adjacent terminal causing a short circuit, while preserving full wire thickness so it does not overheat."
    options = [
        correct,
        "Twisting turns copper into plastic insulation so electricity slows down.",
        "Nicking half the copper strands reduces fire risk by doubling current.",
        "Twisting changes direct current into alternating lightning pulses.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Stripping without nicking keeps the full copper cross-section intact (damaged/thinned strands overheat under load).\n\n"
        "**Step 2:** Twisting strands tightly ensures every strand enters cleanly into the terminal hole without stray whiskers causing a **short circuit**."
    )
    return _q(
        rng, "31", "31_three_pin_plug_cord_stripping_and_strand_twisting",
        "Cord Stripping & Twisting Copper Strands Safely",
        prompt, correct, sol, 2, "mcq",
        ["leaving_untwisted_whiskers_in_plug"],
        "Think what happens if one loose copper whisker sticks out sideways or strands are cut thin.",
        "Prevents stray strands short-circuiting terminals and keeps full copper thickness.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Prevent stray-strand short circuits and preserve conductor thickness", "marks": 2, "editable": True}],
        options=options,
        diagram_spec=spec,
    )


def arch_32_loose_strands_and_cord_grip_clamp_function(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["vacuum cleaner", "lawnmower", "floor polisher", "electric drill"])
    prompt = (
        f"When someone pulls on the cable of a **{app}** to unplug it, mechanical tension transfers along the cord.\n\n"
        "1. State what the **cord grip (cable clamp)** inside the plug base must hold tightly [1].\n"
        "2. Explain the electrical danger if the cord grip is left loose or unscrewed [2]."
    )
    correct = "1) It must clamp tightly over the outer white/black insulated sheath; 2) Without it, tugging the cable pulls the inner Live/Neutral/Earth wires loose from their pin screws, creating exposed live contacts or short circuits."
    sol = (
        "**Step 1:** The cord grip must clamp firmly over the **outer insulated sheath** (jacket), NOT on bare inner wires [1].\n\n"
        "**Step 2:** If left loose, pulling the cord yanks copper wires out of their brass pin screws, causing **short circuits**, sparks, or an **exposed live wire** [2]."
    )
    return _q(
        rng, "32", "32_loose_strands_and_cord_grip_clamp_function",
        "Cord Grip Function & Strain-Relief Hazard",
        prompt, correct, sol, 3, "structured",
        ["clamping_inner_wires_instead_of_outer_sheath"],
        "What stops tugging forces from reaching the tiny brass terminal screws?",
        "Clamps outer jacket so pulling does not yank inner wires out of pin screws.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Clamp grips outer insulated sheath", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Prevents wires pulling loose causing short circuits/shock", "marks": 2, "editable": True},
        ],
    )


def arch_33_diagnosing_miswired_three_pin_plug_hazards(rng: random.Random) -> Dict[str, Any]:
    fault = rng.choice([
        ("live_earth_swap", "Electric Kettle", "Brown (Live) is connected to the Earth pin E", "the metal kettle casing becomes live at 230 V, causing fatal electric shock on touch"),
        ("stray_strand", "Toaster", "a loose copper strand bridges from Live (L) to Neutral (N)", "it creates a direct low-resistance short circuit inside the plug, causing sparks and blowing the fuse/breaker"),
        ("loose_grip", "Steam Iron", "the cord grip is completely unscrewed and loose", "pulling the cord can yank wires loose from terminals causing a short circuit or electric shock"),
    ])
    f_key, app, obs, consequence = fault
    spec = _svg_three_pin_plug_open(rng, app, f_key)
    prompt = (
        f"Inspect the faulty opened 3-pin plug belonging to a **{app}**.\n\n"
        f"1. Identify the specific wiring error ({obs}) [1].\n"
        f"2. Predict the immediate safety hazard when the {app} is plugged in and switched on [2]."
    )
    correct = f"Wiring fault: {obs}; Consequence: {consequence}."
    sol = (
        f"**Step 1 (Fault Identified):** {obs} [1].\n\n"
        f"**Step 2 (Hazard Prediction):** When energized, **{consequence}** [2]."
    )
    return _q(
        rng, "33", "33_diagnosing_miswired_three_pin_plug_hazards",
        "Diagnosing Miswired 3-Pin Plug Faults",
        prompt, correct, sol, 3, "structured",
        ["ignoring_plug_inspection_before_closing_cover"],
        "Trace where each coloured wire or stray copper strand goes inside the plug.",
        f"{obs} -> {consequence}.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Identify exact wiring fault", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Predict resulting electric shock or short-circuit hazard", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_34_double_insulation_two_pin_plug_appliances(rng: random.Random) -> Dict[str, Any]:
    app, watts = rng.choice([
        ("Hairdryer", 1600),
        ("Plastic Food Blender", 500),
        ("Cellphone Charger", 25),
        ("Corded Jigsaw", 650),
    ])
    spec = _svg_double_insulation_symbol(rng, app, watts)
    prompt = (
        f"Inspect the nameplate and 2-pin plug schematic for a **{app}** ({watts} W).\n\n"
        "What does the **square-inside-a-square symbol** certify, and why does this appliance safely use only a **2-pin plug** (no Earth wire)?"
    )
    correct = "It certifies Double Insulation (Class II): internal live conductors have insulation plus a complete outer non-conducting plastic casing, so external touchable parts can never become live."
    options = [
        correct,
        "It means the appliance runs on square batteries and needs double mains voltage.",
        "It warns that the plastic outer shell conducts current like solid copper.",
        "It shows the appliance contains two blown glass fuses inside the cord.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** The **concentric squares symbol** denotes **Double Insulation**.\n\n"
        "**Step 2:** Two independent layers of insulation (wire insulation + non-conductive plastic outer housing) prevent any live part from reaching the user's hand, eliminating the need for an Earth wire."
    )
    return _q(
        rng, "34", "34_double_insulation_two_pin_plug_appliances",
        "Double Insulation Symbol & 2-Pin Plugs",
        prompt, correct, sol, 2, "mcq",
        ["thinking_2_pin_appliances_lack_safety_protection"],
        "Look at the outer material of hairdryers/chargers and the meaning of two nested squares.",
        "Double insulation (two insulating layers / plastic housing) -> no Earth wire needed.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Explain double insulation and non-conductive outer casing", "marks": 2, "editable": True}],
        options=options,
        diagram_spec=spec,
    )


def arch_35_plug_wiring_general_safety_precautions(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        "fitting a replacement plug onto an extension lead",
        "checking loose terminal screws inside a lamp plug",
        "rewiring a torn kettle plug in the workshop",
        "inspecting an appliance cord connector at home",
    ])
    prompt = (
        f"Before beginning the task of **{context}**, a learner prepares the workspace.\n\n"
        "State **three essential safety precautions** that must be observed before and during plug wiring [3]."
    )
    correct = "1) Completely unplug/disconnect from the mains supply and switch off power; 2) Work on a dry, non-conducting surface with dry hands; 3) Double-check wire colour positions, tighten all pin screws, clamp outer sheath in cord grip, and inspect for stray strands before closing."
    sol = (
        "**Three Core Precautions:**\n"
        "1. **Disconnect completely** from the mains wall socket (never wire while plugged in or near live power) [1].\n"
        "2. Work on a **dry surface** with **dry hands** [1].\n"
        "3. Verify **no stray copper strands**, correct colour-to-pin connections, and tight **cord grip** before replacing the cover [1]."
    )
    return _q(
        rng, "35", "35_plug_wiring_general_safety_precautions",
        "Safety Precautions When Wiring a 3-Pin Plug",
        prompt, correct, sol, 3, "short_answer",
        ["wiring_plug_on_damp_sink_counter"],
        "Think about power disconnection, dry working conditions, and final inspection before closing.",
        "Unplug from mains; dry surface/hands; check colours, tight screws, no stray strands.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Disconnect/unplug power supply", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Work on dry surface with dry hands", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Verify wiring colours, tight screws & no stray strands", "marks": 1, "editable": True},
        ],
    )


def arch_36_earthing_metal_casing_fault_protection_mechanism(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["Washing Machine", "Metal Electric Kettle", "Metal Toaster", "Electric Stove"])
    fuse_a = rng.choice([10, 13, 16])
    r_earth = round(rng.uniform(0.1, 0.3), 1)
    spec = _svg_earthed_appliance_fault(rng, app, fuse_a, r_earth)
    prompt = (
        f"Inspect the earthing schematic of a **{app}** where an internal fault causes the **230 V Live wire** to touch the metal casing.\n\n"
        f"Explain step-by-step how the **Earth wire** (connected to the metal casing, $R \\approx {_fmt(r_earth, 1)}\\ \\Omega$) and the **{fuse_a} A fuse** protect a person from electric shock [4]."
    )
    correct = f"The Earth wire connects the metal casing directly to the ground via a very low-resistance path ({_fmt(r_earth, 1)} Ω). Fault current surges straight to earth, instantly blowing the {fuse_a} A fuse (or tripping the breaker) and disconnecting the 230 V supply before someone touches the casing."
    sol = (
        "**Step 1:** A loose Live wire energizes the conductive metal casing [1].\n"
        f"**Step 2:** The bolted **Earth wire** provides an ultra-low-resistance path ($R \\approx {_fmt(r_earth, 1)}\\ \\Omega$) directly to the ground [1].\n"
        f"**Step 3:** A massive short-circuit surge flows down the Earth wire, instantly **melting the {fuse_a} A fuse** (or tripping the circuit breaker) [1].\n"
        "**Step 4:** The Live supply is permanently cut off, preventing electric shock [1]."
    )
    return _q(
        rng, "36", "36_earthing_metal_casing_fault_protection_mechanism",
        "How Earthing Protects Metal-Cased Appliances",
        prompt, correct, sol, 4, "structured",
        ["thinking_earth_wire_absorbs_charge_like_a_sponge_without_tripping"],
        "Trace the fault path: Live -> Metal casing -> Low-R Earth wire -> Huge surge -> Blows fuse.",
        f"Low-R Earth path creates surge that blows {fuse_a} A fuse, isolating 230 V.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Earth wire attached to metal casing", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Low-resistance path to ground", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Massive current surge blows fuse/trips breaker", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Power cut prevents shock to user", "marks": 1, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_37_earth_wire_near_zero_resistance_ohms_law(rng: random.Random) -> Dict[str, Any]:
    v_mains = 230
    r_earth = rng.choice([0.1, 0.2, 0.5])
    i_surge = int(round(v_mains / r_earth))
    prompt = (
        f"Curriculum standards specify that a household Earth wire must have **almost zero resistance** (e.g. $R = {_fmt(r_earth, 1)}\\ \\Omega$).\n\n"
        f"1. Calculate the fault surge current at **{v_mains} V** if the Live wire touches an earthed metal casing ($I = \\frac{{V}}{{R}}$) [2].\n"
        "2. Explain why the Earth wire would **fail to protect a user** if it had a high resistance (e.g. $100\\ \\Omega$) [2]."
    )
    correct = f"I_fault = {i_surge} A; if earth resistance were high (100 Ω), current (2,3 A) would be too small to blow a 16 A breaker/fuse, leaving the metal casing dangerously live at high voltage."
    sol = (
        f"**Step 1:** $I_{{\\text{{fault}}}} = \\frac{{{v_mains}}}{{{_fmt(r_earth, 1)}}} = {i_surge}\\text{{ A}}$ [2].\n\n"
        "**Step 2:** A huge surge like this immediately blows any 13 A–20 A fuse/breaker. If Earth resistance were $100\\ \\Omega$, fault current would only be $2{{,}}3\\text{{ A}}$ — too weak to trip protection — leaving the metal casing fatally live [2]."
    )
    return _q(
        rng, "37", "37_earth_wire_near_zero_resistance_ohms_law",
        "Why Earth Wire Resistance Must Be Almost Zero",
        prompt, correct, sol, 4, "calculation",
        ["thinking_high_earth_resistance_is_safer"],
        "Calculate I = 230 / R and compare to a typical 16 A fuse or breaker.",
        f"I = {v_mains} / {_fmt(r_earth, 1)} = {i_surge} A; high R stops breaker from tripping.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Correct fault current = {i_surge} A", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "High R yields low current that fails to blow fuse/trip breaker", "marks": 2, "editable": True},
        ],
    )


def arch_38_ungrounded_faulty_metal_appliance_shock_risk(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["fridge", "metal kettle", "washing machine", "metal microwave"])
    prompt = (
        f"A faulty **{app}** has an exposed 230 V Live wire touching its metal casing, AND its Earth wire was disconnected inside the plug.\n\n"
        "What happens the moment a barefoot user standing on a damp tiled floor touches the metal casing?"
    )
    correct = "The metal casing is energized at 230 V; the person's body becomes the conducting path to the ground, causing a severe or fatal electric shock."
    options = [
        correct,
        "Nothing happens because electricity stays politely inside metal until a switch is flipped.",
        "The plastic feet of the person generate reverse voltage that repairs the wire.",
        "Current flows backward up the air into the ceiling lights.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Without an Earth wire, the Live-to-casing fault energizes the entire metal shell at 230 V without blowing the fuse.\n\n"
        "**Step 2:** When a user touches the live metal, their body completes the circuit to Earth, resulting in dangerous or fatal **electrocution**."
    )
    return _q(
        rng, "38", "38_ungrounded_faulty_metal_appliance_shock_risk",
        "Electric Shock Risk in Unearthed Faulty Appliances",
        prompt, correct, sol, 2, "mcq",
        ["thinking_broken_earth_wire_just_turns_appliance_off"],
        "Who becomes the path to the ground if the Earth wire is missing during a casing fault?",
        "User's body completes path to ground -> dangerous/fatal electric shock.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Person becomes conducting path to ground and gets shocked", "marks": 2, "editable": True}],
        options=options,
    )


def arch_39_neutral_wire_earthed_leaving_house_grid_protection(rng: random.Random) -> Dict[str, Any]:
    event = rng.choice([
        "high-voltage lightning strike hits overhead Eskom distribution lines",
        "summer thunderstorm induces a massive surge on outdoor supply cables",
        "lightning discharge strikes a neighbourhood pole transformer line",
        "electrical storm hits overhead street mains",
    ])
    prompt = (
        f"In South African domestic installations, the **Neutral wire** is earthed as it leaves the house.\n\n"
        f"Explain how earthing the Neutral wire protects the house and national grid when a **{event}** [2]."
    )
    correct = "Earthing the Neutral wire provides a direct low-resistance path into the ground so massive lightning surge currents discharge safely into Earth rather than travelling into the house and burning up domestic wiring."
    sol = (
        "**Step 1:** The **Neutral wire** is earthed at the supply boundary leaving the house [1].\n\n"
        "**Step 2:** If lightning strikes overhead mains lines, the huge surge is diverted **into the ground** instead of burning out the house's internal network [1]."
    )
    return _q(
        rng, "39", "39_neutral_wire_earthed_leaving_house_grid_protection",
        "Grid Lightning Protection via Earthed Neutral",
        prompt, correct, sol, 2, "short_answer",
        ["thinking_only_plug_earth_pin_connects_to_ground"],
        "Where does excess lightning surge go when the Neutral line is connected to ground?",
        "Directed safely into the ground rather than burning out domestic wiring.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Provides direct path into the ground", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Prevents lightning surge from burning household network", "marks": 1, "editable": True},
        ],
    )


def arch_40_earth_leakage_unit_differential_current_detection(rng: random.Random) -> Dict[str, Any]:
    i_live = round(rng.choice([4.000, 6.000, 8.000]), 3)
    leak_ma = rng.choice([35, 45, 60, 80])
    i_neut = round(i_live - leak_ma / 1000.0, 3)
    spec = _svg_earth_leakage_comparator(rng, i_live, i_neut, leak_ma)
    prompt = (
        f"Inspect the **Earth Leakage Circuit Breaker (ELCB)** schematic monitoring a domestic circuit: "
        f"Live wire current entering is **{_fmt(i_live, 3)} A**, while Neutral wire current returning is **{_fmt(i_neut, 3)} A**.\n\n"
        "1. Calculate the **leakage current** escaping to Earth in **milliamperes (mA)** [2].\n"
        "2. Explain how the Earth Leakage unit detects this fault and reacts [2]."
    )
    correct = f"Leakage = {leak_ma} mA; because Live current exceeds Neutral current by {leak_ma} mA (> 30 mA), the unit detects current leaking to Earth and immediately cuts off all mains power."
    sol = (
        f"**Step 1:** Differential current $\\Delta I = I_{{\\text{{live}}}} - I_{{\\text{{neutral}}}} = {_fmt(i_live, 3)} - {_fmt(i_neut, 3)} = {_fmt(leak_ma / 1000.0, 3)}\\text{{ A}} = {leak_ma}\\text{{ mA}}$ [2].\n\n"
        f"**Step 2:** Under normal use, $I_{{\\text{{live}}}} = I_{{\\text{{neutral}}}}$. Detecting a **{leak_ma} mA** imbalance means charge is leaking to Earth (potentially through a person), so the ELCB instantly shuts down power [2]."
    )
    return _q(
        rng, "40", "40_earth_leakage_unit_differential_current_detection",
        "Earth Leakage (ELCB) Differential Current Detection",
        prompt, correct, sol, 4, "calculation",
        ["thinking_earth_leakage_only_measures_live_wire"],
        "Compare I_live minus I_neutral, then convert amperes to milliamperes (× 1 000).",
        f"ΔI = {leak_ma} mA -> ELCB detects earth leakage and cuts power.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Calculate ΔI = {leak_ma} mA", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Explain Live vs Neutral comparison & instant power cut", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_41_earth_leakage_tripping_threshold_and_response_time(rng: random.Random) -> Dict[str, Any]:
    fault = rng.choice([
        "a child touches a wet damaged toaster frame",
        "current leaks through damp bathroom floor tiles from a faulty geyser",
        "a bare live wire brushes against a garden tap",
        "moisture enters an outdoor extension connector held by a user",
    ])
    prompt = (
        f"Suppose {fault} in a home fitted with a compliant **Earth Leakage unit**.\n\n"
        "At what approximate **leakage current** and **response speed** must the Earth Leakage switch trip to save a human life?"
    )
    correct = "Approximately 30 mA (0,03 A) within less than 30 milliseconds (0,03 s), cutting off power before fatal heart fibrillation."
    options = [
        correct,
        "Only after 15 A flows for 60 seconds so the house lights do not flicker.",
        "At 500 A after 5 minutes once copper wires melt.",
        "At 0,001 mA once every 24 hours via manual clock timer.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Standard household Earth Leakage units trip at a tiny leakage difference of **30 mA (0,03 A)**.\n\n"
        "**Step 2:** They disconnect in **under 30 milliseconds (0,03 s)** to stop current before cardiac arrest occurs."
    )
    return _q(
        rng, "41", "41_earth_leakage_tripping_threshold_and_response_time",
        "Earth Leakage Sensitivity & Tripping Speed",
        prompt, correct, sol, 2, "mcq",
        ["thinking_earth_leakage_trips_at_16A"],
        "Remember humans suffer heart fibrillation at tens of milliamperes, not 16 amperes!",
        "Trips at ~30 mA in < 30 ms.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Identify 30 mA threshold and ~30 ms speed", "marks": 2, "editable": True}],
        options=options,
    )


def arch_42_distinguishing_mcb_vs_earth_leakage_protection_roles(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        "someone plugs 4 heaters into one socket (28 A total) vs someone getting shocked by 40 mA",
        "a short circuit draws 180 A vs wet hands leaking 35 mA to ground",
        "an iron draws 24 A on a 16 A plug line vs a frayed kettle cord leaking 50 mA",
        "an oven element shorts to Neutral vs a toaster leaking 45 mA through a user",
    ])
    prompt = (
        f"Compare two emergencies on a distribution board: **{scenario}**.\n\n"
        "Clearly distinguish the primary protection role of an **MCB (or fuse)** versus an **Earth Leakage (ELCB/RCD)** unit [3]."
    )
    correct = "An MCB/fuse protects wiring and buildings from fires caused by overloads and high-current short circuits (amps); an Earth Leakage unit protects human life from electrocution by detecting tiny mA current leaks to Earth."
    sol = (
        "**Step 1 (MCB / Fuse):** Protects **cables and property** against **overload and short-circuit fires** when total current exceeds large ratings like 10 A–20 A [1].\n\n"
        "**Step 2 (Earth Leakage):** Protects **human life** against **fatal electric shock** by detecting tiny imbalances (~30 mA) leaking to Earth [2]."
    )
    return _q(
        rng, "42", "42_distinguishing_mcb_vs_earth_leakage_protection_roles",
        "MCB / Fuse vs Earth Leakage Protection Roles",
        prompt, correct, sol, 3, "structured",
        ["thinking_mcb_and_earth_leakage_do_exact_same_job"],
        "Contrast wire/fire protection (high amps) vs human shock protection (tiny milliamperes).",
        "MCB = wires/fire (overcurrent); Earth Leakage = human lives (mA leakage to ground).",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "MCB/fuse protects wiring/property against overcurrent/fires", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Earth leakage protects human life against tiny mA shock leakage", "marks": 2, "editable": True},
        ],
    )


def arch_43_lightning_rod_roof_spike_and_grounding_path(rng: random.Random) -> Dict[str, Any]:
    bldg, height_m = rng.choice([
        ("Farmhouse", 7),
        ("Rural Clinic", 9),
        ("School Hall", 11),
        ("Thatch Lodge", 8),
    ])
    spec = _svg_lightning_rod_house(rng, bldg, height_m)
    prompt = (
        f"Refer to the lightning protection setup installed on the **{bldg}** ({height_m} m high).\n\n"
        "Explain the physical **structure** and **operation** of a **lightning spike (lightning rod)** in preventing fires during storms [3]."
    )
    correct = "A tall pointed metal pole mounted above the roof connects via a thick copper conductor to a metal earthing rod buried deep underground; when lightning strikes, it offers the easiest low-resistance path straight into Earth, bypassing house wiring."
    sol = (
        "**Step 1 (Structure):** A pointed metal **lightning spike** sits at the highest point of the roof, joined by a heavy copper strip to an **earth rod buried deep underground** [1].\n\n"
        "**Step 2 (Operation):** Charge flows naturally from high to low electrical potential; the rod provides a safe, low-resistance path guiding massive lightning currents straight into the ground rather than through the roof or indoor wiring [2]."
    )
    return _q(
        rng, "43", "43_lightning_rod_roof_spike_and_grounding_path",
        "Lightning Spike Structure & Grounding Path",
        prompt, correct, sol, 3, "structured",
        ["thinking_lightning_rods_attract_strikes_inside_house"],
        "Explain both the rooftop metal spike + deep buried earthing rod, and how current bypasses the building.",
        "Metal spike + buried earth rod safely conducts lightning surge straight to ground.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Metal roof spike connected to deep buried earth rod", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Channels huge surge safely into ground bypassing house wiring", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


def arch_44_wet_hands_skin_resistance_drop_ohms_law_shock(rng: random.Random) -> Dict[str, Any]:
    r_dry = rng.choice([100000, 80000, 120000])
    r_wet = rng.choice([500, 800, 1000])
    v = 230
    i_dry_ma = round((v / r_dry) * 1000.0, 2)
    i_wet_ma = round((v / r_wet) * 1000.0, 1)
    prompt = (
        f"Dry human skin has a high electrical resistance of approximately **{r_dry:,} Ω**, whereas wet soapy skin drops to **{r_wet:,} Ω**.\n\n"
        f"Using Ohm's Law ($I = \\frac{{V}}{{R}}$) at South African mains voltage (**{v} V**), calculate the electric shock current (in **mA**) through both dry hands and wet hands, and state why wet conditions are lethal [4]."
    )
    correct = f"Dry: {_fmt(i_dry_ma, 2)} mA (mild tingle); Wet: {_fmt(i_wet_ma, 1)} mA (lethal ventricular fibrillation / cardiac arrest)."
    sol = (
        f"**Step 1 (Dry hands):** $I_{{\\text{{dry}}}} = \\frac{{{v}}}{{{r_dry}}} = {_fmt(v / r_dry, 5)}\\text{{ A}} = {_fmt(i_dry_ma, 2)}\\text{{ mA}}$ [1].\n\n"
        f"**Step 2 (Wet hands):** $I_{{\\text{{wet}}}} = \\frac{{{v}}}{{{r_wet}}} = {_fmt(v / r_wet, 3)}\\text{{ A}} = {_fmt(i_wet_ma, 1)}\\text{{ mA}}$ [2].\n\n"
        f"**Step 3:** Water with dissolved salts slashes skin resistance dramatically, letting **{_fmt(i_wet_ma, 1)} mA** surge across the chest—well above the lethal heart-fibrillation threshold [1]."
    )
    return _q(
        rng, "44", "44_wet_hands_skin_resistance_drop_ohms_law_shock",
        "Wet Skin Resistance Drop & Shock Current (Ohm's Law)",
        prompt, correct, sol, 4, "calculation",
        ["thinking_water_only_makes_plugs_rust"],
        "Calculate I = 230 / R in amperes, then multiply by 1 000 to convert to milliamperes (mA).",
        f"I_dry = {_fmt(i_dry_ma, 2)} mA; I_wet = {_fmt(i_wet_ma, 1)} mA (lethal).",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Dry current = {_fmt(i_dry_ma, 2)} mA", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Wet current = {_fmt(i_wet_ma, 1)} mA", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Explain water reduces resistance causing lethal current", "marks": 1, "editable": True},
        ],
    )


def arch_45_physiological_current_thresholds_human_body(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        (2, "1–5 mA", "Faint tingling sensation only", "Instant bone vaporization", "Immediate safe muscle relaxation", "Zero biological effect"),
        (16, "10–20 mA", "Painful muscular contraction ('can't let go' of wire)", "Gentle warming with zero grip effect", "Painless spark", "Normal harmless heartbeat"),
        (55, "30–75 mA", "Severe respiratory arrest and potentially fatal heart fibrillation", "Mild tickle on fingertips", "Harmless static pop", "Only dries skin moisture"),
        (120, "100+ mA", "Fatal ventricular fibrillation and severe internal tissue burns", "Faint tickle felt only by pets", "Instant hair drying", "Zero shock risk"),
    ])
    curr_ma, band, ok_desc, d1, d2, d3 = case
    spec = _svg_shock_current_scale(rng, curr_ma, band)
    prompt = (
        f"Refer to the body current severity scale marking a shock current of **{curr_ma} mA** passing through the human chest.\n\n"
        f"Which physiological effect corresponds to **{curr_ma} mA**?"
    )
    options = [ok_desc, d1, d2, d3]
    rng.shuffle(options)
    sol = (
        "**Electric Shock Current Thresholds:**\n"
        "- 1–5 mA: Mild tingling\n"
        "- 10–20 mA: Painful involuntary muscle contraction ('can't let go')\n"
        "- 30–75 mA: Breathing paralysis / life-threatening cardiac risk\n"
        "- 100+ mA: Fatal ventricular fibrillation & burns\n\n"
        f"**Conclusion:** At **{curr_ma} mA** ({band}), the effect is **{ok_desc}**."
    )
    return _q(
        rng, "45", "45_physiological_current_thresholds_human_body",
        "Physiological Effects of Electric Shock Currents",
        prompt, ok_desc, sol, 2, "mcq",
        ["thinking_voltage_alone_determines_harm_without_current"],
        f"Locate {curr_ma} mA on the severity scale ({band}).",
        f"{curr_ma} mA -> {ok_desc}.",
        ok_desc,
        marking_points=[{"id": "mp_1", "desc": f"Correct effect for {curr_ma} mA", "marks": 2, "editable": True}],
        options=options,
        diagram_spec=spec,
    )


def arch_46_damaged_frayed_cords_and_carpet_routing_hazards(rng: random.Random) -> Dict[str, Any]:
    appliance = rng.choice(["electric heater", "office kettle", "floor lamp", "extension lead"])
    prompt = (
        f"A learner notices a cracked, frayed power cord on a **{appliance}** wrapped temporarily with sticky PVC insulation tape, "
        "and routed underneath a heavy wool lounge carpet.\n\n"
        "Explain **two serious safety hazards** created by this arrangement [2]."
    )
    correct = "1) Frayed cords patched with tape expose live copper if tape peels, risking electrocution or short circuits (damaged cords must be replaced properly); 2) Cords hidden under carpets suffer unseen foot-traffic crushing and trapped heat, causing fire."
    sol = (
        "**Step 1 (Frayed Cord / Tape):** Insulation tape is NOT a permanent safe repair—damaged cords must be replaced completely so exposed copper cannot cause shocks or short circuits [1].\n\n"
        "**Step 2 (Under Carpets):** Foot traffic crushes unseen insulation under carpets while the carpet traps heat, causing overheating and hidden fires [1]."
    )
    return _q(
        rng, "46", "46_damaged_frayed_cords_and_carpet_routing_hazards",
        "Damaged Power Cords & Carpet Routing Hazards",
        prompt, correct, sol, 2, "short_answer",
        ["thinking_sticky_tape_permanently_repairs_frayed_cords"],
        "Think about wear-and-tear under footsteps + trapped heat + peeling tape.",
        "Replace damaged cords (never tape permanently); never hide cords under carpets.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Tape is unsafe temporary fix; replace frayed cord", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Carpet crushes insulation unseen & traps fire heat", "marks": 1, "editable": True},
        ],
    )


def arch_47_illegal_connections_definition_and_energy_theft(rng: random.Random) -> Dict[str, Any]:
    actor = rng.choice(["an unauthorized connector", "an unmetered overhead tap", "a bypassed municipal meter", "an unlicensed backyard tap"])
    prompt = (
        f"In several South African neighbourhoods, households receive power via **{actor}** attached directly to overhead municipal or Eskom distribution lines without a meter.\n\n"
        "Aside from physical injury hazards, why are **illegal electricity connections** criminalized?"
    )
    correct = "They constitute energy theft: electricity is consumed without utility consent or metering, causing severe revenue losses to Eskom and municipalities and overloading local transformers."
    options = [
        correct,
        "Because legal meters turn alternating current into harmless distilled water.",
        "Because utility poles only carry electricity on weekends.",
        "Because unpaid electrons travel faster than legal paid electrons.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Attaching a home circuit to the national grid without an electricity meter or Eskom/municipal authorization is **energy theft**.\n\n"
        "**Step 2:** Unpaid consumption causes financial losses for utilities, starves infrastructure maintenance, and triggers unmonitored transformer overloads."
    )
    return _q(
        rng, "47", "47_illegal_connections_definition_and_energy_theft",
        "Illegal Connections as Energy Theft & Utility Impact",
        prompt, correct, sol, 2, "mcq",
        ["thinking_illegal_connections_only_affect_one_wire"],
        "Think about metering, payment, utility revenue (Eskom/municipality), and grid load.",
        "Energy theft bypassing meters causes utility revenue loss and transformer overloads.",
        correct,
        marking_points=[{"id": "mp_1", "desc": "Identify energy theft and utility revenue/grid impact", "marks": 2, "editable": True}],
        options=options,
    )


def arch_48_illegal_connections_physical_dangers_exposed_wires(rng: random.Random) -> Dict[str, Any]:
    place = rng.choice(["wet footpath near corrugated-iron dwellings", "school playground perimeter", "muddy alley beside metal roofs", "busy neighbourhood crossing"])
    prompt = (
        f"Unqualified individuals have strung makeshift wires from a street pole across a **{place}** without fuses, circuit breakers, or earth leakage protection.\n\n"
        "Identify **three physical dangers** these illegal connections pose to residents, children, and passers-by [3]."
    )
    correct = "1) Uninsulated/thin wires lying on wet ground electrocute children and pedestrians; 2) Unprotected joints spark and ignite devastating shack/building fires; 3) Makeshift poles collapse or live metal roofs become energized."
    sol = (
        "**Three Physical Dangers:**\n"
        "1. **Fatal electrocution:** Bare or thinly insulated wires on wet footpaths shock children, pedestrians, and pets [1].\n"
        "2. **Fires:** No fuses/breakers exist to stop overloads, igniting rapid fires in nearby dwellings [1].\n"
        "3. **Structural/contact hazards:** Makeshift poles topple and live wires can energize metal sheeting [1]."
    )
    return _q(
        rng, "48", "48_illegal_connections_physical_dangers_exposed_wires",
        "Physical Dangers of Illegal Electricity Connections",
        prompt, correct, sol, 3, "short_answer",
        ["underestimating_illegal_wire_electrocution_risk"],
        "Consider bare wires on wet ground, absence of breakers/fuses, and metal roofs.",
        "Electrocution of pedestrians/children, uncontrolled fires, collapsing poles/live metal.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": "Electrocution from bare/wet ground wires", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Fire hazard without fuses/breakers", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Unstable makeshift poles / live metal structures", "marks": 1, "editable": True},
        ],
    )


def arch_49_doornbach_case_study_low_hanging_wires_and_land_tenure(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice([
        ("low-hanging wires strung across Potsdam Road", "passing trucks snagged and snapped live wires, endangering pedestrians and motorists"),
        ("legal land-tenure restriction prior to May 2011", "the City could not legally install municipal infrastructure on privately owned land until purchasing it"),
        ("switching from paraffin stoves and candles to legal electricity", "legal supply drastically reduced devastating shack fires and indoor smoke"),
        ("youth climbing makeshift poles to strip scrap wire", "extreme risk of fatal electrocution and falling from unstable poles"),
    ])
    topic_a, answer_a = aspect
    prompt = (
        "In the **Doornbach informal settlement** (near Cape Town) case study, residents celebrated receiving ~200 legal municipal electricity connections "
        "and immediately cut down the dangerous web of illegal overhead wires.\n\n"
        f"1. Explain the significance of **{topic_a}** in the Doornbach case study [2].\n"
        "2. Why did the City also install street lighting alongside legal household connections [1]?"
    )
    correct = f"1) {answer_a}; 2) Street lighting improves night visibility and helps reduce local crime."
    sol = (
        f"**Step 1:** Regarding **{topic_a}**: {answer_a} [2].\n\n"
        "**Step 2:** Installing public **street lighting** improves community safety and helps reduce local crime rates [1]."
    )
    return _q(
        rng, "49", "49_doornbach_case_study_low_hanging_wires_and_land_tenure",
        "Doornbach Informal Settlement Electrification Case Study",
        prompt, correct, sol, 3, "structured",
        ["ignoring_socioeconomic_land_tenure_context"],
        f"Recall the Doornbach settlement facts on {topic_a} and community street lighting.",
        f"{answer_a}; street lights reduce crime.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Accurate explanation of {topic_a}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Street lighting reduces crime", "marks": 1, "editable": True},
        ],
    )


def arch_50_community_safety_audit_distribution_board_and_grid(rng: random.Random) -> Dict[str, Any]:
    tripped = rng.choice(["ELCB", "Plugs", "Lights"])
    elcb_ma = 30
    lights_a = rng.choice([10, 15])
    plugs_a = rng.choice([16, 20])
    spec = _svg_distribution_board(rng, tripped, elcb_ma, lights_a, plugs_a)
    if tripped == "ELCB":
        meaning = f"the {elcb_ma} mA Earth Leakage detected current leaking to Earth (e.g. damp appliance or human contact)"
    elif tripped == "Plugs":
        meaning = f"the {plugs_a} A Plugs MCB detected an overload or short circuit on wall sockets"
    else:
        meaning = f"the {lights_a} A Lights MCB detected a short circuit or overload on ceiling lighting"
    prompt = (
        f"Examine the household Distribution Board (DB) schematic showing **{tripped}** in the **TRIPPED** state.\n\n"
        f"1. Diagnose the exact type of fault indicated by **{tripped}** tripping [2].\n"
        "2. State **two safe actions** the homeowner must take before resetting the switch, and state how a certified electrician verifies legal house wiring before property sale [2]."
    )
    correct = f"Fault diagnosis: {meaning}. Safe steps: unplug/inspect faulty appliances and fix the wiring fault before resetting (never bypass with wire). Certification: licensed electrician issues a Certificate of Compliance (CoC)."
    sol = (
        f"**Step 1 (Diagnosis):** **{tripped}** tripping indicates **{meaning}** [2].\n\n"
        "**Step 2 (Safe Procedure & Compliance):** Disconnect suspect appliances, have the fault repaired before resetting the switch [1], "
        "and ensure legal household wiring meets safety legislation via a certified electrician's **compliance inspection** [1]."
    )
    return _q(
        rng, "50", "50_community_safety_audit_distribution_board_and_grid",
        "Comprehensive Household DB & Electrical Safety Audit",
        prompt, correct, sol, 4, "structured",
        ["confusing_elcb_trip_with_lights_mcb_trip"],
        f"Read which switch is TRIPPED ({tripped}): ELCB = earth leakage; MCB = overload/short.",
        f"{tripped} tripped -> {meaning}; fix fault before reset + certified inspection.",
        correct,
        marking_points=[
            {"id": "mp_1", "desc": f"Correct fault diagnosis for {tripped} trip", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Unplug/repair before resetting + certified electrician compliance check", "marks": 2, "editable": True},
        ],
        diagram_spec=spec,
    )


BUILDERS_26_50 = {
    "26_three_pin_plug_wire_colour_codes_identification": arch_26_three_pin_plug_wire_colour_codes_identification,
    "27_live_neutral_earth_wire_electrical_functions": arch_27_live_neutral_earth_wire_electrical_functions,
    "28_three_pin_plug_terminal_pin_positions_opened_view": arch_28_three_pin_plug_terminal_pin_positions_opened_view,
    "29_fuse_mandatory_placement_on_live_wire": arch_29_fuse_mandatory_placement_on_live_wire,
    "30_longer_thicker_earth_pin_safety_engineering": arch_30_longer_thicker_earth_pin_safety_engineering,
    "31_three_pin_plug_cord_stripping_and_strand_twisting": arch_31_three_pin_plug_cord_stripping_and_strand_twisting,
    "32_loose_strands_and_cord_grip_clamp_function": arch_32_loose_strands_and_cord_grip_clamp_function,
    "33_diagnosing_miswired_three_pin_plug_hazards": arch_33_diagnosing_miswired_three_pin_plug_hazards,
    "34_double_insulation_two_pin_plug_appliances": arch_34_double_insulation_two_pin_plug_appliances,
    "35_plug_wiring_general_safety_precautions": arch_35_plug_wiring_general_safety_precautions,
    "36_earthing_metal_casing_fault_protection_mechanism": arch_36_earthing_metal_casing_fault_protection_mechanism,
    "37_earth_wire_near_zero_resistance_ohms_law": arch_37_earth_wire_near_zero_resistance_ohms_law,
    "38_ungrounded_faulty_metal_appliance_shock_risk": arch_38_ungrounded_faulty_metal_appliance_shock_risk,
    "39_neutral_wire_earthed_leaving_house_grid_protection": arch_39_neutral_wire_earthed_leaving_house_grid_protection,
    "40_earth_leakage_unit_differential_current_detection": arch_40_earth_leakage_unit_differential_current_detection,
    "41_earth_leakage_tripping_threshold_and_response_time": arch_41_earth_leakage_tripping_threshold_and_response_time,
    "42_distinguishing_mcb_vs_earth_leakage_protection_roles": arch_42_distinguishing_mcb_vs_earth_leakage_protection_roles,
    "43_lightning_rod_roof_spike_and_grounding_path": arch_43_lightning_rod_roof_spike_and_grounding_path,
    "44_wet_hands_skin_resistance_drop_ohms_law_shock": arch_44_wet_hands_skin_resistance_drop_ohms_law_shock,
    "45_physiological_current_thresholds_human_body": arch_45_physiological_current_thresholds_human_body,
    "46_damaged_frayed_cords_and_carpet_routing_hazards": arch_46_damaged_frayed_cords_and_carpet_routing_hazards,
    "47_illegal_connections_definition_and_energy_theft": arch_47_illegal_connections_definition_and_energy_theft,
    "48_illegal_connections_physical_dangers_exposed_wires": arch_48_illegal_connections_physical_dangers_exposed_wires,
    "49_doornbach_case_study_low_hanging_wires_and_land_tenure": arch_49_doornbach_case_study_low_hanging_wires_and_land_tenure,
    "50_community_safety_audit_distribution_board_and_grid": arch_50_community_safety_audit_distribution_board_and_grid,
}
