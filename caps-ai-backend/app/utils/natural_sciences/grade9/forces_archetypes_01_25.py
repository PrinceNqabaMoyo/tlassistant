"""Grade 9 Natural Sciences - Forces: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African comma notation."""
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
        "id": f"ns9_frc_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
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


def _svg_tug_of_war(rng: random.Random, f_left: int, f_right: int, obj_lbl: str) -> Dict[str, Any]:
    """Parameterized opposing horizontal force vector diagram."""
    l_len = max(45, min(115, int(f_left * 0.45)))
    r_len = max(45, min(115, int(f_right * 0.45)))
    y_off = rng.randint(-4, 4)
    y = 95 + y_off
    svg = (
        f'<svg viewBox="0 0 430 185" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="185" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="25" y1="{y + 32}" x2="405" y2="{y + 32}" stroke="#cbd5e1" stroke-width="2"/>'
        f'<rect x="175" y="{y - 26}" width="80" height="56" rx="4" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="215" y="{y + 6}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{obj_lbl}</text>'
        f'<line x1="175" y1="{y}" x2="{175 - l_len}" y2="{y}" stroke="#dc2626" stroke-width="3.5"/>'
        f'<polygon points="{175 - l_len},{y} {185 - l_len},{y - 6} {185 - l_len},{y + 6}" fill="#dc2626"/>'
        f'<text x="{175 - l_len // 2}" y="{y - 12}" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">{f_left} N</text>'
        f'<line x1="255" y1="{y}" x2="{255 + r_len}" y2="{y}" stroke="#2563eb" stroke-width="3.5"/>'
        f'<polygon points="{255 + r_len},{y} {245 + r_len},{y - 6} {245 + r_len},{y + 6}" fill="#2563eb"/>'
        f'<text x="{255 + r_len // 2}" y="{y - 12}" font-size="11" font-weight="bold" fill="#2563eb" text-anchor="middle">{f_right} N</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_free_body_box(rng: random.Random, fg_val: int, fn_val: int, f_app: int, f_fric: int) -> Dict[str, Any]:
    """Parameterized 4-force free-body diagram of a sliding crate/go-cart."""
    y_shift = rng.randint(-3, 3)
    cx, cy = 215, 110 + y_shift
    svg = (
        f'<svg viewBox="0 0 430 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="220" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="{cx - 28}" y="{cy - 22}" width="56" height="44" rx="4" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="{cx}" y="{cy + 4}" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Crate</text>'
        f'<line x1="{cx}" y1="{cy - 22}" x2="{cx}" y2="{cy - 76}" stroke="#16a34a" stroke-width="3"/>'
        f'<polygon points="{cx},{cy - 76} {cx - 5},{cy - 66} {cx + 5},{cy - 66}" fill="#16a34a"/>'
        f'<text x="{cx + 8}" y="{cy - 60}" font-size="10.5" font-weight="bold" fill="#15803d">N = {fn_val} N</text>'
        f'<line x1="{cx}" y1="{cy + 22}" x2="{cx}" y2="{cy + 76}" stroke="#7c3aed" stroke-width="3"/>'
        f'<polygon points="{cx},{cy + 76} {cx - 5},{cy + 66} {cx + 5},{cy + 66}" fill="#7c3aed"/>'
        f'<text x="{cx + 8}" y="{cy + 68}" font-size="10.5" font-weight="bold" fill="#6d28d9">Fg = {fg_val} N</text>'
        f'<line x1="{cx + 28}" y1="{cy}" x2="{cx + 125}" y2="{cy}" stroke="#2563eb" stroke-width="3"/>'
        f'<polygon points="{cx + 125},{cy} {cx + 115},{cy - 5} {cx + 115},{cy + 5}" fill="#2563eb"/>'
        f'<text x="{cx + 80}" y="{cy - 10}" font-size="10.5" font-weight="bold" fill="#2563eb">F_app = {f_app} N</text>'
        f'<line x1="{cx - 28}" y1="{cy}" x2="{cx - 105}" y2="{cy}" stroke="#dc2626" stroke-width="3"/>'
        f'<polygon points="{cx - 105},{cy} {cx - 95},{cy - 5} {cx - 95},{cy + 5}" fill="#dc2626"/>'
        f'<text x="{cx - 72}" y="{cy - 10}" font-size="10.5" font-weight="bold" fill="#dc2626">F_f = {f_fric} N</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_friction_normal_graph(rng: random.Random, k_coeff: float, max_n: int) -> Dict[str, Any]:
    """Parameterized linear graph of static friction vs normal force."""
    f1 = k_coeff * max_n
    x1 = 65 + int((max_n / 50.0) * 290)
    y1 = 175 - int((f1 / 25.0) * 130)
    mid_n = max_n // 2
    mid_f = k_coeff * mid_n
    xm = 65 + int((mid_n / 50.0) * 290)
    ym = 175 - int((mid_f / 25.0) * 130)
    svg = (
        f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="65" y1="25" x2="65" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="385" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="65" y1="175" x2="{x1}" y2="{y1}" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="{xm}" cy="{ym}" r="4.5" fill="#1d4ed8"/>'
        f'<circle cx="{x1}" cy="{y1}" r="4.5" fill="#1d4ed8"/>'
        f'<line x1="65" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="175" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<text x="56" y="{y1 + 4}" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="end">{_fmt_num(f1)}</text>'
        f'<text x="{x1}" y="191" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{max_n}</text>'
        f'<text x="56" y="178" font-size="11" fill="#334155" text-anchor="end">0</text>'
        f'<text x="225" y="208" font-size="11" fill="#0f172a" text-anchor="middle">Normal Force (N)</text>'
        f'<text x="20" y="100" font-size="11" fill="#0f172a" transform="rotate(-90 20 100)" text-anchor="middle">Max Static Friction (N)</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_force_definition_push_or_pull_newton_unit(rng: random.Random) -> Dict[str, Any]:
    action = rng.choice([
        ("stretching a rubber band between two fingers", "pull"),
        ("kicking a stationary soccer ball across the pitch", "push"),
        ("towing a stalled taxi using a steel cable", "pull"),
        ("pressing down onto soft clay with a thumb", "push"),
    ])
    desc, kind = action
    prompt = (
        f"Consider the action: **{desc}**.\n\n"
        "1. Define a **force** in physics [1].\n"
        f"2. Classify the applied force above as a **push** or a **pull** [1].\n"
        "3. State the SI unit and symbol used to measure forces [2]."
    )
    correct = f"A push or a pull acting on an object as a result of interaction; {kind.capitalize()}; Newton (N)"
    sol = (
        "**Step 1:** A **force** is a push or a pull exerted on one object by another object [1].\n\n"
        f"**Step 2:** {desc.capitalize()} is a **{kind}** force [1].\n\n"
        "**Step 3:** Forces are measured in **newtons** (symbol **N**), named after Sir Isaac Newton [2]."
    )
    return _q(
        rng, "01", "01_force_definition_push_or_pull_newton_unit", prompt, correct, sol, 4, "structured",
        ["confusing_force_unit_newton_with_kilogram"],
        "Think about whether objects are pushed away or drawn closer, and recall SI unit for force.",
        f"{kind.capitalize()}; SI unit = newton (N).",
        correct,
    )


def arch_02_effects_of_forces_speed_direction_and_deformation(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("A goalkeeper catches and stops a fast moving soccer ball", "decreases speed / brings a moving object to rest"),
        ("A baker squeezes a soft foam sponge flat with both hands", "deforms (changes the shape of) the object"),
        ("A cricket batsman strikes an incoming ball towards cover boundary", "changes the direction (and speed) of motion"),
        ("A sprinter pushes off starting blocks accelerating from rest", "sets a stationary object in motion (accelerates it)"),
    ])
    scene, effect = case
    prompt = (
        f"**Scenario:** *{scene}.*\n\n"
        "1. Identify the specific **effect of the force** demonstrated in this scenario [1].\n"
        "2. List **two other** possible effects that forces can have on physical objects [2]."
    )
    correct = f"{effect.capitalize()}; Forces can start motion, stop/slow motion, speed up, change direction, change shape (deform), or rotate an object"
    sol = (
        f"**Step 1:** This scenario demonstrates how a force **{effect}** [1].\n\n"
        "**Step 2:** Other general effects include altering **speed** (accelerating/decelerating), altering **direction** of velocity, rotating an object, or causing **deformation** (change in shape/size) [2]."
    )
    return _q(
        rng, "02", "02_effects_of_forces_speed_direction_and_deformation", prompt, correct, sol, 3, "structured",
        ["forces_only_cause_movement_not_shape_change_myth"],
        "Remember the four main categories: speed up, slow/stop, steer direction, or deform shape.",
        f"Here: {effect}.",
        correct,
    )


def arch_03_force_pairs_action_reaction_opposite_equal(rng: random.Random) -> Dict[str, Any]:
    mag_n = rng.choice([25, 40, 65, 80])
    pair = rng.choice([
        ("a learner pushes northward against a solid brick wall", "the brick wall pushes southward on the learner"),
        ("a swimmer pushes backward against the pool wall", "the pool wall pushes forward on the swimmer"),
        ("Earth pulls downward on a hanging apple", "the apple pulls upward on Earth"),
    ])
    act, react = pair
    prompt = (
        f"Forces always occur in **interaction pairs** between two objects. Suppose {act} with a force of **{mag_n} N**.\n\n"
        "1. Identify the exact **reaction partner force** acting at the same moment [1].\n"
        "2. State both the **magnitude** and **direction** of that partner force [2]."
    )
    correct = f"{react.capitalize()}; {mag_n} N in the exact opposite direction"
    sol = (
        f"**Step 1:** By Newton's Third Law, interaction partner: **{react}** [1].\n\n"
        f"**Step 2:** Force pairs are **equal in magnitude ({mag_n} N)** and act in **exact opposite directions** on the two different interacting bodies [2]."
    )
    return _q(
        rng, "03", "03_force_pairs_action_reaction_opposite_equal", prompt, correct, sol, 3, "structured",
        ["thinking_reaction_force_is_smaller_than_action_myth"],
        "Action-reaction pairs are ALWAYS equal in strength and opposite in direction, acting on two different objects.",
        f"{mag_n} N opposite direction; {react}.",
        correct,
    )


def arch_04_identifying_agent_and_receiver_in_force_interactions(rng: random.Random) -> Dict[str, Any]:
    ex = rng.choice([
        ("A crane magnet lifts a scrap steel car upward", "Crane magnet (exerter)", "Scrap steel car (receiver)", "magnetic field attraction"),
        ("A rugby boot kicks a rugby ball downfield", "Rugby boot", "Rugby ball", "contact push"),
        ("A tow-truck chain pulls a broken-down bakkie forward", "Tow-truck chain", "Broken-down bakkie", "tension contact pull"),
    ])
    sentence, agent, receiver, ftype = ex
    prompt = (
        f"Analyse the physical interaction: *\"{sentence}.\"*\n\n"
        "1. Identify the **agent** (object exerting the force) and the **receiver** (object experiencing the force) [2].\n"
        "2. Classify the force nature [1]."
    )
    correct = f"Agent: {agent}; Receiver: {receiver}; Nature: {ftype}"
    sol = (
        f"**Step 1:** Agent = **{agent}**; Receiver = **{receiver}** [2].\n\n"
        f"**Step 2:** Type of force = **{ftype}** [1]."
    )
    return _q(
        rng, "04", "04_identifying_agent_and_receiver_in_force_interactions", prompt, correct, sol, 3, "short_answer",
        ["confusing_force_agent_with_force_receiver"],
        "Ask: WHO/WHAT does the pushing or pulling (Agent), and ON WHAT does it act (Receiver)?",
        f"Agent: {agent}; Receiver: {receiver}.",
        correct,
    )


def arch_05_vector_force_arrow_magnitude_and_direction_representation(rng: random.Random) -> Dict[str, Any]:
    f1 = rng.choice([60, 80, 100])
    f2 = f1 * rng.choice([2, 3])
    prompt = (
        f"On a physics diagram, Force A of **{f1} N east** is drawn as a horizontal arrow of length **3 cm** pointing right.\n\n"
        f"Using the exact same vector scale, how long and in which direction must the arrow representing Force B of **{f2} N west** be drawn? [2]"
    )
    scale_len = int(3 * (f2 / f1))
    correct = f"{scale_len} cm long arrow pointing to the left (west)"
    sol = (
        f"**Step 1:** Scale ratio is $3\\text{{ cm}} : {f1}\\text{{ N}} \\Rightarrow {f2 // f1} \\times 3\\text{{ cm}} = \\mathbf{{{scale_len}\\text{{ cm}}}}$ [1].\n\n"
        "**Step 2:** Because west is opposite to east, the arrow points **left (west)** [1]."
    )
    return _q(
        rng, "05", "05_vector_force_arrow_magnitude_and_direction_representation", prompt, correct, sol, 2, "short_answer",
        ["arrow_length_unrelated_to_force_magnitude_myth"],
        "A force vector conveys BOTH magnitude (arrow length) and direction (arrowhead pointing).",
        f"Multiply 3 cm by ({f2}/{f1}) = {scale_len} cm, pointing left (west).",
        correct,
    )


def arch_06_balanced_forces_and_equilibrium_zero_net_force(rng: random.Random) -> Dict[str, Any]:
    f_val = rng.choice([120, 180, 240, 300])
    prompt = (
        f"A heavy crate sits motionless on a level factory floor while two forklifts push in opposite directions: Forklift 1 pushes **{f_val} N east** and Forklift 2 pushes **{f_val} N west**.\n\n"
        "1. Calculate the **net (resultant) force** on the crate [1].\n"
        "2. Explain what the term **balanced forces** means for the crate's state of motion [2]."
    )
    correct = "0 N (net force is zero); Balanced forces are equal and opposite so no change in speed or direction occurs (stationary crate stays at rest)"
    sol = (
        f"**Step 1:** Taking east positive: $F_{{\\text{{net}}}} = +{f_val}\\text{{ N}} + (-{f_val}\\text{{ N}}) = \\mathbf{{0\\text{{ N}}}}$ [1].\n\n"
        "**Step 2:** **Balanced forces** yield zero net force, meaning an object at rest stays stationary (or a moving object keeps constant velocity) [2]."
    )
    return _q(
        rng, "06", "06_balanced_forces_and_equilibrium_zero_net_force", prompt, correct, sol, 3, "structured",
        ["adding_opposite_forces_instead_of_subtracting_error"],
        "Equal forces pulling in opposite directions cancel out!",
        f"{f_val} N - {f_val} N = 0 N -> stays at rest.",
        correct,
    )


def arch_07_unbalanced_forces_and_net_resultant_calculation(rng: random.Random) -> Dict[str, Any]:
    f_left = rng.randint(11, 18) * 10
    f_right = f_left + rng.choice([-40, -30, 30, 50, 60])
    obj = rng.choice(["Rope knot", "Trolley", "Sled"])
    spec = _svg_tug_of_war(rng, f_left, f_right, obj)
    if f_right > f_left:
        net = f_right - f_left
        dir_str = "to the right"
    else:
        net = f_left - f_right
        dir_str = "to the left"
    prompt = (
        f"Refer to the force diagram for the **{obj}** pulled horizontally by two opposing teams.\n\n"
        f"Calculate the magnitude and direction of the **net (resultant) force** acting on the {obj}, and state whether the forces are balanced or unbalanced [3]."
    )
    correct = f"{net} N {dir_str}; Unbalanced forces"
    sol = (
        f"**Step 1:** Subtract the smaller opposing force from the larger force: $|{f_right} - {f_left}| = \\mathbf{{{net}\\text{{ N}}}}$ [2].\n\n"
        f"**Step 2:** Since the two forces differ, they are **unbalanced**, accelerating the {obj} **{dir_str}** [1]."
    )
    return _q(
        rng, "07", "07_unbalanced_forces_and_net_resultant_calculation", prompt, correct, sol, 3, "short_answer",
        ["summing_opposite_forces_for_net_force_error"],
        "Opposing vectors work against each other -> subtract magnitudes and keep the larger arrow's direction.",
        f"|{f_right} - {f_left}| = {net} N {dir_str}.",
        correct, diagram_spec=spec,
    )


def arch_08_free_body_diagram_vertical_and_horizontal_forces(rng: random.Random) -> Dict[str, Any]:
    fg = rng.choice([200, 250, 300])
    fn = fg
    f_fric = rng.choice([35, 45, 55])
    f_app = f_fric + rng.choice([45, 65, 85])
    spec = _svg_free_body_box(rng, fg, fn, f_app, f_fric)
    f_net_h = f_app - f_fric
    prompt = (
        "Examine the free-body diagram of a crate moving along a horizontal concrete floor.\n\n"
        "1. Calculate the **vertical net force** ($N$ vs $F_g$) and explain what it implies about vertical motion [2].\n"
        "2. Calculate the **horizontal net force** ($F_{\\text{app}}$ vs $F_f$) and state which way the crate accelerates [2]."
    )
    correct = f"Vertical net force = 0 N (crate stays on the floor, balanced); Horizontal net force = {f_net_h} N to the right (accelerates right)"
    sol = (
        f"**Step 1:** Vertical: $F_{{\\text{{net,y}}}} = N - F_g = {fn} - {fg} = \\mathbf{{0\\text{{ N}}}}$, so the crate neither floats up nor sinks into the floor [2].\n\n"
        f"**Step 2:** Horizontal: $F_{{\\text{{net,x}}}} = {f_app} - {f_fric} = \\mathbf{{{f_net_h}\\text{{ N}}}}$ to the **right**, so the crate accelerates rightwards [2]."
    )
    return _q(
        rng, "08", "08_free_body_diagram_vertical_and_horizontal_forces", prompt, correct, sol, 4, "structured",
        ["combining_vertical_and_horizontal_forces_in_net_force_error"],
        "Resolve vertical forces separately from horizontal forces — never mix N/Fg directly with left/right pushes!",
        f"Vertical: {fn} - {fg} = 0 N; Horizontal: {f_app} - {f_fric} = {f_net_h} N right.",
        correct, diagram_spec=spec,
    )


def arch_09_spring_balance_dynamometer_calibration_and_reading(rng: random.Random) -> Dict[str, Any]:
    reading = _fmt_num(rng.choice([3.5, 4.2, 6.8, 8.4]))
    prompt = (
        f"A learner hooks a wooden block onto a **spring balance (Newton meter)** and drags it steadily along a bench until the pointer reads **{reading} N**.\n\n"
        "1. State the physical property of the spring inside a spring balance that permits force measurement [1].\n"
        "2. Why must you zero the scale horizontally before sliding the block across the bench? [1]"
    )
    correct = "Hooke's law / elastic extension (stretch of the coil spring is directly proportional to applied pulling force); Eliminates zero/systematic offset error caused by internal spring friction or indicator drift"
    sol = (
        "**Step 1:** Inside a spring balance, **spring extension is proportional to the pulling force** within its elastic limit [1].\n\n"
        f"**Step 2:** Zeroing the balance ensures there is no **zero (systematic) error**, keeping the **{reading} N** reading accurate [1]."
    )
    return _q(
        rng, "09", "09_spring_balance_dynamometer_calibration_and_reading", prompt, correct, sol, 2, "short_answer",
        ["confusing_spring_balance_with_beam_balance"],
        "Think about what stretches inside the Newton meter and why calibration at 0 N matters.",
        "Elastic spring extension proportional to force; zeroing prevents systematic error.",
        correct,
    )


def arch_10_contact_vs_non_contact_field_force_classification(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice([
        ("Earth pulling an airborne rugby ball downward", "Field (non-contact) force — gravitational force"),
        ("Brake pads squeezing against a bicycle rim", "Contact force — friction force"),
        ("A charged balloon pulling dry hair upward without touching it", "Field (non-contact) force — electrostatic force"),
        ("Two bar magnets repelling each other across a wooden table", "Field (non-contact) force — magnetic force"),
        ("A suspension bridge steel cable holding up the road deck", "Contact force — tension force"),
    ])
    scene, ans = item
    prompt = (
        "Classify the force in the given physical situation as either a **contact force** or a **field (non-contact) force**, and name the specific type of force:\n\n"
        f"**Situation:** *{scene}.* [2]"
    )
    correct = ans
    sol = (
        "**Step 1:** Check whether direct physical touching is required between the interacting objects [1].\n\n"
        f"**Step 2:** Classification: **{ans}** [1]."
    )
    return _q(
        rng, "10", "10_contact_vs_non_contact_field_force_classification", prompt, correct, sol, 2, "short_answer",
        ["classifying_gravity_or_magnetism_as_contact_force_error"],
        "Field forces act across empty space (gravity, magnetism, electrostatics); contact forces need physical touching (friction, tension, compression, normal).",
        ans,
        correct,
    )


def arch_11_tension_pulling_force_in_ropes_cables_and_bridges(rng: random.Random) -> Dict[str, Any]:
    struct = rng.choice(["Gautrain suspension footbridge", "mine hoist steel rope pulling an ore cage", "taut washing line holding wet blankets"])
    prompt = (
        f"Consider the steel cables or ropes supporting a **{struct}**.\n\n"
        "1. Define **tension** as a contact force [1].\n"
        "2. State whether tension acts along the rope to **pull** or **compress** the load [1]."
    )
    correct = "Tension is a stretching/pulling force transmitted along a taut rope, string, wire, or cable; Always acts as a pull along the cable"
    sol = (
        "**Step 1:** **Tension** is a contact pulling force transmitted axially through a stretched rope, cable, or chain [1].\n\n"
        "**Step 2:** Unlike rigid rods, flexible ropes/cables can **only pull** (never push/compress) [1]."
    )
    return _q(
        rng, "11", "11_tension_pulling_force_in_ropes_cables_and_bridges", prompt, correct, sol, 2, "short_answer",
        ["claiming_ropes_can_push_objects_myth"],
        "Can you push a crate forward with a loose piece of string?",
        "Tension is a pulling contact force along a taut wire/rope.",
        correct,
    )


def arch_12_compression_pushing_squeezing_force_in_pillars_and_springs(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("concrete highway bridge pillars supporting traffic overhead", "Compression"),
        ("high-tensile steel suspender cables hanging from bridge towers", "Tension"),
        ("a car coil shock-absorber spring squashing over a speed hump", "Compression"),
    ])
    ex, ans = pair
    prompt = (
        "Mechanical structures experience both **compression** (pushing inward to shorten/squash) and **tension** (pulling outward to stretch).\n\n"
        f"Identify whether **{ex}** primarily experiences compression or tension, justifying your answer [2]."
    )
    correct = f"{ans}; Forces act inward to squash/push together (compression) vs pull apart (tension) along the member"
    sol = (
        f"**Step 1:** Inspect whether the load squashes or stretches the structural element [1].\n\n"
        f"**Step 2:** **{ex.capitalize()}** primarily undergoes **{ans}** [1]."
    )
    return _q(
        rng, "12", "12_compression_pushing_squeezing_force_in_pillars_and_springs", prompt, correct, sol, 2, "short_answer",
        ["mixing_tension_and_compression_in_bridges"],
        "Compression = squashing/pushing inwards; Tension = stretching/pulling outwards.",
        f"{ex} -> {ans}.",
        correct,
    )


def arch_13_friction_opposing_motion_and_microscopic_surface_roughness(rng: random.Random) -> Dict[str, Any]:
    direction = rng.choice(["northward", "westward", "down a sloped plank"])
    opp = {"northward": "southward", "westward": "eastward", "down a sloped plank": "up the sloped plank"}[direction]
    prompt = (
        f"A heavy wooden block slides **{direction}** across a concrete pavement and gradually slows to a halt.\n\n"
        "1. In which direction does the **friction force** act on the sliding block? [1]\n"
        "2. Explain on a microscopic surface level why even apparently flat surfaces experience friction [2]."
    )
    correct = f"{opp.capitalize()} (directly opposing motion); Microscopic bumps and ridges on both touching surfaces interlock and catch against each other"
    sol = (
        f"**Step 1:** Friction always opposes motion or attempted sliding, so it acts **{opp}** [1].\n\n"
        "**Step 2:** Under magnification, even smooth surfaces possess tiny **microscopic bumps and irregularities** that interlock and resist sliding past one another [2]."
    )
    return _q(
        rng, "13", "13_friction_opposing_motion_and_microscopic_surface_roughness", prompt, correct, sol, 3, "structured",
        ["friction_acts_in_same_direction_as_motion_myth"],
        "Remember: friction opposes sliding motion, and microscopically zero surfaces are perfectly flat.",
        f"Acts {opp}; microscopic ridges interlock.",
        correct,
    )


def arch_14_static_vs_kinetic_sliding_friction_investigation(rng: random.Random) -> Dict[str, Any]:
    f_peak = _fmt_num(rng.choice([6.4, 7.2, 8.8]))
    f_slide = _fmt_num(rng.choice([4.6, 5.2, 5.8]))
    prompt = (
        f"A learner pulls a brick slowly with a spring balance. The reading climbs to a maximum of **{f_peak} N** just before the brick breaks free and starts sliding, then settles to a steady **{f_slide} N** while moving at constant speed.\n\n"
        "Identify the **maximum static friction** and **kinetic (sliding) friction**, and state which is greater [2]."
    )
    correct = f"Max static friction = {f_peak} N; Kinetic friction = {f_slide} N; Static friction is greater than kinetic friction"
    sol = (
        f"**Step 1:** **Maximum static friction** = peak force right before slip (**{f_peak} N**); **kinetic friction** = force during steady sliding (**{f_slide} N**) [1].\n\n"
        "**Step 2:** Breaking stationary microscopic interlocking bonds takes more force than gliding over them, so **static > kinetic friction** [1]."
    )
    return _q(
        rng, "14", "14_static_vs_kinetic_sliding_friction_investigation", prompt, correct, sol, 2, "short_answer",
        ["kinetic_friction_greater_than_static_friction_myth"],
        "Note which reading happened just BEFORE movement vs DURING steady motion.",
        f"Static ({f_peak} N) > Kinetic ({f_slide} N).",
        correct,
    )


def arch_15_normal_force_perpendicular_support_on_horizontal_surface(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([5, 10, 15])
    weight = _fmt_num(mass * 9.8)
    prompt = (
        f"A steel toolbox of mass **{mass} kg** (weight **${weight}\\text{{ N}}$** downward) rests quietly on a flat workbench ($g = 9{{,}}8\\text{{ N/kg}}$).\n\n"
        "1. Define the **normal force ($N$)** exerted by the table [1].\n"
        "2. State the magnitude and direction of the normal force acting on this resting toolbox [2]."
    )
    correct = f"The perpendicular upward contact support force exerted by a surface on an object pressing against it; {weight} N upwards"
    sol = (
        "**Step 1:** The **normal force ($N$)** is the support force exerted by a surface **perpendicular (at $90^\\circ$)** to the surface [1].\n\n"
        f"**Step 2:** Because vertical forces are balanced on a level bench, $N = F_g = \\mathbf{{{weight}\\text{{ N}}}}$ pointing **straight upwards** [2]."
    )
    return _q(
        rng, "15", "15_normal_force_perpendicular_support_on_horizontal_surface", prompt, correct, sol, 3, "structured",
        ["confusing_normal_force_with_weight_gravity_pair"],
        "'Normal' in geometry/physics means perpendicular (90°) to the contact surface.",
        f"N = {weight} N upwards (balancing weight).",
        correct,
    )


def arch_16_relationship_between_normal_force_load_and_friction(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([0.3, 0.4, 0.5])
    max_n = rng.choice([30, 40, 50])
    f1 = k * max_n
    spec = _svg_friction_normal_graph(rng, k, max_n)
    prompt = (
        "Inspect the linear graph plotting maximum static friction force against normal force when wooden blocks are stacked on a bench.\n\n"
        "1. State the mathematical **relationship** between normal force and maximum static friction shown by the line through the origin [2].\n"
        f"2. Predict the friction force when the normal force equals **{max_n // 2} N** [1]."
    )
    half_f = _fmt_num(f1 / 2.0)
    correct = f"Maximum static friction is directly proportional to the normal force; {half_f} N"
    sol = (
        "**Step 1:** A straight line passing through $(0, 0)$ proves **maximum static friction is directly proportional to the normal force** ($f \\propto N$) [2].\n\n"
        f"**Step 2:** At half the plotted max load ($N = {max_n // 2}\\text{{ N}}$), friction is half of {_fmt_num(f1)} N = **${half_f}\\text{{ N}}$** [1]."
    )
    return _q(
        rng, "16", "16_relationship_between_normal_force_load_and_friction", prompt, correct, sol, 3, "structured",
        ["friction_unrelated_to_normal_force_myth"],
        "Look at the straight line through (0;0) and scale proportionally.",
        f"Directly proportional; at {max_n // 2} N -> {half_f} N.",
        correct, diagram_spec=spec,
    )


def arch_17_helpful_vs_nuisance_friction_everyday_reducing_methods(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("Applying oil/grease inside a squeaky bicycle chain", "reduces unwanted friction wear and heat"),
        ("Putting deep rubber tread grooves on bakkie tyres for wet Cape roads", "increases helpful friction grip to avoid skidding"),
        ("Installing steel ball bearings inside skateboard wheel hubs", "replaces sliding friction with much lower rolling friction"),
    ])
    act, purpose = case
    prompt = (
        f"Engineers actively either increase or reduce friction depending on the machine or safety requirement.\n\n"
        f"State whether **{act.lower()}** aims to increase or decrease friction, and explain the practical benefit [2]."
    )
    correct = f"{purpose.capitalize()}"
    sol = (
        "**Step 1:** Identify whether slipping is dangerous (needs high friction) or parts are rubbing and wearing (needs low friction) [1].\n\n"
        f"**Step 2:** {act} **{purpose}** [1]."
    )
    return _q(
        rng, "17", "17_helpful_vs_nuisance_friction_everyday_reducing_methods", prompt, correct, sol, 2, "short_answer",
        ["thinking_friction_is_always_harmful_myth"],
        "Without friction, tyres could not grip asphalt and shoes could not walk!",
        f"{act}: {purpose}.",
        correct,
    )


def arch_18_air_resistance_drag_surface_area_and_falling_objects(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("a flat unfolded A4 paper sheet", "an identical sheet crushed into a tight compact ball"),
        ("an open parachute canopy", "the same parachute packed tightly inside its bag"),
    ])
    wide, tight = pair
    prompt = (
        f"If you drop **{wide}** and **{tight}** simultaneously from a second-floor balcony (same mass), **{tight}** hits the ground much faster.\n\n"
        "1. Name the upward fluid friction force slowing down the wider object [1].\n"
        "2. Would both objects hit the bottom at the exact same instant inside an evacuated **vacuum tube**? Explain [2]."
    )
    correct = "Air resistance (aerodynamic drag); Yes, in a vacuum there is no air so only equal gravitational acceleration acts on both objects regardless of shape or mass"
    sol = (
        "**Step 1:** The upward fluid friction proportional to cross-sectional area is **air resistance (drag)** [1].\n\n"
        "**Step 2:** **Yes!** In a vacuum without air particles, zero air resistance exists, so gravity accelerates all falling objects identically [2]."
    )
    return _q(
        rng, "18", "18_air_resistance_drag_surface_area_and_falling_objects", prompt, correct, sol, 3, "structured",
        ["heavier_objects_fall_faster_in_a_vacuum_myth"],
        "Recall Galileo / Moon feather-and-hammer experiment: what causes flat paper to lag in room air?",
        "Air resistance slows wide area in air; in vacuum both land together.",
        correct,
    )


def arch_19_gravitational_field_force_attraction_between_masses(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["an orbiting satellite", "a thrown cricket ball", "your school desk"])
    prompt = (
        f"Which fundamental statement accurately describes **gravitational force** acting on {obj}?"
    )
    correct = "A universal non-contact attractive field force pulling every pair of objects with mass toward each other."
    distractors = [
        "A contact push caused only by atmospheric air pressure pushing downward from clouds.",
        "A force that either attracts or repels depending on whether an object is made of iron.",
        "A force that disappears completely once an object rises 100 m above Earth's surface.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Gravity is strictly **attractive** (never repulsive) and acts on **all masses** across space without touching [2]."
    )
    return _q(
        rng, "19", "19_gravitational_field_force_attraction_between_masses", prompt, correct, sol, 2, "multiple_choice",
        ["air_pressure_causes_gravity_myth"],
        "Gravity acts even on the airless Moon and attracts ALL matter with mass.",
        "Universal attractive non-contact force between all masses.",
        correct, options=options,
    )


def arch_20_gravitational_factors_mass_product_and_distance_separation(rng: random.Random) -> Dict[str, Any]:
    change = rng.choice([
        ("moving a spacecraft twice as far away from Earth's centre", "decreases strongly (drops to 1/4 of original pull)"),
        ("doubling the mass of a planet without changing its radius", "doubles (increases proportionally with mass)"),
    ])
    scenario, outcome = change
    prompt = (
        "Universal gravitational attraction between two bodies depends strictly on their **masses** and the **distance between their centres**.\n\n"
        f"State how the gravitational force between Earth and an object changes when **{scenario}** [2]."
    )
    correct = f"Gravitational attraction {outcome}"
    sol = (
        "**Step 1:** More mass creates stronger gravity ($F \\propto m_1 m_2$); larger distance weakens gravity rapidly ($F \\propto 1/r^2$) [1].\n\n"
        f"**Step 2:** Therefore, {scenario} means the force **{outcome}** [1]."
    )
    return _q(
        rng, "20", "20_gravitational_factors_mass_product_and_distance_separation", prompt, correct, sol, 2, "short_answer",
        ["larger_distance_increases_gravity_myth"],
        "Closer + heavier = stronger pull; farther + lighter = weaker pull.",
        f"{outcome}.",
        correct,
    )


def arch_21_planetary_orbits_gravity_keeping_moon_and_planets_in_orbit(rng: random.Random) -> Dict[str, Any]:
    body, centre = rng.choice([("Earth", "the Sun"), ("the Moon", "Earth"), ("Jupiter", "the Sun")])
    prompt = (
        f"Why does **{body}** travel along a continuous curved orbit around **{centre}** instead of flying straight off into deep space or crashing directly into {centre}?"
    )
    correct = f"{centre.capitalize()}'s inward gravitational pull continuously curves {body}'s high-speed forward tangential motion into a stable closed orbit."
    distractors = [
        f"Invisible magnetic ropes weld {body} rigidly to {centre}.",
        f"Zero gravity exists in space, so {body} drifts randomly in circles.",
        f"Solar wind friction holds {body} motionless at one fixed point.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Without gravity, {body}'s inertia would carry it in a straight tangent line.\n"
        f"**Step 2:** Continuous inward **gravitational attraction** bends that fast sideways motion smoothly into an **orbit** around {centre} [2]."
    )
    return _q(
        rng, "21", "21_planetary_orbits_gravity_keeping_moon_and_planets_in_orbit", prompt, correct, sol, 2, "multiple_choice",
        ["zero_gravity_in_space_orbits_myth"],
        "An orbit needs BOTH fast sideways speed AND inward gravitational pull.",
        f"Gravity curves {body}'s forward velocity around {centre}.",
        correct, options=options,
    )


def arch_22_mass_vs_weight_units_instruments_and_location_invariance(rng: random.Random) -> Dict[str, Any]:
    prop = rng.choice(["kilograms (kg)", "newtons (N)"])
    is_kg = "kg" in prop
    prompt = (
        "An astronaut packs a scientific instrument box on Earth and flies it to the Moon.\n\n"
        f"1. State whether the quantity measured in **{prop}** represents **mass** or **weight** [1].\n"
        "2. State whether that quantity stays constant or decreases on the Moon, giving a scientific definition [2]."
    )
    if is_kg:
        correct = "Mass (measured on a balance in kg); Remains constant everywhere because mass is the amount of matter inside an object"
    else:
        correct = "Weight (measured on a spring balance/dynamometer in N); Decreases (to ~1/6) on the Moon because weight is gravitational force depending on local planet gravity"
    sol = (
        f"**Step 1:** **{prop}** measures **{'mass' if is_kg else 'weight'}** [1].\n\n"
        f"**Step 2:** {correct.split('; ')[1]} [2]."
    )
    return _q(
        rng, "22", "22_mass_vs_weight_units_instruments_and_location_invariance", prompt, correct, sol, 3, "structured",
        ["mass_decreases_on_moon_error"],
        "Remember: Mass (kg) = amount of matter (constant anywhere); Weight (N) = gravitational force (varies with g).",
        f"{prop} -> {'Mass (constant)' if is_kg else 'Weight (decreases on Moon)'}.",
        correct,
    )


def arch_23_calculating_weight_w_equals_m_times_g_on_earth(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([45, 55, 65, 75, 85])
    w = mass * 9.8
    prompt = (
        f"A Grade 9 learner carries a school backpack plus books with a combined **mass of {mass} kg** on Earth ($g = 9{{,}}8\\text{{ N/kg}}$).\n\n"
        "Calculate the downward **weight ($W$)** acting on the learner + bag, showing formula, substitution, and unit [3]."
    )
    correct = f"{_fmt_num(w)} N"
    sol = (
        "**Step 1:** Formula: **$W = m \\times g$** [1].\n\n"
        f"**Step 2:** Substitute: $W = {mass}\\text{{ kg}} \\times 9{{,}}8\\text{{ N/kg}} = \\mathbf{{{_fmt_num(w)}\\text{{ N}}}}$ downwards [2]."
    )
    return _q(
        rng, "23", "23_calculating_weight_w_equals_m_times_g_on_earth", prompt, correct, sol, 3, "short_answer",
        ["dividing_mass_by_9_8_for_weight_error"],
        "Weight = mass x gravitational acceleration ($W = m \\times g$).",
        f"{mass} x 9,8 = {_fmt_num(w)} N.",
        correct,
    )


def arch_24_calculating_mass_from_weight_on_earth_or_planets(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([12, 25, 40, 60])
    planet, g_val = rng.choice([("Earth", 9.8), ("Mars", 3.7), ("Jupiter", 24.8)])
    weight = mass * g_val
    prompt = (
        f"A rover scientific crate weighs **${_fmt_num(weight)}\\text{{ N}}$** on **{planet}**, where gravitational field strength is **$g = {_fmt_num(g_val)}\\text{{ N/kg}}$**.\n\n"
        "Calculate the **mass ($m$)** of the crate in kilograms [3]."
    )
    correct = f"{mass} kg"
    sol = (
        "**Step 1:** Rearrange $W = m \\times g \\Rightarrow \\mathbf{m = \\frac{W}{g}}$ [1].\n\n"
        f"**Step 2:** $m = \\frac{{{_fmt_num(weight)}}}{{{_fmt_num(g_val)}}} = \\mathbf{{{mass}\\text{{ kg}}}}$ [2]."
    )
    return _q(
        rng, "24", "24_calculating_mass_from_weight_on_earth_or_planets", prompt, correct, sol, 3, "short_answer",
        ["multiplying_weight_by_g_to_get_mass_error"],
        "If W = m x g, divide Weight by g to recover mass m.",
        f"{_fmt_num(weight)} / {_fmt_num(g_val)} = {mass} kg.",
        correct,
    )


def arch_25_weight_comparison_across_earth_moon_mars_and_jupiter(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([50, 60, 70, 80])
    target_body, g_body = rng.choice([("Moon", 1.6), ("Mars", 3.7), ("Jupiter", 24.8)])
    w_earth = mass * 9.8
    w_target = mass * g_body
    prompt = (
        f"An explorer has a fixed body mass of **{mass} kg**.\n"
        f"Given $g_{{\\text{{Earth}}}} = 9{{,}}8\\text{{ N/kg}}$ and $g_{{\\text{{{target_body}}}}} = {_fmt_num(g_body)}\\text{{ N/kg}}$:\n\n"
        f"1. Calculate the explorer's weight on **Earth** vs on **{target_body}** [2].\n"
        f"2. What is the explorer's **mass** upon stepping onto {target_body}? [1]"
    )
    correct = f"Earth: {_fmt_num(w_earth)} N; {target_body}: {_fmt_num(w_target)} N; Mass on {target_body}: {mass} kg"
    sol = (
        f"**Step 1:** On Earth: $W = {mass} \\times 9{{,}}8 = \\mathbf{{{_fmt_num(w_earth)}\\text{{ N}}}}$. On {target_body}: $W = {mass} \\times {_fmt_num(g_body)} = \\mathbf{{{_fmt_num(w_target)}\\text{{ N}}}}$ [2].\n\n"
        f"**Step 2:** Mass depends only on matter content, remaining unchanged at **{mass} kg** [1]."
    )
    return _q(
        rng, "25", "25_weight_comparison_across_earth_moon_mars_and_jupiter", prompt, correct, sol, 3, "structured",
        ["thinking_mass_scales_with_planet_gravity_error"],
        "Use W = m x g for each body, and remember mass never changes with planet!",
        f"Earth: {_fmt_num(w_earth)} N, {target_body}: {_fmt_num(w_target)} N, Mass = {mass} kg.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_force_definition_push_or_pull_newton_unit": arch_01_force_definition_push_or_pull_newton_unit,
    "02_effects_of_forces_speed_direction_and_deformation": arch_02_effects_of_forces_speed_direction_and_deformation,
    "03_force_pairs_action_reaction_opposite_equal": arch_03_force_pairs_action_reaction_opposite_equal,
    "04_identifying_agent_and_receiver_in_force_interactions": arch_04_identifying_agent_and_receiver_in_force_interactions,
    "05_vector_force_arrow_magnitude_and_direction_representation": arch_05_vector_force_arrow_magnitude_and_direction_representation,
    "06_balanced_forces_and_equilibrium_zero_net_force": arch_06_balanced_forces_and_equilibrium_zero_net_force,
    "07_unbalanced_forces_and_net_resultant_calculation": arch_07_unbalanced_forces_and_net_resultant_calculation,
    "08_free_body_diagram_vertical_and_horizontal_forces": arch_08_free_body_diagram_vertical_and_horizontal_forces,
    "09_spring_balance_dynamometer_calibration_and_reading": arch_09_spring_balance_dynamometer_calibration_and_reading,
    "10_contact_vs_non_contact_field_force_classification": arch_10_contact_vs_non_contact_field_force_classification,
    "11_tension_pulling_force_in_ropes_cables_and_bridges": arch_11_tension_pulling_force_in_ropes_cables_and_bridges,
    "12_compression_pushing_squeezing_force_in_pillars_and_springs": arch_12_compression_pushing_squeezing_force_in_pillars_and_springs,
    "13_friction_opposing_motion_and_microscopic_surface_roughness": arch_13_friction_opposing_motion_and_microscopic_surface_roughness,
    "14_static_vs_kinetic_sliding_friction_investigation": arch_14_static_vs_kinetic_sliding_friction_investigation,
    "15_normal_force_perpendicular_support_on_horizontal_surface": arch_15_normal_force_perpendicular_support_on_horizontal_surface,
    "16_relationship_between_normal_force_load_and_friction": arch_16_relationship_between_normal_force_load_and_friction,
    "17_helpful_vs_nuisance_friction_everyday_reducing_methods": arch_17_helpful_vs_nuisance_friction_everyday_reducing_methods,
    "18_air_resistance_drag_surface_area_and_falling_objects": arch_18_air_resistance_drag_surface_area_and_falling_objects,
    "19_gravitational_field_force_attraction_between_masses": arch_19_gravitational_field_force_attraction_between_masses,
    "20_gravitational_factors_mass_product_and_distance_separation": arch_20_gravitational_factors_mass_product_and_distance_separation,
    "21_planetary_orbits_gravity_keeping_moon_and_planets_in_orbit": arch_21_planetary_orbits_gravity_keeping_moon_and_planets_in_orbit,
    "22_mass_vs_weight_units_instruments_and_location_invariance": arch_22_mass_vs_weight_units_instruments_and_location_invariance,
    "23_calculating_weight_w_equals_m_times_g_on_earth": arch_23_calculating_weight_w_equals_m_times_g_on_earth,
    "24_calculating_mass_from_weight_on_earth_or_planets": arch_24_calculating_mass_from_weight_on_earth_or_planets,
    "25_weight_comparison_across_earth_moon_mars_and_jupiter": arch_25_weight_comparison_across_earth_moon_mars_and_jupiter,
}
