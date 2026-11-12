"""Grade 9 Natural Sciences - Cost of Electrical Energy: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Cost of electrical energy.md.
Focus:
Electrical power (P = E / t), SI units (W, kW, J/s), Joules & kilojoules conversions,
Watts & kilowatts conversions, appliance rating plates, heating vs non-heating demand,
sequencing appliances by power, kilowatt-hour (kWh) definition & conversion to MJ,
time conversions (s, min, h), and energy consumption calculations (E = P * t).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 2) -> str:
    """Format a number using South African comma notation, stripping trailing zeros if needed."""
    s = f"{val:.{decimals}f}"
    if decimals > 0 and "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_fixed(val: float, decimals: int = 2) -> str:
    """Format a fixed-decimal number using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


def _fmt_tex(val: float, decimals: int = 2) -> str:
    """Format a number for KaTeX/LaTeX using South African {,} comma separator."""
    s = f"{val:.{decimals}f}"
    if decimals > 0 and "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_int(val: int) -> str:
    """Format integer with South African thin/regular space thousands separator."""
    return f"{val:,}".replace(",", " ")


def _title_from_subskill(subskill: str) -> str:
    parts = subskill.split("_", 1)
    core = parts[1] if len(parts) > 1 else subskill
    return f"Cost of Electrical Energy: {core.replace('_', ' ').title()}"


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
    title: Optional[str] = None,
) -> Dict[str, Any]:
    guide = f"Marking Guide ({marks} marks): Award credit for each verified scientific step and unit shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_cee_{code}_{rng.randint(100000, 999999)}",
        "title": title or _title_from_subskill(subskill),
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


# ---------------------------------------------------------------------------
# Parameterized SVG Helpers (inline_svg)
# ---------------------------------------------------------------------------

