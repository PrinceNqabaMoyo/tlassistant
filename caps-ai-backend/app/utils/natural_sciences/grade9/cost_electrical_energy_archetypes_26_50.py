"""Grade 9 Natural Sciences - Cost of Electrical Energy: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Cost of electrical energy.md.
Focus:
Domestic electricity meter readings, single-appliance & multi-appliance cost calculations,
cents to Rands conversions, Eskom/municipal inclining block (tiered) tariffs, VAT & fixed charges,
municipal bill auditing, prepaid electricity vouchers & longevity, reverse time/power problems,
thermostat cycling, incandescent vs CFL vs LED Sankey efficiency & cost payback,
mercury hazards & lifespan, geyser blankets & standby power savings, grid/carbon impact, and careers.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 2) -> str:
    """Format a number using South African comma notation, stripping trailing zeros."""
    s = f"{val:.{decimals}f}"
    if decimals > 0 and "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_fixed(val: float, decimals: int = 2) -> str:
    """Format a fixed-decimal number (e.g. Rands & cents) using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


def _fmt_tex(val: float, decimals: int = 2) -> str:
    """Format a number for KaTeX/LaTeX using South African {,} comma separator."""
    s = f"{val:.{decimals}f}"
    if decimals > 0 and "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_tex_fixed(val: float, decimals: int = 2) -> str:
    """Format a fixed-decimal currency/tariff number for KaTeX/LaTeX using {,}."""
    return f"{val:.{decimals}f}".replace(".", "{,}")


def _fmt_int(val: int) -> str:
    """Format integer with South African space thousands separator."""
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
    guide = f"Marking Guide ({marks} marks): Award credit for each verified calculation step, unit, and scientific reason shown in the solution."
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

