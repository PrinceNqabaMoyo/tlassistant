"""
Grade 7 Mathematics - Construction of Geometric Figures Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Construction of geometric figures.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Basic Compass Constructions (26 - 34)
# ==============================================================================

def arch_26_circle_construction_steps(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([3, 4, 5, 6])

    prompt = (
        f"List the 4 key steps required to construct a circle of radius **{r} cm** using a compass and ruler."
    )
    sol = (
        f"**Step 1:** Use a ruler to set the distance between the sharp compass point and pencil to exactly {r} cm [1 Mark].\n\n"
        f"**Step 2:** Mark a small dot on the paper to be the centre $O$ of the circle.\n\n"
        f"**Step 3:** Place the sharp point firmly on $O$.\n\n"
        f"**Step 4:** Rotate the pencil $360^\\circ$ smoothly around $O$ keeping the compass legs at a fixed width [1 Mark: Complete procedural accuracy]."
    )
    return {
        "id": f"g7_geo_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Set compass to {r} cm on ruler, mark centre, place needle on centre, rotate 360°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_circle_construction_steps",
        "hints": {
            "tier_1": f"Measure {r} cm, mark centre, hold needle firmly, rotate.",
            "tier_2": "Set radius on ruler, mark point O, draw circle.",
            "tier_3": f"Set {r} cm, mark centre, insert needle, rotate 360°."
        }
    }


def arch_27_perpendicular_bisector_steps(rng: random.Random) -> Dict[str, Any]:
    len_ab = rng.choice([6, 8, 10, 12])
    half_ab = len_ab // 2
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<line x1="40" y1="80" x2="200" y2="80" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="120" y1="20" x2="120" y2="140" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,3"/>'
            f'<path d="M 105,40 A 50,50 0 0,1 135,40" stroke="#94a3b8" stroke-width="1.5" fill="none"/>'
            f'<path d="M 105,120 A 50,50 0 0,1 135,120" stroke="#94a3b8" stroke-width="1.5" fill="none"/>'
            f'<circle cx="40" cy="80" r="3.5" fill="#ef4444"/>'
            f'<circle cx="200" cy="80" r="3.5" fill="#ef4444"/>'
            f'<circle cx="120" cy="80" r="3" fill="#2563eb"/>'
            f'<text x="35" y="95" font-size="12" font-weight="bold" fill="#0f172a">A</text>'
            f'<text x="200" y="95" font-size="12" font-weight="bold" fill="#0f172a">B</text>'
            f'<text x="125" y="95" font-size="12" font-weight="bold" fill="#2563eb">M ({len_ab} cm)</text>'
            f'</svg>'
        ),
        "caption": f"Perpendicular bisector of segment AB ({len_ab} cm) intersecting at midpoint M",
        "diagram_role": "context"
    }

    prompt = (
        f"When constructing the perpendicular bisector of line segment $AB$ of length {len_ab} cm:\n\n"
        f"1. Why must the compass width be opened to **more than half** the length of $AB$ (i.e. $> {half_ab}\\text{{ cm}}$)?\n"
        f"2. What two geometric properties does the constructed line have relative to segment $AB$?"
    )
    sol = (
        f"**Step 1:** If the compass width is less than or equal to half of $AB$, the two circular arcs from $A$ and $B$ will **not intersect** above and below the line [1 Mark].\n\n"
        f"**Step 2:** The constructed line: (a) cuts $AB$ in half at its **midpoint** (bisects it), and (b) meets $AB$ at an exact **$90^\\circ$ right angle** (perpendicular) [1 Mark]."
    )
    return {
        "id": f"g7_geo_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Arcs must intersect; 2. Perpendicular (90°) and bisects (cuts in half)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "27_perpendicular_bisector_steps",
        "hints": {
            "tier_1": "What happens if the arcs are too small to touch? What does 'perpendicular' and 'bisector' mean?",
            "tier_2": "Arcs must overlap to create crossing points. It makes 90° and cuts in half.",
            "tier_3": "1. So arcs intersect; 2. Perpendicular (90°) and cuts in half."
        }
    }


def arch_28_midpoint_calculation_from_bisector(rng: random.Random) -> Dict[str, Any]:
    ab = rng.choice([6, 8, 10, 12, 14, 16])
    am = ab // 2

    prompt = (
        f"A line segment $AB$ has a length of **{ab} cm**.\n"
        f"Its perpendicular bisector cuts the segment at midpoint $M$.\n\n"
        f"Calculate the length of segment $AM$."
    )
    sol = (
        f"**Step 1:** A bisector divides a line segment into two exactly equal halves: "
        f"$$AM = \\frac{{AB}}{{2}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$AM = \\frac{{{ab}}}{{2}} = \\mathbf{{{am}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{am} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_midpoint_calculation_from_bisector",
        "hints": {
            "tier_1": f"Halve {ab} cm.",
            "tier_2": f"{ab} / 2 = {am}.",
            "tier_3": f"{am} cm."
        }
    }


def arch_29_angle_bisector_steps(rng: random.Random) -> Dict[str, Any]:
    angle_val = rng.choice([60, 70, 80, 100])
    half_angle = angle_val // 2

    prompt = (
        f"An angle $\\angle ABC$ measures **{angle_val}°**.\n\n"
        f"1. What is an **angle bisector**?\n"
        f"2. If ray $BD$ bisects $\\angle ABC$, calculate the size of $\\angle ABD$."
    )
    sol = (
        f"**Step 1:** An angle bisector is a line or ray that divides an angle into **two equal angles** [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\angle ABD = \\frac{{{angle_val}^\\circ}}{{2}} = \\mathbf{{{half_angle}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. A line dividing an angle into two equal parts; 2. {half_angle}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_angle_bisector_steps",
        "hints": {
            "tier_1": f"To bisect means to divide in half. Divide {angle_val}° by 2.",
            "tier_2": f"{angle_val} / 2 = {half_angle}.",
            "tier_3": f"1. Divides angle into two equal parts; 2. {half_angle}°."
        }
    }


def arch_30_construct_sixty_degree_angle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain how to construct an exact **60° angle** using only a pair of compasses and a straightedge (no protractor)."
    )
    sol = (
        f"**Step 1:** Draw a base line segment $AB$. Set the compass to width $AB$ and draw an arc from $A$ above the line [1 Mark].\n\n"
        f"**Step 2:** Without changing compass width, draw a second arc from $B$ intersecting the first arc at point $C$. Join $A$ to $C$. Because triangle $ABC$ is equilateral (all three sides equal), $\\angle CAB = \\mathbf{{60^\\circ}}$ [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Draw equilateral triangle using equal compass arcs; each angle of equilateral triangle is 60°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_construct_sixty_degree_angle",
        "hints": {
            "tier_1": "What type of triangle has all angles equal to 60°?",
            "tier_2": "An equilateral triangle.",
            "tier_3": "Construct an equilateral triangle with equal compass arcs; the corner angle is 60°."
        }
    }


def arch_31_construct_thirty_degree_angle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"How can you construct an angle of **30°** using only a compass and straightedge?"
    )
    sol = (
        f"**Step 1:** Construct a **$60^\\circ$ angle** first using the equilateral triangle arc method [1 Mark].\n\n"
        f"**Step 2:** Use compass arcs to construct the **angle bisector** of the $60^\\circ$ angle. Halving $60^\\circ$ produces: "
        f"$$\\frac{{60^\\circ}}{{2}} = \\mathbf{{30^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Construct a 60° angle and bisect it to obtain 30°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_construct_thirty_degree_angle",
        "hints": {
            "tier_1": "30° is half of 60°.",
            "tier_2": "Construct 60° and bisect it.",
            "tier_3": "Construct a 60° angle, then construct its angle bisector."
        }
    }


def arch_32_construct_ninety_degree_angle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain how to construct an exact **90° right angle** at a point $P$ on a straight line using compass arcs."
    )
    sol = (
        f"**Step 1:** Place the compass on $P$ and draw arcs on either side of $P$ to create two equidistant points $A$ and $B$ ($P$ is now the midpoint of $AB$) [1 Mark].\n\n"
        f"**Step 2:** Open compass wider than $AP$. Draw intersecting arcs above the line from $A$ and from $B$ to meet at $Q$. Drawing line $PQ$ forms a perpendicular bisector, giving an angle of **$90^\\circ$** [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Construct perpendicular bisector through point P on the straight line (halving 180° into 90°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_construct_ninety_degree_angle",
        "hints": {
            "tier_1": "A straight angle is 180°. How do you halve 180° into 90°?",
            "tier_2": "Bisect a straight line segment around P.",
            "tier_3": "Construct a perpendicular bisector at point P."
        }
    }


def arch_33_construct_forty_five_degree_angle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What construction steps will produce an angle of **45°** using a compass and straightedge?"
    )
    sol = (
        f"**Step 1:** Construct a **$90^\\circ$ right angle** using the perpendicular construction [1 Mark].\n\n"
        f"**Step 2:** Construct the **angle bisector** of the $90^\\circ$ angle: "
        f"$$\\frac{{90^\\circ}}{{2}} = \\mathbf{{45^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Construct a 90° angle and bisect it to obtain 45°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_construct_forty_five_degree_angle",
        "hints": {
            "tier_1": "45° is half of 90°.",
            "tier_2": "Construct 90° and bisect it.",
            "tier_3": "Construct 90° right angle, then construct its angle bisector."
        }
    }


def arch_34_perpendicular_from_external_point(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"You are given a line segment $AB$ and a point $P$ lying above the line.\n\n"
        f"Describe the first step when constructing a line through $P$ perpendicular to $AB$."
    )
    sol = (
        f"**Step 1:** Place the sharp point of the compass on external point $P$ [1 Mark].\n\n"
        f"**Step 2:** Open the compass wide enough so that an arc cuts line $AB$ in **two distinct points** [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Place compass on point P and draw an arc cutting the line in two points",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_perpendicular_from_external_point",
        "hints": {
            "tier_1": "Put the compass point on P and draw an arc across the line.",
            "tier_2": "The arc must cut the line in two places.",
            "tier_3": "Place compass needle on P and swing an arc that intersects the line at two points."
        }
    }


# ==============================================================================
# CLUSTER 5: Triangle and Polygon Constructions (35 - 42)
# ==============================================================================

def arch_35_equilateral_triangle_construction(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 5, 6, 7])

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,140 160,140 100,36" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="100" y="155" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{s} cm</text>'
            f'<text x="60" y="85" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="end">{s} cm</text>'
            f'<text x="140" y="85" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="start">{s} cm</text>'
            f'</svg>'
        ),
        "caption": f"Equilateral triangle with side length s = {s} cm",
        "diagram_role": "context"
    }

    prompt = (
        f"You construct an equilateral triangle with side lengths of **{s} cm** using a compass and ruler.\n\n"
        f"1. What is the compass width setting used to draw the intersecting arcs?\n"
        f"2. What is the size of each interior angle in this constructed triangle?"
    )
    sol = (
        f"**Step 1:** The compass width must be set to the side length: **{s} cm** [1 Mark: Method].\n\n"
        f"**Step 2:** In an equilateral triangle, all three interior angles are equal: "
        f"$$\\frac{{180^\\circ}}{{3}} = \\mathbf{{60^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_geo_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. {s} cm; 2. 60°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "35_equilateral_triangle_construction",
        "hints": {
            "tier_1": f"All sides are {s} cm. All angles in an equilateral triangle are 60°.",
            "tier_2": f"Compass set to {s} cm; angles are 60°.",
            "tier_3": f"1. {s} cm; 2. 60°."
        }
    }


def arch_36_isosceles_triangle_construction(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([6, 8])
    legs = rng.choice([5, 7, 9])

    prompt = (
        f"Constructing an isosceles triangle $\\Delta ABC$ with base $BC = {base}\\text{{ cm}}$ and equal legs $AB = AC = {legs}\\text{{ cm}}$:\n\n"
        f"1. What length should be drawn on paper first with the ruler?\n"
        f"2. What width should the compass be set to when drawing arcs from $B$ and $C$ to find vertex $A$?"
    )
    sol = (
        f"**Step 1:** First draw the base segment **$BC = {base}\\text{{ cm}}$** with the ruler [1 Mark].\n\n"
        f"**Step 2:** Open the compass to the leg length **${legs}\\text{{ cm}}$** and swing intersecting arcs from $B$ and $C$ [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. Base BC = {base} cm; 2. Compass width = {legs} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_isosceles_triangle_construction",
        "hints": {
            "tier_1": f"Draw base {base} cm first, then set compass to {legs} cm.",
            "tier_2": f"Base {base} cm; compass {legs} cm.",
            "tier_3": f"1. Base {base} cm; 2. Compass width {legs} cm."
        }
    }


def arch_37_scalene_triangle_sss_construction(rng: random.Random) -> Dict[str, Any]:
    a, b, c = 4, 6, 7  # 4 + 6 > 7

    prompt = (
        f"To construct triangle $PQR$ with side lengths $PQ = 7\\text{{ cm}}$, $QR = 6\\text{{ cm}}$, and $PR = 4\\text{{ cm}}$:\n\n"
        f"If you draw $PQ = 7\\text{{ cm}}$ first as the base, state the compass settings needed from point $P$ and point $Q$ to locate vertex $R$."
    )
    sol = (
        f"**Step 1:** From point $P$, draw an arc with compass width set to $PR = \\mathbf{{4\\text{{ cm}}}}$ [1 Mark].\n\n"
        f"**Step 2:** From point $Q$, draw an arc with compass width set to $QR = \\mathbf{{6\\text{{ cm}}}}$ [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "From P: 4 cm; From Q: 6 cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_scalene_triangle_sss_construction",
        "hints": {
            "tier_1": "Vertex R is 4 cm from P and 6 cm from Q.",
            "tier_2": "Arc of radius 4 cm from P, arc of radius 6 cm from Q.",
            "tier_3": "From P: 4 cm; From Q: 6 cm."
        }
    }


def arch_38_triangle_inequality_theorem(rng: random.Random) -> Dict[str, Any]:
    can_construct = rng.choice([True, False])
    if can_construct:
        a, b, c = 5, 7, 10  # 5+7 = 12 > 10
        ans = "Yes, can be constructed (5 + 7 = 12 > 10)"
    else:
        a, b, c = 3, 4, 8   # 3+4 = 7 < 8
        ans = "No, cannot be constructed (3 + 4 = 7 < 8, arcs will not meet)"

    prompt = (
        f"A learner tries to construct a triangle with sticks of lengths **{a} cm**, **{b} cm**, and **{c} cm**.\n\n"
        f"Can this triangle be constructed? State the **Triangle Inequality Theorem** in your explanation."
    )
    sol = (
        f"**Step 1:** The Triangle Inequality Theorem states that the sum of the two shorter sides must be **strictly greater** than the longest side: $a + b > c$ [1 Mark: Method].\n\n"
        f"**Step 2:** Check: ${a} + {b} = {a+b}\\text{{ cm}}$ compared to ${c}\\text{{ cm}}$. {'Since 12 > 10, the triangle CAN be constructed.' if can_construct else 'Since 7 < 8, the arcs will never meet and the triangle CANNOT be constructed.'} [1 Mark: Accuracy]"
    )
    return {
        "id": f"g7_geo_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_triangle_inequality_theorem",
        "hints": {
            "tier_1": f"Add the two shorter sides ({a} + {b}) and compare to {c}.",
            "tier_2": f"{a} + {b} = {a+b}.",
            "tier_3": ans
        }
    }


def arch_39_construct_triangle_sas(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Describe the order of steps to construct a triangle given two side lengths and the included angle (SAS: Side-Angle-Side)."
    )
    sol = (
        f"**Step 1:** Use a ruler to draw the first side length [1 Mark].\n\n"
        f"**Step 2:** At one endpoint, use a protractor to construct the given included angle.\n\n"
        f"**Step 3:** Use a compass or ruler to mark off the second side length along the angled ray, then join the endpoints to complete the triangle [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Draw first side, construct angle at vertex, measure second side on ray, join endpoints",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_construct_triangle_sas",
        "hints": {
            "tier_1": "Draw side 1 -> draw angle -> measure side 2 -> connect ends.",
            "tier_2": "Side, then Angle, then Side.",
            "tier_3": "Draw first side, construct angle, mark second side, join endpoints."
        }
    }


def arch_40_construct_triangle_asa(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Describe how to construct a triangle given one side and the two angles at either end of that side (ASA: Angle-Side-Angle)."
    )
    sol = (
        f"**Step 1:** Draw the given base side length using a ruler [1 Mark].\n\n"
        f"**Step 2:** Use a protractor to construct the first angle at the left endpoint, and construct the second angle at the right endpoint. Extend both rays until they **intersect** at the third vertex [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Draw base side, construct angles at each endpoint, extend rays until they intersect",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_construct_triangle_asa",
        "hints": {
            "tier_1": "Draw the base line first, then build an angle at each end.",
            "tier_2": "The two rays cross to form the top vertex.",
            "tier_3": "Draw base side, construct angles at both ends, extend rays until they meet."
        }
    }


def arch_41_regular_hexagon_in_circle(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([3, 4, 5])

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<circle cx="100" cy="100" r="70" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
            f'<polygon points="170,100 135,160.6 65,160.6 30,100 65,39.4 135,39.4" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<circle cx="100" cy="100" r="3" fill="#ef4444"/>'
            f'<line x1="100" y1="100" x2="170" y2="100" stroke="#2563eb" stroke-width="2"/>'
            f'<text x="135" y="93" font-size="12" font-weight="bold" fill="#2563eb">r = {r} cm</text>'
            f'</svg>'
        ),
        "caption": f"Regular hexagon inscribed in a circle of radius r = {r} cm",
        "diagram_role": "context"
    }

    prompt = (
        f"A regular hexagon is constructed inside a circle of radius $r = {r}\\text{{ cm}}$ by stepping the compass around the circumference.\n\n"
        f"1. What is the length of each side of the inscribed regular hexagon?\n"
        f"2. How many steps of radius length fit exactly around the circle?"
    )
    sol = (
        f"**Step 1:** The side length of a regular hexagon inscribed in a circle is equal to the radius: **${r}\\text{{ cm}}$** [1 Mark: Method].\n\n"
        f"**Step 2:** Exactly **6 steps** fit around the circumference (forming 6 equilateral triangles meeting at the centre) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. {r} cm; 2. 6 steps",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "41_regular_hexagon_in_circle",
        "hints": {
            "tier_1": "The side of a hexagon inscribed in a circle equals the circle's radius.",
            "tier_2": f"Side = {r} cm; a hexagon has 6 sides.",
            "tier_3": f"1. {r} cm; 2. 6 steps."
        }
    }


def arch_42_seven_circle_flower_pattern(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the classic 'seven-circle pattern' (one central circle surrounded by six identical overlapping circles of the same radius $r$):\n\n"
        f"Where do the centres of the six surrounding circles lie?"
    )
    sol = (
        f"**Step 1:** The centres of the six surrounding circles lie directly on the **circumference of the central circle** [1 Mark: Method].\n\n"
        f"**Step 2:** Each surrounding circle passes through the centre of the central circle and intersects its neighbouring circles at radius intervals [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "On the circumference of the central circle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_seven_circle_flower_pattern",
        "hints": {
            "tier_1": "Where do you place the compass needle to draw the outer 6 circles?",
            "tier_2": "On the boundary (circumference) of the first circle.",
            "tier_3": "On the circumference of the central circle."
        }
    }


# ==============================================================================
# CLUSTER 6: Parallel Lines & Geometric Properties (43 - 50)
# ==============================================================================

def arch_43_parallel_lines_ruler_and_set_square(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain how a **ruler and a set square** are used together to draw a line parallel to a given line $AB$ through a point $P$."
    )
    sol = (
        f"**Step 1:** Align one edge of the set square along the given line $AB$ [1 Mark].\n\n"
        f"**Step 2:** Place the straightedge of the ruler firmly against another edge of the set square as a guide rail. Slide the set square along the ruler until its edge meets point $P$, then draw the parallel line [1 Mark: Method]."
    )
    return {
        "id": f"g7_geo_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Align set square on line AB, place ruler against it, slide set square to point P and draw line",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_parallel_lines_ruler_and_set_square",
        "hints": {
            "tier_1": "Align the set square on the line, lock the ruler against it, slide to P.",
            "tier_2": "The ruler acts as a guide rail while the set square slides.",
            "tier_3": "Align set square on AB, hold ruler against it, slide set square to point P and rule the line."
        }
    }


def arch_44_parallel_lines_compass_rhombus_method(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When using a compass to construct a line parallel to line $AB$ through point $P$ using the rhombus method:\n\n"
        f"Why must all four arcs be drawn with the **exact same compass width**?"
    )
    sol = (
        f"**Step 1:** In a rhombus, all four sides are of equal length [1 Mark].\n\n"
        f"**Step 2:** By keeping the compass width constant, the four points form a rhombus, and opposite sides of any rhombus are strictly **parallel** ($AB \\parallel PQ$) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "To form a rhombus where all 4 sides are equal, ensuring opposite sides are parallel",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_parallel_lines_compass_rhombus_method",
        "hints": {
            "tier_1": "What 4-sided geometric shape has all 4 sides equal and opposite sides parallel?",
            "tier_2": "A rhombus.",
            "tier_3": "To create a rhombus with 4 equal sides; opposite sides of a rhombus are parallel."
        }
    }


def arch_45_distance_between_parallel_lines(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6])

    prompt = (
        f"Line $L_1$ is parallel to line $L_2$.\n"
        f"At point $A$, the perpendicular distance between the lines is **{d} cm**.\n\n"
        f"What is the perpendicular distance between the two lines at a point $B$ located 20 cm further down?"
    )
    sol = (
        f"**Step 1:** By definition, parallel lines never meet and remain **equidistant** (the same perpendicular distance apart everywhere) [1 Mark: Method].\n\n"
        f"**Step 2:** The distance at point $B$ is identically **{d} cm** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{d} cm; parallel lines are equidistant everywhere",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_distance_between_parallel_lines",
        "hints": {
            "tier_1": "Does the perpendicular distance between parallel lines ever change?",
            "tier_2": f"It remains {d} cm everywhere.",
            "tier_3": f"{d} cm."
        }
    }


def arch_46_perpendicular_lines_right_angle_identification(rng: random.Random) -> Dict[str, Any]:
    l_pair = rng.choice([("L₁", "L₂"), ("P₁", "P₂"), ("M₁", "M₂"), ("K₁", "K₂")])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<line x1="20" y1="120" x2="180" y2="120" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="100" y1="20" x2="100" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
            f'<rect x="100" y="105" width="15" height="15" fill="none" stroke="#ef4444" stroke-width="2"/>'
            f'<text x="185" y="125" font-size="12" font-weight="bold" fill="#0f172a">{l_pair[0]}</text>'
            f'<text x="105" y="25" font-size="12" font-weight="bold" fill="#0f172a">{l_pair[1]}</text>'
            f'</svg>'
        ),
        "caption": f"Two lines {l_pair[0]} and {l_pair[1]} intersecting with a square right-angle symbol",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the geometric diagram showing lines ${l_pair[0]}$ and ${l_pair[1]}$.\n\n"
        f"1. What does the square symbol at the intersection indicate?\n"
        f"2. What is the mathematical term used to describe lines that meet at this angle?"
    )
    sol = (
        f"**Step 1:** The square symbol indicates a **right angle ($90^\\circ$)** [1 Mark: Method].\n\n"
        f"**Step 2:** Lines that meet at $90^\\circ$ are called **perpendicular lines** (${l_pair[0]} \\perp {l_pair[1]}$) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 90° right angle; 2. Perpendicular lines",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "46_perpendicular_lines_right_angle_identification",
        "hints": {
            "tier_1": "The square corner symbol means 90°. What word describes 90° lines?",
            "tier_2": "Perpendicular.",
            "tier_3": "1. 90° right angle; 2. Perpendicular."
        }
    }


def arch_47_tangent_perpendicular_to_radius(rng: random.Random) -> Dict[str, Any]:
    r_circ = rng.choice([45, 50, 55, 60])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<circle cx="100" cy="80" r="{r_circ}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="20" y1="{80 + r_circ}" x2="180" y2="{80 + r_circ}" stroke="#2563eb" stroke-width="2.5"/>'  # tangent
            f'<line x1="100" y1="80" x2="100" y2="{80 + r_circ}" stroke="#1e293b" stroke-width="2"/>'  # radius
            f'<circle cx="100" cy="80" r="3" fill="#0f172a"/>'
            f'<circle cx="100" cy="{80 + r_circ}" r="3.5" fill="#ef4444"/>'
            f'<rect x="100" y="{65 + r_circ}" width="12" height="15" fill="none" stroke="#ef4444" stroke-width="1.5"/>'
            f'<text x="90" y="80" font-size="11" font-weight="bold">O</text>'
            f'<text x="105" y="{95 + r_circ}" font-size="11" font-weight="bold" fill="#ef4444">T</text>'
            f'</svg>'
        ),
        "caption": "Tangent line touching circle at point T, perpendicular to radius OT",
        "diagram_role": "context"
    }

    prompt = (
        f"A straight line touches a circle at exactly one point $T$ (a tangent line).\n\n"
        f"What is the angle formed between this tangent line and the radius $OT$ drawn to the point of contact?"
    )
    sol = (
        f"**Step 1:** A tangent line to a circle is always **perpendicular** to the radius at the point of contact [1 Mark: Method].\n\n"
        f"**Step 2:** The angle is exactly **$90^\\circ$ (a right angle)** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "90° (perpendicular)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "47_tangent_perpendicular_to_radius",
        "hints": {
            "tier_1": "Radius meets tangent at a right angle.",
            "tier_2": "Angle is 90°.",
            "tier_3": "90° (right angle)."
        }
    }


def arch_48_true_false_geometric_constructions(rng: random.Random) -> Dict[str, Any]:
    statements = [
        ("The diameter of a circle is twice its radius.", "True", "d = 2r"),
        ("An angle bisector divides an angle into three equal parts.", "False", "It divides into two equal parts"),
        ("The arms of an angle must be of equal length for the angle to be measured.", "False", "Arm length does not affect angle size"),
        ("A perpendicular bisector cuts a line segment in half at 90°.", "True", "It bisects at a right angle")
    ]
    stmt, ans, reason = rng.choice(statements)

    prompt = (
        f"State whether the following statement is **True** or **False** and provide a brief reason:\n\n"
        f"\"{stmt}\""
    )
    sol = (
        f"**Step 1:** The statement is **{ans}** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Reason: {reason} [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_true_false_geometric_constructions",
        "hints": {
            "tier_1": "Consider the geometric definition carefully.",
            "tier_2": f"It is {ans}.",
            "tier_3": f"{ans} because {reason}."
        }
    }


def arch_49_flawed_construction_diagnosis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner tries to construct the perpendicular bisector of a 10 cm segment $AB$.\n"
        f"They set their compass to 4 cm and draw arcs from $A$ and $B$, but the arcs do not cross.\n\n"
        f"1. Explain what error the learner made.\n"
        f"2. What minimum compass setting should they use instead?"
    )
    sol = (
        f"**Step 1:** Error: The compass width of 4 cm is **less than half** of the segment length ($10 \\div 2 = 5\\text{{ cm}}$), so the arcs cannot reach each other to intersect [1 Mark: Method].\n\n"
        f"**Step 2:** The compass setting must be **strictly greater than 5 cm** (e.g. 6 cm, 7 cm, or 8 cm) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Compass was set to less than half (4 cm < 5 cm); 2. More than 5 cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_flawed_construction_diagnosis",
        "hints": {
            "tier_1": "Half of 10 cm is 5 cm. What happens if compass is only 4 cm?",
            "tier_2": "The compass must be opened to more than half (> 5 cm).",
            "tier_3": "1. 4 cm is less than half; 2. Must be greater than 5 cm."
        }
    }


def arch_50_compass_opening_for_intersections(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([8, 12, 14, 16])
    half = d // 2
    rec = half + 2

    prompt = (
        f"Two points $X$ and $Y$ are **{d} cm** apart on a page.\n\n"
        f"What is the smallest whole number compass opening (in cm) that guarantees arcs drawn from $X$ and $Y$ will cross each other above and below the line?"
    )
    sol = (
        f"**Step 1:** Arcs must reach beyond the midpoint of $XY$: $$\\text{{Midpoint distance}} = \\frac{{{d}}}{{2}} = {half}\\text{{ cm}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** The smallest whole number strictly greater than {half} cm is **{half + 1} cm** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_geo_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{half + 1} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_compass_opening_for_intersections",
        "hints": {
            "tier_1": f"Find half of {d} cm and add 1 cm.",
            "tier_2": f"{half} + 1 = {half + 1}.",
            "tier_3": f"{half + 1} cm."
        }
    }
