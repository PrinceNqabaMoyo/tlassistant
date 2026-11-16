"""Grade 10 Physical Sciences — Electric Circuits & Magnetism: Archetypes 01 to 25.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/:
- 04. Magnetism.md: Magnetic fields, poles, field lines, Earth's magnetic field, compass directions, ferromagnetic domains.
- 05. Electrostatics.md: Triboelectric charging, conservation of charge (Q_new = (Q1+Q2)/2), charge quantisation (Q = n*e, e = 1,6 x 10^-19 C), electron transfer direction & mass.
- 06. Electric circuits.md: Circuit symbols, conventional current vs electron drift, current I = Q/Delta t, potential difference V = W/Q, EMF vs terminal potential difference, voltmeter & ammeter placement, cells in series and parallel.

100% Aligned with South African National Curriculum Standards.
Complies strictly with 6-Pillar Generator Contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Electric circuits"
SUBJECT = "Physical Sciences"
GRADE = "10"
E_CHARGE = 1.6e-19  # Elementary charge in C
ELECTRON_MASS = 9.11e-31  # Electron mass in kg


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format decimal numbers using South African comma decimal separator for KaTeX."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{{,}}")


def _fmt_plain(val: float | int, decimals: int = 2) -> str:
    """Format decimal numbers using South African comma decimal separator for plain text."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_q(
    r: random.Random,
    subskill: str,
    num: int,
    prompt: str,
    correct_ans: str,
    worked_sol: str,
    marks: int,
    misconceptions: List[str],
    criteria: List[Dict[str, Any]],
    hints: Dict[str, str],
    diagram_spec: Optional[Dict[str, Any]] = None,
    weight: int = 15,
    duration: int = 5,
) -> Dict[str, Any]:
    qid = f"phys10_circ_{num:02d}_{r.randint(10000, 99999)}"
    q: Dict[str, Any] = {
        "id": qid,
        "question_id": qid,
        "topic": TOPIC,
        "subject": SUBJECT,
        "grade": GRADE,
        "term": 2,
        "subskill": subskill,
        "mode": f"elementary_{subskill}",
        "question_type": "short_answer",
        "question": prompt,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "answer": correct_ans,
        "worked_solution": worked_sol,
        "explanation": worked_sol,
        "marks": marks,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": criteria,
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = "context"
    return q


# =========================================================================== #
# 01. Magnetism: Magnetic Poles, Attraction & Repulsion
# =========================================================================== #
def _build_01_magnetic_poles_attraction_repulsion(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    left_pole = r.choice(["North", "South"])
    right_pole = r.choice(["North", "South"])
    will_attract = (left_pole != right_pole)
    force_type = "attractive" if will_attract else "repulsive"
    action = "attract each other" if will_attract else "repel each other"

    color_l = "#ef4444" if left_pole == "North" else "#3b82f6"
    color_r = "#ef4444" if right_pole == "North" else "#3b82f6"
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 160" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Interaction Between Two Permanent Bar Magnets</text>'
        f'<g transform="translate(40, 50)">'
        f'<rect x="0" y="0" width="70" height="40" fill="{color_l}" rx="4"/>'
        f'<rect x="70" y="0" width="70" height="40" fill="{"#3b82f6" if left_pole == "North" else "#ef4444"}" rx="4"/>'
        f'<text x="35" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">{left_pole[0]}</text>'
        f'<text x="105" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">{"S" if left_pole == "North" else "N"}</text>'
        f'<text x="70" y="55" text-anchor="middle" font-size="11" fill="#475569">Magnet A</text>'
        f'</g>'
        f'<g transform="translate(280, 50)">'
        f'<rect x="0" y="0" width="70" height="40" fill="{color_r}" rx="4"/>'
        f'<rect x="70" y="0" width="70" height="40" fill="{"#3b82f6" if right_pole == "North" else "#ef4444"}" rx="4"/>'
        f'<text x="35" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">{right_pole[0]}</text>'
        f'<text x="105" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">{"S" if right_pole == "North" else "N"}</text>'
        f'<text x="70" y="55" text-anchor="middle" font-size="11" fill="#475569">Magnet B</text>'
        f'</g>'
        f'<path d="M 195 70 L 220 70 M 265 70 L 240 70" stroke="#64748b" stroke-width="2" stroke-dasharray="3,3"/>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying magnetic diagram, the **{left_pole} pole** of Magnet A is brought close to the "
        f"**{right_pole} pole** of Magnet B.\n\n"
        f"1. State whether magnetic forces are classified as contact or non-contact forces.\n"
        f"2. State the fundamental law of magnetic poles.\n"
        f"3. Predict the nature of the magnetic force between Magnet A and Magnet B ({force_type}).\n"
        f"4. If Magnet A is cut directly in half across its middle, describe the magnetic poles of the resulting pieces."
    )
    ans = (
        f"1. Non-contact force; 2. Like magnetic poles repel one another, while unlike magnetic poles attract one another; "
        f"3. The magnets will {action} ({force_type} force); 4. Each piece will form a new, complete magnet with both a North and a South pole."
    )
    sol = (
        f"1. Magnetic forces act across a distance without physical contact, therefore magnetism is a **non-contact force** [1M].\n"
        f"2. **Law of poles:** Like poles repel, unlike poles attract [1M].\n"
        f"3. Because we have a **{left_pole} pole** facing a **{right_pole} pole**, these are {'opposite (unlike)' if will_attract else 'identical (like)'} poles. "
        f"They will **{action}** [1A].\n"
        f"4. Magnetic monopoles do not exist in nature. Cutting a magnet produces two smaller independent magnets, each possessing a North and a South pole [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "01_magnetic_poles_attraction_repulsion", 1, prompt, ans, sol, 4,
        ["magnetic_monopole_fallacy", "confuses_magnetic_poles_with_electrostatic_charges"],
        [
            {"id": "mp1", "desc": "Non-contact force classification", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Law of magnetic poles statement", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Force prediction: {force_type}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Explanation of dipoles (no isolated monopole)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Recall: like poles repel, unlike poles attract. Magnets always exist as dipoles.",
            "tier_2": f"Facing poles: {left_pole} vs {right_pole}. Non-contact force acts through the magnetic field.",
            "tier_3": f"Facing poles will {action}. Both pieces will still have a North and a South pole.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 02. Magnetism: Magnetic Field Lines and Direction
# =========================================================================== #
def _build_02_magnetic_field_lines_and_direction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compass_pos = r.choice(["above North pole", "above South pole", "near middle", "to the left of North pole", "to the right of South pole"])
    if "above North" in compass_pos:
        needle_dir = "pointing away from the North pole"
        cx, cy = 180, 40
    elif "above South" in compass_pos:
        needle_dir = "pointing towards the South pole"
        cx, cy = 280, 40
    elif "left of North" in compass_pos:
        needle_dir = "pointing away from the North pole"
        cx, cy = 90, 100
    elif "right of South" in compass_pos:
        needle_dir = "pointing towards the South pole"
        cx, cy = 370, 100
    else:
        needle_dir = "pointing parallel to the magnet from North towards South"
        cx, cy = 230, 46

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Magnetic Field Lines Surrounding a Bar Magnet</text>'
        f'<g transform="translate(150, 80)">'
        f'<rect x="0" y="0" width="80" height="40" fill="#ef4444" rx="3"/>'
        f'<rect x="80" y="0" width="80" height="40" fill="#3b82f6" rx="3"/>'
        f'<text x="40" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">N</text>'
        f'<text x="120" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">S</text>'
        f'</g>'
        f'<path d="M 150 90 C 80 50, 80 150, 150 110" fill="none" stroke="#64748b" stroke-width="1.8"/>'
        f'<path d="M 310 90 C 380 50, 380 150, 310 110" fill="none" stroke="#64748b" stroke-width="1.8"/>'
        f'<path d="M 180 80 C 180 40, 280 40, 280 80" fill="none" stroke="#64748b" stroke-width="1.8"/>'
        f'<path d="M 180 120 C 180 160, 280 160, 280 120" fill="none" stroke="#64748b" stroke-width="1.8"/>'
        f'<polygon points="235,46 225,41 225,51" fill="#475569"/>'
        f'<polygon points="235,154 225,149 225,159" fill="#475569"/>'
        f'<circle cx="{cx}" cy="{cy}" r="12" fill="#f8fafc" stroke="#0ea5e9" stroke-width="2"/>'
        f'<line x1="{cx - 8}" y1="{cy}" x2="{cx + 8}" y2="{cy}" stroke="#ef4444" stroke-width="2.5"/>'
        f'<text x="{cx}" y="{cy - 16}" text-anchor="middle" font-size="10" fill="#0369a1">Compass</text>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying magnetic field diagram, magnetic field lines are mapped around a permanent bar magnet.\n\n"
        f"1. Define the term **magnetic field**.\n"
        f"2. By convention, state the direction in which magnetic field lines point outside a magnet.\n"
        f"3. Explain what the spacing (density) of magnetic field lines indicates about the magnetic field strength.\n"
        f"4. A plotting compass is positioned **{compass_pos}**. State the direction in which the north-seeking pole of the compass needle will point."
    )
    ans = (
        f"1. A region in space where a magnetic material experiences a magnetic force; "
        f"2. From the North pole to the South pole; "
        f"3. Closer lines indicate a stronger field; lines farther apart indicate a weaker field; "
        f"4. The needle points {needle_dir}."
    )
    sol = (
        f"1. **Magnetic field:** A region in space where a magnet or ferromagnetic material experiences a non-contact magnetic force [1M].\n"
        f"2. Outside the magnet, lines always run **from the North pole to the South pole** [1M].\n"
        f"3. Field line concentration represents flux density: where lines are **closest together** (near the poles), the field is **strongest**; "
        f"where they are widely spaced, the field is **weaker** [1M].\n"
        f"4. A compass needle aligns tangentially with the local magnetic field line, with its north pole pointing along the field: **{needle_dir}** [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "02_magnetic_field_lines_and_direction", 2, prompt, ans, sol, 4,
        ["field_lines_direction_reversed", "crossing_field_lines_misconception"],
        [
            {"id": "mp1", "desc": "Definition of magnetic field", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Direction: North to South outside magnet", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Density indicates field strength", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Compass alignment: {needle_dir}", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Magnetic field lines never cross. Outside a magnet, they point North to South.",
            "tier_2": "The compass north pole points in the direction of the field lines.",
            "tier_3": f"Compass needle direction: {needle_dir}.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 03. Magnetism: Earth's Magnetic Field, Geomagnetism & Aurora
# =========================================================================== #
def _build_03_earth_magnetic_field_and_compass(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    angle_deg = r.choice([11.0, 11.5, 12.0])
    phenom = r.choice(["solar wind shielding", "aurora borealis/australis", "geomagnetic storm"])

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Earth’s Geomagnetic Field and Geographic Axes</text>'
        f'<circle cx="230" cy="115" r="55" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>'
        f'<line x1="230" y1="40" x2="230" y2="190" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>'
        f'<text x="230" y="36" text-anchor="middle" font-size="10" fill="#334155">Geographic North</text>'
        f'<line x1="210" y1="42" x2="250" y2="188" stroke="#ef4444" stroke-width="2.5"/>'
        f'<text x="200" y="48" text-anchor="end" font-size="10" font-weight="bold" fill="#dc2626">Magnetic South (Compass N)</text>'
        f'<text x="245" y="70" font-size="10" fill="#b91c1c">~{_fmt_plain(angle_deg)}°</text>'
        f'<path d="M 230 60 C 130 10, 130 220, 230 170" fill="none" stroke="#64748b" stroke-width="1.5"/>'
        f'<path d="M 230 60 C 330 10, 330 220, 230 170" fill="none" stroke="#64748b" stroke-width="1.5"/>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying geomagnetic diagram, Earth's magnetic field lines are shown surrounding the globe, "
        f"with an angular difference of approximately **{_fmt(angle_deg)}^\\circ** between geographic and magnetic poles.\n\n"
        f"1. Explain why the north-seeking pole of a navigation compass points towards Earth's geographic North Pole.\n"
        f"2. State what causes Earth's magnetic field in the planetary interior.\n"
        f"3. Explain how Earth's magnetosphere protects biological life from the solar wind.\n"
        f"4. Describe how energetic charged particles from the solar wind produce the phenomenon known as **aurorae**."
    )
    ans = (
        f"1. Because unlike poles attract, Earth's geographic North Pole corresponds to a magnetic South pole; "
        f"2. Convection currents of molten iron and nickel in Earth's outer liquid core; "
        f"3. The magnetic field deflects lethal ionizing protons and electrons away from the surface; "
        f"4. Trapped charged particles collide with atmospheric oxygen and nitrogen atoms near the poles, exciting them and emitting light."
    )
    sol = (
        f"1. Since opposite poles attract, the **north pole of a compass needle** is attracted to the **magnetic south pole** "
        f"of Earth's internal geomagnetic field, which is situated near the geographic North Pole [1M].\n"
        f"2. Earth's magnetic field is generated by the **dynamo effect**: circulating electric currents caused by the convection of "
        f"molten iron and nickel in the outer core [1M].\n"
        f"3. The **magnetosphere** deflects high-energy charged particles (solar wind) around Earth, preventing harmful radiation "
        f"from reaching living organisms on the ground [1M].\n"
        f"4. Charged solar particles funnel along field lines toward the poles and collide with atmospheric gas molecules "
        f"(nitrogen and oxygen), causing them to fluoresce and emit characteristic glowing light (aurorae) [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "03_earth_magnetic_field_and_compass", 3, prompt, ans, sol, 4,
        ["geographic_north_equals_magnetic_north_fallacy", "confuses_solar_wind_with_sunlight"],
        [
            {"id": "mp1", "desc": "Compass north attracted to geomagnetic south", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Dynamo effect / molten iron outer core", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Magnetosphere deflection of solar wind", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Mechanism of atmospheric excitation in aurorae", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Recall: opposites attract. The compass North pole is attracted to a magnetic South pole.",
            "tier_2": "The outer core contains flowing molten iron-nickel liquid producing electric currents.",
            "tier_3": "Earth's geographic North pole behaves magnetically as a South pole. Aurorae result from excited gas molecules in the upper atmosphere.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 04. Magnetism: Ferromagnetic Materials and Magnetic Domains
# =========================================================================== #
def _build_04_ferromagnetic_materials_and_domains(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    material = r.choice(["Soft iron (used in transformer cores)", "Hard steel (used in permanent bar magnets)", "Pure nickel"])
    is_soft = "Soft iron" in material

    prompt = (
        f"A laboratory technician investigates the magnetic properties of **{material}**.\n\n"
        f"1. Define the term **ferromagnetic material** and name three pure elemental metals that exhibit ferromagnetism.\n"
        f"2. Explain what a **magnetic domain** is on a microscopic atomic level.\n"
        f"3. Contrast the alignment of domains in an unmagnetised nail versus a magnetised nail.\n"
        f"4. State whether **{material.split(' ')[0]}** is classified as a soft or hard magnetic material, and explain what happens to its domain alignment once an external magnetising field is removed."
    )
    ans = (
        f"1. A material that can be strongly magnetised and shows spontaneous domain magnetisation; iron, nickel, cobalt; "
        f"2. A microscopic region in which the magnetic fields of millions of atomic electron spins align in parallel; "
        f"3. In unmagnetised material domains point in random directions cancelling out; in magnetised material domains align in a common direction; "
        f"4. {'Soft magnetic material: domains quickly randomize and lose magnetisation easily' if is_soft else 'Hard magnetic material: domains remain locked in alignment, retaining permanent magnetisation'}."
    )
    sol = (
        f"1. **Ferromagnetic material:** Substances that form permanent magnets or are strongly attracted by magnets. "
        f"Three elements: **Iron (Fe)**, **Nickel (Ni)**, **Cobalt (Co)** [1M].\n"
        f"2. A **magnetic domain** is a microscopic cluster ($10^{{12}}$ to $10^{{15}}$ atoms) where unpaired electron spins "
        f"align parallel to each other spontaneously [1M].\n"
        f"3. In an **unmagnetised** sample, domains point randomly, so their net external field is zero. "
        f"When **magnetised**, the domains rotate and align in the direction of the external field, producing a strong net field [1M].\n"
        f"4. {material} is a **{'soft' if is_soft else 'hard'}** magnetic material. "
        f"{'It magnetises easily but loses its magnetism when the field is removed (temporary magnet)' if is_soft else 'It requires a strong field to align domains, but retains its magnetisation permanently once aligned'} [1A]."
    )
    return _make_q(
        r, "04_ferromagnetic_materials_and_domains", 4, prompt, ans, sol, 4,
        ["all_metals_are_ferromagnetic_misconception", "domain_theory_misconception"],
        [
            {"id": "mp1", "desc": "Definition and 3 ferromagnetic metals (Fe, Ni, Co)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Definition of magnetic domain", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Random vs aligned domain orientations", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Soft vs hard magnetic material behavior", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Only iron, nickel, and cobalt are ferromagnetic at room temperature.",
            "tier_2": "Domains are regions of aligned atomic spins. Soft iron loses magnetism easily; hard steel retains it.",
            "tier_3": f"{material} is a {'soft' if is_soft else 'hard'} magnetic material.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 05. Magnetism: Magnetic Field Pattern of Two Bar Magnets
# =========================================================================== #
def _build_05_magnetic_field_patterns_two_bar_magnets(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pattern = r.choice(["like_poles_repelling", "opposite_poles_attracting"])
    is_like = (pattern == "like_poles_repelling")
    pole1 = "N" if is_like else "N"
    pole2 = "N" if is_like else "S"

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">'
        f'Field Pattern: Two Bar Magnets ({pole1} facing {pole2})</text>'
        f'<rect x="40" y="65" width="60" height="35" fill="#3b82f6" rx="3"/>'
        f'<rect x="100" y="65" width="60" height="35" fill="#ef4444" rx="3"/>'
        f'<text x="70" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">S</text>'
        f'<text x="130" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">{pole1}</text>'
        f'<rect x="300" y="65" width="60" height="35" fill="{"#ef4444" if pole2 == "N" else "#3b82f6"}" rx="3"/>'
        f'<rect x="360" y="65" width="60" height="35" fill="{"#3b82f6" if pole2 == "N" else "#ef4444"}" rx="3"/>'
        f'<text x="330" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">{pole2}</text>'
        f'<text x="390" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">{"S" if pole2 == "N" else "N"}</text>'
        + (
            f'<path d="M 160 70 C 190 70, 205 30, 205 10" fill="none" stroke="#64748b" stroke-width="1.8"/>'
            f'<path d="M 160 95 C 190 95, 205 135, 205 155" fill="none" stroke="#64748b" stroke-width="1.8"/>'
            f'<path d="M 300 70 C 270 70, 255 30, 255 10" fill="none" stroke="#64748b" stroke-width="1.8"/>'
            f'<path d="M 300 95 C 270 95, 255 135, 255 155" fill="none" stroke="#64748b" stroke-width="1.8"/>'
            f'<circle cx="230" cy="82" r="5" fill="#e2e8f0" stroke="#94a3b8"/>'
            f'<text x="230" y="105" text-anchor="middle" font-size="10" font-weight="bold" fill="#b91c1c">Neutral Point (X)</text>'
            if is_like else
            f'<line x1="160" y1="82" x2="300" y2="82" stroke="#64748b" stroke-width="2"/>'
            f'<polygon points="235,82 225,77 225,87" fill="#475569"/>'
            f'<path d="M 160 70 C 210 40, 250 40, 300 70" fill="none" stroke="#64748b" stroke-width="1.8"/>'
            f'<path d="M 160 95 C 210 125, 250 125, 300 95" fill="none" stroke="#64748b" stroke-width="1.8"/>'
        )
        + f'</svg>'
    )
    prompt = (
        f"In the accompanying magnetic field diagram, two bar magnets are placed along a line with their **{pole1}** and "
        f"**{pole2}** poles facing each other across a gap.\n\n"
        f"1. Identify whether the field pattern represents attraction or repulsion.\n"
        f"2. {'Define what is meant by a neutral point (marked X in the diagram) and state the net magnetic field strength at this point.' if is_like else 'Describe the trajectory and direction of the magnetic field lines in the region directly between the two facing poles.'}\n"
        f"3. Explain why magnetic field lines can never intersect or cross one another.\n"
        f"4. If iron filings are sprinkled around these magnets, explain why they align along the field lines."
    )
    ans = (
        f"1. {'Repulsion' if is_like else 'Attraction'}; "
        f"2. {'A point where opposing magnetic fields cancel out completely (net B = 0)' if is_like else 'Lines run directly and smoothly from the North pole to the South pole in parallel curves'}; "
        f"3. If they crossed, the field would have two different directions at a single point, which is physically impossible; "
        f"4. Each iron filing becomes a tiny induced magnetic dipole that rotates to align parallel to the local magnetic field."
    )
    sol = (
        f"1. Facing **{pole1}** and **{pole2}** poles results in **{'repulsion' if is_like else 'attraction'}** [1M].\n"
        f"2. {'At the neutral point X, the magnetic fields from the two identical North poles are equal in magnitude and opposite in direction, resulting in a net magnetic field of zero ($B_{{\\text{{net}}}} = 0$)' if is_like else 'The magnetic field lines travel directly from the North pole across the gap into the South pole'} [1M].\n"
        f"3. Magnetic field lines indicate the unique direction of the magnetic force on a north pole. If lines crossed, a compass needle at that intersection would point in two contradictory directions simultaneously [1M].\n"
        f"4. Ferromagnetic iron filings are magnetised by induction; each filing develops opposite poles at its ends and aligns along the magnetic flux lines [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "05_magnetic_field_patterns_two_bar_magnets", 5, prompt, ans, sol, 4,
        ["intersecting_field_lines_misconception", "neutral_point_confusion"],
        [
            {"id": "mp1", "desc": "Identification of attraction or repulsion", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Neutral point / field line behavior description", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Proof that field lines cannot cross", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Iron filing dipole alignment explanation", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Like poles create a neutral point where the net field is zero. Lines never cross.",
            "tier_2": "Field lines indicate the unique direction of the magnetic vector.",
            "tier_3": f"Pattern type: {'Repulsion' if is_like else 'Attraction'}.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 06. Electrostatics: Triboelectric Charging by Friction
# =========================================================================== #
def _build_06_triboelectric_charging_by_friction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pair = r.choice([
        {"obj1": "polythene (plastic) rod", "obj2": "wool cloth", "gains": "polythene rod", "loses": "wool cloth", "charge1": "negative", "charge2": "positive"},
        {"obj1": "perspex (glass) rod", "obj2": "silk cloth", "gains": "silk cloth", "loses": "perspex rod", "charge1": "positive", "charge2": "negative"},
        {"obj1": "ebonite rod", "obj2": "cat fur", "gains": "ebonite rod", "loses": "cat fur", "charge1": "negative", "charge2": "positive"},
    ])

    prompt = (
        f"A learner rubs a neutral **{pair['obj1']}** with a dry neutral piece of **{pair['obj2']}**.\n\n"
        f"1. Name the process of charging objects through contact and friction.\n"
        f"2. In this interaction, negative charge is transferred from the **{pair['loses']}** to the **{pair['gains']}**.\n"
        f"   Identify the sign of the overall electric charge acquired by each object.\n"
        f"3. Explain why protons are not transferred between the objects during the rubbing process.\n"
        f"4. State the **Principle of Conservation of Charge** and verify whether charge was conserved in this experiment."
    )
    ans = (
        f"1. Triboelectric charging; 2. {pair['obj1']}: {pair['charge1']}; {pair['obj2']}: {pair['charge2']}; "
        f"3. Protons are bound tightly inside the atomic nucleus by strong nuclear forces, whereas outer valence electrons are mobile; "
        f"4. Charge is conserved: the magnitude of negative charge gained by the {pair['gains']} equals the magnitude of positive charge left on the {pair['loses']}."
    )
    sol = (
        f"1. The process is **triboelectric charging** (charging by friction) [1M].\n"
        f"2. Gaining electrons gives the **{pair['gains']}** an excess of negative charges $\\rightarrow$ **negative charge**; "
        f"losing electrons leaves the **{pair['loses']}** electron-deficient $\\rightarrow$ **positive charge** [1M].\n"
        f"3. Protons reside within the atomic nucleus and are bound by the strong nuclear force with large mass ($m_p \\approx 1836\\, m_e$). "
        f"Only outer-shell **electrons** are mobile and can be transferred between materials [1M].\n"
        f"4. **Principle of Conservation of Charge:** The net charge of an isolated system remains constant during any physical process. "
        f"Total charge before was $0 + 0 = 0$; after rubbing, $+q + (-q) = 0$, so charge is strictly conserved [1A]."
    )
    return _make_q(
        r, "06_triboelectric_charging_by_friction", 6, prompt, ans, sol, 4,
        ["proton_transfer_fallacy", "charge_creation_misconception"],
        [
            {"id": "mp1", "desc": "Naming triboelectric charging", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Signs of charges on both rubbed objects", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Only electrons move (protons bound in nucleus)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Principle of Conservation of Charge statement & verification", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Only electrons are transferred during rubbing. Protons stay in the nucleus.",
            "tier_2": "Gaining electrons = negative charge; losing electrons = positive charge.",
            "tier_3": f"{pair['obj1']} becomes {pair['charge1']}, {pair['obj2']} becomes {pair['charge2']}.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 07. Electrostatics: Force Between Charges & Polarization of Neutral Objects
# =========================================================================== #
def _build_07_electrostatic_force_and_polarization_neutral_object(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    rod_charge = r.choice(["negatively charged", "positively charged"])
    is_neg = (rod_charge == "negatively charged")

    prompt = (
        f"A **{rod_charge}** plastic ruler is brought close to small, neutral scraps of paper resting on a table, "
        f"without making physical contact.\n\n"
        f"1. State the fundamental law of electrostatics regarding like and unlike charges.\n"
        f"2. Explain why the neutral paper scraps are attracted to the {rod_charge} ruler even though the scraps carry zero resultant electric charge.\n"
        f"3. Name the physical process occurring within the atoms of the paper scraps.\n"
        f"4. If a paper scrap momentarily touches the ruler, predict what will happen immediately after contact."
    )
    ans = (
        f"1. Like charges repel, unlike charges attract; "
        f"2. Charge separation (polarization) occurs in the paper; opposite charges are pulled closer to the ruler than like charges, resulting in a net attractive electrostatic force; "
        f"3. Electrostatic polarization (induced dipole formation); "
        f"4. The paper scrap acquires the same charge as the ruler by conduction and is immediately repelled."
    )
    sol = (
        f"1. **Law of electrostatics:** Like electric charges repel one another; unlike electric charges attract one another [1M].\n"
        f"2. The {rod_charge} rod causes **polarization**: {'electrons in paper atoms are repelled away from the surface, leaving induced positive charges closest to the ruler' if is_neg else 'electrons in paper atoms are pulled toward the surface, making the near surface negative'}. "
        f"Because the closer opposite charges experience a stronger force than the farther like charges ($F \\propto 1/r^2$), "
        f"the net electrostatic force is **attractive** [1M].\n"
        f"3. This process is termed **electrostatic polarization** [1M].\n"
        f"4. Upon contact, charge transfers from the ruler to the paper scrap. Having identical charges, they will now **repel each other** [1A]."
    )
    return _make_q(
        r, "07_electrostatic_force_and_polarization_neutral_object", 7, prompt, ans, sol, 4,
        ["neutral_objects_have_no_charges_misconception", "attraction_implies_opposite_charge_fallacy"],
        [
            {"id": "mp1", "desc": "Fundamental law of electrostatics", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Mechanism of net attraction due to closer induced opposite charge", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Naming polarization", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Charge transfer on contact resulting in repulsion", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Neutral objects contain equal positive and negative charges. Close charges feel a stronger force.",
            "tier_2": "The charged rod induces a dipole in the insulator (polarization).",
            "tier_3": "The paper is attracted due to polarization. After touching, it acquires the same charge and repels.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 08. Electrostatics: Charge Conservation (Two Identical Spheres in Contact)
# =========================================================================== #
def _build_08_charge_conservation_two_identical_spheres(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    q1 = r.choice([-10, -8, -6, -4, -2, 2, 4, 6, 8, 12])
    q2 = r.choice([-6, -4, -2, 2, 4, 6, 8, 10, 14])
    while q1 == q2 or (q1 + q2) % 2 != 0:
        q2 = r.choice([-6, -4, -2, 2, 4, 6, 8, 10, 14])

    q_new = (q1 + q2) // 2
    delta_q = abs(q_new - q1)
    delta_q_c = delta_q * 1e-9
    num_e = delta_q_c / E_CHARGE
    donor = "Sphere 1 to Sphere 2" if q1 < q2 else "Sphere 2 to Sphere 1"

    prompt = (
        f"Two identical conducting spheres on insulated stands carry initial charges of "
        f"**$Q_1 = {q1}\\text{{ nC}}$** and **$Q_2 = {q2}\\text{{ nC}}$** respectively.\n"
        f"The two spheres are brought into contact, allowed to reach electrostatic equilibrium, and then separated.\n\n"
        f"1. State the **Principle of Conservation of Charge**.\n"
        f"2. Calculate the final charge ($Q_{{\\text{{new}}}}$) on each sphere after separation.\n"
        f"3. Calculate the number of electrons transferred between the spheres during contact.\n"
        f"4. State the direction of electron transfer ({donor})."
    )
    ans = (
        f"1. The net charge of an isolated system remains constant during any physical process; "
        f"2. Q_new = {q_new} nC; 3. n = {num_e:.2e} electrons; 4. Electrons moved from {donor}."
    )
    sol = (
        f"1. **Principle of Conservation of Charge:** The net charge of an isolated system remains constant during any physical process [1M].\n"
        f"2. $Q_{{\\text{{new}}}} = \\frac{{Q_1 + Q_2}}{{2}} = \\frac{{{q1} + ({q2})}}{{2}} = {q_new}\\text{{ nC}}$ [1A].\n"
        f"3. Charge transferred: $\\Delta Q = |Q_{{\\text{{new}}}} - Q_1| = |{q_new} - ({q1})| = {delta_q}\\text{{ nC}} = {delta_q} \\times 10^{{-9}}\\text{{ C}}$ [1M].\n"
        f"   $n = \\frac{{\\Delta Q}}{{e}} = \\frac{{{delta_q} \\times 10^{{-9}}}}{{1{{,}}6 \\times 10^{{-19}}}} = {num_e:.2e}\\text{{ electrons}}$ [1A].\n"
        f"4. Electrons are negative, so they flow from the sphere with more negative (or less positive) initial charge: **from {donor}** [1A]."
    )
    return _make_q(
        r, "08_charge_conservation_two_identical_spheres", 8, prompt, ans, sol, 5,
        ["sign_addition_error_in_charge_conservation", "forgot_nano_prefix_conversion"],
        [
            {"id": "mp1", "desc": "Statement of Conservation of Charge", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Formula and calculation of Q_new = {q_new} nC", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Delta Q calculation with 10^-9 factor", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Electron calculation n = {num_e:.2e}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Direction of electron transfer ({donor})", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$Q_{\\text{new}} = \\frac{Q_1 + Q_2}{2}$ and $n = \\frac{\\Delta Q}{e}$. Note: $1\\text{ nC} = 10^{-9}\\text{ C}$.",
            "tier_2": f"Initial charges: {q1} nC and {q2} nC. Average: ({q1} + {q2})/2 = {q_new} nC.",
            "tier_3": f"Q_new = {q_new} nC; n = {num_e:.2e} electrons from {donor}.",
        },
        weight=15, duration=5,
    )


# =========================================================================== #
# 09. Electrostatics: Charge Conservation (Three Spheres Stepwise Contact)
# =========================================================================== #
def _build_09_charge_conservation_three_spheres_successive_contact(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    qa = r.choice([12, 16, 20, 24])
    qb = r.choice([-4, -8, 0, 4])
    qc = 0  # Sphere C initially neutral

    # Step 1: Sphere A touches B, then separated
    q_ab = (qa + qb) / 2
    # Step 2: Sphere B touches C, then separated
    q_bc = (q_ab + qc) / 2

    prompt = (
        f"Three identical conducting spheres on insulated stands have initial charges of "
        f"**$Q_A = {qa}\\text{{ nC}}$**, **$Q_B = {qb}\\text{{ nC}}$**, and **$Q_C = {qc}\\text{{ nC}}$** (neutral).\n\n"
        f"**Step 1:** Sphere A is brought into contact with Sphere B and then separated.\n"
        f"**Step 2:** Sphere B is then brought into contact with Sphere C and separated.\n\n"
        f"1. Calculate the charge on Sphere A after Step 1.\n"
        f"2. Calculate the charge on Sphere B immediately after Step 1.\n"
        f"3. Calculate the final charge on Sphere B and Sphere C after Step 2.\n"
        f"4. Verify that total charge was conserved throughout the entire sequence."
    )
    ans = (
        f"1. Q_A = {_fmt(q_ab)} nC; 2. Q_B = {_fmt(q_ab)} nC; 3. Q_B = Q_C = {_fmt(q_bc)} nC; "
        f"4. Total charge initially = {qa + qb} nC; final sum = {_fmt(q_ab)} + {_fmt(q_bc)} + {_fmt(q_bc)} = {qa + qb} nC."
    )
    sol = (
        f"1. & 2. In Step 1, A and B touch: $Q_{{A1}} = Q_{{B1}} = \\frac{{Q_A + Q_B}}{{2}} = \\frac{{{qa} + ({qb})}}{{2}} = {_fmt(q_ab)}\\text{{ nC}}$ [2M].\n"
        f"3. In Step 2, Sphere B (now carrying ${_fmt(q_ab)}\\text{{ nC}}$) touches neutral Sphere C ($0\\text{{ nC}}$):\n"
        f"   $Q_{{B2}} = Q_{{C2}} = \\frac{{Q_{{B1}} + Q_C}}{{2}} = \\frac{{{_fmt(q_ab)} + 0}}{{2}} = {_fmt(q_bc)}\\text{{ nC}}$ [2M].\n"
        f"4. Total initial charge: $Q_{{\\text{{total}}}} = {qa} + ({qb}) + 0 = {qa + qb}\\text{{ nC}}$.\n"
        f"   Total final charge: $Q_A + Q_B + Q_C = {_fmt(q_ab)} + {_fmt(q_bc)} + {_fmt(q_bc)} = {qa + qb}\\text{{ nC}}$. "
        f"   Charge is strictly conserved [1A]."
    )
    return _make_q(
        r, "09_charge_conservation_three_spheres_successive_contact", 9, prompt, ans, sol, 5,
        ["simultaneous_contact_assumption_fallacy", "arithmetic_sign_error"],
        [
            {"id": "mp1", "desc": "Step 1: Q_A after first contact", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Step 1: Q_B after first contact", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Step 2: Formula for B touching C", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Step 2: Final charge on B and C = {_fmt(q_bc)} nC", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Conservation proof sum verification", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Calculate step-by-step. In Step 2, use the NEW charge of Sphere B from Step 1.",
            "tier_2": f"Step 1: ({qa} + {qb})/2 = {_fmt(q_ab)} nC. Step 2: ({_fmt(q_ab)} + 0)/2.",
            "tier_3": f"Q_A = {_fmt(q_ab)} nC, Q_B = Q_C = {_fmt(q_bc)} nC.",
        },
        weight=15, duration=5,
    )


# =========================================================================== #
# 10. Electrostatics: Charge Quantisation (Q = n * e)
# =========================================================================== #
def _build_10_charge_quantization_number_of_electrons(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_exp = r.choice([10, 11, 12, 13])
    n_base = r.choice([2, 3, 4, 5, 8, 15, 25])
    num_e = n_base * (10 ** n_exp)
    charge_c = num_e * E_CHARGE
    charge_nc = charge_c * 1e9

    prompt = (
        f"A negatively charged conducting sphere carries a net electrostatic charge of "
        f"**$Q = -{_fmt(charge_nc)}\\text{{ nC}}$**.\n\n"
        f"1. State the **Principle of Charge Quantisation**.\n"
        f"2. State the magnitude of the elementary charge ($e$) in Coulombs.\n"
        f"3. Calculate the number of excess electrons ($n$) residing on the sphere."
    )
    ans = (
        f"1. All charges in the universe are integer multiples of the elementary charge e; "
        f"2. e = 1,6 x 10^-19 C; 3. n = {num_e:.2e} electrons."
    )
    sol = (
        f"1. **Principle of Charge Quantisation:** The charge on any object is an integral multiple of the elementary charge ($Q = n \\cdot e$, where $n \\in \\mathbb{{Z}}$) [1M].\n"
        f"2. Elementary charge: $e = 1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$ [1M].\n"
        f"3. $Q = -{_fmt(charge_nc)}\\text{{ nC}} = -{_fmt(charge_nc)} \\times 10^{{-9}}\\text{{ C}}$ [1M].\n"
        f"   $n = \\frac{{|Q|}}{{e}} = \\frac{{{_fmt(charge_c)}}}{{1{{,}}6 \\times 10^{{-19}}}} = {num_e:.2e}\\text{{ electrons}}$ [1A]."
    )
    return _make_q(
        r, "10_charge_quantization_number_of_electrons", 10, prompt, ans, sol, 4,
        ["forgot_elementary_charge_value", "inverted_quantization_formula"],
        [
            {"id": "mp1", "desc": "Statement of Charge Quantisation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Value of elementary charge e", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Unit conversion nC to C", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculated electron count = {num_e:.2e}", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$Q = n \\cdot e$. Convert nC to Coulombs by multiplying by $10^{-9}$.",
            "tier_2": f"Divide charge by $1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$.",
            "tier_3": f"n = {num_e:.2e} electrons.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 11. Electrostatics: Permissible Charge Validity Test
# =========================================================================== #
def _build_11_charge_quantization_charge_validity_test(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    is_valid = r.choice([True, False])
    if is_valid:
        n = r.choice([2500, 4000, 5500, 7500, 10000])
        test_q_c = n * E_CHARGE
    else:
        n_approx = r.choice([2500, 4000, 5500, 7500])
        test_q_c = (n_approx + 0.35) * E_CHARGE

    prompt = (
        f"A researcher claims to have measured an isolated electrostatic charge of "
        f"**$Q = {_fmt(test_q_c * 1e15)}\\text{{ fC}}$** ($Q = {_fmt(test_q_c * 1e15)} \\times 10^{{-15}}\\text{{ C}}$) on a suspended particle.\n\n"
        f"1. State the mathematical condition required by the Principle of Charge Quantisation ($Q = n \\cdot e$).\n"
        f"2. Perform a calculation to test whether this measured charge is physically permissible.\n"
        f"3. Conclude with a clear statement: is this charge valid or invalid, and provide your scientific justification."
    )
    ans = (
        f"1. n = Q / e must be an integer (whole number); 2. n = {test_q_c / E_CHARGE:.2f}; "
        f"3. This charge is {'VALID' if is_valid else 'INVALID'} because n is {'an integer' if is_valid else 'not an integer; fractional electrons cannot exist in isolation'}."
    )
    sol = (
        f"1. According to the **Principle of Charge Quantisation**, $n = \\frac{{Q}}{{e}}$ must be a whole positive or negative integer ($n \\in \\mathbb{{Z}}$) [1M].\n"
        f"2. $n = \\frac{{Q}}{{e}} = \\frac{{{_fmt(test_q_c)}}}{{1{{,}}6 \\times 10^{{-19}}}} = {test_q_c / E_CHARGE:.2f}$ [1M].\n"
        f"3. Conclusion: The charge is **{'VALID' if is_valid else 'INVALID'}** [1A]. "
        f"{'Since n is exactly an integer, the charge corresponds to an exact number of elementary charges.' if is_valid else 'Electrons are indivisible in electrostatics; fractional elementary charges cannot exist on isolated bodies.'} [1M]."
    )
    return _make_q(
        r, "11_charge_quantization_charge_validity_test", 11, prompt, ans, sol, 4,
        ["accepts_fractional_electrons_misconception", "misunderstands_charge_quantisation"],
        [
            {"id": "mp1", "desc": "Integer condition n in Z", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Calculation of n = Q/e", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Valid/Invalid conclusion ({'VALID' if is_valid else 'INVALID'})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Justification regarding indivisibility of electron", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Calculate n = Q / e. Check if n is an integer.",
            "tier_2": f"n = {test_q_c / E_CHARGE:.2f}. An electron cannot be split in half.",
            "tier_3": f"Charge is {'VALID' if is_valid else 'INVALID'}.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 12. Electrostatics: Electron Transfer Direction and Mass Change
# =========================================================================== #
def _build_12_electron_transfer_direction_and_mass_change(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_electrons = r.choice([2.5e12, 5.0e12, 1.0e13, 2.0e13])
    delta_mass_kg = n_electrons * ELECTRON_MASS
    q_transferred_c = n_electrons * E_CHARGE
    q_transferred_uc = q_transferred_c * 1e6

    prompt = (
        f"During an electrostatic charging process, **{n_electrons:.1e} electrons** are transferred from a wool cloth to a plastic rod.\n\n"
        f"1. Calculate the magnitude of the electric charge transferred in microcoulombs ($\\mu\\text{{C}}$).\n"
        f"2. Given the rest mass of an electron ($m_e = 9{{,}}11 \\times 10^{{-31}}\\text{{ kg}}$), calculate the total mass gained by the plastic rod in kilograms.\n"
        f"3. Explain why this gain in mass is impossible to detect using a standard school laboratory electronic balance."
    )
    ans = (
        f"1. Q = {_fmt(q_transferred_uc)} uC; 2. Delta m = {delta_mass_kg:.2e} kg; "
        f"3. The mass change (~{delta_mass_kg:.2e} kg) is infinitely smaller than the precision limit of school balances (0,01 g = 10^-5 kg)."
    )
    sol = (
        f"1. $Q = n \\cdot e = ({n_electrons:.1e}) \\times (1{{,}}6 \\times 10^{{-19}}\\text{{ C}}) = {_fmt(q_transferred_c)}\\text{{ C}} = {_fmt(q_transferred_uc)}\\ \\mu\\text{{C}}$ [1A].\n"
        f"2. $\\Delta m = n \\times m_e = ({n_electrons:.1e}) \\times (9{{,}}11 \\times 10^{{-31}}\\text{{ kg}}) = {delta_mass_kg:.2e}\\text{{ kg}}$ [2M].\n"
        f"3. The mass gain of $\\approx {delta_mass_kg:.2e}\\text{{ kg}}$ is extremely negligible, several orders of magnitude below the resolution of laboratory balances ($0{{,}}001\\text{{ g}} = 10^{{-6}}\\text{{ kg}}$) [1M]."
    )
    return _make_q(
        r, "12_electron_transfer_direction_and_mass_change", 12, prompt, ans, sol, 4,
        ["charge_has_no_mass_misconception", "microcoulomb_prefix_error"],
        [
            {"id": "mp1", "desc": "Calculation of Q = n*e in microcoulombs", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula Delta m = n * m_e", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of Delta m = {delta_mass_kg:.2e} kg", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Scientific explanation of imperceptible mass change", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$Q = n \\cdot e$ and $\\Delta m = n \\cdot m_e$. Remember $1\\ \\mu\\text{C} = 10^{-6}\\text{ C}$.",
            "tier_2": f"Multiply {n_electrons:.1e} by electron mass $9{{,}}11 \\times 10^{{-31}}\\text{{ kg}}$.",
            "tier_3": f"Q = {_fmt(q_transferred_uc)} uC; Delta m = {delta_mass_kg:.2e} kg.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 13. Electric Circuits: Circuit Components & Standard Symbols
# =========================================================================== #
def _build_13_circuit_components_and_symbols_identification(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    symbols = [
        {"name": "Cell", "desc": "Single electrochemical energy source providing potential difference", "svg_part": '<line x1="20" y1="30" x2="35" y2="30"/><line x1="35" y1="15" x2="35" y2="45" stroke-width="2.5"/><line x1="43" y1="20" x2="43" y2="40" stroke-width="4"/><line x1="43" y1="30" x2="60" y2="30"/>'},
        {"name": "Open Switch", "desc": "Breaks the conducting path to stop current flow", "svg_part": '<line x1="20" y1="30" x2="35" y2="30"/><circle cx="35" cy="30" r="3"/><line x1="35" y1="30" x2="52" y2="16"/><circle cx="55" cy="30" r="3"/><line x1="55" y1="30" x2="70" y2="30"/>'},
        {"name": "Light Bulb (Lamp)", "desc": "Converts electrical energy into light and heat energy", "svg_part": '<line x1="20" y1="30" x2="30" y2="30"/><circle cx="45" cy="30" r="14" fill="none"/><line x1="35" y1="20" x2="55" y2="40"/><line x1="35" y1="40" x2="55" y2="20"/><line x1="60" y1="30" x2="70" y2="30"/>'},
        {"name": "Resistor", "desc": "Opposes the flow of electric charge and drops voltage", "svg_part": '<line x1="15" y1="30" x2="25" y2="30"/><rect x="25" y="20" width="30" height="20" fill="none"/><line x1="55" y1="30" x2="65" y2="30"/>'},
        {"name": "Voltmeter", "desc": "Measures potential difference across two points; connected in parallel", "svg_part": '<line x1="15" y1="30" x2="25" y2="30"/><circle cx="45" cy="30" r="15" fill="none"/><text x="45" y="35" text-anchor="middle" font-weight="bold">V</text><line x1="65" y1="30" x2="75" y2="30"/>'},
        {"name": "Ammeter", "desc": "Measures the rate of flow of charge; connected in series", "svg_part": '<line x1="15" y1="30" x2="25" y2="30"/><circle cx="45" cy="30" r="15" fill="none"/><text x="45" y="35" text-anchor="middle" font-weight="bold">A</text><line x1="65" y1="30" x2="75" y2="30"/>'},
    ]
    chosen = r.sample(symbols, 4)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 140" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">Standard Electric Circuit Component Symbols</text>'
        f'<g stroke="#1e293b" stroke-width="2" fill="#0f172a">'
        f'<g transform="translate(20, 35)">{chosen[0]["svg_part"]}<text x="40" y="70" stroke="none" text-anchor="middle" font-size="11">Symbol (A)</text></g>'
        f'<g transform="translate(130, 35)">{chosen[1]["svg_part"]}<text x="40" y="70" stroke="none" text-anchor="middle" font-size="11">Symbol (B)</text></g>'
        f'<g transform="translate(240, 35)">{chosen[2]["svg_part"]}<text x="40" y="70" stroke="none" text-anchor="middle" font-size="11">Symbol (C)</text></g>'
        f'<g transform="translate(350, 35)">{chosen[3]["svg_part"]}<text x="40" y="70" stroke="none" text-anchor="middle" font-size="11">Symbol (D)</text></g>'
        f'</g>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying circuit symbol diagram, four standard circuit symbols labeled (A), (B), (C), and (D) are illustrated.\n\n"
        f"1. Identify the name of each component represented by symbols (A), (B), (C), and (D).\n"
        f"2. State the primary operational function of component (A).\n"
        f"3. State whether component (D) must be connected in series or in parallel within a circuit, giving a reason."
    )
    ans = (
        f"1. (A) {chosen[0]['name']}, (B) {chosen[1]['name']}, (C) {chosen[2]['name']}, (D) {chosen[3]['name']}; "
        f"2. {chosen[0]['desc']}; "
        f"3. Connected in {'series' if 'Ammeter' in chosen[3]['name'] else 'parallel' if 'Voltmeter' in chosen[3]['name'] else 'series or parallel depending on design'}."
    )
    sol = (
        f"1. Component identification [2M]:\n"
        f"   - (A): **{chosen[0]['name']}**\n"
        f"   - (B): **{chosen[1]['name']}**\n"
        f"   - (C): **{chosen[2]['name']}**\n"
        f"   - (D): **{chosen[3]['name']}**\n"
        f"2. Function of (A) ({chosen[0]['name']}): {chosen[0]['desc']} [1M].\n"
        f"3. Connection of (D) ({chosen[3]['name']}): {'Connected in series to measure all charge passing through the branch' if 'Ammeter' in chosen[3]['name'] else 'Connected in parallel to measure potential difference across two points without diverting branch current' if 'Voltmeter' in chosen[3]['name'] else 'Connected in series with circuit loads'} [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "13_circuit_components_and_symbols_identification", 13, prompt, ans, sol, 4,
        ["confuses_voltmeter_and_ammeter_symbols", "resistor_lightbulb_symbol_confusion"],
        [
            {"id": "mp1", "desc": "Identification of components A, B, C, D", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Function of component A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Connection rule and justification for component D", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Circle with V is voltmeter (parallel); circle with A is ammeter (series); circle with X is bulb.",
            "tier_2": "Cell has long thin positive line and short thick negative line.",
            "tier_3": f"(A) {chosen[0]['name']}, (B) {chosen[1]['name']}, (C) {chosen[2]['name']}, (D) {chosen[3]['name']}.",
        },
        diagram_spec=diag, weight=10, duration=4,
    )


# =========================================================================== #
# 14. Electric Circuits: Conventional Current vs Electron Flow
# =========================================================================== #
def _build_14_conventional_current_vs_electron_drift(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    charge_val = r.choice([1.5, 2.0, 2.5, 3.0, 4.0, 5.0])
    carrier_is_pos = r.choice([True, False])
    carrier_desc = f"+{_fmt(charge_val)}\\text{{ C}}" if carrier_is_pos else f"-{_fmt(charge_val)}\\text{{ C}}"
    carrier_type = "positive test charge" if carrier_is_pos else "negatively charged electron packet"
    flow_type = "conventional current" if carrier_is_pos else "real electron flow"
    away_terminal = "positive terminal (+)" if carrier_is_pos else "negative terminal (-)"
    toward_terminal = "negative terminal (-)" if carrier_is_pos else "positive terminal (+)"

    prompt = (
        f"In electric circuit theory, a fundamental distinction is made between **conventional current** and **electron flow**.\n\n"
        f"1. State the direction of **conventional current** in an external circuit.\n"
        f"2. State the direction of actual **electron drift** in an external metallic conductor.\n"
        f"3. Briefly explain the historical reason why conventional current points in the opposite direction to electron flow.\n"
        f"4. A **{carrier_type}** carrying **${carrier_desc}$** moves along the external circuit in the direction of {flow_type}. "
        f"State which terminal of the source it is moving away from, and which terminal it is moving towards."
    )
    ans = (
        f"1. From the positive terminal to the negative terminal; "
        f"2. From the negative terminal to the positive terminal; "
        f"3. Benjamin Franklin established the convention before the electron was discovered, assuming positive charges flowed; "
        f"4. Moving away from the {away_terminal} and towards the {toward_terminal}."
    )
    sol = (
        f"1. **Conventional current:** Defined as flowing from the **positive terminal ($+$) to the negative terminal ($-$)** through the external circuit [1M].\n"
        f"2. **Electron flow:** Real mobile charge carriers in metals are negatively charged electrons that are repelled by the negative terminal and attracted to the positive terminal: from **negative ($-$) to positive ($+$)** [1M].\n"
        f"3. **Historical origin:** In the 18th century, Benjamin Franklin hypothesised electricity as a single fluid flowing from positive to negative. When J.J. Thomson discovered the electron in 1897, the convention was already universally adopted in engineering and retained [1M].\n"
        f"4. The {carrier_type} (${carrier_desc}$) moving in the direction of {flow_type} is repelled by the {away_terminal} and attracted towards the {toward_terminal} [1A]."
    )
    return _make_q(
        r, "14_conventional_current_vs_electron_drift", 14, prompt, ans, sol, 4,
        ["confuses_electron_flow_with_conventional_current", "charge_carrier_polarity_confusion"],
        [
            {"id": "mp1", "desc": "Direction of conventional current (+ to -)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Direction of electron flow (- to +)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Historical explanation (Franklin / early convention)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Motion of {carrier_desc} (away from {away_terminal}, towards {toward_terminal})", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Conventional current: positive to negative. Electron drift: negative to positive.",
            "tier_2": f"Consider the charge sign ({carrier_desc}): like charges repel, unlike attract.",
            "tier_3": f"1. Positive to negative. 2. Negative to positive. 4. Away from {away_terminal}.",
        },
        weight=10, duration=3,
    )


# =========================================================================== #
# 15. Electric Circuits: Current Definition (I = Q / Delta t)
# =========================================================================== #
def _build_15_electric_current_definition_I_Q_t(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    time_s = r.choice([2, 4, 5, 8, 10, 15, 20])
    current_a = r.choice([0.5, 1.2, 1.5, 2.0, 2.5, 3.0, 4.5])
    charge_c = round(current_a * time_s, 2)

    prompt = (
        f"During an experiment, an amount of charge equal to **${_fmt(charge_c)}\\text{{ C}}$** passes past a fixed cross-section "
        f"of a conducting wire in a time interval of **{time_s} seconds**.\n\n"
        f"1. Define the term **electric current**.\n"
        f"2. State the SI unit of current and define it in terms of Coulombs and seconds.\n"
        f"3. Calculate the electric current ($I$) flowing through the conductor."
    )
    ans = (
        f"1. The rate of flow of electric charge; 2. Ampere (A), 1 A = 1 C/s (one coulomb per second); "
        f"3. I = {_fmt(current_a)} A."
    )
    sol = (
        f"1. **Electric current:** The rate of flow of charge [1M].\n"
        f"2. The SI unit is the **Ampere (A)**. One ampere is defined as one coulomb of charge moving past a point in one second ($1\\text{{ A}} = 1\\text{{ C}}\\cdot\\text{{s}}^{{-1}}$) [1M].\n"
        f"3. $I = \\frac{{Q}}{{\\Delta t}}$ [1M]\n"
        f"   $I = \\frac{{{_fmt(charge_c)}\\text{{ C}}}}{{{time_s}\\text{{ s}}}} = {_fmt(current_a)}\\text{{ A}}$ [1A]."
    )
    return _make_q(
        r, "15_electric_current_definition_I_Q_t", 15, prompt, ans, sol, 4,
        ["current_is_energy_misconception", "formula_inversion_error"],
        [
            {"id": "mp1", "desc": "Definition of electric current", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Unit Ampere = Coulomb/second", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula I = Q / Delta t", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation I = {_fmt(current_a)} A", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$I = \\frac{Q}{\\Delta t}$. Current is measured in Amperes ($1\\text{ A} = 1\\text{ C/s}$).",
            "tier_2": f"Divide {_fmt(charge_c)} C by {time_s} s.",
            "tier_3": f"I = {_fmt(current_a)} A.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 16. Electric Circuits: Current Time Conversion (Minutes & Hours to Seconds)
# =========================================================================== #
def _build_16_electric_current_time_conversion_minutes_hours(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    time_unit = r.choice(["minutes", "hours"])
    if time_unit == "minutes":
        t_val = r.choice([2, 3, 5, 8, 10, 15])
        t_sec = t_val * 60
    else:
        t_val = r.choice([0.5, 1.0, 1.5, 2.0])
        t_sec = int(t_val * 3600)

    current_a = r.choice([0.4, 0.8, 1.5, 2.0, 3.2])
    charge_c = round(current_a * t_sec, 1)

    prompt = (
        f"An electric heating element carries a steady current of **${_fmt(current_a)}\\text{{ A}}$** for a duration of "
        f"**{_fmt_plain(t_val)} {time_unit}**.\n\n"
        f"1. Convert the operating time into standard SI units (seconds).\n"
        f"2. Write down the relationship connecting charge ($Q$), current ($I$), and time interval ($\\Delta t$).\n"
        f"3. Calculate the total charge ($Q$) in Coulombs that flows through the element during this period."
    )
    ans = f"1. Delta t = {t_sec} s; 2. Q = I * Delta t; 3. Q = {_fmt(charge_c)} C."
    sol = (
        f"1. Time conversion: $\\Delta t = {_fmt_plain(t_val)} \\times {60 if time_unit == 'minutes' else 3600} = {t_sec}\\text{{ s}}$ [1M].\n"
        f"2. $I = \\frac{{Q}}{{\\Delta t}} \\implies Q = I \\times \\Delta t$ [1M].\n"
        f"3. $Q = ({_fmt(current_a)}\\text{{ A}}) \\times ({t_sec}\\text{{ s}}) = {_fmt(charge_c)}\\text{{ C}}$ [2M]."
    )
    return _make_q(
        r, "16_electric_current_time_conversion_minutes_hours", 16, prompt, ans, sol, 4,
        ["forgot_time_unit_conversion_to_seconds", "multiplication_by_60_instead_of_3600"],
        [
            {"id": "mp1", "desc": f"Conversion of time to seconds ({t_sec} s)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula Q = I * Delta t", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitution and calculation of Q = {_fmt(charge_c)} C", "marks": 2, "editable": True},
        ],
        {
            "tier_1": "Time must always be in seconds! (1 min = 60 s; 1 hour = 3600 s).",
            "tier_2": f"Time in seconds = {t_sec} s. $Q = I \\times \\Delta t$.",
            "tier_3": f"Q = {_fmt(charge_c)} C.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 17. Electric Circuits: Rate of Electron Flow (Electrons per Second)
# =========================================================================== #
def _build_17_number_of_electrons_passing_cross_section(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    current_ma = r.choice([160, 320, 480, 640, 800])
    current_a = current_ma / 1000.0
    electrons_per_sec = current_a / E_CHARGE
    time_s = r.choice([5, 10, 20])
    total_q = round(current_a * time_s, 3)
    total_electrons = round(electrons_per_sec * time_s)

    prompt = (
        f"A light bulb draws a steady current of **{current_ma}\\text{{ mA}}** (${_fmt(current_a)}\\text{{ A}}$).\n\n"
        f"1. Convert the current from milliamperes (mA) to amperes (A).\n"
        f"2. Calculate the total charge ($Q$) passing through the bulb in **{time_s} seconds**.\n"
        f"3. Calculate the total number of electrons ($n$) passing through the bulb during this time.\n"
        f"4. Determine the rate of electron flow (number of electrons passing per second)."
    )
    ans = (
        f"1. I = {_fmt(current_a)} A; 2. Q = {_fmt(total_q)} C; "
        f"3. n = {total_electrons:.2e} electrons; 4. Rate = {electrons_per_sec:.2e} electrons/second."
    )
    sol = (
        f"1. $I = {current_ma}\\text{{ mA}} \\times 10^{{-3}} = {_fmt(current_a)}\\text{{ A}}$ [1M].\n"
        f"2. $Q = I \\times \\Delta t = ({_fmt(current_a)}\\text{{ A}}) \\times ({time_s}\\text{{ s}}) = {_fmt(total_q)}\\text{{ C}}$ [1M].\n"
        f"3. $n = \\frac{{Q}}{{e}} = \\frac{{{_fmt(total_q)}}}{{1{{,}}6 \\times 10^{{-19}}}} = {total_electrons:.2e}\\text{{ electrons}}$ [1A].\n"
        f"4. Rate $= \\frac{{n}}{{\\Delta t}} = \\frac{{{total_electrons:.2e}}}{{{time_s}}} = {electrons_per_sec:.2e}\\text{{ electrons}}\\cdot\\text{{s}}^{{-1}}$ "
        f"(or directly $\\frac{{I}}{{e}} = \\frac{{{_fmt(current_a)}}}{{1{{,}}6 \\times 10^{{-19}}}}$) [1A]."
    )
    return _make_q(
        r, "17_rate_of_electron_flow_through_conductor", 17, prompt, ans, sol, 4,
        ["milliampere_prefix_error", "confuses_current_with_number_of_electrons"],
        [
            {"id": "mp1", "desc": "Milliampere to Ampere conversion", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Charge calculation Q = {_fmt(total_q)} C", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Total electrons n = {total_electrons:.2e}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Rate of electron flow = {electrons_per_sec:.2e} e/s", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$1\\text{ mA} = 10^{-3}\\text{ A}$. $Q = I \\times \\Delta t$ and $n = Q / e$.",
            "tier_2": f"Total charge = {_fmt(total_q)} C. Divide by $1{{,}}6 \\times 10^{{-19}}$.",
            "tier_3": f"n = {total_electrons:.2e} electrons; rate = {electrons_per_sec:.2e} electrons/s.",
        },
        weight=14, duration=5,
    )


# =========================================================================== #
# 18. Electric Circuits: Ammeter Series Connection & Internal Resistance
# =========================================================================== #
def _build_18_ammeter_series_connection_and_ideal_resistance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([6.0, 9.0, 12.0, 24.0])
    r_load = r.choice([10, 15, 20, 30, 40])
    r_ammeter = r.choice([0.01, 0.02, 0.05])
    i_normal = round(v_batt / r_load, 2)
    i_short = int(v_batt / r_ammeter)

    prompt = (
        f"A laboratory circuit consists of a **${_fmt(v_batt)}\\text{{ V}}$** DC power supply connected across a "
        f"**${r_load}\\ \\Omega$** protective resistor. An ammeter with internal resistance of **${_fmt(r_ammeter)}\\ \\Omega$** is used to measure current.\n\n"
        f"1. State whether an **ammeter** must be connected in series or in parallel with the resistor to measure the current flowing through it.\n"
        f"2. Calculate the normal operating current ($I_{{\\text{{normal}}}}$) when the ammeter is correctly connected in series (ignore ammeter resistance).\n"
        f"3. Explain why an ideal ammeter must have an **extremely low (near zero) internal resistance**.\n"
        f"4. If a learner accidentally connects this ammeter directly across the **${_fmt(v_batt)}\\text{{ V}}$** terminals in parallel, "
        f"calculate the dangerous short-circuit current ($I_{{\\text{{short}}}}$) that surges through the ammeter, and state its physical consequence."
    )
    ans = (
        f"1. Connected in series; "
        f"2. I_normal = {_fmt(i_normal)} A; "
        f"3. So that it introduces negligible resistance into the branch and leaves the measured current unaltered; "
        f"4. I_short = {i_short} A; this massive current creates a short circuit that will blow the fuse, melt meter wiring, or damage the power source."
    )
    sol = (
        f"1. An ammeter must always be connected in **series** so that all charge moving through that branch must also pass through the ammeter [1M].\n"
        f"2. $I_{{\\text{{normal}}}} = \\frac{{V}}{{R}} = \\frac{{{_fmt(v_batt)}}}{{{r_load}}} = {_fmt(i_normal)}\\text{{ A}}$ [1A].\n"
        f"3. An ideal ammeter has **zero internal resistance** so that inserting it into the circuit does not increase total circuit resistance, leaving the measured current unchanged ($I = \\frac{{V}}{{R}}$) [1M].\n"
        f"4. **Accidental parallel connection (short circuit):**\n"
        f"   $I_{{\\text{{short}}}} = \\frac{{V}}{{r_A}} = \\frac{{{_fmt(v_batt)}}}{{{_fmt(r_ammeter)}}} = {i_short}\\text{{ A}}$ [1M].\n"
        f"   This massive current of **{i_short}\\text{{ A}}** will immediately blow the ammeter's internal fuse, burn the galvanometer coil, or overheat the power supply [1A]."
    )
    return _make_q(
        r, "18_ammeter_series_connection_and_ideal_resistance", 18, prompt, ans, sol, 5,
        ["ammeter_in_parallel_fallacy", "believes_ammeter_must_have_high_resistance"],
        [
            {"id": "mp1", "desc": "Ammeter in series statement", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Normal current calculation I = {_fmt(i_normal)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Low internal resistance explanation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Short circuit current calculation I_short = {i_short} A", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Consequence statement (blown fuse / meter damage)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Ammeters measure current flowing THROUGH a path: connect in series with very LOW resistance.",
            "tier_2": f"Normal current: {v_batt} / {r_load} = {_fmt(i_normal)} A. Short-circuit: {v_batt} / {r_ammeter} = {i_short} A.",
            "tier_3": f"1. In series. 2. {_fmt(i_normal)} A. 4. {i_short} A (short circuit blows fuse).",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 19. Electric Circuits: Potential Difference Definition (V = W / Q)
# =========================================================================== #
def _build_19_potential_difference_definition_V_W_Q(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    charge_c = r.choice([2.0, 4.0, 5.0, 8.0, 10.0])
    voltage_v = r.choice([6.0, 9.0, 12.0, 15.0, 24.0])
    work_j = round(voltage_v * charge_c, 1)

    prompt = (
        f"A battery transfers an amount of energy equal to **${_fmt(work_j)}\\text{{ J}}$** to move a charge of "
        f"**${_fmt(charge_c)}\\text{{ C}}$** through a complete electrical circuit.\n\n"
        f"1. Define the term **potential difference**.\n"
        f"2. State the SI unit of potential difference and define it in terms of Joules and Coulombs.\n"
        f"3. Calculate the potential difference ($V$) supplied by the battery."
    )
    ans = (
        f"1. The work done per unit positive charge; "
        f"2. Volt (V), 1 V = 1 J/C (one joule per coulomb); "
        f"3. V = {_fmt(voltage_v)} V."
    )
    sol = (
        f"1. **Potential difference:** The work done per unit positive charge ($V = \\frac{{W}}{{Q}}$) [1M].\n"
        f"2. The SI unit is the **Volt (V)**. One volt is defined as one joule of work done per coulomb of charge ($1\\text{{ V}} = 1\\text{{ J}}\\cdot\\text{{C}}^{{-1}}$) [1M].\n"
        f"3. $V = \\frac{{W}}{{Q}}$ [1M]\n"
        f"   $V = \\frac{{{_fmt(work_j)}\\text{{ J}}}}{{{_fmt(charge_c)}\\text{{ C}}}} = {_fmt(voltage_v)}\\text{{ V}}$ [1A]."
    )
    return _make_q(
        r, "19_potential_difference_definition_V_W_Q", 19, prompt, ans, sol, 4,
        ["confuses_potential_difference_with_current", "formula_inversion_V_W_Q"],
        [
            {"id": "mp1", "desc": "Definition of potential difference", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Unit Volt = Joule / Coulomb", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula V = W / Q", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation V = {_fmt(voltage_v)} V", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$V = \\frac{W}{Q}$. 1 Volt = 1 Joule per Coulomb.",
            "tier_2": f"Divide work ({_fmt(work_j)} J) by charge ({_fmt(charge_c)} C).",
            "tier_3": f"V = {_fmt(voltage_v)} V.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 20. Electric Circuits: Electromotive Force (EMF) in Open Circuit
# =========================================================================== #
def _build_20_electromotive_force_emf_open_circuit(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    emf_val = r.choice([3.0, 6.0, 9.0, 12.0])
    num_cells = int(emf_val / 1.5)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Measuring EMF Across an Open Circuit</text>'
        f'<rect x="150" y="60" width="160" height="70" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(200, 60)">'
        f'<line x1="0" y1="0" x2="20" y2="0"/>'
        f'<line x1="20" y1="-15" x2="20" y2="15" stroke-width="2.5"/>'
        f'<line x1="28" y1="-8" x2="28" y2="8" stroke-width="4"/>'
        f'<line x1="28" y1="0" x2="50" y2="0"/>'
        f'<text x="25" y="-20" text-anchor="middle" font-size="11" fill="#b91c1c">Battery ({_fmt(emf_val)} V)</text>'
        f'</g>'
        f'<g transform="translate(310, 85)">'
        f'<circle cx="0" cy="0" r="3" fill="#334155"/>'
        f'<line x1="0" y1="0" x2="18" y2="-12" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="22" cy="0" r="3" fill="#334155"/>'
        f'<text x="12" y="20" text-anchor="middle" font-size="10" fill="#475569">Switch S (OPEN)</text>'
        f'</g>'
        f'<g transform="translate(230, 130)">'
        f'<line x1="-50" y1="0" x2="-20" y2="0"/>'
        f'<rect x="-20" y="-10" width="40" height="20" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>'
        f'<line x1="20" y1="0" x2="50" y2="0"/>'
        f'<text x="0" y="5" text-anchor="middle" font-size="10">R</text>'
        f'</g>'
        f'<g transform="translate(180, 35)">'
        f'<line x1="0" y1="25" x2="0" y2="0"/>'
        f'<line x1="0" y1="0" x2="100" y2="0"/>'
        f'<line x1="100" y1="0" x2="100" y2="25"/>'
        f'<circle cx="50" cy="0" r="14" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/>'
        f'<text x="50" y="5" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">V</text>'
        f'<text x="50" y="-8" text-anchor="middle" font-size="10" fill="#0284c7">{_fmt(emf_val)} V</text>'
        f'</g>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying circuit diagram, a voltmeter connected across a battery reads **${_fmt(emf_val)}\\text{{ V}}$** "
        f"when the main switch S is **open**.\n\n"
        f"1. Define the term **electromotive force (EMF)**.\n"
        f"2. Explain why the voltmeter reads the full EMF when the switch is open and no current flows through the external circuit.\n"
        f"3. If the battery is constructed from identical $1{{,}}5\\text{{ V}}$ cells in series, calculate the number of cells inside the battery."
    )
    ans = (
        f"1. The maximum amount of electrical energy supplied per unit charge by the source (or work done per unit charge when no current flows); "
        f"2. When the switch is open, current is zero, so there is zero internal voltage drop ('lost volts') inside the battery; "
        f"3. Number of cells = {num_cells}."
    )
    sol = (
        f"1. **EMF (Electromotive force):** The maximum energy supplied per unit charge by the battery (or work done per unit charge to move charge across the full circuit when current is zero) [1M].\n"
        f"2. With the switch open, circuit current is $I = 0\\text{{ A}}$. Because no current flows through the battery's internal resistance, there are no 'lost volts' ($I r = 0$). Hence, terminal voltage equals full EMF [1M].\n"
        f"3. Cells in series add up: $N = \\frac{{V_{{\\text{{total}}}}}}{{V_{{\\text{{cell}}}}}} = \\frac{{{_fmt(emf_val)}}}{{1{{,}}5}} = {num_cells}\\text{{ cells}}$ [2M]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "20_electromotive_force_emf_open_circuit", 20, prompt, ans, sol, 4,
        ["emf_is_a_mechanical_force_misconception", "confuses_emf_with_terminal_voltage"],
        [
            {"id": "mp1", "desc": "Definition of EMF", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explanation of zero current / zero internal voltage drop", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of number of cells = {num_cells}", "marks": 2, "editable": True},
        ],
        {
            "tier_1": "EMF is not a force; it is energy per unit charge (Joules/Coulomb). Measured across open circuit.",
            "tier_2": f"Each cell is $1{{,}}5\\text{{ V}}$. Total EMF is {_fmt(emf_val)} V.",
            "tier_3": f"Number of cells = {_fmt(emf_val)} / 1,5 = {num_cells} cells.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 21. Electric Circuits: Terminal Potential Difference in Closed Circuit
# =========================================================================== #
def _build_21_terminal_potential_difference_closed_circuit(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    emf_val = r.choice([6.0, 9.0, 12.0])
    v_term = round(emf_val - r.choice([0.6, 0.8, 1.0, 1.2]), 1)
    lost_volts = round(emf_val - v_term, 1)

    prompt = (
        f"A voltmeter connected across the terminals of a battery reads **${_fmt(emf_val)}\\text{{ V}}$** when the circuit switch is **open**.\n"
        f"When the switch is **closed**, current begins to flow and the voltmeter reading drops to **${_fmt(v_term)}\\text{{ V}}$**.\n\n"
        f"1. Name the quantity measured by the voltmeter when the switch is open.\n"
        f"2. Name the quantity measured by the voltmeter when the switch is closed.\n"
        f"3. Calculate the potential difference 'lost' inside the battery (the lost volts).\n"
        f"4. Explain why the terminal potential difference decreases when current flows."
    )
    ans = (
        f"1. Electromotive force (EMF); 2. Terminal potential difference; "
        f"3. Lost volts = {_fmt(lost_volts)} V; "
        f"4. The battery has internal resistance; when current flows, work must be done to drive charge through the battery itself, causing an internal voltage drop (lost volts)."
    )
    sol = (
        f"1. Switch open $\\rightarrow$ **Electromotive force (EMF)** [1M].\n"
        f"2. Switch closed $\\rightarrow$ **Terminal potential difference** [1M].\n"
        f"3. $\\text{{Lost volts}} = \\text{{EMF}} - V_{{\\text{{terminal}}}} = {_fmt(emf_val)} - {_fmt(v_term)} = {_fmt(lost_volts)}\\text{{ V}}$ [1M].\n"
        f"4. Inside the battery, the electrolyte and electrodes possess **internal resistance ($r$)**. When charge flows, work ($V_{{\\text{{internal}}}} = I r$) is done overcoming this resistance and converted into heat, reducing the potential available to the external circuit [1A]."
    )
    return _make_q(
        r, "21_terminal_potential_difference_closed_circuit", 21, prompt, ans, sol, 4,
        ["battery_stores_current_misconception", "confuses_emf_with_terminal_potential_difference"],
        [
            {"id": "mp1", "desc": "Naming EMF (open switch)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Naming terminal potential difference (closed switch)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of lost volts = {_fmt(lost_volts)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Explanation of internal resistance causing voltage drop", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Open switch = EMF. Closed switch = Terminal potential difference. Difference = lost volts.",
            "tier_2": f"Lost volts = {_fmt(emf_val)} V - {_fmt(v_term)} V.",
            "tier_3": f"Lost volts = {_fmt(lost_volts)} V due to internal resistance.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 22. Electric Circuits: Voltmeter Parallel Connection & High Resistance
# =========================================================================== #
def _build_22_voltmeter_parallel_connection_and_high_resistance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([6.0, 9.0, 12.0, 24.0])
    r_bulb = r.choice([10, 15, 20, 24, 30])
    r_vm_meg = r.choice([1, 2, 5, 10])  # in Megaohms
    r_vm_ohms = r_vm_meg * 1_000_000
    i_normal = round(v_batt / r_bulb, 2)
    i_series_micro = round((v_batt / (r_bulb + r_vm_ohms)) * 1_000_000, 2)

    prompt = (
        f"A laboratory circuit consists of a **${_fmt(v_batt)}\\text{{ V}}$** battery powering a **${r_bulb}\\ \\Omega$** light bulb. "
        f"A digital voltmeter with an internal resistance of **${r_vm_meg}\\text{{ M}}\\Omega$** (${r_vm_meg} \\times 10^6\\ \\Omega$) is available.\n\n"
        f"1. State whether a **voltmeter** must be connected in series or in parallel across the light bulb to measure the potential difference across it.\n"
        f"2. Calculate the normal operating current ($I_{{\\text{{normal}}}}$) through the bulb when connected directly to the battery.\n"
        f"3. Explain why an ideal voltmeter must have an **infinitely high internal resistance**.\n"
        f"4. If a learner mistakenly connects this voltmeter in series with the light bulb, "
        f"calculate the minute current ($I_{{\\text{{series}}}}$) in microamperes ($\\mu\\text{{A}}$) that trickles through the circuit, and state whether the bulb will glow."
    )
    ans = (
        f"1. Connected in parallel; "
        f"2. I_normal = {_fmt(i_normal)} A; "
        f"3. So that it draws virtually zero current from the circuit component, leaving circuit operation unaltered; "
        f"4. I_series = {_fmt(i_series_micro)} \\mu A; the light bulb will not glow at all because the current is negligible."
    )
    sol = (
        f"1. A voltmeter must always be connected in **parallel** across the two points between which the potential difference is to be measured [1M].\n"
        f"2. $I_{{\\text{{normal}}}} = \\frac{{V}}{{R}} = \\frac{{{_fmt(v_batt)}}}{{{r_bulb}}} = {_fmt(i_normal)}\\text{{ A}}$ [1A].\n"
        f"3. An ideal voltmeter has **infinitely high resistance** ($R_v \\approx \\infty$) so that negligible current is diverted away from the component being measured, preserving the original current and voltage conditions ($I = \\frac{{V}}{{R_v}} \\approx 0$) [1M].\n"
        f"4. **Accidental series connection:**\n"
        f"   $R_{{\\text{{total}}}} = R_{{\\text{{bulb}}}} + R_v = {r_bulb} + {r_vm_ohms:,}\\ \\Omega \\approx {r_vm_ohms:,}\\ \\Omega$ [1M].\n"
        f"   $I_{{\\text{{series}}}} = \\frac{{{_fmt(v_batt)}}}{{{r_bulb + r_vm_ohms}}} = {_fmt(i_series_micro)} \\times 10^{{-6}}\\text{{ A}} = {_fmt(i_series_micro)}\\ \\mu\\text{{A}}$ [1M].\n"
        f"   Because this current is negligible, the **light bulb will not glow at all** [1A]."
    )
    return _make_q(
        r, "22_voltmeter_parallel_connection_and_high_resistance", 22, prompt, ans, sol, 6,
        ["voltmeter_in_series_fallacy", "confuses_voltmeter_resistance_with_ammeter_resistance"],
        [
            {"id": "mp1", "desc": "Voltmeter in parallel statement", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Normal current calculation I = {_fmt(i_normal)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "High resistance justification (draws no current)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Total resistance formula with series voltmeter", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Series current calculation I = {_fmt(i_series_micro)} muA", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Deduction that light bulb will not glow", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Voltmeters measure voltage ACROSS two points: connect in PARALLEL with very HIGH resistance.",
            "tier_2": f"Normal: {v_batt} / {r_bulb} = {_fmt(i_normal)} A. In series: {v_batt} / ({r_vm_meg} x 10^6) = {_fmt(i_series_micro)} uA.",
            "tier_3": f"1. In parallel. 2. {_fmt(i_normal)} A. 4. {_fmt(i_series_micro)} muA (bulb will not glow).",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 23. Electric Circuits: Work Done by Charge in Component (W = V * Q)
# =========================================================================== #
def _build_23_work_done_moving_charge_through_component(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_drop = r.choice([3.0, 4.5, 6.0, 9.0, 12.0])
    current_a = r.choice([0.5, 1.0, 1.5, 2.0])
    time_s = r.choice([10, 20, 30, 60])
    charge_c = round(current_a * time_s, 2)
    work_j = round(v_drop * charge_c, 1)

    prompt = (
        f"A filament lamp operates with a potential difference of **${_fmt(v_drop)}\\text{{ V}}$** across its terminals, "
        f"carrying a steady current of **${_fmt(current_a)}\\text{{ A}}$** for a time of **{time_s} seconds**.\n\n"
        f"1. Calculate the total charge ($Q$) passing through the lamp during this time.\n"
        f"2. State the formula relating work done ($W$), potential difference ($V$), and charge ($Q$).\n"
        f"3. Calculate the total electrical work done (energy dissipated) by the lamp in this time.\n"
        f"4. Name the two main forms of energy into which electrical energy is transformed in the lamp."
    )
    ans = (
        f"1. Q = {_fmt(charge_c)} C; 2. W = V * Q; 3. W = {_fmt(work_j)} J; 4. Heat (thermal) energy and light (radiant) energy."
    )
    sol = (
        f"1. $Q = I \\times \\Delta t = ({_fmt(current_a)}\\text{{ A}}) \\times ({time_s}\\text{{ s}}) = {_fmt(charge_c)}\\text{{ C}}$ [1M].\n"
        f"2. $V = \\frac{{W}}{{Q}} \\implies W = V \\times Q$ [1M].\n"
        f"3. $W = ({_fmt(v_drop)}\\text{{ V}}) \\times ({_fmt(charge_c)}\\text{{ C}}) = {_fmt(work_j)}\\text{{ J}}$ [1A].\n"
        f"4. Electrical energy is converted into **heat energy** (due to electron collisions in the tungsten filament) and **light energy** (incandescence) [1M]."
    )
    return _make_q(
        r, "23_work_done_moving_charge_through_component", 23, prompt, ans, sol, 4,
        ["energy_destroyed_misconception", "formula_algebraic_error"],
        [
            {"id": "mp1", "desc": f"Charge calculation Q = {_fmt(charge_c)} C", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula W = V * Q", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of work done W = {_fmt(work_j)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Forms of energy: heat and light", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$Q = I \\times \\Delta t$, then $W = V \\times Q$. Work is in Joules.",
            "tier_2": f"Charge = {_fmt(charge_c)} C. Work = {_fmt(v_drop)} V * {_fmt(charge_c)} C.",
            "tier_3": f"W = {_fmt(work_j)} J. Energy forms: heat and light.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 24. Electric Circuits: Cells in Series (Aiding and Opposing)
# =========================================================================== #
def _build_24_cells_in_series_aiding_and_opposing(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_aiding = r.choice([3, 4])
    n_opposing = 1
    cell_v = 1.5
    v_aiding = round(n_aiding * cell_v, 2)
    v_opposing = round((n_aiding - n_opposing) * cell_v, 2)

    prompt = (
        f"A learner constructs a battery using **{n_aiding + n_opposing} identical cells**, each having an EMF of **$1{{,}}5\\text{{ V}}$**.\n\n"
        f"**Case 1:** All {n_aiding + n_opposing} cells are connected in series with their positive terminals connected to negative terminals (series aiding).\n"
        f"**Case 2:** {n_aiding} cells are connected aiding, but **{n_opposing} cell** is accidentally reversed in orientation (series opposing).\n\n"
        f"1. Calculate the total EMF of the battery in **Case 1**.\n"
        f"2. Calculate the total EMF of the battery in **Case 2**.\n"
        f"3. Explain why the reversed cell reduces the total EMF of the battery.\n"
        f"4. State the main advantage of connecting cells in series aiding rather than using a single cell."
    )
    ans = (
        f"1. Case 1 EMF = {_fmt((n_aiding + n_opposing) * cell_v)} V; 2. Case 2 EMF = {_fmt(v_opposing)} V; "
        f"3. The reversed cell pushes charge in the opposite direction, cancelling out the EMF of one of the aiding cells; "
        f"4. Higher total potential difference (EMF) to drive greater current through external resistors."
    )
    sol = (
        f"1. **Case 1 (All aiding):** $V_{{\\text{{total}}}} = V_1 + V_2 + \\dots = ({n_aiding + n_opposing}) \\times 1{{,}}5\\text{{ V}} = {_fmt((n_aiding + n_opposing) * cell_v)}\\text{{ V}}$ [1M].\n"
        f"2. **Case 2 (One reversed):** $V_{{\\text{{total}}}} = ({n_aiding} \\times 1{{,}}5) - ({n_opposing} \\times 1{{,}}5) = {_fmt(n_aiding * cell_v)} - 1{{,}}5 = {_fmt(v_opposing)}\\text{{ V}}$ [1M].\n"
        f"3. The opposing cell sets up a counter-electromotive force, driving charge in reverse and subtracting from the forward EMF [1M].\n"
        f"4. Advantage: Series aiding provides a **higher total potential difference (voltage)** to power higher-voltage components [1A]."
    )
    return _make_q(
        r, "24_cells_in_series_aiding_and_opposing", 24, prompt, ans, sol, 4,
        ["ignoring_cell_polarity_misconception", "cells_in_series_summation_error"],
        [
            {"id": "mp1", "desc": f"Case 1 total EMF = {_fmt((n_aiding + n_opposing) * cell_v)} V", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Case 2 total EMF = {_fmt(v_opposing)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Explanation of counter-EMF from reversed cell", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Advantage of series aiding (increased total voltage)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Aiding cells add ($V_1 + V_2$). A reversed cell subtracts its EMF.",
            "tier_2": f"Case 1: {n_aiding + n_opposing} * 1,5 V. Case 2: ({n_aiding} - {n_opposing}) * 1,5 V.",
            "tier_3": f"Case 1: {_fmt((n_aiding + n_opposing) * cell_v)} V; Case 2: {_fmt(v_opposing)} V.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 25. Electric Circuits: Cells in Parallel Characteristics
# =========================================================================== #
def _build_25_cells_in_parallel_identical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_cells = r.choice([2, 3, 4])
    cell_emf = r.choice([1.5, 3.0, 6.0])

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">'
        f'{n_cells} Identical Cells Connected in Parallel ({_fmt(cell_emf)} V each)</text>'
        f'<g transform="translate(180, 50)">'
        f'<line x1="0" y1="0" x2="30" y2="0"/><line x1="30" y1="-10" x2="30" y2="10" stroke-width="2.5"/><line x1="38" y1="-6" x2="38" y2="6" stroke-width="4"/><line x1="38" y1="0" x2="70" y2="0"/>'
        f'<text x="35" y="-14" text-anchor="middle" font-size="9" fill="#0284c7">Cell 1 ({_fmt(cell_emf)} V)</text>'
        f'</g>'
        f'<g transform="translate(180, 85)">'
        f'<line x1="0" y1="0" x2="30" y2="0"/><line x1="30" y1="-10" x2="30" y2="10" stroke-width="2.5"/><line x1="38" y1="-6" x2="38" y2="6" stroke-width="4"/><line x1="38" y1="0" x2="70" y2="0"/>'
        f'<text x="35" y="-14" text-anchor="middle" font-size="9" fill="#0284c7">Cell 2 ({_fmt(cell_emf)} V)</text>'
        f'</g>'
        + (
            f'<g transform="translate(180, 120)">'
            f'<line x1="0" y1="0" x2="30" y2="0"/><line x1="30" y1="-10" x2="30" y2="10" stroke-width="2.5"/><line x1="38" y1="-6" x2="38" y2="6" stroke-width="4"/><line x1="38" y1="0" x2="70" y2="0"/>'
            f'<text x="35" y="-14" text-anchor="middle" font-size="9" fill="#0284c7">Cell 3 ({_fmt(cell_emf)} V)</text>'
            f'</g>' if n_cells >= 3 else ''
        )
        + f'<line x1="180" y1="50" x2="180" y2="{"120" if n_cells >= 3 else "85"}" stroke="#334155" stroke-width="2"/>'
        f'<line x1="250" y1="50" x2="250" y2="{"120" if n_cells >= 3 else "85"}" stroke="#334155" stroke-width="2"/>'
        f'<line x1="130" y1="65" x2="180" y2="65" stroke="#334155" stroke-width="2"/>'
        f'<line x1="250" y1="65" x2="300" y2="65" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="130" cy="65" r="3" fill="#334155"/><circle cx="300" cy="65" r="3" fill="#334155"/>'
        f'</svg>'
    )
    prompt = (
        f"In the accompanying circuit diagram, **{n_cells} identical cells**, each having an EMF of **${_fmt(cell_emf)}\\text{{ V}}$**, "
        f"are connected in parallel with one another.\n\n"
        f"1. State the total EMF supplied by this parallel battery combination.\n"
        f"2. Explain why connecting identical cells in parallel does not increase the total potential difference.\n"
        f"3. State two distinct practical advantages of connecting cells in parallel rather than in series.\n"
        f"4. If a torch draws $0{{,}}6\\text{{ A}}$ from this parallel battery, determine the current supplied by each individual cell."
    )
    current_per_cell = round(0.6 / n_cells, 3)
    ans = (
        f"1. Total EMF = {_fmt(cell_emf)} V; "
        f"2. Parallel branches share the same potential difference; adding identical parallel paths does not add voltages; "
        f"3. The battery lasts longer (increased capacity/lifetime) and each cell supplies only a fraction of the total current (lower internal heat/resistance); "
        f"4. Each cell supplies {_fmt(current_per_cell)} A."
    )
    sol = (
        f"1. For identical cells in parallel: $V_{{\\text{{total}}}} = V_{{\\text{{single cell}}}} = {_fmt(cell_emf)}\\text{{ V}}$ [1M].\n"
        f"2. Points connected in parallel are at identical electrical potentials; each cell delivers energy to separate parallel streams of charge without cascading potential steps [1M].\n"
        f"3. Advantages [1M]:\n"
        f"   - **Longer lifespan / capacity:** The battery operates for {n_cells} times longer.\n"
        f"   - **Lower effective internal resistance:** Reduces internal energy dissipation ($r_p = r / {n_cells}$).\n"
        f"4. Current splits equally: $I_{{\\text{{cell}}}} = \\frac{{I_{{\\text{{total}}}}}}{{{n_cells}}} = \\frac{{0{{,}}6\\text{{ A}}}}{{{n_cells}}} = {_fmt(current_per_cell)}\\text{{ A}}$ [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "25_cells_in_parallel_identical", 25, prompt, ans, sol, 4,
        ["adding_voltages_in_parallel_fallacy", "current_sharing_misunderstanding"],
        [
            {"id": "mp1", "desc": f"Total EMF = {_fmt(cell_emf)} V", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reason why parallel cells do not increase voltage", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Two advantages (longer lifetime, lower internal resistance)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Current per cell calculation = {_fmt(current_per_cell)} A", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Identical cells in parallel have the SAME voltage as one single cell!",
            "tier_2": f"Total EMF is {_fmt(cell_emf)} V. Total current divides equally among the {n_cells} branches.",
            "tier_3": f"Total EMF = {_fmt(cell_emf)} V. Current per cell = 0,6 / {n_cells} = {_fmt(current_per_cell)} A.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# Export Dictionary for Subskills 01 to 25
# =========================================================================== #
BUILDERS_01_25: Dict[str, Any] = {
    "01_magnetic_poles_attraction_repulsion": _build_01_magnetic_poles_attraction_repulsion,
    "02_magnetic_field_lines_and_direction": _build_02_magnetic_field_lines_and_direction,
    "03_earth_magnetic_field_and_compass": _build_03_earth_magnetic_field_and_compass,
    "04_ferromagnetic_materials_and_magnetic_domains": _build_04_ferromagnetic_materials_and_domains,
    "05_magnetic_field_patterns_two_bar_magnets": _build_05_magnetic_field_patterns_two_bar_magnets,
    "06_triboelectric_charging_by_friction": _build_06_triboelectric_charging_by_friction,
    "07_electrostatic_force_and_polarization_neutral_object": _build_07_electrostatic_force_and_polarization_neutral_object,
    "08_charge_conservation_two_identical_spheres": _build_08_charge_conservation_two_identical_spheres,
    "09_charge_conservation_three_spheres_successive_contact": _build_09_charge_conservation_three_spheres_successive_contact,
    "10_charge_quantization_number_of_electrons": _build_10_charge_quantization_number_of_electrons,
    "11_charge_quantization_charge_validity_test": _build_11_charge_quantization_charge_validity_test,
    "12_electron_transfer_direction_and_mass_change": _build_12_electron_transfer_direction_and_mass_change,
    "13_circuit_components_and_symbols_identification": _build_13_circuit_components_and_symbols_identification,
    "14_conventional_current_vs_electron_drift": _build_14_conventional_current_vs_electron_drift,
    "15_electric_current_definition_I_Q_t": _build_15_electric_current_definition_I_Q_t,
    "16_electric_current_time_conversion_minutes_hours": _build_16_electric_current_time_conversion_minutes_hours,
    "17_rate_of_electron_flow_through_conductor": _build_17_number_of_electrons_passing_cross_section,
    "18_ammeter_series_connection_and_ideal_resistance": _build_18_ammeter_series_connection_and_ideal_resistance,
    "19_potential_difference_definition_V_W_Q": _build_19_potential_difference_definition_V_W_Q,
    "20_electromotive_force_emf_open_circuit": _build_20_electromotive_force_emf_open_circuit,
    "21_terminal_potential_difference_closed_circuit": _build_21_terminal_potential_difference_closed_circuit,
    "22_voltmeter_parallel_connection_and_high_resistance": _build_22_voltmeter_parallel_connection_and_high_resistance,
    "23_work_done_by_charge_in_circuit_component": _build_23_work_done_moving_charge_through_component,
    "24_cells_in_series_aiding_and_opposing": _build_24_cells_in_series_aiding_and_opposing,
    "25_cells_in_parallel_characteristics": _build_25_cells_in_parallel_identical,
}
