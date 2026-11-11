"""Natural Sciences Grade 8 Term 3: Electric Circuits Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Energy transfer in electrical systems.md.
Covers:
- Circuit components, standard circuit symbols, and conductor pathways.
- Series circuits: Current constancy (I_T = I_1 = I_2), voltage division (V_T = V_1 + V_2), and bulb dimming effects.
- Parallel circuits: Branch current division (I_T = I_1 + I_2), equal potential difference (V_T = V_1 = V_2), and independent branch operation.
- Correct connection rules: Ammeter in series (negligible resistance) vs Voltmeter in parallel (high resistance).
- Short circuits, safety fuses, and domestic wiring logic.
- Diagram integration via 3-layer anti-leak circuit schematic plate.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

SUBSKILLS = [
    "circuit_components",
    "meter_connection_rules",
    "parallel_vs_series_behavior",
    "series_parallel_calculations",
    "short_circuits_safety"
]

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import build_electric_circuit_ns_question


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_series_parallel_rules(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Qualitative and basic quantitative series vs parallel circuit analysis."""
    v_total = r.choice([6, 9, 12])
    v_branch1 = round(v_total / 2, 1)
    i_total = r.choice([0.6, 1.2, 2.0, 3.0])
    i_branch1 = round(i_total / 2, 1)
    qid = _make_id("ns8_circuits_rules", seed, idx)

    if mode == "elementary_meter_rules":
        prompt = (
            "Meters are used in electrical circuits to measure electrical quantities.\n\n"
            "1. Name the meter used to measure electric current and state how it must be connected in a circuit (series or parallel).\n"
            "2. Name the meter used to measure potential difference (voltage) and state how it must be connected in a circuit.\n"
            "3. Explain what happens if an ammeter is accidentally connected in parallel across a bulb."
        )
        ans_str = (
            "1. Ammeter, connected in series; "
            "2. Voltmeter, connected in parallel; "
            "3. Ammeter has near-zero resistance, so it causes a short circuit, bypassing the bulb and drawing excessive current."
        )
        memo = (
            "1. Ammeter: Connected in **series** [1].\n"
            "2. Voltmeter: Connected in **parallel** [1].\n"
            "3. Short circuit consequence [2]: An ammeter has extremely low (near zero) internal resistance [1]. "
            "Connecting it in parallel provides an effortless bypass path (short circuit) that diverts current away from the bulb and can blow a fuse or damage the meter [1]."
        )
        hints = {
            "tier_1": "Current flows through an ammeter in series. Voltage is measured across a component in parallel.",
            "tier_2": "Ammeter = series (low resistance). Voltmeter = parallel (high resistance). Putting ammeter in parallel shorts the bulb.",
            "tier_3": "1. Ammeter in series. 2. Voltmeter in parallel. 3. Causes a short circuit because ammeter has almost zero resistance.",
        }
        marks = 4
        misconceptions = ["ammeter_voltmeter_connection_inversion", "short_circuit_concept_missing"]
    else:
        # Full compound question: Series vs Parallel comparisons
        prompt = (
            f"An electrical circuit contains a ${_fmt_sa(v_total)}\\text{{ V}}$ battery and two identical light bulbs.\n\n"
            f"1. In **Circuit A**, the two bulbs are connected in **series**.\n"
            f"   a) What is the voltage across each individual bulb?\n"
            f"   b) Explain what happens to the remaining bulb if one bulb's filament burns out.\n"
            f"2. In **Circuit B**, the two identical bulbs are connected in **parallel** across the same ${_fmt_sa(v_total)}\\text{{ V}}$ battery.\n"
            f"   a) What is the voltage across each individual bulb in Circuit B?\n"
            f"   b) Compare the brightness of the bulbs in Circuit B to those in Circuit A.\n"
            f"3. State ONE reason why home lighting circuits are wired in parallel rather than in series."
        )
        ans_str = (
            f"1. a) {_fmt_sa(v_branch1)} V; b) The other bulb goes out because the circuit loop is broken; "
            f"2. a) {_fmt_sa(v_total)} V; b) Bulbs in Circuit B are significantly brighter than in Circuit A; "
            f"3. Each appliance receives full mains voltage (230V) and can be turned on/off independently without affecting other appliances."
        )
        memo = (
            f"1. Series Circuit A [2]:\n"
            f"   a) Voltage divides equally across identical series loads: $V = \\frac{{{v_total}\\text{{ V}}}}{{2}} = {_fmt_sa(v_branch1)}\\text{{ V}}$ [1].\n"
            f"   b) If one bulb blows, the physical conducting loop is broken, halting current flow so the other bulb goes out [1].\n"
            f"2. Parallel Circuit B [3]:\n"
            f"   a) Potential difference across every parallel branch equals total supply voltage: ${_fmt_sa(v_total)}\\text{{ V}}$ [1].\n"
            f"   b) Bulbs in Circuit B shine **brighter** than Circuit A [1] because they receive the full supply voltage (${_fmt_sa(v_total)}\\text{{ V}}$ vs ${_fmt_sa(v_branch1)}\\text{{ V}}$) and draw greater current [1].\n"
            f"3. Domestic parallel wiring rationale (any 1) [2]:\n"
            f"   - Each light or appliance receives the full mains potential difference (230 V) [2].\n"
            f"   - Appliances can be operated independently with their own switch; if one bulb blows, all others remain lit [2]."
        )
        hints = {
            "tier_1": "In series, voltage splits (V/2). In parallel, every branch gets full battery voltage. Full voltage = brighter light.",
            "tier_2": f"Series: {v_total}/2 = {v_branch1} V per bulb. Parallel: full {v_total} V per bulb. Parallel bulbs are brighter and work independently.",
            "tier_3": f"1. a) {v_branch1} V; b) other bulb turns off. 2. a) {v_total} V; b) Parallel is brighter. 3. Independent operation / full voltage.",
        }
        marks = 7
        misconceptions = ["parallel_voltage_division_error", "series_current_drop_misconception", "bulb_brightness_misunderstanding"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Energy Transfer in Electrical Systems > Electric circuits",
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Series voltage division and circuit break effect", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Parallel branch voltage and brightness comparison", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Domestic parallel installation rationale", "marks": 2, "editable": True},
            ],
            "deductions": [],
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
    """Master entry point for Grade 8 Electric Circuits."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("circuit_schematic", "meter_connection"):
            q = build_electric_circuit_ns_question(sub_seed, grade=8, mode=mode)
        elif subskill in ("series_parallel_rules", "domestic_circuits") or mode == "elementary_meter_rules":
            q = _generate_series_parallel_rules(sub_r, sub_seed, i, mode)
        else:
            # Alternating between circuit diagram schematic and series/parallel rules
            if i % 2 == 0:
                q = build_electric_circuit_ns_question(sub_seed, grade=8, mode=mode)
            else:
                q = _generate_series_parallel_rules(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
