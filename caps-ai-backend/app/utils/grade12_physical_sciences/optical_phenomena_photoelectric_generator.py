"""Grade 12 Physical Sciences — Optical Phenomena & Photoelectric Effect Generator.
Deterministic 6-pillar CAPS question generator covering Paper 1 (Physics Term 3):
- Dual particle-wave nature of light: Photoelectric effect as evidence for particle nature.
- Work function (W0) and threshold (cut-off) frequency (f0): W0 = h * f0.
- Einstein's photoelectric equation: E = W0 + Ek_max => hf = W0 + 1/2 m (v_max)^2.
- Cut-off wavelength (lambda_0 = c / f0) and photon energy (E = hf = hc / lambda).
- Effect of frequency vs intensity of incident light on emission rate and kinetic energy.
- Emission and absorption line spectra.

Constants (from CAPS Physics Data Sheet):
- Planck's constant: h = 6.63 x 10^-34 J.s
- Speed of light in vacuum: c = 3.0 x 10^8 m/s
- Mass of an electron: m_e = 9.11 x 10^-31 kg
- Elementary charge: e = 1.6 x 10^-19 C

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{{,}}")


METALS_DATA = [
    {"name": "Sodium (Na)", "w0_joules": 3.65e-19, "w0_ev": 2.28},
    {"name": "Potassium (K)", "w0_joules": 3.68e-19, "w0_ev": 2.30},
    {"name": "Zinc (Zn)", "w0_joules": 6.88e-19, "w0_ev": 4.30},
    {"name": "Platinum (Pt)", "w0_joules": 1.01e-18, "w0_ev": 6.35},
    {"name": "Cesium (Cs)", "w0_joules": 3.42e-19, "w0_ev": 2.14},
    {"name": "Copper (Cu)", "w0_joules": 7.52e-19, "w0_ev": 4.70},
]

H = 6.63e-34
C = 3.0e8
ME = 9.11e-31


def _build_photoelectric_drill(r: random.Random) -> Dict[str, Any]:
    metal = r.choice(METALS_DATA)
    w0 = metal["w0_joules"]
    f0 = w0 / H
    lambda0 = (C / f0) * 1e9  # in nm

    # Choose incident frequency above threshold: 1.25x to 2.2x f0
    multiplier = round(r.uniform(1.3, 2.0), 2)
    f_incident = f0 * multiplier
    e_photon = H * f_incident
    ek_max = e_photon - w0
    v_max = math.sqrt((2 * ek_max) / ME)

    prompt = (
        f"In a photoelectric experiment, ultraviolet radiation of frequency "
        f"**${f_incident:.2e}\\text{{ Hz}}$** is shone onto the clean surface of a **{metal['name']}** cathode.\n"
        f"The work function of {metal['name']} is **${w0:.2e}\\text{{ J}}$**.\n\n"
        f"1. Define the term *work function* ($W_0$) of a metal.\n"
        f"2. Calculate the threshold frequency ($f_0$) of {metal['name']}.\n"
        f"3. Calculate the maximum kinetic energy ($E_{{k,\\text{{max}}}}$) of the ejected photoelectrons.\n"
        f"4. Calculate the maximum speed ($v_{{\\text{{max}}}}$) with which photoelectrons leave the cathode surface.\n"
        f"5. State the effect on $E_{{k,\\text{{max}}}}$ if the intensity of the incident radiation is doubled while keeping the frequency constant."
    )

    sol = (
        f"1. **Work function:** The minimum amount of energy needed to emit an electron from the surface of a metal.\n\n"
        f"2. $W_0 = h f_0$\n"
        f"   $f_0 = \\frac{{W_0}}{{h}} = \\frac{{{w0:.2e}}}{{6{{,}}63 \\times 10^{{-34}}}} = {f0:.2e}\\text{{ Hz}}$\n\n"
        f"3. $E = W_0 + E_{{k,\\text{{max}}}}$\n"
        f"   $h f = W_0 + E_{{k,\\text{{max}}}}$\n"
        f"   $(6{{,}}63 \\times 10^{{-34}})({f_incident:.2e}) = {w0:.2e} + E_{{k,\\text{{max}}}}$\n"
        f"   ${e_photon:.2e} = {w0:.2e} + E_{{k,\\text{{max}}}}$\n"
        f"   $E_{{k,\\text{{max}}}} = {e_photon:.2e} - {w0:.2e} = {ek_max:.2e}\\text{{ J}}$\n\n"
        f"4. $E_{{k,\\text{{max}}}} = \\frac{{1}}{{2}} m v_{{\\text{{max}}}}^2$\n"
        f"   ${ek_max:.2e} = \\frac{{1}}{{2}} (9{{,}}11 \\times 10^{{-31}}) v_{{\\text{{max}}}}^2$\n"
        f"   $v_{{\\text{{max}}}}^2 = \\frac{{2 \\times {ek_max:.2e}}}{{9{{,}}11 \\times 10^{{-31}}}} = {((2 * ek_max) / ME):.2e}$\n"
        f"   $v_{{\\text{{max}}}} = {v_max:.2e}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n\n"
        f"5. **No effect / Remains unchanged.** Increasing the intensity increases the number of photoelectrons emitted per second, but does not alter the energy of individual photons or $E_{{k,\\text{{max}}}}$."
    )

    return {
        "id": f"g12_ps_photo_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"f0={f0:.2e} Hz, Ek_max={ek_max:.2e} J, vmax={v_max:.2e} m/s",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of work function: minimum energy required to emit an electron", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: W0 = h * f0", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate f0 = {f0:.2e} Hz", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Formula: E = W0 + Ek_max (or hf = W0 + Ek_max)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate Ek_max = {ek_max:.2e} J", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Calculate vmax = {v_max:.2e} m/s", "marks": 1, "editable": True},
                {"id": "mp7", "desc": "Intensity effect: No effect on Ek_max (increases emission rate only)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "confused_intensity_and_frequency_effects", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Apply Einstein's photoelectric equation: $E = W_0 + E_{k,\\text{max}}$ where $E = hf$.",
            "tier_2": "Threshold frequency is calculated from $W_0 = h f_0$. Maximum velocity from $E_{k,\\text{max}} = \\frac{1}{2}m v_{\\text{max}}^2$.",
            "tier_3": f"$f_0 = {w0:.2e} / 6{{,}}63 \\times 10^{{-34}} = {f0:.2e}\\text{{ Hz}}$. $E_{{k,\\text{{max}}}} = {ek_max:.2e}\\text{{ J}}$.",
        },
        "misconception_tags": ["confused_intensity_and_frequency_effects", "forgot_threshold_frequency_condition"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    return _build_photoelectric_drill(r)
