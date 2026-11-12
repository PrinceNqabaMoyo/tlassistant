"""Grade 9 Natural Sciences - Energy and the National Electricity Grid: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Energy and the national electricity grid.md.
Focus: Coal power stations, pulverisation, steam turbines, cooling towers, coal formation & SA geography,
environmental impacts, alternative & renewable sources, hydroelectric dams & classroom turbine activity,
pumped storage hydro ("water battery"), Faraday's law & electromagnetic induction, Faraday disk, portable generators,
bicycle dynamos, wind, solar PV vs sun-heated steam, tidal/biofuels, intermittency, and Sankey efficiency.
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


def _svg_coal_station_flow(rng: random.Random, masked_idx: int, mw: int) -> Dict[str, Any]:
    """Parameterized schematic of a coal-fired thermal power station with one masked stage."""
    stages = ["Coal Supply", "Pulveriser", "Furnace & Boiler", "Steam Turbine", "Generator", "Grid Lines"]
    colors = ["#475569", "#64748b", "#ea580c", "#0284c7", "#16a34a", "#7c3aed"]
    boxes = []
    for i, label in enumerate(stages):
        x = 18 + i * 68
        shown = "Stage X" if i == masked_idx else label
        fill = "#fef08a" if i == masked_idx else "#f8fafc"
        stroke = "#ca8a04" if i == masked_idx else colors[i]
        short = shown.replace(" & ", "/").replace(" Supply", "").replace(" Lines", "")
        boxes.append(
            f'<rect x="{x}" y="76" width="56" height="44" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            f'<text x="{x + 28}" y="102" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{short}</text>'
        )
        if i < len(stages) - 1:
            boxes.append(
                f'<line x1="{x + 56}" y1="98" x2="{x + 68}" y2="98" stroke="#334155" stroke-width="2"/>'
                f'<polygon points="{x + 68},98 {x + 62},94 {x + 62},102" fill="#334155"/>'
            )
    svg = (
        f'<svg viewBox="0 0 435 170" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="170" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="26" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Thermal Coal Power Station Process ({mw} MW)</text>'
        f'{"".join(boxes)}'
        f'<text x="217" y="148" font-size="10" fill="#475569" text-anchor="middle">Identify Stage X and its physical role</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_hydro_station(rng: random.Random, dam_name: str, head_m: int) -> Dict[str, Any]:
    """Parameterized hydroelectric dam and powerhouse cross-section."""
    y_water = 48 + rng.randint(-4, 4)
    svg = (
        f'<svg viewBox="0 0 435 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{dam_name} Hydroelectric Station (Head = {head_m} m)</text>'
        f'<rect x="20" y="{y_water}" width="135" height="{175 - y_water}" fill="#bae6fd" stroke="#0284c7"/>'
        f'<text x="86" y="{y_water + 25}" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">Dam Reservoir (A)</text>'
        f'<polygon points="155,{y_water - 8} 185,{y_water - 8} 205,175 155,175" fill="#94a3b8" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 155 120 L 235 155" stroke="#0284c7" stroke-width="10" fill="none"/>'
        f'<text x="195" y="128" font-size="9.5" font-weight="bold" fill="#0f172a">Penstock (B)</text>'
        f'<rect x="230" y="102" width="110" height="72" rx="4" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="256" cy="148" r="14" fill="#38bdf8" stroke="#0369a1" stroke-width="2"/>'
        f'<text x="256" y="152" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">C</text>'
        f'<rect x="290" y="114" width="38" height="26" fill="#fde047" stroke="#ca8a04" stroke-width="1.8"/>'
        f'<text x="309" y="131" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">D</text>'
        f'<line x1="256" y1="134" x2="290" y2="127" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="340" y="160" width="80" height="16" fill="#bae6fd"/>'
        f'<text x="380" y="192" font-size="9.5" fill="#334155" text-anchor="middle">River Outflow</text>'
        f'<polyline points="328,118 370,68 415,68" fill="none" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="382" y="58" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Power Lines</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_foil_turbine_activity(rng: random.Random, mass_g: int, lift_cm: int) -> Dict[str, Any]:
    """Parameterized classroom foil water wheel and lifting mass setup."""
    dx = rng.randint(-5, 5)
    svg = (
        f'<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Classroom Water Turbine Apparatus</text>'
        f'<path d="M 110 34 L 110 56 L 138 56" stroke="#475569" stroke-width="6" fill="none"/>'
        f'<line x1="138" y1="58" x2="138" y2="105" stroke="#0ea5e9" stroke-width="5" stroke-dasharray="6,3"/>'
        f'<text x="88" y="48" font-size="9.5" font-weight="bold" fill="#0369a1" text-anchor="end">Running Tap</text>'
        f'<circle cx="{150 + dx}" cy="122" r="28" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>'
        f'<line x1="{122 + dx}" y1="122" x2="{178 + dx}" y2="122" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{150 + dx}" y1="94" x2="{150 + dx}" y2="150" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{150 + dx}" y1="122" x2="295" y2="122" stroke="#d97706" stroke-width="6"/>'
        f'<text x="225" y="110" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">Pencil Axle</text>'
        f'<line x1="278" y1="125" x2="278" y2="165" stroke="#334155" stroke-width="2"/>'
        f'<rect x="266" y="165" width="24" height="20" rx="3" fill="#64748b" stroke="#0f172a"/>'
        f'<text x="278" y="179" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">{mass_g} g</text>'
        f'<text x="348" y="170" font-size="9.5" font-weight="bold" fill="#16a34a" text-anchor="middle">Lifted {lift_cm} cm</text>'
        f'<line x1="310" y1="185" x2="310" y2="140" stroke="#16a34a" stroke-width="2"/>'
        f'<polygon points="310,140 306,148 314,148" fill="#16a34a"/>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_pumped_storage(rng: random.Random, scheme: str, is_peak: bool, mw: int) -> Dict[str, Any]:
    """Parameterized pumped storage hydroelectric scheme showing peak generation vs off-peak pumping."""
    mode_lbl = "PEAK DEMAND (Generating)" if is_peak else "OFF-PEAK NIGHT (Pumping)"
    arrow_pts = "205,130 198,120 208,118" if is_peak else "148,88 156,95 147,99"
    col = "#16a34a" if is_peak else "#2563eb"
    svg = (
        f'<svg viewBox="0 0 435 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{scheme}: {mode_lbl} ({mw} MW)</text>'
        f'<rect x="35" y="45" width="115" height="40" rx="4" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="92" y="69" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">Upper Mountain Dam</text>'
        f'<line x1="138" y1="85" x2="245" y2="152" stroke="{col}" stroke-width="7"/>'
        f'<polygon points="{arrow_pts}" fill="{col}"/>'
        f'<rect x="240" y="145" width="145" height="40" rx="4" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="312" y="169" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Lower Valley Dam</text>'
        f'<circle cx="195" cy="121" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="195" y="125" font-size="8.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Turb/Pump</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_generator_coil_magnet(rng: random.Random, rpm: int, v_out: int) -> Dict[str, Any]:
    """Parameterized AC generator schematic with rotating magnet inside stationary coils."""
    tilt = rng.randint(-4, 4)
    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Electromagnetic Generator ({rpm} rpm | {v_out} V)</text>'
        f'<rect x="95" y="55" width="38" height="82" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>'
        f'<rect x="285" y="55" width="38" height="82" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>'
        f'<text x="114" y="152" font-size="9.5" font-weight="bold" fill="#b45309" text-anchor="middle">Copper Coil</text>'
        f'<text x="304" y="152" font-size="9.5" font-weight="bold" fill="#b45309" text-anchor="middle">Copper Coil</text>'
        f'<rect x="160" y="{82 + tilt}" width="50" height="28" fill="#dc2626" stroke="#0f172a" stroke-width="1.8"/>'
        f'<rect x="210" y="{82 + tilt}" width="50" height="28" fill="#2563eb" stroke="#0f172a" stroke-width="1.8"/>'
        f'<text x="185" y="{100 + tilt}" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">N</text>'
        f'<text x="235" y="{100 + tilt}" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">S</text>'
        f'<path d="M 192 68 A 28 28 0 0 1 228 68" fill="none" stroke="#16a34a" stroke-width="2.5"/>'
        f'<polygon points="228,68 220,64 222,73" fill="#16a34a"/>'
        f'<text x="210" y="176" font-size="9.5" fill="#334155" text-anchor="middle">Turbine shaft rotates magnet inside stationary coils</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_bicycle_dynamo(rng: random.Random, speed_kmh: int) -> Dict[str, Any]:
    """Parameterized bicycle wheel driving a bottle dynamo and headlamp."""
    r_wheel = 54 + rng.randint(-3, 3)
    svg = (
        f'<svg viewBox="0 0 430 195" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="195" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Bicycle Wheel &amp; Dynamo System ({speed_kmh} km/h)</text>'
        f'<circle cx="135" cy="115" r="{r_wheel}" fill="none" stroke="#334155" stroke-width="6"/>'
        f'<circle cx="135" cy="115" r="6" fill="#0f172a"/>'
        f'<rect x="200" y="92" width="16" height="24" rx="2" fill="#64748b" stroke="#0f172a"/>'
        f'<rect x="216" y="84" width="54" height="40" rx="5" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="243" y="108" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Dynamo</text>'
        f'<polyline points="270,104 335,104 335,76" fill="none" stroke="#dc2626" stroke-width="2"/>'
        f'<circle cx="335" cy="64" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="335" y="68" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">Lamp</text>'
        f'<text x="215" y="182" font-size="9.5" fill="#475569" text-anchor="middle">Rotating tyre turns knurled roller -&gt; magnet spins inside wire coil</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_intermittency_curve(rng: random.Random, solar_peak_mw: int, eve_demand_mw: int) -> Dict[str, Any]:
    """Parameterized 24-hour Solar PV supply vs Evening Peak demand curve."""
    y_peak_s = 165 - int((solar_peak_mw / 45000.0) * 110)
    y_eve_d = 165 - int((eve_demand_mw / 45000.0) * 110)
    svg = (
        f'<svg viewBox="0 0 435 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Daily Solar Supply vs Grid Demand ({eve_demand_mw} MW Peak)</text>'
        f'<line x1="55" y1="35" x2="55" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="55" y1="165" x2="405" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<path d="M 70 165 L 145 165 Q 210 {y_peak_s} 275 165 L 390 165" fill="none" stroke="#eab308" stroke-width="3"/>'
        f'<path d="M 70 120 L 140 105 L 220 112 L 315 {y_eve_d} L 390 125" fill="none" stroke="#dc2626" stroke-width="3"/>'
        f'<text x="210" y="{y_peak_s + 14}" font-size="9.5" font-weight="bold" fill="#a16207" text-anchor="middle">Solar ({solar_peak_mw} MW)</text>'
        f'<text x="315" y="{y_eve_d - 8}" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">19:00 Peak ({eve_demand_mw} MW)</text>'
        f'<text x="145" y="182" font-size="9" fill="#334155" text-anchor="middle">06:00</text>'
        f'<text x="210" y="182" font-size="9" fill="#334155" text-anchor="middle">12:00</text>'
        f'<text x="315" y="182" font-size="9" fill="#334155" text-anchor="middle">19:00</text>'
        f'<text x="230" y="198" font-size="10" fill="#0f172a" text-anchor="middle">Time of Day (Hours)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_footprint_bars(rng: random.Random, coal_co2: int, wind_co2: int, mwh: int) -> Dict[str, Any]:
    """Parameterized bar graph comparing CO2 intensity per MWh across Coal and Wind."""
    h_coal = 110
    h_wind = max(6, int((wind_co2 / float(coal_co2)) * 110))
    svg = (
        f'<svg viewBox="0 0 420 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">CO2 Emissions per MWh ({mwh} MWh Generation Target)</text>'
        f'<line x1="60" y1="35" x2="60" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="165" x2="380" y2="165" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="115" y="{165 - h_coal}" width="65" height="{h_coal}" fill="#64748b" stroke="#0f172a"/>'
        f'<text x="147" y="{158 - h_coal}" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{coal_co2} kg/MWh</text>'
        f'<text x="147" y="184" font-size="10.5" fill="#0f172a" text-anchor="middle">Coal</text>'
        f'<rect x="245" y="{165 - h_wind}" width="65" height="{h_wind}" fill="#22c55e" stroke="#0f172a"/>'
        f'<text x="277" y="{154 - h_wind}" font-size="10.5" font-weight="bold" fill="#15803d" text-anchor="middle">{wind_co2} kg/MWh</text>'
        f'<text x="277" y="184" font-size="10.5" fill="#0f172a" text-anchor="middle">Wind</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_station_sankey(rng: random.Random, e_in: int, e_elec: int, station: str) -> Dict[str, Any]:
    """Parameterized Sankey energy flow diagram for thermal power station efficiency."""
    e_heat = e_in - e_elec
    h_e = max(18, int(92 * (e_elec / float(e_in))))
    h_h = max(18, 92 - h_e)
    svg = (
        f'<svg viewBox="0 0 435 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="435" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="217" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{station} Sankey Energy Flow</text>'
        f'<rect x="30" y="60" width="145" height="92" fill="#93c5fd" stroke="#1d4ed8"/>'
        f'<text x="102" y="106" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Coal Input: {e_in} MJ</text>'
        f'<rect x="175" y="60" width="215" height="{h_e}" fill="#4ade80" stroke="#15803d"/>'
        f'<text x="282" y="{60 + h_e // 2 + 4}" font-size="10.5" font-weight="bold" fill="#14532d" text-anchor="middle">Electrical Output: {e_elec} MJ</text>'
        f'<rect x="175" y="{60 + h_e + 6}" width="215" height="{h_h}" fill="#fca5a5" stroke="#dc2626"/>'
        f'<text x="282" y="{60 + h_e + 6 + h_h // 2 + 4}" font-size="10.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">Wasted Heat: {e_heat} MJ</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_coal_power_station_pulverisation_to_steam_sequence(rng: random.Random) -> Dict[str, Any]:
    masked_idx = rng.choice([1, 2, 3, 4])
    mw = rng.choice([450, 600, 720, 800])
    stage_details = {
        1: ("Pulveriser", "crushes large coal chunks into fine powder so it burns rapidly and completely in the furnace"),
        2: ("Furnace & Boiler", "burns the coal dust to release thermal energy that boils water into high-pressure steam"),
        3: ("Steam Turbine", "captures kinetic energy from expanding steam jets to spin its angled rotor blades"),
        4: ("Generator", "uses the rotating turbine shaft to spin magnets inside wire coils, inducing electric current"),
    }
    name, role = stage_details[masked_idx]
    spec = _svg_coal_station_flow(rng, masked_idx, mw)
    prompt = (
        f"Examine the process schematic of a **{mw} MW** coal-fired thermal power station.\n\n"
        "1. Name the component represented by **Stage X** [1].\n"
        "2. Describe the physical function of **Stage X** inside the power station [2]."
    )
    correct = f"{name}; {role.capitalize()}"
    sol = (
        f"**Step 1:** Looking at the sequence Coal -> Pulveriser -> Furnace & Boiler -> Steam Turbine -> Generator -> Grid Lines, **Stage X** is the **{name}** [1].\n\n"
        f"**Step 2:** It {role} [2]."
    )
    return _q(
        rng, "01", "01_coal_power_station_pulverisation_to_steam_sequence", prompt, correct, sol, 3, "short_answer",
        ["reversing_turbine_and_generator_order"],
        "Trace the step immediately before and after Stage X in the flow.",
        f"{name}: {role}.",
        correct, diagram_spec=spec,
    )


def arch_02_coal_station_complete_energy_transformation_chain(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Arnot", "Camden", "Duvha", "Lethabo", "Matimba"])
    prompt = (
        f"At **{station} Power Station**, pulverised coal is burned to boil water, producing high-pressure steam that spins a turbine connected to an electrical generator.\n\n"
        "Which energy conversion sequence correctly tracks energy from raw coal to the transmission grid?"
    )
    correct = "Chemical potential energy -> Thermal (heat) energy -> Mechanical kinetic energy -> Electrical energy"
    distractors = [
        "Electrical energy -> Chemical potential energy -> Nuclear energy -> Thermal energy",
        "Gravitational potential energy -> Light energy -> Sound energy -> Electrical energy",
        "Thermal energy -> Chemical energy -> Elastic potential energy -> Electrical energy",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Coal stores **chemical potential energy**, released as **thermal (heat) energy** during furnace combustion.\n"
        f"**Step 2:** Steam drives turbine blades (**mechanical kinetic energy**), which turn the generator to produce **electrical energy** at {station} [2]."
    )
    return _q(
        rng, "02", "02_coal_station_complete_energy_transformation_chain", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_coal_converts_directly_to_electricity_without_heat"],
        "Identify the energy stored in coal, released in the fire, turning the turbine, and leaving in the wires.",
        "Chemical -> Thermal -> Kinetic (mechanical) -> Electrical.",
        correct, options=options,
    )


def arch_03_pulverised_coal_surface_area_combustion_efficiency(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Arnot", "Duvha", "Lethabo", "Matimba"])
    temp_c = rng.choice([1250, 1350, 1450])
    prompt = (
        f"Before entering the **{temp_c} °C** furnace at **{station} Power Station**, large mined coal lumps pass through a crushing mill called a **pulveriser**.\n\n"
        "1. Explain what happens to coal inside the pulveriser [1].\n"
        "2. Explain scientifically why crushing coal into a fine powder improves furnace combustion [2]."
    )
    correct = "Coal lumps are crushed into fine powder; Increasing total exposed surface area speeds up reaction with oxygen so combustion is faster, hotter, and more complete"
    sol = (
        "**Step 1:** The **pulveriser** grinds large solid coal rocks into a fine dust/powder [1].\n\n"
        "**Step 2:** Powdering vastly increases **exposed surface area** in contact with furnace oxygen, producing faster, cleaner, and more complete combustion [2]."
    )
    return _q(
        rng, "03", "03_pulverised_coal_surface_area_combustion_efficiency", prompt, correct, sol, 3, "short_answer",
        ["thinking_pulverisation_changes_chemical_composition_of_coal"],
        "Think about why sawdust burns much faster than a solid wooden log.",
        "Crushed to fine powder -> larger surface area -> faster complete burning.",
        correct,
    )


def arch_04_steam_turbine_prime_mover_mechanical_rotation(rng: random.Random) -> Dict[str, Any]:
    rpm = rng.choice([3000, 1500])
    pressure_mpa = rng.choice([16.5, 18.0, 21.0])
    prompt = (
        f"Superheated steam at **{_fmt_num(pressure_mpa)} MPa** strikes the angled rotor blades of a turbine, spinning the central drive shaft at **{rpm} revolutions per minute**.\n\n"
        "Explain the physical role of the **steam turbine** and identify the energy transfer that occurs across its blades [2]."
    )
    correct = "The turbine acts as a mechanical prime mover; high-speed expanding steam transfers kinetic energy to the angled blades, rotating the shaft coupled to the generator"
    sol = (
        f"**Step 1:** Fast-moving steam pushes against angled turbine blades, converting **thermal/kinetic energy of steam** into **rotational kinetic energy** [1].\n\n"
        f"**Step 2:** Because the turbine shaft is coupled directly to the generator rotor at {rpm} rpm, it mechanically drives the generator [1]."
    )
    return _q(
        rng, "04", "04_steam_turbine_prime_mover_mechanical_rotation", prompt, correct, sol, 2, "short_answer",
        ["confusing_turbine_with_electrical_generator"],
        "Does the turbine create electricity itself, or spin something else that creates electricity?",
        "Steam pushes turbine blades -> mechanical rotation turns the generator shaft.",
        correct,
    )


def arch_05_cooling_towers_hyperbolic_water_vapour_myth(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Lethabo Power Station", "Orlando Power Station in Soweto", "Duvha Power Station"])
    myth = rng.choice(["toxic carbon monoxide gas", "thick black coal smoke", "radioactive fallout clouds"])
    prompt = (
        f"Passing **{station}**, a learner points at the wide white clouds billowing from the tall hyperbolic **cooling towers** and claims they are **{myth}**.\n\n"
        "What actually exits the top of hyperbolic cooling towers, and what is their engineering function?"
    )
    correct = "Harmless pure water vapour (condensing into clean water droplets); they cool warm condenser water so purified boiler water can be reused"
    distractors = [
        f"Dense {myth} pumped directly from the coal furnace fire.",
        "Pure liquid oxygen formed by splitting coal ash inside the furnace.",
        "Excess electrical current leaking upward into thunderclouds.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Furnace flue gases exit through the tall thin chimney stack, NOT the wide curved cooling towers.\n"
        "**Step 2:** Hyperbolic cooling towers cool hot condenser water using airflow; the white plume is harmless **water vapour / condensed steam droplets** [2]."
    )
    return _q(
        rng, "05", "05_cooling_towers_hyperbolic_water_vapour_myth", prompt, correct, sol, 2, "multiple_choice",
        ["cooling_towers_emit_toxic_smoke_myth"],
        "Distinguish the narrow furnace smokestack from the wide hyperbolic water-cooling towers.",
        "Harmless water vapour / steam droplets from cooling recycled condenser water.",
        correct, options=options,
    )


def arch_06_coal_geological_formation_and_non_renewable_classification(rng: random.Random) -> Dict[str, Any]:
    coalfield = rng.choice(["eMalahleni (Witbank) coalfield", "Waterberg coalfield", "Highveld coalfield", "Ermelo coalfield"])
    years_m = rng.choice([250, 280, 300])
    prompt = (
        f"Coal extracted from the **{coalfield}** supplies South African thermal power stations.\n\n"
        f"1. Describe how coal formed from prehistoric swamps over roughly **{years_m} million years** [2].\n"
        "2. Classify coal as renewable or non-renewable and justify your classification [2]."
    )
    correct = "Ancient swamp vegetation was buried under sediment layers and compressed under high pressure and heat over millions of years; Non-renewable because reserves are finite and take millions of years to form, far slower than human consumption"
    sol = (
        f"**Step 1:** Prehistoric swamp plants were buried by **layers of sediment** and compressed under intense pressure and heat over ~{years_m} million years to form fossilised coal [2].\n\n"
        "**Step 2:** Coal is **non-renewable** because Earth holds a finite supply that cannot be replenished within a human timescale [2]."
    )
    return _q(
        rng, "06", "06_coal_geological_formation_and_non_renewable_classification", prompt, correct, sol, 4, "short_answer",
        ["claiming_coal_is_renewable_because_plants_grow_quickly"],
        "Remember two keywords: buried swamp vegetation + sediment compression over millions of years.",
        "Fossil fuel from compressed prehistoric swamps; finite and non-renewable.",
        correct,
    )


def arch_07_south_african_coal_power_stations_geographic_clustering(rng: random.Random) -> Dict[str, Any]:
    station, prov = rng.choice([
        ("Arnot Power Station", "Mpumalanga"),
        ("Camden Power Station", "Mpumalanga"),
        ("Duvha Power Station", "Mpumalanga"),
        ("Lethabo Power Station", "Free State"),
        ("Matimba Power Station", "Limpopo"),
        ("Kelvin Power Station", "Gauteng"),
    ])
    prompt = (
        f"In South Africa, **{station}** is an established coal-fired electricity generating facility.\n\n"
        f"In which South African province is **{station}** located, and why are most major coal stations clustered near the Mpumalanga coalfields?"
    )
    correct = f"{prov}; locating power stations right next to coal mines minimises transport cost and delays of hauling millions of tonnes of coal"
    all_provs = ["Mpumalanga", "Free State", "Limpopo", "Gauteng", "Western Cape", "Northern Cape"]
    wrong_provs = [p for p in all_provs if p != prov]
    rng.shuffle(wrong_provs)
    options = [
        correct,
        f"{wrong_provs[0]}; coal must be shipped from Atlantic ocean tankers.",
        f"{wrong_provs[1]}; stations require desert sand to boil furnace water.",
        f"{wrong_provs[2]}; coal only burns effectively at coastal sea level.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** **{station}** is situated in **{prov}** [1].\n\n"
        "**Step 2:** Building stations near mines (especially in Mpumalanga) avoids huge transport costs and logistical bottlenecks [1]."
    )
    return _q(
        rng, "07", "07_south_african_coal_power_stations_geographic_clustering", prompt, correct, sol, 2, "multiple_choice",
        ["locating_all_sa_coal_stations_in_western_cape"],
        "Think about where South Africa's rich coalfields lie and why stations sit right beside the mines.",
        f"{station} -> {prov}.",
        correct, options=options,
    )


def arch_08_coal_combustion_greenhouse_gases_and_acid_rain_impacts(rng: random.Random) -> Dict[str, Any]:
    tonnes = rng.choice([8500, 11200, 14000, 16500])
    prompt = (
        f"A large coal-fired power station burns approximately **{tonnes} tonnes** of coal every day to meet national electricity demand.\n\n"
        "1. Identify the primary **greenhouse gas** released during combustion and explain its climate consequence [2].\n"
        "2. Name one acidic pollutant gas emitted alongside carbon dioxide and explain how it harms ecosystems [2].\n"
        "3. State one additional land or water impact of coal-based generation [1]."
    )
    correct = "Carbon dioxide (CO2) traps infrared heat in the atmosphere (enhanced greenhouse effect / global warming); Sulfur dioxide (SO2) forms acid rain that acidifies soils and rivers; Open-cast mining scars land / stations consume vast fresh water / fly ash causes respiratory illness"
    sol = (
        "**Step 1:** **Carbon dioxide ($\\text{CO}_2$)** accumulates in the atmosphere, enhancing the greenhouse effect and driving **global warming / climate change** [2].\n\n"
        "**Step 2:** **Sulfur dioxide ($\\text{SO}_2$)** (or nitrogen oxides) reacts with atmospheric moisture to form **acid rain**, damaging soil fertility, crops, and aquatic habitats [2].\n\n"
        "**Step 3:** Open-cast mining degrades ecosystems, fly ash causes lung irritation, and boilers/cooling consume large volumes of freshwater [1]."
    )
    return _q(
        rng, "08", "08_coal_combustion_greenhouse_gases_and_acid_rain_impacts", prompt, correct, sol, 5, "structured",
        ["confusing_greenhouse_effect_with_ozone_hole"],
        "Link CO2 to global warming, SO2 to acid rain, and ash/mining/water to local environmental harm.",
        "CO2 (climate change), SO2 (acid rain), fly ash/mining/water depletion.",
        correct,
    )


def arch_09_alternative_energy_meaning_and_renewable_distinction(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("wind turbines and hydroelectric dams", "both are renewable"),
        ("nuclear fission and solar photovoltaic farms", "solar is renewable, whereas nuclear uses finite uranium fuel (non-renewable)"),
        ("tidal wave generators and biofuels", "both are renewable"),
        ("sun-heated steam towers and nuclear fission", "sun-heated steam is renewable, whereas uranium for nuclear fission is non-renewable"),
    ])
    sources, renew_note = pair
    prompt = (
        f"Energy planners refer to **{sources}** as **alternative energy sources** in South Africa.\n\n"
        "1. Explain why non-coal generation methods are called *alternative* energy sources in South Africa [1].\n"
        f"2. Classify **{sources}** as renewable or non-renewable [2]."
    )
    correct = f"Coal is South Africa's main baseline electricity source, so any non-coal source used instead is an alternative; {renew_note.capitalize()}"
    sol = (
        "**Step 1:** Because South Africa relies primarily on **coal** for electricity generation, other power options are grouped as **alternative energy sources** [1].\n\n"
        f"**Step 2:** Classification of {sources}: **{renew_note}** [2]."
    )
    return _q(
        rng, "09", "09_alternative_energy_meaning_and_renewable_distinction", prompt, correct, sol, 3, "short_answer",
        ["assuming_all_alternative_energy_is_automatically_renewable"],
        "Ask: alternative to WHAT main SA fuel? And check whether uranium is replenished naturally.",
        f"Alternative to dominant coal; {renew_note}.",
        correct,
    )


def arch_10_hydroelectric_dam_energy_transformation_chain(rng: random.Random) -> Dict[str, Any]:
    dam = rng.choice(["Gariep Dam", "Vanderkloof Dam", "Kouga Dam"])
    head_m = rng.choice([45, 65, 85, 110])
    spec = _svg_hydro_station(rng, dam, head_m)
    prompt = (
        f"Study the hydroelectric station schematic for **{dam}** (water head height **{head_m} m**).\n\n"
        "1. Identify the form of energy stored in the high reservoir water at **A** [1].\n"
        "2. Describe the energy transfer as water accelerates down the penstock **B** into turbine **C** [2].\n"
        "3. Identify component **D** and state the energy output delivered via the power lines [2]."
    )
    correct = "Gravitational potential energy; Gravitational potential energy converts to kinetic energy of falling water, which turns turbine C mechanically; D is the electrical generator outputting electrical energy"
    sol = (
        "**Step 1:** Elevated water behind the dam wall at **A** stores **gravitational potential energy** [1].\n\n"
        "**Step 2:** Rushing down **B**, potential energy becomes **kinetic energy** of flowing water, transferring mechanical rotational energy to **turbine C** [2].\n\n"
        "**Step 3:** **D** is the **generator**, converting mechanical energy into **electrical energy** sent onto the national power lines [2]."
    )
    return _q(
        rng, "10", "10_hydroelectric_dam_energy_transformation_chain", prompt, correct, sol, 5, "structured",
        ["confusing_water_kinetic_energy_at_rest_behind_dam"],
        "Water sitting high up has gravitational potential energy; falling water gains kinetic energy.",
        "A = gravitational potential; B->C = kinetic to turbine rotation; D = generator -> electrical.",
        correct, diagram_spec=spec,
    )


def arch_11_south_african_hydroelectric_dams_and_river_systems(rng: random.Random) -> Dict[str, Any]:
    station, loc = rng.choice([
        ("Gariep Dam Hydroelectric Station", "Free State–Eastern Cape border"),
        ("Vanderkloof Dam Hydroelectric Station", "Northern Cape"),
        ("Kouga Dam Hydroelectric Station", "Eastern Cape"),
        ("Ingula Pumped Storage Scheme", "KwaZulu-Natal (and Free State escarpment)"),
        ("Palmiet Pumped Storage Scheme", "Western Cape"),
    ])
    prompt = (
        f"South Africa operates several hydroelectric and pumped-storage stations alongside coal plants.\n\n"
        f"Where is **{station}** located?"
    )
    all_locs = [
        "Free State–Eastern Cape border",
        "Northern Cape",
        "Eastern Cape",
        "KwaZulu-Natal (and Free State escarpment)",
        "Western Cape",
        "Limpopo",
    ]
    wrongs = [x for x in all_locs if x != loc]
    rng.shuffle(wrongs)
    options = [loc] + wrongs[:3]
    rng.shuffle(options)
    sol = f"**Step 1:** Official South African provincial record: **{station}** is located in **{loc}** [1]."
    return _q(
        rng, "11", "11_south_african_hydroelectric_dams_and_river_systems", prompt, loc, sol, 1, "multiple_choice",
        ["confusing_gariep_dam_with_western_cape_stations"],
        "Recall the Orange River dams (Gariep, Vanderkloof) vs Western Cape and Drakensberg schemes.",
        f"{station}: {loc}.",
        loc, options=options,
    )


def arch_12_classroom_aluminium_wheel_water_turbine_investigation(rng: random.Random) -> Dict[str, Any]:
    mass_g = rng.choice([25, 40, 50, 75])
    lift_cm = rng.choice([30, 45, 60])
    spec = _svg_foil_turbine_activity(rng, mass_g, lift_cm)
    prompt = (
        f"Inspect the classroom water turbine apparatus lifting a **{mass_g} g** metal nut by **{lift_cm} cm**.\n\n"
        "1. Trace the complete energy transfer from the falling tap water to the lifted metal mass [3].\n"
        "2. Why would an aluminium foil plate wheel outlast a thick cardboard wheel during repeated trials? [1]"
    )
    correct = f"Gravitational potential energy of tap water -> kinetic energy of falling stream -> rotational kinetic energy of wheel and pencil axle -> gravitational potential energy gained by the {mass_g} g mass lifted {lift_cm} cm; Aluminium foil is waterproof whereas wet cardboard softens and loses shape"
    sol = (
        "**Step 1:** Falling water converts gravitational potential energy to kinetic energy [1], spinning the aluminium wheel blades and pencil axle [1], which winds the string to raise the mass piece and increase its **gravitational potential energy** [1].\n\n"
        "**Step 2:** Cardboard absorbs water, turns soggy, and collapses, whereas **aluminium foil is waterproof** [1]."
    )
    return _q(
        rng, "12", "12_classroom_aluminium_wheel_water_turbine_investigation", prompt, correct, sol, 4, "short_answer",
        ["omitting_gravitational_potential_energy_gain_of_lifted_mass"],
        "Follow the energy step-by-step: tap water -> blades -> pencil -> winding string -> raised weight.",
        "Water GPE -> Water KE -> Wheel & axle KE -> Mass GPE; foil resists water damage.",
        correct, diagram_spec=spec,
    )


def arch_13_pumped_storage_hydro_water_battery_peak_vs_offpeak(rng: random.Random) -> Dict[str, Any]:
    scheme = rng.choice(["Ingula Pumped Storage Scheme", "Drakensberg Pumped Storage Scheme", "Palmiet Pumped Storage Scheme"])
    is_peak = rng.choice([True, False])
    mw = rng.choice([1000, 1200, 1332])
    spec = _svg_pumped_storage(rng, scheme, is_peak, mw)
    if is_peak:
        prompt = (
            f"Inspect the operating mode of **{scheme}** (**{mw} MW**), often described as a giant 'water battery'.\n\n"
            "1. State the direction of water flow during **evening peak demand** and describe the energy conversion taking place [2].\n"
            "2. Explain why pumped storage schemes are valuable for stabilising the national grid [1]."
        )
        correct = "Water flows downward from the upper mountain dam through turbines to the lower dam, converting gravitational potential energy -> kinetic energy -> electrical energy; They rapidly supply extra peak power within minutes when demand spikes"
    else:
        prompt = (
            f"Inspect the operating mode of **{scheme}** (**{mw} MW**) during **off-peak early morning hours**.\n\n"
            "1. State the direction of water movement and explain how excess grid electrical energy is stored [2].\n"
            "2. Why is it economical to pump water uphill during off-peak hours rather than midday? [1]"
        )
        correct = "Surplus grid electricity runs pumps that push water uphill from the lower dam back to the upper dam, storing electrical energy as gravitational potential energy; Off-peak grid electricity is cheaper and excess baseload coal power would otherwise be wasted"
    sol = (
        f"**Step 1:** In **{'peak generation' if is_peak else 'off-peak pumping'}** mode at {scheme}: {correct.split('; ')[0]} [2].\n\n"
        f"**Step 2:** {correct.split('; ')[1]} [1]."
    )
    return _q(
        rng, "13", "13_pumped_storage_hydro_water_battery_peak_vs_offpeak", prompt, correct, sol, 3, "structured",
        ["thinking_pumped_storage_creates_net_free_energy"],
        "Check whether water is flowing DOWN to generate peak power or pumped UP using surplus off-peak power.",
        correct, correct, diagram_spec=spec,
    )


def arch_14_pumped_storage_efficiency_and_net_energy_calculation(rng: random.Random) -> Dict[str, Any]:
    e_in = rng.choice([400, 500, 640, 800])
    eff = rng.choice([72, 75, 78, 80])
    e_out = e_in * (eff / 100.0)
    e_lost = e_in - e_out
    prompt = (
        f"During off-peak hours, **{e_in} MWh** of surplus grid electricity is used to pump water to the upper reservoir of a pumped storage scheme with an overall cycle efficiency of **{eff}%**.\n\n"
        "1. Calculate the electrical energy (in MWh) recovered during evening peak generation [2].\n"
        "2. Calculate the energy lost as friction and heat during the full pumping–generation cycle [1]."
    )
    correct = f"{_fmt_num(e_out, 1)} MWh recovered; {_fmt_num(e_lost, 1)} MWh lost"
    sol = (
        f"**Step 1:** Recovered energy: $E_{{\\text{{out}}}} = {e_in} \\times \\frac{{{eff}}}{{100}} = \\mathbf{{{_fmt_num(e_out, 1)}\\text{{ MWh}}}}$ [2].\n\n"
        f"**Step 2:** Energy wasted to friction/heat: $E_{{\\text{{lost}}}} = {e_in} - {_fmt_num(e_out, 1)} = \\mathbf{{{_fmt_num(e_lost, 1)}\\text{{ MWh}}}}$ [1]."
    )
    return _q(
        rng, "14", "14_pumped_storage_efficiency_and_net_energy_calculation", prompt, correct, sol, 3, "calculation",
        ["assuming_pumped_storage_is_100_percent_efficient"],
        "Multiply input MWh by (efficiency / 100) to find useful output, then subtract from input.",
        f"{_fmt_num(e_out, 1)} MWh recovered; {_fmt_num(e_lost, 1)} MWh lost.",
        correct,
    )


def arch_15_faraday_electromagnetic_induction_principle(rng: random.Random) -> Dict[str, Any]:
    action = rng.choice([
        "pushing a strong bar magnet rapidly into a stationary coil of copper wire",
        "spinning a coil of insulated copper wire between opposite poles of a magnet",
        "rotating heavy rotor magnets past fixed copper stator windings inside a generator",
    ])
    prompt = (
        f"In an investigation, **{action}** produces an electric current detected on a sensitive meter, even with no battery attached.\n\n"
        "1. Name the scientific principle discovered by Michael Faraday in 1831–1832 that explains this observation [1].\n"
        "2. State the two physical requirements needed for a generator to keep inducing electric current [2]."
    )
    correct = "Electromagnetic induction; An electrical conductor (wire coil) and relative motion through a changing magnetic field"
    sol = (
        "**Step 1:** This phenomenon is **electromagnetic induction** (Faraday's Law) [1].\n\n"
        "**Step 2:** Relative motion between a **conducting coil** and a **magnetic field** creates a potential difference across the wire ends, driving electric current [2]."
    )
    return _q(
        rng, "15", "15_faraday_electromagnetic_induction_principle", prompt, correct, sol, 3, "short_answer",
        ["thinking_stationary_magnet_inside_coil_generates_continuous_current"],
        "What did Michael Faraday discover in 1831 about moving a magnet or wire?",
        "Electromagnetic induction: conductor + changing magnetic field (relative motion).",
        correct,
    )


def arch_16_generator_rotor_stator_coil_and_magnet_configurations(rng: random.Random) -> Dict[str, Any]:
    rpm = rng.choice([1500, 3000])
    v_out = rng.choice([11000, 20000, 22000])
    spec = _svg_generator_coil_magnet(rng, rpm, v_out)
    prompt = (
        f"Inspect the power-station generator layout operating at **{rpm} rpm** and **{v_out} V**.\n\n"
        "If the steam supply shuts off completely so the central magnet stops spinning, what happens to the induced voltage and why?"
    )
    correct = "Induced voltage drops immediately to 0 V because without continuous relative motion there is no changing magnetic field across the copper coils"
    distractors = [
        f"Induced voltage stays constant at {v_out} V because the permanent magnet holds stored charge.",
        "Induced voltage doubles because stationary magnets attract more electrons from the wire.",
        "The copper coils melt instantly as soon as mechanical rotation stops.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Electromagnetic induction requires **continuous change** (relative movement between the magnet and conducting coils).\n"
        "**Step 2:** When rotation halts, magnetic flux stops changing and induced voltage drops to **0 V** [2]."
    )
    return _q(
        rng, "16", "16_generator_rotor_stator_coil_and_magnet_configurations", prompt, correct, sol, 2, "multiple_choice",
        ["believing_stationary_magnets_generate_electricity"],
        "Does a stationary magnet next to a stationary coil induce current?",
        "Drops to 0 V because relative motion / changing magnetic field stops.",
        correct, options=options, diagram_spec=spec,
    )


def arch_17_faraday_copper_disk_historical_generator(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice([
        ("rotating copper disk between horseshoe magnet poles", "acts as the electrical conductor moving through a magnetic field to induce current"),
        ("sliding metal brushes touching the disk edge and axle", "collect the induced electric current from the spinning disk and feed it to external wires"),
    ])
    comp, func = part
    prompt = (
        "In 1831, Michael Faraday built the **Faraday Disk**, the world's first electromagnetic generator, by turning a copper disc between the poles of a horseshoe magnet.\n\n"
        f"What is the role of the **{comp}** in this historical apparatus?"
    )
    correct = f"It {func}."
    distractors = [
        "It burns pulverised coal to boil water into high-pressure steam.",
        "It chemically dissolves copper into acid like a primary electric cell.",
        "It converts electrical energy into nuclear radiation for storage.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** In the 1831 Faraday Disk, the **{comp}** {func} [2]."
    )
    return _q(
        rng, "17", "17_faraday_copper_disk_historical_generator", prompt, correct, sol, 2, "multiple_choice",
        ["confusing_faraday_disk_with_electrochemical_battery"],
        "Think about Faraday's Disk parts: horseshoe magnet (field), spinning copper disc (conductor), brushes (contacts).",
        correct, correct, options=options,
    )


def arch_18_portable_petrol_diesel_generator_energy_and_safety(rng: random.Random) -> Dict[str, Any]:
    fuel = rng.choice(["petrol", "diesel"])
    load_w = rng.choice([1200, 2400, 3500])
    prompt = (
        f"During an outage, a household runs a portable **{fuel}-powered generator** supplying **{load_w} W** for lights and a refrigerator.\n\n"
        "1. State the sequence of energy conversions inside the portable generator [2].\n"
        "2. State **two critical safety precautions** that must be followed when operating a portable fuel generator [2]."
    )
    correct = f"Chemical potential energy ({fuel}) -> thermal and mechanical kinetic energy in the engine -> electrical energy in the alternator; Operate strictly outdoors in a well-ventilated space to avoid fatal carbon monoxide exhaust poisoning, and keep away from water/rain to prevent electrocution"
    sol = (
        f"**Step 1:** Combustion converts **chemical potential energy** in {fuel} into **mechanical kinetic energy** spinning the engine shaft, which drives an alternator to induce **electrical energy** [2].\n\n"
        "**Step 2:** (a) Run **outdoors in a well-ventilated area** — exhaust contains poisonous gases such as carbon monoxide; (b) keep dry and **away from water** to avoid short-circuits and shock [2]."
    )
    return _q(
        rng, "18", "18_portable_petrol_diesel_generator_energy_and_safety", prompt, correct, sol, 4, "structured",
        ["running_portable_generator_inside_closed_garage_safety_error"],
        "Remember fuel energy chain + exhaust gas asphyxiation risk + moisture shock risk.",
        "Chemical -> Mechanical -> Electrical; outdoors (ventilation) + dry away from water.",
        correct,
    )


def arch_19_bicycle_dynamo_mechanical_to_electrical_operation(rng: random.Random) -> Dict[str, Any]:
    speed_kmh = rng.choice([12, 18, 24, 30])
    spec = _svg_bicycle_dynamo(rng, speed_kmh)
    prompt = (
        f"Inspect the bicycle dynamo operating while a cyclist rides at **{speed_kmh} km/h**.\n\n"
        "1. Describe how the moving tyre produces electrical energy inside the dynamo casing [2].\n"
        "2. Explain what happens to the brightness of the headlamp when the cyclist slows down and stops at an intersection [2]."
    )
    correct = "The turning tyre spins the dynamo roller and internal permanent magnet inside surrounding stationary wire coils, inducing electric current via electromagnetic induction; As speed drops, the magnet rotates slower producing dimmer light, and at rest the lamp goes off completely because induction stops"
    sol = (
        "**Step 1:** Friction between the spinning tyre and knurled roller rotates an internal **permanent magnet inside copper wire coils**, inducing electric current [2].\n\n"
        f"**Step 2:** Slowing down from {speed_kmh} km/h reduces the rate of magnetic field change so the lamp dims; at a full stop (0 km/h) current drops to zero and the **lamp turns off** [2]."
    )
    return _q(
        rng, "19", "19_bicycle_dynamo_mechanical_to_electrical_operation", prompt, correct, sol, 4, "short_answer",
        ["thinking_bicycle_dynamo_contains_rechargeable_battery_that_stays_bright_when_stopped"],
        "A classic bottle dynamo has NO battery—it only induces current while the wheel spins!",
        "Tyre spins magnet in coil -> current; dims as cyclist slows and turns off when stopped.",
        correct, diagram_spec=spec,
    )


def arch_20_wind_turbines_and_offshore_wind_farm_energy_conversion(rng: random.Random) -> Dict[str, Any]:
    site = rng.choice(["Jeffreys Bay Wind Farm", "Darling Wind Farm", "Noupoort Wind Farm", "an offshore coastal wind farm"])
    wind_ms = rng.choice([8.5, 11.2, 14.0])
    prompt = (
        f"At **{site}**, large rotor blades turn in steady coastal winds blowing at **{_fmt_num(wind_ms)} m/s**.\n\n"
        "1. State the energy conversion chain inside a wind turbine [2].\n"
        "2. Give one environmental advantage and one practical disadvantage of relying solely on wind generation [2]."
    )
    correct = "Kinetic energy of moving air (wind) -> rotational mechanical kinetic energy of turbine blades/shaft -> electrical energy in the generator; Advantage: renewable with zero greenhouse gas emissions during operation; Disadvantage: intermittent/weather-dependent (stops when wind calms)"
    sol = (
        f"**Step 1:** Wind (**kinetic energy of moving air**) spins the angled blades (**mechanical kinetic energy**), driving an internal **generator** to produce **electrical energy** [2].\n\n"
        "**Step 2:** Advantage: **renewable and emission-free** during operation [1]. Disadvantage: **intermittent / variable** depending on wind speed and location [1]."
    )
    return _q(
        rng, "20", "20_wind_turbines_and_offshore_wind_farm_energy_conversion", prompt, correct, sol, 4, "short_answer",
        ["thinking_wind_turbines_create_wind_like_fans"],
        "Remember: wind moves the blades (not electricity moving blades), and wind is clean yet variable.",
        "Wind KE -> Rotor KE -> Electrical; clean & renewable, but intermittent.",
        correct,
    )


def arch_21_solar_pv_vs_concentrated_solar_steam_power(rng: random.Random) -> Dict[str, Any]:
    town = rng.choice(["Upington", "Kathu", "De Aar", "Pofadder"])
    prompt = (
        f"In the sunny Northern Cape near **{town}**, engineers deploy two distinct solar technologies: **Solar Photovoltaic (PV) panels** and **sun-heated steam towers** (concentrated solar power).\n\n"
        "How do these two solar systems differ mechanically in generating electricity?"
    )
    correct = "Solar PV converts sunlight directly into electrical energy using semiconductor cells with no moving turbines, whereas sun-heated steam stations boil water/fluid to turn a turbine and generator"
    distractors = [
        "Solar PV burns coal dust underground, whereas sun-heated steam uses nuclear fission.",
        "Both technologies rely on underground water tides pushing magnetic pistons.",
        "Sun-heated steam works exclusively during cloudy midnight storms, whereas Solar PV requires wind.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** **Solar PV panels** convert radiant light energy directly into electricity via semiconductor cells (no steam, no turbine).\n"
        "**Step 2:** **Sun-heated steam** systems focus sunlight to heat water into steam, turning a conventional **turbine and generator** [2]."
    )
    return _q(
        rng, "21", "21_solar_pv_vs_concentrated_solar_steam_power", prompt, correct, sol, 2, "multiple_choice",
        ["thinking_solar_pv_panels_contain_boiling_water_and_turbines"],
        "Distinguish direct light-to-electricity semiconductor panels from sun-heated steam driving a turbine.",
        "PV = direct semiconductor conversion (no turbine); sun-heated steam = boils fluid to spin turbine.",
        correct, options=options,
    )


def arch_22_tidal_wave_and_biofuel_alternative_generation(rng: random.Random) -> Dict[str, Any]:
    tech = rng.choice([
        ("tidal energy turbines", "gravitational pull of the Moon and Sun driving ocean tides", "kinetic energy of rising/falling seawater turns underwater turbines linked to generators"),
        ("biofuel power plants", "living/recently living organic plant matter (biomass, ethanol, biogas)", "burning renewable plant-derived fuel heats water into steam to spin a turbine and generator"),
    ])
    name, origin, mech = tech
    prompt = (
        f"Both tidal energy and biofuels appear in national alternative energy mixes.\n\n"
        f"For **{name}**:\n"
        "1. Identify the primary energy origin [1].\n"
        "2. Describe how mechanical or thermal motion reaches the electrical generator [2]."
    )
    correct = f"Origin: {origin.capitalize()}; Mechanism: {mech.capitalize()}"
    sol = (
        f"**Step 1:** Primary origin of {name}: **{origin}** [1].\n\n"
        f"**Step 2:** Generation mechanism: **{mech}** [2]."
    )
    return _q(
        rng, "22", "22_tidal_wave_and_biofuel_alternative_generation", prompt, correct, sol, 3, "short_answer",
        ["confusing_biofuels_with_geological_coal_or_nuclear_fuel"],
        "Consider whether ocean gravitational tides or organic plant fuels drive the turbine.",
        f"{origin}; {mech}.",
        correct,
    )


def arch_23_renewable_intermittency_and_baseload_grid_stability(rng: random.Random) -> Dict[str, Any]:
    solar_peak = rng.choice([9500, 12000, 15000])
    eve_demand = rng.choice([31000, 34000, 36500])
    spec = _svg_intermittency_curve(rng, solar_peak, eve_demand)
    prompt = (
        f"Analyse the plotted 24-hour Solar PV output (peaking at **{solar_peak} MW** at midday) against national demand (peaking at **{eve_demand} MW** around 19:00).\n\n"
        "1. Identify the engineering mismatch visible at **19:00** [1].\n"
        "2. Explain why a grid powered by intermittent solar and wind needs **energy storage** (such as pumped storage or batteries) or dispatchable baseload power [2]."
    )
    correct = f"At 19:00 solar generation drops to 0 MW right when national demand peaks at {eve_demand} MW; Because solar and wind depend on sunlight and weather, storage or dispatchable stations must supply electricity when renewable generation drops below demand"
    sol = (
        f"**Step 1:** At **19:00** (sunset), solar output falls to **0 MW** at the exact hour consumer demand hits **{eve_demand} MW** [1].\n\n"
        "**Step 2:** Weather-dependent renewables are **intermittent**; grid storage (pumped hydro/batteries) or reliable baseload stations must bridge evening peaks and calm cloudy days [2]."
    )
    return _q(
        rng, "23", "23_renewable_intermittency_and_baseload_grid_stability", prompt, correct, sol, 3, "short_answer",
        ["assuming_solar_panels_generate_peak_power_during_evening_demand"],
        "Compare the yellow solar curve vs the red demand curve at 19:00!",
        "Solar drops to 0 MW at 19:00 peak -> needs storage/baseload backup.",
        correct, diagram_spec=spec,
    )


def arch_24_comparing_coal_hydro_and_wind_water_and_emission_footprint(rng: random.Random) -> Dict[str, Any]:
    coal_co2 = rng.choice([950, 1000, 1050])
    wind_co2 = rng.choice([12, 15, 20])
    mwh = rng.choice([20, 30, 50])
    saved_kg = (coal_co2 - wind_co2) * mwh
    saved_tonnes = saved_kg / 1000.0
    spec = _svg_footprint_bars(rng, coal_co2, wind_co2, mwh)
    prompt = (
        f"Study the emissions bar graph comparing Coal (**{coal_co2} kg CO₂/MWh**) and Wind (**{wind_co2} kg CO₂/MWh**).\n\n"
        f"If a coastal wind farm supplies **{mwh} MWh** to replace coal generation, calculate the mass of $\\text{{CO}}_2$ emissions avoided in **tonnes** ($1\\text{{ tonne}} = 1\\,000\\text{{ kg}}$) [3]."
    )
    correct = f"{_fmt_num(saved_tonnes, 2)} tonnes"
    sol = (
        f"**Step 1:** Saving per MWh: ${coal_co2} - {wind_co2} = {coal_co2 - wind_co2}\\text{{ kg/MWh}}$ [1].\n\n"
        f"**Step 2:** Total mass saved for {mwh} MWh: ${coal_co2 - wind_co2} \\times {mwh} = {saved_kg}\\text{{ kg}}$ [1].\n\n"
        f"**Step 3:** Convert to tonnes: $\\frac{{{saved_kg}}}{{1\\,000}} = \\mathbf{{{_fmt_num(saved_tonnes, 2)}\\text{{ tonnes}}}}$ [1]."
    )
    return _q(
        rng, "24", "24_comparing_coal_hydro_and_wind_water_and_emission_footprint", prompt, correct, sol, 3, "calculation",
        ["forgetting_to_divide_kg_by_1000_for_tonnes"],
        "Find difference per MWh, multiply by total MWh, then divide by 1 000.",
        f"{_fmt_num(saved_tonnes, 2)} tonnes CO2 avoided.",
        correct, diagram_spec=spec,
    )


def arch_25_power_station_energy_efficiency_sankey_analysis(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Duvha", "Camden", "Arnot", "Tutuka"])
    e_in = rng.choice([1000, 1200, 1500, 2000])
    eff_target = rng.choice([32, 35, 38, 40])
    e_elec = int(e_in * (eff_target / 100.0))
    e_heat = e_in - e_elec
    spec = _svg_station_sankey(rng, e_in, e_elec, station)
    prompt = (
        f"Analyse the Sankey energy flow visual for **{station} Power Station**: coal chemical input is **{e_in} MJ**, electrical output is **{e_elec} MJ**, and wasted thermal exhaust/condenser heat is **{e_heat} MJ**.\n\n"
        "1. Calculate the percentage **thermal efficiency** of the station [2].\n"
        "2. State where most of the wasted thermal energy leaves the station [1]."
    )
    correct = f"{eff_target}%; Lost via hot furnace flue gases and warm condenser cooling water/towers"
    sol = (
        f"**Step 1:** $\\text{{Efficiency}} = \\frac{{\\text{{Useful Electrical Output}}}}{{\\text{{Total Input}}}} \\times 100\\% = \\frac{{{e_elec}}}{{{e_in}}} \\times 100\\% = \\mathbf{{{eff_target}\\%}}$ [2].\n\n"
        "**Step 2:** Unconverted thermal energy dissipates via **cooling tower water vapour** and **hot chimney flue gases** [1]."
    )
    return _q(
        rng, "25", "25_power_station_energy_efficiency_sankey_analysis", prompt, correct, sol, 3, "calculation",
        ["dividing_wasted_heat_instead_of_useful_electricity_for_efficiency"],
        "Efficiency = (Useful Electrical Output / Total Chemical Input) x 100%.",
        f"{eff_target}% efficiency; dissipated in cooling towers and flue exhaust.",
        correct, diagram_spec=spec,
    )


BUILDERS_01_25 = {
    "01_coal_power_station_pulverisation_to_steam_sequence": arch_01_coal_power_station_pulverisation_to_steam_sequence,
    "02_coal_station_complete_energy_transformation_chain": arch_02_coal_station_complete_energy_transformation_chain,
    "03_pulverised_coal_surface_area_combustion_efficiency": arch_03_pulverised_coal_surface_area_combustion_efficiency,
    "04_steam_turbine_prime_mover_mechanical_rotation": arch_04_steam_turbine_prime_mover_mechanical_rotation,
    "05_cooling_towers_hyperbolic_water_vapour_myth": arch_05_cooling_towers_hyperbolic_water_vapour_myth,
    "06_coal_geological_formation_and_non_renewable_classification": arch_06_coal_geological_formation_and_non_renewable_classification,
    "07_south_african_coal_power_stations_geographic_clustering": arch_07_south_african_coal_power_stations_geographic_clustering,
    "08_coal_combustion_greenhouse_gases_and_acid_rain_impacts": arch_08_coal_combustion_greenhouse_gases_and_acid_rain_impacts,
    "09_alternative_energy_meaning_and_renewable_distinction": arch_09_alternative_energy_meaning_and_renewable_distinction,
    "10_hydroelectric_dam_energy_transformation_chain": arch_10_hydroelectric_dam_energy_transformation_chain,
    "11_south_african_hydroelectric_dams_and_river_systems": arch_11_south_african_hydroelectric_dams_and_river_systems,
    "12_classroom_aluminium_wheel_water_turbine_investigation": arch_12_classroom_aluminium_wheel_water_turbine_investigation,
    "13_pumped_storage_hydro_water_battery_peak_vs_offpeak": arch_13_pumped_storage_hydro_water_battery_peak_vs_offpeak,
    "14_pumped_storage_efficiency_and_net_energy_calculation": arch_14_pumped_storage_efficiency_and_net_energy_calculation,
    "15_faraday_electromagnetic_induction_principle": arch_15_faraday_electromagnetic_induction_principle,
    "16_generator_rotor_stator_coil_and_magnet_configurations": arch_16_generator_rotor_stator_coil_and_magnet_configurations,
    "17_faraday_copper_disk_historical_generator": arch_17_faraday_copper_disk_historical_generator,
    "18_portable_petrol_diesel_generator_energy_and_safety": arch_18_portable_petrol_diesel_generator_energy_and_safety,
    "19_bicycle_dynamo_mechanical_to_electrical_operation": arch_19_bicycle_dynamo_mechanical_to_electrical_operation,
    "20_wind_turbines_and_offshore_wind_farm_energy_conversion": arch_20_wind_turbines_and_offshore_wind_farm_energy_conversion,
    "21_solar_pv_vs_concentrated_solar_steam_power": arch_21_solar_pv_vs_concentrated_solar_steam_power,
    "22_tidal_wave_and_biofuel_alternative_generation": arch_22_tidal_wave_and_biofuel_alternative_generation,
    "23_renewable_intermittency_and_baseload_grid_stability": arch_23_renewable_intermittency_and_baseload_grid_stability,
    "24_comparing_coal_hydro_and_wind_water_and_emission_footprint": arch_24_comparing_coal_hydro_and_wind_water_and_emission_footprint,
    "25_power_station_energy_efficiency_sankey_analysis": arch_25_power_station_energy_efficiency_sankey_analysis,
}
