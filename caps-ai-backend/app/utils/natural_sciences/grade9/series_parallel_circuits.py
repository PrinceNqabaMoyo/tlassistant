"""Natural Sciences Grade 9 Term 3: Series and Parallel Circuits Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Series and Parallel circuits.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. series_circuit_current_and_voltage: Series circuit laws (I is identical everywhere, V_total = V1 + V2 + ...), total resistance increases.
2. parallel_circuit_current_and_voltage: Parallel circuit laws (V is identical across branches, I_total = I1 + I2 + ...), total resistance decreases.
3. meter_placement_ammeter_vs_voltmeter: Correct meter connection (ammeter in series, voltmeter in parallel), internal resistance rationale.
4. bulb_failure_diagnostics_series_vs_parallel: Open-circuit failure analysis, household wiring applications, independent branch control.
5. circuit_calculation_and_spec_generation: Quantitative Ohm's law calculations for combined circuits with dynamic circuit_spec emission.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Series and parallel circuits"
ORDERED_SUBSKILLS = [
    "series_circuit_current_and_voltage",
    "parallel_circuit_current_and_voltage",
    "meter_placement_ammeter_vs_voltmeter",
    "bulb_failure_diagnostics_series_vs_parallel",
    "circuit_calculation_and_spec_generation",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_spc"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 3) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    elif "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["grade"] = "9"
    res["term"] = term
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Series Circuit Current and Voltage
    if chosen_subskill == "series_circuit_current_and_voltage":
        v_bat = [6, 9, 12][actual_seed % 3]
        r1 = [2, 3, 4][actual_seed % 3]
        r2 = [4, 6, 8][actual_seed % 3]
        r_tot = r1 + r2
        i_cur = round(v_bat / r_tot, 2)
        v1 = round(i_cur * r1, 2)
        v2 = round(i_cur * r2, 2)

        question_text = (
            f"A series circuit contains a **{v_bat} V** battery connected in a single loop with two resistors: "
            f"**R₁ = {r1} Ω** and **R₂ = {r2} Ω**.\n\n"
            "1. State the fundamental rule regarding the **electric current** at any point in a series circuit.\n"
            f"2. Calculate the **total equivalent resistance (R_total)** of the series circuit.\n"
            f"3. Calculate the **electric current (I)** flowing through the circuit.\n"
            f"4. Calculate the potential difference across each resistor: **V₁** (across R₁) and **V₂** (across R₂).\n"
            "5. Verify that the sum of the potential differences equals the total battery voltage."
        )
        sample = (
            "1. **Series Current Rule:** The electric current is **identical at all points** in a series circuit (I_total = I₁ = I₂);\n"
            f"2. **Total Resistance:** R_total = R₁ + R₂ = {r1} Ω + {r2} Ω = **{r_tot} Ω**;\n"
            f"3. **Circuit Current:** I = V / R_total = {v_bat} V / {r_tot} Ω = **{i_cur} A**;\n"
            f"4. **Potential Differences:**\n"
            f"   • V₁ = I · R₁ = {i_cur} A × {r1} Ω = **{v1} V**;\n"
            f"   • V₂ = I · R₂ = {i_cur} A × {r2} Ω = **{v2} V**;\n"
            f"5. **Verification:** V₁ + V₂ = {v1} V + {v2} V = **{v_bat} V** = V_battery (Conservation of energy confirmed)."
        )
        marking = (
            "• 1 mark: Current is the same everywhere in series [1]\n"
            f"• 1 mark: Total resistance R_total = {r_tot} Ω [1]\n"
            f"• 2 marks: Current calculation: I = V/R [1], {i_cur} A [1]\n"
            f"• 2 marks: V1 = {v1} V [1], V2 = {v2} V [1]\n"
            f"• 1 mark: Sum equals battery voltage ({v_bat} V) [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": f"Series Circuit Laws: Current & Voltage Divider ({v_bat} V)",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "In a series circuit, current is the same through every single component.",
                f"Add resistors to find total resistance: {r1} + {r2} = {r_tot} Ω.",
                f"Use I = V / R = {v_bat} / {r_tot} = {i_cur} A. Voltages add up to {v_bat} V.",
            ],
            "misconception_tags": ["current_is_consumed_by_first_resistor_myth", "voltage_is_identical_across_series_resistors_myth"],
            "learning_objective_id": "NS9.EC.16.01",
        })

    # Subskill 2: Parallel Circuit Current and Voltage
    if chosen_subskill == "parallel_circuit_current_and_voltage":
        v_bat = [12, 24][actual_seed % 2]
        r1 = [6, 12][actual_seed % 2]
        r2 = [12, 24][actual_seed % 2]
        i1 = round(v_bat / r1, 1)
        i2 = round(v_bat / r2, 1)
        i_tot = round(i1 + i2, 1)

        question_text = (
            f"A parallel circuit has a **{v_bat} V** power supply connected to two parallel branches containing "
            f"resistors **R₁ = {r1} Ω** and **R₂ = {r2} Ω**.\n\n"
            "1. State the fundamental rule regarding the **potential difference (voltage)** across individual branches in a parallel circuit.\n"
            f"2. State the voltage across **R₁** and across **R₂**.\n"
            f"3. Calculate the branch current **I₁** flowing through R₁.\n"
            f"4. Calculate the branch current **I₂** flowing through R₂.\n"
            f"5. Calculate the **total current (I_total)** leaving the battery.\n"
            "6. What happens to the total circuit resistance when additional parallel branches are added?"
        )
        sample = (
            f"1. **Parallel Voltage Rule:** The potential difference (voltage) across every branch in parallel is **identical** and equal to the supply voltage (V_battery = V₁ = V₂);\n"
            f"2. **Voltages:** Both resistors experience exactly **{v_bat} V** across their terminals;\n"
            f"3. **Current I₁:** I₁ = V / R₁ = {v_bat} V / {r1} Ω = **{i1} A**;\n"
            f"4. **Current I₂:** I₂ = V / R₂ = {v_bat} V / {r2} Ω = **{i2} A**;\n"
            f"5. **Total Current:** I_total = I₁ + I₂ = {i1} A + {i2} A = **{i_tot} A**;\n"
            "6. **Total Resistance Effect:** Adding more parallel branches provides additional alternative pathways for electrons to flow, which **decreases the overall circuit resistance** and causes the total current drawn from the battery to increase."
        )
        marking = (
            "• 1 mark: Voltage is identical across all parallel branches [1]\n"
            f"• 1 mark: V1 = V2 = {v_bat} V [1]\n"
            f"• 1 mark: I1 = {i1} A [1]\n"
            f"• 1 mark: I2 = {i2} A [1]\n"
            f"• 1 mark: I_total = {i_tot} A [1]\n"
            "• 1 mark: Adding parallel branches decreases total resistance [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Parallel Circuit Laws: Branch Currents & Voltage ({v_bat} V)",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                f"Every parallel branch gets the full battery voltage ({v_bat} V).",
                "Calculate branch currents separately: I = V / R.",
                "Total current is the sum of branch currents: I_total = I1 + I2.",
            ],
            "misconception_tags": ["adding_parallel_resistors_increases_resistance_myth", "voltage_splits_in_parallel_myth"],
            "learning_objective_id": "NS9.EC.16.02",
        })

    # Subskill 3: Meter Placement Ammeter vs Voltmeter
    if chosen_subskill == "meter_placement_ammeter_vs_voltmeter":
        question_text = (
            "Measuring electrical quantities requires correct instrument placement in a circuit.\n\n"
            "1. State how an **ammeter** must be connected into a circuit (in series or in parallel) and explain why in terms of its internal resistance.\n"
            "2. State how a **voltmeter** must be connected into a circuit (in series or in parallel) and explain why in terms of its internal resistance.\n"
            "3. What would happen to the circuit if an ammeter were accidentally connected **in parallel across a light bulb**?\n"
            "4. What would happen to the circuit if a voltmeter were accidentally connected **in series in the main line**?"
        )
        sample = (
            "1. **Ammeter Connection:** Must be connected **in series** (in line with the flow of current). "
            "An ammeter has an extremely **low internal resistance (near zero)** so that it does not alter or restrict the current it is measuring;\n"
            "2. **Voltmeter Connection:** Must be connected **in parallel** (across the component). "
            "A voltmeter has an extremely **high internal resistance (near infinite)** so that virtually zero current diverts through it, preventing distortion of circuit conditions;\n"
            "3. **Ammeter in Parallel (Short Circuit):** Because the ammeter has near-zero resistance, almost all current bypasses the light bulb through the ammeter. "
            "This causes a short circuit that can draw excessive current, blowing the ammeter's internal fuse or damaging the battery;\n"
            "4. **Voltmeter in Series (Open Circuit):** Because the voltmeter has immense internal resistance, it blocks almost all current from flowing through the series loop. "
            "The circuit current drops to virtually zero, causing the light bulb to turn off, while the voltmeter simply reads the full battery voltage."
        )
        marking = (
            "• 2 marks: Ammeter in series [1], very low internal resistance to not restrict current [1]\n"
            "• 2 marks: Voltmeter in parallel [1], very high internal resistance to avoid diverting current [1]\n"
            "• 1 mark: Ammeter in parallel creates a short circuit / blows fuse [1]\n"
            "• 1 mark: Voltmeter in series blocks current, shutting off the circuit [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Instrument Placement: Ammeter vs Voltmeter Internals",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Ammeters go in SERIES (low resistance).",
                "Voltmeters go in PARALLEL across the component (high resistance).",
                "Putting an ammeter in parallel shorts out the circuit; putting a voltmeter in series stops the current.",
            ],
            "misconception_tags": ["ammeter_goes_in_parallel_error", "voltmeter_draws_heavy_current_myth"],
            "learning_objective_id": "NS9.EC.16.03",
        })

    # Subskill 4: Bulb Failure Diagnostics Series vs Parallel
    if chosen_subskill == "bulb_failure_diagnostics_series_vs_parallel":
        question_text = (
            "Consider two lighting circuits in a school building:\n\n"
            "• **Circuit S:** Three incandescent light bulbs connected in series to a 230 V power supply.\n"
            "• **Circuit P:** Three incandescent light bulbs connected in parallel to a 230 V power supply.\n\n"
            "1. If the tungsten filament of **Bulb 1 burns out (breaks)** in Circuit S, state what happens to Bulbs 2 and 3. Explain the electrical reason.\n"
            "2. If the tungsten filament of **Bulb 1 burns out (breaks)** in Circuit P, state what happens to Bulbs 2 and 3 and their brightness. Explain the electrical reason.\n"
            "3. State **two compelling practical reasons** why domestic household electrical sockets and lights are wired in parallel rather than in series.\n"
            "4. Why do old-fashioned decorative Christmas tree fairy lights, when wired in series, present a diagnostic challenge when one bulb fails?"
        )
        sample = (
            "1. **Circuit S Failure:** Bulbs 2 and 3 **extinguish immediately**. In a series circuit, there is only one continuous conducting path; when one filament breaks, it creates an open circuit (air gap) that halts all current throughout the entire loop;\n"
            "2. **Circuit P Failure:** Bulbs 2 and 3 **remain lit with unchanged brightness**. In a parallel circuit, each branch is an independent closed pathway connected directly across the 230 V supply. The broken filament only opens Branch 1;\n"
            "3. **Household Parallel Wiring Advantages:**\n"
            "   • **Independent Control & Continuity:** Switching off or failure of one appliance does not disrupt power to any other device;\n"
            "   • **Constant Operating Voltage:** Every domestic appliance receives the full rated 230 V mains potential difference, operating at intended design power;\n"
            "4. **Series Christmas Lights Problem:** Because all bulbs share one continuous series loop, if any single miniature filament burns out, all 50 bulbs extinguish simultaneously, making it time-consuming to locate the single defective bulb without testing each one individually."
        )
        marking = (
            "• 2 marks: Circuit S: both extinguish [1], single path broken creating open circuit [1]\n"
            "• 2 marks: Circuit P: remain lit at normal brightness [1], independent parallel branches [1]\n"
            "• 2 marks: Two domestic advantages: independent control [1], full 230 V voltage to all appliances [1]\n"
            "• 1 mark: All fairy lights go out at once, making the faulty bulb hard to find [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Circuit Diagnostics: Series vs Parallel Failure Modes",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Series has only ONE path: if one breaks, all go out.",
                "Parallel has separate branches: if one breaks, the others stay on with full brightness.",
                "Houses use parallel so you can turn off one light without plunging the whole house into darkness.",
            ],
            "misconception_tags": ["parallel_bulbs_dim_when_one_burns_out_myth", "homes_are_wired_in_series_myth"],
            "learning_objective_id": "NS9.EC.16.04",
        })

    # Subskill 5: Circuit Calculation and Spec Generation
    v_s = [12, 18, 24][actual_seed % 3]
    r_s = [3, 6, 9][actual_seed % 3]
    r_p1 = [6, 12][actual_seed % 2]
    r_p2 = [6, 12][actual_seed % 2]
    # R_parallel = (r_p1 * r_p2) / (r_p1 + r_p2)
    r_p_eq = round((r_p1 * r_p2) / (r_p1 + r_p2), 1)
    r_tot = round(r_s + r_p_eq, 1)
    i_tot = round(v_s / r_tot, 2)
    v_series = round(i_tot * r_s, 2)
    v_parallel = round(v_s - v_series, 2)

    question_text = (
        f"A combination electrical circuit is powered by a **{v_s} V** DC source.\n"
        f"A resistor **R_series = {r_s} Ω** is connected in series with a parallel combination consisting of "
        f"two parallel branches: **R_p1 = {r_p1} Ω** and **R_p2 = {r_p2} Ω**.\n\n"
        f"1. Calculate the **equivalent resistance (R_p)** of the parallel branch combination.\n"
        f"2. Calculate the **total circuit resistance (R_total)** connected to the source.\n"
        f"3. Calculate the **total current (I_total)** leaving the power source.\n"
        f"4. Calculate the potential difference across the series resistor: **V_series**.\n"
        f"5. Calculate the potential difference across the parallel combination: **V_parallel**."
    )
    sample = (
        f"1. **Equivalent Parallel Resistance:**\n"
        f"   1/R_p = 1/R_p1 + 1/R_p2 = 1/{r_p1} + 1/{r_p2}  ==>  R_p = ({r_p1} × {r_p2}) / ({r_p1} + {r_p2}) = **{r_p_eq} Ω**;\n"
        f"2. **Total Resistance:**\n"
        f"   R_total = R_series + R_p = {r_s} Ω + {r_p_eq} Ω = **{r_tot} Ω**;\n"
        f"3. **Total Current:**\n"
        f"   I_total = V_source / R_total = {v_s} V / {r_tot} Ω = **{i_tot} A**;\n"
        f"4. **Potential Difference V_series:**\n"
        f"   V_series = I_total · R_series = {i_tot} A × {r_s} Ω = **{v_series} V**;\n"
        f"5. **Potential Difference V_parallel:**\n"
        f"   V_parallel = V_source - V_series = {v_s} V - {v_series} V = **{v_parallel} V** (or I_total · R_p = {i_tot} × {r_p_eq} = {v_parallel} V)."
    )
    marking = (
        f"• 2 marks: Parallel equivalent calculation: R_p = {r_p_eq} Ω [2]\n"
        f"• 1 mark: Total resistance: R_total = {r_tot} Ω [1]\n"
        f"• 2 marks: Total current: I = V/R [1], {i_tot} A [1]\n"
        f"• 1 mark: V_series = {v_series} V [1]\n"
        f"• 1 mark: V_parallel = {v_parallel} V [1]\n"
        "**Total: 7 marks**"
    )
    res_dict = {
        "title": f"Combination Circuit Analysis ({v_s} V Source)",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 3,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            f"First find the parallel equivalent: R_p = (R1 × R2) / (R1 + R2) = {r_p_eq} Ω.",
            f"Add the series resistor to get total resistance: {r_s} + {r_p_eq} = {r_tot} Ω.",
            f"Use I = V / R = {v_s} / {r_tot} = {i_tot} A.",
        ],
        "misconception_tags": ["adding_series_and_parallel_without_resolving_branches_first_error", "assuming_all_resistors_get_equal_current_myth"],
        "learning_objective_id": "NS9.EC.16.05",
        "circuit_spec": {
            "type": "combination",
            "source_voltage": v_s,
            "components": [
                {"id": "V_source", "type": "dc_source", "value": v_s, "unit": "V"},
                {"id": "R_s", "type": "resistor", "value": r_s, "unit": "Ω", "placement": "series"},
                {"id": "R_p1", "type": "resistor", "value": r_p1, "unit": "Ω", "placement": "branch_1"},
                {"id": "R_p2", "type": "resistor", "value": r_p2, "unit": "Ω", "placement": "branch_2"},
            ],
            "solution": {
                "r_parallel": r_p_eq,
                "r_total": r_tot,
                "i_total": i_tot,
                "v_series": v_series,
                "v_parallel": v_parallel,
            },
        },
    }
    return _normalize_res(res_dict)
