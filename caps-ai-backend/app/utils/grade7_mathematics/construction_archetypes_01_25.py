"""
Grade 7 Mathematics - Construction of Geometric Figures Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Construction of geometric figures.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Angle Concepts & Clock Face Angles (01 - 08)
# ==============================================================================

def arch_01_identifying_arms_and_vertex(rng: random.Random) -> Dict[str, Any]:
    labels = [("P", "Q", "R"), ("A", "B", "C"), ("X", "Y", "Z"), ("K", "L", "M")]
    p1, v, p2 = rng.choice(labels)

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<line x1="40" y1="140" x2="190" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="40" y1="140" x2="140" y2="40" stroke="#1e293b" stroke-width="2.5"/>'
            f'<circle cx="40" cy="140" r="4" fill="#ef4444"/>'
            f'<circle cx="190" cy="140" r="3" fill="#1e293b"/>'
            f'<circle cx="140" cy="40" r="3" fill="#1e293b"/>'
            f'<path d="M 70,140 A 30,30 0 0,0 61,119" fill="none" stroke="#2563eb" stroke-width="2"/>'
            f'<text x="25" y="155" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#ef4444">{v}</text>'
            f'<text x="195" y="155" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e293b">{p2}</text>'
            f'<text x="145" y="35" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e293b">{p1}</text>'
            f'</svg>'
        ),
        "caption": f"Angle formed by rays {v}{p1} and {v}{p2}",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the geometric diagram.\n\n"
        f"1. Name the **vertex** of the angle.\n"
        f"2. Name the two **arms** (rays) that form this angle."
    )
    sol = (
        f"**Step 1:** The vertex is the common endpoint where the two rays meet: **Point {v}** [1 Mark: Method].\n\n"
        f"**Step 2:** The two arms of the angle are rays **{v}{p1}** (or {p1}{v}) and **{v}{p2}** (or {p2}{v}) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Vertex: {v}; Arms: {v}{p1} and {v}{p2}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "01_identifying_arms_and_vertex",
        "hints": {
            "tier_1": "The vertex is the corner point. The arms are the lines branching from the corner.",
            "tier_2": f"Corner is {v}. Arms are {v}{p1} and {v}{p2}.",
            "tier_3": f"Vertex is {v}; Arms are {v}{p1} and {v}{p2}."
        }
    }


def arch_02_correct_three_letter_naming(rng: random.Random) -> Dict[str, Any]:
    pts = [("D", "E", "F"), ("M", "N", "P"), ("R", "S", "T")]
    a, b, c = rng.choice(pts)

    prompt = (
        f"An angle has its vertex at point **{b}**, with arms passing through points **{a}** and **{c}**.\n\n"
        f"Which of the following is a mathematically correct 3-letter name for this angle?\n"
        f"A) $\\angle {a}{c}{b}$\n"
        f"B) $\\angle {a}{b}{c}$\n"
        f"C) $\\angle {b}{a}{c}$\n"
        f"Explain why."
    )
    sol = (
        f"**Step 1:** In 3-letter geometric notation, the vertex letter MUST always be placed in the **middle** [1 Mark: Method].\n\n"
        f"**Step 2:** The vertex is point {b}, so the correct name is **B) $\\angle {a}{b}{c}$** (or $\\angle {c}{b}{a}$) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"B) Angle {a}{b}{c}; vertex letter must be in the middle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_correct_three_letter_naming",
        "hints": {
            "tier_1": "Remember that the vertex must always be the middle letter.",
            "tier_2": f"Vertex is {b}, so {b} must be between {a} and {c}.",
            "tier_3": f"B) Angle {a}{b}{c}."
        }
    }


def arch_03_arm_length_misconception_check(rng: random.Random) -> Dict[str, Any]:
    angle_deg = rng.choice([30, 45, 60])

    prompt = (
        f"Learner X draws an angle of {angle_deg}° with arms 3 cm long.\n"
        f"Learner Y draws an angle of {angle_deg}° with arms 8 cm long.\n\n"
        f"Learner Y claims that their angle is bigger because the arms are longer.\n"
        f"Is Learner Y correct? Explain your reasoning."
    )
    sol = (
        f"**Step 1:** No, Learner Y is **incorrect** [1 Mark: Method].\n\n"
        f"**Step 2:** The size of an angle depends strictly on the **amount of turn (rotation)** between the arms, NOT on the length of the arms drawn. Both angles measure exactly ${angle_deg}^\\circ$ [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No; angle size depends on rotation/turn, not arm length",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_arm_length_misconception_check",
        "hints": {
            "tier_1": "Does extending the lines of an angle change how wide it opens?",
            "tier_2": f"Both angles open to {angle_deg}°.",
            "tier_3": "No; arm length does not affect angle size."
        }
    }


def arch_04_clock_face_one_hour_angle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A circular clock face is divided into 12 equal hour intervals.\n\n"
        f"1. How many degrees are there in one complete revolution?\n"
        f"2. Calculate the angle in degrees between any two consecutive hour numbers (e.g. from 12 to 1)."
    )
    sol = (
        f"**Step 1:** One complete circular revolution has **$360^\\circ$** [1 Mark: Method].\n\n"
        f"**Step 2:** Divide $360^\\circ$ by 12 equal hour marks: "
        f"$$\\frac{{360^\\circ}}{{12}} = \\mathbf{{30^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 360°; 2. 30°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_clock_face_one_hour_angle",
        "hints": {
            "tier_1": "Divide 360 degrees by 12 hours.",
            "tier_2": "360 / 12 = 30.",
            "tier_3": "1. 360°; 2. 30°."
        }
    }


def arch_05_clock_face_angles_at_exact_hours(rng: random.Random) -> Dict[str, Any]:
    cases = [(1, 30), (2, 60), (3, 90), (4, 120), (5, 150), (6, 180)]
    hr, deg = rng.choice(cases)

    # Clock SVG
    rad = math.radians(hr * 30 - 90)
    hx = 100 + 40 * math.cos(rad)
    hy = 100 + 40 * math.sin(rad)
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<circle cx="100" cy="100" r="80" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="100" y1="100" x2="100" y2="40" stroke="#1e293b" stroke-width="2.5"/>'  # minute hand at 12
            f'<line x1="100" y1="100" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#2563eb" stroke-width="3.5"/>'  # hour hand
            f'<circle cx="100" cy="100" r="4" fill="#ef4444"/>'
            f'<text x="100" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">12</text>'
            f'<text x="168" y="104" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>'
            f'<text x="100" y="174" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">6</text>'
            f'<text x="32" y="104" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">9</text>'
            f'</svg>'
        ),
        "caption": f"Clock showing {hr}:00",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the clock diagram showing **{hr}:00**.\n\n"
        f"Calculate the smaller angle (in degrees) formed between the hour hand and the minute hand."
    )
    sol = (
        f"**Step 1:** Each 1-hour jump is $30^\\circ$. At {hr}:00, the hands are {hr} hour intervals apart [1 Mark: Method].\n\n"
        f"**Step 2:** Angle = $${hr} \\times 30^\\circ = \\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "05_clock_face_angles_at_exact_hours",
        "hints": {
            "tier_1": f"Multiply the number of hours ({hr}) by 30°.",
            "tier_2": f"{hr} * 30 = {deg}.",
            "tier_3": f"{deg}°."
        }
    }


def arch_06_clock_face_reflex_angle_at_hour(rng: random.Random) -> Dict[str, Any]:
    cases = [(8, 120, 240), (9, 90, 270), (10, 60, 300), (7, 150, 210)]
    hr, smaller, reflex = rng.choice(cases)

    prompt = (
        f"At **{hr}:00**, the smaller angle between the clock hands measures ${smaller}^\\circ$.\n\n"
        f"Calculate the **reflex angle** formed on the outside between the two hands."
    )
    sol = (
        f"**Step 1:** The angles around a complete circular clock add up to $360^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract smaller angle: "
        f"$$360^\\circ - {smaller}^\\circ = \\mathbf{{{reflex}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{reflex}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_clock_face_reflex_angle_at_hour",
        "hints": {
            "tier_1": f"Subtract {smaller}° from 360°.",
            "tier_2": f"360 - {smaller} = {reflex}.",
            "tier_3": f"{reflex}°."
        }
    }


def arch_07_fractions_of_a_revolution(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("quarter turn", "1/4", 90),
        ("half turn", "1/2", 180),
        ("three-quarter turn", "3/4", 270),
        ("full turn", "1", 360)
    ]
    name, frac, deg = rng.choice(cases)

    prompt = (
        f"How many degrees are in a **{name}** ({frac} of a complete revolution)?"
    )
    sol = (
        f"**Step 1:** One full revolution $= 360^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** $${frac} \\times 360^\\circ = \\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_fractions_of_a_revolution",
        "hints": {
            "tier_1": f"Multiply 360° by {frac}.",
            "tier_2": f"360 * {frac} = {deg}.",
            "tier_3": f"{deg}°."
        }
    }


def arch_08_supplementary_angles_on_straight_line(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([35, 45, 60, 75, 110, 125, 130])
    a2 = 180 - a1

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 260 140" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<line x1="20" y1="110" x2="240" y2="110" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="130" y1="110" x2="80" y2="30" stroke="#1e293b" stroke-width="2.5"/>'
            f'<circle cx="130" cy="110" r="3.5" fill="#ef4444"/>'
            f'<text x="75" y="100" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{a1}°</text>'
            f'<text x="160" y="100" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">x</text>'
            f'</svg>'
        ),
        "caption": f"Adjacent angles on a straight line, one angle = {a1}°",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the diagram showing two adjacent angles on a straight line.\n\n"
        f"If one angle measures ${a1}^\\circ$, calculate the value of $x$."
    )
    sol = (
        f"**Step 1:** Angles on a straight line add up to $180^\\circ$ (supplementary angles) [1 Mark: Method].\n\n"
        f"**Step 2:** $$x = 180^\\circ - {a1}^\\circ = \\mathbf{{{a2}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a2}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "08_supplementary_angles_on_straight_line",
        "hints": {
            "tier_1": "Angles on a straight line sum to 180°.",
            "tier_2": f"180 - {a1}.",
            "tier_3": f"{a2}°."
        }
    }


# ==============================================================================
# CLUSTER 2: Angle Classification & Protractor Reading (09 - 16)
# ==============================================================================

def arch_09_classify_angle_by_degree(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (42, "Acute", "between 0° and 90°"),
        (90, "Right", "exactly 90°"),
        (135, "Obtuse", "between 90° and 180°"),
        (180, "Straight", "exactly 180°"),
        (245, "Reflex", "between 180° and 360°"),
        (360, "Revolution", "exactly 360°")
    ]
    deg, cat, reason = rng.choice(cases)

    prompt = (
        f"Classify an angle measuring **{deg}°** as acute, right, obtuse, straight, reflex, or revolution.\n"
        f"Give a reason for your answer."
    )
    sol = (
        f"**Step 1:** An angle measuring ${deg}^\\circ$ is classified as an **{cat} angle** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Reason: because its measurement is {reason} [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cat}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_classify_angle_by_degree",
        "hints": {
            "tier_1": f"Compare {deg}° to 90° and 180°.",
            "tier_2": f"It is {reason}.",
            "tier_3": f"{cat} angle."
        }
    }


def arch_10_calculate_reflex_angle_from_interior(rng: random.Random) -> Dict[str, Any]:
    interior = rng.choice([38, 55, 72, 115, 140])
    reflex = 360 - interior

    prompt = (
        f"An interior angle at a vertex measures **{interior}°**.\n\n"
        f"Calculate the size of the corresponding **reflex angle** around that vertex."
    )
    sol = (
        f"**Step 1:** Angles around a single point form a complete revolution ($360^\\circ$) [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\text{{Reflex angle}} = 360^\\circ - {interior}^\\circ = \\mathbf{{{reflex}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{reflex}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_calculate_reflex_angle_from_interior",
        "hints": {
            "tier_1": f"Subtract {interior}° from 360°.",
            "tier_2": f"360 - {interior} = {reflex}.",
            "tier_3": f"{reflex}°."
        }
    }


def arch_11_protractor_scale_selection_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A standard 180° semi-circular protractor has two sets of numbers (an inner scale and an outer scale).\n\n"
        f"Explain how you decide whether to read from the **inner scale** or the **outer scale** when measuring an angle."
    )
    sol = (
        f"**Step 1:** Align the origin (centre point) of the protractor over the vertex of the angle [1 Mark].\n\n"
        f"**Step 2:** Look at where the base arm of the angle passes through the protractor's baseline: start reading from the scale (inner or outer) whose **zero ($0^\\circ$)** lies on that base arm [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Start with the scale whose 0° mark aligns with the base arm of the angle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_protractor_scale_selection_concept",
        "hints": {
            "tier_1": "Look at where the zero mark is located along the bottom arm.",
            "tier_2": "Always start counting from 0° on the arm.",
            "tier_3": "Use the scale that starts at 0° on the base arm."
        }
    }


def arch_12_read_acute_angle_on_protractor(rng: random.Random) -> Dict[str, Any]:
    deg = rng.choice([35, 45, 50, 65, 75])

    # Protractor SVG diagram
    rad = math.radians(deg)
    rx = 120 + 85 * math.cos(rad)
    ry = 130 - 85 * math.sin(rad)
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<path d="M 30,130 A 90,90 0 0,1 210,130 Z" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>'
            f'<line x1="30" y1="130" x2="210" y2="130" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="120" y1="130" x2="210" y2="130" stroke="#2563eb" stroke-width="3"/>'  # base arm
            f'<line x1="120" y1="130" x2="{rx:.1f}" y2="{ry:.1f}" stroke="#2563eb" stroke-width="3"/>'  # angled arm
            f'<circle cx="120" cy="130" r="3.5" fill="#ef4444"/>'
            f'<text x="205" y="125" font-size="10" fill="#64748b">0°</text>'
            f'<text x="120" y="32" font-size="10" fill="#64748b" text-anchor="middle">90°</text>'
            f'<text x="35" y="125" font-size="10" fill="#64748b">180°</text>'
            f'<text x="{rx+10:.1f}" y="{ry:.1f}" font-size="12" font-weight="bold" fill="#2563eb">{deg}°</text>'
            f'</svg>'
        ),
        "caption": f"Protractor measuring an acute angle opening to the right",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the diagram where an angle is measured with a protractor.\n\n"
        f"State the measurement of this acute angle in degrees."
    )
    sol = (
        f"**Step 1:** The base ray points to $0^\\circ$ on the right [1 Mark: Method].\n\n"
        f"**Step 2:** Reading up along the scale to the angled ray gives: "
        f"$$\\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "12_read_acute_angle_on_protractor",
        "hints": {
            "tier_1": "Read the angle indicated by the ray passing through the curved scale.",
            "tier_2": f"The ray passes through {deg}°.",
            "tier_3": f"{deg}°."
        }
    }


def arch_13_read_obtuse_angle_on_protractor(rng: random.Random) -> Dict[str, Any]:
    deg = rng.choice([110, 125, 135, 150])

    rad = math.radians(180 - deg)
    rx = 120 - 85 * math.cos(rad)
    ry = 130 - 85 * math.sin(rad)
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<path d="M 30,130 A 90,90 0 0,1 210,130 Z" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>'
            f'<line x1="30" y1="130" x2="210" y2="130" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="120" y1="130" x2="210" y2="130" stroke="#2563eb" stroke-width="3"/>'  # base arm right
            f'<line x1="120" y1="130" x2="{rx:.1f}" y2="{ry:.1f}" stroke="#2563eb" stroke-width="3"/>'  # obtuse arm
            f'<circle cx="120" cy="130" r="3.5" fill="#ef4444"/>'
            f'<text x="205" y="125" font-size="10" fill="#64748b">0°</text>'
            f'<text x="120" y="32" font-size="10" fill="#64748b" text-anchor="middle">90°</text>'
            f'<text x="35" y="125" font-size="10" fill="#64748b">180°</text>'
            f'<text x="{rx-20:.1f}" y="{ry-5:.1f}" font-size="12" font-weight="bold" fill="#2563eb">{deg}°</text>'
            f'</svg>'
        ),
        "caption": f"Protractor measuring an obtuse angle of {deg}°",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the protractor diagram showing an obtuse angle opening from the right.\n\n"
        f"What is the size of this angle in degrees?"
    )
    sol = (
        f"**Step 1:** Since the angle is wider than a right angle ($90^\\circ$), it is obtuse [1 Mark: Method].\n\n"
        f"**Step 2:** Reading from $0^\\circ$ on the right, the ray aligns with: "
        f"$$\\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "13_read_obtuse_angle_on_protractor",
        "hints": {
            "tier_1": f"The angle is obtuse (greater than 90°).",
            "tier_2": f"Reading from 0° on the right gives {deg}°.",
            "tier_3": f"{deg}°."
        }
    }


def arch_14_angle_not_aligned_with_zero(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([20, 30, 40])
    diff = rng.choice([45, 50, 60, 70])
    t2 = t1 + diff

    prompt = (
        f"A learner places a protractor over an angle, but neither arm aligns with $0^\\circ$.\n"
        f"One arm passes through **{t1}°** and the second arm passes through **{t2}°** on the same scale.\n\n"
        f"Calculate the size of the angle."
    )
    sol = (
        f"**Step 1:** Subtract the smaller reading from the larger reading on the same scale: "
        f"$$\\text{{Angle}} = {t2}^\\circ - {t1}^\\circ \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$\\mathbf{{{diff}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_angle_not_aligned_with_zero",
        "hints": {
            "tier_1": f"Subtract the two readings: {t2} - {t1}.",
            "tier_2": f"{t2} - {t1} = {diff}.",
            "tier_3": f"{diff}°."
        }
    }


def arch_15_benchmarking_angle_estimation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Without using a protractor, explain how you can use a folded sheet of A4 paper to check whether an angle is acute, right, or obtuse."
    )
    sol = (
        f"**Step 1:** The corner of an unfolded or neatly folded sheet of A4 paper forms an exact **right angle ($90^\\circ$)** [1 Mark].\n\n"
        f"**Step 2:** Place the paper corner on the angle vertex:\n"
        f"- If the angle fits inside the paper corner, it is **acute** ($< 90^\\circ$)\n"
        f"- If it matches the corner exactly, it is **right** ($= 90^\\circ$)\n"
        f"- If it opens wider than the corner, it is **obtuse** ($> 90^\\circ$) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "The corner of A4 paper is 90°; compare the angle opening to the corner",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_benchmarking_angle_estimation",
        "hints": {
            "tier_1": "What angle does the corner of a standard sheet of paper make?",
            "tier_2": "A paper corner is 90°.",
            "tier_3": "Use the 90° paper corner to see if the angle is smaller, equal, or larger."
        }
    }


def arch_16_complementary_angles(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([25, 30, 35, 40, 55, 60, 65])
    a2 = 90 - a1

    prompt = (
        f"Two angles are **complementary** (they add up to a right angle, $90^\\circ$).\n\n"
        f"If one angle measures **{a1}°**, calculate the size of its complement."
    )
    sol = (
        f"**Step 1:** Complementary angles sum to $90^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\text{{Complement}} = 90^\\circ - {a1}^\\circ = \\mathbf{{{a2}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a2}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_complementary_angles",
        "hints": {
            "tier_1": f"Subtract {a1}° from 90°.",
            "tier_2": f"90 - {a1} = {a2}.",
            "tier_3": f"{a2}°."
        }
    }


# ==============================================================================
# CLUSTER 3: Circles, Radii & Diameters (17 - 25)
# ==============================================================================

def arch_17_definitions_circle_parts(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("radius", "a line segment joining the centre to any point on the circumference"),
        ("diameter", "a line segment passing through the centre joining two points on the circumference"),
        ("chord", "a straight line joining any two points on the circumference"),
        ("circumference", "the curved outer boundary or perimeter of the circle"),
        ("arc", "a portion or segment of the curved circumference")
    ]
    term, definition = rng.choice(cases)

    prompt = (
        f"In geometry, what is the definition of the **{term}** of a circle?"
    )
    sol = (
        f"**Step 1:** The **{term}** of a circle is defined as: "
        f"**{definition}** [2 Marks: Accurate mathematical definition]."
    )
    return {
        "id": f"g7_geo_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": definition,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_definitions_circle_parts",
        "hints": {
            "tier_1": f"Think about what '{term}' represents in circle geometry.",
            "tier_2": f"It is {definition}.",
            "tier_3": definition
        }
    }


def arch_18_radius_diameter_relationship(rng: random.Random) -> Dict[str, Any]:
    is_r_to_d = rng.choice([True, False])
    if is_r_to_d:
        r = rng.randint(3, 18)
        ans = 2 * r
        prompt = f"A circle has a radius of $r = {r}\\text{{ cm}}$. Calculate its **diameter**."
        sol = (
            f"**Step 1:** Diameter is twice the radius: $d = 2r$ [1 Mark: Method].\n\n"
            f"**Step 2:** $$d = 2 \\times {r} = \\mathbf{{{ans}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
        )
        ans_s = f"{ans} cm"
    else:
        d = rng.choice([8, 12, 14, 16, 22, 28, 36])
        ans = d / 2
        ans_int = int(ans)
        prompt = f"A circle has a diameter of $d = {d}\\text{{ cm}}$. Calculate its **radius**."
        sol = (
            f"**Step 1:** Radius is half the diameter: $r = \\frac{{d}}{{2}}$ [1 Mark: Method].\n\n"
            f"**Step 2:** $$r = \\frac{{{d}}}{{2}} = \\mathbf{{{ans_int}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
        )
        ans_s = f"{ans_int} cm"

    return {
        "id": f"g7_geo_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_radius_diameter_relationship",
        "hints": {
            "tier_1": "Diameter = 2 * Radius.",
            "tier_2": "Double the radius or halve the diameter.",
            "tier_3": ans_s
        }
    }


def arch_19_setting_compass_width_on_ruler(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([4, 5, 6, 7])

    prompt = (
        f"You need to construct a circle with a radius of **{r} cm** using a pair of compasses and a ruler.\n\n"
        f"Explain step-by-step how to set the compass legs to the correct width."
    )
    sol = (
        f"**Step 1:** Place the sharp steel point of the compass exactly on the **0 cm mark** of the ruler [1 Mark: Method].\n\n"
        f"**Step 2:** Open the compass legs until the pencil point aligns exactly with the **{r} cm mark** on the ruler [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Place sharp point on 0 cm and pencil point on {r} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_setting_compass_width_on_ruler",
        "hints": {
            "tier_1": "Put the needle on 0 and stretch the pencil to the required length.",
            "tier_2": f"Needle on 0 cm, pencil on {r} cm.",
            "tier_3": f"Set needle on 0 cm and pencil on {r} cm."
        }
    }


def arch_20_radius_from_decimal_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([7.0, 9.0, 11.0, 13.0, 15.0])
    r = d / 2.0
    r_s = f"{r:.1f}".replace(".", ",")

    prompt = (
        f"A bicycle wheel has an outer diameter of ${d:.0f}\\text{{ cm}}$.\n\n"
        f"Calculate the radius of the wheel."
    )
    sol = (
        f"**Step 1:** Radius is half the diameter: $r = \\frac{{d}}{{2}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$r = \\frac{{{d:.0f}}}{{2}} = \\mathbf{{{r_s}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r_s} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_radius_from_decimal_diameter",
        "hints": {
            "tier_1": f"Divide {d:.0f} by 2.",
            "tier_2": f"{d:.0f} / 2 = {r_s}.",
            "tier_3": f"{r_s} cm."
        }
    }


def arch_21_concentric_circles_definition(rng: random.Random) -> Dict[str, Any]:
    c_lbl = rng.choice(["O", "C", "M", "P"])
    r_outer = rng.choice([68, 70, 74, 78])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<circle cx="100" cy="100" r="{r_outer}" fill="none" stroke="#1e293b" stroke-width="2"/>'
            f'<circle cx="100" cy="100" r="45" fill="none" stroke="#2563eb" stroke-width="2"/>'
            f'<circle cx="100" cy="100" r="20" fill="none" stroke="#ef4444" stroke-width="2"/>'
            f'<circle cx="100" cy="100" r="3" fill="#0f172a"/>'
            f'<text x="100" y="93" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{c_lbl}</text>'
            f'</svg>'
        ),
        "caption": f"Three concentric circles sharing centre {c_lbl}",
        "diagram_role": "context"
    }

    prompt = (
        f"Look at the geometric diagram showing three circles with centre {c_lbl}.\n\n"
        f"1. What special term describes circles that share the exact same centre point?\n"
        f"2. How do their radii compare?"
    )
    sol = (
        f"**Step 1:** Circles sharing the same centre are called **concentric circles** [1 Mark: Method].\n\n"
        f"**Step 2:** They have the same centre but **different radii (sizes)** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Concentric circles; 2. Different radii",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "21_concentric_circles_definition",
        "hints": {
            "tier_1": "What word means 'with the same centre'?",
            "tier_2": "Concentric.",
            "tier_3": "1. Concentric circles; 2. Different radii."
        }
    }


def arch_22_touching_circles_centre_distance(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([3, 4, 5])
    r2 = rng.choice([2, 6, 7])
    dist = r1 + r2

    prompt = (
        f"Two circles touch each other externally at a single point.\n\n"
        f"The radius of Circle A is ${r1}\\text{{ cm}}$ and the radius of Circle B is ${r2}\\text{{ cm}}$.\n"
        f"Calculate the distance between their centres."
    )
    sol = (
        f"**Step 1:** For externally touching circles, the distance between centres equals the sum of their radii: "
        f"$$\\text{{Distance}} = r_1 + r_2 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$\\text{{Distance}} = {r1} + {r2} = \\mathbf{{{dist}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{dist} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_touching_circles_centre_distance",
        "hints": {
            "tier_1": "Add the two radii together.",
            "tier_2": f"{r1} + {r2} = {dist}.",
            "tier_3": f"{dist} cm."
        }
    }


def arch_23_longest_chord_is_diameter(rng: random.Random) -> Dict[str, Any]:
    r = rng.randint(5, 15)
    d = 2 * r

    prompt = (
        f"A circle has a radius of ${r}\\text{{ cm}}$.\n\n"
        f"1. What is the name of the longest possible chord that can be drawn inside this circle?\n"
        f"2. What is its length?"
    )
    sol = (
        f"**Step 1:** The longest chord of any circle passes through the centre and is called the **diameter** [1 Mark: Method].\n\n"
        f"**Step 2:** Its length is $2r = 2 \\times {r} = \\mathbf{{{d}\\text{{ cm}}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Diameter; {d} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_longest_chord_is_diameter",
        "hints": {
            "tier_1": "The longest straight line inside a circle is the diameter.",
            "tier_2": f"Diameter = 2 * {r} = {d}.",
            "tier_3": f"Diameter; {d} cm."
        }
    }


def arch_24_concentric_ring_width(rng: random.Random) -> Dict[str, Any]:
    r_in = rng.choice([3, 4, 5, 6])
    w = rng.choice([2, 3, 4])
    r_out = r_in + w

    prompt = (
        f"Two concentric circles have radii of $r_1 = {r_in}\\text{{ cm}}$ and $r_2 = {r_out}\\text{{ cm}}$.\n\n"
        f"Calculate the **width of the ring** (annulus) between the two circles."
    )
    sol = (
        f"**Step 1:** The ring width is the difference between the outer radius and inner radius: "
        f"$$w = r_2 - r_1 \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$w = {r_out} - {r_in} = \\mathbf{{{w}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{w} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_concentric_ring_width",
        "hints": {
            "tier_1": f"Subtract the inner radius from the outer radius: {r_out} - {r_in}.",
            "tier_2": f"{r_out} - {r_in} = {w}.",
            "tier_3": f"{w} cm."
        }
    }


def arch_25_circles_along_a_line(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([2, 3, 4, 5])
    d = 2 * r
    n = rng.choice([3, 4, 5])
    L = n * d

    prompt = (
        f"Identical coins each have a radius of ${r}\\text{{ cm}}$.\n\n"
        f"They are placed in a straight line touching rim-to-rim.\n"
        f"If the line of coins measures ${L}\\text{{ cm}}$ from end to end, how many coins are in the line?"
    )
    sol = (
        f"**Step 1:** The diameter of each coin is $d = 2 \\times {r} = {d}\\text{{ cm}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Number of coins: $$\\frac{{{L}}}{{{d}}} = \\mathbf{{{n}}} \\text{{ coins [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_circles_along_a_line",
        "hints": {
            "tier_1": f"Find diameter of one coin: 2 * {r} = {d} cm.",
            "tier_2": f"Divide total length {L} by {d}.",
            "tier_3": f"{n} coins."
        }
    }