def _svg_rating_plate(rng: random.Random, brand: str, appliance: str, model: str, watts: int, freq: int) -> Dict[str, Any]:
    """Parameterized manufacturer electrical rating plate sticker."""
    volts = rng.choice([220, 230, 240])
    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="35" y="20" width="360" height="150" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="35" y="20" width="360" height="34" rx="8" fill="#1e293b"/>'
        f'<text x="215" y="42" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{brand} — {appliance}</text>'
        f'<text x="55" y="78" font-size="11.5" fill="#334155">Model: {model}</text>'
        f'<text x="55" y="104" font-size="12" font-weight="bold" fill="#0f172a">Rated Input: {volts} V ~ {freq} Hz</text>'
        f'<rect x="55" y="118" width="205" height="34" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="157" y="140" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">Power: {watts} W</text>'
        f'<rect x="285" y="70" width="88" height="82" rx="4" fill="#e2e8f0" stroke="#64748b"/>'
        f'<text x="329" y="107" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">SABS</text>'
        f'<text x="329" y="126" font-size="10" fill="#475569" text-anchor="middle">APPROVED</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_power_bar_chart(rng: random.Random, items: List[tuple], title: str) -> Dict[str, Any]:
    """Parameterized bar graph of household appliance power ratings in Watts."""
    max_w = max(w for _, w in items)
    scale_max = max(2000, ((max_w + 499) // 500) * 500)
    palette = ["#2563eb", "#16a34a", "#ea580c", "#7c3aed", "#dc2626"]
    n = len(items)
    plot_w = 340
    slot = plot_w // n
    bar_w = min(46, slot - 16)
    bars_svg = []
    for i, (name, w_val) in enumerate(items):
        h = max(8, int((w_val / float(scale_max)) * 118))
        x = 72 + i * slot + (slot - bar_w) // 2
        y = 160 - h
        col = palette[i % len(palette)]
        short_lbl = name if len(name) <= 11 else name[:10] + "."
        bars_svg.append(
            f'<rect x="{x}" y="{y}" width="{bar_w}" height="{h}" fill="{col}" stroke="#0f172a"/>'
            f'<text x="{x + bar_w // 2}" y="{y - 5}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{w_val} W</text>'
            f'<text x="{x + bar_w // 2}" y="177" font-size="9.5" fill="#1e293b" text-anchor="middle">{short_lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 440 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="205" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="225" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>'
        f'<line x1="65" y1="34" x2="65" y2="160" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="160" x2="418" y2="160" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="58" y="42" font-size="9.5" fill="#475569" text-anchor="end">{scale_max}</text>'
        f'<text x="58" y="100" font-size="9.5" fill="#475569" text-anchor="end">{scale_max // 2}</text>'
        f'<text x="58" y="162" font-size="9.5" fill="#475569" text-anchor="end">0</text>'
        f'<text x="20" y="98" font-size="10.5" fill="#0f172a" transform="rotate(-90 20 98)" text-anchor="middle">Power (W)</text>'
        f'{"".join(bars_svg)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_time_conversion_bar(minutes: int) -> Dict[str, Any]:
    """Parameterized fraction-of-an-hour clock/bar diagram."""
    max_mins = 120 if minutes > 60 else 60
    frac_w = max(28, int((minutes / float(max_mins)) * 300))
    mid_lbl = "60 min (1,0 h)" if max_mins == 120 else "30 min (0,5 h)"
    end_lbl = "120 min (2,0 h)" if max_mins == 120 else "60 min (1,0 h)"
    hdr_lbl = "2 Hours (120 min)" if max_mins == 120 else "1 Hour (60 min)"
    svg = (
        f'<svg viewBox="0 0 420 150" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="150" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="25" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Operating Time Portion of {hdr_lbl}</text>'
        f'<rect x="60" y="50" width="300" height="36" rx="4" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>'
        f'<rect x="60" y="50" width="{frac_w}" height="36" rx="4" fill="#3b82f6" stroke="#1d4ed8"/>'
        f'<text x="{60 + frac_w // 2}" y="73" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">{minutes} min</text>'
        f'<text x="60" y="106" font-size="10" fill="#475569">0 min (0 h)</text>'
        f'<text x="210" y="106" font-size="10" fill="#475569" text-anchor="middle">{mid_lbl}</text>'
        f'<text x="360" y="106" font-size="10" fill="#475569" text-anchor="end">{end_lbl}</text>'
        f'<text x="210" y="132" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Active Duration: {minutes} min ({_fmt_int(minutes * 60)} s)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_dual_appliance_energy(name1: str, w1: int, h1: float, name2: str, w2: int, h2: float) -> Dict[str, Any]:
    """Parameterized visual comparing two appliances' power ratings and run durations."""
    e1 = (w1 / 1000.0) * h1
    e2 = (w2 / 1000.0) * h2
    max_e = max(e1, e2, 0.5)
    b1 = max(25, int((e1 / max_e) * 230))
    b2 = max(25, int((e2 / max_e) * 230))
    svg = (
        f'<svg viewBox="0 0 430 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="185" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="24" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Appliance Power and Usage Duration Comparison</text>'
        f'<text x="24" y="64" font-size="11" font-weight="bold" fill="#1e3a8a">{name1} ({w1} W for {_fmt_num(h1, 2)} h)</text>'
        f'<rect x="24" y="72" width="{b1}" height="24" rx="4" fill="#2563eb"/>'
        f'<text x="{24 + b1 + 8}" y="88" font-size="10.5" font-weight="bold" fill="#1e3a8a">E₁ = ?</text>'
        f'<text x="24" y="124" font-size="11" font-weight="bold" fill="#9a3412">{name2} ({w2} W for {_fmt_num(h2, 2)} h)</text>'
        f'<rect x="24" y="132" width="{b2}" height="24" rx="4" fill="#ea580c"/>'
        f'<text x="{24 + b2 + 8}" y="148" font-size="10.5" font-weight="bold" fill="#9a3412">E₂ = ?</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ---------------------------------------------------------------------------
# Archetypes 01 to 25
# ---------------------------------------------------------------------------

def arch_01_electrical_power_rate_of_energy_transfer_definition(rng: random.Random) -> Dict[str, Any]:
    app, watts = rng.choice([
        ("an electric kettle", 2000),
        ("a microwave oven", 1200),
        ("a steam iron", 1800),
        ("an electric fan", 120),
        ("a toaster", 900),
        ("an electric urn", 1500),
    ])
    town = rng.choice(["Polokwane", "Gqeberha", "Bloemfontein", "Rustenburg", "Mbombela"])
    prompt = (
        f"A learner in {town} inspects {app} stamped with a power rating of ${watts}\\text{{ W}}$.\n\n"
        "Which statement accurately defines **electrical power** and explains the physical meaning of a **rate**?"
    )
    correct = "The rate at which electrical energy is supplied or transferred per unit of time, comparing energy transferred to elapsed time just as speed compares distance to time."
    options = [
        correct,
        "The total amount of electric charge stored permanently inside an unplugged copper cord.",
        "The maximum voltage pushed across an open switch when no electrons are flowing.",
        "The total energy consumed over a full thirty-day municipal billing period regardless of duration.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** **Electrical power** ($P$) is the **rate** of electrical energy supply — the quantity of electrical energy transferred per unit time ($P = \\frac{E}{t}$).\n\n"
        "**Step 2:** Just as speed ($\\text{km/h}$) is a rate comparing distance to time, electrical power ($\\text{J/s}$ or $\\text{W}$) measures how rapidly energy is delivered.\n\n"
        f"**Conclusion:** {correct}"
    )
    return _q(
        rng, "01", "01_electrical_power_rate_of_energy_transfer_definition", prompt, correct, sol, 2, "mcq",
        ["confusing_electrical_power_with_total_energy"],
        "Think about what a 'rate' always compares a physical quantity against.",
        "Power measures how fast electrical energy is supplied per second (E / t).",
        correct,
        options=options,
    )


def arch_02_watt_definition_one_joule_per_second_meaning(rng: random.Random) -> Dict[str, Any]:
    app, watts = rng.choice([
        ("electric frying pan", 1400),
        ("pedestal cooling fan", 120),
        ("toaster", 700),
        ("electric beater", 175),
        ("electric urn", 1500),
        ("flat-screen television", 54),
        ("steam iron", 1600),
    ])
    prompt = (
        f"A household **{app}** has a power rating of **${watts}\\text{{ W}}$**.\n\n"
        "1. State what **1 watt ($1\\text{ W}$)** represents in terms of joules and seconds [1].\n"
        f"2. Explain what a rating of **${watts}\\text{{ W}}$** tells you about the energy conversion of this {app} every second [1]."
    )
    correct = f"1 W = 1 joule of electrical energy transferred per second (1 J/s); The {app} converts {watts} J of electrical energy every second."
    sol = (
        "**Step 1:** By definition, $1\\text{ W} = 1\\text{ J/s}$ ($1\\text{ joule}$ of energy transferred per $1\\text{ second}$) [1].\n\n"
        f"**Step 2:** Therefore, a rating of ${watts}\\text{{ W}}$ means the {app} supplies and converts **${watts}\\text{{ J}}$ of electrical energy every second** [1]."
    )
    return _q(
        rng, "02", "02_watt_definition_one_joule_per_second_meaning", prompt, correct, sol, 2, "short_answer",
        ["thinking_watt_measures_voltage_instead_of_joules_per_second"],
        "Recall the fundamental unit equation: 1 W = 1 ? / 1 ?.",
        f"1 W = 1 J/s, so {watts} W equals {watts} Joules every second.",
        correct,
    )


def arch_03_calculating_power_p_equals_e_over_t_joules_seconds(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("desktop fan", 180000, 1800),
        ("laboratory hotplate", 450000, 300),
        ("electric kettle", 360000, 180),
        ("hair dryer", 270000, 150),
        ("microwave oven", 120000, 100),
        ("study lamp", 14400, 360),
        ("blender", 90000, 150),
    ]
    app, e_j, t_s = rng.choice(scenarios)
    p_w = e_j // t_s
    prompt = (
        f"A **{app}** transfers **${_fmt_int(e_j)}\\text{{ J}}$** of electrical energy during **${_fmt_int(t_s)}\\text{{ s}}$** of continuous operation.\n\n"
        "Use the formula $P = \\frac{E}{t}$ to calculate the **electrical power ($P$)** of the appliance in watts ($\\text{W}$) [3]."
    )
    correct = f"{p_w} W"
    sol = (
        "**Step 1 — Formula:**\n"
        "$$P = \\frac{E}{t}$$ [1]\n\n"
        "**Step 2 — Substitution:**\n"
        f"$$P = \\frac{{{_fmt_int(e_j)}\\text{{ J}}}}{{{_fmt_int(t_s)}\\text{{ s}}}}$$ [1]\n\n"
        f"**Step 3 — Answer:**\n"
        f"$$P = {p_w}\\text{{ W}}$$ [1]"
    )
    return _q(
        rng, "03", "03_calculating_power_p_equals_e_over_t_joules_seconds", prompt, correct, sol, 3, "calculation",
        ["multiplying_energy_by_time_instead_of_dividing"],
        "Divide total energy in Joules by time in seconds: P = E / t.",
        f"P = {e_j} / {t_s}.",
        correct,
    )


def arch_04_calculating_power_converting_kilojoules_and_minutes(rng: random.Random) -> Dict[str, Any]:
    app, e_kj, mins = rng.choice([
        ("toaster", 108, 2),
        ("sandwich press", 180, 3),
        ("electric kettle", 360, 3),
        ("microwave oven", 216, 3),
        ("steam iron", 288, 4),
        ("hair dryer", 300, 4),
        ("coffee percolator", 240, 5),
    ])
    e_j = e_kj * 1000
    t_s = mins * 60
    p_w = e_j // t_s
    prompt = (
        f"During a practical task, a **{app}** uses **${e_kj}\\text{{ kJ}}$** of electrical energy in **${mins}\\text{{ minutes}}$**.\n\n"
        "Convert both quantities to standard SI units ($\\text{J}$ and $\\text{s}$) and calculate the **power rating ($P$)** in watts [4]."
    )
    correct = f"{p_w} W"
    sol = (
        "**Step 1 — Convert kilojoules to joules:**\n"
        f"$$E = {e_kj}\\text{{ kJ}} \\times 1\\,000 = {_fmt_int(e_j)}\\text{{ J}}$$ [1]\n\n"
        "**Step 2 — Convert minutes to seconds:**\n"
        f"$$t = {mins}\\text{{ min}} \\times 60 = {t_s}\\text{{ s}}$$ [1]\n\n"
        "**Step 3 — Calculate power:**\n"
        f"$$P = \\frac{{E}}{{t}} = \\frac{{{_fmt_int(e_j)}}}{{{t_s}}} = {p_w}\\text{{ W}}$$ [2]"
    )
    return _q(
        rng, "04", "04_calculating_power_converting_kilojoules_and_minutes", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_convert_kj_to_joules_or_minutes_to_seconds"],
        "Power in Watts requires Energy in Joules (multiply kJ by 1 000) and Time in seconds (multiply minutes by 60).",
        f"E = {e_j} J; t = {t_s} s; P = E / t.",
        correct,
    )


def arch_05_calculating_energy_in_joules_from_power_and_time(rng: random.Random) -> Dict[str, Any]:
    app, watts, secs = rng.choice([
        ("microwave oven", 1000, 60),
        ("electric kettle", 2000, 90),
        ("toaster", 800, 120),
        ("steam iron", 1500, 40),
        ("hair dryer", 1200, 75),
        ("hand blender", 350, 80),
        ("LED spotlight", 25, 240),
    ])
    e_j = watts * secs
    e_kj = e_j / 1000.0
    prompt = (
        f"A **${watts}\\text{{ W}}$ {app}** operates steadily for **${secs}\\text{{ s}}$**.\n\n"
        "Calculate the total electrical energy transferred in **joules ($\\text{J}$)** and express your final answer in **kilojoules ($\\text{kJ}$)** as well [3]."
    )
    correct = f"{_fmt_int(e_j)} J ({_fmt_num(e_kj, 2)} kJ)"
    sol = (
        "**Step 1 — Rearrange $P = \\frac{E}{t}$:**\n"
        "$$E = P \\times t$$ [1]\n\n"
        "**Step 2 — Calculate Energy in Joules:**\n"
        f"$$E = {watts}\\text{{ W}} \\times {secs}\\text{{ s}} = {_fmt_int(e_j)}\\text{{ J}}$$ [1]\n\n"
        "**Step 3 — Convert to Kilojoules:**\n"
        f"$$E = \\frac{{{_fmt_int(e_j)}}}{{1\\,000}} = {_fmt_tex(e_kj, 2)}\\text{{ kJ}}$$ [1]"
    )
    return _q(
        rng, "05", "05_calculating_energy_in_joules_from_power_and_time", prompt, correct, sol, 3, "calculation",
        ["dividing_power_by_time_to_find_energy"],
        "Multiply power in Watts by time in seconds: E = P x t.",
        f"E = {watts} x {secs} = {e_j} J; divide by 1 000 for kJ.",
        correct,
    )


def arch_06_calculating_time_duration_from_energy_and_power(rng: random.Random) -> Dict[str, Any]:
    app, watts, e_kj = rng.choice([
        ("electric kettle", 2000, 240),
        ("toaster", 800, 96),
        ("microwave", 1200, 144),
        ("fan heater", 1500, 270),
        ("electric pan", 1400, 210),
        ("vacuum cleaner", 1600, 240),
    ])
    e_j = e_kj * 1000
    t_s = e_j // watts
    t_min = t_s / 60.0
    prompt = (
        f"An **{app}** rated at **${watts}\\text{{ W}}$** transfers **${e_kj}\\text{{ kJ}}$** of electrical energy while heating.\n\n"
        "Calculate for how many **seconds** (and **minutes**) the appliance was switched on [4]."
    )
    correct = f"{t_s} s ({_fmt_num(t_min, 2)} min)"
    sol = (
        "**Step 1 — Convert energy to Joules:**\n"
        f"$$E = {e_kj} \\times 1\\,000 = {_fmt_int(e_j)}\\text{{ J}}$$ [1]\n\n"
        "**Step 2 — Rearrange $P = \\frac{E}{t}$ for $t$:**\n"
        "$$t = \\frac{E}{P}$$ [1]\n\n"
        "**Step 3 — Substitute and solve:**\n"
        f"$$t = \\frac{{{_fmt_int(e_j)}}}{{{watts}}} = {t_s}\\text{{ s}}$$ [1]\n\n"
        f"**Step 4 — Express in minutes:**\n"
        f"$$t = \\frac{{{t_s}}}{{60}} = {_fmt_tex(t_min, 2)}\\text{{ min}}$$ [1]"
    )
    return _q(
        rng, "06", "06_calculating_time_duration_from_energy_and_power", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_convert_kj_before_dividing_by_watts"],
        "First convert kJ to J, then rearrange P = E / t to get t = E / P.",
        f"t = ({e_kj} x 1 000) / {watts} = {t_s} s.",
        correct,
    )


def arch_07_converting_between_joules_and_kilojoules(rng: random.Random) -> Dict[str, Any]:
    j_vals = [rng.choice([120, 145, 250, 480, 750]), rng.choice([1230, 1650, 2450, 3890, 4120])]
    kj_vals = [rng.choice([34, 48, 65, 134]), rng.choice([24.6, 32.12, 18.4, 15.75])]
    ans_1 = j_vals[0] / 1000.0
    ans_2 = int(round(kj_vals[0] * 1000))
    ans_3 = j_vals[1] / 1000.0
    ans_4 = int(round(kj_vals[1] * 1000))
    prompt = (
        "Perform the following standard metric energy conversions ($1\\text{ kJ} = 1\\,000\\text{ J}$):\n\n"
        f"1. Convert **${j_vals[0]}\\text{{ J}}$** to kilojoules ($\\text{{kJ}}$) [1].\n"
        f"2. Convert **${kj_vals[0]}\\text{{ kJ}}$** to joules ($\\text{{J}}$) [1].\n"
        f"3. Convert **${_fmt_int(j_vals[1])}\\text{{ J}}$** to kilojoules ($\\text{{kJ}}$) [1].\n"
        f"4. Convert **${_fmt_tex(kj_vals[1], 2)}\\text{{ kJ}}$** to joules ($\\text{{J}}$) [1]."
    )
    correct = f"1) {_fmt_num(ans_1, 3)} kJ; 2) {_fmt_int(ans_2)} J; 3) {_fmt_num(ans_3, 3)} kJ; 4) {_fmt_int(ans_4)} J"
    sol = (
        "**Rule:** To convert $\\text{J} \\to \\text{kJ}$, divide by $1\\,000$. To convert $\\text{kJ} \\to \\text{J}$, multiply by $1\\,000$.\n\n"
        f"1. $\\frac{{{j_vals[0]}}}{{1\\,000}} = {_fmt_tex(ans_1, 3)}\\text{{ kJ}}$ [1]\n"
        f"2. ${kj_vals[0]} \\times 1\\,000 = {_fmt_int(ans_2)}\\text{{ J}}$ [1]\n"
        f"3. $\\frac{{{_fmt_int(j_vals[1])}}}{{1\\,000}} = {_fmt_tex(ans_3, 3)}\\text{{ kJ}}$ [1]\n"
        f"4. ${_fmt_tex(kj_vals[1], 2)} \\times 1\\,000 = {_fmt_int(ans_4)}\\text{{ J}}$ [1]"
    )
    return _q(
        rng, "07", "07_converting_between_joules_and_kilojoules", prompt, correct, sol, 4, "calculation",
        ["multiplying_instead_of_dividing_by_1000_j_to_kj"],
        "Remember: 'kilo' always means 1 000. Moving from smaller units (J) to larger units (kJ) means dividing.",
        "Divide J by 1 000 -> kJ; Multiply kJ by 1 000 -> J.",
        correct,
    )


def arch_08_converting_watts_to_kilowatts_divide_by_1000(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice([1760, 1850, 2200, 2400, 1450])
    w2 = rng.choice([25, 32, 48, 60, 85])
    w3 = rng.choice([485, 560, 750, 920])
    k1, k2, k3 = w1 / 1000.0, w2 / 1000.0, w3 / 1000.0
    prompt = (
        "Before calculating household electricity costs in $\\text{kWh}$, power ratings must be converted from watts ($\\text{W}$) to kilowatts ($\\text{kW}$).\n\n"
        "Convert each power rating into **kilowatts ($\\text{kW}$)**:\n"
        f"1. **${_fmt_int(w1)}\\text{{ W}}$** (electric kettle) [1]\n"
        f"2. **${w2}\\text{{ W}}$** (pedestal fan / LED array) [1]\n"
        f"3. **${w3}\\text{{ W}}$** (microwave / blender) [1]"
    )
    correct = f"1) {_fmt_num(k1, 3)} kW; 2) {_fmt_num(k2, 3)} kW; 3) {_fmt_num(k3, 3)} kW"
    sol = (
        "**Rule:** $P(\\text{kW}) = \\frac{P(\\text{W})}{1\\,000}$\n\n"
        f"1. $\\frac{{{_fmt_int(w1)}}}{{1\\,000}} = {_fmt_tex(k1, 3)}\\text{{ kW}}$ [1]\n"
        f"2. $\\frac{{{w2}}}{{1\\,000}} = {_fmt_tex(k2, 3)}\\text{{ kW}}$ [1]\n"
        f"3. $\\frac{{{w3}}}{{1\\,000}} = {_fmt_tex(k3, 3)}\\text{{ kW}}$ [1]"
    )
    return _q(
        rng, "08", "08_converting_watts_to_kilowatts_divide_by_1000", prompt, correct, sol, 3, "calculation",
        ["dividing_watts_by_100_instead_of_1000"],
        "1 kilowatt = 1 000 watts, so shift the decimal comma three places to the left.",
        f"{w1}/1000={_fmt_num(k1, 3)}; {w2}/1000={_fmt_num(k2, 3)}; {w3}/1000={_fmt_num(k3, 3)}.",
        correct,
    )


def arch_09_converting_kilowatts_to_watts_multiply_by_1000(rng: random.Random) -> Dict[str, Any]:
    kw1 = rng.choice([3.79, 4.56, 2.85, 3.25, 1.95])
    kw2 = rng.choice([0.56, 0.75, 0.42, 0.085, 0.125])
    w1 = int(round(kw1 * 1000))
    w2 = int(round(kw2 * 1000))
    prompt = (
        "An electrician inspects two industrial specification sheets where appliance power is listed in **kilowatts ($\\text{kW}$)**.\n\n"
        f"Convert **${_fmt_tex(kw1, 2)}\\text{{ kW}}$** and **${_fmt_tex(kw2, 3)}\\text{{ kW}}$** back into **watts ($\\text{{W}}$)** [2]."
    )
    correct = f"{_fmt_int(w1)} W and {w2} W"
    sol = (
        "**Rule:** $P(\\text{W}) = P(\\text{kW}) \\times 1\\,000$\n\n"
        f"1. ${_fmt_tex(kw1, 2)}\\text{{ kW}} \\times 1\\,000 = {_fmt_int(w1)}\\text{{ W}}$ [1]\n"
        f"2. ${_fmt_tex(kw2, 3)}\\text{{ kW}} \\times 1\\,000 = {w2}\\text{{ W}}$ [1]"
    )
    return _q(
        rng, "09", "09_converting_kilowatts_to_watts_multiply_by_1000", prompt, correct, sol, 2, "calculation",
        ["dividing_kw_by_1000_instead_of_multiplying"],
        "Kilowatts are larger than watts (1 kW = 1 000 W). Multiply by 1 000.",
        f"{_fmt_num(kw1, 2)} x 1 000 = {w1} W; {_fmt_num(kw2, 3)} x 1 000 = {w2} W.",
        correct,
    )


def arch_10_interpreting_appliance_rating_plate_voltage_power(rng: random.Random) -> Dict[str, Any]:
    brand = rng.choice(["KalahariHome", "KarooTech", "HighveldPro", "CapeHeat", "SavannaElec"])
    app, watts = rng.choice([
        ("Electric Kettle", 2200),
        ("Stainless Urn", 1500),
        ("Steam Iron", 1800),
        ("Electric Pan", 1400),
        ("Air Fryer", 1650),
        ("Toaster", 850),
    ])
    model = f"KH-{rng.randint(210, 980)}"
    kw = watts / 1000.0
    d_spec = _svg_rating_plate(rng, brand, app, model, watts, 50)
    prompt = (
        f"Study the manufacturer rating plate shown in the diagram below for a domestic **{app}**.\n\n"
        "1. Identify the rated electrical power in **watts** and convert it to **kilowatts ($\\text{kW}$)** [2].\n"
        "2. Explain why manufacturers are required to print this power rating clearly on every appliance [1]."
    )
    correct = f"{watts} W ({_fmt_num(kw, 2)} kW); It informs consumers of the rate of energy consumption and helps calculate running costs and safe circuit loading."
    sol = (
        f"**Step 1:** From the rating plate, the power rating is **${watts}\\text{{ W}}$**.\n"
        f"$$P(\\text{{kW}}) = \\frac{{{watts}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [2]\n\n"
        "**Step 2:** Manufacturers print power ratings on labels so consumers know how rapidly the device draws electrical energy, can estimate electricity costs, and avoid overloading household sockets [1]."
    )
    return _q(
        rng, "10", "10_interpreting_appliance_rating_plate_voltage_power", prompt, correct, sol, 3, "short_answer",
        ["confusing_230v_voltage_rating_with_power_rating"],
        "Look for the number stamped next to the unit W (watts), not V (volts) or Hz (hertz).",
        f"Power = {watts} W = {_fmt_num(kw, 2)} kW.",
        correct,
        diagram_spec=d_spec,
    )


def arch_11_comparing_energy_transfer_rates_joules_per_second(rng: random.Random) -> Dict[str, Any]:
    high_app, high_j = rng.choice([
        ("electric stove plate", 3600),
        ("electric geyser", 3000),
        ("industrial urn", 2500),
        ("bar heater", 2400),
    ])
    low_app, low_j = rng.choice([
        ("microwave oven", 1200),
        ("toaster", 700),
        ("pedestal fan", 120),
        ("television", 90),
    ])
    diff_ratio = round(high_j / float(low_j), 1)
    prompt = (
        f"An **{high_app}** transfers **${_fmt_int(high_j)}\\text{{ J/s}}$**, while a **{low_app}** transfers **${_fmt_int(low_j)}\\text{{ J/s}}$**.\n\n"
        "Which appliance draws electrical power at a higher rate, and why?"
    )
    correct = f"The {high_app} uses more power ({high_j} W vs {low_j} W) because it transfers {_fmt_num(diff_ratio, 1)} times more joules of electrical energy every second."
    options = [
        correct,
        f"The {low_app} uses more power because smaller J/s numbers mean electrons move faster.",
        "Both appliances have identical power ratings because both plug into a 230 V South African wall socket.",
        f"The {high_app} has lower power because it loses zero joules per second as heat.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** $1\\text{{ J/s}} = 1\\text{{ W}}$, so the {high_app} is rated at ${high_j}\\text{{ W}}$ and the {low_app} at ${low_j}\\text{{ W}}$.\n\n"
        f"**Step 2:** Since ${high_j} > {low_j}$, the {high_app} transfers more energy per second (by a factor of ${_fmt_tex(diff_ratio, 1)}$).\n\n"
        f"**Conclusion:** {correct}"
    )
    return _q(
        rng, "11", "11_comparing_energy_transfer_rates_joules_per_second", prompt, correct, sol, 2, "mcq",
        ["believing_all_230v_appliances_consume_identical_power"],
        "1 J/s equals 1 Watt. Compare the energy transferred in a single second.",
        f"{high_j} J/s ({high_j} W) > {low_j} J/s ({low_j} W).",
        correct,
        options=options,
    )


def arch_12_reading_appliance_power_rating_bar_chart(rng: random.Random) -> Dict[str, Any]:
    urn_w = rng.choice([1500, 1800, 2000, 2200])
    toast_w = rng.choice([700, 850, 950])
    beat_w = rng.choice([175, 220, 300])
    tv_w = rng.choice([54, 75, 95])
    items = [("Toaster", toast_w), ("Beater", beat_w), ("TV", tv_w), ("Urn", urn_w)]
    rng.shuffle(items)
    d_spec = _svg_power_bar_chart(rng, items, "Measured Power Ratings of Four Kitchen & Lounge Appliances")
    diff_w = urn_w - tv_w
    prompt = (
        "The bar graph below displays the power ratings recorded during a home electricity audit.\n\n"
        "1. Identify which appliance has the **highest** power rating and which has the **lowest** power rating [2].\n"
        "2. Calculate the difference in power rating (in $\\text{W}$ and $\\text{kW}$) between the highest-rated and lowest-rated appliances [2]."
    )
    correct = f"Highest: Urn ({urn_w} W); Lowest: TV ({tv_w} W); Difference: {diff_w} W ({_fmt_num(diff_w / 1000.0, 3)} kW)"
    sol = (
        f"**Step 1:** Reading the bars on the graph: Highest = **Urn (${urn_w}\\text{{ W}}$)**; Lowest = **TV (${tv_w}\\text{{ W}}$)** [2].\n\n"
        f"**Step 2:** Difference $= {urn_w}\\text{{ W}} - {tv_w}\\text{{ W}} = {diff_w}\\text{{ W}}$ [1].\n\n"
        f"**Step 3:** Convert to kW: $\\frac{{{diff_w}}}{{1\\,000}} = {_fmt_tex(diff_w / 1000.0, 3)}\\text{{ kW}}$ [1]."
    )
    return _q(
        rng, "12", "12_reading_appliance_power_rating_bar_chart", prompt, correct, sol, 4, "short_answer",
        ["misreading_bar_chart_scales_or_forgetting_kw_conversion"],
        "Compare the tallest and shortest bars on the power graph, then subtract and divide by 1 000.",
        f"Urn ({urn_w} W) - TV ({tv_w} W) = {diff_w} W.",
        correct,
        diagram_spec=d_spec,
    )


def arch_13_heating_vs_non_heating_appliance_power_demand(rng: random.Random) -> Dict[str, Any]:
    heat_pair = rng.choice([
        ("electric geyser and electric kettle", "cooling fan and transistor radio"),
        ("steam iron and toaster", "LED television and laptop charger"),
        ("electric stove plate and oil heater", "desktop monitor and ceiling fan"),
        ("electric frying pan and hair dryer", "Wi-Fi router and bedside lamp"),
    ])
    hi_devs, lo_devs = heat_pair
    prompt = (
        f"When auditing domestic appliances, a learner compares **{hi_devs}** against **{lo_devs}**.\n\n"
        "Which generalisation correctly explains the huge difference in power ratings between these two groups?"
    )
    correct = f"Heating appliances ({hi_devs}) require very high power (often 1 000–3 500 W) because generating thermal energy via resistive elements demands rapid energy transfer, whereas {lo_devs} use much less power for sound, light, or light rotation."
    options = [
        correct,
        f"Appliances producing sound or light ({lo_devs}) always draw more watts than heating appliances.",
        f"Heating appliances ({hi_devs}) consume fewer watts because heat is created out of empty space.",
        "Only appliances with plastic casings have power ratings above 1 000 W.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Converting electrical energy into large amounts of thermal energy (boiling water, baking, ironing) requires high current through resistive heating elements.\n\n"
        f"**Step 2:** Therefore, **{hi_devs}** typically operate at $700\\text{{ W}} - 3\\,600\\text{{ W}}$, whereas **{lo_devs}** typically draw $10\\text{{ W}} - 150\\text{{ W}}$."
    )
    return _q(
        rng, "13", "13_heating_vs_non_heating_appliance_power_demand", prompt, correct, sol, 2, "mcq",
        ["assuming_televisions_use_more_power_than_kettles"],
        "Ask yourself: does boiling/heating require far more energy per second than spinning a small fan or displaying a picture?",
        f"Thermal heating appliances ({hi_devs}) have the highest power ratings.",
        correct,
        options=options,
    )


def arch_14_sequencing_appliances_highest_to_lowest_power(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Oven", rng.choice([3400, 3600])),
        ("Kettle", rng.choice([2000, 2200])),
        ("Iron", rng.choice([1500, 1600])),
        ("Toaster", rng.choice([700, 850])),
        ("Fridge", rng.choice([220, 280])),
        ("Fan", rng.choice([85, 120])),
        ("LED Bulb", rng.choice([8, 12])),
    ]
    chosen = rng.sample(pool, 5)
    rng.shuffle(chosen)
    d_spec = _svg_power_bar_chart(rng, chosen, "Appliance Power Ratings for Sequencing")
    sorted_desc = sorted(chosen, key=lambda x: x[1], reverse=True)
    seq_str = " > ".join(f"{name} ({w} W)" for name, w in sorted_desc)
    prompt = (
        "Examine the power ratings displayed in the chart below.\n\n"
        "1. Sequence all five appliances from **highest power consumption to lowest power consumption** [2].\n"
        "2. State what the top two appliances in your sequence have in common functionally [1]."
    )
    correct = f"{seq_str}; Both use heating elements to convert electrical energy into thermal energy."
    sol = (
        "**Step 1 — Order from highest to lowest wattage:**\n"
        f"{seq_str} [2]\n\n"
        "**Step 2 — Common feature:** The highest-power appliances convert electrical energy into **heat** using resistive heating elements [1]."
    )
    return _q(
        rng, "14", "14_sequencing_appliances_highest_to_lowest_power", prompt, correct, sol, 3, "short_answer",
        ["sequencing_appliances_ascending_instead_of_descending"],
        "Check the prompt carefully: highest power comes first, lowest comes last.",
        seq_str,
        correct,
        diagram_spec=d_spec,
    )


def arch_15_estimating_typical_household_appliance_wattages(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("a conventional electric geyser", "3 000 W to 4 800 W", ["9 W to 15 W", "50 W to 80 W", "120 W to 180 W"]),
        ("a domestic LED light globe", "8 W to 12 W", ["1 500 W to 2 200 W", "3 500 W to 6 000 W", "700 W to 900 W"]),
        ("a household microwave oven", "1 000 W to 1 400 W", ["5 W to 12 W", "40 W to 60 W", "12 000 W to 15 000 W"]),
        ("a domestic electric kettle", "1 800 W to 2 400 W", ["15 W to 25 W", "90 W to 120 W", "20 000 W to 30 000 W"]),
        ("a ceiling or desk cooling fan", "50 W to 120 W", ["2 500 W to 3 500 W", "5 000 W to 6 000 W", "0,5 W to 1 W"]),
    ])
    app, ans, wrongs = case
    options = [ans] + wrongs
    rng.shuffle(options)
    prompt = (
        f"Based on typical South African domestic appliance specifications, which power rating range is most realistic for **{app}**?"
    )
    sol = (
        f"**Analysis:** In household audits, **{app}** operates in the **{ans}** power range."
    )
    return _q(
        rng, "15", "15_estimating_typical_household_appliance_wattages", prompt, ans, sol, 2, "mcq",
        ["unrealistic_wattage_order_of_magnitude_estimate"],
        "Remember: LEDs ~10 W, fans/TVs ~50-150 W, microwaves ~1 200 W, kettles/geysers ~2 000-4 800 W.",
        f"Realistic range for {app}: {ans}.",
        ans,
        options=options,
    )


def arch_16_why_electricity_utilities_bill_in_kwh_not_joules(rng: random.Random) -> Dict[str, Any]:
    kwh_ex = rng.choice([250, 320, 450, 600, 780])
    j_ex = kwh_ex * 3_600_000
    city = rng.choice(["Johannesburg (City Power)", "Cape Town", "Durban (eThekwini)", "Tshwane", "Eskom Direct"])
    prompt = (
        f"A household supplied by **{city}** consumes **${kwh_ex}\\text{{ kWh}}$** in one month (equivalent to **${_fmt_int(j_ex)}\\text{{ J}}$**).\n\n"
        "Explain why electricity suppliers measure and bill domestic energy consumption in **kilowatt-hours ($\\text{kWh}$)** rather than in standard SI **joules ($\\text{J}$)** [2]."
    )
    correct = "The joule is a tiny unit of energy for household consumption, resulting in impractically huge multi-million or billion-digit numbers; the kilowatt-hour is a much larger, practical commercial unit."
    sol = (
        "**Step 1:** $1\\text{ J}$ is a tiny quantity of energy (running a $1\\,000\\text{ W}$ microwave for 1 hour uses $3\\,600\\,000\\text{ J}$) [1].\n\n"
        f"**Step 2:** Billing a home for ${_fmt_int(j_ex)}\\text{{ J}}$ creates unwieldy, error-prone nine- or ten-digit numbers, whereas **${kwh_ex}\\text{{ kWh}}$** is compact and practical for metering and billing [1]."
    )
    return _q(
        rng, "16", "16_why_electricity_utilities_bill_in_kwh_not_joules", prompt, correct, sol, 2, "short_answer",
        ["thinking_kwh_is_a_unit_of_power_instead_of_energy"],
        "Look at the huge number of joules compared to the compact kWh value.",
        "Joules produce unwieldy multi-million/billion numbers; kWh is practical for household billing.",
        correct,
    )


def arch_17_kilowatt_hour_definition_1kw_for_1_hour(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("1 000 W", "1 hour"),
        ("2 000 W", "30 minutes (0,5 hour)"),
        ("500 W", "2 hours"),
        ("250 W", "4 hours"),
        ("4 000 W", "15 minutes (0,25 hour)"),
    ])
    p_str, t_str = scenario
    prompt = (
        "An electricity meter records **$1\\text{ unit}$**, which equals **$1\\text{ kilowatt-hour (1 kWh)}$** of electrical energy.\n\n"
        f"Which definition of **$1\\text{{ kWh}}$** is scientifically accurate (for example, running a {p_str} appliance for {t_str})?"
    )
    correct = "1 kWh is the total electrical energy transferred when an appliance with a power rating of 1 kW (1 000 W) operates continuously for 1 hour."
    options = [
        correct,
        "1 kWh is the power rating of a 1 000 W appliance divided by 1 hour of operation.",
        "1 kWh is the current of 1 ampere flowing through a circuit in 1 hour.",
        "1 kWh equals exactly 1 000 joules of electrical energy.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** $E = P(\\text{kW}) \\times t(\\text{h})$.\n\n"
        "**Step 2:** $1\\text{ kWh} = 1\\text{ kW} \\times 1\\text{ h} = 1\\,000\\text{ W} \\times 1\\text{ h}$. Notice that multiplying $\\text{kW}$ by $\\text{h}$ gives **energy**, not power.\n\n"
        f"**Conclusion:** {correct}"
    )
    return _q(
        rng, "17", "17_kilowatt_hour_definition_1kw_for_1_hour", prompt, correct, sol, 2, "mcq",
        ["reading_kwh_as_kilowatts_per_hour_dividing_instead_of_multiplying"],
        "Notice there is NO 'per' in kilowatt-hour: it is kW multiplied by hours.",
        "Energy used by a 1 kW (1 000 W) appliance running for 1 hour.",
        correct,
        options=options,
    )


def arch_18_converting_kwh_to_joules_and_megajoules(rng: random.Random) -> Dict[str, Any]:
    kwh = rng.choice([1, 2, 2.5, 3, 4, 5, 7.5, 10])
    j_val = int(round(kwh * 3_600_000))
    mj_val = kwh * 3.6
    prompt = (
        f"Show step-by-step how to convert **${_fmt_tex(kwh, 1)}\\text{{ kWh}}$** into standard SI **joules ($\\text{{J}}$)** and **megajoules ($\\text{{MJ}}$)** [3].\n"
        "*(Recall: $1\\text{ kW} = 1\\,000\\text{ J/s}$ and $1\\text{ hour} = 3\\,600\\text{ s}$.)*"
    )
    correct = f"{_fmt_int(j_val)} J ({_fmt_num(mj_val, 2)} MJ)"
    sol = (
        "**Step 1 — Convert $1\\text{ kWh}$ to Joules:**\n"
        "$$1\\text{ kWh} = 1\\,000\\text{ J/s} \\times 3\\,600\\text{ s} = 3\\,600\\,000\\text{ J} = 3{,}6\\text{ MJ}$$ [1]\n\n"
        f"**Step 2 — Scale by ${_fmt_tex(kwh, 1)}\\text{{ kWh}}$:**\n"
        f"$$E = {_fmt_tex(kwh, 1)} \\times 3\\,600\\,000\\text{{ J}} = {_fmt_int(j_val)}\\text{{ J}}$$ [1]\n\n"
        f"**Step 3 — Express in megajoules ($1\\text{{ MJ}} = 1\\,000\\,000\\text{{ J}}$):**\n"
        f"$$E = {_fmt_tex(mj_val, 2)}\\text{{ MJ}}$$ [1]"
    )
    return _q(
        rng, "18", "18_converting_kwh_to_joules_and_megajoules", prompt, correct, sol, 3, "calculation",
        ["multiplying_1000_by_60_instead_of_3600_seconds_per_hour"],
        "1 hour = 60 x 60 = 3 600 seconds. Multiply 1 000 W by 3 600 s first.",
        f"{_fmt_num(kwh, 1)} x 3 600 000 J = {_fmt_int(j_val)} J ({_fmt_num(mj_val, 2)} MJ).",
        correct,
    )


def arch_19_converting_seconds_and_minutes_to_decimal_hours(rng: random.Random) -> Dict[str, Any]:
    mins = rng.choice([6, 12, 15, 18, 24, 36, 45, 90, 120])
    secs = mins * 60
    hrs = mins / 60.0
    d_spec = _svg_time_conversion_bar(mins)
    prompt = (
        f"An appliance runs for **${_fmt_int(secs)}\\text{{ seconds}}$** (which equals **${mins}\\text{{ minutes}}$**) illustrated in the duration bar below.\n\n"
        "Convert this operating duration into **decimal hours ($\\text{h}$)** so it can be substituted directly into $E = P \\times t$ [2]."
    )
    correct = f"{_fmt_num(hrs, 2)} h"
    sol = (
        "**Step 1 — Formula:**\n"
        "$$t(\\text{h}) = \\frac{t(\\text{min})}{60} = \\frac{t(\\text{s})}{3\\,600}$$ [1]\n\n"
        "**Step 2 — Calculation:**\n"
        f"$$t = \\frac{{{mins}}}{{60}} = {_fmt_tex(hrs, 2)}\\text{{ h}}$$ [1]"
    )
    return _q(
        rng, "19", "19_converting_seconds_and_minutes_to_decimal_hours", prompt, correct, sol, 2, "calculation",
        ["writing_minutes_as_decimals_directly_eg_15_min_as_0_15_h"],
        "There are 60 minutes in 1 hour, NOT 100 minutes! Divide minutes by 60.",
        f"{mins} / 60 = {_fmt_num(hrs, 2)} h.",
        correct,
        diagram_spec=d_spec,
    )


def arch_20_calculating_energy_in_watt_hours_and_kwh(rng: random.Random) -> Dict[str, Any]:
    app, watts, hrs = rng.choice([
        ("table lamp", 60, 3.5),
        ("security floodlight", 120, 4.0),
        ("pedestal fan", 80, 5.5),
        ("LED monitor", 45, 6.0),
        ("study radio", 30, 8.0),
        ("aquarium pump", 150, 12.0),
    ])
    wh = watts * hrs
    kwh = wh / 1000.0
    prompt = (
        f"A **${watts}\\text{{ W}}$ {app}** is left switched on for **${_fmt_tex(hrs, 1)}\\text{{ hours}}$**.\n\n"
        "1. Calculate the electrical energy consumed in **watt-hours ($\\text{Wh}$)** [2].\n"
        "2. Convert your answer into **kilowatt-hours ($\\text{kWh}$)** [1]."
    )
    correct = f"{_fmt_num(wh, 1)} Wh ({_fmt_num(kwh, 3)} kWh)"
    sol = (
        "**Step 1 — Energy in Watt-hours:**\n"
        f"$$E(\\text{{Wh}}) = {watts}\\text{{ W}} \\times {_fmt_tex(hrs, 1)}\\text{{ h}} = {_fmt_tex(wh, 1)}\\text{{ Wh}}$$ [2]\n\n"
        "**Step 2 — Convert Wh to kWh:**\n"
        f"$$E(\\text{{kWh}}) = \\frac{{{_fmt_tex(wh, 1)}}}{{1\\,000}} = {_fmt_tex(kwh, 3)}\\text{{ kWh}}$$ [1]"
    )
    return _q(
        rng, "20", "20_calculating_energy_in_watt_hours_and_kwh", prompt, correct, sol, 3, "calculation",
        ["forgetting_to_divide_watt_hours_by_1000_to_get_kwh"],
        "Multiply W x h to get Wh, then divide by 1 000 to get kWh.",
        f"{watts} x {_fmt_num(hrs, 1)} = {_fmt_num(wh, 1)} Wh = {_fmt_num(kwh, 3)} kWh.",
        correct,
    )


def arch_21_calculating_energy_kwh_watts_to_kw_conversion(rng: random.Random) -> Dict[str, Any]:
    app, watts, hrs = rng.choice([
        ("electric oven", 3600, 1.5),
        ("oil heater", 2000, 3.5),
        ("tumble dryer", 2500, 2.0),
        ("electric geyser", 3000, 4.0),
        ("air conditioner", 1800, 5.0),
        ("washing machine", 2200, 1.5),
        ("pool pump", 750, 6.0),
    ])
    kw = watts / 1000.0
    kwh = kw * hrs
    prompt = (
        f"An **{app}** with a power rating of **${_fmt_int(watts)}\\text{{ W}}$** operates for **${_fmt_tex(hrs, 1)}\\text{{ hours}}$**.\n\n"
        "1. Convert the power rating into **kilowatts ($\\text{kW}$)** [1].\n"
        "2. Calculate the **total energy consumption** in **kilowatt-hours ($\\text{kWh}$)** [2]."
    )
    correct = f"{_fmt_num(kwh, 2)} kWh (P = {_fmt_num(kw, 2)} kW)"
    sol = (
        "**Step 1 — Convert Watts to Kilowatts:**\n"
        f"$$P = \\frac{{{_fmt_int(watts)}\\text{{ W}}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [1]\n\n"
        "**Step 2 — Calculate Energy ($E = P \\times t$):**\n"
        f"$$E = {_fmt_tex(kw, 2)}\\text{{ kW}} \\times {_fmt_tex(hrs, 1)}\\text{{ h}} = {_fmt_tex(kwh, 2)}\\text{{ kWh}}$$ [2]"
    )
    return _q(
        rng, "21", "21_calculating_energy_kwh_watts_to_kw_conversion", prompt, correct, sol, 3, "calculation",
        ["multiplying_watts_directly_by_hours_and_calling_it_kwh"],
        "Never skip converting W to kW first: divide Watts by 1 000.",
        f"P = {_fmt_num(kw, 2)} kW; E = {_fmt_num(kw, 2)} x {_fmt_num(hrs, 1)} = {_fmt_num(kwh, 2)} kWh.",
        correct,
    )


def arch_22_short_duration_kettle_or_microwave_kwh_minutes(rng: random.Random) -> Dict[str, Any]:
    app, watts, mins = rng.choice([
        ("electric kettle", 2200, 6),
        ("microwave oven", 1360, 12),
        ("toaster", 900, 15),
        ("hair dryer", 1800, 10),
        ("vacuum cleaner", 1600, 30),
        ("steam iron", 1500, 24),
        ("blender", 600, 3),
    ])
    kw = watts / 1000.0
    hrs = mins / 60.0
    kwh = kw * hrs
    prompt = (
        f"A **{app}** rated at **${_fmt_int(watts)}\\text{{ W}}$** is switched on for **${mins}\\text{{ minutes}}$**.\n\n"
        "Convert the power to kilowatts and the time to hours, then calculate the electrical energy consumed in **$\\text{kWh}$** [4]."
    )
    correct = f"{_fmt_num(kwh, 4)} kWh"
    sol = (
        "**Step 1 — Convert Power to kW:**\n"
        f"$$P = \\frac{{{_fmt_int(watts)}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [1]\n\n"
        "**Step 2 — Convert Minutes to Hours:**\n"
        f"$$t = \\frac{{{mins}}}{{60}} = {_fmt_tex(hrs, 2)}\\text{{ h}}$$ [1]\n\n"
        "**Step 3 — Calculate Energy ($E = P \\times t$):**\n"
        f"$$E = {_fmt_tex(kw, 2)}\\text{{ kW}} \\times {_fmt_tex(hrs, 2)}\\text{{ h}} = {_fmt_tex(kwh, 4)}\\text{{ kWh}}$$ [2]"
    )
    return _q(
        rng, "22", "22_short_duration_kettle_or_microwave_kwh_minutes", prompt, correct, sol, 4, "calculation",
        ["multiplying_kw_by_minutes_instead_of_hours"],
        "Both conversions are needed: W -> kW (/1 000) and minutes -> hours (/60).",
        f"P = {_fmt_num(kw, 2)} kW, t = {_fmt_num(hrs, 2)} h, E = {_fmt_num(kwh, 4)} kWh.",
        correct,
    )


def arch_23_comparing_total_energy_consumed_power_vs_duration(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (("120 W Floodlight", 120, 2.0), ("60 W Study Lamp", 60, 3.5)),
        (("2 000 W Kettle", 2000, 0.15), ("150 W Fridge", 150, 4.0)),
        (("1 200 W Microwave", 1200, 0.25), ("100 W Television", 100, 5.0)),
        (("1 800 W Hair Dryer", 1800, 0.2), ("80 W Pedestal Fan", 80, 6.0)),
        (("1 500 W Steam Iron", 1500, 0.5), ("200 W Computer", 200, 4.5)),
    ]
    (n1, w1, h1), (n2, w2, h2) = rng.choice(pairs)
    e1 = (w1 / 1000.0) * h1
    e2 = (w2 / 1000.0) * h2
    winner = n1 if e1 > e2 else n2
    d_spec = _svg_dual_appliance_energy(n1, w1, h1, n2, w2, h2)
    prompt = (
        "Examine the energy comparison diagram below showing two appliances with different power ratings and run times:\n"
        f"- **Appliance 1:** {n1} running for ${_fmt_tex(h1, 2)}\\text{{ h}}$\n"
        f"- **Appliance 2:** {n2} running for ${_fmt_tex(h2, 2)}\\text{{ h}}$\n\n"
        "Calculate the energy consumed (in $\\text{kWh}$) by each appliance and determine which one consumes **more total electrical energy** [4]."
    )
    correct = f"{n1}: {_fmt_num(e1, 3)} kWh; {n2}: {_fmt_num(e2, 3)} kWh; {winner} consumes more energy."
    sol = (
        f"**Step 1 — Energy for {n1}:**\n"
        f"$$E_1 = {_fmt_tex(w1 / 1000.0, 3)}\\text{{ kW}} \\times {_fmt_tex(h1, 2)}\\text{{ h}} = {_fmt_tex(e1, 3)}\\text{{ kWh}}$$ [1]\n\n"
        f"**Step 2 — Energy for {n2}:**\n"
        f"$$E_2 = {_fmt_tex(w2 / 1000.0, 3)}\\text{{ kW}} \\times {_fmt_tex(h2, 2)}\\text{{ h}} = {_fmt_tex(e2, 3)}\\text{{ kWh}}$$ [1]\n\n"
        f"**Step 3 — Conclusion:** Since energy depends on both power AND time ($E = P \\times t$), the **{winner}** consumes more total electrical energy [2]."
    )
    return _q(
        rng, "23", "23_comparing_total_energy_consumed_power_vs_duration", prompt, correct, sol, 4, "calculation",
        ["assuming_higher_wattage_always_uses_more_total_energy_regardless_of_time"],
        "Total energy = Power x Time. A lower-power device run for many hours can beat a high-power device run briefly!",
        f"E1 = {_fmt_num(e1, 3)} kWh; E2 = {_fmt_num(e2, 3)} kWh; {winner} uses more.",
        correct,
        diagram_spec=d_spec,
    )


def arch_24_monthly_cumulative_energy_consumption_days_calculation(rng: random.Random) -> Dict[str, Any]:
    app, watts, hrs_day, days = rng.choice([
        ("electric heater", 1500, 3.0, 28),
        ("microwave oven", 1000, 1.0, 31),
        ("electric geyser", 3000, 4.0, 30),
        ("swimming pool pump", 750, 6.0, 30),
        ("security light array", 200, 10.0, 31),
        ("oil heater", 2000, 3.5, 28),
    ])
    kw = watts / 1000.0
    total_hrs = hrs_day * days
    total_kwh = kw * total_hrs
    prompt = (
        f"A family runs a **${_fmt_int(watts)}\\text{{ W}}$ {app}** for **${_fmt_tex(hrs_day, 1)}\\text{{ hours}}$ every day** across a **${days}\\text{{-day}}$ month**.\n\n"
        "1. Calculate the total number of operating hours for the month [1].\n"
        "2. Calculate the total monthly electrical energy consumed in **$\\text{kWh}$** [3]."
    )
    correct = f"{_fmt_num(total_hrs, 1)} hours; {_fmt_num(total_kwh, 2)} kWh"
    sol = (
        "**Step 1 — Total Monthly Hours:**\n"
        f"$$t = {_fmt_tex(hrs_day, 1)}\\text{{ h/day}} \\times {days}\\text{{ days}} = {_fmt_tex(total_hrs, 1)}\\text{{ hours}}$$ [1]\n\n"
        "**Step 2 — Convert Power to kW:**\n"
        f"$$P = \\frac{{{_fmt_int(watts)}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [1]\n\n"
        "**Step 3 — Total Energy Consumed:**\n"
        f"$$E = {_fmt_tex(kw, 2)}\\text{{ kW}} \\times {_fmt_tex(total_hrs, 1)}\\text{{ h}} = {_fmt_tex(total_kwh, 2)}\\text{{ kWh}}$$ [2]"
    )
    return _q(
        rng, "24", "24_monthly_cumulative_energy_consumption_days_calculation", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_multiply_daily_hours_by_days_in_month"],
        "Multiply daily hours by the number of days in the month before multiplying by kW.",
        f"Total hours = {_fmt_num(total_hrs, 1)} h; Energy = {_fmt_num(total_kwh, 2)} kWh.",
        correct,
    )


def arch_25_rearranging_kwh_formula_to_find_power_or_time(rng: random.Random) -> Dict[str, Any]:
    find_time = rng.choice([True, False])
    if find_time:
        app, watts, kwh = rng.choice([
            ("electric iron", 1600, 2.4),
            ("geyser", 3000, 10.5),
            ("fan heater", 2000, 7.0),
            ("dishwasher", 1800, 2.7),
            ("vacuum cleaner", 1500, 1.2),
        ])
        kw = watts / 1000.0
        hrs = kwh / kw
        mins = int(round(hrs * 60))
        prompt = (
            f"A **${_fmt_int(watts)}\\text{{ W}}$ {app}** consumes exactly **${_fmt_tex(kwh, 2)}\\text{{ kWh}}$** of electrical energy during a chore.\n\n"
            "Rearrange $E = P \\times t$ to calculate how long (in **hours** and **minutes**) the appliance was operated [3]."
        )
        correct = f"{_fmt_num(hrs, 2)} hours ({mins} minutes)"
        sol = (
            "**Step 1 — Convert Power to kW:**\n"
            f"$$P = \\frac{{{_fmt_int(watts)}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [1]\n\n"
            "**Step 2 — Rearrange $E = P \\times t$ for $t$:**\n"
            f"$$t = \\frac{{E}}{{P}} = \\frac{{{_fmt_tex(kwh, 2)}\\text{{ kWh}}}}{{{_fmt_tex(kw, 2)}\\text{{ kW}}}} = {_fmt_tex(hrs, 2)}\\text{{ h}}$$ [1]\n\n"
            f"**Step 3 — Convert to minutes:** ${_fmt_tex(hrs, 2)} \\times 60 = {mins}\\text{{ minutes}}$ [1]."
        )
        t1 = "Rearrange E = P x t to solve for time: t = E / P (using kW)."
        t2 = f"t = {_fmt_num(kwh, 2)} / {_fmt_num(kw, 2)} = {_fmt_num(hrs, 2)} hours."
    else:
        app, hrs, kwh = rng.choice([
            ("air conditioner", 4.0, 6.4),
            ("electric oven", 2.5, 9.0),
            ("pool pump", 5.0, 3.75),
            ("underfloor heater", 6.0, 10.8),
            ("tumble dryer", 2.0, 4.8),
        ])
        kw = kwh / hrs
        watts = int(round(kw * 1000))
        prompt = (
            f"An unknown **{app}** operates continuously for **${_fmt_tex(hrs, 1)}\\text{{ hours}}$** and uses **${_fmt_tex(kwh, 2)}\\text{{ kWh}}$** of electrical energy.\n\n"
            "Rearrange $E = P \\times t$ to determine the appliance's power rating in **kilowatts ($\\text{kW}$)** and **watts ($\\text{W}$)** [3]."
        )
        correct = f"{_fmt_num(kw, 2)} kW ({_fmt_int(watts)} W)"
        sol = (
            "**Step 1 — Rearrange $E = P \\times t$ for $P$:**\n"
            f"$$P = \\frac{{E}}{{t}} = \\frac{{{_fmt_tex(kwh, 2)}\\text{{ kWh}}}}{{{_fmt_tex(hrs, 1)}\\text{{ h}}}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [2]\n\n"
            f"**Step 2 — Convert kW to W:**\n"
            f"$$P = {_fmt_tex(kw, 2)} \\times 1\\,000 = {_fmt_int(watts)}\\text{{ W}}$$ [1]"
        )
        t1 = "Rearrange E = P x t to solve for power: P = E / t."
        t2 = f"P = {_fmt_num(kwh, 2)} / {_fmt_num(hrs, 1)} = {_fmt_num(kw, 2)} kW = {watts} W."

    return _q(
        rng, "25", "25_rearranging_kwh_formula_to_find_power_or_time", prompt, correct, sol, 3, "calculation",
        ["multiplying_kwh_by_kw_or_hours_instead_of_dividing"],
        t1, t2, correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_electrical_power_rate_of_energy_transfer_definition": arch_01_electrical_power_rate_of_energy_transfer_definition,
    "02_watt_definition_one_joule_per_second_meaning": arch_02_watt_definition_one_joule_per_second_meaning,
    "03_calculating_power_p_equals_e_over_t_joules_seconds": arch_03_calculating_power_p_equals_e_over_t_joules_seconds,
    "04_calculating_power_converting_kilojoules_and_minutes": arch_04_calculating_power_converting_kilojoules_and_minutes,
    "05_calculating_energy_in_joules_from_power_and_time": arch_05_calculating_energy_in_joules_from_power_and_time,
    "06_calculating_time_duration_from_energy_and_power": arch_06_calculating_time_duration_from_energy_and_power,
    "07_converting_between_joules_and_kilojoules": arch_07_converting_between_joules_and_kilojoules,
    "08_converting_watts_to_kilowatts_divide_by_1000": arch_08_converting_watts_to_kilowatts_divide_by_1000,
    "09_converting_kilowatts_to_watts_multiply_by_1000": arch_09_converting_kilowatts_to_watts_multiply_by_1000,
    "10_interpreting_appliance_rating_plate_voltage_power": arch_10_interpreting_appliance_rating_plate_voltage_power,
    "11_comparing_energy_transfer_rates_joules_per_second": arch_11_comparing_energy_transfer_rates_joules_per_second,
    "12_reading_appliance_power_rating_bar_chart": arch_12_reading_appliance_power_rating_bar_chart,
    "13_heating_vs_non_heating_appliance_power_demand": arch_13_heating_vs_non_heating_appliance_power_demand,
    "14_sequencing_appliances_highest_to_lowest_power": arch_14_sequencing_appliances_highest_to_lowest_power,
    "15_estimating_typical_household_appliance_wattages": arch_15_estimating_typical_household_appliance_wattages,
    "16_why_electricity_utilities_bill_in_kwh_not_joules": arch_16_why_electricity_utilities_bill_in_kwh_not_joules,
    "17_kilowatt_hour_definition_1kw_for_1_hour": arch_17_kilowatt_hour_definition_1kw_for_1_hour,
    "18_converting_kwh_to_joules_and_megajoules": arch_18_converting_kwh_to_joules_and_megajoules,
    "19_converting_seconds_and_minutes_to_decimal_hours": arch_19_converting_seconds_and_minutes_to_decimal_hours,
    "20_calculating_energy_in_watt_hours_and_kwh": arch_20_calculating_energy_in_watt_hours_and_kwh,
    "21_calculating_energy_kwh_watts_to_kw_conversion": arch_21_calculating_energy_kwh_watts_to_kw_conversion,
    "22_short_duration_kettle_or_microwave_kwh_minutes": arch_22_short_duration_kettle_or_microwave_kwh_minutes,
    "23_comparing_total_energy_consumed_power_vs_duration": arch_23_comparing_total_energy_consumed_power_vs_duration,
    "24_monthly_cumulative_energy_consumption_days_calculation": arch_24_monthly_cumulative_energy_consumption_days_calculation,
    "25_rearranging_kwh_formula_to_find_power_or_time": arch_25_rearranging_kwh_formula_to_find_power_or_time,
}
