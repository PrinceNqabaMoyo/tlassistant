"""Natural Sciences Grade 8 Term 2: Particle Model of Matter Generator.

Covers:
- States of matter: Microscopic arrangement, forces, spacing, and kinetic movement in solids, liquids, and gases.
- Phase changes: Melting, evaporation/boiling, condensation, freezing, and sublimation.
- Diffusion: Brownian motion and concentration gradients (factors: temperature, particle mass, state).
- Density calculations: Density = Mass / Volume (rho = m / V) with South African comma notation.
- Thermal expansion and contraction (macroscopic expansion due to microscopic particle spacing).
- Diagram integration via 3-layer anti-leak particle model plate.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

SUBSKILLS = [
    "particle_arrangement",
    "kinetic_energy_states",
    "phase_change_transitions",
    "diffusion_in_fluids",
    "density_and_particle_spacing"
]

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import build_particle_model_question


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_density_and_diffusion(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Density quantitative problems and diffusion kinetic mechanisms."""
    material = r.choice([
        {"name": "aluminium block", "density": 2.7},
        {"name": "iron cube", "density": 7.8},
        {"name": "copper ingot", "density": 8.9},
        {"name": "lead sinker", "density": 11.3},
        {"name": "pine wood block", "density": 0.5},
    ])

    volume_cm3 = r.choice([20, 25, 40, 50, 100])
    mass_g = round(material["density"] * volume_cm3, 1)
    calc_density = mass_g / volume_cm3

    qid = _make_id("ns8_density", seed, idx)

    if mode == "elementary_density_calc":
        prompt = (
            f"A solid metal sample has a mass of ${_fmt_sa(mass_g)}\\text{{ g}}$ and a volume of ${_fmt_sa(volume_cm3)}\\text{{ cm}}^3$.\n\n"
            f"Calculate the density ($\\rho$) of this material using the formula:\n"
            f"$$\\text{{Density}} = \\frac{{\\text{{Mass}}}}{{\\text{{Volume}}}}\"\""
        )
        ans_str = f"Density = {_fmt_sa(calc_density)} g/cm³"
        memo = (
            f"1. Formula: $\\rho = \\frac{{m}}{{V}}$ [M]\n"
            f"2. Substitution: $\\rho = \\frac{{{mass_g}\\text{{ g}}}}{{{volume_cm3}\\text{{ cm}}^3}} = {_fmt_sa(calc_density)}\\text{{ g/cm}}^3$ [A]"
        )
        hints = {
            "tier_1": "Divide the mass by the volume to find density in g/cm³.",
            "tier_2": f"Calculate: {mass_g} / {volume_cm3} = {calc_density}.",
            "tier_3": f"Density = {_fmt_sa(calc_density)} g/cm³.",
        }
        marks = 3
        misconceptions = ["density_formula_inversion", "omitted_units"]
    else:
        # Full compound question: Density + Diffusion + Thermal expansion
        prompt = (
            f"Grade 8 learners investigated the physical behavior of matter using the Particle Model.\n\n"
            f"1. A solid {material['name']} has a mass of ${_fmt_sa(mass_g)}\\text{{ g}}$ and occupies a volume of ${_fmt_sa(volume_cm3)}\\text{{ cm}}^3$.\n"
            f"   Calculate the density of the {material['name']} (in $\\text{{g/cm}}^3$).\n"
            f"2. A drop of food colouring was placed into a beaker of hot water ($70^\\circ\\text{{C}}$) and an identical beaker of cold water ($10^\\circ\\text{{C}}$).\n"
            f"   State which beaker will diffuse the dye faster and explain why in terms of particle kinetic energy.\n"
            f"3. Explain why railway tracks are laid with small expansion gaps between adjacent steel rails."
        )
        ans_str = (
            f"1. Density = {_fmt_sa(calc_density)} g/cm³; "
            f"2. Hot water diffuses faster because higher thermal energy gives water particles greater kinetic energy and faster speed, causing more frequent collisions that disperse dye particles rapidly; "
            f"3. On hot summer days, steel particles vibrate more vigorously and push slightly further apart (thermal expansion); expansion gaps prevent rails from buckling/warping."
        )
        memo = (
            f"1. Density calculation [3]:\n"
            f"   $$\\text{{Density}} = \\frac{{\\text{{Mass}}}}{{\\text{{Volume}}}} = \\frac{{{mass_g}\\text{{ g}}}}{{{volume_cm3}\\text{{ cm}}^3}} = {_fmt_sa(calc_density)}\\text{{ g/cm}}^3$$ [3]\n"
            f"2. Diffusion rate explanation [3]: The hot water beaker will diffuse faster [1]. "
            f"Higher temperature supplies thermal energy, increasing the average kinetic energy and velocity of water particles [1]. "
            f"These faster particles collide more frequently and forcefully with the dye particles, dispersing them more rapidly [1].\n"
            f"3. Railway expansion gaps explanation [2]: During hot weather, the iron atoms vibrate more vigorously, increasing the average inter-particle separation distance and causing the rails to expand [1]. "
            f"Gaps provide space for this thermal expansion, preventing the tracks from buckling and derailing trains [1]."
        )
        hints = {
            "tier_1": "Density = Mass / Volume. Heat makes particles move faster. Metals expand when heated.",
            "tier_2": f"Density = {mass_g} / {volume_cm3} = {calc_density} g/cm³. Faster particle movement at high temperature speeds up diffusion. Gaps allow expansion.",
            "tier_3": f"1. {_fmt_sa(calc_density)} g/cm³. 2. Hot water diffuses faster due to higher kinetic energy. 3. Prevents buckling as rails expand in heat.",
        }
        marks = 8
        misconceptions = ["particle_size_expansion_misconception", "diffusion_speed_temperature_inversion", "omitted_units"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Density calculation with units", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Kinetic explanation of thermal diffusion rate", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Thermal expansion physical rationale", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 8 Particle Model of Matter."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []
    raw_grade = str(kwargs.get("grade", 8)).replace("grade_", "").replace("g", "").strip()
    gr_int = int(raw_grade) if raw_grade.isdigit() else 8

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("particle_diagram", "states_of_matter", "phase_changes", "particle_model"):
            q = build_particle_model_question(sub_seed, grade=gr_int, mode=mode)
        elif subskill in ("density", "diffusion", "thermal_expansion") or mode == "elementary_density_calc":
            q = _generate_density_and_diffusion(sub_r, sub_seed, i, mode)
        else:
            # Deterministic subskill cycling between particle diagram and density/diffusion calculations
            if (sub_seed + i) % 2 == 0:
                q = build_particle_model_question(sub_seed, grade=gr_int, mode=mode)
            else:
                q = _generate_density_and_diffusion(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
