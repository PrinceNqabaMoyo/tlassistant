"""Grade 9 Natural Sciences - Series and Parallel Circuits: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional


def _fmt(val: float, decimals: int = 2) -> str:
    """Format decimal values using South African comma notation, stripping redundant trailing zeros if integer-like."""
    s = f"{val:.{decimals}f}"
    if decimals > 0 and "." in s:
        s = s.rstrip("0").rstrip(".") if decimals > 1 and s.endswith("00") else s
    return s.replace(".", ",")


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
    marking_points: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Build a standard 6-pillar compliant question dictionary."""
    guide = f"Marking Guide ({marks} marks): Award marks for each verified scientific step and unit shown."
    if marking_points:
        schema: Any = {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        }
    else:
        schema = guide

    item: Dict[str, Any] = {
        "id": f"ns9_spc_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": qtype,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct,
        "expected_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": marks,
        "marking_schema": schema,
        "marking_guide": guide,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": tags,
    }
    if options is not None:
        item["options"] = options
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    if marking_points is not None:
        item["marking_points"] = marking_points
    return item


def _svg_symbol_card(rng: random.Random, symbol_kind: str, tag: str) -> Dict[str, Any]:
    """Draw a clean IEC circuit symbol diagram parameterized by label tag."""
    shift = rng.randint(-4, 4)
    cx = 210 + shift
    cy = 88
    body = ""
    if symbol_kind == "ammeter":
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 22}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="22" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>'
            f'<text x="{cx}" y="{cy + 6}" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>'
            f'<line x1="{cx + 22}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
        )
    elif symbol_kind == "voltmeter":
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 22}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="22" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>'
            f'<text x="{cx}" y="{cy + 6}" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">V</text>'
            f'<line x1="{cx + 22}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
        )
    elif symbol_kind == "bulb":
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 22}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="22" fill="#fef9c3" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="{cx - 15}" y1="{cy - 15}" x2="{cx + 15}" y2="{cy + 15}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="{cx - 15}" y1="{cy + 15}" x2="{cx + 15}" y2="{cy - 15}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="{cx + 22}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
        )
    elif symbol_kind == "cell":
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 10}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="{cx - 10}" y1="{cy - 24}" x2="{cx - 10}" y2="{cy + 24}" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{cx + 10}" y1="{cy - 12}" x2="{cx + 10}" y2="{cy + 12}" stroke="#0f172a" stroke-width="4.5"/>'
            f'<line x1="{cx + 10}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<text x="{cx - 22}" y="{cy - 16}" font-size="13" font-weight="bold" fill="#dc2626">+</text>'
            f'<text x="{cx + 18}" y="{cy - 14}" font-size="14" font-weight="bold" fill="#2563eb">-</text>'
        )
    elif symbol_kind == "open_switch":
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 28}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<circle cx="{cx - 28}" cy="{cy}" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{cx - 28}" y1="{cy}" x2="{cx + 22}" y2="{cy - 24}" stroke="#dc2626" stroke-width="2.5"/>'
            f'<circle cx="{cx + 28}" cy="{cy}" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{cx + 28}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
        )
    else:  # resistor
        body = (
            f'<line x1="80" y1="{cy}" x2="{cx - 42}" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<rect x="{cx - 42}" y="{cy - 14}" width="84" height="28" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="{cx + 42}" y1="{cy}" x2="340" y2="{cy}" stroke="#0f172a" stroke-width="2.5"/>'
        )

    svg = (
        f'<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="170" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<text x="210" y="25" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">Circuit Component Symbol ({tag})</text>'
        f'{body}'
        f'<text x="210" y="148" font-size="11" fill="#475569" text-anchor="middle">Identify symbol {tag}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_ammeter_dial(rng: random.Random, reading_a: float, max_scale: float) -> Dict[str, Any]:
    """Draw a clean analogue ammeter scale reading between 0 and max_scale."""
    import math
    frac = max(0.05, min(0.95, reading_a / max_scale))
    angle_deg = 150.0 - frac * 120.0
    rad = math.radians(angle_deg)
    cx, cy = 210, 145
    nx = cx + int(78 * math.cos(rad))
    ny = cy - int(78 * math.sin(rad))
    ticks = []
    steps = 5
    for i in range(steps + 1):
        t_val = (max_scale / steps) * i
        t_ang = math.radians(150.0 - (i / steps) * 120.0)
        x1 = cx + int(82 * math.cos(t_ang))
        y1 = cy - int(82 * math.sin(t_ang))
        x2 = cx + int(94 * math.cos(t_ang))
        y2 = cy - int(94 * math.sin(t_ang))
        tx = cx + int(110 * math.cos(t_ang))
        ty = cy - int(110 * math.sin(t_ang)) + 4
        ticks.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="2"/>'
            f'<text x="{tx}" y="{ty}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{_fmt(t_val, 1)}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="190" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<rect x="75" y="18" width="270" height="154" rx="10" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 128 98 A 95 95 0 0 1 292 98" fill="none" stroke="#94a3b8" stroke-width="2"/>'
        f'{"".join(ticks)}'
        f'<line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="#dc2626" stroke-width="3"/>'
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="#0f172a"/>'
        f'<text x="{cx}" y="112" font-size="16" font-weight="bold" fill="#1e293b" text-anchor="middle">A</text>'
        f'<text x="{cx}" y="164" font-size="11" fill="#475569" text-anchor="middle">Ammeter Scale (0 to {_fmt(max_scale, 1)} A)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_series_three_ammeters(rng: random.Random, v_bat: int, a1_val: float, label_r1: int, label_r2: int) -> Dict[str, Any]:
    """Draw a single-loop series circuit with ammeters A1, A2, and A3 and two resistors."""
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="220" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<rect x="65" y="50" width="310" height="130" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        # Top battery (gap at x=205..235)
        f'<rect x="195" y="32" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="210" y1="32" x2="210" y2="68" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="40" x2="226" y2="60" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="24" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Battery</text>'
        # Left ammeter A1
        f'<circle cx="65" cy="115" r="18" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<text x="65" y="120" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A1</text>'
        f'<text x="36" y="119" font-size="10.5" font-weight="bold" fill="#1d4ed8" text-anchor="end">{_fmt(a1_val, 2)} A</text>'
        # Bottom resistors + middle ammeter A2
        f'<rect x="108" y="168" width="56" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="136" y="184" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">R1={label_r1} Ω</text>'
        f'<circle cx="220" cy="180" r="18" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<text x="220" y="185" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A2</text>'
        f'<rect x="276" y="168" width="56" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="304" y="184" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">R2={label_r2} Ω</text>'
        # Right ammeter A3
        f'<circle cx="375" cy="115" r="18" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.5"/>'
        f'<text x="375" y="120" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A3</text>'
        f'<text x="405" y="119" font-size="10.5" fill="#475569" text-anchor="start">?</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_series_resistors(rng: random.Random, v_bat: int, resistances: List[int]) -> Dict[str, Any]:
    """Draw a series circuit with 2 or 3 labeled resistors."""
    n = len(resistances)
    xs = [125, 295] if n == 2 else [105, 220, 335]
    res_elems = []
    for idx, (rx, rval) in enumerate(zip(xs, resistances), 1):
        res_elems.append(
            f'<rect x="{rx - 28}" y="158" width="56" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
            f'<text x="{rx}" y="174" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">R{idx}={rval} Ω</text>'
        )
    svg = (
        f'<svg viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="210" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<rect x="60" y="48" width="320" height="122" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="195" y="30" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="210" y1="30" x2="210" y2="66" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="38" x2="226" y2="58" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="22" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Supply (Series)</text>'
        f'{"".join(res_elems)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_compare_series_bulbs(rng: random.Random, v_bat: int) -> Dict[str, Any]:
    """Compare Circuit P (1 bulb), Circuit Q (2 bulbs in series), Circuit R (3 bulbs in series)."""
    labels = [("Circuit P", 1, "#fde047"), ("Circuit Q", 2, "#fef08a"), ("Circuit R", 3, "#fef9c3")]
    panels = []
    for idx, (cname, count, fill) in enumerate(labels):
        ox = 20 + idx * 140
        bulbs = []
        bx_list = [ox + 60] if count == 1 else ([ox + 42, ox + 78] if count == 2 else [ox + 30, ox + 60, ox + 90])
        for bx in bx_list:
            bulbs.append(
                f'<circle cx="{bx}" cy="145" r="11" fill="{fill}" stroke="#0f172a" stroke-width="2"/>'
                f'<line x1="{bx - 7}" y1="138" x2="{bx + 7}" y2="152" stroke="#0f172a" stroke-width="1.5"/>'
                f'<line x1="{bx - 7}" y1="152" x2="{bx + 7}" y2="138" stroke="#0f172a" stroke-width="1.5"/>'
            )
        panels.append(
            f'<text x="{ox + 60}" y="28" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{cname}</text>'
            f'<rect x="{ox + 15}" y="52" width="90" height="93" fill="none" stroke="#0f172a" stroke-width="2"/>'
            f'<rect x="{ox + 48}" y="40" width="24" height="24" fill="#ffffff"/>'
            f'<line x1="{ox + 55}" y1="40" x2="{ox + 55}" y2="64" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{ox + 65}" y1="45" x2="{ox + 65}" y2="59" stroke="#0f172a" stroke-width="4"/>'
            f'<text x="{ox + 60}" y="38" font-size="9.5" fill="#475569" text-anchor="middle">{v_bat} V</text>'
            f'{"".join(bulbs)}'
        )
    svg = (
        f'<svg viewBox="0 0 440 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="185" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'{"".join(panels)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_cells_series(rng: random.Random, n_cells: int, cell_v: float, reversed_idx: Optional[int] = None) -> Dict[str, Any]:
    """Draw n_cells in series, optionally with one cell reversed in polarity."""
    cell_elems = []
    start_x = 220 - n_cells * 26
    for i in range(n_cells):
        cx = start_x + i * 52
        is_rev = reversed_idx is not None and (i + 1) == reversed_idx
        if not is_rev:
            cell_elems.append(
                f'<line x1="{cx}" y1="42" x2="{cx}" y2="82" stroke="#0f172a" stroke-width="2"/>'
                f'<line x1="{cx + 12}" y1="52" x2="{cx + 12}" y2="72" stroke="#dc2626" stroke-width="4.5"/>'
                f'<text x="{cx - 4}" y="36" font-size="10" fill="#0f172a">+</text>'
            )
        else:
            cell_elems.append(
                f'<line x1="{cx}" y1="52" x2="{cx}" y2="72" stroke="#dc2626" stroke-width="4.5"/>'
                f'<line x1="{cx + 12}" y1="42" x2="{cx + 12}" y2="82" stroke="#0f172a" stroke-width="2"/>'
                f'<text x="{cx + 14}" y="36" font-size="10" fill="#dc2626">+</text>'
            )
        if i < n_cells - 1:
            cell_elems.append(
                f'<line x1="{cx + 12}" y1="62" x2="{cx + 52}" y2="62" stroke="#0f172a" stroke-width="2.5"/>'
            )
    end_x = start_x + (n_cells - 1) * 52 + 12
    svg = (
        f'<svg viewBox="0 0 440 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="190" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<line x1="70" y1="62" x2="{start_x}" y2="62" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="{end_x}" y1="62" x2="370" y2="62" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="70" y1="62" x2="70" y2="145" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="370" y1="62" x2="370" y2="145" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="70" y1="145" x2="370" y2="145" stroke="#0f172a" stroke-width="2.5"/>'
        f'{"".join(cell_elems)}'
        f'<circle cx="220" cy="145" r="16" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="210" y1="135" x2="230" y2="155" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="210" y1="155" x2="230" y2="135" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="220" y="178" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{n_cells} x {_fmt(cell_v, 1)} V Cells in Series</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_series_fault(rng: random.Random, broken_bulb: str, v_bat: int) -> Dict[str, Any]:
    """Draw a series circuit with Bulbs B1, B2, B3 where one filament is broken."""
    bulbs = [("B1", 120), ("B2", 220), ("B3", 320)]
    elems = []
    for name, bx in bulbs:
        is_broken = name == broken_bulb
        fill = "#f1f5f9" if is_broken else "#e2e8f0"
        elems.append(
            f'<circle cx="{bx}" cy="155" r="15" fill="{fill}" stroke="#0f172a" stroke-width="2"/>'
            f'<text x="{bx}" y="185" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>'
        )
        if is_broken:
            elems.append(
                f'<line x1="{bx - 10}" y1="145" x2="{bx - 2}" y2="153" stroke="#dc2626" stroke-width="2"/>'
                f'<line x1="{bx + 2}" y1="157" x2="{bx + 10}" y2="165" stroke="#dc2626" stroke-width="2"/>'
                f'<text x="{bx}" y="132" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Blown</text>'
            )
        else:
            elems.append(
                f'<line x1="{bx - 10}" y1="145" x2="{bx + 10}" y2="165" stroke="#0f172a" stroke-width="1.8"/>'
                f'<line x1="{bx - 10}" y1="165" x2="{bx + 10}" y2="145" stroke="#0f172a" stroke-width="1.8"/>'
            )
    svg = (
        f'<svg viewBox="0 0 440 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="205" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'<rect x="65" y="45" width="310" height="110" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="195" y="28" width="50" height="34" fill="#ffffff"/>'
        f'<line x1="210" y1="28" x2="210" y2="62" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="36" x2="226" y2="54" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="21" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Battery</text>'
        f'{"".join(elems)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_topology_classify(rng: random.Random, is_parallel: bool, n_bulbs: int, v_bat: int) -> Dict[str, Any]:
    """Draw either a series or parallel bulb schematic for topology classification."""
    if not is_parallel:
        xs = [150, 290] if n_bulbs == 2 else [125, 220, 315]
        bulbs = "".join(
            f'<circle cx="{bx}" cy="155" r="14" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{bx - 9}" y1="146" x2="{bx + 9}" y2="164" stroke="#0f172a" stroke-width="1.8"/>'
            f'<line x1="{bx - 9}" y1="164" x2="{bx + 9}" y2="146" stroke="#0f172a" stroke-width="1.8"/>'
            f'<text x="{bx}" y="182" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">L{idx}</text>'
            for idx, bx in enumerate(xs, 1)
        )
        circuit_body = f'<rect x="75" y="48" width="290" height="107" fill="none" stroke="#0f172a" stroke-width="2.5"/>{bulbs}'
    else:
        ys = [110, 165] if n_bulbs == 2 else [95, 138, 181]
        branches = []
        for idx, by in enumerate(ys, 1):
            branches.append(
                f'<line x1="85" y1="{by}" x2="355" y2="{by}" stroke="#0f172a" stroke-width="2.5"/>'
                f'<circle cx="220" cy="{by}" r="13" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>'
                f'<line x1="212" y1="{by - 8}" x2="228" y2="{by + 8}" stroke="#0f172a" stroke-width="1.6"/>'
                f'<line x1="212" y1="{by + 8}" x2="228" y2="{by - 8}" stroke="#0f172a" stroke-width="1.6"/>'
                f'<text x="245" y="{by + 4}" font-size="10.5" font-weight="bold" fill="#0f172a">L{idx}</text>'
            )
        max_y = ys[-1]
        circuit_body = (
            f'<line x1="85" y1="45" x2="355" y2="45" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="85" y1="45" x2="85" y2="{max_y}" stroke="#0f172a" stroke-width="2.5"/>'
            f'<line x1="355" y1="45" x2="355" y2="{max_y}" stroke="#0f172a" stroke-width="2.5"/>'
            f'{"".join(branches)}'
        )
    svg = (
        f'<svg viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="210" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'{circuit_body}'
        f'<rect x="195" y="28" width="50" height="32" fill="#ffffff"/>'
        f'<line x1="210" y1="28" x2="210" y2="60" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="226" y1="36" x2="226" y2="54" stroke="#0f172a" stroke-width="4.5"/>'
        f'<text x="220" y="21" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{v_bat} V Source ({n_bulbs} Bulbs)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_parallel_four_ammeters(
    rng: random.Random, a1: float, a2: float, a3: float, r1_lbl: str, r2_lbl: str, hide_target: str
) -> Dict[str, Any]:
    """Draw parallel circuit with A1 (top main), A2 (branch 1), A3 (branch 2), A4 (bottom/right main)."""
    a1_txt = "?" if hide_target == "A1" else f"{_fmt(a1, 2)} A"
    a2_txt = "?" if hide_target == "A2" else f"{_fmt(a2, 2)} A"
    a3_txt = "?" if hide_target == "A3" else f"{_fmt(a3, 2)} A"
    a4_txt = "?" if hide_target == "A4" else f"{_fmt(a1, 2)} A"
    svg = (
        f'<svg viewBox="0 0 450 235" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="450" height="235" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        # Main frame
        f'<line x1="65" y1="48" x2="385" y2="48" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="65" y1="48" x2="65" y2="190" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="385" y1="48" x2="385" y2="190" stroke="#0f172a" stroke-width="2.5"/>'
        # Branch 1 (y=120) and Branch 2 (y=190)
        f'<line x1="65" y1="120" x2="385" y2="120" stroke="#0f172a" stroke-width="2.5"/>'
        f'<line x1="65" y1="190" x2="385" y2="190" stroke="#0f172a" stroke-width="2.5"/>'
        # Battery at top center
        f'<rect x="200" y="30" width="50" height="36" fill="#ffffff"/>'
        f'<line x1="215" y1="30" x2="215" y2="66" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="231" y1="38" x2="231" y2="58" stroke="#0f172a" stroke-width="4.5"/>'
        # A1 on left vertical main wire
        f'<circle cx="65" cy="84" r="16" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="65" y="88" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A1</text>'
        f'<text x="42" y="88" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="end">{a1_txt}</text>'
        # A4 on right vertical main wire
        f'<circle cx="385" cy="84" r="16" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="385" y="88" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A4</text>'
        f'<text x="406" y="88" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="start">{a4_txt}</text>'
        # Branch 1: A2 + R1
        f'<circle cx="150" cy="120" r="15" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="150" y="124" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A2</text>'
        f'<text x="150" y="99" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{a2_txt}</text>'
        f'<rect x="245" y="108" width="66" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="278" y="124" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">{r1_lbl}</text>'
        # Branch 2: A3 + R2
        f'<circle cx="150" cy="190" r="15" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="150" y="194" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A3</text>'
        f'<text x="150" y="169" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{a3_txt}</text>'
        f'<rect x="245" y="178" width="66" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
        f'<text x="278" y="194" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">{r2_lbl}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_parallel_add_branches(rng: random.Random, v_bat: int) -> Dict[str, Any]:
    """Compare 1, 2, and 3 identical bulbs connected in parallel across the same battery."""
    configs = [("Circuit X", 1, "#fef08a"), ("Circuit Y", 2, "#fde047"), ("Circuit Z", 3, "#facc15")]
    panels = []
    for idx, (cname, n_b, fill) in enumerate(configs):
        ox = 20 + idx * 140
        ys = [125] if n_b == 1 else ([105, 145] if n_b == 2 else [95, 125, 155])
        max_y = ys[-1]
        branches = "".join(
            f'<line x1="{ox + 15}" y1="{y}" x2="{ox + 105}" y2="{y}" stroke="#0f172a" stroke-width="2"/>'
            f'<circle cx="{ox + 60}" cy="{y}" r="10" fill="{fill}" stroke="#0f172a" stroke-width="1.8"/>'
            f'<line x1="{ox + 53}" y1="{y - 7}" x2="{ox + 67}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.4"/>'
            f'<line x1="{ox + 53}" y1="{y + 7}" x2="{ox + 67}" y2="{y - 7}" stroke="#0f172a" stroke-width="1.4"/>'
            for y in ys
        )
        panels.append(
            f'<text x="{ox + 60}" y="25" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{cname}</text>'
            f'<line x1="{ox + 15}" y1="52" x2="{ox + 105}" y2="52" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{ox + 15}" y1="52" x2="{ox + 15}" y2="{max_y}" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{ox + 105}" y1="52" x2="{ox + 105}" y2="{max_y}" stroke="#0f172a" stroke-width="2"/>'
            f'<rect x="{ox + 48}" y="40" width="24" height="24" fill="#ffffff"/>'
            f'<line x1="{ox + 55}" y1="40" x2="{ox + 55}" y2="64" stroke="#0f172a" stroke-width="2"/>'
            f'<line x1="{ox + 65}" y1="45" x2="{ox + 65}" y2="59" stroke="#0f172a" stroke-width="4"/>'
            f'<text x="{ox + 60}" y="38" font-size="9.5" fill="#475569" text-anchor="middle">{v_bat} V</text>'
            f'{branches}'
        )
    svg = (
        f'<svg viewBox="0 0 440 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="190" fill="#ffffff" stroke="#cbd5e1" rx="6"/>'
        f'{"".join(panels)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ---------------------------------------------------------------------------
# Archetypes 01 to 25
# ---------------------------------------------------------------------------

def arch_01_series_circuit_single_pathway_definition(rng: random.Random) -> Dict[str, Any]:
    app = rng.choice(["a torch light bulb and a switch", "two resistors and an ammeter", "a buzzer and two torch cells"])
    prompt = (
        f"A Grade 9 learner builds a closed loop containing {app} wired one after another with no junctions or branches.\n\n"
        "Which statement accurately defines a **series circuit**?"
    )
    correct = "A circuit configuration providing only one continuous pathway for electric current to follow through all components in turn."
    options = [
        correct,
        "A circuit providing two or more independent branches so current divides at a junction.",
        "A circuit where components are disconnected so electrons remain stationary inside the cell.",
        "A circuit connected exclusively to municipal mains sockets using parallel live wires.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall the structural definition of a series circuit:\n"
        "Components are connected end-to-end along a single continuous loop.\n"
        "Step 2: Because there are no junctions, electrons have **only one pathway** through every component.\n"
        f"Answer: {correct}"
    )
    return _q(
        rng, "01", "01_series_circuit_single_pathway_definition", prompt, correct, sol, 2, "mcq",
        ["confusing_series_and_parallel_pathways"],
        "Count how many separate routes electrons can travel from one terminal of the cell to the other.",
        "End-to-end wiring with no branches means there is only one single pathway.",
        correct, options=options,
    )


def arch_02_circuit_diagram_symbol_identification(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice([
        ("ammeter", "Ammeter — measures electric current strength in amperes (A) when placed in series"),
        ("voltmeter", "Voltmeter — measures potential difference in volts (V) when placed in parallel"),
        ("bulb", "Incandescent light bulb — output device converting electrical energy into light and heat"),
        ("cell", "Single electric cell — chemical energy source supplying electrical energy to the circuit"),
        ("open_switch", "Open switch — breaks the conducting path so electric current stops flowing"),
        ("resistor", "Fixed resistor — opposes electric charge flow to control current strength"),
    ])
    sym_kind, correct = choice
    tag = rng.choice(["K", "M", "P", "X"])
    all_defs = [
        "Ammeter — measures electric current strength in amperes (A) when placed in series",
        "Voltmeter — measures potential difference in volts (V) when placed in parallel",
        "Incandescent light bulb — output device converting electrical energy into light and heat",
        "Single electric cell — chemical energy source supplying electrical energy to the circuit",
        "Open switch — breaks the conducting path so electric current stops flowing",
        "Fixed resistor — opposes electric charge flow to control current strength",
    ]
    distractors = [d for d in all_defs if d != correct]
    rng.shuffle(distractors)
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    prompt = (
        f"Examine the standard circuit symbol labelled **{tag}** in the accompanying schematic.\n\n"
        f"Which component and primary function does symbol **{tag}** represent?"
    )
    sol = (
        f"Step 1: Inspect the geometry of schematic symbol {tag}.\n"
        f"Step 2: Match the standard symbol to its component:\n"
        f"{correct}."
    )
    return _q(
        rng, "02", "02_circuit_diagram_symbol_identification", prompt, correct, sol, 2, "mcq",
        ["misidentifying_standard_circuit_symbols"],
        "Look closely at the letters, circle cross, parallel lines, or rectangular box in the symbol.",
        "Circle with A = ammeter; circle with V = voltmeter; circle with X = bulb; long/short lines = cell; rectangle = resistor.",
        correct, options=options, diagram_spec=_svg_symbol_card(rng, sym_kind, tag),
    )


def arch_03_ammeter_series_connection_and_low_resistance(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        "measuring current through a school laboratory torch bulb",
        "recording electric current flowing out of a 3 V battery pack",
        "checking current strength passing through a nichrome wire resistor",
    ])
    prompt = (
        f"A learner is {context} using an ammeter.\n\n"
        "1. State how the ammeter must be connected into the circuit (series or parallel) [1].\n"
        "2. Explain whether an ammeter has a very low or very high internal resistance, and why this property is essential [2]."
    )
    correct = "Connected in series; very low internal resistance so it does not oppose or reduce the current being measured."
    sol = (
        "1. **Connection:** An ammeter must always be connected in **series** so the entire current to be measured passes through it [1].\n"
        "2. **Internal Resistance:** It has an **extremely low resistance** [1] so that inserting it into the loop does not add significant opposition or reduce the true current strength [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Ammeter is connected in series", "marks": 1, "target_concepts": ["series"], "editable": True},
        {"id": "mp_2", "desc": "Ammeter has very low internal resistance", "marks": 1, "target_concepts": ["low", "resistance"], "editable": True},
        {"id": "mp_3", "desc": "Does not alter or reduce the current it measures", "marks": 1, "target_concepts": ["alter", "reduce", "current"], "editable": True},
    ]
    return _q(
        rng, "03", "03_ammeter_series_connection_and_low_resistance", prompt, correct, sol, 3, "short_answer",
        ["thinking_ammeter_needs_high_resistance", "connecting_ammeter_in_parallel"],
        "Current must flow THROUGH an ammeter. Should the meter block that flow or let it pass freely?",
        "Connect in series; resistance must be near zero so it doesn't reduce the circuit's current.",
        correct, marking_points=mps,
    )


def arch_04_ampere_unit_and_ammeter_scale_reading(rng: random.Random) -> Dict[str, Any]:
    max_scale = rng.choice([1.0, 2.0, 5.0])
    step = max_scale / 10.0
    reading = round(rng.choice([2, 3, 4, 6, 7, 8]) * step, 2)
    ma_val = int(round(reading * 1000))
    prompt = (
        f"An ammeter connected in series with a classroom circuit displays the needle position shown on the scale (0 to {_fmt(max_scale, 1)} A).\n\n"
        f"1. State the reading in amperes (A) [1].\n"
        f"2. Convert this current reading into milliamperes (mA) [1]."
    )
    correct = f"{_fmt(reading, 2)} A ({ma_val} mA)"
    sol = (
        f"Step 1: Read the pointer along the 0 to {_fmt(max_scale, 1)} A arc: $I = {_fmt(reading, 2)}\\text{{ A}}$ [1].\n"
        f"Step 2: Convert amperes to milliamperes ($1\\text{{ A}} = 1\\,000\\text{{ mA}}$):\n"
        f"${_fmt(reading, 2)}\\text{{ A}} \\times 1\\,000 = {ma_val}\\text{{ mA}}$ [1]."
    )
    return _q(
        rng, "04", "04_ampere_unit_and_ammeter_scale_reading", prompt, correct, sol, 2, "math_short",
        ["misreading_ammeter_scale_divisions", "wrong_ampere_to_milliampere_factor"],
        "Check the value of each major tick mark between 0 and the maximum scale value.",
        "Multiply amperes by 1 000 to convert to milliamperes (mA).",
        correct, diagram_spec=_svg_ammeter_dial(rng, reading, max_scale),
    )


def arch_05_current_uniformity_everywhere_in_series_loop(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([6, 9, 12])
    r1 = rng.choice([2, 3, 4, 6])
    r2 = rng.choice([4, 6, 8])
    a1_val = round(v_bat / float(r1 + r2), 2)
    prompt = (
        f"Inspect the series circuit schematic containing three ammeters (**A1**, **A2**, and **A3**) and resistors $R_1 = {r1}\\ \\Omega$ and $R_2 = {r2}\\ \\Omega$.\n\n"
        f"If ammeter **A1** reads **${_fmt(a1_val, 2)}\\text{{ A}}$**, what are the readings on **A2** (between the resistors) and **A3** (returning to the battery)? Explain why [3]."
    )
    correct = f"A2 = {_fmt(a1_val, 2)} A and A3 = {_fmt(a1_val, 2)} A"
    sol = (
        "Step 1: Series current conservation principle:\n"
        "In a single-loop series circuit, electric charge has only one pathway and is never used up by resistors ($A_1 = A_2 = A_3$).\n"
        f"Step 2: Therefore **A2 = {_fmt(a1_val, 2)} A** and **A3 = {_fmt(a1_val, 2)} A** [3]."
    )
    return _q(
        rng, "05", "05_current_uniformity_everywhere_in_series_loop", prompt, correct, sol, 3, "math_short",
        ["current_gets_used_up_after_resistor_myth"],
        "Does electric current get 'used up' as it passes through R1, or is the rate of electron flow identical everywhere in a single loop?",
        "In a series circuit, A1 = A2 = A3 everywhere along the loop.",
        correct, diagram_spec=_svg_series_three_ammeters(rng, v_bat, a1_val, r1, r2),
    )


def arch_06_adding_resistors_in_series_total_resistance(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([6, 9, 12, 18])
    n_res = rng.choice([2, 3])
    resistances = [rng.choice([2, 3, 4, 5, 6]) for _ in range(n_res)]
    r_tot = sum(resistances)
    i_cur = round(v_bat / float(r_tot), 2)
    expr = " + ".join(str(r) for r in resistances)
    prompt = (
        f"The series circuit shown connects a **{v_bat} V** battery in one continuous loop with {n_res} resistors "
        f"({', '.join(f'R{i}={r} Ω' for i, r in enumerate(resistances, 1))}).\n\n"
        "Calculate the **total resistance** ($R_{\\text{total}}$) and the resulting **circuit current** ($I$) [3]."
    )
    correct = f"R_total = {r_tot} Ω; I = {_fmt(i_cur, 2)} A"
    sol = (
        f"Step 1: Add series resistances: $R_{{\\text{{total}}}} = {expr} = {r_tot}\\ \\Omega$ [1].\n"
        f"Step 2: Apply $I = \\frac{{V}}{{R_{{\\text{{total}}}}}} = \\frac{{{v_bat}}}{{{r_tot}}} = {_fmt(i_cur, 2)}\\text{{ A}}$ [2]."
    )
    return _q(
        rng, "06", "06_adding_resistors_in_series_total_resistance", prompt, correct, sol, 3, "math_short",
        ["using_reciprocal_formula_for_series_resistors"],
        "In series, electrons must push through every resistor one after another. Do resistances add together or divide?",
        f"R_total = {expr}, then calculate I = V / R_total.",
        correct, diagram_spec=_svg_series_resistors(rng, v_bat, resistances),
    )


def arch_07_adding_bulbs_in_series_effect_on_current_and_brightness(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([3, 4, 6])
    prompt = (
        f"Three circuits (**P**, **Q**, and **R**) each use an identical **{v_bat} V** cell and identical torch bulbs connected in series as illustrated.\n\n"
        "Rank the circuits from **brightest** bulbs to **dimmest** bulbs and explain why."
    )
    correct = "Circuit P (brightest) > Circuit Q (bright) > Circuit R (dimmest); adding bulbs in series increases total resistance and decreases circuit current."
    options = [
        correct,
        "Circuit R (brightest) > Circuit Q (bright) > Circuit P (dimmest); more bulbs generate more current.",
        "All three circuits glow with identical brightness because every circuit uses the same battery.",
        "Circuit Q is brightest while Circuits P and R remain completely dark.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Compare total resistance in each series circuit:\n"
        "Circuit P has 1 bulb (lowest $R_{\\text{total}}$), Circuit Q has 2 bulbs, Circuit R has 3 bulbs (highest $R_{\\text{total}}$).\n"
        "Step 2: By $I = V / R_{\\text{total}}$, increasing series resistance decreases current strength, making bulbs dimmer: P > Q > R."
    )
    return _q(
        rng, "07", "07_adding_bulbs_in_series_effect_on_current_and_brightness", prompt, correct, sol, 3, "mcq",
        ["more_bulbs_in_series_makes_circuit_brighter_myth"],
        "More bulbs connected one after another in a single loop create more opposition to current flow.",
        "Adding series resistors increases total resistance, which lowers current and dims all bulbs.",
        correct, options=options, diagram_spec=_svg_compare_series_bulbs(rng, v_bat),
    )


def arch_08_equal_brightness_of_identical_bulbs_in_series(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([3, 4])
    prompt = (
        f"A learner connects **{n_bulbs} identical torch bulbs** in a single series loop to a 6 V battery. "
        "Before closing the switch, a classmate predicts that the first bulb closest to the positive terminal will shine brightest and each later bulb will grow progressively dimmer.\n\n"
        "What is actually observed, and what scientific reason explains this observation?"
    )
    correct = f"All {n_bulbs} identical bulbs glow with the exact same brightness because the current strength is uniform throughout every point in a series circuit."
    options = [
        correct,
        "The first bulb burns brightest because it absorbs most of the electric current before the others.",
        "The last bulb near the negative terminal glows brightest because electrons accumulate there.",
        "Only the middle bulb lights up while the outer bulbs act as insulators.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: In a series circuit, every electron passes sequentially through all identical filaments.\n"
        f"Step 2: Because current is identical everywhere ($I_1 = I_2 = \\dots$) and all {n_bulbs} bulbs have equal resistance, each bulb transfers energy at the same rate and glows equally brightly."
    )
    return _q(
        rng, "08", "08_equal_brightness_of_identical_bulbs_in_series", prompt, correct, sol, 2, "mcq",
        ["first_bulb_in_series_gets_more_current_myth"],
        "Remember that electric current is NOT consumed along a single wire loop.",
        "Identical current + identical bulb resistance = equal brightness for every bulb in the loop.",
        correct, options=options,
    )


def arch_09_investigation_variables_adding_bulbs_in_series(rng: random.Random) -> Dict[str, Any]:
    cell_v = rng.choice(["1,5 V", "3,0 V", "4,5 V"])
    prompt = (
        f"During a practical class experiment using a **{cell_v}** power source, learners add 1, 2, and then 3 identical bulbs in series while measuring current on an ammeter.\n\n"
        "Identify:\n"
        "1. The **independent variable** [1].\n"
        "2. The **dependent variable** [1].\n"
        "3. **Two controlled (fixed) variables** needed for a fair investigation [2]."
    )
    correct = "Independent: number of bulbs in series; Dependent: current strength (ammeter reading) / brightness; Controls: cell voltage, identical bulb ratings, conducting wires."
    sol = (
        "1. **Independent variable (changed deliberately):** Number of bulbs (resistors) connected in series [1].\n"
        "2. **Dependent variable (measured outcome):** Current strength in amperes (and bulb brightness) [1].\n"
        f"3. **Controlled variables:** Same battery potential difference ({cell_v}), identical torch bulbs with equal resistance, same copper connecting wires [2]."
    )
    mps = [
        {"id": "mp_1", "desc": "Independent variable: number of bulbs/resistors in series", "marks": 1, "target_concepts": ["number", "bulbs", "series"], "editable": True},
        {"id": "mp_2", "desc": "Dependent variable: current strength / ammeter reading", "marks": 1, "target_concepts": ["current", "ammeter"], "editable": True},
        {"id": "mp_3", "desc": "Two fair-test controls (same battery voltage, identical bulbs/wires)", "marks": 2, "target_concepts": ["voltage", "identical", "bulbs"], "editable": True},
    ]
    return _q(
        rng, "09", "09_investigation_variables_adding_bulbs_in_series", prompt, correct, sol, 4, "short_answer",
        ["swapping_independent_and_dependent_variables"],
        "Independent = what the experimenter changes; Dependent = what is measured on the ammeter.",
        "You vary the number of bulbs and measure the resulting current while keeping the cells and bulb type constant.",
        correct, marking_points=mps,
    )


def arch_10_formulating_hypothesis_resistors_in_series(rng: random.Random) -> Dict[str, Any]:
    investigative_q = rng.choice([
        "How does increasing the number of resistors in a series circuit affect the total electric current?",
        "What happens to the ammeter reading when more identical light bulbs are added one after another in series?",
    ])
    prompt = (
        f"Consider the investigative question: *\"{investigative_q}\"*\n\n"
        "Which option represents a **valid, testable scientific hypothesis** for this investigation?"
    )
    correct = "If more resistors are added in series, then the electric current strength will decrease because the total circuit resistance increases."
    options = [
        correct,
        "Resistors are made of carbon or nichrome wire and cost R15 each at an electronics shop.",
        "I wonder whether the ammeter needle will move slightly to the left or stay still.",
        "Connect two cells, copper wires, and an ammeter together in a single closed loop.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: A scientific hypothesis makes a clear, testable prediction linking the independent variable (number of series resistors) and dependent variable (current strength).\n"
        "Step 2: Only the first statement predicts a testable relationship with a scientific reason."
    )
    return _q(
        rng, "10", "10_formulating_hypothesis_resistors_in_series", prompt, correct, sol, 2, "mcq",
        ["confusing_hypothesis_with_procedure_or_question"],
        "A hypothesis must be a clear prediction statement (If ... then ...), not a question or equipment list.",
        "Look for a testable cause-and-effect prediction relating series resistors to current.",
        correct, options=options,
    )


def arch_11_interpreting_series_investigation_results_table(rng: random.Random) -> Dict[str, Any]:
    i1 = rng.choice([0.18, 0.24, 0.30, 0.36])
    i2 = round(i1 / 2.0, 2)
    i3 = round(i1 / 3.0, 2)
    diff = round(i1 - i3, 2)
    prompt = (
        "A learner records the following laboratory measurements while adding identical bulbs in series across a fixed cell:\n\n"
        "| Number of bulbs in series | Bulb brightness | Ammeter reading (A) |\n"
        "| :---: | :---: | :---: |\n"
        f"| 1 | Brightest | {_fmt(i1, 2)} |\n"
        f"| 2 | Bright | {_fmt(i2, 2)} |\n"
        f"| 3 | Dimmest | {_fmt(i3, 2)} |\n\n"
        "Calculate by how much the current decreases from **1 bulb** to **3 bulbs** in series, and state the mathematical pattern [2]."
    )
    correct = f"{_fmt(diff, 2)} A decrease (current drops to one-third)"
    sol = (
        f"Step 1: Subtract the 3-bulb current from the 1-bulb current:\n"
        f"$\\Delta I = {_fmt(i1, 2)}\\text{{ A}} - {_fmt(i3, 2)}\\text{{ A}} = {_fmt(diff, 2)}\\text{{ A}}$ [1].\n"
        f"Step 2: Tripling the series bulbs triples total resistance, reducing current to one-third (${_fmt(i1, 2)} / 3 = {_fmt(i3, 2)}\\text{{ A}}$) [1]."
    )
    return _q(
        rng, "11", "11_interpreting_series_investigation_results_table", prompt, correct, sol, 2, "math_short",
        ["misreading_inverse_proportion_in_series_data"],
        "Subtract the 3-bulb current reading from the 1-bulb current reading.",
        f"{_fmt(i1, 2)} - {_fmt(i3, 2)} = {_fmt(diff, 2)} A; notice the ratio 1 : 1/2 : 1/3.",
        correct,
    )


def arch_12_bulb_heating_experimental_error_in_series_lab(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a series circuit investigation, learners notice two real-world anomalies: when 1 torch bulb glows very brightly for a long time, "
        "its measured current drops slightly below the expected theoretical value; additionally, two school ammeters show slightly different readings on the same loop.\n\n"
        "What pair of practical experimental factors explains these two observations?"
    )
    correct = "A hot tungsten filament has higher electrical resistance than a cooler filament, and school ammeters may be poorly calibrated (zero/scale error)."
    options = [
        correct,
        "Electrons evaporate out of hot glass bulbs into the air, and copper wires turn into magnets.",
        "Cold bulbs have infinite resistance, and ammeters measure battery mass instead of current.",
        "Heating a filament removes all resistance, making the ammeter reading fluctuate randomly.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Thermal effect in metallic filaments: as bulb filaments heat up significantly, lattice vibrations increase and filament resistance rises, reducing current slightly.\n"
        "Step 2: Instrument calibration: uncalibrated or poorly serviced school meters introduce small systematic reading discrepancies."
    )
    return _q(
        rng, "12", "12_bulb_heating_experimental_error_in_series_lab", prompt, correct, sol, 2, "mcq",
        ["assuming_bulb_resistance_never_changes_with_heat"],
        "Think about how rising filament temperature affects atomic collisions and how meter wear affects accuracy.",
        "Higher temperature increases metal filament resistance; worn/uncalibrated meters cause systematic error.",
        correct, options=options,
    )


def arch_13_cells_in_series_increasing_current_and_brightness(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    cell_v = 1.5
    v_tot = round(n_cells * cell_v, 1)
    r_bulb = rng.choice([3, 5, 6, 9])
    i_one = round(cell_v / float(r_bulb), 2)
    i_tot = round(v_tot / float(r_bulb), 2)
    prompt = (
        f"Observe the series circuit schematic with **{n_cells} identical 1,5 V cells** connected in series (positive to negative) "
        f"driving a bulb of resistance **$R = {r_bulb}\\ \\Omega$**.\n\n"
        f"1. Calculate the total potential difference supplied by the {n_cells} cells [1].\n"
        f"2. Calculate the circuit current and explain how bulb brightness compares to using just 1 cell ({_fmt(i_one, 2)} A) [2]."
    )
    correct = f"V_total = {_fmt(v_tot, 1)} V; I = {_fmt(i_tot, 2)} A (brighter)"
    sol = (
        f"Step 1: Cells in series add voltages: $V_{{\\text{{total}}}} = {n_cells} \\times 1{{,}}5\\text{{ V}} = {_fmt(v_tot, 1)}\\text{{ V}}$ [1].\n"
        f"Step 2: Calculate current: $I = \\frac{{V}}{{R}} = \\frac{{{_fmt(v_tot, 1)}}}{{{r_bulb}}} = {_fmt(i_tot, 2)}\\text{{ A}}$ [1].\n"
        f"Step 3: Because current increases {n_cells}-fold compared to 1 cell ({_fmt(i_one, 2)} A), the bulb glows **much brighter** [1]."
    )
    return _q(
        rng, "13", "13_cells_in_series_increasing_current_and_brightness", prompt, correct, sol, 3, "math_short",
        ["thinking_cells_in_series_keep_same_voltage"],
        "When cells are linked positive-to-negative in series, their voltages add up.",
        f"V_total = {n_cells} × 1,5 V = {_fmt(v_tot, 1)} V; then I = V_total / R.",
        correct, diagram_spec=_svg_cells_series(rng, n_cells, cell_v),
    )


def arch_14_cells_in_series_polarity_alignment_and_reversal(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([3, 4])
    cell_v = 1.5
    rev_idx = rng.choice([2, n_cells])
    net_v = round((n_cells - 2) * cell_v, 1)
    prompt = (
        f"A learner connects **{n_cells} identical 1,5 V cells** in series to power a torch bulb, but accidentally inserts **Cell {rev_idx} backwards** as shown.\n\n"
        "Calculate the **net effective battery voltage** available to push current around the circuit [2]."
    )
    correct = f"{_fmt(net_v, 1)} V"
    sol = (
        f"Step 1: {n_cells - 1} cells push forward (${_fmt((n_cells - 1) * cell_v, 1)}\\text{{ V}}$), while 1 reversed cell opposes them ($-1{{,}}5\\text{{ V}}$) [1].\n"
        f"Step 2: $V_{{\\text{{net}}}} = {_fmt((n_cells - 1) * cell_v, 1)}\\text{{ V}} - 1{{,}}5\\text{{ V}} = {_fmt(net_v, 1)}\\text{{ V}}$ [1]."
    )
    return _q(
        rng, "14", "14_cells_in_series_polarity_alignment_and_reversal", prompt, correct, sol, 2, "math_short",
        ["forgetting_reversed_cell_cancels_one_forward_cell"],
        "A reversed cell doesn't just add 0 V — it pushes backwards against one of the correctly aligned cells!",
        f"One reversed cell cancels one forward cell, leaving ({n_cells} - 2) × 1,5 V.",
        correct, diagram_spec=_svg_cells_series(rng, n_cells, cell_v, reversed_idx=rev_idx),
    )


def arch_15_circuit_safety_precaution_preventing_excess_current_in_cells_series(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([3, 4])
    v_tot = round(n_cells * 1.5, 1)
    prompt = (
        f"In a Grade 9 investigation testing **{n_cells} cells in series** (supplying **{_fmt(v_tot, 1)} V** total), "
        "the laboratory manual warns learners **not** to connect only a single low-voltage torch bulb in the loop, recommending at least two bulbs (or one bulb plus a resistor).\n\n"
        "Explain the physical reason for this safety precaution [2]."
    )
    correct = "Connecting only one low-resistance bulb across multiple series cells creates too little total resistance, causing excessive current that overheats and blows (burns out) the bulb filament."
    sol = (
        f"Step 1: {_fmt(v_tot, 1)} V across a single torch bulb produces a very large electric current ($I = V / R$) [1].\n"
        "Step 2: Excess current rapidly overheats and **melts/blows the delicate bulb filament**; adding a second bulb or resistor increases total resistance to keep current at a safe level [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "High voltage across small resistance drives excessive current", "marks": 1, "target_concepts": ["current", "resistance"], "editable": True},
        {"id": "mp_2", "desc": "Prevents overheating or blowing/burning out the bulb filament", "marks": 1, "target_concepts": ["filament", "burn", "blow", "overheat"], "editable": True},
    ]
    return _q(
        rng, "15", "15_circuit_safety_precaution_preventing_excess_current_in_cells_series", prompt, correct, sol, 2, "short_answer",
        ["ignoring_excess_current_filament_burnout"],
        "Think about what happens to current strength when battery voltage triples while resistance stays tiny.",
        "High current can overheat and burn out a single torch bulb filament; extra resistance limits current.",
        correct, marking_points=mps,
    )


def arch_16_delocalised_electron_drift_open_vs_closed_circuit(rng: random.Random) -> Dict[str, Any]:
    room_len = rng.choice(["5 m", "10 m", "15 m"])
    prompt = (
        f"A classroom demonstration uses {room_len} of copper wire between a battery, switch, and ceiling bulb. "
        "The moment the switch is closed, the bulb glows instantaneously.\n\n"
        "Which statement accurately describes **electron movement** inside the copper conductor before and immediately after the switch is closed?"
    )
    correct = "Before closing, delocalised electrons drift randomly in all directions; upon closing, electrons throughout the entire wire loop begin drifting synchronously towards the positive terminal."
    options = [
        correct,
        "Electrons sit completely frozen inside the battery until the switch opens, then sprint down empty wires.",
        "Copper atoms detach from the wire and flow through the bulb filament at the speed of light.",
        "Electrons move directly from the positive terminal to the negative terminal inside the outer copper wire.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Metals contain a sea of free (delocalised) electrons moving in random directions when the circuit is open.\n"
        "Step 2: Closing the switch establishes an electric field throughout the conductor so all electrons in the loop begin moving together towards the positive terminal at once."
    )
    return _q(
        rng, "16", "16_delocalised_electron_drift_open_vs_closed_circuit", prompt, correct, sol, 2, "mcq",
        ["thinking_electrons_start_only_at_battery_when_switched_on"],
        "Are electrons already present inside all parts of the copper wire before the switch closes?",
        "Free electrons already fill the wire; closing the switch synchronizes their drift toward the positive terminal.",
        correct, options=options,
    )


def arch_17_series_circuit_open_switch_or_broken_filament_fault(rng: random.Random) -> Dict[str, Any]:
    broken_bulb = rng.choice(["B1", "B2", "B3"])
    others = " and ".join(b for b in ("B1", "B2", "B3") if b != broken_bulb)
    v_bat = rng.choice([6, 9, 12])
    prompt = (
        f"In the series circuit shown ({v_bat} V battery), the filament inside bulb **{broken_bulb}** suddenly snaps open.\n\n"
        f"What happens to the remaining bulbs **{others}**, and why?"
    )
    correct = f"Both {others} extinguish immediately because the broken filament creates an open circuit, interrupting the single conducting pathway."
    options = [
        correct,
        f"Both {others} glow noticeably brighter because they now share the extra current.",
        f"Only the bulb after {broken_bulb} goes out while the other stays lit.",
        f"Both {others} continue glowing at unchanged brightness until the battery runs flat.",
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: In a series circuit there is only ONE continuous conducting pathway.\n"
        f"Step 2: When {broken_bulb} blows, an air gap (open circuit) forms, halting electron flow everywhere so {others} switch off immediately."
    )
    return _q(
        rng, "17", "17_series_circuit_open_switch_or_broken_filament_fault", prompt, correct, sol, 2, "mcq",
        ["thinking_remaining_series_bulbs_stay_lit_or_brighter"],
        "How many paths does the current have around a series circuit?",
        "Breaking the single pathway creates an open circuit, stopping current everywhere.",
        correct, options=options, diagram_spec=_svg_series_fault(rng, broken_bulb, v_bat),
    )


def arch_18_parallel_circuit_multiple_pathways_definition(rng: random.Random) -> Dict[str, Any]:
    ctx = rng.choice(["two electric fans", "three classroom ceiling lamps", "a heater and a radio"])
    prompt = (
        f"An electrician wires {ctx} so each appliance sits on its own separate branch connected across the same two supply points.\n\n"
        "Which statement correctly defines this **parallel circuit** configuration?"
    )
    correct = "A circuit offering two or more independent conducting pathways (branches) where electric current divides between the branches."
    options = [
        correct,
        "A circuit arranged in a single closed loop with zero junctions between components.",
        "A circuit where current flows only through the first component and skips all others.",
        "A circuit containing only cells connected positive-to-negative without any load.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: A parallel circuit splits into multiple branches between two junction nodes.\n"
        "Step 2: Each branch forms an independent pathway for current flow."
    )
    return _q(
        rng, "18", "18_parallel_circuit_multiple_pathways_definition", prompt, correct, sol, 2, "mcq",
        ["confusing_parallel_branches_with_single_loop"],
        "How many pathways are available for current when components sit on separate branches?",
        "Multiple independent pathways between common nodes define a parallel circuit.",
        correct, options=options,
    )


def arch_19_identifying_series_vs_parallel_circuit_topology(rng: random.Random) -> Dict[str, Any]:
    is_parallel = rng.choice([True, False])
    n_bulbs = rng.choice([2, 3])
    v_bat = rng.choice([3, 6, 9])
    if is_parallel:
        correct = f"Parallel circuit — there are {n_bulbs} separate branches providing multiple pathways for current to divide."
        distractor_wrong = f"Series circuit — all {n_bulbs} bulbs share a single undivided wire pathway."
    else:
        correct = f"Series circuit — all {n_bulbs} bulbs lie one after another on one continuous pathway."
        distractor_wrong = f"Parallel circuit — current splits equally into {n_bulbs} independent branches."
    options = [
        correct,
        distractor_wrong,
        "Open short circuit — no conducting wire connects the bulbs to the supply.",
        "Alternating series-only transformer circuit with zero current flow.",
    ]
    rng.shuffle(options)
    prompt = (
        f"Analyse the schematic circuit containing {n_bulbs} bulbs (**L1** to **L{n_bulbs}**) powered by a {v_bat} V cell.\n\n"
        "Classify the circuit arrangement and justify your classification based on current pathways."
    )
    sol = (
        "Step 1: Trace electron paths from one battery terminal to the other.\n"
        f"Step 2: {correct}"
    )
    return _q(
        rng, "19", "19_identifying_series_vs_parallel_circuit_topology", prompt, correct, sol, 2, "mcq",
        ["misclassifying_series_vs_parallel_schematics"],
        "Trace the wire from the positive terminal: does it split into junctions, or stay in one single loop?",
        "Multiple loops/junctions = parallel; single continuous loop = series.",
        correct, options=options, diagram_spec=_svg_topology_classify(rng, is_parallel, n_bulbs, v_bat),
    )


def arch_20_parallel_branch_current_splitting_rule(rng: random.Random) -> Dict[str, Any]:
    a2 = rng.choice([0.30, 0.40, 0.50, 0.60])
    a3 = a2  # identical bulbs
    a1 = round(a2 + a3, 2)
    target = rng.choice(["A1", "A4", "A2"])
    if target == "A1":
        prompt_q = f"Given **A2 = {_fmt(a2, 2)} A** and **A3 = {_fmt(a3, 2)} A**, calculate the main current reading on **A1** and state the reading on **A4** [3]."
        correct = f"A1 = {_fmt(a1, 2)} A; A4 = {_fmt(a1, 2)} A"
        sol_step = f"$A_1 = A_2 + A_3 = {_fmt(a2, 2)} + {_fmt(a3, 2)} = {_fmt(a1, 2)}\\text{{ A}}$, and $A_4 = A_1 = {_fmt(a1, 2)}\\text{{ A}}$ [3]."
    elif target == "A4":
        prompt_q = f"Given **A1 = {_fmt(a1, 2)} A**, **A2 = {_fmt(a2, 2)} A**, and **A3 = {_fmt(a3, 2)} A**, determine the reading on **A4** and verify $A_1 = A_2 + A_3$ [2]."
        correct = f"A4 = {_fmt(a1, 2)} A"
        sol_step = f"$A_4 = A_1 = {_fmt(a1, 2)}\\text{{ A}}$ because the two branch currents recombine at the main junction ($A_2 + A_3 = {_fmt(a2, 2)} + {_fmt(a3, 2)} = {_fmt(a1, 2)}\\text{{ A}}$) [2]."
    else:
        prompt_q = f"Given main current **A1 = {_fmt(a1, 2)} A** and lower branch **A3 = {_fmt(a3, 2)} A**, calculate the upper branch current **A2** [2]."
        correct = f"A2 = {_fmt(a2, 2)} A"
        sol_step = f"$A_2 = A_1 - A_3 = {_fmt(a1, 2)} - {_fmt(a3, 2)} = {_fmt(a2, 2)}\\text{{ A}}$ [2]."
    prompt = (
        "Inspect the parallel circuit schematic containing identical bulbs in two parallel branches with ammeters **A1**, **A2**, **A3**, and **A4**.\n\n"
        + prompt_q
    )
    marks = 3 if target == "A1" else 2
    return _q(
        rng, "20", "20_parallel_branch_current_splitting_rule", prompt, correct, sol_step, marks, "math_short",
        ["thinking_branch_currents_equal_total_current_each"],
        "In a parallel circuit, main line currents A1 and A4 are equal, and they split into A2 + A3 across the branches.",
        "Apply A1 = A4 = A2 + A3.",
        correct, diagram_spec=_svg_parallel_four_ammeters(rng, a1, a2, a3, "Bulb 1", "Bulb 2", target),
    )


def arch_21_unequal_parallel_branches_current_division(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([4, 6])
    r2 = r1 * rng.choice([2, 3])
    v_bat = 12
    i1 = round(v_bat / float(r1), 2)
    i2 = round(v_bat / float(r2), 2)
    i_tot = round(i1 + i2, 2)
    prompt = (
        f"In the parallel circuit shown, two unequal resistors **$R_1 = {r1}\\ \\Omega$** (upper branch) and **$R_2 = {r2}\\ \\Omega$** (lower branch) "
        f"are connected across a **{v_bat} V** battery. Ammeter **A2** reads **{_fmt(i1, 2)} A** and **A3** reads **{_fmt(i2, 2)} A**.\n\n"
        f"1. Calculate the total current **A1** leaving the battery [1].\n"
        f"2. State which branch carries the larger current and explain why [2]."
    )
    correct = f"A1 = {_fmt(i_tot, 2)} A; upper branch R1 ({r1} Ω) carries more current because lower resistance allows greater charge flow."
    sol = (
        f"1. **Total Current:** $A_1 = A_2 + A_3 = {_fmt(i1, 2)}\\text{{ A}} + {_fmt(i2, 2)}\\text{{ A}} = {_fmt(i_tot, 2)}\\text{{ A}}$ [1].\n"
        f"2. **Branch Comparison:** The upper branch ($R_1 = {r1}\\ \\Omega$) carries the larger current (${_fmt(i1, 2)}\\text{{ A}} > {_fmt(i2, 2)}\\text{{ A}}$) because it offers **lower resistance** ($I = V / R$) [2]."
    )
    return _q(
        rng, "21", "21_unequal_parallel_branches_current_division", prompt, correct, sol, 3, "short_answer",
        ["thinking_parallel_current_always_splits_50_50"],
        "Even when resistors are unequal, the total current is still A2 + A3. Which path is easier for electrons to flow through?",
        f"A1 = {_fmt(i1, 2)} + {_fmt(i2, 2)} = {_fmt(i_tot, 2)} A; smaller resistor gets more current.",
        correct, diagram_spec=_svg_parallel_four_ammeters(rng, i_tot, i1, i2, f"{r1} Ω", f"{r2} Ω", "A1"),
        marking_points=[
            {"id": "mp_1", "desc": f"A1 = {_fmt(i_tot, 2)} A", "marks": 1, "target_concepts": [_fmt(i_tot, 2)], "editable": True},
            {"id": "mp_2", "desc": f"R1 ({r1} ohm) branch carries more current", "marks": 1, "target_concepts": ["r1", str(r1), "upper"], "editable": True},
            {"id": "mp_3", "desc": "Lower resistance permits greater current", "marks": 1, "target_concepts": ["lower", "resistance"], "editable": True},
        ],
    )


def arch_22_identical_bulbs_in_parallel_equal_brightness(rng: random.Random) -> Dict[str, Any]:
    n_branches = rng.choice([2, 3, 4])
    prompt = (
        f"A learner connects **{n_branches} identical torch light bulbs** in parallel across a fresh 3 V battery.\n\n"
        "How does the brightness of the bulbs compare to one another, and why?"
    )
    correct = f"All {n_branches} bulbs shine with the same brightness because each branch receives the full 3 V supply voltage and carries an equal share of the current."
    options = [
        correct,
        "The top bulb closest to the battery takes all the current and leaves the lower bulbs completely dark.",
        "Each lower bulb glows half as bright as the bulb directly above it.",
        "Adding identical parallel bulbs prevents any current from entering the bottom branch.",
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Every branch in a parallel network connects across the full 3 V supply.\n"
        f"Step 2: Since all {n_branches} bulbs have equal resistance, identical current flows through each branch ($I_b = V / R$), producing equal brightness."
    )
    return _q(
        rng, "22", "22_identical_bulbs_in_parallel_equal_brightness", prompt, correct, sol, 2, "mcq",
        ["assuming_top_parallel_bulb_steals_all_current"],
        "Are the parallel branches connected to identical terminal voltages and identical resistances?",
        "Identical bulbs in parallel each get full battery voltage and equal branch current, so they glow equally brightly.",
        correct, options=options,
    )


def arch_23_adding_bulbs_in_parallel_decreases_total_resistance(rng: random.Random) -> Dict[str, Any]:
    v_bat = rng.choice([3, 6, 12])
    prompt = (
        f"Circuits **X**, **Y**, and **Z** connect 1, 2, and 3 identical bulbs in parallel across a **{v_bat} V** battery as illustrated.\n\n"
        "What happens to the **overall circuit resistance** and **total current drawn from the battery** as more bulbs are added in parallel (from X to Z)?"
    )
    correct = "Overall circuit resistance decreases because more alternative pathways are created, causing the total current supplied by the battery to increase."
    options = [
        correct,
        "Overall circuit resistance increases just like in series, causing total current from the battery to decrease.",
        "Overall resistance and total battery current remain completely unchanged regardless of how many branches are added.",
        "Total current drops to zero in Circuit Z because current splits too thinly.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Every added parallel branch opens another pathway for electrons to travel between battery terminals.\n"
        "Step 2: More pathways reduce the **total effective resistance**, so the battery pushes a **larger total current** ($I_{\\text{total}} = I_1 + I_2 + \\dots$)."
    )
    return _q(
        rng, "23", "23_adding_bulbs_in_parallel_decreases_total_resistance", prompt, correct, sol, 2, "mcq",
        ["adding_parallel_resistors_increases_resistance_myth"],
        "Think about opening extra checkout lanes in a supermarket: does total resistance to flow go up or down?",
        "Adding parallel pathways lowers overall resistance and increases total battery current.",
        correct, options=options, diagram_spec=_svg_parallel_add_branches(rng, v_bat),
    )


def arch_24_school_hall_doors_analogy_for_parallel_pathways(rng: random.Random) -> Dict[str, Any]:
    hall = rng.choice(["school assembly hall", "community sports centre", "matric exam venue"])
    prompt = (
        f"To explain parallel circuits, a science teacher compares electrons leaving a battery to learners exiting a crowded {hall}. "
        "Initially only 1 exit door is open; then a 2nd and 3rd identical exit door are opened alongside the first.\n\n"
        "Which statement correctly translates this analogy into electrical circuit principles?"
    )
    correct = "Opening extra parallel doors lowers the overall resistance to movement and increases the total rate of learner (current) flow leaving the hall."
    options = [
        correct,
        "Opening more exit doors increases crowding at each door and forces fewer learners to leave per minute.",
        "Opening a second door prevents any learners from using the first door.",
        "The exit doors represent cells wired in series that force learners back into the hall.",
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: One exit door = single path; multiple doors side-by-side = parallel branches.\n"
        "Step 2: More parallel exits reduce bottleneck opposition (**lower total resistance**) and raise the **total flow rate (total current)**."
    )
    return _q(
        rng, "24", "24_school_hall_doors_analogy_for_parallel_pathways", prompt, correct, sol, 2, "mcq",
        ["misinterpreting_parallel_branch_flow_analogy"],
        "When extra identical exit doors open side-by-side, can more people leave per second or fewer?",
        "Extra side-by-side doors = parallel branches = lower total opposition = higher total current.",
        correct, options=options,
    )


def arch_25_investigation_variables_adding_resistors_in_parallel(rng: random.Random) -> Dict[str, Any]:
    bulb_rating = rng.choice(["3 V torch bulbs", "6 V identical lamps", "12 V halogen bulbs"])
    prompt = (
        f"A learner investigates how adding {bulb_rating} in parallel affects the main circuit current measured on an ammeter next to the battery.\n\n"
        "State:\n"
        "1. The **independent variable** [1].\n"
        "2. The **dependent variable** [1].\n"
        "3. Why identical bulbs must be used as a **control variable** [1]."
    )
    correct = "Independent: number of bulbs connected in parallel; Dependent: total current strength (ammeter reading); Control: identical bulbs ensure every new branch has the same resistance for a fair test."
    sol = (
        "1. **Independent variable:** Number of bulbs (resistors) added in parallel [1].\n"
        "2. **Dependent variable:** Total current strength measured by the main-line ammeter [1].\n"
        "3. **Control rationale:** Using identical bulbs keeps individual branch resistance constant so changes in current are caused solely by adding parallel branches [1]."
    )
    mps = [
        {"id": "mp_1", "desc": "Independent: number of bulbs in parallel", "marks": 1, "target_concepts": ["number", "bulbs", "parallel"], "editable": True},
        {"id": "mp_2", "desc": "Dependent: total current strength / main ammeter reading", "marks": 1, "target_concepts": ["current", "ammeter"], "editable": True},
        {"id": "mp_3", "desc": "Identical bulbs keep branch resistance equal for a fair test", "marks": 1, "target_concepts": ["identical", "resistance", "fair"], "editable": True},
    ]
    return _q(
        rng, "25", "25_investigation_variables_adding_resistors_in_parallel", prompt, correct, sol, 3, "short_answer",
        ["confusing_controlled_and_independent_variables"],
        "Identify what you deliberately add (independent), what the main ammeter records (dependent), and why all bulbs match.",
        "Independent = parallel branches; Dependent = main current; Control = identical resistance per bulb.",
        correct, marking_points=mps,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_series_circuit_single_pathway_definition": arch_01_series_circuit_single_pathway_definition,
    "02_circuit_diagram_symbol_identification": arch_02_circuit_diagram_symbol_identification,
    "03_ammeter_series_connection_and_low_resistance": arch_03_ammeter_series_connection_and_low_resistance,
    "04_ampere_unit_and_ammeter_scale_reading": arch_04_ampere_unit_and_ammeter_scale_reading,
    "05_current_uniformity_everywhere_in_series_loop": arch_05_current_uniformity_everywhere_in_series_loop,
    "06_adding_resistors_in_series_total_resistance": arch_06_adding_resistors_in_series_total_resistance,
    "07_adding_bulbs_in_series_effect_on_current_and_brightness": arch_07_adding_bulbs_in_series_effect_on_current_and_brightness,
    "08_equal_brightness_of_identical_bulbs_in_series": arch_08_equal_brightness_of_identical_bulbs_in_series,
    "09_investigation_variables_adding_bulbs_in_series": arch_09_investigation_variables_adding_bulbs_in_series,
    "10_formulating_hypothesis_resistors_in_series": arch_10_formulating_hypothesis_resistors_in_series,
    "11_interpreting_series_investigation_results_table": arch_11_interpreting_series_investigation_results_table,
    "12_bulb_heating_experimental_error_in_series_lab": arch_12_bulb_heating_experimental_error_in_series_lab,
    "13_cells_in_series_increasing_current_and_brightness": arch_13_cells_in_series_increasing_current_and_brightness,
    "14_cells_in_series_polarity_alignment_and_reversal": arch_14_cells_in_series_polarity_alignment_and_reversal,
    "15_circuit_safety_precaution_preventing_excess_current_in_cells_series": arch_15_circuit_safety_precaution_preventing_excess_current_in_cells_series,
    "16_delocalised_electron_drift_open_vs_closed_circuit": arch_16_delocalised_electron_drift_open_vs_closed_circuit,
    "17_series_circuit_open_switch_or_broken_filament_fault": arch_17_series_circuit_open_switch_or_broken_filament_fault,
    "18_parallel_circuit_multiple_pathways_definition": arch_18_parallel_circuit_multiple_pathways_definition,
    "19_identifying_series_vs_parallel_circuit_topology": arch_19_identifying_series_vs_parallel_circuit_topology,
    "20_parallel_branch_current_splitting_rule": arch_20_parallel_branch_current_splitting_rule,
    "21_unequal_parallel_branches_current_division": arch_21_unequal_parallel_branches_current_division,
    "22_identical_bulbs_in_parallel_equal_brightness": arch_22_identical_bulbs_in_parallel_equal_brightness,
    "23_adding_bulbs_in_parallel_decreases_total_resistance": arch_23_adding_bulbs_in_parallel_decreases_total_resistance,
    "24_school_hall_doors_analogy_for_parallel_pathways": arch_24_school_hall_doors_analogy_for_parallel_pathways,
    "25_investigation_variables_adding_resistors_in_parallel": arch_25_investigation_variables_adding_resistors_in_parallel,
}
