"""Grade 9 Natural Sciences - Series and Parallel Circuits: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .series_parallel_circuits_archetypes_01_25 import _fmt, _q


def _svg_parallel_current_graph(rng: random.Random, i_base: float) -> Dict[str, Any]:
    """Draw a Current (A) vs Number of Parallel Bulbs line graph."""
    pts = [(1, round(i_base, 2)), (2, round(2 * i_base, 2)), (3, round(3 * i_base, 2))]
    max_y_val = round(4 * i_base, 2)
    coords = []
    dots = []
    for n, val in pts:
        px = 95 + (n - 1) * 95
        py = 160 - int((val / max_y_val) * 115)
        coords.append(f"{px},{py}")
        dots.append(
            f'<circle cx="{px}" cy="{py}" r="4.5" fill="#1d4ed8"/>'
            f'<text x="{px}" y="{py - 10}" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">({n}; {_fmt(val, 2)} A)</text>'
            f'<text x="{px}" y="177" font-size="11" fill="#0f172a" text-anchor="middle">{n}</text>'
        )
    # 4th x tick for prediction
    dots.append('<text x="380" y="177" font-size="11" fill="#dc2626" font-weight="bold" text-anchor="middle">4 (?)</text>')
    svg = (
        f'<svg viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="210" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<text x="225" y="22" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Total Current vs Number of Identical Parallel Bulbs</text>'
        f'<line x1="65" y1="35" x2="65" y2="160" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="160" x2="405" y2="160" stroke="#0f172a" stroke-width="2"/>'
        f'<polyline points="{" ".join(coords)}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'{"".join(dots)}'
        f'<text x="235" y="196" font-size="10.5" fill="#475569" text-anchor="middle">Number of parallel branches</text>'
        f'<text x="18" y="102" font-size="10.5" fill="#475569" text-anchor="middle" transform="rotate(-90 18 102)">I_total (A)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_parallel_two_resistors(
    rng: random.Random, v_bat: int, r1: int, r2: int, show_voltmeter: bool = False
) -> Dict[str, Any]:
    """Draw a two-branch parallel resistor circuit with optional parallel voltmeter."""
    vm = ""
    if show_voltmeter:
        vm = (
            f'<line x1="150" y1="185" x2="150" y2="215" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,3"/>'
            f'<line x1="300" y1="185" x2="300" y2="215" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,3"/>'
            f'<line x1="150" y1="215" x2="300" y2="215" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,3"/>'
            f'<circle cx="225" cy="215" r="14" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>'
            f'<text x="225" y="219" font-size="11.5" font-weight="bold" fill="#991b1b" text-anchor="middle">V</text>'
        )
    h = 240 if show_voltmeter else 210
    svg = (
        f'<svg viewBox="0 0 440 {h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="{h}" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<line x1="75" y1="48" x2="365" y2="48" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="75" y1="48" x2="75" y2="185" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="365" y1="48" x2="365" y2="185" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="75" y1="120" x2="365" y2="120" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="75" y1="185" x2="365" y2="185" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="195" y="30" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="210" y1="30" x2="210" y2="66" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="38" x2="226" y2="58" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="22" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Battery</text>'
        f'<rect x="182" y="108" width="76" height="24" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="220" y="124" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">R1 = {r1} Ω</text>'
        f'<rect x="182" y="173" width="76" height="24" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="220" y="189" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">R2 = {r2} Ω</text>'
        f'{vm}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_parallel_branch_switch(rng: random.Random, v_bat: int, open_branch: str) -> Dict[str, Any]:
    """Draw a two-branch parallel bulb circuit with switches S1 and S2 where one branch switch is open."""
    s1_line = f'<line x1="125" y1="115" x2="165" y2="115" stroke="#16a34a" stroke-width="2.5"/>' if open_branch != "S1" else f'<line x1="125" y1="115" x2="160" y2="96" stroke="#dc2626" stroke-width="2.5"/>'
    s2_line = f'<line x1="125" y1="178" x2="165" y2="178" stroke="#16a34a" stroke-width="2.5"/>' if open_branch != "S2" else f'<line x1="125" y1="178" x2="160" y2="159" stroke="#dc2626" stroke-width="2.5"/>'
    b1_fill = "#e2e8f0" if open_branch == "S1" else "#fef08a"
    b2_fill = "#e2e8f0" if open_branch == "S2" else "#fef08a"
    svg = (
        f'<svg viewBox="0 0 440 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="215" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<line x1="70" y1="45" x2="370" y2="45" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="70" y1="45" x2="70" y2="178" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="370" y1="45" x2="370" y2="178" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="70" y1="115" x2="125" y2="115" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="165" y1="115" x2="370" y2="115" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="70" y1="178" x2="125" y2="178" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="165" y1="178" x2="370" y2="178" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="195" y="28" width="50" height="34" fill="#ffffff"/>'
        f'<line x1="210" y1="28" x2="210" y2="62" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="36" x2="226" y2="54" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="21" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Parallel Circuit</text>'
        f'{s1_line}<circle cx="125" cy="115" r="3.5" fill="#0f172a"/><circle cx="165" cy="115" r="3.5" fill="#0f172a"/>'
        f'<text x="145" y="133" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">S1</text>'
        f'{s2_line}<circle cx="125" cy="178" r="3.5" fill="#0f172a"/><circle cx="165" cy="178" r="3.5" fill="#0f172a"/>'
        f'<text x="145" y="196" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">S2</text>'
        f'<circle cx="275" cy="115" r="14" fill="{b1_fill}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="305" y="119" font-size="11" font-weight="bold" fill="#0f172a">B1</text>'
        f'<circle cx="275" cy="178" r="14" fill="{b2_fill}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="305" y="182" font-size="11" font-weight="bold" fill="#0f172a">B2</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_cells_parallel(rng: random.Random, n_cells: int, cell_v: float) -> Dict[str, Any]:
    """Draw n_cells connected in parallel (+ to +, - to -) powering a single bulb."""
    ys = [42, 82] if n_cells == 2 else [36, 72, 108]
    rows = []
    for idx, cy in enumerate(ys, 1):
        rows.append(
            f'<line x1="125" y1="{cy}" x2="210" y2="{cy}" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="230" y1="{cy}" x2="315" y2="{cy}" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="210" y1="{cy - 12}" x2="210" y2="{cy + 12}" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="224" y1="{cy - 6}" x2="224" y2="{cy + 6}" stroke="#dc2626" stroke-width="4.5"/>'
            f'<line x1="224" y1="{cy}" x2="230" y2="{cy}" stroke="#0f172a" stroke-width="2"/>'
            f'<text x="196" y="{cy + 4}" font-size="9.5" fill="#475569" text-anchor="end">Cell {idx}</text>'
        )
    top_y, bot_y = ys[0], ys[-1]
    svg = (
        f'<svg viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="200" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<line x1="125" y1="{top_y}" x2="125" y2="162" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="315" y1="{top_y}" x2="315" y2="162" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="125" y1="162" x2="315" y2="162" stroke="#0f172a" stroke-width="2.5"/>'
        f'{"".join(rows)}'
        f'<circle cx="220" cy="162" r="14" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="211" y1="153" x2="229" y2="171" stroke="#0f172a" stroke-width="1.6"/>'
        f'<line x1="211" y1="171" x2="229" y2="153" stroke="#0f172a" stroke-width="1.6"/>'
        f'<text x="220" y="190" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{n_cells} x {_fmt(cell_v, 1)} V Cells in Parallel</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_mixed_abc(rng: random.Random, v_bat: int, switch_open: bool) -> Dict[str, Any]:
    """Draw mixed circuit: main-line Bulb A in series with parallel Bulbs B and C (Switch S in branch C)."""
    sw_svg = (
        f'<line x1="175" y1="186" x2="208" y2="168" stroke="#dc2626" stroke-width="2.5"/>'
        if switch_open
        else f'<line x1="175" y1="186" x2="215" y2="186" stroke="#16a34a" stroke-width="2.5"/>'
    )
    c_fill = "#e2e8f0" if switch_open else "#fef9c3"
    svg = (
        f'<svg viewBox="0 0 440 225" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="225" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        # Top battery wire + Bulb A in main series line
        f'<line x1="65" y1="48" x2="375" y2="48" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="65" y1="48" x2="65" y2="186" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="375" y1="48" x2="375" y2="186" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="130" y="30" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="145" y1="30" x2="145" y2="66" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="161" y1="38" x2="161" y2="58" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="155" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V</text>'
        # Bulb A on main top wire
        f'<circle cx="290" cy="48" r="15" fill="#facc15" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="280" y1="38" x2="300" y2="58" stroke="#0f172a" stroke-width="1.8"/>'
        f'<line x1="280" y1="58" x2="300" y2="38" stroke="#0f172a" stroke-width="1.8"/>'
        f'<text x="290" y="25" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Bulb A</text>'
        # Parallel branches for B (y=122) and C (y=186)
        f'<line x1="65" y1="122" x2="375" y2="122" stroke="#0f172a" stroke-width="2.5"/>'
        f'<circle cx="220" cy="122" r="14" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="211" y1="113" x2="229" y2="131" stroke="#0f172a" stroke-width="1.6"/>'
        f'<line x1="211" y1="131" x2="229" y2="113" stroke="#0f172a" stroke-width="1.6"/>'
        f'<text x="248" y="126" font-size="11" font-weight="bold" fill="#0f172a">Bulb B</text>'
        f'<line x1="65" y1="186" x2="175" y2="186" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="215" y1="186" x2="375" y2="186" stroke="#0f172a" stroke-width="2.5"/>'
        f'{sw_svg}<circle cx="175" cy="186" r="3.5" fill="#0f172a"/><circle cx="215" cy="186" r="3.5" fill="#0f172a"/>'
        f'<text x="195" y="206" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Switch S</text>'
        f'<circle cx="290" cy="186" r="14" fill="{c_fill}" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="281" y1="177" x2="299" y2="195" stroke="#0f172a" stroke-width="1.6"/>'
        f'<line x1="281" y1="195" x2="299" y2="177" stroke="#0f172a" stroke-width="1.6"/>'
        f'<text x="318" y="190" font-size="11" font-weight="bold" fill="#0f172a">Bulb C</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_mixed_resistors(rng: random.Random, v_bat: int, r_s: int, r_p1: int, r_p2: int) -> Dict[str, Any]:
    """Draw combination circuit: R_s in series with parallel pair R_p1 || R_p2."""
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="220" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<line x1="65" y1="48" x2="375" y2="48" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="65" y1="48" x2="65" y2="155" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="375" y1="48" x2="375" y2="155" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="65" y1="155" x2="205" y2="155" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="205" y1="118" x2="375" y2="118" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="205" y1="188" x2="375" y2="188" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="205" y1="118" x2="205" y2="188" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="375" y1="118" x2="375" y2="188" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="195" y="30" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="210" y1="30" x2="210" y2="66" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="38" x2="226" y2="58" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Source</text>'
        f'<rect x="100" y="143" width="76" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="138" y="159" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">Rs = {r_s} Ω</text>'
        f'<rect x="252" y="106" width="76" height="24" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="290" y="122" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Rp1 = {r_p1} Ω</text>'
        f'<rect x="252" y="176" width="76" height="24" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="290" y="192" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Rp2 = {r_p2} Ω</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_sankey_single(
    rng: random.Random, device_name: str, e_in: int, e_useful: int, useful_lbl: str, wasted_lbl: str
) -> Dict[str, Any]:
    """Draw a proportional Sankey diagram for an electrical output device."""
    e_wasted = e_in - e_useful
    h_u = max(16, int(92 * (e_useful / float(e_in))))
    h_w = max(16, 92 - h_u)
    svg = (
        f'<svg viewBox="0 0 440 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="205" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<text x="220" y="23" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Sankey Energy Flow: {device_name}</text>'
        f'<rect x="35" y="58" width="150" height="92" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="1.8"/>'
        f'<text x="110" y="108" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Input: {e_in} J</text>'
        f'<rect x="185" y="58" width="215" height="{h_u}" fill="#bbf7d0" stroke="#15803d" stroke-width="1.8"/>'
        f'<text x="292" y="{58 + h_u // 2 + 4}" font-size="10.5" font-weight="bold" fill="#14532d" text-anchor="middle">{useful_lbl}: {e_useful} J</text>'
        f'<rect x="185" y="{58 + h_u + 8}" width="215" height="{h_w}" fill="#fecaca" stroke="#b91c1c" stroke-width="1.8"/>'
        f'<text x="292" y="{58 + h_u + 8 + h_w // 2 + 4}" font-size="10.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">{wasted_lbl}: {e_wasted} J</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_sankey_compare(rng: random.Random, e_in: int, led_u: int, fil_u: int) -> Dict[str, Any]:
    """Side-by-side Sankey diagram comparing LED Lamp vs Filament Bulb."""
    led_hu = max(14, int(72 * (led_u / float(e_in))))
    led_hw = max(14, 72 - led_hu)
    fil_hu = max(14, int(72 * (fil_u / float(e_in))))
    fil_hw = max(14, 72 - fil_hu)
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="220" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<text x="220" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Device A (LED) vs Device B (Filament Bulb)</text>'
        # Top: LED
        f'<text x="20" y="42" font-size="10.5" font-weight="bold" fill="#15803d">LED Lamp (Input {e_in} J)</text>'
        f'<rect x="20" y="48" width="120" height="72" fill="#bfdbfe" stroke="#1d4ed8"/>'
        f'<rect x="140" y="48" width="265" height="{led_hu}" fill="#fde047" stroke="#ca8a04"/>'
        f'<text x="272" y="{48 + led_hu // 2 + 4}" font-size="10" font-weight="bold" fill="#713f12" text-anchor="middle">Light: {led_u} J</text>'
        f'<rect x="140" y="{48 + led_hu + 4}" width="265" height="{led_hw}" fill="#fecaca" stroke="#b91c1c"/>'
        f'<text x="272" y="{48 + led_hu + 4 + led_hw // 2 + 4}" font-size="10" font-weight="bold" fill="#7f1d1d" text-anchor="middle">Heat: {e_in - led_u} J</text>'
        # Bottom: Filament
        f'<text x="20" y="136" font-size="10.5" font-weight="bold" fill="#991b1b">Filament Bulb (Input {e_in} J)</text>'
        f'<rect x="20" y="142" width="120" height="72" fill="#bfdbfe" stroke="#1d4ed8"/>'
        f'<rect x="140" y="142" width="265" height="{fil_hu}" fill="#fde047" stroke="#ca8a04"/>'
        f'<text x="272" y="{142 + fil_hu // 2 + 4}" font-size="10" font-weight="bold" fill="#713f12" text-anchor="middle">Light: {fil_u} J</text>'
        f'<rect x="140" y="{142 + fil_hu + 4}" width="265" height="{fil_hw}" fill="#fecaca" stroke="#b91c1c"/>'
        f'<text x="272" y="{142 + fil_hu + 4 + fil_hw // 2 + 4}" font-size="10" font-weight="bold" fill="#7f1d1d" text-anchor="middle">Heat: {e_in - fil_u} J</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ---------------------------------------------------------------------------
# Archetypes 26 to 50
# ---------------------------------------------------------------------------

def arch_26_interpreting_parallel_results_table_and_line_graph(rng: random.Random) -> Dict[str, Any]:
    i_base = rng.choice([0.15, 0.20, 0.25, 0.30])
    i_pred = round(4 * i_base, 2)
    prompt = (
        f"Observe the investigation graph plotting **total circuit current** against the number of identical parallel branches "
        f"(1 branch = {_fmt(i_base, 2)} A, 2 branches = {_fmt(2 * i_base, 2)} A, 3 branches = {_fmt(3 * i_base, 2)} A).\n\n"
        "Predict the total ammeter reading when a **4th identical bulb** is connected in parallel, and state the trend [2]."
    )
    correct = f"{_fmt(i_pred, 2)} A (total current increases linearly as parallel branches are added)"
    sol = (
        f"Step 1: Each identical branch draws ${_fmt(i_base, 2)}\\text{{ A}}$ across the constant supply voltage.\n"
        f"Step 2: For 4 branches: $I_{{\\text{{total}}}} = 4 \\times {_fmt(i_base, 2)}\\text{{ A}} = {_fmt(i_pred, 2)}\\text{{ A}}$ [2]."
    )
    return _q(
        rng, "26", "26_interpreting_parallel_results_table_and_line_graph", prompt, correct, sol, 2, "math_short",
        ["predicting_current_drops_when_adding_parallel_branches"],
        "Notice the constant step increase for each extra identical parallel bulb.",
        f"Multiply the single-branch current ({_fmt(i_base, 2)} A) by 4.",
        correct, diagram_spec=_svg_parallel_current_graph(rng, i_base),
    )


def arch_27_calculating_equivalent_parallel_resistance_two_resistors(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([(6, 6), (4, 12), (6, 12), (10, 15), (12, 24)])
    r1, r2 = pair
    r_p = round((r1 * r2) / float(r1 + r2), 2)
    v_bat = rng.choice([12, 24])
    prompt = (
        f"In the parallel circuit shown, resistors **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** are connected across a {v_bat} V battery.\n\n"
        "Calculate the **equivalent parallel resistance** ($R_p$) using $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$ [3]."
    )
    correct = f"{_fmt(r_p, 1)} Ω" if r_p == round(r_p, 1) else f"{_fmt(r_p, 2)} Ω"
    sol = (
        f"Step 1: $\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} = \\frac{{{r1 + r2}}}{{{r1 * r2}}}$ [2].\n"
        f"Step 2: Invert to find $R_p = \\frac{{{r1 * r2}}}{{{r1 + r2}}} = {correct}$ (always smaller than {min(r1, r2)} $\\Omega$) [1]."
    )
    return _q(
        rng, "27", "27_calculating_equivalent_parallel_resistance_two_resistors", prompt, correct, sol, 3, "math_short",
        ["adding_parallel_resistors_directly_without_reciprocals", "forgetting_to_invert_1_over_rp"],
        "Use 1/Rp = 1/R1 + 1/R2 and remember to take the reciprocal at the end!",
        f"Rp = ({r1} × {r2}) / ({r1} + {r2}) = {correct}.",
        correct, diagram_spec=_svg_parallel_two_resistors(rng, v_bat, r1, r2),
    )


def arch_28_ohms_law_in_parallel_constant_branch_voltage(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([12, 24])
    r1 = rng.choice([4, 6])
    r2 = rng.choice([8, 12])
    i1 = round(v_bat / float(r1), 1)
    i2 = round(v_bat / float(r2), 1)
    prompt = (
        f"In the parallel circuit schematic, a voltmeter (**V**) across the lower resistor $R_2 = {r2}\\ \\Omega$ measures **{v_bat} V**, "
        f"and the upper branch holds $R_1 = {r1}\\ \\Omega$.\n\n"
        "1. State the potential difference across $R_1$ [1].\n"
        "2. Calculate the branch currents $I_1$ (through $R_1$) and $I_2$ (through $R_2$) [2]."
    )
    correct = f"V1 = {v_bat} V; I1 = {_fmt(i1, 1)} A and I2 = {_fmt(i2, 1)} A"
    sol = (
        f"1. **Parallel Voltage:** Every parallel branch receives full supply voltage, so $V_1 = {v_bat}\\text{{ V}}$ [1].\n"
        f"2. **Branch Currents:** $I_1 = \\frac{{{v_bat}}}{{{r1}}} = {_fmt(i1, 1)}\\text{{ A}}$ and $I_2 = \\frac{{{v_bat}}}{{{r2}}} = {_fmt(i2, 1)}\\text{{ A}}$ [2]."
    )
    return _q(
        rng, "28", "28_ohms_law_in_parallel_constant_branch_voltage", prompt, correct, sol, 3, "math_short",
        ["splitting_voltage_equally_across_parallel_branches_myth"],
        "In a parallel circuit, is potential difference split across branches or identical across every branch?",
        f"Both R1 and R2 receive {v_bat} V; divide V by each branch resistance.",
        correct, diagram_spec=_svg_parallel_two_resistors(rng, v_bat, r1, r2, show_voltmeter=True),
    )


def arch_29_parallel_circuit_fault_isolation_and_switch_control(rng: random.Random) -> Dict[str, Any]:
    open_sw = rng.choice(["S1", "S2"])
    lit_bulb = "B2" if open_sw == "S1" else "B1"
    dark_bulb = "B1" if open_sw == "S1" else "B2"
    v_bat = rng.choice([6, 9, 12])
    prompt = (
        f"Examine the {v_bat} V parallel circuit schematic where switch **{open_sw}** is open while the other branch switch remains closed.\n\n"
        f"What is observed for bulbs **B1** and **B2**, and why?"
    )
    correct = f"Bulb {dark_bulb} switches off because its branch is open, while bulb {lit_bulb} stays glowing at normal brightness on its own independent closed loop."
    options = [
        correct,
        f"Both B1 and B2 extinguish completely because opening {open_sw} cuts off the entire battery.",
        f"Bulb {lit_bulb} doubles in brightness because all current from {dark_bulb} forces its way into {lit_bulb}.",
        f"Bulb {dark_bulb} stays dimly lit while bulb {lit_bulb} switches off.",
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Opening {open_sw} breaks only the {dark_bulb} branch.\n"
        f"Step 2: Bulb {lit_bulb} retains an unbroken closed pathway across the {v_bat} V supply and stays lit at normal brightness."
    )
    return _q(
        rng, "29", "29_parallel_circuit_fault_isolation_and_switch_control", prompt, correct, sol, 2, "mcq",
        ["parallel_bulbs_go_out_when_one_branch_opens_myth"],
        "Trace an unbroken loop from the battery through each bulb separately.",
        f"Only the branch with open switch {open_sw} loses current; the closed branch operates independently.",
        correct, options=options, diagram_spec=_svg_parallel_branch_switch(rng, v_bat, open_sw),
    )


def arch_30_cells_in_parallel_connection_polarity_rule(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3])
    prompt = (
        f"A Grade 9 group needs to connect **{n_cells} identical 1,5 V dry cells in parallel** during a laboratory practical.\n\n"
        "Which wiring rule correctly connects cells in a parallel configuration?"
    )
    correct = "Connect all positive (+) terminals together to one junction wire, and connect all negative (-) terminals together to the opposite junction wire."
    options = [
        correct,
        "Connect the positive (+) terminal of Cell 1 to the negative (-) terminal of Cell 2 in a single chain.",
        "Connect all positive (+) terminals directly to all negative (-) terminals to form a loop without a bulb.",
        "Leave one terminal of each cell disconnected in open air.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Parallel connection places components across the same two electrical nodes.\n"
        "Step 2: Join all (+) terminals to the positive node and all (-) terminals to the negative node."
    )
    return _q(
        rng, "30", "30_cells_in_parallel_connection_polarity_rule", prompt, correct, sol, 2, "mcq",
        ["wiring_cells_pos_to_neg_when_parallel_requested"],
        "Positive-to-negative chaining is series. How must terminals match in parallel?",
        "Like-to-like: (+ to +) and (- to -).",
        correct, options=options,
    )


def arch_31_cells_in_parallel_no_increase_in_current_or_voltage(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3])
    cell_v = 1.5
    i_single = rng.choice([0.12, 0.15, 0.20, 0.25])
    prompt = (
        f"A circuit with **1 cell** ({_fmt(cell_v, 1)} V) produces an ammeter reading of **{_fmt(i_single, 2)} A** through a torch bulb. "
        f"The learner now connects **{n_cells} identical 1,5 V cells in parallel** as shown.\n\n"
        f"1. State the resulting ammeter reading and bulb brightness [2].\n"
        f"2. State one practical benefit of wiring cells in parallel [1]."
    )
    correct = f"{_fmt(i_single, 2)} A (unchanged brightness); cells last longer"
    sol = (
        f"1. **Voltage & Current:** {n_cells} identical {_fmt(cell_v, 1)} V cells in parallel supply only **1,5 V** total, so current remains **{_fmt(i_single, 2)} A** and bulb brightness stays **unchanged** [2].\n"
        "2. **Benefit:** Because the current demand is shared across the cells, the battery pack supplies energy for **much longer** before running flat [1]."
    )
    return _q(
        rng, "31", "31_cells_in_parallel_no_increase_in_current_or_voltage", prompt, correct, sol, 3, "math_short",
        ["thinking_cells_in_parallel_multiply_voltage_and_current"],
        "Does connecting identical 1,5 V cells in parallel increase total potential difference above 1,5 V?",
        f"Total voltage stays 1,5 V, so current remains {_fmt(i_single, 2)} A, while battery lifespan increases.",
        correct, diagram_spec=_svg_cells_parallel(rng, n_cells, cell_v),
    )


def arch_32_comparing_cells_in_series_vs_cells_in_parallel(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3])
    v_series = round(n_cells * 1.5, 1)
    prompt = (
        f"Compare **{n_cells} identical 1,5 V cells connected in series** versus **{n_cells} identical 1,5 V cells connected in parallel** when driving the same torch bulb.\n\n"
        "Which comparison is scientifically accurate?"
    )
    correct = f"Series cells deliver {_fmt(v_series, 1)} V and higher current (brighter bulb); parallel cells remain at 1,5 V with unchanged brightness but last longer."
    options = [
        correct,
        f"Parallel cells deliver {_fmt(v_series, 1)} V and make the bulb {n_cells} times brighter than series cells.",
        "Both configurations deliver exactly 1,5 V and produce identical bulb brightness.",
        "Series cells prevent current from flowing while parallel cells cause an immediate short circuit.",
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Series cells add potential difference ($n \\times 1{{,}}5\\text{{ V}} = {_fmt(v_series, 1)}\\text{{ V}}$), raising current and brightness.\n"
        "Step 2: Parallel cells keep single-cell voltage ($1{{,}}5\\text{{ V}}$) so current/brightness remain unchanged while capacity increases."
    )
    return _q(
        rng, "32", "32_comparing_cells_in_series_vs_cells_in_parallel", prompt, correct, sol, 2, "mcq",
        ["confusing_cells_in_series_vs_parallel_voltage"],
        "Recall which arrangement adds voltages together and which keeps single-cell voltage.",
        "Series cells = higher voltage + brighter; Parallel cells = same voltage + longer life.",
        correct, options=options,
    )


def arch_33_domestic_household_wiring_parallel_advantages(rng: random.Random) -> Dict[str, Any]:
    home_ctx = rng.choice([
        "a townhouse in Polokwane",
        "a family home in Mitchells Plain",
        "a classroom block in Mthatha",
    ])
    prompt = (
        f"All ceiling lights and wall plug sockets in {home_ctx} are connected to the **230 V** mains supply **in parallel** rather than in series.\n\n"
        "Give **two distinct practical reasons** why household circuits must be wired in parallel [2]."
    )
    correct = "Each light/appliance can be switched independently (if one bulb blows, others stay on), and every appliance receives the full 230 V supply voltage."
    sol = (
        "1. **Independent switching & fault isolation:** Switching off or losing one bulb/appliance leaves all other lights and sockets operating normally [1].\n"
        "2. **Full rated voltage:** Every appliance receives the full 230 V mains potential difference needed to operate at normal power/brightness [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Independent switching / other appliances stay on if one fails", "marks": 1, "target_concepts": ["independent", "switch", "others"], "editable": True},
        {"id": "mp_2", "desc": "Every appliance receives full 230 V supply voltage", "marks": 1, "target_concepts": ["230", "voltage", "full"], "editable": True},
    ]
    return _q(
        rng, "33", "33_domestic_household_wiring_parallel_advantages", prompt, correct, sol, 2, "short_answer",
        ["thinking_households_are_wired_in_series"],
        "Think about what would happen in your kitchen and bedroom if all house lights were on a single series loop.",
        "Independent control/fault isolation + full 230 V delivered to every socket.",
        correct, marking_points=mps,
    )


def arch_34_voltmeter_parallel_connection_and_high_resistance(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice(["a 10 Ω resistor", "a torch light bulb", "a 3 V battery"])
    prompt = (
        f"A learner wants to measure the potential difference across **{comp}** using a voltmeter.\n\n"
        "How must the voltmeter be connected, and what internal resistance must it possess?"
    )
    correct = "Connected in parallel across the component, with extremely high internal resistance so negligible current diverts through the meter."
    options = [
        correct,
        "Connected in series with the component, with near-zero internal resistance.",
        "Connected in parallel across the component, with near-zero internal resistance to draw maximum current.",
        "Connected only to the negative terminal, with moderate resistance equal to the bulb.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Potential difference is measured between two points, so a voltmeter connects **in parallel** across the component.\n"
        "Step 2: It has **very high (near-infinite) internal resistance** so it draws virtually zero current away from the circuit."
    )
    return _q(
        rng, "34", "34_voltmeter_parallel_connection_and_high_resistance", prompt, correct, sol, 2, "mcq",
        ["connecting_voltmeter_in_series", "thinking_voltmeter_has_low_resistance"],
        "A voltmeter sits ACROSS a component without stealing current from it.",
        "Parallel connection + very high resistance.",
        correct, options=options,
    )


def arch_35_meter_misconnection_ammeter_parallel_vs_voltmeter_series(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["ammeter_parallel", "voltmeter_series"])
    if case == "ammeter_parallel":
        prompt = (
            "During practical work, a learner accidentally connects a low-resistance **ammeter in parallel** directly across a glowing light bulb.\n\n"
            "What is the immediate electrical consequence?"
        )
        correct = "Current bypasses the bulb through the near-zero resistance ammeter, creating a dangerous short circuit that can blow the meter's fuse or overheat the battery."
        distractors = [
            "The voltmeter stops working while the bulb shines gently at half power.",
            "Current drops completely to zero because the ammeter blocks electron flow.",
            "The ammeter converts into a cell and doubles the battery voltage.",
        ]
    else:
        prompt = (
            "During practical work, a learner accidentally connects a high-resistance **voltmeter in series** on the main wire leading to a light bulb.\n\n"
            "What is the immediate electrical consequence?"
        )
        correct = "The voltmeter's huge internal resistance blocks almost all current in the single loop, so the bulb stays off while the voltmeter reads close to the full battery voltage."
        distractors = [
            "A massive short-circuit current flows through the bulb, melting the glass.",
            "The bulb shines twice as brightly because the voltmeter supplies extra energy.",
            "The voltmeter needle spins backwards and turns the bulb into an LED.",
        ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "Step 1: Ammeters have ~0 Ω resistance (parallel connection = short circuit).\n"
        "Step 2: Voltmeters have near-infinite resistance (series connection = open-circuit block).\n"
        f"Outcome: {correct}"
    )
    return _q(
        rng, "35", "35_meter_misconnection_ammeter_parallel_vs_voltmeter_series", prompt, correct, sol, 2, "mcq",
        ["ignoring_short_circuit_from_parallel_ammeter", "ignoring_open_circuit_from_series_voltmeter"],
        "Check the internal resistance of the misplaced meter: does ~0 Ω short out the branch, or does ~infinite Ω block the loop?",
        correct, correct, options=options,
    )


def arch_36_mixed_series_parallel_circuit_bulb_brightness_ranking(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([6, 9, 12])
    prompt = (
        f"Consider the combination circuit schematic powered by a {v_bat} V cell with three identical bulbs (**A**, **B**, and **C**). "
        "Switch **S** is **closed**.\n\n"
        "Compare the brightness of **Bulb A**, **Bulb B**, and **Bulb C**."
    )
    correct = "Bulb A is brightest because it carries the full main current; Bulbs B and C glow dimmer with equal brightness because the current splits equally between them."
    options = [
        correct,
        "Bulbs B and C are brighter than Bulb A because parallel bulbs always receive more current than series bulbs.",
        "All three bulbs A, B, and C glow with identical brightness.",
        "Bulb C glows brightest, followed by Bulb B, while Bulb A stays completely dark.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: All current leaving the battery passes through Bulb A ($I_A = I_{\\text{total}}$).\n"
        "Step 2: At the parallel junction, current splits evenly between identical Bulbs B and C ($I_B = I_C = \\frac{1}{2} I_A$).\n"
        "Step 3: Therefore Bulb A is brightest, and Bulbs B and C share equal dimmer brightness."
    )
    return _q(
        rng, "36", "36_mixed_series_parallel_circuit_bulb_brightness_ranking", prompt, correct, sol, 2, "mcq",
        ["thinking_parallel_branches_get_full_main_current_in_mixed_circuit"],
        "Trace how the total current through Bulb A divides when it reaches the parallel junction for B and C.",
        "IA = IB + IC, and IB = IC for identical bulbs; therefore A > B = C.",
        correct, options=options, diagram_spec=_svg_mixed_abc(rng, v_bat, switch_open=False),
    )


def arch_37_mixed_circuit_switch_opened_brightness_reanalysis(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([6, 9, 12])
    prompt = (
        f"In the combination circuit schematic ({v_bat} V cell, identical bulbs A, B, C), switch **S** in branch C is now **opened**.\n\n"
        "What happens to **Bulb C**, **Bulbs A and B**, and the **total current** compared to when switch S was closed?"
    )
    correct = "Bulb C goes off; Bulbs A and B are now in series with equal brightness to each other, while total circuit current decreases because overall resistance increased."
    options = [
        correct,
        "All three bulbs A, B, and C go out immediately because opening S breaks the main series wire.",
        "Bulb A becomes much brighter because the total current increases when branch C opens.",
        "Bulb C stays lit at half brightness while Bulb B goes off.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Opening switch S disconnects Bulb C, so Bulb C goes out.\n"
        "Step 2: Removing the parallel pathway leaves only Bulb A and Bulb B in **series**, increasing total circuit resistance.\n"
        "Step 3: Higher total resistance lowers total main current (so A dims slightly), and A and B now carry the exact same current with equal brightness."
    )
    return _q(
        rng, "37", "37_mixed_circuit_switch_opened_brightness_reanalysis", prompt, correct, sol, 3, "mcq",
        ["thinking_opening_parallel_branch_decreases_resistance"],
        "When branch C opens, does removing a parallel path make total resistance larger or smaller?",
        "Removing a parallel branch increases total resistance, reducing total current; A and B become a pure series pair.",
        correct, options=options, diagram_spec=_svg_mixed_abc(rng, v_bat, switch_open=True),
    )


def arch_38_mixed_circuit_combined_resistance_and_current_calc(rng: random.Random) -> Dict[str, Any]:
    cfg = rng.choice([
        (12, 3, 6, 6),    # Rp=3, Rtot=6, I=2.0
        (18, 5, 8, 8),    # Rp=4, Rtot=9, I=2.0
        (24, 4, 12, 24),  # Rp=8, Rtot=12, I=2.0
        (15, 2, 6, 6),    # Rp=3, Rtot=5, I=3.0
        (20, 6, 8, 8),    # Rp=4, Rtot=10, I=2.0
    ])
    v_bat, r_s, r_p1, r_p2 = cfg
    r_p = round((r_p1 * r_p2) / float(r_p1 + r_p2), 1)
    r_tot = round(r_s + r_p, 1)
    i_tot = round(v_bat / float(r_tot), 1)
    prompt = (
        f"Analyse the combination resistor network shown: a series resistor **$R_s = {r_s}\\ \\Omega$** wired in series with "
        f"parallel resistors **$R_{{p1}} = {r_p1}\\ \\Omega$** and **$R_{{p2}} = {r_p2}\\ \\Omega$** across a **{v_bat} V** source.\n\n"
        "Calculate:\n"
        "1. Equivalent parallel resistance ($R_p$) [2].\n"
        "2. Total circuit resistance ($R_{\\text{total}}$) [1].\n"
        "3. Total main current ($I_{\\text{total}}$) [1]."
    )
    correct = f"Rp = {_fmt(r_p, 1)} Ω; R_total = {_fmt(r_tot, 1)} Ω; I_total = {_fmt(i_tot, 1)} A"
    sol = (
        f"1. **Parallel Equivalent:** $\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r_p1}}} + \\frac{{1}}{{{r_p2}}} \\Rightarrow R_p = {_fmt(r_p, 1)}\\ \\Omega$ [2].\n"
        f"2. **Total Resistance:** $R_{{\\text{{total}}}} = R_s + R_p = {r_s} + {_fmt(r_p, 1)} = {_fmt(r_tot, 1)}\\ \\Omega$ [1].\n"
        f"3. **Total Current:** $I_{{\\text{{total}}}} = \\frac{{{v_bat}}}{{{_fmt(r_tot, 1)}}} = {_fmt(i_tot, 1)}\\text{{ A}}$ [1]."
    )
    return _q(
        rng, "38", "38_mixed_circuit_combined_resistance_and_current_calc", prompt, correct, sol, 4, "math_short",
        ["adding_series_and_parallel_resistors_before_reducing_parallel_block"],
        "Always simplify the parallel pair Rp first, then add Rs in series, then apply I = V / R_total.",
        f"Rp = {_fmt(r_p, 1)} Ω -> R_total = {_fmt(r_tot, 1)} Ω -> I = {_fmt(i_tot, 1)} A.",
        correct, diagram_spec=_svg_mixed_resistors(rng, v_bat, r_s, r_p1, r_p2),
    )


def arch_39_series_vs_parallel_comprehensive_comparison(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice([
        ("current behaviour", "Current is the same everywhere in series, whereas total current splits across branches in parallel."),
        ("adding more identical resistors", "Adding resistors increases total resistance (lower current) in series, whereas it decreases total resistance (higher total current) in parallel."),
        ("number of pathways", "A series circuit has only one continuous pathway, whereas a parallel circuit has two or more branches."),
    ])
    topic_focus, correct = aspect
    options = [
        correct,
        "Current is divided evenly in series, whereas current stays identical in every resistor of an unequal parallel circuit.",
        "Adding resistors in series lowers total resistance while adding resistors in parallel raises total resistance.",
        "Series circuits have three independent loops while parallel circuits always form one closed loop.",
    ]
    rng.shuffle(options)
    prompt = (
        f"Compare **series circuits** and **parallel circuits** specifically regarding **{topic_focus}**.\n\n"
        "Which summary statement is completely accurate?"
    )
    sol = f"Comparison for {topic_focus}: {correct}"
    return _q(
        rng, "39", "39_series_vs_parallel_comprehensive_comparison", prompt, correct, sol, 2, "mcq",
        ["reversing_series_and_parallel_comparison_rules"],
        "Check each claim against the single-loop vs multi-branch definitions.",
        correct, correct, options=options,
    )


def arch_40_metal_wire_conductivity_ranking_copper_to_nichrome(rng: random.Random) -> Dict[str, Any]:
    direction = rng.choice(["lowest to highest resistance", "highest to lowest resistance"])
    if direction == "lowest to highest resistance":
        correct = "Copper (lowest resistance) < Aluminium < Zinc < Nichrome (highest resistance)"
        wrong1 = "Nichrome (lowest resistance) < Zinc < Aluminium < Copper (highest resistance)"
    else:
        correct = "Nichrome (highest resistance) > Zinc > Aluminium > Copper (lowest resistance)"
        wrong1 = "Copper (highest resistance) > Aluminium > Zinc > Nichrome (lowest resistance)"
    options = [
        correct,
        wrong1,
        "Zinc < Copper < Nichrome < Aluminium",
        "All four metals have identical electrical resistance when made into wires.",
    ]
    rng.shuffle(options)
    prompt = (
        "In a conductivity investigation using equal lengths and thicknesses of **copper, aluminium, zinc, and nichrome** wires "
        "tested individually in a circuit with a torch bulb, which order correctly ranks the metals from **" + direction + "**?"
    )
    sol = (
        "Step 1: Copper allows the brightest bulb (lowest resistance), followed by aluminium, zinc, and finally nichrome (dimmest bulb, highest resistance).\n"
        f"Step 2: Ranking ({direction}): {correct}."
    )
    return _q(
        rng, "40", "40_metal_wire_conductivity_ranking_copper_to_nichrome", prompt, correct, sol, 2, "mcq",
        ["thinking_nichrome_has_lower_resistance_than_copper"],
        "Copper is used in household wiring for low resistance, whereas nichrome is used in stove/kettle heating coils.",
        "From best conductor to strongest resistor: Copper -> Aluminium -> Zinc -> Nichrome.",
        correct, options=options,
    )


def arch_41_fair_test_control_variables_metal_resistance_lab(rng: random.Random) -> Dict[str, Any]:
    metals = rng.choice(["copper and nichrome", "aluminium and zinc", "copper, zinc, and nichrome"])
    prompt = (
        f"Learners test wires of **{metals}** using crocodile clips in a circuit to compare which metal offers the highest resistance.\n\n"
        "1. State **two wire dimensions** that must be kept identical as control variables for a fair test [2].\n"
        "2. State one important **safety check** when testing thin aluminium wire across a cell [1]."
    )
    correct = "Same wire length and same wire thickness (diameter); test aluminium beforehand to ensure it does not overheat or ignite."
    sol = (
        "1. **Control variables:** Every wire sample must have the **exact same length** [1] and the **exact same thickness (cross-sectional diameter)** [1].\n"
        "2. **Safety check:** Test aluminium wire beforehand so excessive current does not make it **overheat dangerously or ignite** [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Same wire length", "marks": 1, "target_concepts": ["length"], "editable": True},
        {"id": "mp_2", "desc": "Same wire thickness / diameter", "marks": 1, "target_concepts": ["thickness", "diameter"], "editable": True},
        {"id": "mp_3", "desc": "Test aluminium so it does not overheat / ignite", "marks": 1, "target_concepts": ["overheat", "ignite", "heat"], "editable": True},
    ]
    return _q(
        rng, "41", "41_fair_test_control_variables_metal_resistance_lab", prompt, correct, sol, 3, "short_answer",
        ["comparing_wires_of_different_lengths_or_thicknesses"],
        "Besides material type, what two geometric properties of a wire affect resistance?",
        "Keep length and thickness identical; check aluminium for overheating.",
        correct, marking_points=mps,
    )


def arch_42_copper_conducting_wires_vs_nichrome_elements_application(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["insulated household extension cords", "classroom circuit jumper leads", "electric kettle heating coils"])
    is_copper = "extension" in app or "jumper" in app
    if is_copper:
        correct = "Copper — because it has very low resistance, allowing current to flow with minimal wasted heat energy."
        wrong = "Nichrome — because its high resistance melts the plastic insulation to keep wires warm."
    else:
        correct = "Nichrome — because its high resistance converts electrical energy effectively into thermal (heat) energy without oxidising easily."
        wrong = "Copper — because its near-zero resistance boils water faster without heating up."
    options = [
        correct,
        wrong,
        "Glass — because it is a transparent metal with zero electrical resistance.",
        "Rubber — because free electrons travel faster through rubber insulators.",
    ]
    rng.shuffle(options)
    prompt = (
        f"An electrical manufacturer is choosing wire material for **{app}**.\n\n"
        "Which metal should be selected and what physical property justifies this choice?"
    )
    sol = f"Material selection for {app}: {correct}"
    return _q(
        rng, "42", "42_copper_conducting_wires_vs_nichrome_elements_application", prompt, correct, sol, 2, "mcq",
        ["confusing_conductor_vs_heating_element_material"],
        "Should this application transfer current with minimal heat loss, or intentionally generate heat?",
        correct, correct, options=options,
    )


def arch_43_output_devices_classification_and_energy_conversions(rng: random.Random) -> Dict[str, Any]:
    dev = rng.choice([
        ("electric motor in a ceiling fan", "Electrical energy → kinetic (mechanical) energy"),
        ("school bell buzzer / beeper", "Electrical energy → sound energy"),
        ("LED indicator lamp", "Electrical energy → light energy (with minimal wasted heat)"),
        ("electric geyser heating element", "Electrical energy → thermal (heat) energy"),
    ])
    device_name, correct = dev
    all_conv = [
        "Electrical energy → kinetic (mechanical) energy",
        "Electrical energy → sound energy",
        "Electrical energy → light energy (with minimal wasted heat)",
        "Electrical energy → thermal (heat) energy",
    ]
    options = [correct] + [c for c in all_conv if c != correct]
    rng.shuffle(options)
    prompt = (
        f"Electrical circuits power a variety of **output devices** beyond simple filament bulbs.\n\n"
        f"What is the **primary useful energy conversion** performed by an **{device_name}**?"
    )
    sol = f"Energy transformation in {device_name}: {correct}."
    return _q(
        rng, "43", "43_output_devices_classification_and_energy_conversions", prompt, correct, sol, 2, "mcq",
        ["misidentifying_output_device_useful_energy"],
        "Ask what useful job the output device is designed to perform.",
        correct, correct, options=options,
    )


def arch_44_led_advantages_over_incandescent_filament_bulbs(rng: random.Random) -> Dict[str, Any]:
    building = rng.choice(["a rural clinic in Limpopo", "a school hostel in KwaZulu-Natal", "a municipal office in Bloemfontein"])
    prompt = (
        f"To reduce Eskom electricity usage, {building} replaces old incandescent filament light bulbs with modern **LEDs (Light-Emitting Diodes)**.\n\n"
        "Which combination accurately states why LEDs outperform traditional filament bulbs?"
    )
    correct = "LEDs have no fragile filament to burn out (longer lifespan), waste far less energy as heat, and consume much less electricity for the same brightness."
    options = [
        correct,
        "LEDs contain thicker tungsten filaments that burn hotter and draw 5 times more current.",
        "LEDs only work when connected in series with at least ten 1,5 V cells.",
        "LEDs convert 95% of electrical energy into wasted heat and 5% into light.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: LEDs lack a glowing filament, so they do not burn out rapidly and enjoy a far longer lifespan.\n"
        "Step 2: They convert a much greater fraction of input electricity into light instead of wasted heat, lowering power bills."
    )
    return _q(
        rng, "44", "44_led_advantages_over_incandescent_filament_bulbs", prompt, correct, sol, 2, "mcq",
        ["thinking_leds_use_filaments_and_waste_more_heat"],
        "Does an LED rely on heating a metal filament white-hot like an incandescent bulb?",
        "No filament -> longer lifespan, much less wasted heat, higher efficiency.",
        correct, options=options,
    )


def arch_45_sankey_diagram_energy_conservation_missing_value(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("Electric Kettle", 2000, 1400, "Heat (useful)", "Sound (wasted)"),
        ("LED Torch", 100, 75, "Light (useful)", "Heat (wasted)"),
        ("Electric Motor", 500, 380, "Kinetic (useful)", "Heat & Sound"),
        ("Incandescent Bulb", 200, 40, "Light (useful)", "Heat (wasted)"),
    ])
    dev_name, e_in, e_useful, u_lbl, w_lbl = scenario
    scale = rng.choice([1, 2])
    e_in *= scale
    e_useful *= scale
    e_wasted = e_in - e_useful
    prompt = (
        f"Examine the Sankey energy flow diagram for a **{dev_name}** receiving **{e_in} J** of electrical input energy, "
        f"with **{e_useful} J** transferred as {u_lbl}.\n\n"
        f"Apply the law of conservation of energy to calculate the **wasted energy output ({w_lbl})** in joules [2]."
    )
    correct = f"{e_wasted} J"
    sol = (
        "Step 1: $\\text{Input Energy} = \\text{Useful Output} + \\text{Wasted Output}$ [1].\n"
        f"Step 2: $\\text{{Wasted Output}} = {e_in}\\text{{ J}} - {e_useful}\\text{{ J}} = {e_wasted}\\text{{ J}}$ [1]."
    )
    return _q(
        rng, "45", "45_sankey_diagram_energy_conservation_missing_value", prompt, correct, sol, 2, "math_short",
        ["forgetting_energy_conservation_in_sankey_diagram"],
        "Total input energy must equal the sum of useful and wasted output energies.",
        f"{e_in} J - {e_useful} J = {e_wasted} J.",
        correct, diagram_spec=_svg_sankey_single(rng, dev_name, e_in, e_useful, u_lbl, w_lbl),
    )


def arch_46_sankey_diagram_proportional_arrow_width_interpretation(rng: random.Random) -> Dict[str, Any]:
    e_in = rng.choice([100, 200])
    led_u = int(0.75 * e_in)
    fil_u = int(0.20 * e_in)
    prompt = (
        "Compare the two Sankey energy diagrams for **Device A (LED Lamp)** and **Device B (Filament Bulb)**.\n\n"
        "What does the **relative vertical thickness (width)** of each output band represent, and which device wastes a greater proportion of energy?"
    )
    correct = "Band width is directly proportional to energy quantity (J); Device B (filament bulb) wastes a much larger proportion of input energy as heat."
    options = [
        correct,
        "Band width shows wire length in centimetres; Device A wastes more energy as heat.",
        "Band width represents battery voltage in volts; both devices waste identical amounts of energy.",
        "Band width is purely decorative and carries no quantitative meaning.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: In any Sankey diagram, arrow/band thickness is drawn **proportional to the amount of energy** in joules.\n"
        f"Step 2: Device B shows a very wide wasted heat band ({e_in - fil_u} J of {e_in} J) compared to Device A ({e_in - led_u} J wasted)."
    )
    return _q(
        rng, "46", "46_sankey_diagram_proportional_arrow_width_interpretation", prompt, correct, sol, 2, "mcq",
        ["ignoring_arrow_width_proportionality_in_sankey"],
        "Compare the width of the Light and Heat bands against the Input band.",
        "Width is proportional to joules of energy; the filament bulb's Heat band is far thicker.",
        correct, options=options, diagram_spec=_svg_sankey_compare(rng, e_in, led_u, fil_u),
    )


def arch_47_calculating_energy_efficiency_percentage_led_vs_filament(rng: random.Random) -> Dict[str, Any]:
    e_in = rng.choice([100, 200, 400])
    target_led = rng.choice([True, False])
    if target_led:
        e_u = int(0.75 * e_in)
        dev = "LED Lamp"
        eff = 75
    else:
        e_u = int(0.20 * e_in)
        dev = "Filament Bulb"
        eff = 20
    prompt = (
        f"Use the Sankey diagram values for the **{dev}** (total input = **{e_in} J**, useful light output = **{e_u} J**).\n\n"
        "Calculate the **percentage energy efficiency** of this lamp [3]."
    )
    correct = f"{eff}%"
    sol = (
        "Step 1: Formula: $\\text{Efficiency} = \\left(\\frac{\\text{Useful Energy Output}}{\\text{Total Energy Input}}\\right) \\times 100\\%$ [1].\n"
        f"Step 2: $\\text{{Efficiency}} = \\left(\\frac{{{e_u}}}{{{e_in}}}\\right) \\times 100\\% = {eff}\\%$ [2]."
    )
    return _q(
        rng, "47", "47_calculating_energy_efficiency_percentage_led_vs_filament", prompt, correct, sol, 3, "math_short",
        ["dividing_wasted_energy_instead_of_useful_energy_for_efficiency"],
        "Divide USEFUL output energy (light) by total input energy, then multiply by 100%.",
        f"({e_u} / {e_in}) × 100% = {eff}%.",
        correct, diagram_spec=_svg_sankey_compare(rng, e_in, int(0.75 * e_in), int(0.20 * e_in)),
    )


def arch_48_series_parallel_troubleshooting_christmas_lights_vs_house(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([20, 40, 50])
    prompt = (
        f"A string of older festive fairy lights has **{n_bulbs} miniature bulbs** wired in **series**, whereas a dining room chandelier has 5 bulbs wired in **parallel**.\n\n"
        "Explain why a single burnt-out bulb makes troubleshooting the fairy lights difficult, while replacing a blown bulb in the chandelier is straightforward [2]."
    )
    correct = "In the series fairy lights, one broken filament opens the entire loop so all bulbs go out and every bulb must be tested to find the fault; in the parallel chandelier, only the faulty bulb turns off while the others remain lit."
    sol = (
        f"1. **Series fairy lights:** Because all {n_bulbs} bulbs share one continuous loop, one blown filament shuts off every bulb at once, hiding which specific bulb failed [1].\n"
        "2. **Parallel chandelier:** Each bulb sits on an independent branch, so only the faulty bulb stays dark while the remaining 4 stay lit, immediately pinpointing the broken bulb [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Series: all bulbs go out together, hiding the faulty bulb", "marks": 1, "target_concepts": ["all", "out", "loop"], "editable": True},
        {"id": "mp_2", "desc": "Parallel: only faulty bulb turns off while others remain lit", "marks": 1, "target_concepts": ["only", "lit", "branch"], "editable": True},
    ]
    return _q(
        rng, "48", "48_series_parallel_troubleshooting_christmas_lights_vs_house", prompt, correct, sol, 2, "short_answer",
        ["forgetting_single_loop_fault_hides_broken_bulb"],
        "Compare how many bulbs extinguish when one filament breaks in series vs parallel.",
        "Series -> all go out (hard to locate); Parallel -> only the blown bulb goes out.",
        correct, marking_points=mps,
    )


def arch_49_history_of_electricity_ampere_ohm_faraday_tesla(rng: random.Random) -> Dict[str, Any]:
    fact = rng.choice([
        ("André-Marie Ampère (1825)", "Published foundational theories on electricity and magnetism; the SI unit of current (ampere, A) is named after him."),
        ("Georg Simon Ohm (1827)", "Published quantitative laws linking voltage, current, and resistance; the SI unit of resistance (ohm, Ω) is named after him."),
        ("Michael Faraday (1831)", "Demonstrated electromagnetic induction, forming the operating principle behind power station generators."),
        ("Alessandro Volta (1800)", "Invented the first simple electrochemical cell (voltaic pile) producing steady electric current."),
        ("Nikola Tesla (1880s)", "Developed alternating current (AC) generators and transmission systems used in national electricity grids."),
    ])
    scientist, correct = fact
    all_desc = [
        "Published foundational theories on electricity and magnetism; the SI unit of current (ampere, A) is named after him.",
        "Published quantitative laws linking voltage, current, and resistance; the SI unit of resistance (ohm, Ω) is named after him.",
        "Demonstrated electromagnetic induction, forming the operating principle behind power station generators.",
        "Invented the first simple electrochemical cell (voltaic pile) producing steady electric current.",
        "Developed alternating current (AC) generators and transmission systems used in national electricity grids.",
    ]
    distractors = [d for d in all_desc if d != correct]
    rng.shuffle(distractors)
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    prompt = (
        "The study of electricity progressed over centuries through the work of pioneering scientists and engineers.\n\n"
        f"Which achievement is accurately associated with **{scientist}**?"
    )
    sol = f"Historical contribution of {scientist}: {correct}"
    return _q(
        rng, "49", "49_history_of_electricity_ampere_ohm_faraday_tesla", prompt, correct, sol, 2, "mcq",
        ["confusing_electrical_units_and_pioneers"],
        "Check whether the scientist's name matches an electrical unit (A, Ω, V) or a generator/induction breakthrough.",
        correct, correct, options=options,
    )


def arch_50_electricity_sector_careers_and_phet_circuit_modelling(rng: random.Random) -> Dict[str, Any]:
    role = rng.choice([
        "electrical distribution engineer at Eskom",
        "renewable solar microgrid technician in the Northern Cape",
        "qualified industrial electrician",
    ])
    prompt = (
        f"South Africa's electricity sector depends on skilled specialists such as a(n) **{role}**, "
        "and learners often test circuit designs first using virtual PhET circuit simulations.\n\n"
        "1. State **one core responsibility** of an electrical engineer or technician working with series/parallel networks [1].\n"
        "2. Give **one practical advantage** of testing a circuit in a virtual simulation before wiring real mains or high-current components [1]."
    )
    correct = "Designing/maintaining safe parallel distribution networks and testing circuits for faults; simulations prevent short circuits, blown fuses, and equipment damage while allowing safe parameter testing."
    sol = (
        "1. **Career responsibility:** Designing, installing, monitoring, or troubleshooting safe electrical circuits, substations, or power distribution grids [1].\n"
        "2. **Simulation advantage:** Virtual testing catches short circuits or overloaded components safely without risking shock, fire, or blown school apparatus [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Designs, installs, maintains, or troubleshoots electrical circuits/grids", "marks": 1, "target_concepts": ["design", "maintain", "install", "troubleshoot", "grid", "circuit"], "editable": True},
        {"id": "mp_2", "desc": "Simulations avoid shock/fire/short-circuit equipment damage before building", "marks": 1, "target_concepts": ["safe", "damage", "short", "equipment", "risk"], "editable": True},
    ]
    return _q(
        rng, "50", "50_electricity_sector_careers_and_phet_circuit_modelling", prompt, correct, sol, 2, "short_answer",
        ["underestimating_virtual_circuit_safety_testing"],
        "Think about real-world grid/circuit design duties and why testing virtually avoids blowing real bulbs or fuses.",
        "Electrical careers build/maintain safe distribution circuits; simulations verify wiring safely before physical assembly.",
        correct, marking_points=mps,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_interpreting_parallel_results_table_and_line_graph": arch_26_interpreting_parallel_results_table_and_line_graph,
    "27_calculating_equivalent_parallel_resistance_two_resistors": arch_27_calculating_equivalent_parallel_resistance_two_resistors,
    "28_ohms_law_in_parallel_constant_branch_voltage": arch_28_ohms_law_in_parallel_constant_branch_voltage,
    "29_parallel_circuit_fault_isolation_and_switch_control": arch_29_parallel_circuit_fault_isolation_and_switch_control,
    "30_cells_in_parallel_connection_polarity_rule": arch_30_cells_in_parallel_connection_polarity_rule,
    "31_cells_in_parallel_no_increase_in_current_or_voltage": arch_31_cells_in_parallel_no_increase_in_current_or_voltage,
    "32_comparing_cells_in_series_vs_cells_in_parallel": arch_32_comparing_cells_in_series_vs_cells_in_parallel,
    "33_domestic_household_wiring_parallel_advantages": arch_33_domestic_household_wiring_parallel_advantages,
    "34_voltmeter_parallel_connection_and_high_resistance": arch_34_voltmeter_parallel_connection_and_high_resistance,
    "35_meter_misconnection_ammeter_parallel_vs_voltmeter_series": arch_35_meter_misconnection_ammeter_parallel_vs_voltmeter_series,
    "36_mixed_series_parallel_circuit_bulb_brightness_ranking": arch_36_mixed_series_parallel_circuit_bulb_brightness_ranking,
    "37_mixed_circuit_switch_opened_brightness_reanalysis": arch_37_mixed_circuit_switch_opened_brightness_reanalysis,
    "38_mixed_circuit_combined_resistance_and_current_calc": arch_38_mixed_circuit_combined_resistance_and_current_calc,
    "39_series_vs_parallel_comprehensive_comparison": arch_39_series_vs_parallel_comprehensive_comparison,
    "40_metal_wire_conductivity_ranking_copper_to_nichrome": arch_40_metal_wire_conductivity_ranking_copper_to_nichrome,
    "41_fair_test_control_variables_metal_resistance_lab": arch_41_fair_test_control_variables_metal_resistance_lab,
    "42_copper_conducting_wires_vs_nichrome_elements_application": arch_42_copper_conducting_wires_vs_nichrome_elements_application,
    "43_output_devices_classification_and_energy_conversions": arch_43_output_devices_classification_and_energy_conversions,
    "44_led_advantages_over_incandescent_filament_bulbs": arch_44_led_advantages_over_incandescent_filament_bulbs,
    "45_sankey_diagram_energy_conservation_missing_value": arch_45_sankey_diagram_energy_conservation_missing_value,
    "46_sankey_diagram_proportional_arrow_width_interpretation": arch_46_sankey_diagram_proportional_arrow_width_interpretation,
    "47_calculating_energy_efficiency_percentage_led_vs_filament": arch_47_calculating_energy_efficiency_percentage_led_vs_filament,
    "48_series_parallel_troubleshooting_christmas_lights_vs_house": arch_48_series_parallel_troubleshooting_christmas_lights_vs_house,
    "49_history_of_electricity_ampere_ohm_faraday_tesla": arch_49_history_of_electricity_ampere_ohm_faraday_tesla,
    "50_electricity_sector_careers_and_phet_circuit_modelling": arch_50_electricity_sector_careers_and_phet_circuit_modelling,
}
