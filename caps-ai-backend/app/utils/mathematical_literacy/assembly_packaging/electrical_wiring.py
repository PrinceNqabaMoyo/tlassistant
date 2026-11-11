"""Cluster 2: Domestic Electrical Plug & Appliance Wiring (Subskills 10 to 17).

Covers:
10. South African 3-pin plug wire colour coding (Live, Neutral, Earth)
11. Terminal prong placement (Earth top, Neutral left, Live right)
12. Cord clamp & cable arrester clip safety mechanics
13. 2-prong vs 3-prong plugs (earthing vs double-insulated safety)
14. Copper strand preparation & stripping dimensions (5 mm twist)
15. Appliance power rating & current amperage load (I = P / V)
16. Fault diagnosis & dangerous wiring hazards (shock & short circuit)
17. Wire length safety margins (earth wire longest for tensile fail-safe)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_asm_elec_three_pin_plug_wire_colour_identification(r: random.Random) -> Dict[str, Any]:
    wire_type = r.choice(["Live wire", "Neutral wire", "Earth wire"])
    if wire_type == "Live wire":
        correct_color = "Brown"
        role = "carries the alternating electrical current from the power supply into the appliance"
        distractors = ["Blue", "Green and Yellow stripes", "Solid Black"]
    elif wire_type == "Neutral wire":
        correct_color = "Blue"
        role = "completes the electrical circuit by returning the current to the local distribution board"
        distractors = ["Brown", "Green and Yellow stripes", "Solid Red"]
    else:
        correct_color = "Green and Yellow stripes"
        role = "provides a low-resistance safety path to the ground in case of an internal electrical fault"
        distractors = ["Brown", "Blue", "Solid White"]

    prompt = (
        f"A learner in a Mathematical Literacy practical lesson is studying the internal components of a standard "
        f"South African three-pin domestic plug (SANS 164-1 standard).\n\n"
        f"Which wire insulation colour is legally designated for the **{wire_type}**, which {role}?"
    )
    ans = correct_color
    opts = [correct_color] + distractors

    s1 = f"Recall South African domestic electrical wiring insulation colour standards: Brown = Live (L), Blue = Neutral (N), Green and Yellow stripes = Earth (E)."
    s2 = f"✓ [1 Mark: Method – Identifying standardized colour code for {wire_type}]\nStandard: Live = Brown, Neutral = Blue, Earth = Green/Yellow."
    s3 = f"✓ [1 Mark: Accuracy – Correct wire colour]\nInsulation colour: {correct_color}."

    return _build_question_payload(
        "asm_elec_three_pin_plug_wire_colour_identification",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think of the standard mnemonic: 'bLue' has an 'L' for Left (Neutral), 'bROwn' has 'R' for Right (Live), and green/yellow is the Earth.",
        tier_2_hint=f"Identify the colour designated for the {wire_type}.",
        tier_3_hint=f"The correct colour is {correct_color}.",
    )


def _gen_asm_elec_three_pin_plug_terminal_prong_placement(r: random.Random) -> Dict[str, Any]:
    terminal = r.choice(["Top (largest)", "Left (marked N)", "Right (marked L)"])
    if terminal == "Top (largest)":
        correct_wire = "Green and yellow (Earth wire)"
        explanation_wire = "Earth wire connects to the top, largest grounding prong"
        distractors = ["Brown (Live wire)", "Blue (Neutral wire)", "Black (Negative wire)"]
    elif terminal == "Left (marked N)":
        correct_wire = "Blue (Neutral wire)"
        explanation_wire = "Neutral wire connects to the left terminal prong"
        distractors = ["Brown (Live wire)", "Green and yellow (Earth wire)", "White (Ground wire)"]
    else:
        correct_wire = "Brown (Live wire)"
        explanation_wire = "Live wire connects to the right terminal prong"
        distractors = ["Blue (Neutral wire)", "Green and yellow (Earth wire)", "Grey (Neutral wire)"]

    prompt = (
        f"When looking at the opened base of an open South African 3-pin plug with the largest prong positioned at the top, "
        f"which wire must be inserted into the **{terminal} prong**?"
    )
    ans = correct_wire
    opts = [correct_wire] + distractors

    s1 = f"Identify the three terminal pins in a 3-pin plug: Top = Earth (Green/Yellow), Left = Neutral (Blue), Right = Live (Brown)."
    s2 = f"✓ [1 Mark: Method – Placement rule for {terminal} prong]\nPin layout: Top = Earth, Left = Neutral, Right = Live."
    s3 = f"✓ [1 Mark: Accuracy – Correct wire connection]\nConnection: {correct_wire}."

    return _build_question_payload(
        "asm_elec_three_pin_plug_terminal_prong_placement",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Remember: Top = Earth, Left = Neutral (Blue), Right = Live (Brown).",
        tier_2_hint=f"Check which wire corresponds to the {terminal} terminal.",
        tier_3_hint=f"The correct wire is {correct_wire}.",
    )


def _gen_asm_elec_cord_clamp_cable_arrester_safety(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is wiring a three-pin plug for an electric lawnmower. At the bottom entrance of the plug, "
        f"there is a plastic bracket secured by two small screws called the cable arrester clip (cord grip).\n\n"
        f"What is the crucial safety purpose of this cable arrester clip?"
    )
    ans = "To firmly clamp the thick outer protective sheath so that physical pulling on the cord does not yank the bare copper wires out of the terminal screws."
    opts = [
        "To firmly clamp the thick outer protective sheath so that physical pulling on the cord does not yank the bare copper wires out of the terminal screws.",
        "To insulate the metal plug prongs from the wall socket.",
        "To store spare electrical power when the lawnmower is turned off.",
        "To convert 230 V alternating current into 12 V direct current.",
    ]

    s1 = f"Understand mechanical cable strain relief and electrical fire/shock prevention."
    s2 = f"✓ [1 Mark: Method – Identifying strain relief function]\nThe cord grip must clamp down over the outer insulated jacket, ensuring mechanical tension is borne by the sheath, not the delicate copper terminal connections."
    s3 = f"✓ [1 Mark: Accuracy – Correct safety function]\nFunction: To firmly clamp the thick outer protective sheath so that physical pulling on the cord does not yank the bare copper wires out of the terminal screws."

    return _build_question_payload(
        "asm_elec_cord_clamp_cable_arrester_safety",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens if someone trips over the electrical cord while an appliance is plugged in?",
        tier_2_hint="The clip grips the outer jacket so pulling forces do not strain the screw terminals inside.",
        tier_3_hint="It prevents the bare wires from being yanked loose from the terminal pins.",
    )


def _gen_asm_elec_two_pin_vs_three_pin_comparison(r: random.Random) -> Dict[str, Any]:
    appliance = r.choice([
        ("electric kettle with an external stainless steel metal body", "3-pin plug (earthed)", "The exposed metal body requires an earth wire to safely divert fault current and trip the earth leakage breaker if a live wire touches the metal casing."),
        ("electric steam iron with a metallic soleplate and water reservoir", "3-pin plug (earthed)", "Conductive metal parts in contact with water require an earth wire to prevent lethal electric shock during an internal fault."),
        ("plastic mobile phone charger / power adapter", "2-pin plug (double insulated)", "The entirely non-conductive plastic casing is double insulated, meaning internal live wires cannot electrify the exterior surface."),
        ("plastic hair hairdryer with a double-insulated symbol (square within a square)", "2-pin plug (double insulated)", "The double insulation design ensures no exposed conductive metal can become live, eliminating the need for an earth wire."),
    ])
    app_desc, plug_type, reason = appliance

    prompt = (
        f"In a South African household, an **{app_desc}** is being fitted with a power plug.\n\n"
        f"Which type of plug is legally required, and what is the technical reason?"
    )
    ans = f"{plug_type} — {reason}"
    if "3-pin" in plug_type:
        opts = [
            f"{plug_type} — {reason}",
            "2-pin plug (unearthed) — Any appliance below 3 000 W only requires two wires.",
            "2-pin plug (unearthed) — Earth wires are only mandatory in industrial factories.",
            "3-pin plug (earthed) — The third pin is used to supply extra radio frequency signals.",
        ]
    else:
        opts = [
            f"{plug_type} — {reason}",
            "3-pin plug (earthed) — All appliances regardless of casing material must have an earth wire.",
            "3-pin plug (earthed) — Plastic casings conduct stray static electricity to the floor.",
            "2-pin plug (double insulated) — Two-prong plugs consume half the electricity of three-prong plugs.",
        ]

    s1 = f"Distinguish between Class I earthed appliances (metal exterior requiring 3-pin earthed plug) and Class II double-insulated appliances (symbol of square within a square, safe with 2-pin plug)."
    s2 = f"✓ [1 Mark: Method – Identifying appliance electrical safety class and earthing requirements]\nAppliances with exposed conductive metal casings require an earth wire (3-pin). Plastic double-insulated appliances require only 2-pin."
    s3 = f"✓ [1 Mark: Accuracy – Correct plug selection and rationale]\nRequired: {ans}"

    return _build_question_payload(
        "asm_elec_two_pin_vs_three_pin_comparison",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Does the appliance have an exposed metal casing, or is it double insulated with a plastic body?",
        tier_2_hint="Exposed metal parts require a 3-pin earthed plug; double-insulated plastic devices use 2-pin.",
        tier_3_hint=f"Correct choice is: {ans}",
    )


def _gen_asm_elec_stripping_and_twisting_copper_strands(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} strips the coloured plastic insulation from each of the three wires in a power cord.\n"
        f"The instruction manual specifies: 'Strip approximately 5 mm (0,5 cm) to 8 mm of plastic from each wire end, "
        f"and gently twist the strands of copper wire tightly with your fingers before inserting them into the terminal prongs.'\n\n"
        f"Why must the loose copper wire strands be tightly twisted together?"
    )
    ans = "To prevent stray individual wire hairs from splaying outward and touching neighboring terminals, which would cause a dangerous short circuit or fire."
    opts = [
        "To prevent stray individual wire hairs from splaying outward and touching neighboring terminals, which would cause a dangerous short circuit or fire.",
        "To increase the electrical voltage entering the appliance by 50%.",
        "To permanently weld the copper strands together through friction heat.",
        "To make the copper wire magnetic so it sticks to the plug cover.",
    ]

    s1 = f"Understand proper terminal termination and prevention of accidental bridge contact (short circuits) inside electrical plugs."
    s2 = f"✓ [1 Mark: Method – Explaining copper strand twisting rationale]\nTight twisting bundles fine copper strands into a unified cylindrical core, ensuring complete insertion into the prong hole without loose whisker strands."
    s3 = f"✓ [1 Mark: Accuracy – Correct safety explanation]\nReason: To prevent stray individual wire hairs from splaying outward and touching neighboring terminals, which would cause a dangerous short circuit or fire."

    return _build_question_payload(
        "asm_elec_stripping_and_twisting_copper_strands",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What could happen if a single loose copper hair touches an adjacent terminal inside the plug?",
        tier_2_hint="Loose strands touching another pin will create a short circuit.",
        tier_3_hint="Twisting ensures all strands fit cleanly inside the hole with no splayed whiskers.",
    )


def _gen_asm_elec_fuse_rating_and_replacement_amperage(r: random.Random) -> Dict[str, Any]:
    appliance_name = r.choice(["electric heater", "microwave oven", "electric kettle", "vacuum cleaner"])
    power_watts = r.choice([1150, 1500, 1840, 2070, 2300])
    voltage = 230  # Standard South African mains supply voltage (230 V)
    current_amps = round(power_watts / voltage, 2)
    # Available fuse ratings in South Africa / UK plugs: 3A, 5A, 10A, 13A, 16A
    standard_fuses = [3, 5, 10, 13, 16]
    selected_fuse = next(f for f in standard_fuses if f > current_amps)

    prompt = (
        f"A domestic {appliance_name} is rated at {power_watts} W (Watts) and connects to the South African "
        f"mains electricity supply of {voltage} V (Volts).\n\n"
        f"Formula: Current (in Amperes) = Power (in Watts) ÷ Voltage (in Volts) [I = P / V]\n\n"
        f"1. Calculate the operating electric current (in Amperes) drawn by this appliance (rounded to 2 decimal places).\n"
        f"2. From the standard fuse ratings available (3 A, 5 A, 10 A, 13 A, 16 A), select the most appropriate fuse rating."
    )
    ans = f"{_fmt(current_amps)} A — use {selected_fuse} A fuse"

    s1 = f"Calculate electric current using formula I = P / V ({power_watts} W ÷ {voltage} V), then choose the smallest standard fuse rating greater than the calculated current."
    s2 = f"✓ [1 Mark: Method – Calculating current and selecting fuse rating]\nCurrent = {power_watts} ÷ {voltage} = {_fmt(current_amps)} A.\nAppropriate fuse must exceed operating current without nuisance blowing."
    s3 = f"✓ [1 Mark: Accuracy – Final amperage and fuse selection]\nOperating current = {_fmt(current_amps)} A; recommended rating = {selected_fuse} A fuse."

    return _build_question_payload(
        "asm_elec_fuse_rating_and_replacement_amperage",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide power ({power_watts} W) by mains voltage ({voltage} V).",
        tier_2_hint=f"{power_watts} ÷ {voltage} = {_fmt(current_amps)} A. Choose the next standard fuse above this value.",
        tier_3_hint=f"{_fmt(current_amps)} A — use {selected_fuse} A fuse.",
    )


def _gen_asm_elec_fault_identification_incorrect_wiring(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fault = r.choice([
        (
            "connected the brown (live) wire to the top earth prong and the green/yellow wire to the right live terminal",
            "Extremely dangerous: The metal casing of the appliance will become live with 230 V electricity, posing an immediate fatal electric shock risk to anyone touching it.",
            "The appliance will run backwards at half speed.",
            "The electricity meter will credit units back to the household.",
            "The light bulb will shine blue instead of white."
        ),
        (
            "left the green/yellow earth wire completely disconnected inside a metal kettle plug",
            "Hazardous: If an internal heating element develops a fault and touches the metal kettle body, the circuit will not trip and the kettle will remain live with lethal voltage.",
            "The kettle will boil water twice as quickly.",
            "The water will become carbonated.",
            "The electricity tariff will switch to off-peak rates automatically."
        ),
    ])
    fault_desc, danger, d1, d2, d3 = fault

    prompt = (
        f"{name} wired a 3-pin plug for an electric kettle with a stainless steel body, but mistakenly {fault_desc}.\n\n"
        f"What is the serious electrical hazard and consequence of this incorrect wiring?"
    )
    ans = danger
    opts = [danger, d1, d2, d3]

    s1 = f"Understand domestic electrical safety hazards, earthing mechanics, and fatal shock risks caused by crossed or disconnected wires."
    s2 = f"✓ [1 Mark: Method – Analyzing electrical circuit fault and earthing failure]\nThe earth terminal connects directly to the metal exterior chassis. Connecting live to earth or omitting earth creates a severe shock hazard."
    s3 = f"✓ [1 Mark: Accuracy – Correct hazard identification]\nConsequence: {danger}"

    return _build_question_payload(
        "asm_elec_fault_identification_incorrect_wiring",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about what parts of the kettle are touched by hands.",
        tier_2_hint="If the live wire electrifies the metal chassis, anyone touching it receives a severe electric shock.",
        tier_3_hint=f"Correct hazard: {danger}",
    )


def _gen_asm_elec_cable_length_stripping_measurement(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When electricians strip the outer sheath to wire a South African three-pin plug, "
        f"they intentionally trim the Live (Brown) and Neutral (Blue) wires slightly shorter "
        f"than the Green/Yellow (Earth) wire, leaving the Earth wire with extra slack.\n\n"
        f"What is the vital engineering safety reason for keeping the Earth wire the longest?"
    )
    ans = "If the cable is violently pulled or yanked from the plug, the Live and Neutral wires will snap or disconnect first while the Earth wire remains connected to protect the user."
    opts = [
        "If the cable is violently pulled or yanked from the plug, the Live and Neutral wires will snap or disconnect first while the Earth wire remains connected to protect the user.",
        "The earth wire requires more length because earth electricity travels slower than live electricity.",
        "The longer wire acts as an FM radio antenna to reduce electrical buzzing noises.",
        "It makes the plug easier to close without needing a screwdriver.",
    ]

    s1 = f"Understand safety-in-design principles for domestic appliance wiring (tensile failure hierarchy)."
    s2 = f"✓ [1 Mark: Method – Tensile failure sequence in plug wiring]\nIf the cord grip fails and the cable is pulled, live conductors must disconnect first, de-energizing the circuit before earth protection is lost."
    s3 = f"✓ [1 Mark: Accuracy – Correct mechanical safety rationale]\nReason: If the cable is violently pulled or yanked from the plug, the Live and Neutral wires will snap or disconnect first while the Earth wire remains connected to protect the user."

    return _build_question_payload(
        "asm_elec_cable_length_stripping_measurement",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens to the wires inside if the cable is violently yanked?",
        tier_2_hint="Leaving the earth wire longer ensures that live wires disconnect first while the ground protection stays intact.",
        tier_3_hint="It ensures the earth wire is the last wire to disconnect under extreme tension.",
    )