def _svg_kwh_meter(meter_no: str, prev_kwh: int, curr_kwh: int) -> Dict[str, Any]:
    """Parameterized domestic digital kilowatt-hour meter readout."""
    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="30" y="18" width="370" height="154" rx="8" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
        f'<text x="215" y="42" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">MUNICIPAL kWh ELECTRICITY METER (#{meter_no})</text>'
        f'<rect x="52" y="56" width="150" height="62" rx="4" fill="#0f172a"/>'
        f'<text x="127" y="75" font-size="10" fill="#94a3b8" text-anchor="middle">PREVIOUS READING</text>'
        f'<text x="127" y="102" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle" font-family="monospace">{prev_kwh:05d} kWh</text>'
        f'<rect x="228" y="56" width="150" height="62" rx="4" fill="#0f172a"/>'
        f'<text x="303" y="75" font-size="10" fill="#94a3b8" text-anchor="middle">CURRENT READING</text>'
        f'<text x="303" y="102" font-size="18" font-weight="bold" fill="#4ade80" text-anchor="middle" font-family="monospace">{curr_kwh:05d} kWh</text>'
        f'<text x="215" y="148" font-size="11" fill="#334155" text-anchor="middle">230 V ~ 50 Hz | Class 1 Active Energy Meter</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_daily_energy_bars(items: List[tuple], title: str) -> Dict[str, Any]:
    """Parameterized bar chart of daily kWh consumption per appliance."""
    max_e = max(e for _, e in items)
    scale_max = max(4.0, float(int(max_e) + 2))
    palette = ["#2563eb", "#dc2626", "#16a34a", "#d97706", "#7c3aed"]
    n = len(items)
    slot = 340 // n
    bar_w = min(48, slot - 16)
    bars = []
    for i, (lbl, kwh) in enumerate(items):
        h = max(8, int((kwh / scale_max) * 114))
        x = 70 + i * slot + (slot - bar_w) // 2
        y = 158 - h
        bars.append(
            f'<rect x="{x}" y="{y}" width="{bar_w}" height="{h}" fill="{palette[i % len(palette)]}" stroke="#0f172a"/>'
            f'<text x="{x + bar_w // 2}" y="{y - 5}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{_fmt_num(kwh, 2)}</text>'
            f'<text x="{x + bar_w // 2}" y="175" font-size="9.5" fill="#1e293b" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="200" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="225" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>'
        f'<line x1="62" y1="34" x2="62" y2="158" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="62" y1="158" x2="418" y2="158" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="55" y="42" font-size="9.5" fill="#475569" text-anchor="end">{_fmt_num(scale_max, 0)}</text>'
        f'<text x="55" y="100" font-size="9.5" fill="#475569" text-anchor="end">{_fmt_num(scale_max / 2.0, 1)}</text>'
        f'<text x="55" y="160" font-size="9.5" fill="#475569" text-anchor="end">0</text>'
        f'<text x="18" y="96" font-size="10" fill="#0f172a" transform="rotate(-90 18 96)" text-anchor="middle">Daily Energy (kWh)</text>'
        f'{"".join(bars)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_block_tariff_steps(rates: List[tuple], usage_kwh: int) -> Dict[str, Any]:
    """Parameterized Eskom/municipal inclining block tariff step chart."""
    # rates: [(block_name, range_lbl, rate_c)]
    max_r = max(r for _, _, r in rates) + 30.0
    cols = ["#16a34a", "#2563eb", "#d97706", "#dc2626"]
    rects = []
    for i, (bname, rlbl, rate_c) in enumerate(rates):
        x = 68 + i * 86
        h = max(18, int((rate_c / max_r) * 110))
        y = 152 - h
        rects.append(
            f'<rect x="{x}" y="{y}" width="74" height="{h}" fill="{cols[i]}" fill-opacity="0.85" stroke="#0f172a"/>'
            f'<text x="{x + 37}" y="{y - 6}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{_fmt_fixed(rate_c, 2)} c</text>'
            f'<text x="{x + 37}" y="168" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{bname}</text>'
            f'<text x="{x + 37}" y="182" font-size="8.5" fill="#475569" text-anchor="middle">{rlbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Inclining Block Electricity Tariff (Household Usage: {usage_kwh} kWh)</text>'
        f'<line x1="56" y1="32" x2="56" y2="152" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="56" y1="152" x2="412" y2="152" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="20" y="96" font-size="10" fill="#0f172a" transform="rotate(-90 20 96)" text-anchor="middle">Tariff (c/kWh)</text>'
        f'{"".join(rects)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_municipal_statement(town: str, prev_r: int, curr_r: int, rate_r: float, fixed_r: float) -> Dict[str, Any]:
    """Parameterized municipal electricity statement box."""
    units = curr_r - prev_r
    svg = (
        f'<svg viewBox="0 0 430 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="24" y="16" width="382" height="184" rx="6" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="24" y="16" width="382" height="32" rx="6" fill="#1e3a8a"/>'
        f'<text x="215" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{town.upper()} MUNICIPAL ELECTRICITY ACCOUNT</text>'
        f'<text x="42" y="72" font-size="11" fill="#0f172a">Previous Reading: {prev_r} kWh</text>'
        f'<text x="235" y="72" font-size="11" fill="#0f172a">Current Reading: {curr_r} kWh</text>'
        f'<line x1="40" y1="84" x2="390" y2="84" stroke="#cbd5e1"/>'
        f'<text x="42" y="106" font-size="11" font-weight="bold" fill="#1e293b">Units Consumed: {units} kWh</text>'
        f'<text x="42" y="128" font-size="11" fill="#0f172a">Flat Energy Tariff: R {_fmt_fixed(rate_r, 2)} / kWh (excl. VAT)</text>'
        f'<text x="42" y="150" font-size="11" fill="#0f172a">Monthly Basic Service Fee: R {_fmt_fixed(fixed_r, 2)} (excl. VAT)</text>'
        f'<rect x="42" y="162" width="346" height="26" rx="4" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="215" y="180" font-size="11.5" font-weight="bold" fill="#92400e" text-anchor="middle">Add 15% VAT on Subtotal — Total Due: R ?</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_prepaid_meter(credit_r: float, rate_c: float, load_lbl: str) -> Dict[str, Any]:
    """Parameterized South African prepaid electricity meter LCD display."""
    svg = (
        f'<svg viewBox="0 0 430 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="185" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="40" y="18" width="350" height="148" rx="10" fill="#e2e8f0" stroke="#334155" stroke-width="2.5"/>'
        f'<rect x="65" y="34" width="300" height="74" rx="4" fill="#d9f99d" stroke="#3f6212" stroke-width="2"/>'
        f'<text x="215" y="56" font-size="11" font-weight="bold" fill="#365314" text-anchor="middle">PREPAID CREDIT BALANCE</text>'
        f'<text x="215" y="88" font-size="22" font-weight="bold" fill="#1a2e05" text-anchor="middle" font-family="monospace">R {_fmt_fixed(credit_r, 2)}</text>'
        f'<text x="215" y="130" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Tariff: {_fmt_fixed(rate_c, 2)} c/kWh</text>'
        f'<text x="215" y="150" font-size="10.5" fill="#1e3a8a" text-anchor="middle">Active Load: {load_lbl}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_sankey_bulbs(inc_in: int, inc_light: int, cfl_in: int, cfl_light: int, led_in: int, led_light: int) -> Dict[str, Any]:
    """Parameterized Sankey comparison of Incandescent, CFL, and LED efficiency."""
    rows = [
        ("Incandescent", inc_in, inc_light, inc_in - inc_light, 40),
        ("CFL", cfl_in, cfl_light, cfl_in - cfl_light, 96),
        ("LED", led_in, led_light, led_in - led_light, 152),
    ]
    parts = []
    for name, ein, elight, eheat, y in rows:
        l_frac = max(14, int((elight / float(ein)) * 180))
        h_frac = max(10, 180 - l_frac)
        parts.append(
            f'<text x="16" y="{y + 18}" font-size="10.5" font-weight="bold" fill="#0f172a">{name}</text>'
            f'<text x="16" y="{y + 32}" font-size="9.5" fill="#475569">In: {ein} J/s</text>'
            f'<rect x="108" y="{y}" width="{l_frac}" height="32" fill="#fde047" stroke="#ca8a04"/>'
            f'<text x="{108 + l_frac // 2}" y="{y + 20}" font-size="9.5" font-weight="bold" fill="#713f12" text-anchor="middle">Light {elight} J</text>'
            f'<rect x="{108 + l_frac}" y="{y}" width="{h_frac}" height="32" fill="#fca5a5" stroke="#dc2626"/>'
            f'<text x="{108 + l_frac + h_frac // 2}" y="{y + 20}" font-size="9.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">Heat {eheat} J</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Light Bulb Energy Split (Equal 800-Lumen Light Output)</text>'
        f'{"".join(parts)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_annual_bulb_cost(inc_r: float, cfl_r: float, led_r: float, hrs_yr: int) -> Dict[str, Any]:
    """Parameterized bar chart of annual electricity running cost for 3 bulb types."""
    max_r = max(inc_r, cfl_r, led_r, 20.0) * 1.15
    items = [("Incandescent", inc_r, "#dc2626"), ("CFL", cfl_r, "#d97706"), ("LED", led_r, "#16a34a")]
    bars = []
    for i, (lbl, val, col) in enumerate(items):
        h = max(12, int((val / max_r) * 110))
        x = 92 + i * 105
        y = 156 - h
        bars.append(
            f'<rect x="{x}" y="{y}" width="56" height="{h}" fill="{col}" stroke="#0f172a"/>'
            f'<text x="{x + 28}" y="{y - 6}" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">R {_fmt_fixed(val, 2)}</text>'
            f'<text x="{x + 28}" y="174" font-size="10.5" font-weight="bold" fill="#1e293b" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 198" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="198" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Annual Electricity Running Cost ({_fmt_int(hrs_yr)} h/year)</text>'
        f'<line x1="60" y1="36" x2="60" y2="156" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="156" x2="395" y2="156" stroke="#0f172a" stroke-width="2"/>'
        f'{"".join(bars)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_standby_power_strip(devices: List[tuple]) -> Dict[str, Any]:
    """Parameterized multi-plug standby ('vampire') load schematic."""
    total_w = sum(w for _, w in devices)
    boxes = []
    for i, (name, w) in enumerate(devices):
        x = 24 + i * 98
        boxes.append(
            f'<rect x="{x}" y="96" width="88" height="46" rx="4" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>'
            f'<text x="{x + 44}" y="115" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>'
            f'<text x="{x + 44}" y="132" font-size="10.5" font-weight="bold" fill="#dc2626" text-anchor="middle">{w} W idle</text>'
            f'<line x1="{x + 44}" y1="68" x2="{x + 44}" y2="96" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2"/>'
        )
    svg = (
        f'<svg viewBox="0 0 430 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="185" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="20" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Standby Power Strip (Wall Socket Left ON)</text>'
        f'<rect x="44" y="34" width="342" height="34" rx="5" fill="#1e293b"/>'
        f'<text x="215" y="55" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">Total Continuous Standby Draw: {total_w} W</text>'
        f'{"".join(boxes)}'
        f'<text x="215" y="168" font-size="10" fill="#475569" text-anchor="middle">All devices switched OFF via remote control only (wall switch still ON)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_home_audit_comparison(base_kwh: float, retro_kwh: float, rate_r: float) -> Dict[str, Any]:
    """Parameterized baseline vs retrofitted daily kWh chart."""
    b_cost = base_kwh * rate_r * 30
    r_cost = retro_kwh * rate_r * 30
    w_base = 240
    w_retro = max(40, int((retro_kwh / base_kwh) * 240))
    svg = (
        f'<svg viewBox="0 0 430 180" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="180" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="22" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Home Energy Audit: Daily Usage Before vs After Retrofit</text>'
        f'<text x="28" y="58" font-size="10.5" font-weight="bold" fill="#991b1b">Before (Old Geyser + Incandescent):</text>'
        f'<rect x="28" y="66" width="{w_base}" height="24" rx="3" fill="#dc2626"/>'
        f'<text x="{28 + w_base + 8}" y="82" font-size="10.5" font-weight="bold" fill="#991b1b">{_fmt_num(base_kwh, 2)} kWh/day</text>'
        f'<text x="28" y="118" font-size="10.5" font-weight="bold" fill="#166534">After (Blanket + LEDs):</text>'
        f'<rect x="28" y="126" width="{w_retro}" height="24" rx="3" fill="#16a34a"/>'
        f'<text x="{28 + w_retro + 8}" y="142" font-size="10.5" font-weight="bold" fill="#166534">{_fmt_num(retro_kwh, 2)} kWh/day</text>'
        f'<text x="215" y="168" font-size="10" fill="#334155" text-anchor="middle">Tariff: R {_fmt_fixed(rate_r, 2)}/kWh | 30-day audit (before = R {_fmt_fixed(b_cost, 2)} vs after = R {_fmt_fixed(r_cost, 2)})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ---------------------------------------------------------------------------
# Archetypes 26 to 50
# ---------------------------------------------------------------------------

def arch_26_reading_domestic_electricity_meter_kwh_difference(rng: random.Random) -> Dict[str, Any]:
    prev_r = rng.choice([3456, 4120, 5285, 6740, 8190, 9045])
    delta = rng.choice([680, 845, 920, 1110, 1240, 1380])
    curr_r = prev_r + delta
    rate_c = rng.choice([71.65, 185.50, 215.00, 248.40])
    cost_c = delta * rate_c
    cost_r = round(cost_c / 100.0, 2)
    meter_no = f"SA-{rng.randint(1040, 9980)}"
    d_spec = _svg_kwh_meter(meter_no, prev_r, curr_r)
    prompt = (
        f"Study the domestic kilowatt-hour meter readings shown in the diagram below for meter **#{meter_no}**.\n\n"
        "1. Calculate the total electrical energy consumed during this billing month in **$\\text{kWh}$** [2].\n"
        f"2. If the municipality charges **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**, calculate the monthly electricity cost in **Rands** [2]."
    )
    correct = f"{delta} kWh; R {_fmt_fixed(cost_r, 2)}"
    sol = (
        "**Step 1 — Energy Consumed:**\n"
        f"$$E = {curr_r} - {prev_r} = {delta}\\text{{ kWh}}$$ [2]\n\n"
        "**Step 2 — Total Cost in Cents & Rands:**\n"
        f"$$\\text{{Cost}} = {delta} \\times {_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}} = {_fmt_tex(cost_c, 2)}\\text{{ cents}}$$ [1]\n"
        f"$$\\text{{Cost (Rands)}} = \\frac{{{_fmt_tex(cost_c, 2)}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(cost_r, 2)}$$ [1]"
    )
    return _q(
        rng, "26", "26_reading_domestic_electricity_meter_kwh_difference", prompt, correct, sol, 4, "calculation",
        ["adding_previous_and_current_meter_readings_instead_of_subtracting"],
        "Subtract the previous meter reading from the current meter reading to find kWh used.",
        f"Used = {curr_r} - {prev_r} = {delta} kWh; multiply by {_fmt_fixed(rate_c, 2)} c and divide by 100.",
        correct,
        diagram_spec=d_spec,
    )


def arch_27_calculating_electricity_cost_cents_to_rands_conversion(rng: random.Random) -> Dict[str, Any]:
    kwh = rng.choice([240, 320, 415, 510, 625, 740])
    rate_c = rng.choice([71.65, 85.60, 142.50, 218.20, 265.00])
    cents = kwh * rate_c
    rands = round(cents / 100.0, 2)
    town = rng.choice(["Mangaung", "Nelson Mandela Bay", "eThekwini", "City of Cape Town", "Ekurhuleni"])
    prompt = (
        f"A household in **{town}** consumes **${kwh}\\text{{ kWh}}$** of electricity during a winter month at a unit price of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**.\n\n"
        "Calculate the total electricity cost in **cents** and convert your final answer to **Rands** (rounded to two decimal places) [3]."
    )
    correct = f"{_fmt_num(cents, 2)} cents (R {_fmt_fixed(rands, 2)})"
    sol = (
        "**Step 1 — Formula:**\n"
        "$$\\text{Cost} = \\text{Energy (kWh)} \\times \\text{Unit Tariff (c/kWh)}$$ [1]\n\n"
        "**Step 2 — Cost in Cents:**\n"
        f"$$\\text{{Cost}} = {kwh} \\times {_fmt_tex_fixed(rate_c, 2)} = {_fmt_tex(cents, 2)}\\text{{ cents}}$$ [1]\n\n"
        "**Step 3 — Convert Cents to Rands ($\\div 100$):**\n"
        f"$$\\text{{Cost}} = \\frac{{{_fmt_tex(cents, 2)}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(rands, 2)}$$ [1]"
    )
    return _q(
        rng, "27", "27_calculating_electricity_cost_cents_to_rands_conversion", prompt, correct, sol, 3, "calculation",
        ["forgetting_to_divide_cents_by_100_to_get_rands"],
        "100 cents = R 1,00. Multiply kWh by c/kWh first, then divide by 100.",
        f"{kwh} x {_fmt_fixed(rate_c, 2)} = {_fmt_num(cents, 2)} c = R {_fmt_fixed(rands, 2)}.",
        correct,
    )


def arch_28_single_appliance_operating_cost_watts_hours_tariff(rng: random.Random) -> Dict[str, Any]:
    app, watts, hrs = rng.choice([
        ("small oven", 1500, 1.0),
        ("electric geyser", 3000, 4.0),
        ("tumble dryer", 2500, 2.0),
        ("oil heater", 2000, 3.5),
        ("refrigerator compressor", 2200, 2.5),
        ("electric pan", 1400, 1.5),
        ("steam iron", 1600, 0.5),
    ])
    rate_c = rng.choice([71.65, 195.40, 240.00, 285.50])
    kw = watts / 1000.0
    kwh = kw * hrs
    cents = kwh * rate_c
    rands = round(cents / 100.0, 2)
    prompt = (
        f"A **${_fmt_int(watts)}\\text{{ W}}$ {app}** is operated for **${_fmt_tex(hrs, 1)}\\text{{ hours}}$** at an electricity tariff of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**.\n\n"
        "Calculate the total **cost in Rands** to run this appliance using $\\text{Cost} = P(\\text{kW}) \\times t(\\text{h}) \\times \\text{Tariff}$ [4]."
    )
    correct = f"R {_fmt_fixed(rands, 2)}"
    sol = (
        "**Step 1 — Convert Power to kW:**\n"
        f"$$P = \\frac{{{_fmt_int(watts)}}}{{1\\,000}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$$ [1]\n\n"
        "**Step 2 — Calculate Energy (kWh):**\n"
        f"$$E = {_fmt_tex(kw, 2)}\\text{{ kW}} \\times {_fmt_tex(hrs, 1)}\\text{{ h}} = {_fmt_tex(kwh, 2)}\\text{{ kWh}}$$ [1]\n\n"
        "**Step 3 — Calculate Cost in Cents & Convert to Rands:**\n"
        f"$$\\text{{Cost}} = {_fmt_tex(kwh, 2)} \\times {_fmt_tex_fixed(rate_c, 2)} = {_fmt_tex(cents, 2)}\\text{{ c}} = \\text{{R }}\\,{_fmt_tex_fixed(rands, 2)}$$ [2]"
    )
    return _q(
        rng, "28", "28_single_appliance_operating_cost_watts_hours_tariff", prompt, correct, sol, 4, "calculation",
        ["multiplying_watts_directly_by_tariff_without_dividing_by_1000"],
        "Convert Watts to kW (/1 000), multiply by hours, multiply by tariff (c/kWh), then divide by 100 for Rands.",
        f"P = {_fmt_num(kw, 2)} kW; E = {_fmt_num(kwh, 2)} kWh; Cost = R {_fmt_fixed(rands, 2)}.",
        correct,
    )


def arch_29_comparing_cooking_cost_microwave_vs_conventional_oven(rng: random.Random) -> Dict[str, Any]:
    mw_w, mw_min = rng.choice([(1360, 12), (1200, 10), (1400, 15)])
    ov_w, ov_hr = rng.choice([(6000, 1.0), (3600, 1.0), (4500, 1.2)])
    rate_c = rng.choice([71.65, 210.00, 255.00])
    mw_kwh = (mw_w / 1000.0) * (mw_min / 60.0)
    ov_kwh = (ov_w / 1000.0) * ov_hr
    mw_r = round((mw_kwh * rate_c) / 100.0, 2)
    ov_r = round((ov_kwh * rate_c) / 100.0, 2)
    saved_r = round(ov_r - mw_r, 2)
    food = rng.choice(["a large baking potato", "two sweet potatoes", "a winter vegetable casserole"])
    prompt = (
        f"Cooking **{food}** takes **${mw_min}\\text{{ minutes}}$** in a **${_fmt_int(mw_w)}\\text{{ W}}$ microwave oven**, compared to **${_fmt_tex(ov_hr, 1)}\\text{{ hour}}$** in a **${_fmt_int(ov_w)}\\text{{ W}}$ conventional oven**.\n\n"
        f"Using a tariff of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**, calculate the electricity cost (in Rands) for **each** appliance and state how much money is saved by choosing the microwave [5]."
    )
    correct = f"Microwave: R {_fmt_fixed(mw_r, 2)}; Conventional oven: R {_fmt_fixed(ov_r, 2)}; Savings: R {_fmt_fixed(saved_r, 2)}"
    sol = (
        f"**Step 1 — Microwave Cost ($t = \\frac{{{mw_min}}}{{60}} = {_fmt_tex(mw_min / 60.0, 2)}\\text{{ h}}$):**\n"
        f"$$E_{{\\text{{mw}}}} = {_fmt_tex(mw_w / 1000.0, 2)}\\text{{ kW}} \\times {_fmt_tex(mw_min / 60.0, 2)}\\text{{ h}} = {_fmt_tex(mw_kwh, 3)}\\text{{ kWh}}$$\n"
        f"$$\\text{{Cost}}_{{\\text{{mw}}}} = \\frac{{{_fmt_tex(mw_kwh, 3)} \\times {_fmt_tex_fixed(rate_c, 2)}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(mw_r, 2)}$$ [2]\n\n"
        "**Step 2 — Conventional Oven Cost:**\n"
        f"$$E_{{\\text{{ov}}}} = {_fmt_tex(ov_w / 1000.0, 2)}\\text{{ kW}} \\times {_fmt_tex(ov_hr, 1)}\\text{{ h}} = {_fmt_tex(ov_kwh, 2)}\\text{{ kWh}}$$\n"
        f"$$\\text{{Cost}}_{{\\text{{ov}}}} = \\frac{{{_fmt_tex(ov_kwh, 2)} \\times {_fmt_tex_fixed(rate_c, 2)}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(ov_r, 2)}$$ [2]\n\n"
        f"**Step 3 — Savings:** $\\text{{R }}\\,{_fmt_tex_fixed(ov_r, 2)} - \\text{{R }}\\,{_fmt_tex_fixed(mw_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(saved_r, 2)}$ saved [1]."
    )
    return _q(
        rng, "29", "29_comparing_cooking_cost_microwave_vs_conventional_oven", prompt, correct, sol, 5, "calculation",
        ["forgetting_to_convert_microwave_minutes_to_hours"],
        "Convert the microwave's minutes to hours (/60) and both wattages to kW (/1 000).",
        f"Microwave = R {_fmt_fixed(mw_r, 2)}; Oven = R {_fmt_fixed(ov_r, 2)}; Save R {_fmt_fixed(saved_r, 2)}.",
        correct,
    )


def arch_30_multi_unit_lighting_cost_school_week_or_home(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([6, 8, 10, 12, 16])
    bulb_w = rng.choice([60, 40, 15, 10])
    hrs_day = rng.choice([5.0, 6.0, 7.5, 8.0])
    days = rng.choice([5, 7, 20, 30])
    rate_c = rng.choice([71.65, 220.00, 250.00])
    total_kw = (n_bulbs * bulb_w) / 1000.0
    total_hrs = hrs_day * days
    total_kwh = total_kw * total_hrs
    cost_r = round((total_kwh * rate_c) / 100.0, 2)
    place = rng.choice(["a Grade 9 classroom", "a school science laboratory", "a community hall", "a family home"])
    prompt = (
        f"In **{place}**, **${n_bulbs}$ identical light bulbs** rated at **${bulb_w}\\text{{ W}}$ each** remain switched on for **${_fmt_tex(hrs_day, 1)}\\text{{ hours}}$ per day** over **${days}\\text{{ days}}$**.\n\n"
        f"At an electricity tariff of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**, calculate the **total energy consumed ($\\text{{kWh}}$)** and **total electricity cost (Rands)** for all ${n_bulbs}$ bulbs combined [4]."
    )
    correct = f"{_fmt_num(total_kwh, 2)} kWh; R {_fmt_fixed(cost_r, 2)}"
    sol = (
        "**Step 1 — Combined Power Rating in kW:**\n"
        f"$$P_{{\\text{{total}}}} = \\frac{{{n_bulbs} \\times {bulb_w}\\text{{ W}}}}{{1\\,000}} = {_fmt_tex(total_kw, 3)}\\text{{ kW}}$$ [1]\n\n"
        "**Step 2 — Total Hours & Energy:**\n"
        f"$$t = {_fmt_tex(hrs_day, 1)} \\times {days} = {_fmt_tex(total_hrs, 1)}\\text{{ h}}$$\n"
        f"$$E = {_fmt_tex(total_kw, 3)}\\text{{ kW}} \\times {_fmt_tex(total_hrs, 1)}\\text{{ h}} = {_fmt_tex(total_kwh, 2)}\\text{{ kWh}}$$ [2]\n\n"
        "**Step 3 — Total Cost:**\n"
        f"$$\\text{{Cost}} = \\frac{{{_fmt_tex(total_kwh, 2)} \\times {_fmt_tex_fixed(rate_c, 2)}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(cost_r, 2)}$$ [1]"
    )
    return _q(
        rng, "30", "30_multi_unit_lighting_cost_school_week_or_home", prompt, correct, sol, 4, "calculation",
        ["calculating_cost_for_only_one_bulb_instead_of_multiplying_by_count"],
        "Find combined power first (number of bulbs x W), convert to kW, then multiply by total hours.",
        f"Total P = {_fmt_num(total_kw, 3)} kW; E = {_fmt_num(total_kwh, 2)} kWh; Cost = R {_fmt_fixed(cost_r, 2)}.",
        correct,
    )


def arch_31_household_daily_appliance_survey_to_monthly_bill(rng: random.Random) -> Dict[str, Any]:
    geyser_kwh = rng.choice([6.0, 7.5, 9.0, 10.5])
    stove_kwh = rng.choice([2.5, 3.0, 3.6, 4.2])
    fridge_kwh = rng.choice([1.8, 2.2, 2.5])
    lights_kwh = rng.choice([0.8, 1.0, 1.2])
    tv_kwh = rng.choice([0.4, 0.5, 0.6])
    items = [
        ("Geyser", geyser_kwh),
        ("Stove", stove_kwh),
        ("Fridge", fridge_kwh),
        ("Lights", lights_kwh),
        ("TV", tv_kwh),
    ]
    daily_kwh = round(sum(e for _, e in items), 2)
    monthly_kwh = round(daily_kwh * 30.0, 2)
    rate_r = rng.choice([2.20, 2.45, 2.60, 2.85])
    monthly_cost = round(monthly_kwh * rate_r, 2)
    d_spec = _svg_daily_energy_bars(items, "Household Daily Electricity Consumption Survey (kWh/day)")
    prompt = (
        "The bar chart below summarises a family's daily home electricity audit across five appliance groups.\n\n"
        "1. Calculate the **total daily energy consumption** ($\\text{kWh/day}$) [1].\n"
        "2. Calculate the **30-day monthly energy consumption** ($\\text{kWh}$) [1].\n"
        f"3. Using a flat municipal rate of **R ${_fmt_tex_fixed(rate_r, 2)}/\\text{{kWh}}$**, calculate the estimated **30-day monthly electricity bill** in Rands [2]."
    )
    correct = f"{_fmt_num(daily_kwh, 2)} kWh/day; {_fmt_num(monthly_kwh, 2)} kWh/month; R {_fmt_fixed(monthly_cost, 2)}"
    sol = (
        "**Step 1 — Daily Total:**\n"
        f"$$E_{{\\text{{day}}}} = {_fmt_tex(geyser_kwh, 2)} + {_fmt_tex(stove_kwh, 2)} + {_fmt_tex(fridge_kwh, 2)} + {_fmt_tex(lights_kwh, 2)} + {_fmt_tex(tv_kwh, 2)} = {_fmt_tex(daily_kwh, 2)}\\text{{ kWh/day}}$$ [1]\n\n"
        "**Step 2 — Monthly Total (30 Days):**\n"
        f"$$E_{{\\text{{month}}}} = {_fmt_tex(daily_kwh, 2)} \\times 30 = {_fmt_tex(monthly_kwh, 2)}\\text{{ kWh}}$$ [1]\n\n"
        "**Step 3 — Monthly Bill:**\n"
        f"$$\\text{{Cost}} = {_fmt_tex(monthly_kwh, 2)} \\times \\text{{R }}\\,{_fmt_tex_fixed(rate_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(monthly_cost, 2)}$$ [2]"
    )
    return _q(
        rng, "31", "31_household_daily_appliance_survey_to_monthly_bill", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_multiply_daily_total_by_30_days"],
        "Sum all 5 daily kWh values first, multiply by 30 days, then multiply by the R/kWh tariff.",
        f"Daily = {_fmt_num(daily_kwh, 2)} kWh; 30-day = {_fmt_num(monthly_kwh, 2)} kWh; Cost = R {_fmt_fixed(monthly_cost, 2)}.",
        correct,
        diagram_spec=d_spec,
    )


def arch_32_purpose_of_tiered_inclining_block_electricity_tariffs(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Tshwane", "Johannesburg", "Cape Town", "eThekwini", "Mbombela", "Gqeberha"])
    b1_rate = rng.choice(["69,35 c/kWh", "145,20 c/kWh", "168,00 c/kWh"])
    b4_rate = rng.choice(["139,31 c/kWh", "298,40 c/kWh", "345,00 c/kWh"])
    prompt = (
        f"Eskom and South African municipalities such as **{city}** apply an **inclining block (tiered) tariff** system — for example, charging **{b1_rate}** for the first $50\\text{{ kWh}}$ per month, rising up to **{b4_rate}** above $600\\text{{ kWh}}$.\n\n"
        "Explain **two** key social and energy-management reasons why electricity utilities use tiered tariffs instead of a single flat unit price [2]."
    )
    correct = "1) To encourage households to conserve electricity because higher usage pushes units into more expensive blocks; 2) To keep essential basic electricity affordable for low-income, low-consumption households."
    sol = (
        "**Step 1 — Conservation Incentive:** As monthly consumption crosses higher block thresholds, each additional kilowatt-hour costs significantly more, motivating families to save electricity and reduce strain on the national grid [1].\n\n"
        "**Step 2 — Social Equity:** Essential first units (Block 1, $\\le 50\\text{ kWh}$) are kept cheaper (cross-subsidised by high-consumption users) so lower-income households can afford basic lighting and cooking [1]."
    )
    return _q(
        rng, "32", "32_purpose_of_tiered_inclining_block_electricity_tariffs", prompt, correct, sol, 2, "short_answer",
        ["thinking_tiered_tariffs_offer_bulk_discounts_for_high_electricity_usage"],
        "Unlike bulk supermarket discounts, electricity block prices go UP when you buy more!",
        "Tiered tariffs discourage wasteful high usage and keep basic Block 1 units affordable for poorer homes.",
        correct,
    )


def arch_33_interpreting_eskom_block_tariff_step_graph_and_rate(rng: random.Random) -> Dict[str, Any]:
    rates = [
        ("Block 1", "0-50 kWh", rng.choice([69.35, 145.20, 162.50])),
        ("Block 2", "51-350 kWh", rng.choice([85.60, 189.40, 210.80])),
        ("Block 3", "351-600 kWh", rng.choice([127.02, 265.10, 294.30])),
        ("Block 4", ">600 kWh", rng.choice([139.31, 312.80, 348.60])),
    ]
    usage_info = rng.choice([
        (42, 0, "Block 1 (0-50 kWh)"),
        (252, 1, "Block 2 (51-350 kWh)"),
        (485, 2, "Block 3 (351-600 kWh)"),
        (740, 3, "Block 4 (>600 kWh)"),
    ])
    usage, idx, blk_lbl = usage_info
    rate_c = rates[idx][2]
    d_spec = _svg_block_tariff_steps(rates, usage)
    correct = f"{blk_lbl}, where additional units are charged at {_fmt_fixed(rate_c, 2)} c/kWh."
    options = [
        f"{rates[i][0]} ({rates[i][1]}), where additional units are charged at {_fmt_fixed(rates[i][2], 2)} c/kWh."
        for i in range(4)
    ]
    rng.shuffle(options)
    prompt = (
        f"Study the inclining block tariff graph below. A household consumes **${usage}\\text{{ kWh}}$** during the month.\n\n"
        "Which tariff block does the household's **final (marginal) kilowatt-hour** fall into, and what is the unit rate for that block?"
    )
    sol = (
        f"**Step 1:** Locate ${usage}\\text{{ kWh}}$ against the block ranges on the chart:\n"
        "- Block 1: $0 - 50\\text{ kWh}$\n"
        "- Block 2: $51 - 350\\text{ kWh}$\n"
        "- Block 3: $351 - 600\\text{ kWh}$\n"
        "- Block 4: $> 600\\text{ kWh}$\n\n"
        f"**Step 2:** ${usage}\\text{{ kWh}}$ sits in **{blk_lbl}** at **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**."
    )
    return _q(
        rng, "33", "33_interpreting_eskom_block_tariff_step_graph_and_rate", prompt, correct, sol, 2, "mcq",
        ["misidentifying_block_boundary_for_monthly_kwh_usage"],
        "Check which kWh interval contains the total monthly consumption.",
        f"{usage} kWh falls into {blk_lbl} ({_fmt_fixed(rate_c, 2)} c/kWh).",
        correct,
        options=options,
        diagram_spec=d_spec,
    )


def arch_34_calculating_tiered_inclining_block_electricity_bill(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Eskom Homepower example: Block 1 <= 50, Block 2 51..350
    b1_rate = rng.choice([69.35, 140.00, 165.00])
    b2_rate = rng.choice([85.60, 185.00, 215.00])
    total_kwh = rng.choice([210, 252, 285, 315, 340])
    b1_units = 50
    b2_units = total_kwh - 50
    b1_cents = b1_units * b1_rate
    b2_cents = b2_units * b2_rate
    tot_cents = b1_cents + b2_cents
    tot_rands = round(tot_cents / 100.0, 2)
    prompt = (
        "An electricity supplier applies a two-block inclining tariff (including environmental levy):\n"
        f"- **Block 1 ($0 - 50\\text{{ kWh}}$):** ${_fmt_tex_fixed(b1_rate, 2)}\\text{{ c/kWh}}$\n"
        f"- **Block 2 ($51 - 350\\text{{ kWh}}$):** ${_fmt_tex_fixed(b2_rate, 2)}\\text{{ c/kWh}}$\n\n"
        f"Calculate the total monthly electricity cost (in **Rands**, rounded to two decimal places) for a home that uses **${total_kwh}\\text{{ kWh}}$** [4]."
    )
    correct = f"R {_fmt_fixed(tot_rands, 2)}"
    sol = (
        "**Step 1 — Cost for Block 1 (first 50 kWh):**\n"
        f"$$50 \\times {_fmt_tex_fixed(b1_rate, 2)} = {_fmt_tex(b1_cents, 2)}\\text{{ cents}}$$ [1]\n\n"
        f"**Step 2 — Remaining Units in Block 2 (${total_kwh} - 50 = {b2_units}\\text{{ kWh}}$):**\n"
        f"$${b2_units} \\times {_fmt_tex_fixed(b2_rate, 2)} = {_fmt_tex(b2_cents, 2)}\\text{{ cents}}$$ [1]\n\n"
        "**Step 3 — Sum & Convert to Rands:**\n"
        f"$$\\text{{Total}} = {_fmt_tex(b1_cents, 2)} + {_fmt_tex(b2_cents, 2)} = {_fmt_tex(tot_cents, 2)}\\text{{ c}} = \\text{{R }}\\,{_fmt_tex_fixed(tot_rands, 2)}$$ [2]"
    )
    return _q(
        rng, "34", "34_calculating_tiered_inclining_block_electricity_bill", prompt, correct, sol, 4, "calculation",
        ["multiplying_all_kwh_by_block_2_rate_instead_of_splitting_first_50_kwh"],
        "Split the total into two parts: first 50 kWh at Block 1 rate, then (Total - 50) kWh at Block 2 rate.",
        f"50 x {_fmt_fixed(b1_rate, 2)} + {b2_units} x {_fmt_fixed(b2_rate, 2)} = {_fmt_num(tot_cents, 2)} c = R {_fmt_fixed(tot_rands, 2)}.",
        correct,
    )


def arch_35_electricity_bill_with_fixed_charge_and_15_percent_vat(rng: random.Random) -> Dict[str, Any]:
    units = rng.choice([280, 350, 420, 500, 560])
    rate_r = rng.choice([2.10, 2.35, 2.50, 2.75])
    fixed_r = rng.choice([120.00, 145.00, 165.00, 180.00])
    energy_r = round(units * rate_r, 2)
    subtotal = round(energy_r + fixed_r, 2)
    vat = round(subtotal * 0.15, 2)
    total_due = round(subtotal + vat, 2)
    prompt = (
        f"A municipality bills a small bakery for **${units}\\text{{ kWh}}$** at **R ${_fmt_tex_fixed(rate_r, 2)}/\\text{{kWh}}$**, plus a monthly fixed service charge of **R ${_fmt_tex_fixed(fixed_r, 2)}$** (both excluding VAT).\n\n"
        "Calculate:\n"
        "1. The subtotal excluding VAT [2].\n"
        "2. The **15% VAT** amount [1].\n"
        "3. The **final amount payable** including VAT [1]."
    )
    correct = f"Subtotal: R {_fmt_fixed(subtotal, 2)}; VAT (15%): R {_fmt_fixed(vat, 2)}; Total payable: R {_fmt_fixed(total_due, 2)}"
    sol = (
        "**Step 1 — Energy Charge & Subtotal (excl. VAT):**\n"
        f"$$\\text{{Energy Charge}} = {units} \\times \\text{{R }}\\,{_fmt_tex_fixed(rate_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(energy_r, 2)}$$\n"
        f"$$\\text{{Subtotal}} = \\text{{R }}\\,{_fmt_tex_fixed(energy_r, 2)} + \\text{{R }}\\,{_fmt_tex_fixed(fixed_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)}$$ [2]\n\n"
        "**Step 2 — 15% VAT:**\n"
        f"$$\\text{{VAT}} = 0{{,}}15 \\times \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(vat, 2)}$$ [1]\n\n"
        "**Step 3 — Total Payable:**\n"
        f"$$\\text{{Total}} = \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)} + \\text{{R }}\\,{_fmt_tex_fixed(vat, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(total_due, 2)}$$ [1]"
    )
    return _q(
        rng, "35", "35_electricity_bill_with_fixed_charge_and_15_percent_vat", prompt, correct, sol, 4, "calculation",
        ["applying_vat_only_to_energy_and_forgetting_fixed_service_fee"],
        "Add the energy cost and the fixed service charge before multiplying by 1,15 (or adding 15%).",
        f"Subtotal = R {_fmt_fixed(subtotal, 2)}; VAT = R {_fmt_fixed(vat, 2)}; Total = R {_fmt_fixed(total_due, 2)}.",
        correct,
    )


def arch_36_auditing_municipal_electricity_statement_errors(rng: random.Random) -> Dict[str, Any]:
    town = rng.choice(["Mangaung", "Tshwane", "eThekwini", "Sol Plaatje", "Stellenbosch"])
    prev_r = rng.choice([12400, 15620, 21350, 28410])
    units = rng.choice([420, 480, 540, 610])
    curr_r = prev_r + units
    rate_r = rng.choice([2.25, 2.40, 2.65])
    fixed_r = rng.choice([110.00, 130.00, 150.00])
    subtotal = round(units * rate_r + fixed_r, 2)
    vat = round(subtotal * 0.15, 2)
    total_due = round(subtotal + vat, 2)
    d_spec = _svg_municipal_statement(town, prev_r, curr_r, rate_r, fixed_r)
    prompt = (
        "Inspect the municipal electricity account summary shown in the diagram below.\n\n"
        "Verify the units consumed from the meter readings and calculate the **total amount due (including 15% VAT)** in Rands [4]."
    )
    correct = f"R {_fmt_fixed(total_due, 2)} (Subtotal R {_fmt_fixed(subtotal, 2)} + VAT R {_fmt_fixed(vat, 2)})"
    sol = (
        "**Step 1 — Verify Units:**\n"
        f"$${curr_r} - {prev_r} = {units}\\text{{ kWh}}$$ [1]\n\n"
        "**Step 2 — Calculate Subtotal (excl. VAT):**\n"
        f"$$\\text{{Subtotal}} = ({units} \\times \\text{{R }}\\,{_fmt_tex_fixed(rate_r, 2)}) + \\text{{R }}\\,{_fmt_tex_fixed(fixed_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)}$$ [1]\n\n"
        "**Step 3 — Add 15% VAT:**\n"
        f"$$\\text{{VAT}} = 0{{,}}15 \\times \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(vat, 2)}$$\n"
        f"$$\\text{{Total Due}} = \\text{{R }}\\,{_fmt_tex_fixed(subtotal, 2)} + \\text{{R }}\\,{_fmt_tex_fixed(vat, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(total_due, 2)}$$ [2]"
    )
    return _q(
        rng, "36", "36_auditing_municipal_electricity_statement_errors", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_add_15_percent_vat_on_municipal_bill"],
        "Multiply units by the Rand rate, add the basic fee, then multiply by 1,15 for 15% VAT.",
        f"Subtotal = R {_fmt_fixed(subtotal, 2)}; Total with 15% VAT = R {_fmt_fixed(total_due, 2)}.",
        correct,
        diagram_spec=d_spec,
    )


def arch_37_eskom_direct_vs_municipal_tariff_variations(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("Soweto (Eskom Direct)", "Midrand (City Power)"),
        ("Khayelitsha (Eskom Direct)", "Claremont (City of Cape Town)"),
        ("Tembisa (Eskom Direct)", "Centurion (City of Tshwane)"),
        ("Kwamashu (Eskom Direct)", "Umhlanga (eThekwini Municipality)"),
    ])
    a1, a2 = pair
    prompt = (
        f"Two neighbouring households — one in **{a1}** and one in **{a2}** — consume identical amounts of electricity ($350\\text{{ kWh}}$), yet receive slightly different monthly bills.\n\n"
        "Which explanation accurately accounts for why South African electricity unit rates vary between areas?"
    )
    correct = "Unit electricity tariffs depend on whether electricity is bought directly from Eskom or through a local municipality, and different municipalities set their own tariff schedules and service charges."
    options = [
        correct,
        "Electrons travel more slowly through municipal copper cables, losing half of every kilowatt-hour before reaching the meter.",
        "Municipalities supply 460 V electricity instead of 230 V, doubling every appliance's wattage.",
        "Households closer to coal mines receive free unlimited kWh by national law.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** South Africa has two main retail distribution channels: direct **Eskom** supply and **municipal** distributors.\n\n"
        "**Step 2:** Municipalities purchase bulk power from Eskom and add local distribution maintenance costs, producing distinct municipal tariff schedules across towns and cities."
    )
    return _q(
        rng, "37", "37_eskom_direct_vs_municipal_tariff_variations", prompt, correct, sol, 2, "mcq",
        ["assuming_one_identical_electricity_price_across_all_south_african_municipalities"],
        "Think about who sells electricity to households: Eskom directly vs local municipalities.",
        "Tariffs vary between direct Eskom supply and different municipal distributors.",
        correct,
        options=options,
    )


def arch_38_prepaid_electricity_voucher_kwh_units_purchased(rng: random.Random) -> Dict[str, Any]:
    voucher_r = rng.choice([50.00, 100.00, 150.00, 200.00, 350.00])
    rate_c = rng.choice([71.65, 210.50, 245.00, 275.00])
    voucher_c = voucher_r * 100.0
    kwh_bought = round(voucher_c / rate_c, 2)
    prompt = (
        f"A family buys a **R ${_fmt_tex_fixed(voucher_r, 2)}$** prepaid electricity voucher at a flat tariff of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**.\n\n"
        "Convert the voucher value into cents and calculate how many **kilowatt-hours (units)** will load onto the prepaid meter (to two decimal places) [3]."
    )
    correct = f"{_fmt_fixed(kwh_bought, 2)} kWh"
    sol = (
        "**Step 1 — Convert Voucher Value to Cents:**\n"
        f"$$\\text{{R }}\\,{_fmt_tex_fixed(voucher_r, 2)} \\times 100 = {_fmt_int(int(voucher_c))}\\text{{ cents}}$$ [1]\n\n"
        "**Step 2 — Divide by Unit Rate (c/kWh):**\n"
        f"$$\\text{{Units}} = \\frac{{{_fmt_int(int(voucher_c))}\\text{{ cents}}}}{{{_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}}} = {_fmt_tex_fixed(kwh_bought, 2)}\\text{{ kWh}}$$ [2]"
    )
    return _q(
        rng, "38", "38_prepaid_electricity_voucher_kwh_units_purchased", prompt, correct, sol, 3, "calculation",
        ["dividing_rands_directly_by_cents_without_converting_rands_to_cents"],
        "Ensure matching units! Multiply Rands by 100 to get cents before dividing by c/kWh.",
        f"{int(voucher_c)} c / {_fmt_fixed(rate_c, 2)} c/kWh = {_fmt_fixed(kwh_bought, 2)} kWh.",
        correct,
    )


def arch_39_prepaid_meter_credit_longevity_hours_and_days(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        (35.00, 71.65, "230 W Television", 230),
        (50.00, 200.00, "2 000 W Heater", 2000),
        (100.00, 250.00, "1 000 W Fridge", 1000),
        (75.00, 240.00, "1 500 W Iron", 1500),
        (120.00, 220.00, "3 000 W Geyser", 3000),
    ])
    credit_r, rate_c, load_lbl, watts = scenario
    kwh_avail = (credit_r * 100.0) / rate_c
    kw = watts / 1000.0
    hours_left = round(kwh_avail / kw, 2)
    d_spec = _svg_prepaid_meter(credit_r, rate_c, load_lbl)
    prompt = (
        "Examine the prepaid electricity meter display shown in the diagram below.\n\n"
        "1. Calculate how many **kilowatt-hours ($\\text{kWh}$)** remain on the meter [2].\n"
        f"2. Calculate for how many **hours** the connected **{load_lbl}** can operate continuously before the credit reaches R 0,00 [2]."
    )
    correct = f"{_fmt_fixed(kwh_avail, 2)} kWh; {_fmt_fixed(hours_left, 2)} hours"
    sol = (
        "**Step 1 — Remaining Energy Units (kWh):**\n"
        f"$$E = \\frac{{{_fmt_tex_fixed(credit_r, 2)} \\times 100}}{{{_fmt_tex_fixed(rate_c, 2)}}} = {_fmt_tex_fixed(kwh_avail, 2)}\\text{{ kWh}}$$ [2]\n\n"
        f"**Step 2 — Convert Power to kW ($P = \\frac{{{watts}}}{{1\\,000}} = {_fmt_tex(kw, 3)}\\text{{ kW}}$) and Solve for Time:**\n"
        f"$$t = \\frac{{E}}{{P}} = \\frac{{{_fmt_tex_fixed(kwh_avail, 2)}}}{{{_fmt_tex(kw, 3)}}} = {_fmt_tex_fixed(hours_left, 2)}\\text{{ hours}}$$ [2]"
    )
    return _q(
        rng, "39", "39_prepaid_meter_credit_longevity_hours_and_days", prompt, correct, sol, 4, "calculation",
        ["forgetting_to_convert_watts_to_kw_when_dividing_prepaid_kwh"],
        "First find kWh available (cents / tariff), then divide by power in kW (Watts / 1 000).",
        f"Energy = {_fmt_fixed(kwh_avail, 2)} kWh; Hours = {_fmt_fixed(hours_left, 2)} h.",
        correct,
        diagram_spec=d_spec,
    )


def arch_40_reverse_cost_to_operating_time_or_appliance_power(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("pool pump", 4500, 4.84, 71.65),
        ("electric heater", 2000, 7.20, 240.00),
        ("electric geyser", 3000, 18.75, 250.00),
        ("tumble dryer", 2500, 11.25, 225.00),
        ("air conditioner", 1800, 12.96, 240.00),
    ])
    app, watts, cost_r, rate_c = case
    kwh = (cost_r * 100.0) / rate_c
    kw = watts / 1000.0
    hrs = round(kwh / kw, 2)
    prompt = (
        f"Operating a **${_fmt_int(watts)}\\text{{ W}}$ {app}** cost **R ${_fmt_tex_fixed(cost_r, 2)}$** at an electricity tariff of **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**.\n\n"
        "Work backwards to calculate:\n"
        "1. The total electrical energy consumed in **$\\text{kWh}$** [2].\n"
        "2. How long (in **hours**, to two decimal places) the appliance was switched on [2]."
    )
    correct = f"{_fmt_fixed(kwh, 2)} kWh; {_fmt_fixed(hrs, 2)} hours"
    sol = (
        "**Step 1 — Find Energy Consumed from Cost:**\n"
        f"$$E = \\frac{{\\text{{Cost (cents)}}}}{{\\text{{Tariff (c/kWh)}}}} = \\frac{{{_fmt_tex_fixed(cost_r * 100.0, 0)}}}{{{_fmt_tex_fixed(rate_c, 2)}}} = {_fmt_tex_fixed(kwh, 2)}\\text{{ kWh}}$$ [2]\n\n"
        f"**Step 2 — Convert Power (${watts}\\text{{ W}} = {_fmt_tex(kw, 2)}\\text{{ kW}}$) and Find Time ($t = \\frac{{E}}{{P}}$):**\n"
        f"$$t = \\frac{{{_fmt_tex_fixed(kwh, 2)}}}{{{_fmt_tex(kw, 2)}}} = {_fmt_tex_fixed(hrs, 2)}\\text{{ hours}}$$ [2]"
    )
    return _q(
        rng, "40", "40_reverse_cost_to_operating_time_or_appliance_power", prompt, correct, sol, 4, "calculation",
        ["multiplying_cost_by_tariff_instead_of_dividing"],
        "Convert Rands to cents, divide by tariff (c/kWh) to get kWh, then divide by kW to get hours.",
        f"E = {_fmt_fixed(kwh, 2)} kWh; t = {_fmt_fixed(hrs, 2)} hours.",
        correct,
    )


def arch_41_thermostat_cycling_in_fridges_and_geysers(rng: random.Random) -> Dict[str, Any]:
    app, watts, role = rng.choice([
        ("refrigerator", 2200, "switches the compressor and condenser on when internal air warms up and switches them off once cold"),
        ("electric geyser", 3000, "switches the heating element on when water cools below 60 °C and switches it off once the set temperature is reached"),
        ("deep chest freezer", 350, "cycles the cooling compressor intermittently whenever heat enters through door openings"),
        ("thermostatic oil heater", 2000, "cuts power to the heating coils once room air reaches the dial temperature"),
    ])
    prompt = (
        f"A household **{app}** in {rng.choice(['Soweto', 'Durban', 'Cape Town', 'Pretoria', 'Polokwane', 'Gqeberha'])} is plugged into the wall all day ($24\\text{{ hours}}$) and carries a rating of **${watts}\\text{{ W}}$**, yet its actual daily electricity consumption is far lower than ${_fmt_tex(watts / 1000.0, 2)} \\times 24\\text{{ kWh}}$."
        "\n\nExplain the role of the **thermostat** and **insulation** in reducing the appliance's true operating hours [3]."
    )
    correct = f"The thermostat monitors temperature and {role}, so the high-power component does not run continuously for all 24 hours; good thermal insulation slows heat transfer and keeps the appliance switched off longer."
    sol = (
        f"**Step 1 — Thermostat Control:** A **thermostat** acts as an automatic temperature-sensitive switch that {role} [2].\n\n"
        "**Step 2 — Role of Insulation:** Thick thermal insulation reduces unwanted heat entry (in a fridge) or heat escape (in a geyser), lengthening the idle intervals and cutting electricity consumption [1]."
    )
    return _q(
        rng, "41", "41_thermostat_cycling_in_fridges_and_geysers", prompt, correct, sol, 3, "short_answer",
        ["assuming_a_fridge_or_geyser_draws_peak_wattage_for_all_24_hours"],
        "Does the motor or heating element stay on every second of the day, or does a temperature switch cycle it?",
        "Thermostat cycles power on/off to maintain target temperature; insulation reduces heat loss/gain.",
        correct,
    )


def arch_42_sankey_efficiency_incandescent_cfl_led_comparison(rng: random.Random) -> Dict[str, Any]:
    inc_in = rng.choice([60, 75, 100])
    inc_l = 6 if inc_in == 60 else (8 if inc_in == 75 else 10)
    cfl_in = rng.choice([15, 18, 20])
    cfl_l = 6 if cfl_in == 15 else (7 if cfl_in == 18 else 8)
    led_in = rng.choice([8, 9, 10])
    led_l = 6 if led_in == 8 else (7 if led_in == 9 else 8)
    d_spec = _svg_sankey_bulbs(inc_in, inc_l, cfl_in, cfl_l, led_in, led_l)
    eff_inc = round((inc_l / float(inc_in)) * 100.0, 1)
    eff_led = round((led_l / float(led_in)) * 100.0, 1)
    prompt = (
        "Examine the energy-split diagram below comparing three light bulbs that produce the same $800\\text{ lumens}$ of brightness.\n\n"
        f"1. State why the **{inc_in} W incandescent bulb** requires much more electrical input power than the **{led_in} W LED** [2].\n"
        "2. Calculate the useful light efficiency ($\\frac{\\text{useful light}}{\\text{total input}} \\times 100\\%$) for both the incandescent bulb and the LED bulb [2]."
    )
    correct = f"Incandescent bulbs waste roughly {_fmt_num(100 - eff_inc, 1)}% of electrical energy as unwanted heat in a glowing filament, whereas LEDs convert most input directly into light; Efficiency: Incandescent = {_fmt_num(eff_inc, 1)}%, LED = {_fmt_num(eff_led, 1)}%."
    sol = (
        f"**Step 1 — Energy Waste Mechanism:** An incandescent bulb heats a thin tungsten wire until it glows, wasting **${inc_in - inc_l}\\text{{ J/s}}$ as heat** and outputting only ${inc_l}\\text{{ J/s}}$ as light. An LED converts electrical energy directly into light with only ${led_in - led_l}\\text{{ J/s}}$ lost as heat [2].\n\n"
        f"**Step 2 — Efficiencies:**\n"
        f"- Incandescent: $\\frac{{{inc_l}}}{{{inc_in}}} \\times 100\\% = {_fmt_tex(eff_inc, 1)}\\%$ [1]\n"
        f"- LED: $\\frac{{{led_l}}}{{{led_in}}} \\times 100\\% = {_fmt_tex(eff_led, 1)}\\%$ [1]"
    )
    return _q(
        rng, "42", "42_sankey_efficiency_incandescent_cfl_led_comparison", prompt, correct, sol, 4, "short_answer",
        ["thinking_hotter_bulbs_are_more_energy_efficient"],
        "Useful output is light, wasted output is heat. Efficiency = (Light / Total Input) x 100%.",
        f"Incandescent wastes {inc_in - inc_l} J as heat ({_fmt_num(eff_inc, 1)}% efficient); LED is {_fmt_num(eff_led, 1)}% efficient.",
        correct,
        diagram_spec=d_spec,
    )


def arch_43_percentage_energy_saved_led_bulb_upgrade(rng: random.Random) -> Dict[str, Any]:
    old_w, new_w = rng.choice([
        (60, 8),
        (60, 9),
        (75, 10),
        (100, 12),
        (60, 15),
        (100, 15),
    ])
    diff_w = old_w - new_w
    pct = round((diff_w / float(old_w)) * 100.0, 1)
    old_lbl = "incandescent globe"
    new_lbl = "LED globe" if new_w <= 12 else "CFL energy saver"
    prompt = (
        f"A school replaces all **${old_w}\\text{{ W}}$ {old_lbl}s** with **${new_w}\\text{{ W}}$ {new_lbl}s** that emit the exact same brightness ($800\\text{{ lumens}}$).\n\n"
        "Calculate the **percentage of electrical energy saved** by making this switch [3]."
    )
    correct = f"{_fmt_num(pct, 1)}%"
    sol = (
        "**Step 1 — Power Reduction:**\n"
        f"$$\\Delta P = {old_w}\\text{{ W}} - {new_w}\\text{{ W}} = {diff_w}\\text{{ W saved}}$$ [1]\n\n"
        "**Step 2 — Percentage Energy Saved:**\n"
        f"$$\\%\\text{{ Saved}} = \\frac{{{diff_w}}}{{{old_w}}} \\times 100\\% = {_fmt_tex(pct, 1)}\\%$$ [2]"
    )
    return _q(
        rng, "43", "43_percentage_energy_saved_led_bulb_upgrade", prompt, correct, sol, 3, "calculation",
        ["dividing_savings_by_new_wattage_instead_of_original_wattage"],
        "Percentage saved = ((Old Power - New Power) / Old Power) x 100%.",
        f"({old_w} - {new_w}) / {old_w} x 100% = {_fmt_num(pct, 1)}%.",
        correct,
    )


def arch_44_annual_running_cost_and_payback_bulb_comparison(rng: random.Random) -> Dict[str, Any]:
    hrs_day = rng.choice([4, 5, 6])
    hrs_yr = hrs_day * 365
    rate_c = rng.choice([71.65, 220.00, 250.00])
    inc_r = round((0.060 * hrs_yr * rate_c) / 100.0, 2)
    cfl_r = round((0.015 * hrs_yr * rate_c) / 100.0, 2)
    led_r = round((0.008 * hrs_yr * rate_c) / 100.0, 2)
    saved_yr = round(inc_r - led_r, 2)
    d_spec = _svg_annual_bulb_cost(inc_r, cfl_r, led_r, hrs_yr)
    prompt = (
        f"Study the annual running cost bar chart below for a bulb used **${hrs_day}\\text{{ hours}}$ per day** for a full year (**${_fmt_int(hrs_yr)}\\text{{ hours/year}}$**) at **${_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}$**.\n\n"
        f"1. Verify the annual electricity cost of the **$8\\text{{ W}}$ LED** ($0{{,}}008\\text{{ kW}}$) [2].\n"
        "2. Explain why an LED bulb is more economical over a year than a $60\\text{ W}$ incandescent bulb even if the LED costs R 35 more to buy in the shop [2]."
    )
    correct = f"R {_fmt_fixed(led_r, 2)}/year; The LED saves R {_fmt_fixed(saved_yr, 2)} in electricity in just one year and lasts up to 50 000 hours (replacing over 40 incandescent bulbs)."
    sol = (
        "**Step 1 — LED Annual Running Cost:**\n"
        f"$$\\text{{Cost}} = \\frac{{0{{,}}008\\text{{ kW}} \\times {_fmt_int(hrs_yr)}\\text{{ h}} \\times {_fmt_tex_fixed(rate_c, 2)}\\text{{ c/kWh}}}}{{100}} = \\text{{R }}\\,{_fmt_tex_fixed(led_r, 2)}$$ [2]\n\n"
        f"**Step 2 — Economic Justification:** Compared to the $60\\text{{ W}}$ incandescent bulb (R {_fmt_tex_fixed(inc_r, 2)}/yr), the LED saves **R {_fmt_tex_fixed(saved_yr, 2)} per year** in electricity alone and has a lifespan up to $50\\,000\\text{{ hours}}$ vs $1\\,200\\text{{ hours}}$ [2]."
    )
    return _q(
        rng, "44", "44_annual_running_cost_and_payback_bulb_comparison", prompt, correct, sol, 4, "calculation",
        ["judging_bulb_economy_only_by_shelf_purchase_price"],
        "Multiply 0,008 kW x annual hours x tariff (in c/kWh), then divide by 100 for Rands.",
        f"LED cost = R {_fmt_fixed(led_r, 2)}/yr; annual saving vs incandescent = R {_fmt_fixed(saved_yr, 2)}.",
        correct,
        diagram_spec=d_spec,
    )


def arch_45_environmental_hazard_mercury_in_cfl_vs_led_lifespan(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice([
        ("toxic heavy-metal chemical hazard when broken or dumped in landfill", "Compact Fluorescent Light bulbs (CFLs), because their glass tubes contain poisonous mercury vapour", "LED bulbs, because their silicon chip emits zero carbon"),
        ("longest operating lifespan (~50 000 hours vs 8 000 h for CFLs and 1 200 h for incandescent)", "LED bulbs, reducing manufacturing waste and frequent replacements", "Incandescent tungsten filament bulbs, because glowing metal never wears out"),
        ("most environmentally friendly overall choice for both energy efficiency and non-toxic materials", "LED bulbs (lowest wattage ~8 W and completely mercury-free)", "CFL bulbs (highest wattage and filled with mercury)"),
    ])
    criterion, correct, wrong_a = aspect
    options = [
        correct,
        wrong_a,
        "Halogen floodlights, because they convert 95% of energy into heat.",
        "All three bulbs contain identical mercury tubes and last 50 000 hours.",
    ]
    rng.shuffle(options)
    prompt = (
        f"When evaluating household lighting for **{criterion}**, which choice is scientifically accurate?"
    )
    sol = (
        "**Comparison Summary:**\n"
        "- **Incandescent ($60\\text{ W}$):** ~$1\\,200\\text{ h}$ lifespan, mercury-free, very inefficient.\n"
        "- **CFL ($15\\text{ W}$):** ~$8\\,000\\text{ h}$ lifespan, efficient, but contains **toxic mercury** requiring safe hazardous recycling.\n"
        "- **LED ($8\\text{ W}$):** ~$50\\,000\\text{ h}$ lifespan, highest efficiency, and **mercury-free**.\n\n"
        f"**Conclusion:** {correct}"
    )
    return _q(
        rng, "45", "45_environmental_hazard_mercury_in_cfl_vs_led_lifespan", prompt, correct, sol, 2, "mcq",
        ["thinking_cfl_energy_savers_are_mercury_free"],
        "Recall which bulb contains toxic mercury inside its spiral tube and which solid-state bulb lasts 50 000 h.",
        correct,
        correct,
        options=options,
    )


def arch_46_household_conservation_geyser_blanket_and_thermostat(rng: random.Random) -> Dict[str, Any]:
    strategy = rng.choice([
        ("installing a geyser thermal insulation blanket and lagging hot-water pipes", "traps thermal energy inside the cylinder and pipes, slowing heat loss into cold roof cavities so the thermostat activates the high-power heating element far less often"),
        ("lowering a geyser thermostat from 70 °C to 55 °C and fitting a timer", "reduces the temperature difference with the surrounding roof air (slowing heat loss) and avoids keeping water scalding hot during empty daytime hours"),
        ("installing a solar water heater (SWH) on a north-facing roof", "uses free solar thermal radiation to preheat household water, drastically cutting or replacing electrical geyser demand"),
        ("washing laundry in cold water and placing lids on cooking pots", "eliminates the massive electrical energy normally required to heat water inside a washing machine and traps steam heat inside pots so food cooks faster"),
    ])
    action, mechanism = strategy
    prompt = (
        f"Because water heating typically accounts for over 40% of a South African home's electricity bill, energy auditors recommend **{action}**.\n\n"
        "Explain **scientifically** how this conservation measure reduces monthly $\\text{kWh}$ consumption [2]."
    )
    correct = f"It {mechanism}."
    sol = (
        "**Step 1 — Physics of Thermal Energy Loss:** Heating water demands very high electrical power ($2\\,000 - 4\\,800\\text{ W}$).\n\n"
        f"**Step 2 — Conservation Effect:** By {action}, the household {mechanism} [2]."
    )
    return _q(
        rng, "46", "46_household_conservation_geyser_blanket_and_thermostat", prompt, correct, sol, 2, "short_answer",
        ["thinking_geyser_blankets_generate_electricity_themselves"],
        "Focus on how heat loss or high-power heating duration is reduced.",
        correct,
        correct,
    )


def arch_47_eliminating_standby_vampire_power_annual_savings(rng: random.Random) -> Dict[str, Any]:
    tv_w = rng.choice([8, 10, 12])
    dec_w = rng.choice([12, 15, 18])
    mw_w = rng.choice([3, 4, 5])
    chg_w = rng.choice([2, 3, 4])
    devices = [("Smart TV", tv_w), ("Decoder", dec_w), ("Microwave", mw_w), ("Charger", chg_w)]
    total_w = sum(w for _, w in devices)
    idle_hrs = rng.choice([16, 18, 20])
    rate_r = rng.choice([2.40, 2.60, 2.85])
    annual_kwh = round((total_w / 1000.0) * idle_hrs * 365.0, 2)
    annual_r = round(annual_kwh * rate_r, 2)
    d_spec = _svg_standby_power_strip(devices)
    prompt = (
        "Inspect the multi-plug standby load schematic shown below. Four household devices remain switched ON at the wall socket for "
        f"**${idle_hrs}\\text{{ hours}}$ every idle night and day** over $365\\text{{ days}}$ (even when turned off by remote control).\n\n"
        "1. Calculate the **total standby ('vampire') power** in **watts** and **kilowatts** [2].\n"
        f"2. Calculate how much **energy ($\\text{{kWh}}$)** and **money (at R ${_fmt_tex_fixed(rate_r, 2)}/\\text{{kWh}}$)** is wasted per year unless switched off at the wall [3]."
    )
    correct = f"{total_w} W ({_fmt_num(total_w / 1000.0, 3)} kW); {_fmt_fixed(annual_kwh, 2)} kWh/year; R {_fmt_fixed(annual_r, 2)}/year"
    sol = (
        "**Step 1 — Combined Standby Power:**\n"
        f"$$P = {tv_w} + {dec_w} + {mw_w} + {chg_w} = {total_w}\\text{{ W}} = {_fmt_tex(total_w / 1000.0, 3)}\\text{{ kW}}$$ [2]\n\n"
        "**Step 2 — Annual Standby Energy Wasted:**\n"
        f"$$E = {_fmt_tex(total_w / 1000.0, 3)}\\text{{ kW}} \\times {idle_hrs}\\text{{ h/day}} \\times 365\\text{{ days}} = {_fmt_tex_fixed(annual_kwh, 2)}\\text{{ kWh}}$$ [2]\n\n"
        "**Step 3 — Annual Financial Savings:**\n"
        f"$$\\text{{Savings}} = {_fmt_tex_fixed(annual_kwh, 2)} \\times \\text{{R }}\\,{_fmt_tex_fixed(rate_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(annual_r, 2)}$$ [1]"
    )
    return _q(
        rng, "47", "47_eliminating_standby_vampire_power_annual_savings", prompt, correct, sol, 5, "calculation",
        ["believing_appliances_turned_off_by_remote_draw_zero_electricity"],
        "Sum all 4 idle wattages, divide by 1 000 for kW, then multiply by idle hours x 365 days.",
        f"Total = {total_w} W; Annual energy = {_fmt_fixed(annual_kwh, 2)} kWh; Saved = R {_fmt_fixed(annual_r, 2)}.",
        correct,
        diagram_spec=d_spec,
    )


def arch_48_knock_on_grid_coal_and_greenhouse_gas_reduction(rng: random.Random) -> Dict[str, Any]:
    pct_drop = rng.choice([15, 20, 25, 30])
    coal_kg = rng.choice([450, 600, 750, 900])
    prompt = (
        f"Suppose millions of South African households cut their electricity usage by **${pct_drop}\\%$** — saving enough power to avoid burning **${coal_kg}\\text{{ tonnes}}$** of coal daily at Eskom power stations.\n\n"
        "Trace the three-step positive **knock-on environmental chain** connecting lower household electricity usage to climate change mitigation [3]."
    )
    correct = "1) Lower household usage reduces total demand on the national electricity grid; 2) Power stations burn less coal (conserving non-renewable fossil fuels); 3) Fewer greenhouse gases (especially carbon dioxide, CO2) and air pollutants are emitted into the atmosphere, slowing global warming."
    sol = (
        "**Step 1 — Grid Demand:** Saving electricity at home lowers total demand on the Eskom national grid (reducing peak overloads/load-shedding) [1].\n\n"
        "**Step 2 — Fossil Fuel Conservation:** Because South Africa generates most electricity from coal-fired power stations, lower demand means less coal is burned [1].\n\n"
        "**Step 3 — Greenhouse Gas Reduction:** Burning less coal cuts emissions of $\\text{CO}_2$ and sulfur/nitrogen oxides, reducing air pollution and mitigating climate change [1]."
    )
    return _q(
        rng, "48", "48_knock_on_grid_coal_and_greenhouse_gas_reduction", prompt, correct, sol, 3, "short_answer",
        ["disconnecting_household_kwh_savings_from_coal_power_station_emissions"],
        "Trace the chain: Home kWh -> National grid demand -> Coal burned -> Greenhouse gas emissions.",
        correct,
        correct,
    )


def arch_49_careers_and_roles_in_south_african_energy_sector(rng: random.Random) -> Dict[str, Any]:
    role = rng.choice([
        ("Energy Auditor", "inspects buildings, measures appliance kWh consumption, identifies energy waste, and recommends LED or thermal upgrades to cut costs"),
        ("Electrical Engineer", "designs high-voltage transmission networks, transformers, power station generators, and smart renewable energy systems"),
        ("Qualified Electrician", "installs, tests, and maintains safe household and industrial wiring, earth-leakage protection, and distribution boards"),
        ("IT Grid Specialist", "develops smart-metering software and automated grid-monitoring systems to balance electricity supply and demand in real time"),
        ("Renewable Energy Technician", "installs and services solar photovoltaic panels, inverters, and wind turbine power equipment"),
    ])
    title_role, desc = role
    others = [
        "performs dental surgery and orthodontic fittings",
        "forecasts ocean fish migration routes for trawlers",
        "designs clothing textiles from synthetic dyes",
    ]
    options = [desc.capitalize() + "."] + [o.capitalize() + "." for o in others]
    rng.shuffle(options)
    correct = desc.capitalize() + "."
    prompt = (
        f"In the South African electrical energy sector, what is the primary professional responsibility of an **{title_role}**?"
    )
    sol = (
        f"**Career Profile — {title_role}:**\n"
        f"An **{title_role}** {desc}."
    )
    return _q(
        rng, "49", "49_careers_and_roles_in_south_african_energy_sector", prompt, correct, sol, 2, "mcq",
        ["confusing_electrical_sector_careers"],
        f"Match the title '{title_role}' to its electrical energy and grid function.",
        correct,
        correct,
        options=options,
    )


def arch_50_capstone_household_energy_audit_tariff_and_efficiency(rng: random.Random) -> Dict[str, Any]:
    base_kwh = rng.choice([24.0, 28.0, 32.0])
    retro_kwh = rng.choice([15.0, 17.5, 20.0])
    rate_r = rng.choice([2.40, 2.60, 2.80])
    daily_saved = round(base_kwh - retro_kwh, 2)
    monthly_saved_kwh = round(daily_saved * 30.0, 2)
    monthly_saved_r = round(monthly_saved_kwh * rate_r, 2)
    pct_cut = round((daily_saved / base_kwh) * 100.0, 1)
    d_spec = _svg_home_audit_comparison(base_kwh, retro_kwh, rate_r)
    prompt = (
        "Examine the Home Energy Audit comparison diagram below. A family upgraded from an uninsulated geyser and incandescent bulbs to a geyser blanket and LED lighting.\n\n"
        "1. Calculate the **daily** and **30-day monthly $\\text{kWh}$** saved [2].\n"
        "2. Calculate the **percentage reduction** in daily energy use [2].\n"
        f"3. At **R ${_fmt_tex_fixed(rate_r, 2)}/\\text{{kWh}}$**, calculate the **monthly Rand savings** and state one positive environmental effect on Eskom's coal grid [2]."
    )
    correct = f"{_fmt_num(daily_saved, 2)} kWh/day ({_fmt_num(monthly_saved_kwh, 2)} kWh/month); {_fmt_num(pct_cut, 1)}% reduction; R {_fmt_fixed(monthly_saved_r, 2)} saved/month; Reduces coal burnt and CO2 emissions."
    sol = (
        "**Step 1 — Daily & Monthly Energy Saved:**\n"
        f"$$\\Delta E_{{\\text{{day}}}} = {_fmt_tex(base_kwh, 2)} - {_fmt_tex(retro_kwh, 2)} = {_fmt_tex(daily_saved, 2)}\\text{{ kWh/day}}$$\n"
        f"$$\\Delta E_{{\\text{{month}}}} = {_fmt_tex(daily_saved, 2)} \\times 30 = {_fmt_tex(monthly_saved_kwh, 2)}\\text{{ kWh/month}}$$ [2]\n\n"
        "**Step 2 — Percentage Energy Reduction:**\n"
        f"$$\\%\\text{{ Cut}} = \\frac{{{_fmt_tex(daily_saved, 2)}}}{{{_fmt_tex(base_kwh, 2)}}} \\times 100\\% = {_fmt_tex(pct_cut, 1)}\\%$$ [2]\n\n"
        "**Step 3 — Monthly Rand Savings & Environmental Impact:**\n"
        f"$$\\text{{Savings}} = {_fmt_tex(monthly_saved_kwh, 2)} \\times \\text{{R }}\\,{_fmt_tex_fixed(rate_r, 2)} = \\text{{R }}\\,{_fmt_tex_fixed(monthly_saved_r, 2)}$$ [1]\n"
        "Lower household demand eases pressure on the national grid, reduces coal combustion, and lowers greenhouse gas ($\\text{CO}_2$) emissions [1]."
    )
    return _q(
        rng, "50", "50_capstone_household_energy_audit_tariff_and_efficiency", prompt, correct, sol, 6, "structured",
        ["failing_to_integrate_energy_savings_cost_and_emissions"],
        "Subtract after-retrofit kWh from baseline kWh, multiply by 30 days, and multiply by the Rand rate.",
        f"Saved {_fmt_num(monthly_saved_kwh, 2)} kWh/month ({_fmt_num(pct_cut, 1)}%) = R {_fmt_fixed(monthly_saved_r, 2)}/month.",
        correct,
        diagram_spec=d_spec,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_reading_domestic_electricity_meter_kwh_difference": arch_26_reading_domestic_electricity_meter_kwh_difference,
    "27_calculating_electricity_cost_cents_to_rands_conversion": arch_27_calculating_electricity_cost_cents_to_rands_conversion,
    "28_single_appliance_operating_cost_watts_hours_tariff": arch_28_single_appliance_operating_cost_watts_hours_tariff,
    "29_comparing_cooking_cost_microwave_vs_conventional_oven": arch_29_comparing_cooking_cost_microwave_vs_conventional_oven,
    "30_multi_unit_lighting_cost_school_week_or_home": arch_30_multi_unit_lighting_cost_school_week_or_home,
    "31_household_daily_appliance_survey_to_monthly_bill": arch_31_household_daily_appliance_survey_to_monthly_bill,
    "32_purpose_of_tiered_inclining_block_electricity_tariffs": arch_32_purpose_of_tiered_inclining_block_electricity_tariffs,
    "33_interpreting_eskom_block_tariff_step_graph_and_rate": arch_33_interpreting_eskom_block_tariff_step_graph_and_rate,
    "34_calculating_tiered_inclining_block_electricity_bill": arch_34_calculating_tiered_inclining_block_electricity_bill,
    "35_electricity_bill_with_fixed_charge_and_15_percent_vat": arch_35_electricity_bill_with_fixed_charge_and_15_percent_vat,
    "36_auditing_municipal_electricity_statement_errors": arch_36_auditing_municipal_electricity_statement_errors,
    "37_eskom_direct_vs_municipal_tariff_variations": arch_37_eskom_direct_vs_municipal_tariff_variations,
    "38_prepaid_electricity_voucher_kwh_units_purchased": arch_38_prepaid_electricity_voucher_kwh_units_purchased,
    "39_prepaid_meter_credit_longevity_hours_and_days": arch_39_prepaid_meter_credit_longevity_hours_and_days,
    "40_reverse_cost_to_operating_time_or_appliance_power": arch_40_reverse_cost_to_operating_time_or_appliance_power,
    "41_thermostat_cycling_in_fridges_and_geysers": arch_41_thermostat_cycling_in_fridges_and_geysers,
    "42_sankey_efficiency_incandescent_cfl_led_comparison": arch_42_sankey_efficiency_incandescent_cfl_led_comparison,
    "43_percentage_energy_saved_led_bulb_upgrade": arch_43_percentage_energy_saved_led_bulb_upgrade,
    "44_annual_running_cost_and_payback_bulb_comparison": arch_44_annual_running_cost_and_payback_bulb_comparison,
    "45_environmental_hazard_mercury_in_cfl_vs_led_lifespan": arch_45_environmental_hazard_mercury_in_cfl_vs_led_lifespan,
    "46_household_conservation_geyser_blanket_and_thermostat": arch_46_household_conservation_geyser_blanket_and_thermostat,
    "47_eliminating_standby_vampire_power_annual_savings": arch_47_eliminating_standby_vampire_power_annual_savings,
    "48_knock_on_grid_coal_and_greenhouse_gas_reduction": arch_48_knock_on_grid_coal_and_greenhouse_gas_reduction,
    "49_careers_and_roles_in_south_african_energy_sector": arch_49_careers_and_roles_in_south_african_energy_sector,
    "50_capstone_household_energy_audit_tariff_and_efficiency": arch_50_capstone_household_energy_audit_tariff_and_efficiency,
}
