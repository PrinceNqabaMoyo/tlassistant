"""Physical Sciences (Grades 10 & 11) — Electrostatics Archetypes 01 to 25.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Grade 10 Term 2: Two types of charge, attraction/repulsion, charging by contact/induction,
  Principle of conservation of charge: Q_new = (Q1 + Q2) / 2,
  Principle of charge quantization: Q = n * e (where e = 1.6 * 10^-19 C).
- Grade 11 Term 2: Coulomb's Law: F = k * Q1 * Q2 / r^2 (k = 9.0 * 10^9 N*m^2/C^2),
  collinear 1D multi-charge forces, 2D perpendicular multi-charge forces,
  Electric fields: E = F / q and E = k * Q / r^2, field line patterns,
  neutral points, uniform field between parallel plates, and Millikan oil drop balance.

100% deterministic, SymPy/math backed, zero-LLM, compliant with 6-pillar contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

K_COULOMB = 9.0e9          # N*m^2/C^2
E_CHARGE = 1.6e-19         # C (elementary charge magnitude)
M_ELECTRON = 9.11e-31      # kg (electron mass)
G_ACCEL = 9.8              # m/s^2 (gravitational acceleration)


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Format number with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_sci(val: float, decimals: int = 2) -> str:
    """Format scientific notation with South African comma decimal separator."""
    exponent = int(math.floor(math.log10(abs(val)))) if val != 0 else 0
    mantissa = val / (10 ** exponent) if val != 0 else 0.0
    mant_str = f"{mantissa:.{decimals}f}".rstrip("0").rstrip(".").replace(".", ",")
    return f"{mant_str} \\times 10^{{{exponent}}}"


def _clean_svg(svg: str) -> str:
    """Trim leading/trailing whitespace from SVG strings."""
    return svg.strip()


# Archetype 01: Triboelectric charging and types of charge
def _b01_charge_types_and_triboelectric_series(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("glass rod", "silk cloth", "positive", "negative", "electrons transferred from glass to silk"),
        ("ebonite (hard rubber) rod", "wool or fur", "negative", "positive", "electrons transferred from wool/fur to ebonite"),
        ("perspex plastic rod", "woollen cloth", "positive", "negative", "electrons transferred from perspex to wool"),
        ("polythene rod", "dry woollen cloth", "negative", "positive", "electrons transferred from wool to polythene"),
    ]
    rod, cloth, rod_chg, cloth_chg, transfer_dir = r.choice(scenarios)
    q_mag_nc = r.choice([2, 3, 4, 5, 6, 8, 9, 12, 15, 18, 20, 24])

    svg = _clean_svg(f"""
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#f8fafc" rx="8"/>
  <rect x="40" y="80" width="160" height="24" rx="6" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
  <text x="120" y="96" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">{rod.title()} ({q_mag_nc} nC)</text>
  <path d="M 230,70 Q 280,50 330,75 Q 360,110 320,135 Q 260,140 230,110 Z" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="285" y="105" font-size="11" font-weight="bold" fill="#9a3412" text-anchor="middle">{cloth.title()}</text>
  <path d="M 180,75 C 205,55 215,65 240,75" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="245,75 235,70 238,78" fill="#2563eb"/>
  <text x="200" y="170" font-size="12" fill="#334155" text-anchor="middle">Triboelectric charging by friction (|Q| = {q_mag_nc} nC)</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a {rod} being rubbed with a piece of {cloth} until it acquires a charge magnitude of $|Q| = {q_mag_nc}\\text{{ nC}}$.\n\n"
        f"1. State whether the {rod} becomes positively charged or negatively charged after rubbing.\n"
        f"2. Explain this charging process in terms of the transfer of subatomic particles (protons or electrons)."
    )

    ans_latex = (
        rf"1.\; \text{{{rod.title()} becomes {rod_chg}.}}\n"
        rf"2.\; \text{{{transfer_dir.capitalize()}; protons remain stationary in nuclei.}}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Identify correct charge polarity ({rod_chg})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "State that only electrons are transferred (protons do not move)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"State direction of electron transfer: {transfer_dir}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_protons_moved", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Only electrons can move between materials during friction; positive protons stay bound in nuclei.",
        "tier_2": f"A material that loses electrons becomes positive; a material gaining electrons becomes negative.",
        "tier_3": f"For {rod} and {cloth}: {rod_chg} rod because {transfer_dir}.",
    }

    return {
        "id": f"ps_elec_tribo_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_tribo_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "01_charge_types_and_triboelectric_series",
        "learning_objective_id": "ps_elec_01_triboelectric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["protons_transferred_during_rubbing", "confused_positive_negative_polarity"],
        "keywords": ["triboelectric", "friction", "charge types", "electrons"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 3,
    }


# Archetype 02: Principle of conservation of charge (two identical spheres)
def _b02_principle_of_charge_conservation_two_spheres(r: random.Random) -> Dict[str, Any]:
    q1 = r.choice([-12, -10, -8, -6, -4, 2, 4, 6, 8, 10])
    q2 = r.choice([-8, -6, -4, 2, 4, 6, 8, 12, 14])
    while (q1 + q2) % 2 != 0 or q1 == q2:
        q2 = r.choice([-8, -6, -4, 2, 4, 6, 8, 12, 14])

    q_new = (q1 + q2) // 2

    svg = _clean_svg(f"""
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#f8fafc" rx="8"/>
  <!-- Sphere A -->
  <line x1="120" y1="110" x2="120" y2="170" stroke="#475569" stroke-width="4"/>
  <rect x="90" y="170" width="60" height="10" fill="#64748b" rx="2"/>
  <circle cx="120" cy="80" r="30" fill="#38bdf8" stroke="#0284c7" stroke-width="2.5"/>
  <text x="120" y="75" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Sphere A</text>
  <text x="120" y="95" font-size="11" fill="#0f172a" text-anchor="middle">{_fmt_sa(q1)} nC</text>
  <!-- Sphere B -->
  <line x1="280" y1="110" x2="280" y2="170" stroke="#475569" stroke-width="4"/>
  <rect x="250" y="170" width="60" height="10" fill="#64748b" rx="2"/>
  <circle cx="280" cy="80" r="30" fill="#f472b6" stroke="#db2777" stroke-width="2.5"/>
  <text x="280" y="75" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Sphere B</text>
  <text x="280" y="95" font-size="11" fill="#0f172a" text-anchor="middle">{_fmt_sa(q2)} nC</text>
  <text x="200" y="30" font-size="12" fill="#334155" text-anchor="middle">Identical conducting spheres on insulated stands</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing two identical insulated conducting spheres, $A$ and $B$, "
        f"carrying initial charges of $Q_A = {_fmt_sa(q1)}\\text{{ nC}}$ and $Q_B = {_fmt_sa(q2)}\\text{{ nC}}$ respectively.\n"
        f"The spheres are brought into contact with each other and then separated.\n\n"
        f"1. State the Principle of Conservation of Charge in words.\n"
        f"2. Calculate the final charge $Q_{{\\text{{new}}}}$ on each sphere after separation."
    )

    ans_latex = (
        rf"1.\; \text{{The net charge of an isolated system remains constant during any physical process.}}\n"
        rf"2.\; Q_{{\text{{new}}}} = \frac{{Q_A + Q_B}}{{2}} = \frac{{{q1} + ({q2})}}{{2}} = {_fmt_sa(q_new)}\text{{ nC}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State Principle of Conservation of Charge correctly", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: Q_new = (Q1 + Q2) / 2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct substitution and evaluation: {q_new} nC", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: An isolated system conserves total charge. Identical spheres share the net charge equally.",
        "tier_2": f"Use formula $Q_{{\\text{{new}}}} = \\frac{{Q_1 + Q_2}}{{2}}$. Pay close attention to positive and negative signs.",
        "tier_3": f"Substitute: ({q1} + {q2}) / 2 = {q_new} nC.",
    }

    return {
        "id": f"ps_elec_cons2_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_cons2_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "02_principle_of_charge_conservation_two_spheres",
        "learning_objective_id": "ps_elec_02_conservation_two",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["neglected_negative_sign_in_addition", "multiplied_charges_instead_of_adding"],
        "keywords": ["conservation of charge", "insulated stand", "contact", "separation"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 03: Sequential contact of three identical conducting spheres
def _b03_principle_of_charge_conservation_three_spheres(r: random.Random) -> Dict[str, Any]:
    qa = r.choice([-16, -12, 8, 12, 16])
    qb = r.choice([-8, -4, 4, 8])
    qc = 0  # neutral sphere C

    # First A touches B
    q_ab = (qa + qb) / 2
    # Then B touches C (which is initially neutral)
    q_bc = q_ab / 2

    prompt = (
        f"Three identical conducting spheres on insulated stands have initial charges:\n"
        f"$$Q_A = {_fmt_sa(qa)}\\text{{ nC}}, \\quad Q_B = {_fmt_sa(qb)}\\text{{ nC}}, \\quad Q_C = 0\\text{{ nC (neutral)}}$$\n"
        f"Sphere $A$ is touched to sphere $B$ and separated. Thereafter, sphere $B$ is touched to sphere $C$ and separated.\n\n"
        f"Calculate the final charge on:\n"
        f"1. Sphere $A$\n"
        f"2. Sphere $B$\n"
        f"3. Sphere $C$"
    )

    ans_latex = (
        rf"1.\; Q_A' = \frac{{{qa} + ({qb})}}{{2}} = {_fmt_sa(q_ab)}\text{{ nC}}\n"
        rf"2.\; Q_B' = \frac{{{_fmt_sa(q_ab)} + 0}}{{2}} = {_fmt_sa(q_bc)}\text{{ nC}}\n"
        rf"3.\; Q_C' = {_fmt_sa(q_bc)}\text{{ nC}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"First contact A and B: Q_A' = Q_B' = {q_ab} nC", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Second contact B and C: Q_B'' = Q_C' = {q_bc} nC", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "divided_by_three_simultaneously", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Perform the calculation in two sequential steps: contact 1, then contact 2.",
        "tier_2": f"Step 1: A and B share charge: ({qa} + {qb}) / 2 = {_fmt_sa(q_ab)} nC.",
        "tier_3": f"Step 2: B (now {_fmt_sa(q_ab)} nC) touches neutral C: ({_fmt_sa(q_ab)} + 0) / 2 = {_fmt_sa(q_bc)} nC.",
    }

    return {
        "id": f"ps_elec_cons3_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_cons3_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "03_principle_of_charge_conservation_three_spheres",
        "learning_objective_id": "ps_elec_03_conservation_three",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["simultaneous_sharing_instead_of_sequential", "forgot_neutral_charge_is_zero"],
        "keywords": ["sequential contact", "three spheres", "charge conservation"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 04: Quantization of charge (number of electrons)
def _b04_quantization_of_charge_number_of_electrons(r: random.Random) -> Dict[str, Any]:
    n_exp = r.choice([10, 11, 12, 13])
    n_base = r.choice([2, 3, 4, 5, 8])
    n_electrons = n_base * (10 ** n_exp)
    charge_c = n_electrons * E_CHARGE
    charge_nc = round(charge_c * 1e9, 2)
    polarity = r.choice(["negative", "positive"])

    if polarity == "negative":
        chg_text = f"-{_fmt_sa(charge_nc)}\\text{{ nC}}"
        process = "gained"
    else:
        chg_text = f"+{_fmt_sa(charge_nc)}\\text{{ nC}}"
        process = "lost"

    prompt = (
        f"A small conducting sphere acquires a net charge of $Q = {chg_text}$.\n\n"
        f"1. State the Principle of Charge Quantization in words.\n"
        f"2. Calculate the number of electrons {process} by the sphere during the charging process."
    )

    ans_latex = (
        rf"1.\; \text{{Every charge in the universe is an integer multiple of the elementary charge }} e.\n"
        rf"2.\; n = \frac{{|Q|}}{{e}} = \frac{{{_fmt_sa(charge_nc)} \times 10^{{-9}}}}{{1{{,}}6 \times 10^{{-19}}}} = {_fmt_sci(float(n_electrons))}\text{{ electrons}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of charge quantization principle", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: n = Q / e", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitution and calculation: {_fmt_sci(float(n_electrons))} electrons", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_nano_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Charge is quantized; $Q = n \\cdot e$, where $e = 1{,}6 \\times 10^{-19}\\text{ C}$.",
        "tier_2": f"Convert nano-coulombs to coulombs: $1\\text{{ nC}} = 10^{{-9}}\\text{{ C}}$.",
        "tier_3": f"Divide total charge by elementary charge: $n = ({_fmt_sa(charge_nc)} \\times 10^{{-9}}) / (1{{,}}6 \\times 10^{{-19}}) = {_fmt_sci(float(n_electrons))}$.",
    }

    return {
        "id": f"ps_elec_quant_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_quant_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "04_quantization_of_charge_number_of_electrons",
        "learning_objective_id": "ps_elec_04_quantization",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_nano_coulomb_factor", "divided_elementary_charge_by_Q"],
        "keywords": ["charge quantization", "elementary charge", "electrons"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 05: Mass change due to electron transfer during charging
def _b05_electron_mass_transfer_during_charging(r: random.Random) -> Dict[str, Any]:
    n_exp = r.choice([12, 13, 14])
    n_electrons = r.choice([2, 5, 8]) * (10 ** n_exp)
    q_c = n_electrons * E_CHARGE
    q_uc = round(q_c * 1e6, 3)
    delta_m = n_electrons * M_ELECTRON

    prompt = (
        f"A neutral polyethylene rod is rubbed with a woollen cloth and gains a net negative charge "
        f"of $Q = -{_fmt_sa(q_uc)}\\mu\\text{{C}}$.\n\n"
        f"1. Calculate the number of electrons transferred to the rod ($e = 1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$).\n"
        f"2. Given the mass of an electron $m_e = 9{{,}}11 \\times 10^{{-31}}\\text{{ kg}}$, calculate the change in mass ($\\Delta m$) of the rod."
    )

    ans_latex = (
        rf"1.\; n = \frac{{|Q|}}{{e}} = \frac{{{_fmt_sa(q_uc)} \times 10^{{-6}}}}{{1{{,}}6 \times 10^{{-19}}}} = {_fmt_sci(float(n_electrons))}\text{{ electrons}}\n"
        rf"2.\; \Delta m = n \cdot m_e = ({_fmt_sci(float(n_electrons))}) \times (9{{,}}11 \times 10^{{-31}}) = {_fmt_sci(delta_m)}\text{{ kg}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: n = Q / e", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of n = {_fmt_sci(float(n_electrons))} electrons", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula: delta m = n * m_e", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation of delta m = {_fmt_sci(delta_m)} kg", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_micro_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: $Q = n \\cdot e$, so $n = Q/e$. Each electron has mass $m_e = 9{,}11 \\times 10^{-31}\\text{ kg}$.",
        "tier_2": f"Convert $\\mu\\text{{C}}$ to $\\text{{C}}$: ${q_uc} \\times 10^{{-6}}\\text{{ C}}$. Find $n$, then $\\Delta m = n \\times m_e$.",
        "tier_3": f"$n = {_fmt_sci(float(n_electrons))}$, $\\Delta m = {_fmt_sci(delta_m)}\\text{{ kg}}$.",
    }

    return {
        "id": f"ps_elec_mass_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_mass_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "05_electron_mass_transfer_during_charging",
        "learning_objective_id": "ps_elec_05_electron_mass",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["neglected_micro_conversion", "claimed_mass_decreased_when_gaining_electrons"],
        "keywords": ["electron mass", "mass change", "microcoulombs"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 06: Gold-leaf electroscope and induction
def _b06_electroscope_leaf_divergence_and_induction(r: random.Random) -> Dict[str, Any]:
    rod_type = r.choice(["negatively charged", "positively charged"])
    gap_mm = r.choice([10, 12, 15, 18, 20, 22, 25, 28, 30, 35])
    opposite_chg = "positive" if rod_type == "negatively charged" else "negative"
    same_chg = "negative" if rod_type == "negatively charged" else "positive"

    svg = _clean_svg(f"""
<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="240" fill="#f8fafc" rx="8"/>
  <!-- Rod -->
  <rect x="30" y="30" width="120" height="18" rx="4" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="90" y="44" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">{rod_type.title()} Rod ({gap_mm} mm)</text>
  <!-- Cap / Disc -->
  <circle cx="200" cy="50" r="24" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
  <!-- Stem -->
  <line x1="200" y1="74" x2="200" y2="150" stroke="#d97706" stroke-width="4"/>
  <!-- Leaves -->
  <line x1="200" y1="150" x2="175" y2="190" stroke="#d97706" stroke-width="2.5"/>
  <line x1="200" y1="150" x2="225" y2="190" stroke="#d97706" stroke-width="2.5"/>
  <!-- Glass casing -->
  <rect x="150" y="90" width="100" height="120" rx="8" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="200" y="230" font-size="11" fill="#475569" text-anchor="middle">Gold-leaf electroscope (air gap {gap_mm} mm)</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a {rod_type} rod brought within an air gap of ${gap_mm}\\text{{ mm}}$ (without touching) "
        f"near the metal cap of an uncharged gold-leaf electroscope.\n\n"
        f"1. State what happens to the gold leaves of the electroscope.\n"
        f"2. Explain why this observation occurs in terms of electron movement within the electroscope.\n"
        f"3. If the cap is now briefly touched by a human finger (earthed) while the rod remains in place, "
        f"and the finger is then removed followed by the rod, what permanent charge will the electroscope retain?"
    )

    ans_latex = (
        rf"1.\; \text{{The gold leaves diverge (repel each other).}}\n"
        rf"2.\; \text{{Electrons in the cap are {('repelled downward to' if rod_type == 'negatively charged' else 'attracted upward from')} the leaves, leaving both leaves with like {same_chg} charges that repel.}}\n"
        rf"3.\; \text{{The electroscope retains a permanent net {opposite_chg} charge (charging by induction).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State that the leaves diverge / spread apart", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Explain electron movement ({same_chg} charge on leaves)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Identify like charges repel on the leaves", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Permanent induced charge is opposite ({opposite_chg})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_protons_moved", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Electrostatic induction causes charges within the conductor to separate.",
        "tier_2": f"Near a {rod_type} rod, electrons move so that the cap gets {opposite_chg} charge and the leaves get {same_chg} charge.",
        "tier_3": f"When earthed, electrons flow {('to ground' if rod_type == 'negatively charged' else 'from ground')}, leaving a net {opposite_chg} charge.",
    }

    return {
        "id": f"ps_elec_scope_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_scope_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "06_electroscope_leaf_divergence_and_induction",
        "learning_objective_id": "ps_elec_06_electroscope",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["induction_gives_same_charge_as_rod", "neutral_objects_do_not_interact"],
        "keywords": ["electroscope", "induction", "divergence", "earthing"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 07: Polarisation of neutral insulators
def _b07_polarisation_of_neutral_insulators(r: random.Random) -> Dict[str, Any]:
    obj = r.choice(["small neutral pieces of paper", "a thin stream of falling water", "a neutral lightweight polystyrene sphere"])
    charged_item = r.choice(["negatively charged plastic comb", "positively charged glass rod"])
    dist_mm = r.choice([5, 8, 10, 12, 15, 18, 20, 25, 30])

    prompt = (
        f"A learner notices that when a {charged_item} is brought to a distance of ${dist_mm}\\text{{ mm}}$ from {obj}, "
        f"they are attracted towards the charged item, even though they carry no net charge.\n\n"
        f"1. Name the physical phenomenon responsible for this attraction.\n"
        f"2. Explain, with reference to the atomic distribution of charge, why a net attractive force occurs."
    )

    ans_latex = (
        rf"1.\; \text{{Polarisation (induced dipole / charge separation in neutral matter).}}\n"
        rf"2.\; \text{{The charged item causes electron clouds within the neutral molecules to shift slightly, "
        rf"bringing opposite charges closer than like charges. Because electrostatic force decreases with distance "
        rf"($F \propto 1/r^2$), the attractive force between closer opposite charges exceeds the repulsive force, producing a net attraction.}}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Identify phenomenon as polarisation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explain shift of electron clouds creating dipoles", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "State that closer opposite charges experience stronger attractive force (inverse-square law)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Neutral insulators do not have free-flowing electrons, but their molecular electron clouds can distort.",
        "tier_2": "This distortion is called polarisation.",
        "tier_3": "The opposite charges are closer to the charged comb than like charges; hence attraction > repulsion.",
    }

    return {
        "id": f"ps_elec_polar_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_polar_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "07_polarisation_of_neutral_insulators",
        "learning_objective_id": "ps_elec_07_polarisation",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["believed_neutral_matter_has_no_electrons", "confused_conduction_with_polarisation"],
        "keywords": ["polarisation", "neutral insulator", "induced dipole", "attraction"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 3,
    }


# Archetype 08: Coulomb's Law direct calculation between two point charges
def _b08_coulombs_law_two_point_charges_direct(r: random.Random) -> Dict[str, Any]:
    # Q1 and Q2 in microcoulombs or nanocoulombs
    q1_val = r.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    q2_val = r.choice([2.0, 4.0, 5.0, 8.0])
    sign1 = r.choice([1, -1])
    sign2 = r.choice([1, -1])
    q1_c = sign1 * q1_val * 1e-6
    q2_c = sign2 * q2_val * 1e-6

    # distance in centimetres
    r_cm = r.choice([10.0, 15.0, 20.0, 25.0, 30.0])
    r_m = r_cm / 100.0

    force = K_COULOMB * abs(q1_c * q2_c) / (r_m ** 2)
    nature = "repulsive" if sign1 * sign2 > 0 else "attractive"

    svg = _clean_svg(f"""
<svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="160" fill="#f8fafc" rx="8"/>
  <circle cx="100" cy="80" r="20" fill="{'#38bdf8' if sign1 > 0 else '#f87171'}" stroke="#0f172a" stroke-width="2"/>
  <text x="100" y="85" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{'+' if sign1 > 0 else '-'}{_fmt_sa(q1_val)} μC</text>
  <circle cx="300" cy="80" r="20" fill="{'#38bdf8' if sign2 > 0 else '#f87171'}" stroke="#0f172a" stroke-width="2"/>
  <text x="300" y="85" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{'+' if sign2 > 0 else '-'}{_fmt_sa(q2_val)} μC</text>
  <line x1="100" y1="120" x2="300" y2="120" stroke="#475569" stroke-width="1.5"/>
  <polygon points="100,117 92,120 100,123" fill="#475569"/>
  <polygon points="300,117 308,120 300,123" fill="#475569"/>
  <text x="200" y="138" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">r = {_fmt_sa(r_cm)} cm</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing two point charges, $Q_1 = {'+' if sign1 > 0 else '-'}{_fmt_sa(q1_val)}\\mu\\text{{C}}$ "
        f"and $Q_2 = {'+' if sign2 > 0 else '-'}{_fmt_sa(q2_val)}\\mu\\text{{C}}$, separated by a distance of $r = {_fmt_sa(r_cm)}\\text{{ cm}}$ in a vacuum.\n\n"
        f"1. State Coulomb's Law in words.\n"
        f"2. Calculate the magnitude of the electrostatic force exerted by $Q_1$ on $Q_2$.\n"
        f"3. State whether the force is attractive or repulsive."
    )

    ans_latex = (
        rf"1.\; \text{{The magnitude of the electrostatic force exerted by two point charges on each other "
        rf"is directly proportional to the product of the magnitudes of the charges and inversely proportional "
        rf"to the square of the distance between them.}}\n"
        rf"2.\; F = \frac{{k |Q_1 Q_2|}}{{r^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_val)} \times 10^{{-6}})({_fmt_sa(q2_val)} \times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(force, 2)}\text{{ N}}\n"
        rf"3.\; \text{{{nature.capitalize()}}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of Coulomb's Law", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: F = k * Q1 * Q2 / r^2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct substitution (including cm to m and micro to 10^-6) and calculation ({_fmt_sa(force, 2)} N)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"State nature: {nature}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "omitted_square_on_distance", "penalty": -1},
            {"rule": "forgot_micro_conversion", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall Coulomb's Law: $F = k \\frac{|Q_1 Q_2|}{r^2}$. Always convert cm to metres and $\\mu\\text{C}$ to coulombs ($10^{-6}\\text{ C}$).",
        "tier_2": f"Here $r = {_fmt_sa(r_cm)}\\text{{ cm}} = {_fmt_sa(r_m)}\\text{{ m}}$. Square of distance: $({_fmt_sa(r_m)})^2$.",
        "tier_3": f"Calculate: $F = (9 \\times 10^9 \\times {_fmt_sa(q1_val)} \\times 10^{{-6}} \\times {_fmt_sa(q2_val)} \\times 10^{{-6}}) / ({_fmt_sa(r_m)})^2 = {_fmt_sa(force, 2)}\\text{{ N}}$ ({nature}).",
    }

    return {
        "id": f"ps_elec_coul_dir_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_coul_dir_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "08_coulombs_law_two_point_charges_direct",
        "learning_objective_id": "ps_elec_08_coulomb_direct",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_square_on_distance", "failed_cm_to_m_conversion", "included_negative_signs_in_force_magnitude"],
        "keywords": ["Coulomb's Law", "electrostatic force", "point charges", "microcoulombs"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 09: Coulomb's Law proportionality and scaling factors
def _b09_coulombs_law_proportionality_scaling(r: random.Random) -> Dict[str, Any]:
    f_orig = r.choice([24, 36, 48, 72, 96, 120])
    scenario_type = r.choice([
        ("distance doubled, charge Q1 doubled", 2, 0.5, 2 * 0.5**2, "2 / 2^2 = 1/2"),
        ("distance tripled", 1, 1/3, (1/3)**2, "1 / 3^2 = 1/9"),
        ("distance halved", 1, 2, 2**2, "1 / (1/2)^2 = 4"),
        ("both charges doubled and distance doubled", 4, 0.5, 4 * 0.5**2, "2 * 2 / 2^2 = 1"),
    ])
    desc, q_factor, r_factor, net_factor, factor_expl = scenario_type
    f_new = round(f_orig * net_factor, 2)

    prompt = (
        f"Two point charges exert an electrostatic force of magnitude $F = {f_orig}\\text{{ N}}$ on each other.\n\n"
        f"Determine the new electrostatic force when the {desc}."
    )

    ans_latex = (
        rf"F \propto \frac{{Q_1 Q_2}}{{r^2}} \implies F_{{\text{{new}}}} = F \times ({factor_expl}) = "
        rf"{f_orig} \times {_fmt_sa(net_factor, 3)} = {_fmt_sa(f_new)}\\text{{ N}}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "State proportionality F proportional to Q1*Q2 / r^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Determine net factor = {factor_expl}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate new force = {_fmt_sa(f_new)} N", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "linear_distance_scaling", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: $F \\propto 1/r^2$. Changing distance by factor $k$ changes force by factor $1/k^2$.",
        "tier_2": f"Here, {desc}. Net scaling factor is {factor_expl}.",
        "tier_3": f"New force = {f_orig} * {factor_expl} = {_fmt_sa(f_new)} N.",
    }

    return {
        "id": f"ps_elec_prop_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_prop_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "09_coulombs_law_proportionality_scaling",
        "learning_objective_id": "ps_elec_09_proportionality",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["linear_distance_scaling_without_squaring", "inverted_factor"],
        "keywords": ["proportionality", "scaling", "inverse-square law"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 3,
    }


# Archetype 10: Coulomb's Law: solve for separation distance r
def _b10_coulombs_law_solve_for_separation_distance(r: random.Random) -> Dict[str, Any]:
    q1_uc = r.choice([2.0, 3.0, 4.0, 5.0])
    q2_uc = r.choice([3.0, 5.0, 6.0, 8.0])
    # Pick target distance r in cm: 10, 15, 20, 25, 30 cm
    target_r_cm = r.choice([10.0, 15.0, 20.0, 25.0])
    target_r_m = target_r_cm / 100.0
    f_val = round(K_COULOMB * (q1_uc * 1e-6) * (q2_uc * 1e-6) / (target_r_m ** 2), 2)

    prompt = (
        f"Two point charges of $Q_1 = {_fmt_sa(q1_uc)}\\mu\\text{{C}}$ and $Q_2 = {_fmt_sa(q2_uc)}\\mu\\text{{C}}$ "
        f"experience an electrostatic repulsive force of magnitude $F = {_fmt_sa(f_val)}\\text{{ N}}$.\n\n"
        f"Calculate the distance of separation $r$ between the two charges in metres (and in centimetres)."
    )

    ans_latex = (
        rf"r^2 = \frac{{k Q_1 Q_2}}{{F}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{{_fmt_sa(f_val)}}} "
        rf"= {_fmt_sa(target_r_m**2, 4)}\\text{{ m}}^2\n"
        rf"r = \sqrt{{{_fmt_sa(target_r_m**2, 4)}}} = {_fmt_sa(target_r_m, 3)}\\text{{ m}} = {_fmt_sa(target_r_cm)}\\text{{ cm}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: F = k * Q1 * Q2 / r^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Rearrange: r = sqrt(k * Q1 * Q2 / F)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct substitution with micro to 10^-6", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Answer: {target_r_m} m ({target_r_cm} cm)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_square_root", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Rearrange Coulomb's formula to make $r^2$ the subject: $r^2 = \\frac{k Q_1 Q_2}{F}$.",
        "tier_2": "Take the square root of both sides: $r = \\sqrt{\\frac{k Q_1 Q_2}{F}}$.",
        "tier_3": f"Evaluate: $r = \\sqrt{{(9 \\times 10^9 \\times {q1_uc} \\times 10^{{-6}} \\times {q2_uc} \\times 10^{{-6}}) / {f_val}}} = {_fmt_sa(target_r_m)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_elec_dist_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_dist_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "10_coulombs_law_solve_for_separation_distance",
        "learning_objective_id": "ps_elec_10_separation_distance",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_square_root_r_squared", "algebraic_inversion_error"],
        "keywords": ["separation distance", "Coulomb's Law", "rearranging formula"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 11: Coulomb's Law: identical unknown charges
def _b11_coulombs_law_solve_for_unknown_charge(r: random.Random) -> Dict[str, Any]:
    target_q_uc = r.choice([2.0, 3.0, 4.0, 5.0, 8.0])
    target_q_c = target_q_uc * 1e-6
    r_cm = r.choice([5.0, 10.0, 15.0, 20.0])
    r_m = r_cm / 100.0
    f_val = round(K_COULOMB * (target_q_c ** 2) / (r_m ** 2), 2)

    prompt = (
        f"Two identical small conducting spheres carry equal charges of magnitude $Q$.\n"
        f"When placed a distance of $r = {_fmt_sa(r_cm)}\\text{{ cm}}$ apart in a vacuum, "
        f"they repel each other with an electrostatic force of $F = {_fmt_sa(f_val)}\\text{{ N}}$.\n\n"
        f"Calculate the magnitude of the charge $Q$ on each sphere in microcoulombs ($\\mu\\text{{C}}$)."
    )

    ans_latex = (
        rf"F = \frac{{k Q^2}}{{r^2}} \implies Q^2 = \frac{{F r^2}}{{k}} = \frac{{{_fmt_sa(f_val)} \times ({_fmt_sa(r_m)})^2}}{{9{{,}}0 \times 10^9}}\n"
        rf"Q = \sqrt{{\frac{{{_fmt_sa(f_val)} \times ({_fmt_sa(r_m)})^2}}{{9{{,}}0 \times 10^9}}}} = {_fmt_sci(target_q_c)}\\text{{ C}} = {_fmt_sa(target_q_uc)}\\mu\\text{{C}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: F = k * Q^2 / r^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Rearrange for Q = sqrt(F * r^2 / k)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Correct substitution with r in metres", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Answer: {target_q_uc} microcoulombs", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_square_root", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Since the charges are identical, $Q_1 = Q_2 = Q$, so $Q_1 Q_2 = Q^2$.",
        "tier_2": "Formula becomes $F = \\frac{k Q^2}{r^2} \\implies Q = \\sqrt{\\frac{F r^2}{k}}$.",
        "tier_3": f"Substitute $F = {f_val}\\text{{ N}}$ and $r = {_fmt_sa(r_m)}\\text{{ m}}$: $Q = {_fmt_sa(target_q_uc)}\\mu\\text{{C}}$.",
    }

    return {
        "id": f"ps_elec_ident_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_ident_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "11_coulombs_law_solve_for_unknown_charge",
        "learning_objective_id": "ps_elec_11_unknown_charge",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_square_root_Q_squared", "used_cm_without_converting_to_m"],
        "keywords": ["identical charges", "Coulomb's Law", "equal charge"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 12: Force after contact and return to original separation
def _b12_coulomb_force_after_contact_and_separation(r: random.Random) -> Dict[str, Any]:
    # Two charges touch, then return to original distance r
    q1 = r.choice([6.0, 8.0, 10.0])
    q2 = r.choice([-4.0, -2.0, -6.0])
    r_cm = r.choice([10.0, 20.0, 30.0])
    r_m = r_cm / 100.0

    f_initial = K_COULOMB * abs(q1 * 1e-6 * q2 * 1e-6) / (r_m ** 2)

    # After contact
    q_new = (q1 + q2) / 2.0
    f_final = K_COULOMB * (q_new * 1e-6) ** 2 / (r_m ** 2)

    prompt = (
        f"Two identical insulated conducting spheres, $P$ and $Q$, carry charges of "
        f"$Q_P = +{_fmt_sa(q1)}\\mu\\text{{C}}$ and $Q_Q = {_fmt_sa(q2)}\\mu\\text{{C}}$. "
        f"They are placed a distance of $r = {_fmt_sa(r_cm)}\\text{{ cm}}$ apart.\n\n"
        f"1. Calculate the initial electrostatic force between them, and state whether it is attractive or repulsive.\n"
        f"2. The spheres are allowed to touch each other and are then returned to their original positions. "
        f"Calculate the new electrostatic force between them."
    )

    ans_latex = (
        rf"1.\; F_{{\text{{initial}}}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1)} \times 10^{{-6}})({_fmt_sa(abs(q2))} \times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(f_initial, 2)}\text{{ N (attractive)}}\n"
        rf"2.\; Q_{{\text{{new}}}} = \frac{{{_fmt_sa(q1)} + ({_fmt_sa(q2)})}}{{2}} = {_fmt_sa(q_new)}\mu\text{{C}}\n"
        rf"F_{{\text{{final}}}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q_new)} \times 10^{{-6}})^2}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(f_final, 2)}\text{{ N (repulsive)}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Initial Coulomb force formula and substitution", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Initial force = {_fmt_sa(f_initial, 2)} N (attractive)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Charge conservation formula: Q_new = (Q1 + Q2) / 2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Q_new = {_fmt_sa(q_new)} uC", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Final Coulomb force substitution", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Final force = {_fmt_sa(f_final, 2)} N (repulsive)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_nature_of_force", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate initial force via $F = k \\frac{|Q_1 Q_2|}{r^2}$. Then find new charge $Q = (Q_1 + Q_2)/2$.",
        "tier_2": f"Both spheres now have $Q_{{\\text{{new}}}} = {_fmt_sa(q_new)}\\mu\\text{{C}}$. Calculate $F_{{\\text{{final}}}} = k \\frac{{Q_{{\\text{{new}}}}^2}}{{r^2}}$.",
        "tier_3": f"Initial: {_fmt_sa(f_initial, 2)} N (attractive). Final: {_fmt_sa(f_final, 2)} N (repulsive).",
    }

    return {
        "id": f"ps_elec_contact_f_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_contact_f_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "12_coulomb_force_after_contact_and_separation",
        "learning_objective_id": "ps_elec_12_force_after_contact",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_calculate_new_charge", "maintained_attraction_after_touching_identical_spheres"],
        "keywords": ["contact and separation", "Coulomb force", "charge sharing"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 13: Collinear 1D multi-charge arrangement: net force on centre charge
def _b13_collinear_three_charges_net_force_on_centre(r: random.Random) -> Dict[str, Any]:
    # Three collinear charges: Q1 at x=0, Q2 at x=r1, Q3 at x=r1+r2
    q1_uc = r.choice([2.0, 4.0, 6.0])
    q2_uc = r.choice([1.0, 2.0, 3.0])  # centre charge (positive)
    q3_uc = r.choice([3.0, 5.0, 6.0])

    r1_cm = r.choice([10.0, 15.0, 20.0])
    r2_cm = r.choice([10.0, 15.0, 20.0])
    r1_m = r1_cm / 100.0
    r2_m = r2_cm / 100.0

    # Let Q1 be positive, Q2 positive, Q3 positive
    # Force on Q2 from Q1: repulsive -> directed right (+x)
    f12 = K_COULOMB * (q1_uc * 1e-6) * (q2_uc * 1e-6) / (r1_m ** 2)
    # Force on Q2 from Q3: repulsive -> directed left (-x)
    f32 = K_COULOMB * (q3_uc * 1e-6) * (q2_uc * 1e-6) / (r2_m ** 2)

    f_net = f12 - f32
    direction = "to the right (away from Q1)" if f_net > 0 else "to the left (away from Q3)"
    f_net_mag = abs(f_net)

    svg = _clean_svg(f"""
<svg viewBox="0 0 450 160" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="160" fill="#f8fafc" rx="8"/>
  <line x1="60" y1="80" x2="390" y2="80" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Q1 -->
  <circle cx="80" cy="80" r="18" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
  <text x="80" y="85" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">+{_fmt_sa(q1_uc)}μC</text>
  <text x="80" y="50" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Q₁</text>
  <!-- Q2 -->
  <circle cx="225" cy="80" r="18" fill="#a78bfa" stroke="#7c3aed" stroke-width="2"/>
  <text x="225" y="85" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">+{_fmt_sa(q2_uc)}μC</text>
  <text x="225" y="50" font-size="11" font-weight="bold" fill="#7c3aed" text-anchor="middle">Q₂</text>
  <!-- Q3 -->
  <circle cx="370" cy="80" r="18" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
  <text x="370" y="85" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">+{_fmt_sa(q3_uc)}μC</text>
  <text x="370" y="50" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Q₃</text>
  <!-- Dimension arrows -->
  <text x="152" y="115" font-size="11" fill="#475569" text-anchor="middle">r₁ = {_fmt_sa(r1_cm)} cm</text>
  <text x="297" y="115" font-size="11" fill="#475569" text-anchor="middle">r₂ = {_fmt_sa(r2_cm)} cm</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing three collinear positive point charges, "
        f"$Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$, $Q_2 = +{_fmt_sa(q2_uc)}\\mu\\text{{C}}$, and "
        f"$Q_3 = +{_fmt_sa(q3_uc)}\\mu\\text{{C}}$, arranged along a straight horizontal line.\n"
        f"The distance between $Q_1$ and $Q_2$ is $r_1 = {_fmt_sa(r1_cm)}\\text{{ cm}}$, and between $Q_2$ and $Q_3$ is $r_2 = {_fmt_sa(r2_cm)}\\text{{ cm}}$.\n\n"
        f"1. Draw a free-body diagram showing the electrostatic forces acting on $Q_2$.\n"
        f"2. Calculate the net electrostatic force (magnitude and direction) exerted on $Q_2$."
    )

    ans_latex = (
        rf"F_{{1\text{{ on }}2}} = \frac{{k Q_1 Q_2}}{{r_1^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r1_m)})^2}} = {_fmt_sa(f12, 2)}\text{{ N (to the right)}}\n"
        rf"F_{{3\text{{ on }}2}} = \frac{{k Q_3 Q_2}}{{r_2^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q3_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r2_m)})^2}} = {_fmt_sa(f32, 2)}\text{{ N (to the left)}}\n"
        rf"F_{{\text{{net}}}} = |F_{{1\text{{ on }}2}} - F_{{3\text{{ on }}2}}| = {_fmt_sa(f_net_mag, 2)}\text{{ N, }} {direction}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Free body diagram showing two opposing horizontal forces on Q2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate F_1_on_2 = {_fmt_sa(f12, 2)} N to the right", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate F_3_on_2 = {_fmt_sa(f32, 2)} N to the left", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Net force magnitude = {_fmt_sa(f_net_mag, 2)} N", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Net force direction: {direction}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_direction", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate the force on $Q_2$ from $Q_1$ and from $Q_3$ separately using Coulomb's Law.",
        "tier_2": "Like charges repel: $Q_1$ pushes $Q_2$ to the right; $Q_3$ pushes $Q_2$ to the left.",
        "tier_3": f"Subtract the opposing forces: $|{_fmt_sa(f12, 2)} - {_fmt_sa(f32, 2)}| = {_fmt_sa(f_net_mag, 2)}\\text{{ N}}$, directed {direction}.",
    }

    return {
        "id": f"ps_elec_collin3_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_collin3_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "13_collinear_three_charges_net_force_on_centre",
        "learning_objective_id": "ps_elec_13_collinear_centre",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_opposing_forces_instead_of_subtracting", "omitted_direction_vector"],
        "keywords": ["collinear charges", "net electrostatic force", "superposition"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 14: Collinear 1D multi-charge arrangement: net force on end charge
def _b14_collinear_three_charges_net_force_on_end(r: random.Random) -> Dict[str, Any]:
    # Q1 at x=0 (+), Q2 at x=d1 (-), Q3 at x=d1+d2 (+)
    # Find net force on Q3
    q1_uc = r.choice([3.0, 6.0, 9.0])
    q2_uc = r.choice([2.0, 4.0, 5.0])
    q3_uc = r.choice([2.0, 3.0, 4.0])

    d1_cm = r.choice([10.0, 15.0])
    d2_cm = r.choice([10.0, 15.0])
    d1_m = d1_cm / 100.0
    d2_m = d2_cm / 100.0
    d_total_m = d1_m + d2_m

    # Q1 is +, Q3 is + => Repulsive: Q1 pushes Q3 right (+x)
    f13 = K_COULOMB * (q1_uc * 1e-6) * (q3_uc * 1e-6) / (d_total_m ** 2)
    # Q2 is -, Q3 is + => Attractive: Q2 pulls Q3 left (-x)
    f23 = K_COULOMB * (q2_uc * 1e-6) * (q3_uc * 1e-6) / (d2_m ** 2)

    f_net = f13 - f23
    direction = "to the right (away from Q1)" if f_net > 0 else "to the left (towards Q2)"
    f_net_mag = abs(f_net)

    prompt = (
        f"Three point charges lie at fixed coordinates in a vacuum:\n"
        f"- $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ at $x = 0\\text{{ cm}}$\n"
        f"- $Q_2 = -{_fmt_sa(q2_uc)}\\mu\\text{{C}}$ at $x = {_fmt_sa(d1_cm)}\\text{{ cm}}$\n"
        f"- $Q_3 = +{_fmt_sa(q3_uc)}\\mu\\text{{C}}$ at $x = {_fmt_sa(d1_cm + d2_cm)}\\text{{ cm}}$\n\n"
        f"Calculate the resultant electrostatic force (magnitude and direction) exerted on charge $Q_3$."
    )

    ans_latex = (
        rf"F_{{1\text{{ on }}3}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})({_fmt_sa(q3_uc)} \times 10^{{-6}})}}{{({_fmt_sa(d_total_m)})^2}} = {_fmt_sa(f13, 2)}\text{{ N (right)}}\n"
        rf"F_{{2\text{{ on }}3}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q2_uc)} \times 10^{{-6}})({_fmt_sa(q3_uc)} \times 10^{{-6}})}}{{({_fmt_sa(d2_m)})^2}} = {_fmt_sa(f23, 2)}\text{{ N (left)}}\n"
        rf"F_{{\text{{net}}}} = {_fmt_sa(f_net_mag, 2)}\text{{ N, }} {direction}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate F_1_on_3 using total distance ({_fmt_sa(d_total_m)} m): {_fmt_sa(f13, 2)} N right", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate F_2_on_3 using separation ({_fmt_sa(d2_m)} m): {_fmt_sa(f23, 2)} N left", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Subtract vectors to get net magnitude = {_fmt_sa(f_net_mag, 2)} N", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"State direction: {direction}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_wrong_distance_between_Q1_and_Q3", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The distance between $Q_1$ and $Q_3$ is the sum of both intervals: $d_1 + d_2$.",
        "tier_2": f"$Q_1$ repels $Q_3$ (pushes right); $Q_2$ attracts $Q_3$ (pulls left).",
        "tier_3": f"Net force = $|{_fmt_sa(f13, 2)} - {_fmt_sa(f23, 2)}| = {_fmt_sa(f_net_mag, 2)}\\text{{ N}}$, {direction}.",
    }

    return {
        "id": f"ps_elec_collin_end_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_collin_end_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "14_collinear_three_charges_net_force_on_end",
        "learning_objective_id": "ps_elec_14_collinear_end",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_partial_distance_for_outer_charges", "forgot_attraction_pulls_towards_negative"],
        "keywords": ["net force on end charge", "superposition", "collinear"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 15: Collinear zero-net-force equilibrium position
def _b15_collinear_zero_net_force_equilibrium_position(r: random.Random) -> Dict[str, Any]:
    # Two positive charges Q1 and Q2 at distance d
    # F1 = F2 => k Q1 q / x^2 = k Q2 q / (d - x)^2 => sqrt(Q1)/x = sqrt(Q2)/(d - x)
    # Pick nice squares: Q1 = 4 uC, Q2 = 9 uC, d = 50 cm
    # sqrt(Q1) = 2, sqrt(Q2) = 3 => 2/x = 3/(d - x) => 2d - 2x = 3x => 5x = 2d => x = 2/5 d
    pair = r.choice([
        (4.0, 9.0, 2.0, 3.0),
        (1.0, 4.0, 1.0, 2.0),
        (1.0, 9.0, 1.0, 3.0),
        (4.0, 16.0, 2.0, 4.0),
        (9.0, 16.0, 3.0, 4.0),
        (9.0, 25.0, 3.0, 5.0),
    ])
    q1_uc, q2_uc, s1, s2 = pair
    d_cm = r.choice([20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0])
    x_cm = round((s1 / (s1 + s2)) * d_cm, 2)

    prompt = (
        f"Two positive point charges, $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ and $Q_2 = +{_fmt_sa(q2_uc)}\\mu\\text{{C}}$, "
        f"are separated by $d = {_fmt_sa(d_cm)}\\text{{ cm}}$ in a vacuum.\n"
        f"A third positive charge $q$ is introduced between $Q_1$ and $Q_2$ such that the resultant electrostatic force "
        f"on charge $q$ is zero.\n\n"
        f"Calculate the distance $x$ from charge $Q_1$ at which charge $q$ experiences zero resultant force."
    )

    ans_latex = (
        rf"F_1 = F_2 \implies \frac{{k Q_1 q}}{{x^2}} = \frac{{k Q_2 q}}{{({_fmt_sa(d_cm)} - x)^2}}\n"
        rf"\frac{{\sqrt{{{q1_uc}}}}}{{x}} = \frac{{\sqrt{{{q2_uc}}}}}{{{_fmt_sa(d_cm)} - x}} \implies "
        rf"\frac{{{s1}}}{{x}} = \frac{{{s2}}}{{{_fmt_sa(d_cm)} - x}}\n"
        rf"{s1}({_fmt_sa(d_cm)} - x) = {s2}x \implies {s1 + s2}x = {s1 * d_cm} \implies x = {_fmt_sa(x_cm)}\text{{ cm}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Equate forces: F1 = F2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Cancel k and q: Q1 / x^2 = Q2 / (d - x)^2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Take square root of both sides to avoid quadratic", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Solve linear equation for x = {_fmt_sa(x_cm)} cm", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_algebra", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "For net force to be zero between two like charges, the repulsive force from $Q_1$ must balance the repulsive force from $Q_2$.",
        "tier_2": "Set $\\frac{Q_1}{x^2} = \\frac{Q_2}{(d - x)^2}$. Taking square roots on both sides simplifies the equation to linear form.",
        "tier_3": f"$\\frac{{{s1}}}{{x}} = \\frac{{{s2}}}{{{_fmt_sa(d_cm)} - x}} \\implies x = {_fmt_sa(x_cm)}\\text{{ cm}}$ from $Q_1$.",
    }

    return {
        "id": f"ps_elec_equil_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_equil_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "15_collinear_zero_net_force_equilibrium_position",
        "learning_objective_id": "ps_elec_15_zero_force_point",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["placed_charge_outside_line_segment", "algebraic_square_root_expansion_error"],
        "keywords": ["equilibrium", "zero net force", "collinear charges"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 16: 2D Perpendicular three-charge system (resultant force)
def _b16_perpendicular_2d_three_charges_net_force(r: random.Random) -> Dict[str, Any]:
    # Q1 on y-axis at (0, y), Q2 at origin (0, 0), Q3 on x-axis at (x, 0)
    # Find net force on Q2
    q1_uc = r.choice([3.0, 4.0, 5.0])
    q2_uc = r.choice([2.0, 3.0])  # charge at origin
    q3_uc = r.choice([4.0, 6.0, 8.0])

    y_cm = r.choice([15.0, 20.0, 30.0])
    x_cm = r.choice([15.0, 20.0, 30.0])
    y_m = y_cm / 100.0
    x_m = x_cm / 100.0

    # Let Q1 be +, Q2 be +, Q3 be +
    # Force on Q2 from Q1: repulsive -> downwards along -y
    fy = K_COULOMB * (q1_uc * 1e-6) * (q2_uc * 1e-6) / (y_m ** 2)
    # Force on Q2 from Q3: repulsive -> leftwards along -x
    fx = K_COULOMB * (q3_uc * 1e-6) * (q2_uc * 1e-6) / (x_m ** 2)

    f_res = math.sqrt(fx**2 + fy**2)
    theta_deg = math.degrees(math.atan2(fy, fx))

    svg = _clean_svg(f"""
<svg viewBox="0 0 320 280" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="280" fill="#f8fafc" rx="8"/>
  <!-- Axes -->
  <line x1="60" y1="220" x2="280" y2="220" stroke="#cbd5e1" stroke-width="2"/>
  <line x1="60" y1="220" x2="60" y2="40" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Q1 on y-axis -->
  <circle cx="60" cy="70" r="16" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
  <text x="95" y="75" font-size="11" font-weight="bold" fill="#0284c7">Q₁ (+{_fmt_sa(q1_uc)}μC)</text>
  <!-- Q2 at origin -->
  <circle cx="60" cy="220" r="16" fill="#a78bfa" stroke="#7c3aed" stroke-width="2"/>
  <text x="35" y="245" font-size="11" font-weight="bold" fill="#7c3aed">Q₂ (+{_fmt_sa(q2_uc)}μC)</text>
  <!-- Q3 on x-axis -->
  <circle cx="230" cy="220" r="16" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
  <text x="230" y="250" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">Q₃ (+{_fmt_sa(q3_uc)}μC)</text>
  <!-- Labels -->
  <text x="25" y="145" font-size="11" fill="#475569">{_fmt_sa(y_cm)} cm</text>
  <text x="145" y="210" font-size="11" fill="#475569">{_fmt_sa(x_cm)} cm</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing three point charges arranged in a right-angled triangle in a vacuum:\n"
        f"- $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ on the $y$-axis at a distance of $r_y = {_fmt_sa(y_cm)}\\text{{ cm}}$ from the origin\n"
        f"- $Q_2 = +{_fmt_sa(q2_uc)}\\mu\\text{{C}}$ placed at the origin $(0; 0)$\n"
        f"- $Q_3 = +{_fmt_sa(q3_uc)}\\mu\\text{{C}}$ on the $x$-axis at a distance of $r_x = {_fmt_sa(x_cm)}\\text{{ cm}}$ from the origin\n\n"
        f"1. Draw a vector diagram showing the components of the electrostatic forces acting on $Q_2$.\n"
        f"2. Calculate the magnitude and direction of the resultant electrostatic force on charge $Q_2$."
    )

    ans_latex = (
        rf"F_y = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(y_m)})^2}} = {_fmt_sa(fy, 2)}\text{{ N (downwards)}}\n"
        rf"F_x = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q3_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(x_m)})^2}} = {_fmt_sa(fx, 2)}\text{{ N (leftwards)}}\n"
        rf"F_{{\text{{net}}}} = \sqrt{{F_x^2 + F_y^2}} = \sqrt{{({_fmt_sa(fx, 2)})^2 + ({_fmt_sa(fy, 2)})^2}} = {_fmt_sa(f_res, 2)}\text{{ N}}\n"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(fy, 2)}}}{{{_fmt_sa(fx, 2)}}}\right) = {_fmt_sa(theta_deg, 1)}^\circ\text{{ below negative x-axis (third quadrant)}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Vector diagram showing perpendicular component forces on Q2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate F_y = {_fmt_sa(fy, 2)} N", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate F_x = {_fmt_sa(fx, 2)} N", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Apply Pythagoras: F_net = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Resultant magnitude = {_fmt_sa(f_res, 2)} N", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Direction angle: {_fmt_sa(theta_deg, 1)} deg", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "added_scalars_instead_of_vectors", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate the electrostatic force along each axis separately using Coulomb's Law.",
        "tier_2": "Because the forces are perpendicular ($90^\\circ$), use Pythagoras theorem $F_{\\text{res}} = \\sqrt{F_x^2 + F_y^2}$.",
        "tier_3": f"Resultant = $\\sqrt{{({_fmt_sa(fx, 2)})^2 + ({_fmt_sa(fy, 2)})^2}} = {_fmt_sa(f_res, 2)}\\text{{ N}}$, $\\theta = {_fmt_sa(theta_deg, 1)}^\\circ$.",
    }

    return {
        "id": f"ps_elec_2d_force_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_2d_force_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "16_perpendicular_2d_three_charges_net_force",
        "learning_objective_id": "ps_elec_16_2d_force",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_perpendicular_forces_scalar", "trigonometric_ratio_inversion"],
        "keywords": ["2D Coulomb force", "perpendicular charges", "Pythagoras resultant"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 17: Suspended charged pith ball in electrostatic equilibrium
def _b17_suspended_charged_pith_ball_equilibrium(r: random.Random) -> Dict[str, Any]:
    # A small sphere of mass m suspended by light string of length L, repelled by fixed charge Q
    mass_g = r.choice([2.0, 3.0, 4.0, 5.0])
    mass_kg = mass_g / 1000.0
    fg = mass_kg * G_ACCEL
    theta_deg = r.choice([15.0, 20.0, 25.0, 30.0])
    theta_rad = math.radians(theta_deg)

    # In equilibrium: T*cos(theta) = mg, T*sin(theta) = Fe => tan(theta) = Fe / mg
    fe = fg * math.tan(theta_rad)
    tension = fg / math.cos(theta_rad)

    prompt = (
        f"A small conducting sphere of mass $m = {_fmt_sa(mass_g)}\\text{{ g}}$ carries an electric charge and is suspended "
        f"from a ceiling by a light, inextensible insulating thread.\n"
        f"When another charged sphere is brought near it horizontally, the suspended sphere is repelled and remains in "
        f"equilibrium at an angle of $\\theta = {_fmt_sa(theta_deg)}^\\circ$ to the vertical.\n\n"
        f"1. Draw a labelled free-body diagram showing all the forces acting on the suspended sphere.\n"
        f"2. Calculate the magnitude of the gravitational force (weight) acting on the sphere ($g = 9{{,}}8\\text{{ m/s}}^2$).\n"
        f"3. Calculate the electrostatic repulsive force $F_E$ acting on the sphere."
    )

    ans_latex = (
        rf"1.\; \text{{Forces: Weight }} \vec{{F}}_g \text{{ (downwards), Tension }} \vec{{T}} \text{{ (along string), Electric force }} \vec{{F}}_E \text{{ (horizontal)}}\n"
        rf"2.\; F_g = mg = ({_fmt_sa(mass_kg)})({G_ACCEL}) = {_fmt_sa(fg, 4)}\text{{ N}}\n"
        rf"3.\; \tan\theta = \frac{{F_E}}{{F_g}} \implies F_E = F_g \tan\theta = {_fmt_sa(fg, 4)} \times \tan({_fmt_sa(theta_deg)}^\circ) = {_fmt_sa(fe, 4)}\text{{ N}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Free-body diagram with 3 labelled forces (T, Fg, FE)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate weight: Fg = mg = {_fmt_sa(fg, 4)} N", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Trigonometric equilibrium relation: tan(theta) = FE / Fg", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate FE = {_fmt_sa(fe, 4)} N", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_grams_to_kg_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Resolve forces: Vertically, $T \\cos\\theta = mg$. Horizontally, $T \\sin\\theta = F_E$.",
        "tier_2": "Dividing the two equations gives $\\tan\\theta = \\frac{F_E}{mg}$.",
        "tier_3": f"Weight = {mass_kg} * 9.8 = {_fmt_sa(fg, 4)} N. $F_E = {_fmt_sa(fg, 4)} \\times \\tan({theta_deg}^\\circ) = {_fmt_sa(fe, 4)}\\text{{ N}}$.",
    }

    return {
        "id": f"ps_elec_pith_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_pith_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "17_suspended_charged_pith_ball_equilibrium",
        "learning_objective_id": "ps_elec_17_pith_ball_equilibrium",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["swapped_sin_and_cos_in_angle_resolution", "forgot_mass_conversion_grams_to_kg"],
        "keywords": ["pith ball", "static equilibrium", "tension", "weight"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 18: Electric field definition and E = F / q
def _b18_electric_field_at_point_from_test_charge(r: random.Random) -> Dict[str, Any]:
    q_nc = r.choice([2.0, 4.0, 5.0, 8.0])
    q_c = q_nc * 1e-9
    f_mn = r.choice([12.0, 16.0, 24.0, 36.0, 48.0])
    f_n = f_mn * 1e-3

    e_field = f_n / q_c
    dir_choice = r.choice(["east", "west", "north", "south", "to the right"])

    prompt = (
        f"A small positive test charge of $q = +{_fmt_sa(q_nc)}\\text{{ nC}}$ experiences an electrostatic force "
        f"of $F = {_fmt_sa(f_mn)}\\text{{ mN}}$ directed {dir_choice} when placed at point $P$.\n\n"
        f"1. Define the concept of an **electric field** at a point in words.\n"
        f"2. Calculate the magnitude and direction of the electric field intensity $\\vec{{E}}$ at point $P$."
    )

    ans_latex = (
        rf"1.\; \text{{The electrostatic force experienced per unit positive charge placed at that point.}}\n"
        rf"2.\; E = \frac{{F}}{{q}} = \frac{{{_fmt_sa(f_mn)} \times 10^{{-3}}}}{{{_fmt_sa(q_nc)} \times 10^{{-9}}}} = {_fmt_sci(e_field)}\text{{ N/C (or N}}\cdot\text{{C}}^{{-1}}\text{{) directed {dir_choice}}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of electric field at a point (force per unit positive charge)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: E = F / q", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation ({_fmt_sci(e_field)} N/C) and direction ({dir_choice})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_direction_on_vector_field", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Electric field at a point is the force per unit positive charge: $E = F/q$.",
        "tier_2": f"Convert $\\text{{mN}}$ to $\\text{{N}}$ ($10^{{-3}}$) and $\\text{{nC}}$ to $\\text{{C}}$ ($10^{{-9}}$). Direction matches the force on a positive test charge.",
        "tier_3": f"$E = ({_fmt_sa(f_mn)} \\times 10^{{-3}}) / ({_fmt_sa(q_nc)} \\times 10^{{-9}}) = {_fmt_sci(e_field)}\\text{{ N/C}}$ {dir_choice}.",
    }

    return {
        "id": f"ps_elec_efield_def_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_efield_def_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "18_electric_field_at_point_from_test_charge",
        "learning_objective_id": "ps_elec_18_field_definition",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["inverted_formula_q_over_F", "forgot_metric_prefix_conversion"],
        "keywords": ["electric field", "test charge", "N/C", "force per unit charge"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 19: Electric field strength from a single point charge E = kQ/r^2
def _b19_electric_field_strength_single_point_charge(r: random.Random) -> Dict[str, Any]:
    q_uc = r.choice([3.0, 4.0, 5.0, 6.0, 8.0])
    sign = r.choice([1, -1])
    q_c = sign * q_uc * 1e-6
    r_cm = r.choice([10.0, 15.0, 20.0, 30.0])
    r_m = r_cm / 100.0

    e_val = K_COULOMB * (q_uc * 1e-6) / (r_m ** 2)
    dir_str = "away from the charge" if sign > 0 else "towards the charge"

    prompt = (
        f"A point charge $Q = {'+' if sign > 0 else '-'}{_fmt_sa(q_uc)}\\mu\\text{{C}}$ is fixed in a vacuum.\n\n"
        f"Calculate the electric field strength $\\vec{{E}}$ (magnitude and direction relative to the charge) "
        f"at a point $M$ located $r = {_fmt_sa(r_cm)}\\text{{ cm}}$ away from charge $Q$."
    )

    ans_latex = (
        rf"E = \frac{{k Q}}{{r^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} "
        rf"= {_fmt_sci(e_val)}\\text{{ N/C (or N}}\cdot\text{{C}}^{{-1}}\text{{), directed {dir_str}}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: E = k * Q / r^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Substitution with conversion of cm to m and uC to 10^-6 C", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of magnitude = {_fmt_sci(e_val)} N/C", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Direction: {dir_str}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_square_of_distance", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Electric field from a single point charge is $E = \\frac{k Q}{r^2}$.",
        "tier_2": f"Positive charges create fields directed radially outwards (away); negative charges create fields directed radially inwards (towards).",
        "tier_3": f"$E = (9 \\times 10^9 \\times {q_uc} \\times 10^{{-6}}) / ({r_m})^2 = {_fmt_sci(e_val)}\\text{{ N/C}}$ ({dir_str}).",
    }

    return {
        "id": f"ps_elec_efield_pt_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_efield_pt_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "19_electric_field_strength_single_point_charge",
        "learning_objective_id": "ps_elec_19_field_point_charge",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_distance_squared", "swapped_direction_for_positive_negative_charge"],
        "keywords": ["point charge", "electric field strength", "Coulomb constant"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 20: Electric field lines pattern interpretation
def _b20_electric_field_lines_pattern_interpretation(r: random.Random) -> Dict[str, Any]:
    pair_type = r.choice(["unlike", "like"])
    sep_cm = r.choice([6, 8, 10, 12, 14, 15, 16, 18, 20, 24])
    q_mag_nc = r.choice([2, 3, 4, 5, 6, 8, 10, 12])

    if pair_type == "unlike":
        svg = _clean_svg(f"""
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#f8fafc" rx="8"/>
  <!-- Field lines connecting + and - -->
  <line x1="120" y1="100" x2="280" y2="100" stroke="#3b82f6" stroke-width="2"/>
  <path d="M 120,100 C 170,40 230,40 280,100" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 120,100 C 170,160 230,160 280,100" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 120,100 C 160,10 240,10 280,100" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 120,100 C 160,190 240,190 280,100" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <!-- Arrows -->
  <polygon points="205,97 215,100 205,103" fill="#3b82f6"/>
  <polygon points="205,48 215,51 207,57" fill="#3b82f6"/>
  <polygon points="205,152 215,149 207,143" fill="#3b82f6"/>
  <!-- Charges -->
  <circle cx="120" cy="100" r="16" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
  <text x="120" y="105" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
  <text x="120" y="70" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Charge X ({q_mag_nc} nC)</text>
  <circle cx="280" cy="100" r="16" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
  <text x="280" y="105" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  <text x="280" y="70" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Charge Y ({q_mag_nc} nC)</text>
  <text x="200" y="192" font-size="10" fill="#475569" text-anchor="middle">d = {sep_cm} cm</text>
</svg>""")
        charge_x = "positive"
        charge_y = "negative"
    else:
        svg = _clean_svg(f"""
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#f8fafc" rx="8"/>
  <!-- Field lines repelling -->
  <path d="M 120,100 C 160,95 180,50 180,10" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 120,100 C 160,105 180,150 180,190" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 280,100 C 240,95 220,50 220,10" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <path d="M 280,100 C 240,105 220,150 220,190" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
  <!-- Neutral point dot -->
  <circle cx="200" cy="100" r="3" fill="#64748b"/>
  <text x="200" y="115" font-size="10" fill="#64748b" text-anchor="middle">Point N (d = {sep_cm} cm)</text>
  <!-- Charges -->
  <circle cx="120" cy="100" r="16" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
  <text x="120" y="105" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
  <text x="120" y="70" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Charge X ({q_mag_nc} nC)</text>
  <circle cx="280" cy="100" r="16" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
  <text x="280" y="105" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
  <text x="280" y="70" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Charge Y ({q_mag_nc} nC)</text>
</svg>""")
        charge_x = "positive"
        charge_y = "positive"

    prompt = (
        f"Refer to the accompanying diagram representing the electric field pattern between two point charges, $X$ and $Y$, "
        f"each of magnitude $|Q| = {q_mag_nc}\\text{{ nC}}$ and separated by $d = {sep_cm}\\text{{ cm}}$.\n\n"
        f"1. State two key properties of electric field lines.\n"
        f"2. Identify the sign of charge $X$ and charge $Y$.\n"
        f"3. Explain what the spacing (density) of the field lines indicates about the electric field strength."
    )

    ans_latex = (
        rf"1.\; \text{{(i) Lines never cross/intersect; (ii) Lines start on positive charges and end on negative charges (or at infinity); (iii) Lines enter/leave surfaces at right angles. [Any two]}}\n"
        rf"2.\; \text{{Charge }} X \text{{ is {charge_x}; Charge }} Y \text{{ is {charge_y}.}}\n"
        rf"3.\; \text{{The density/closeness of the field lines is directly proportional to the magnitude of the electric field strength (closer lines indicate a stronger field).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Two valid properties of field lines", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct polarities: X is {charge_x}, Y is {charge_y}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Closer line spacing indicates stronger electric field", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Field lines originate on positive charges and terminate on negative charges.",
        "tier_2": "Where field lines are packed closely together, the field is strongest.",
        "tier_3": "Electric field lines never cross each other.",
    }

    return {
        "id": f"ps_elec_lines_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_lines_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "20_electric_field_lines_pattern_interpretation",
        "learning_objective_id": "ps_elec_20_field_lines",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_lines_can_cross", "confused_direction_into_positive"],
        "keywords": ["electric field lines", "pattern", "field line density"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 21: Collinear net electric field from two point charges
def _b21_collinear_two_charges_net_electric_field(r: random.Random) -> Dict[str, Any]:
    # Point P is between Q1 and Q2 or beyond them
    q1_uc = r.choice([3.0, 5.0, 6.0])
    q2_uc = r.choice([2.0, 4.0, 8.0])
    r1_cm = r.choice([10.0, 15.0, 20.0])
    r2_cm = r.choice([10.0, 15.0, 20.0])
    r1_m = r1_cm / 100.0
    r2_m = r2_cm / 100.0

    # Let Q1 be positive, Q2 be negative
    # Point P between them:
    # E1 from Q1 (+): directed to the right (+x, away from Q1)
    # E2 from Q2 (-): directed to the right (+x, towards Q2)
    # Both fields point to the right!
    e1 = K_COULOMB * (q1_uc * 1e-6) / (r1_m ** 2)
    e2 = K_COULOMB * (q2_uc * 1e-6) / (r2_m ** 2)
    e_net = e1 + e2

    prompt = (
        f"Two point charges, $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ and $Q_2 = -{_fmt_sa(q2_uc)}\\mu\\text{{C}}$, "
        f"are held in a vacuum.\n"
        f"Point $P$ lies on the segment joining the charges, at distance $r_1 = {_fmt_sa(r1_cm)}\\text{{ cm}}$ "
        f"from $Q_1$ and $r_2 = {_fmt_sa(r2_cm)}\\text{{ cm}}$ from $Q_2$.\n\n"
        f"1. State the direction of the electric field at point $P$ due to charge $Q_1$ alone.\n"
        f"2. State the direction of the electric field at point $P$ due to charge $Q_2$ alone.\n"
        f"3. Calculate the magnitude and direction of the resultant electric field $\\vec{{E}}_{{\\text{{res}}}}$ at point $P$."
    )

    ans_latex = (
        rf"1.\; \vec{{E}}_1 = \frac{{k Q_1}}{{r_1^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r1_m)})^2}} = {_fmt_sci(e1)}\text{{ N/C (to the right)}}\n"
        rf"2.\; \vec{{E}}_2 = \frac{{k |Q_2|}}{{r_2^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r2_m)})^2}} = {_fmt_sci(e2)}\text{{ N/C (to the right)}}\n"
        rf"3.\; E_{{\text{{net}}}} = E_1 + E_2 = {_fmt_sci(e1)} + {_fmt_sci(e2)} = {_fmt_sci(e_net)}\text{{ N/C to the right (towards }} Q_2\text{{)}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Direction of E1 is to the right (away from positive Q1)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Direction of E2 is to the right (towards negative Q2)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate E1 = {_fmt_sci(e1)} N/C", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate E2 = {_fmt_sci(e2)} N/C", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Add collinear vectors: E_net = {_fmt_sci(e_net)} N/C to the right", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "subtracted_aligned_fields", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: A positive charge pushes a positive test charge away; a negative charge pulls a test charge towards itself.",
        "tier_2": "At a point between a positive and a negative charge, both electric fields point towards the negative charge (same direction).",
        "tier_3": f"Add the two field magnitudes: $E_{{\\text{{net}}}} = E_1 + E_2 = {_fmt_sci(e_net)}\\text{{ N/C}}$ to the right.",
    }

    return {
        "id": f"ps_elec_collin_e_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_collin_e_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "21_collinear_two_charges_net_electric_field",
        "learning_objective_id": "ps_elec_21_collinear_net_field",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["subtracted_fields_pointing_in_same_direction", "substituted_negative_sign_in_magnitude"],
        "keywords": ["net electric field", "superposition", "collinear charges"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 22: Neutral point (zero electric field) location
def _b22_collinear_neutral_point_zero_electric_field(r: random.Random) -> Dict[str, Any]:
    # Two positive charges Q1 and Q2 at distance d
    # E1 = E2 => k Q1 / x^2 = k Q2 / (d - x)^2 => sqrt(Q1)/x = sqrt(Q2)/(d - x)
    pair = r.choice([
        (4.0, 16.0, 2.0, 4.0),
        (1.0, 9.0, 1.0, 3.0),
        (4.0, 9.0, 2.0, 3.0),
        (9.0, 16.0, 3.0, 4.0),
        (1.0, 4.0, 1.0, 2.0),
        (9.0, 25.0, 3.0, 5.0),
    ])
    q1_uc, q2_uc, s1, s2 = pair
    d_cm = r.choice([24.0, 30.0, 36.0, 40.0, 45.0, 50.0, 60.0, 70.0, 75.0, 90.0])
    x_cm = round((s1 / (s1 + s2)) * d_cm, 2)

    prompt = (
        f"Two positive point charges, $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ and $Q_2 = +{_fmt_sa(q2_uc)}\\mu\\text{{C}}$, "
        f"are placed $d = {_fmt_sa(d_cm)}\\text{{ cm}}$ apart in a vacuum.\n\n"
        f"1. Explain what is meant by a **neutral point** in an electric field.\n"
        f"2. Calculate the distance $x$ from charge $Q_1$ to the neutral point between the two charges."
    )

    ans_latex = (
        rf"1.\; \text{{A point in space where the net electric field intensity is zero (}}\vec{{E}}_{{\text{{net}}}} = \vec{{0}}\text{{).}}\n"
        rf"2.\; E_1 = E_2 \implies \frac{{k Q_1}}{{x^2}} = \frac{{k Q_2}}{{({_fmt_sa(d_cm)} - x)^2}}\n"
        rf"\frac{{{s1}}}{{x}} = \frac{{{s2}}}{{{_fmt_sa(d_cm)} - x}} \implies {s1}({_fmt_sa(d_cm)} - x) = {s2}x \implies x = {_fmt_sa(x_cm)}\\text{{ cm}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of neutral point (E_net = 0)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Equate field strengths: E1 = E2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula substitution: Q1/x^2 = Q2/(d - x)^2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Take square roots and set up linear ratio", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Final position x = {_fmt_sa(x_cm)} cm from Q1", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_algebra", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "At the neutral point, the electric fields produced by $Q_1$ and $Q_2$ are equal in magnitude and opposite in direction.",
        "tier_2": "Set $E_1 = E_2 \\implies \\frac{Q_1}{x^2} = \\frac{Q_2}{(d - x)^2}$. Taking square roots simplifies the work.",
        "tier_3": f"$\\frac{{{s1}}}{{x}} = \\frac{{{s2}}}{{{_fmt_sa(d_cm)} - x}} \\implies x = {_fmt_sa(x_cm)}\\text{{ cm}}$ from $Q_1$.",
    }

    return {
        "id": f"ps_elec_neut_pt_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_neut_pt_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "22_collinear_neutral_point_zero_electric_field",
        "learning_objective_id": "ps_elec_22_neutral_point",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_neutral_point_means_E_equals_zero", "expanded_quadratic_with_sign_errors"],
        "keywords": ["neutral point", "zero field", "superposition"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 23: 2D Perpendicular net electric field
def _b23_perpendicular_2d_net_electric_field(r: random.Random) -> Dict[str, Any]:
    # Point P is at (0, 0). Q1 on y-axis at (0, y), Q2 on x-axis at (x, 0)
    q1_uc = r.choice([2.0, 4.0, 6.0])
    q2_uc = r.choice([3.0, 5.0, 8.0])
    y_cm = r.choice([10.0, 20.0, 30.0])
    x_cm = r.choice([10.0, 20.0, 30.0])
    y_m = y_cm / 100.0
    x_m = x_cm / 100.0

    # Let Q1 be positive (at y), Q2 be positive (at x)
    # Field at origin (0, 0):
    # E1 from Q1 (+y): points away from Q1 -> downwards (-y)
    # E2 from Q2 (+x): points away from Q2 -> leftwards (-x)
    ey = K_COULOMB * (q1_uc * 1e-6) / (y_m ** 2)
    ex = K_COULOMB * (q2_uc * 1e-6) / (x_m ** 2)
    e_net = math.sqrt(ex**2 + ey**2)
    theta_deg = math.degrees(math.atan2(ey, ex))

    prompt = (
        f"Two point charges are held at fixed Cartesian coordinates:\n"
        f"- $Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ at $(0; +{_fmt_sa(y_cm)}\\text{{ cm}})$\n"
        f"- $Q_2 = +{_fmt_sa(q2_uc)}\\mu\\text{{C}}$ at $(+{_fmt_sa(x_cm)}\\text{{ cm}}; 0)$\n\n"
        f"Calculate the magnitude and direction of the resultant electric field $\\vec{{E}}_{{\\text{{res}}}}$ at the origin $(0; 0)$."
    )

    ans_latex = (
        rf"E_y = \frac{{k Q_1}}{{r_y^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})}}{{({_fmt_sa(y_m)})^2}} = {_fmt_sci(ey)}\text{{ N/C (downwards)}}\n"
        rf"E_x = \frac{{k Q_2}}{{r_x^2}} = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(x_m)})^2}} = {_fmt_sci(ex)}\text{{ N/C (leftwards)}}\n"
        rf"E_{{\text{{net}}}} = \sqrt{{E_x^2 + E_y^2}} = {_fmt_sci(e_net)}\text{{ N/C}}\n"
        rf"\theta = \arctan\left(\frac{{E_y}}{{E_x}}\right) = {_fmt_sa(theta_deg, 1)}^\circ\text{{ below negative x-axis (third quadrant)}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate Ey = {_fmt_sci(ey)} N/C downwards", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate Ex = {_fmt_sci(ex)} N/C leftwards", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Pythagoras: E_net = sqrt(Ex^2 + Ey^2)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Magnitude E_net = {_fmt_sci(e_net)} N/C", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Direction angle: {_fmt_sa(theta_deg, 1)} deg", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "added_scalars", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate the electric field produced by each charge at the origin independently.",
        "tier_2": "Because the field vectors are at $90^\\circ$ to each other, use Pythagoras to find the resultant.",
        "tier_3": f"$E_{{\\text{{net}}}} = \\sqrt{{({_fmt_sci(ex)})^2 + ({_fmt_sci(ey)})^2}} = {_fmt_sci(e_net)}\\text{{ N/C}}$.",
    }

    return {
        "id": f"ps_elec_2d_field_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_2d_field_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "23_perpendicular_2d_net_electric_field",
        "learning_objective_id": "ps_elec_23_2d_field",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_perpendicular_fields_scalar", "swapped_radial_direction_for_positive_charge"],
        "keywords": ["2D electric field", "resultant field", "perpendicular"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 24: Uniform electric field between parallel plates E = V / d
def _b24_electric_field_uniform_parallel_plates(r: random.Random) -> Dict[str, Any]:
    v_volts = r.choice([200, 400, 500, 800, 1000, 1200])
    d_mm = r.choice([4.0, 5.0, 8.0, 10.0, 20.0])
    d_m = d_mm / 1000.0

    e_field = v_volts / d_m
    f_electron = e_field * E_CHARGE
    a_electron = f_electron / M_ELECTRON

    svg = _clean_svg(f"""
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="200" fill="#f8fafc" rx="8"/>
  <!-- Top plate + -->
  <rect x="50" y="40" width="260" height="12" fill="#f87171" rx="2"/>
  <text x="180" y="32" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Positive Plate (+{v_volts} V)</text>
  <!-- Bottom plate 0V -->
  <rect x="50" y="150" width="260" height="12" fill="#60a5fa" rx="2"/>
  <text x="180" y="180" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Negative Plate (0 V)</text>
  <!-- Uniform field lines -->
  <line x1="100" y1="52" x2="100" y2="150" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="100,105 97,97 103,97" fill="#94a3b8"/>
  <line x1="180" y1="52" x2="180" y2="150" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="180,105 177,97 183,97" fill="#94a3b8"/>
  <line x1="260" y1="52" x2="260" y2="150" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="260,105 257,97 263,97" fill="#94a3b8"/>
  <text x="325" y="105" font-size="11" fill="#475569">d = {_fmt_sa(d_mm)} mm</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing two parallel conducting plates separated by a distance of "
        f"$d = {_fmt_sa(d_mm)}\\text{{ mm}}$ with a potential difference of $V = {v_volts}\\text{{ V}}$ applied across them.\n\n"
        f"1. State whether the electric field between the plates is uniform or non-uniform.\n"
        f"2. Calculate the magnitude of the electric field intensity $E$ between the plates ($E = V/d$).\n"
        f"3. An electron ($q = -1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$, $m_e = 9{{,}}11 \\times 10^{{-31}}\\text{{ kg}}$) is released from rest at the negative plate. "
        f"Calculate the acceleration of the electron towards the positive plate."
    )

    ans_latex = (
        rf"1.\; \text{{Uniform (constant magnitude and direction throughout).}}\n"
        rf"2.\; E = \frac{{V}}{{d}} = \frac{{{v_volts}}}{{{_fmt_sa(d_m)}}} = {_fmt_sci(e_field)}\text{{ V/m (or N/C)}}\n"
        rf"3.\; F_E = qE = (1{{,}}6 \times 10^{{-19}})({_fmt_sci(e_field)}) = {_fmt_sci(f_electron)}\text{{ N}}\n"
        rf"a = \frac{{F_E}}{{m_e}} = \frac{{{_fmt_sci(f_electron)}}}{{9{{,}}11 \times 10^{{-31}}}} = {_fmt_sci(a_electron)}\text{{ m/s}}^2"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Identify field as uniform", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula E = V / d and mm to m conversion", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate E = {_fmt_sci(e_field)} V/m", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Formula F = qE and a = F/m", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Calculate acceleration a = {_fmt_sci(a_electron)} m/s^2", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_mm_to_m_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The electric field between parallel plates is uniform: $E = \\frac{V}{d}$. Convert mm to metres ($10^{-3}$).",
        "tier_2": "The electrostatic force on the electron is $F = qE$. Newton's second law gives $a = \\frac{F}{m}$.",
        "tier_3": f"$E = {_fmt_sci(e_field)}\\text{{ V/m}}$, acceleration $a = {_fmt_sci(a_electron)}\\text{{ m/s}}^2$.",
    }

    return {
        "id": f"ps_elec_plates_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_plates_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "24_electric_field_uniform_parallel_plates",
        "learning_objective_id": "ps_elec_24_parallel_plates",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_mm_to_m_conversion", "swapped_V_and_d"],
        "keywords": ["parallel plates", "uniform field", "electron acceleration"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 25: Millikan oil drop balance (levitation equilibrium)
def _b25_millikan_oil_drop_levitation_equilibrium(r: random.Random) -> Dict[str, Any]:
    # Oil drop balanced: Fe = Fg => q * E = m * g => q * (V / d) = m * g
    # Pick n elementary charges: 2, 3, 4, 5
    n_e = r.choice([2, 3, 4, 5])
    q_c = n_e * E_CHARGE
    d_mm = r.choice([5.0, 8.0, 10.0])
    d_m = d_mm / 1000.0
    v_volts = r.choice([200, 400, 600, 800])
    e_field = v_volts / d_m
    m_kg = (q_c * e_field) / G_ACCEL

    prompt = (
        f"In a Millikan oil-drop experiment, a negatively charged oil drop of mass $m = {_fmt_sci(m_kg)}\\text{{ kg}}$ "
        f"is held stationary (suspended in equilibrium) between two horizontal parallel plates separated by $d = {_fmt_sa(d_mm)}\\text{{ mm}}$. "
        f"The potential difference across the plates is $V = {v_volts}\\text{{ V}}$, with the top plate being positive.\n\n"
        f"1. Explain why the top plate must be positive for the negatively charged drop to remain suspended.\n"
        f"2. Calculate the magnitude of the electric charge $q$ on the oil drop ($g = 9{{,}}8\\text{{ m/s}}^2$).\n"
        f"3. Determine the number of excess electrons on the drop ($e = 1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{The negative drop experiences an upward electrostatic force towards the positive top plate, balancing the downward gravitational force.}}\n"
        rf"2.\; F_E = F_g \implies q \left(\frac{{V}}{{d}}\right) = mg \implies q = \frac{{mgd}}{{V}} = "
        rf"\frac{{({_fmt_sci(m_kg)})(9{{,}}8)({_fmt_sa(d_m)})}}{{{v_volts}}} = {_fmt_sci(q_c)}\\text{{ C}}\n"
        rf"3.\; n = \frac{{q}}{{e}} = \frac{{{_fmt_sci(q_c)}}}{{1{{,}}6 \times 10^{{-19}}}} = {n_e}\text{{ electrons}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Explain upward electrostatic force balances downward gravity", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Equate forces: qE = mg or q(V/d) = mg", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate charge magnitude q = {_fmt_sci(q_c)} C", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Calculate number of excess electrons n = {n_e}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_mm_to_m_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "For the drop to hover stationary, the upward electrostatic force equals the downward weight: $F_E = F_g$.",
        "tier_2": "Substitute $F_E = q \\frac{V}{d}$ and $F_g = mg$, then solve for $q = \\frac{mgd}{V}$.",
        "tier_3": f"Charge $q = {_fmt_sci(q_c)}\\text{{ C}}$. Number of electrons: $n = q/e = {n_e}$.",
    }

    return {
        "id": f"ps_elec_millikan_{r.randint(100000, 999999)}",
        "question_id": f"ps_elec_millikan_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "25_millikan_oil_drop_levitation_equilibrium",
        "learning_objective_id": "ps_elec_25_millikan_drop",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_gravity_in_equilibrium", "inverted_potential_and_distance"],
        "keywords": ["Millikan oil drop", "equilibrium", "charge quantization", "uniform field"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Export Dictionary of Builders 01–25
BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_charge_types_and_triboelectric_series": _b01_charge_types_and_triboelectric_series,
    "02_principle_of_charge_conservation_two_spheres": _b02_principle_of_charge_conservation_two_spheres,
    "03_principle_of_charge_conservation_three_spheres": _b03_principle_of_charge_conservation_three_spheres,
    "04_quantization_of_charge_number_of_electrons": _b04_quantization_of_charge_number_of_electrons,
    "05_electron_mass_transfer_during_charging": _b05_electron_mass_transfer_during_charging,
    "06_electroscope_leaf_divergence_and_induction": _b06_electroscope_leaf_divergence_and_induction,
    "07_polarisation_of_neutral_insulators": _b07_polarisation_of_neutral_insulators,
    "08_coulombs_law_two_point_charges_direct": _b08_coulombs_law_two_point_charges_direct,
    "09_coulombs_law_proportionality_scaling": _b09_coulombs_law_proportionality_scaling,
    "10_coulombs_law_solve_for_separation_distance": _b10_coulombs_law_solve_for_separation_distance,
    "11_coulombs_law_solve_for_unknown_charge": _b11_coulombs_law_solve_for_unknown_charge,
    "12_coulomb_force_after_contact_and_separation": _b12_coulomb_force_after_contact_and_separation,
    "13_collinear_three_charges_net_force_on_centre": _b13_collinear_three_charges_net_force_on_centre,
    "14_collinear_three_charges_net_force_on_end": _b14_collinear_three_charges_net_force_on_end,
    "15_collinear_zero_net_force_equilibrium_position": _b15_collinear_zero_net_force_equilibrium_position,
    "16_perpendicular_2d_three_charges_net_force": _b16_perpendicular_2d_three_charges_net_force,
    "17_suspended_charged_pith_ball_equilibrium": _b17_suspended_charged_pith_ball_equilibrium,
    "18_electric_field_at_point_from_test_charge": _b18_electric_field_at_point_from_test_charge,
    "19_electric_field_strength_single_point_charge": _b19_electric_field_strength_single_point_charge,
    "20_electric_field_lines_pattern_interpretation": _b20_electric_field_lines_pattern_interpretation,
    "21_collinear_two_charges_net_electric_field": _b21_collinear_two_charges_net_electric_field,
    "22_collinear_neutral_point_zero_electric_field": _b22_collinear_neutral_point_zero_electric_field,
    "23_perpendicular_2d_net_electric_field": _b23_perpendicular_2d_net_electric_field,
    "24_electric_field_uniform_parallel_plates": _b24_electric_field_uniform_parallel_plates,
    "25_millikan_oil_drop_levitation_equilibrium": _b25_millikan_oil_drop_levitation_equilibrium,
}
