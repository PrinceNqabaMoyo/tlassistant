"""Grade 7 Mathematics - Geometry of Straight Lines: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of straight lines.md
"""
import random
import math
from typing import Dict, Any, List


def _svg_wrap(inner: str, width: int = 400, height: int = 240) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{inner}'
        f'</svg>'
    )


# 01. Line segment definition and endpoints
def arch_01_line_segment_definition_and_endpoints(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(["A", "P", "K", "X"])
    p2 = chr(ord(p1) + 1)
    length = rng.choice([6, 8, 10, 12, 15])
    svg = _svg_wrap(
        f'<line x1="60" y1="120" x2="340" y2="120" stroke="#1e293b" stroke-width="4"/>'
        f'<circle cx="60" cy="120" r="5" fill="#1e293b"/>'
        f'<circle cx="340" cy="120" r="5" fill="#1e293b"/>'
        f'<text x="55" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{p1}</text>'
        f'<text x="335" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{p2}</text>'
        f'<text x="180" y="150" font-family="sans-serif" font-size="14" fill="#475569">{length} cm</text>'
    )
    prompt = (
        f"Refer to the geometric figure {p1}{p2} shown with length {length} cm.\n\n"
        f"1. Give the exact geometric name of this straight path with two fixed endpoints.\n"
        f"2. Explain why this geometric object can be measured, whereas a full line cannot be measured."
    )
    sol = (
        f"**Step 1:** A straight path with two definite endpoints is called a **line segment**.\n\n"
        f"**Step 2:** A line segment has fixed boundaries (endpoints {p1} and {p2}), giving it a measurable length ({length} cm). "
        f"A line extends infinitely in both directions without endpoints, so its length cannot be measured."
    )
    ans = f"1. Line segment; 2. It has two definite endpoints and a fixed measurable length ({length} cm), unlike an infinite line."
    return {
        "id": f"g7_line_01_{rng.randint(100000, 999999)}",
        "subskill": "01_line_segment_definition_and_endpoints",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Identify Endpoints", "body": f"Notice the solid dots at point {p1} and point {p2}."},
                {"title": "Classification", "body": "Two definite endpoints define a line segment."},
                {"title": "Measurability", "body": f"The segment has a fixed span of {length} cm."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_01",
        "hints": {
            "tier_1": "Look at whether the path has arrows or solid dots at both ends.",
            "tier_2": "A line segment has 2 endpoints, a ray has 1, and a line has 0.",
            "tier_3": "It is a line segment because it starts at one point and ends at another."
        },
        "misconception_tags": ["confused_line_and_line_segment"]
    }


# 02. Ray definition and direction
def arch_02_ray_definition_and_direction(rng: random.Random) -> Dict[str, Any]:
    origin = rng.choice(["O", "P", "M", "A"])
    through = rng.choice(["T", "Q", "N", "B"])
    direction = rng.choice(["right", "left"])
    if direction == "right":
        svg = _svg_wrap(
            f'<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">'
            f'<path d="M0,0 L0,6 L9,3 z" fill="#1e293b"/></marker></defs>'
            f'<line x1="80" y1="120" x2="320" y2="120" stroke="#1e293b" stroke-width="4" marker-end="url(#arr)"/>'
            f'<circle cx="80" cy="120" r="5" fill="#1e293b"/>'
            f'<circle cx="260" cy="120" r="4" fill="#1e293b"/>'
            f'<text x="75" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{origin}</text>'
            f'<text x="255" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{through}</text>'
        )
    else:
        svg = _svg_wrap(
            f'<defs><marker id="arrl" markerWidth="10" markerHeight="10" refX="3" refY="3" orient="auto">'
            f'<path d="M9,0 L9,6 L0,3 z" fill="#1e293b"/></marker></defs>'
            f'<line x1="320" y1="120" x2="80" y2="120" stroke="#1e293b" stroke-width="4" marker-end="url(#arrl)"/>'
            f'<circle cx="320" cy="120" r="5" fill="#1e293b"/>'
            f'<circle cx="140" cy="120" r="4" fill="#1e293b"/>'
            f'<text x="315" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{origin}</text>'
            f'<text x="135" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{through}</text>'
        )
    prompt = (
        f"A straight path starts at fixed endpoint {origin} and passes through point {through}, continuing infinitely with an arrowhead.\n\n"
        f"1. Name this geometric figure.\n"
        f"2. Write the standard symbolic notation for this figure.\n"
        f"3. Can this figure be measured with a ruler? Give a reason."
    )
    sol = (
        f"**Step 1:** A path with one endpoint extending indefinitely in one direction is called a **ray**.\n\n"
        f"**Step 2:** Symbolically it is written as $\\text{{ray }}{origin}{through}$ or $\\vec{{{origin}{through}}}$.\n\n"
        f"**Step 3:** No, it cannot be measured because it extends infinitely in one direction."
    )
    ans = f"1. Ray; 2. Ray {origin}{through} (or \\vec{{{origin}{through}}}); 3. No, it extends infinitely in one direction."
    return {
        "id": f"g7_line_02_{rng.randint(100000, 999999)}",
        "subskill": "02_ray_definition_and_direction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check Endpoints", "body": f"One endpoint is fixed at {origin}, while the other end has an arrowhead."},
                {"title": "Definition of Ray", "body": "A straight path with one endpoint is a ray."},
                {"title": "Notation", "body": f"We write ray {origin}{through} starting from the origin point."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_02",
        "hints": {
            "tier_1": "Think of a sun ray: it has a beginning point and shines outward infinitely.",
            "tier_2": "One endpoint + one infinite direction = ray.",
            "tier_3": "Write Ray followed by origin and passing point."
        },
        "misconception_tags": ["confused_ray_and_line"]
    }


# 03. Line infinite extent properties
def arch_03_line_infinite_extent_properties(rng: random.Random) -> Dict[str, Any]:
    l1 = rng.choice(["C", "L", "R", "S"])
    l2 = chr(ord(l1) + 1)
    svg = _svg_wrap(
        f'<defs>'
        f'<marker id="ah1" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto"><path d="M8,0 L0,4 L8,8 z" fill="#1e293b"/></marker>'
        f'<marker id="ah2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1e293b"/></marker>'
        f'</defs>'
        f'<line x1="50" y1="120" x2="350" y2="120" stroke="#1e293b" stroke-width="4" marker-start="url(#ah1)" marker-end="url(#ah2)"/>'
        f'<circle cx="120" cy="120" r="4" fill="#1e293b"/>'
        f'<circle cx="280" cy="120" r="4" fill="#1e293b"/>'
        f'<text x="115" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{l1}</text>'
        f'<text x="275" y="100" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">{l2}</text>'
    )
    prompt = (
        f"Consider line {l1}{l2} with arrowheads shown on both ends.\n\n"
        f"1. What do the arrowheads at both ends indicate?\n"
        f"2. Can the entire line {l1}{l2} ever be completely drawn on paper? Explain."
    )
    sol = (
        f"**Step 1:** The arrowheads indicate that the line extends **indefinitely (infinitely) in both directions**.\n\n"
        f"**Step 2:** No, an entire line cannot be drawn completely because it has infinite length; we only draw a representation."
    )
    ans = f"1. The line extends infinitely in both directions; 2. No, because it has infinite length and no endpoints."
    return {
        "id": f"g7_line_03_{rng.randint(100000, 999999)}",
        "subskill": "03_line_infinite_extent_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Observe Arrowheads", "body": "Both ends have arrowheads showing extension without bound."},
                {"title": "Infinite Extent", "body": "A geometric line has zero thickness and infinite length."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_03",
        "hints": {
            "tier_1": "Arrowheads mean the line keeps going.",
            "tier_2": "Can anything that is infinite fit entirely onto a piece of paper?",
            "tier_3": "Arrowheads represent infinite length in both directions."
        },
        "misconception_tags": ["finite_line_misconception"]
    }


# 04. Identify line, ray, segment from diagram
def arch_04_identify_line_ray_segment_from_diagram(rng: random.Random) -> Dict[str, Any]:
    end_x = rng.choice([150, 160, 170, 180])
    svg = _svg_wrap(
        f'<defs>'
        f'<marker id="ar_r" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1e293b"/></marker>'
        f'<marker id="ar_l" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto"><path d="M8,0 L0,4 L8,8 z" fill="#1e293b"/></marker>'
        f'</defs>'
        # Segment AB
        f'<line x1="40" y1="50" x2="{end_x}" y2="50" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="40" cy="50" r="4" fill="#1e293b"/><circle cx="{end_x}" cy="50" r="4" fill="#1e293b"/>'
        f'<text x="95" y="40" font-family="sans-serif" font-size="13" font-weight="bold">Figure 1</text>'
        # Ray CD
        f'<line x1="40" y1="120" x2="{end_x}" y2="120" stroke="#1e293b" stroke-width="3" marker-end="url(#ar_r)"/>'
        f'<circle cx="40" cy="120" r="4" fill="#1e293b"/>'
        f'<text x="95" y="110" font-family="sans-serif" font-size="13" font-weight="bold">Figure 2</text>'
        # Line EF
        f'<line x1="40" y1="190" x2="{end_x}" y2="190" stroke="#1e293b" stroke-width="3" marker-start="url(#ar_l)" marker-end="url(#ar_r)"/>'
        f'<text x="95" y="180" font-family="sans-serif" font-size="13" font-weight="bold">Figure 3</text>'
        , width=300, height=220
    )
    prompt = (
        "Classify Figures 1, 2, and 3 shown in the diagram as a line segment, ray, or line.\n\n"
        "Figure 1: __________\n"
        "Figure 2: __________\n"
        "Figure 3: __________"
    )
    sol = (
        "**Figure 1:** Has two endpoints with no arrows $\\rightarrow$ **Line segment**.\n"
        "**Figure 2:** Has one endpoint and an arrow at the other end $\\rightarrow$ **Ray**.\n"
        "**Figure 3:** Has arrows at both ends $\\rightarrow$ **Line**."
    )
    ans = "Figure 1: Line segment; Figure 2: Ray; Figure 3: Line"
    return {
        "id": f"g7_line_04_{rng.randint(100000, 999999)}",
        "subskill": "04_identify_line_ray_segment_from_diagram",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check End Conditions", "body": "Count endpoints and arrowheads for each figure."},
                {"title": "Figure 1", "body": "Two endpoints = line segment."},
                {"title": "Figure 2", "body": "One endpoint + one arrow = ray."},
                {"title": "Figure 3", "body": "Two arrows = line."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_04",
        "hints": {
            "tier_1": "Look at the arrows vs dots at the ends.",
            "tier_2": "0 arrows = segment, 1 arrow = ray, 2 arrows = line.",
            "tier_3": "Figure 1 is a line segment, Figure 2 is a ray, Figure 3 is a line."
        },
        "misconception_tags": ["confused_endpoints_arrows"]
    }


# 05. Symbolic notation matching
def arch_05_symbolic_notation_matching(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Match each geometric term with its correct symbolic representation:\n\n"
        "1. Line segment between points P and Q\n"
        "2. Ray starting at P and passing through Q\n"
        "3. Straight line passing through points P and Q\n\n"
        "Choose from:\n"
        "A) $\\overleftrightarrow{PQ}$ (or line $PQ$)\n"
        "B) $PQ$ (or segment $PQ$)\n"
        "C) $\\vec{PQ}$ (or ray $PQ$)"
    )
    sol = (
        "**1.** Line segment between P and Q $\\rightarrow$ **B) $PQ$** (no arrows on top).\n"
        "**2.** Ray starting at P through Q $\\rightarrow$ **C) $\\vec{PQ}$** (one arrow pointing right).\n"
        "**3.** Straight line through P and Q $\\rightarrow$ **A) $\\overleftrightarrow{PQ}$** (double-headed arrow)."
    )
    ans = "1 - B, 2 - C, 3 - A"
    return {
        "id": f"g7_line_05_{rng.randint(100000, 999999)}",
        "subskill": "05_symbolic_notation_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_05",
        "hints": {
            "tier_1": "The top bar symbol mirrors what the actual figure looks like.",
            "tier_2": "A line has arrows on both ends of the bar, a ray has an arrow on one end.",
            "tier_3": "1 matches B, 2 matches C, 3 matches A."
        },
        "misconception_tags": ["incorrect_geometric_notation"]
    }


# 06. Parallel lines concept and distance
def arch_06_parallel_lines_concept_and_distance(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([3, 4, 5, 6])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="150" x2="350" y2="150" stroke="#1e293b" stroke-width="3"/>'
        # Perpendicular distance markers
        f'<line x1="120" y1="70" x2="120" y2="150" stroke="#dc2626" stroke-dasharray="4,4" stroke-width="2"/>'
        f'<line x1="280" y1="70" x2="280" y2="150" stroke="#dc2626" stroke-dasharray="4,4" stroke-width="2"/>'
        f'<rect x="120" y="70" width="10" height="10" fill="none" stroke="#dc2626"/>'
        f'<rect x="280" y="70" width="10" height="10" fill="none" stroke="#dc2626"/>'
        f'<text x="130" y="115" font-family="sans-serif" font-size="13" fill="#dc2626">{dist} cm</text>'
        f'<text x="290" y="115" font-family="sans-serif" font-size="13" fill="#dc2626">{dist} cm</text>'
        f'<text x="360" y="75" font-family="sans-serif" font-size="14" font-weight="bold">Line 1</text>'
        f'<text x="360" y="155" font-family="sans-serif" font-size="14" font-weight="bold">Line 2</text>'
    )
    prompt = (
        f"Two straight lines are drawn such that the perpendicular distance between them is measured as {dist} cm at point A and {dist} cm at point B.\n\n"
        f"1. What is the special mathematical term for lines that maintain a constant distance apart?\n"
        f"2. Will these two lines ever intersect if extended infinitely? State why."
    )
    sol = (
        f"**Step 1:** Lines that are always the same distance apart are called **parallel lines**.\n\n"
        f"**Step 2:** No, they will never intersect because the distance between them remains constant ({dist} cm) everywhere."
    )
    ans = f"1. Parallel lines; 2. No, they will never intersect because the perpendicular distance remains constant ({dist} cm)."
    return {
        "id": f"g7_line_06_{rng.randint(100000, 999999)}",
        "subskill": "06_parallel_lines_concept_and_distance",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Measure Distance", "body": f"The distance between the lines is {dist} cm at every point."},
                {"title": "Parallel Definition", "body": "Constant distance between straight lines means they are parallel."},
                {"title": "Intersection", "body": "Parallel lines never meet."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_06",
        "hints": {
            "tier_1": "Think of railway tracks.",
            "tier_2": "Constant perpendicular distance means parallel.",
            "tier_3": "They are parallel and will never intersect."
        },
        "misconception_tags": ["parallel_lines_intersection_belief"]
    }


# 07. Parallel lines arrow symbol notation
def arch_07_parallel_lines_arrow_symbol_notation(rng: random.Random) -> Dict[str, Any]:
    l1 = rng.choice(["AB", "PQ", "KL"])
    l2 = rng.choice(["CD", "RS", "MN"])
    svg = _svg_wrap(
        f'<line x1="40" y1="80" x2="340" y2="80" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="40" y1="160" x2="340" y2="160" stroke="#1e293b" stroke-width="3"/>'
        # Parallel marker arrows along the line
        f'<path d="M180,74 L190,80 L180,86" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M180,154 L190,160 L180,166" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<text x="20" y="85" font-family="sans-serif" font-size="14" font-weight="bold">{l1[0]}</text>'
        f'<text x="350" y="85" font-family="sans-serif" font-size="14" font-weight="bold">{l1[1]}</text>'
        f'<text x="20" y="165" font-family="sans-serif" font-size="14" font-weight="bold">{l2[0]}</text>'
        f'<text x="350" y="165" font-family="sans-serif" font-size="14" font-weight="bold">{l2[1]}</text>'
    )
    prompt = (
        f"In geometric diagrams, arrows are marked directly along the length of lines {l1} and {l2}.\n\n"
        f"1. What do matching arrows on two lines signify?\n"
        f"2. Write the statement '{l1} is parallel to {l2}' using the mathematical symbol for parallel lines."
    )
    sol = (
        f"**Step 1:** Matching arrows along the lines indicate that the two lines are **parallel**.\n\n"
        f"**Step 2:** The mathematical symbol for parallel is $//$. Therefore, we write: ${l1} // {l2}$."
    )
    ans = f"1. The lines are parallel; 2. {l1} // {l2}"
    return {
        "id": f"g7_line_07_{rng.randint(100000, 999999)}",
        "subskill": "07_parallel_lines_arrow_symbol_notation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Identify Arrow Marks", "body": "Notice the small chevrons (arrows) along the middle of both lines."},
                {"title": "Meaning", "body": "Matching chevrons mean parallel."},
                {"title": "Symbol", "body": f"Use the // symbol: {l1} // {l2}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_07",
        "hints": {
            "tier_1": "Chevrons on lines do not show direction, they show parallel status.",
            "tier_2": "The symbol for parallel looks like two vertical slashes //.",
            "tier_3": f"Matching arrows mean parallel. Write {l1} // {l2}."
        },
        "misconception_tags": ["confused_chevron_with_direction"]
    }


# 08. Perpendicular lines right angle concept
def arch_08_perpendicular_lines_right_angle_concept(rng: random.Random) -> Dict[str, Any]:
    vx = rng.choice([180, 195, 205, 220])
    svg = _svg_wrap(
        f'<line x1="60" y1="140" x2="340" y2="140" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="{vx}" y1="20" x2="{vx}" y2="220" stroke="#1e293b" stroke-width="3"/>'
        f'<rect x="{vx}" y="125" width="15" height="15" fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="{vx+10}" y="115" font-family="sans-serif" font-size="12" fill="#2563eb">?</text>'
        f'<text x="350" y="145" font-family="sans-serif" font-size="14" font-weight="bold">AB</text>'
        f'<text x="{vx-10}" y="15" font-family="sans-serif" font-size="14" font-weight="bold">CD</text>'
    )
    prompt = (
        "Two lines AB and CD intersect such that a square marker is placed at the intersection point.\n\n"
        "1. What exact angle size does the square symbol represent?\n"
        "2. What is the mathematical term for two lines that meet at this angle?\n"
        "3. How many right angles are formed at this intersection?"
    )
    sol = (
        "**Step 1:** The square symbol represents a **right angle**, which is exactly $90^\\circ$.\n\n"
        "**Step 2:** Lines that meet at $90^\\circ$ are called **perpendicular lines**.\n\n"
        "**Step 3:** Exactly **4** right angles are formed around the intersection."
    )
    ans = "1. 90°; 2. Perpendicular lines; 3. 4 right angles"
    return {
        "id": f"g7_line_08_{rng.randint(100000, 999999)}",
        "subskill": "08_perpendicular_lines_right_angle_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Square Symbol", "body": "A small square at a vertex always indicates a 90° right angle."},
                {"title": "Term", "body": "Two lines meeting at 90° are perpendicular."},
                {"title": "All 4 Quadrants", "body": "All 4 angles at the intersection equal 90°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_08",
        "hints": {
            "tier_1": "The square is the universal symbol for a right angle.",
            "tier_2": "A right angle is 90 degrees; lines at 90 degrees are perpendicular.",
            "tier_3": "1. 90°, 2. Perpendicular lines, 3. 4 right angles."
        },
        "misconception_tags": ["perpendicular_definition_error"]
    }


# 09. Perpendicular symbol and identifying 90 deg
def arch_09_perpendicular_symbol_and_identifying_90_deg(rng: random.Random) -> Dict[str, Any]:
    name1 = rng.choice(["MN", "XY", "PQ"])
    name2 = rng.choice(["RS", "ZT", "KL"])
    prompt = (
        f"Line {name1} intersects line {name2} at an angle of 90°.\n\n"
        f"1. Which mathematical symbol is used to denote perpendicular lines?\n"
        f"2. Write the relationship between {name1} and {name2} using this symbol."
    )
    sol = (
        f"**Step 1:** The mathematical symbol for perpendicular is $\\perp$.\n\n"
        f"**Step 2:** We write: ${name1} \\perp {name2}$."
    )
    ans = f"1. ⊥; 2. {name1} ⊥ {name2}"
    return {
        "id": f"g7_line_09_{rng.randint(100000, 999999)}",
        "subskill": "09_perpendicular_symbol_and_identifying_90_deg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_09",
        "hints": {
            "tier_1": "The perpendicular symbol looks like an upside-down letter T.",
            "tier_2": "Symbol is ⊥.",
            "tier_3": f"Write {name1} ⊥ {name2}."
        },
        "misconception_tags": ["confused_parallel_and_perpendicular_symbols"]
    }


# 10. Intersecting lines point of intersection
def arch_10_intersecting_lines_point_of_intersection(rng: random.Random) -> Dict[str, Any]:
    inter_pt = rng.choice(["O", "E", "P", "M"])
    svg = _svg_wrap(
        f'<line x1="50" y1="50" x2="350" y2="190" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="190" x2="350" y2="50" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="200" cy="120" r="5" fill="#dc2626"/>'
        f'<text x="210" y="115" font-family="sans-serif" font-size="16" font-weight="bold" fill="#dc2626">{inter_pt}</text>'
        f'<text x="35" y="45" font-family="sans-serif" font-size="14" font-weight="bold">A</text>'
        f'<text x="360" y="200" font-family="sans-serif" font-size="14" font-weight="bold">B</text>'
        f'<text x="35" y="200" font-family="sans-serif" font-size="14" font-weight="bold">C</text>'
        f'<text x="360" y="45" font-family="sans-serif" font-size="14" font-weight="bold">D</text>'
    )
    prompt = (
        f"Lines AB and CD cross each other at point {inter_pt}.\n\n"
        f"1. What is the special term for point {inter_pt} where two lines cross?\n"
        f"2. How many points in total can two distinct straight lines share if they are not parallel and not identical?"
    )
    sol = (
        f"**Step 1:** The point where two lines cross is called the **point of intersection**.\n\n"
        f"**Step 2:** Two distinct straight lines can intersect at **exactly one point**."
    )
    ans = f"1. Point of intersection; 2. Exactly one point"
    return {
        "id": f"g7_line_10_{rng.randint(100000, 999999)}",
        "subskill": "10_intersecting_lines_point_of_intersection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Meeting Point", "body": f"Point {inter_pt} lies on both line AB and line CD."},
                {"title": "Terminology", "body": "The meeting point is called the point of intersection."},
                {"title": "Uniqueness", "body": "Two straight lines intersect at at most one single point."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_10",
        "hints": {
            "tier_1": "Intersection is when paths cross.",
            "tier_2": "Can straight lines curve back to cross again?",
            "tier_3": "They cross at the point of intersection, exactly 1 point."
        },
        "misconception_tags": ["multiple_intersections_straight_lines"]
    }


# 11. Adjacent angles on a straight line numeric
def arch_11_adjacent_angles_on_straight_line_numeric(rng: random.Random) -> Dict[str, Any]:
    angle_given = rng.choice([35, 45, 55, 65, 75, 115, 125, 135])
    unknown = 180 - angle_given
    svg = _svg_wrap(
        f'<line x1="40" y1="180" x2="360" y2="180" stroke="#1e293b" stroke-width="4"/>'
        f'<line x1="200" y1="180" x2="280" y2="60" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="200" cy="180" r="4" fill="#1e293b"/>'
        f'<text x="210" y="200" font-family="sans-serif" font-size="14" font-weight="bold">O</text>'
        f'<text x="30" y="195" font-family="sans-serif" font-size="14" font-weight="bold">A</text>'
        f'<text x="370" y="195" font-family="sans-serif" font-size="14" font-weight="bold">B</text>'
        f'<text x="290" y="55" font-family="sans-serif" font-size="14" font-weight="bold">C</text>'
        f'<text x="130" y="165" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle_given}°</text>'
        f'<text x="250" y="165" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the diagram, AOB is a straight line. Ray OC divides the straight angle into two adjacent angles: "
        f"$\\angle AOC = {angle_given}^\\circ$ and $\\angle BOC = x$.\n\n"
        f"Calculate the value of $x$, providing the standard geometric reason."
    )
    sol = (
        f"**Step 1:** State the geometric theorem:\n"
        f"Adjacent angles on a straight line add up to $180^\\circ$ [$\\angle\\text{{s on a straight line}}$].\n\n"
        f"**Step 2:** Formulate and solve the equation:\n"
        f"$$x + {angle_given}^\\circ = 180^\\circ$$\n"
        f"$$x = 180^\\circ - {angle_given}^\\circ = {unknown}^\\circ$$\n\n"
        f"**Conclusion:** $x = {unknown}^\\circ$ [$\\angle\\text{{s on a straight line}}$]."
    )
    ans = f"x = {unknown}° [∠s on straight line]"
    return {
        "id": f"g7_line_11_{rng.randint(100000, 999999)}",
        "subskill": "11_adjacent_angles_on_straight_line_numeric",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Identify Straight Angle", "body": "AOB is a straight line, which measures 180°."},
                {"title": "Set up Equation", "body": f"x + {angle_given}° = 180° [∠s on a straight line]."},
                {"title": "Calculate x", "body": f"x = 180° - {angle_given}° = {unknown}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_11",
        "hints": {
            "tier_1": "What is the total angle of a straight line?",
            "tier_2": "Subtract the given angle from 180°.",
            "tier_3": f"x = 180 - {angle_given} = {unknown}°."
        },
        "misconception_tags": ["added_to_90_instead_of_180"]
    }


# 12. Adjacent angles on straight line algebraic
def arch_12_adjacent_angles_on_straight_line_algebraic(rng: random.Random) -> Dict[str, Any]:
    # 2x + 4x = 180 -> 6x = 180 -> x = 30
    # or 3x + 2x = 180 -> 5x = 180 -> x = 36
    # or x + 3x = 180 -> 4x = 180 -> x = 45
    coeff_pairs = [(1, 3), (2, 3), (2, 4), (1, 5)]
    c1, c2 = rng.choice(coeff_pairs)
    total_coeff = c1 + c2
    x_val = 180 // total_coeff
    ang1 = c1 * x_val
    ang2 = c2 * x_val
    svg = _svg_wrap(
        f'<line x1="40" y1="180" x2="360" y2="180" stroke="#1e293b" stroke-width="4"/>'
        f'<line x1="200" y1="180" x2="260" y2="60" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="200" y="200" font-family="sans-serif" font-size="14" font-weight="bold">O</text>'
        f'<text x="30" y="195" font-family="sans-serif" font-size="14" font-weight="bold">P</text>'
        f'<text x="370" y="195" font-family="sans-serif" font-size="14" font-weight="bold">Q</text>'
        f'<text x="270" y="55" font-family="sans-serif" font-size="14" font-weight="bold">R</text>'
        f'<text x="120" y="165" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{c1}x</text>'
        f'<text x="250" y="165" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">{c2}x</text>'
    )
    prompt = (
        f"In the diagram, POQ is a straight line. The two adjacent angles are ${c1}x$ and ${c2}x$.\n\n"
        f"1. Solve for $x$.\n"
        f"2. Hence, calculate the size of each angle."
    )
    sol = (
        f"**Step 1:** State the geometric reason:\n"
        f"Adjacent angles on a straight line add up to $180^\\circ$ [$\\angle\\text{{s on a straight line}}$].\n\n"
        f"**Step 2:** Solve for $x$:\n"
        f"$${c1}x + {c2}x = 180^\\circ$$\n"
        f"$${total_coeff}x = 180^\\circ$$\n"
        f"$$x = \\frac{{180^\\circ}}{{{total_coeff}}} = {x_val}^\\circ$$\n\n"
        f"**Step 3:** Calculate each angle:\n"
        f"Angle 1: ${c1}({x_val}^\\circ) = {ang1}^\\circ$\n"
        f"Angle 2: ${c2}({x_val}^\\circ) = {ang2}^\\circ$"
    )
    ans = f"1. x = {x_val}°; 2. {ang1}° and {ang2}°"
    return {
        "id": f"g7_line_12_{rng.randint(100000, 999999)}",
        "subskill": "12_adjacent_angles_on_straight_line_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Sum of Angles", "body": f"{c1}x + {c2}x = 180° [adj ∠s on straight line]."},
                {"title": "Combine Like Terms", "body": f"{total_coeff}x = 180°."},
                {"title": "Solve x", "body": f"x = {x_val}°."},
                {"title": "Substitute", "body": f"The angles are {ang1}° and {ang2}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_12",
        "hints": {
            "tier_1": f"Combine the terms: {c1}x + {c2}x = {total_coeff}x.",
            "tier_2": f"Set {total_coeff}x = 180° and divide by {total_coeff}.",
            "tier_3": f"x = {x_val}°. Substitute to find {ang1}° and {ang2}°."
        },
        "misconception_tags": ["algebraic_linear_pair_error"]
    }


# 13. Adjacent three angles on a straight line
def arch_13_adjacent_three_angles_on_straight_line(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([30, 40, 50])
    a2 = rng.choice([60, 70, 80])
    a3 = 180 - (a1 + a2)
    svg = _svg_wrap(
        f'<line x1="40" y1="180" x2="360" y2="180" stroke="#1e293b" stroke-width="4"/>'
        f'<line x1="200" y1="180" x2="130" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="180" x2="270" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="200" y="200" font-family="sans-serif" font-size="14" font-weight="bold">O</text>'
        f'<text x="80" y="165" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{a1}°</text>'
        f'<text x="190" y="130" font-family="sans-serif" font-size="13" font-weight="bold" fill="#059669">{a2}°</text>'
        f'<text x="290" y="165" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">y</text>'
    )
    prompt = (
        f"Three angles lie on a straight line at vertex O. Two of the angles are {a1}° and {a2}°.\n\n"
        f"Calculate the value of the third angle $y$, giving a reason for your answer."
    )
    sol = (
        f"**Step 1:** The sum of angles on a straight line is $180^\\circ$ [$\\angle\\text{{s on a straight line}}$].\n\n"
        f"**Step 2:** Set up the equation:\n"
        f"$${a1}^\\circ + {a2}^\\circ + y = 180^\\circ$$\n"
        f"$${a1 + a2}^\\circ + y = 180^\\circ$$\n"
        f"$$y = 180^\\circ - {a1 + a2}^\\circ = {a3}^\\circ$$\n\n"
        f"**Conclusion:** $y = {a3}^\\circ$ [$\\angle\\text{{s on a straight line}}$]."
    )
    ans = f"y = {a3}° [∠s on straight line]"
    return {
        "id": f"g7_line_13_{rng.randint(100000, 999999)}",
        "subskill": "13_adjacent_three_angles_on_straight_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Angle Sum", "body": f"{a1}° + {a2}° + y = 180° [∠s on straight line]."},
                {"title": "Sum Knowns", "body": f"{a1}° + {a2}° = {a1 + a2}°."},
                {"title": "Solve for y", "body": f"y = 180° - {a1 + a2}° = {a3}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_13",
        "hints": {
            "tier_1": "Add the two known angles together first.",
            "tier_2": f"Subtract {a1 + a2}° from 180°.",
            "tier_3": f"y = 180 - {a1 + a2} = {a3}°."
        },
        "misconception_tags": ["arithmetic_subtraction_straight_line"]
    }


# 14. Perpendicular line adjacent complement
def arch_14_perpendicular_line_adjacent_complement(rng: random.Random) -> Dict[str, Any]:
    angle_given = rng.choice([25, 32, 48, 55, 63])
    comp = 90 - angle_given
    svg = _svg_wrap(
        f'<line x1="60" y1="180" x2="340" y2="180" stroke="#1e293b" stroke-width="4"/>'
        f'<line x1="200" y1="180" x2="200" y2="40" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="180" x2="290" y2="90" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="200" y="165" width="15" height="15" fill="none" stroke="#1e293b"/>'
        f'<text x="200" y="200" font-family="sans-serif" font-size="14" font-weight="bold">O</text>'
        f'<text x="210" y="130" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{angle_given}°</text>'
        f'<text x="250" y="165" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the figure, a perpendicular ray divides a right angle into two parts: {angle_given}° and $x$.\n\n"
        f"Calculate the value of $x$, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** The two angles together form a right angle ($90^\\circ$) [complementary $\\angle\\text{{s}}$].\n\n"
        f"**Step 2:** Solve for $x$:\n"
        f"$$x + {angle_given}^\\circ = 90^\\circ$$\n"
        f"$$x = 90^\\circ - {angle_given}^\\circ = {comp}^\\circ$$\n\n"
        f"**Conclusion:** $x = {comp}^\\circ$ [comp $\\angle\\text{{s}}$ or $\\angle\\text{{s in a right angle}}$]."
    )
    ans = f"x = {comp}° [complementary ∠s]"
    return {
        "id": f"g7_line_14_{rng.randint(100000, 999999)}",
        "subskill": "14_perpendicular_line_adjacent_complement",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Right Angle", "body": "The two angles form a 90° angle."},
                {"title": "Equation", "body": f"x + {angle_given}° = 90°."},
                {"title": "Subtract", "body": f"x = 90° - {angle_given}° = {comp}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_14",
        "hints": {
            "tier_1": "Notice the right-angle marker (square corner).",
            "tier_2": "Complementary angles add to 90°.",
            "tier_3": f"x = 90 - {angle_given} = {comp}°."
        },
        "misconception_tags": ["subtracted_from_180_instead_of_90"]
    }


# 15. Complementary angles concept and calc
def arch_15_complementary_angles_concept_and_calc(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([15, 27, 34, 45, 62, 73])
    comp = 90 - angle
    prompt = (
        f"1. What is the sum of two complementary angles in degrees?\n"
        f"2. Calculate the complement of an angle measuring {angle}°."
    )
    sol = (
        f"**Step 1:** Complementary angles add up to **$90^\\circ$**.\n\n"
        f"**Step 2:** The complement of {angle}° is:\n"
        f"$$90^\\circ - {angle}^\\circ = {comp}^\\circ$$"
    )
    ans = f"1. 90°; 2. {comp}°"
    return {
        "id": f"g7_line_15_{rng.randint(100000, 999999)}",
        "subskill": "15_complementary_angles_concept_and_calc",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_15",
        "hints": {
            "tier_1": "Complementary adds to 90°, Supplementary adds to 180°.",
            "tier_2": f"Subtract {angle} from 90.",
            "tier_3": f"1. 90°, 2. {comp}°."
        },
        "misconception_tags": ["confused_complementary_supplementary"]
    }


# 16. Vertically opposite angles identification
def arch_16_vertically_opposite_angles_identification(rng: random.Random) -> Dict[str, Any]:
    y_off = rng.choice([45, 50, 55, 60])
    svg = _svg_wrap(
        f'<line x1="50" y1="{y_off}" x2="350" y2="{240 - y_off}" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="{240 - y_off}" x2="350" y2="{y_off}" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="200" y="75" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠1</text>'
        f'<text x="270" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#059669">∠2</text>'
        f'<text x="200" y="175" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠3</text>'
        f'<text x="130" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#059669">∠4</text>'
    )
    prompt = (
        "Two straight lines intersect, forming angles ∠1, ∠2, ∠3, and ∠4 as shown.\n\n"
        "1. Identify the pairs of vertically opposite angles.\n"
        "2. State the geometric theorem regarding the sizes of vertically opposite angles."
    )
    sol = (
        "**Step 1:** The angles across from each other at the intersection are vertically opposite:\n"
        "- **∠1 and ∠3** are vertically opposite.\n"
        "- **∠2 and ∠4** are vertically opposite.\n\n"
        "**Step 2:** Vertically opposite angles are **equal** [$\\text{{vert opp }}\\angle\\text{{s are equal}}$]."
    )
    ans = "1. (∠1 and ∠3) and (∠2 and ∠4); 2. Vertically opposite angles are equal."
    return {
        "id": f"g7_line_16_{rng.randint(100000, 999999)}",
        "subskill": "16_vertically_opposite_angles_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Opposite Angles", "body": "Look directly across the intersection vertex."},
                {"title": "Pairs", "body": "∠1 is opposite ∠3; ∠2 is opposite ∠4."},
                {"title": "Theorem", "body": "Vertically opposite angles are always equal."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_16",
        "hints": {
            "tier_1": "Vertically opposite means directly across the vertex like scissors.",
            "tier_2": "Opposite angles share only the vertex point.",
            "tier_3": "∠1 & ∠3 are opposite, ∠2 & ∠4 are opposite; they are equal."
        },
        "misconception_tags": ["confused_adjacent_with_opposite"]
    }


# 17. Vertically opposite angles numeric solve
def arch_17_vertically_opposite_angles_numeric_solve(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([38, 47, 56, 68, 74, 82, 112, 125, 138])
    svg = _svg_wrap(
        f'<line x1="50" y1="50" x2="350" y2="190" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="190" x2="350" y2="50" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="200" y="75" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle}°</text>'
        f'<text x="200" y="175" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the diagram of intersecting straight lines, the top angle is {angle}° and the bottom angle is $x$.\n\n"
        f"Determine the value of $x$, giving the correct geometric reason."
    )
    sol = (
        f"**Step 1:** Identify the geometric relationship:\n"
        f"The two angles are vertically opposite each other [$\\text{{vert opp }}\\angle\\text{{s}}$].\n\n"
        f"**Step 2:** Apply the theorem:\n"
        f"$$x = {angle}^\\circ \\text{{ [vert opp }}\\angle\\text{{s]}}$$"
    )
    ans = f"x = {angle}° [vert opp ∠s]"
    return {
        "id": f"g7_line_17_{rng.randint(100000, 999999)}",
        "subskill": "17_vertically_opposite_angles_numeric_solve",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Angle Position", "body": "The two angles are across from each other at the intersection."},
                {"title": "Equality", "body": f"Vertically opposite angles are equal: x = {angle}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_17",
        "hints": {
            "tier_1": "Are the angles adjacent or directly across?",
            "tier_2": "Vertically opposite angles are equal.",
            "tier_3": f"x = {angle}° [vert opp ∠s]."
        },
        "misconception_tags": ["subtracted_from_180_for_vert_opp"]
    }


# 18. Vertically opposite angles algebraic solve
def arch_18_vertically_opposite_angles_algebraic_solve(rng: random.Random) -> Dict[str, Any]:
    # 2x + 10 = 70 -> 2x = 60 -> x = 30
    x_val = rng.choice([15, 20, 25, 30, 35])
    a = rng.choice([2, 3, 4])
    b = rng.choice([10, 15, 20])
    total_deg = a * x_val + b
    svg = _svg_wrap(
        f'<line x1="50" y1="50" x2="350" y2="190" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="190" x2="350" y2="50" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="180" y="75" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{a}x + {b}°</text>'
        f'<text x="200" y="175" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">{total_deg}°</text>'
    )
    prompt = (
        f"Two straight lines intersect. Two vertically opposite angles measure $({a}x + {b}^\\circ)$ and ${total_deg}^\\circ$.\n\n"
        f"1. Set up an equation and solve for $x$.\n"
        f"2. Give the geometric reason."
    )
    sol = (
        f"**Step 1:** Vertically opposite angles are equal [$\\text{{vert opp }}\\angle\\text{{s}}$].\n\n"
        f"**Step 2:** Set up and solve the equation:\n"
        f"$${a}x + {b} = {total_deg}$$\n"
        f"$${a}x = {total_deg} - {b} = {a * x_val}$$\n"
        f"$$x = \\frac{{{a * x_val}}}{{{a}}} = {x_val}$$\n\n"
        f"**Conclusion:** $x = {x_val}$ [$\\text{{vert opp }}\\angle\\text{{s}}$]."
    )
    ans = f"x = {x_val} [vert opp ∠s]"
    return {
        "id": f"g7_line_18_{rng.randint(100000, 999999)}",
        "subskill": "18_vertically_opposite_angles_algebraic_solve",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Reason", "body": "Vertically opposite angles are equal."},
                {"title": "Equation", "body": f"{a}x + {b} = {total_deg}."},
                {"title": "Isolate Term", "body": f"{a}x = {total_deg - b}."},
                {"title": "Solve x", "body": f"x = {x_val}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_18",
        "hints": {
            "tier_1": f"Equate the two expressions: {a}x + {b} = {total_deg}.",
            "tier_2": f"Subtract {b} from both sides.",
            "tier_3": f"Divide by {a} to get x = {x_val}."
        },
        "misconception_tags": ["algebraic_equation_solving_error"]
    }


# 19. Intersecting lines four angles puzzle
def arch_19_intersecting_lines_four_angles_puzzle(rng: random.Random) -> Dict[str, Any]:
    angle_a = rng.choice([40, 50, 60, 70, 110, 120, 130])
    angle_b = 180 - angle_a
    svg = _svg_wrap(
        f'<line x1="50" y1="50" x2="350" y2="190" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="190" x2="350" y2="50" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="200" y="75" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle_a}°</text>'
        f'<text x="270" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">a</text>'
        f'<text x="200" y="175" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">b</text>'
        f'<text x="130" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">c</text>'
    )
    prompt = (
        f"Two straight lines intersect. One of the angles formed is {angle_a}°.\n\n"
        f"Calculate the values of unknown angles $a$, $b$, and $c$, providing geometric reasons for each."
    )
    sol = (
        f"**Step 1:** Find angle $b$:\n"
        f"Angle $b$ is vertically opposite to {angle_a}°:\n"
        f"$$b = {angle_a}^\\circ \\text{{ [vert opp }}\\angle\\text{{s]}}$$\n\n"
        f"**Step 2:** Find angle $a$:\n"
        f"Angle $a$ and {angle_a}° lie on a straight line:\n"
        f"$$a + {angle_a}^\\circ = 180^\\circ \\text{{ [}}\\angle\\text{{s on a straight line]}}$$\n"
        f"$$a = 180^\\circ - {angle_a}^\\circ = {angle_b}^\\circ$$\n\n"
        f"**Step 3:** Find angle $c$:\n"
        f"Angle $c$ is vertically opposite to angle $a$:\n"
        f"$$c = a = {angle_b}^\\circ \\text{{ [vert opp }}\\angle\\text{{s]}}$$"
    )
    ans = f"a = {angle_b}°, b = {angle_a}°, c = {angle_b}°"
    return {
        "id": f"g7_line_19_{rng.randint(100000, 999999)}",
        "subskill": "19_intersecting_lines_four_angles_puzzle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Vert Opp", "body": f"b = {angle_a}° [vert opp ∠s]."},
                {"title": "Straight Line", "body": f"a = 180° - {angle_a}° = {angle_b}° [∠s on straight line]."},
                {"title": "Vert Opp for c", "body": f"c = a = {angle_b}° [vert opp ∠s]."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_19",
        "hints": {
            "tier_1": "Use straight line property (adds to 180°) and vertically opposite angles (equal).",
            "tier_2": f"Opposite angle b is {angle_a}°. Adjacent angle a is 180 - {angle_a}.",
            "tier_3": f"a = {angle_b}°, b = {angle_a}°, c = {angle_b}°."
        },
        "misconception_tags": ["confused_adjacent_and_opposite_measures"]
    }


# 20. Angles around a point revolution numeric
def arch_20_angles_around_a_point_revolution_numeric(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([85, 90, 110, 120])
    a2 = rng.choice([75, 80, 95, 105])
    a3 = rng.choice([60, 70, 85])
    unknown = 360 - (a1 + a2 + a3)
    svg = _svg_wrap(
        f'<line x1="200" y1="120" x2="340" y2="120" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="200" y2="20" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="80" y2="120" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="140" y2="210" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="200" cy="120" r="4" fill="#1e293b"/>'
        f'<text x="240" y="80" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{a1}°</text>'
        f'<text x="130" y="80" font-family="sans-serif" font-size="13" font-weight="bold" fill="#059669">{a2}°</text>'
        f'<text x="130" y="170" font-family="sans-serif" font-size="13" font-weight="bold" fill="#7c3aed">{a3}°</text>'
        f'<text x="250" y="170" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"Four angles meet at a common vertex point: {a1}°, {a2}°, {a3}°, and $x$.\n\n"
        f"Calculate the value of $x$, giving the standard geometric reason."
    )
    sum_known = a1 + a2 + a3
    sol = (
        f"**Step 1:** State the geometric theorem:\n"
        f"Angles around a point add up to $360^\\circ$ [$\\angle\\text{{s around a point}}$ or revolution].\n\n"
        f"**Step 2:** Formulate and solve the equation:\n"
        f"$${a1}^\\circ + {a2}^\\circ + {a3}^\\circ + x = 360^\\circ$$\n"
        f"$${sum_known}^\\circ + x = 360^\\circ$$\n"
        f"$$x = 360^\\circ - {sum_known}^\\circ = {unknown}^\\circ$$\n\n"
        f"**Conclusion:** $x = {unknown}^\\circ$ [$\\angle\\text{{s around a point}}$]."
    )
    ans = f"x = {unknown}° [∠s around a point]"
    return {
        "id": f"g7_line_20_{rng.randint(100000, 999999)}",
        "subskill": "20_angles_around_a_point_revolution_numeric",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Full Revolution", "body": "Angles sharing a single point form a full revolution of 360°."},
                {"title": "Sum Knowns", "body": f"{a1}° + {a2}° + {a3}° = {sum_known}°."},
                {"title": "Subtract from 360°", "body": f"x = 360° - {sum_known}° = {unknown}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_20",
        "hints": {
            "tier_1": "What is the degree measure of a full circle / revolution?",
            "tier_2": f"Add the known angles ({sum_known}°) and subtract from 360°.",
            "tier_3": f"x = 360 - {sum_known} = {unknown}°."
        },
        "misconception_tags": ["used_180_instead_of_360_for_point"]
    }


# 21. Angles around a point revolution algebraic
def arch_21_angles_around_a_point_revolution_algebraic(rng: random.Random) -> Dict[str, Any]:
    # 2x + 3x + 4x + 90 = 360 -> 9x = 270 -> x = 30
    x_val = rng.choice([20, 25, 30])
    coeffs = [2, 3, 4]
    sum_coeffs = sum(coeffs) # 9
    const_ang = 360 - (sum_coeffs * x_val)
    svg = _svg_wrap(
        f'<line x1="200" y1="120" x2="330" y2="120" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="200" y2="30" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="90" y2="120" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="200" y1="120" x2="130" y2="200" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="200" cy="120" r="4" fill="#1e293b"/>'
        f'<text x="240" y="80" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">{coeffs[0]}x</text>'
        f'<text x="130" y="80" font-family="sans-serif" font-size="13" font-weight="bold" fill="#059669">{coeffs[1]}x</text>'
        f'<text x="130" y="170" font-family="sans-serif" font-size="13" font-weight="bold" fill="#7c3aed">{coeffs[2]}x</text>'
        f'<text x="240" y="170" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">{const_ang}°</text>'
    )
    prompt = (
        f"Four angles meeting at a point are given by ${coeffs[0]}x$, ${coeffs[1]}x$, ${coeffs[2]}x$, and ${const_ang}^\\circ$.\n\n"
        f"Calculate the value of $x$, providing the geometric reason."
    )
    sol = (
        f"**Step 1:** The sum of angles around a point is $360^\\circ$ [$\\angle\\text{{s around a point}}$].\n\n"
        f"**Step 2:** Formulate the equation:\n"
        f"$${coeffs[0]}x + {coeffs[1]}x + {coeffs[2]}x + {const_ang} = 360$$\n"
        f"$${sum_coeffs}x + {const_ang} = 360$$\n"
        f"$${sum_coeffs}x = 360 - {const_ang} = {sum_coeffs * x_val}$$\n"
        f"$$x = \\frac{{{sum_coeffs * x_val}}}{{{sum_coeffs}}} = {x_val}$$\n\n"
        f"**Conclusion:** $x = {x_val}$ [$\\angle\\text{{s around a point}}$]."
    )
    ans = f"x = {x_val} [∠s around a point]"
    return {
        "id": f"g7_line_21_{rng.randint(100000, 999999)}",
        "subskill": "21_angles_around_a_point_revolution_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Sum around Point", "body": f"{sum_coeffs}x + {const_ang}° = 360°."},
                {"title": "Subtract Constant", "body": f"{sum_coeffs}x = {sum_coeffs * x_val}°."},
                {"title": "Divide", "body": f"x = {x_val}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_21",
        "hints": {
            "tier_1": f"Combine like terms: {coeffs[0]}x + {coeffs[1]}x + {coeffs[2]}x = {sum_coeffs}x.",
            "tier_2": f"Set {sum_coeffs}x + {const_ang} = 360.",
            "tier_3": f"x = {x_val}."
        },
        "misconception_tags": ["angles_around_point_algebra_error"]
    }


# 22. Perpendicular bisector visual properties
def arch_22_perpendicular_bisector_visual_properties(rng: random.Random) -> Dict[str, Any]:
    seg_len = rng.choice([10, 12, 14, 16])
    half = seg_len // 2
    svg = _svg_wrap(
        f'<line x1="60" y1="120" x2="340" y2="120" stroke="#1e293b" stroke-width="4"/>'
        f'<line x1="200" y1="30" x2="200" y2="210" stroke="#0284c7" stroke-width="3"/>'
        f'<rect x="200" y="105" width="15" height="15" fill="none" stroke="#0284c7" stroke-width="2"/>'
        f'<circle cx="60" cy="120" r="4" fill="#1e293b"/>'
        f'<circle cx="340" cy="120" r="4" fill="#1e293b"/>'
        f'<circle cx="200" cy="120" r="4" fill="#0284c7"/>'
        # Tick marks on both halves
        f'<line x1="130" y1="112" x2="130" y2="128" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="270" y1="112" x2="270" y2="128" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="50" y="105" font-family="sans-serif" font-size="14" font-weight="bold">A</text>'
        f'<text x="345" y="105" font-family="sans-serif" font-size="14" font-weight="bold">B</text>'
        f'<text x="205" y="140" font-family="sans-serif" font-size="14" font-weight="bold">M ({seg_len} cm)</text>'
        f'<text x="210" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0284c7">L</text>'
    )
    prompt = (
        f"Line L cuts line segment AB ({seg_len} cm long) at point M. "
        f"A right angle symbol is shown at M, and tick marks show that AM = MB.\n\n"
        f"1. What is the special mathematical term for line L?\n"
        f"2. Calculate the length of segment AM in cm."
    )
    sol = (
        f"**Step 1:** A line that is perpendicular to a segment and divides it into two equal halves is called a **perpendicular bisector**.\n\n"
        f"**Step 2:** Since M bisects AB:\n"
        f"$$AM = \\frac{{AB}}{{2}} = \\frac{{{seg_len}}}{{2}} = {half}\\text{{ cm}}$$"
    )
    ans = f"1. Perpendicular bisector; 2. {half} cm"
    return {
        "id": f"g7_line_22_{rng.randint(100000, 999999)}",
        "subskill": "22_perpendicular_bisector_visual_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Two Properties", "body": "Line L forms a 90° angle AND cuts AB into two equal segments."},
                {"title": "Term", "body": "This makes Line L the perpendicular bisector of AB."},
                {"title": "Half Length", "body": f"AM = {seg_len} / 2 = {half} cm."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_22",
        "hints": {
            "tier_1": "Perpendicular means 90°; bisect means cut into two equal halves.",
            "tier_2": "Combine both words: perpendicular bisector.",
            "tier_3": f"1. Perpendicular bisector, 2. {half} cm."
        },
        "misconception_tags": ["confused_bisector_with_median"]
    }


# 23. Parallel lines transversal identification
def arch_23_parallel_lines_transversal_identification(rng: random.Random) -> Dict[str, Any]:
    tx1 = rng.choice([90, 100, 110, 120])
    svg = _svg_wrap(
        f'<line x1="40" y1="70" x2="360" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="40" y1="170" x2="360" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        # Transversal line
        f'<line x1="{tx1}" y1="20" x2="{400 - tx1}" y2="220" stroke="#dc2626" stroke-width="3"/>'
        f'<text x="370" y="75" font-family="sans-serif" font-size="14" font-weight="bold">Line 1</text>'
        f'<text x="370" y="175" font-family="sans-serif" font-size="14" font-weight="bold">Line 2</text>'
        f'<text x="310" y="215" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">Line T</text>'
    )
    prompt = (
        "In the diagram, Line 1 and Line 2 are parallel lines. Line T cuts across both parallel lines at two distinct points.\n\n"
        "1. What is the specific geometric name for a line that intersects two or more lines?\n"
        "2. How many total angles are formed at the two intersection points?"
    )
    sol = (
        "**Step 1:** A line that cuts across two or more other lines is called a **transversal**.\n\n"
        "**Step 2:** Four angles are formed at each intersection point, making a total of **8 angles**."
    )
    ans = "1. Transversal; 2. 8 angles"
    return {
        "id": f"g7_line_23_{rng.randint(100000, 999999)}",
        "subskill": "23_parallel_lines_transversal_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Cutting Line", "body": "Line T cuts across both parallel lines."},
                {"title": "Name", "body": "It is called a transversal."},
                {"title": "Total Angles", "body": "4 angles per vertex * 2 vertices = 8 angles."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_23",
        "hints": {
            "tier_1": "The word starts with 'trans' meaning across.",
            "tier_2": "It is a transversal line.",
            "tier_3": "1. Transversal, 2. 8 angles."
        },
        "misconception_tags": ["transversal_terminology_error"]
    }


# 24. Corresponding angles F-shape identification
def arch_24_corresponding_angles_f_shape_identification(rng: random.Random) -> Dict[str, Any]:
    tx1 = rng.choice([110, 120, 130, 140])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="{tx1}" y1="20" x2="{400 - tx1}" y2="220" stroke="#1e293b" stroke-width="3"/>'
        # Top-right angle at upper intersection
        f'<text x="180" y="60" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠1</text>'
        # Top-right angle at lower intersection
        f'<text x="260" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠2</text>'
    )
    prompt = (
        "Two parallel lines are intersected by a transversal. Angles ∠1 and ∠2 occupy the matching top-right position at each intersection.\n\n"
        "1. What is the name of this pair of angles?\n"
        "2. Which letter of the alphabet (F, Z, or C) helps identify corresponding angles?\n"
        "3. Are ∠1 and ∠2 equal or supplementary?"
    )
    sol = (
        "**Step 1:** Angles in the same relative position at each intersection are **corresponding angles**.\n\n"
        "**Step 2:** The letter **F** (can be upside down or backwards) identifies corresponding angles.\n\n"
        "**Step 3:** When the lines are parallel, corresponding angles are **equal** [$\\text{{corr }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = "1. Corresponding angles; 2. F; 3. Equal"
    return {
        "id": f"g7_line_24_{rng.randint(100000, 999999)}",
        "subskill": "24_corresponding_angles_f_shape_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Relative Position", "body": "Both angles sit on the top-right of the parallel line and transversal."},
                {"title": "F-Shape", "body": "This creates an F-shaped relationship: corresponding angles."},
                {"title": "Equality", "body": "Because the lines are parallel, ∠1 = ∠2."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_24",
        "hints": {
            "tier_1": "Think of the letters: F (corresponding), Z (alternate), C (co-interior).",
            "tier_2": "Same position = corresponding = F-shape.",
            "tier_3": "1. Corresponding angles, 2. F, 3. Equal."
        },
        "misconception_tags": ["confused_f_and_z_shapes"]
    }


# 25. Corresponding angles solve for x
def arch_25_corresponding_angles_solve_for_x(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([52, 64, 71, 108, 115, 128])
    l1 = "AB"
    l2 = "CD"
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="120" y1="20" x2="280" y2="220" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="35" y="75" font-family="sans-serif" font-size="14" font-weight="bold">A</text>'
        f'<text x="360" y="75" font-family="sans-serif" font-size="14" font-weight="bold">B</text>'
        f'<text x="35" y="175" font-family="sans-serif" font-size="14" font-weight="bold">C</text>'
        f'<text x="360" y="175" font-family="sans-serif" font-size="14" font-weight="bold">D</text>'
        f'<text x="180" y="60" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle}°</text>'
        f'<text x="260" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the diagram, {l1} // {l2} and a transversal cuts both lines. One angle is given as {angle}°.\n\n"
        f"Determine the value of $x$, writing down the full geometric statement and reason."
    )
    sol = (
        f"**Step 1:** Notice that $x$ and {angle}° are in matching corresponding positions in an F-configuration.\n\n"
        f"**Step 2:** Since ${l1} // {l2}$, corresponding angles are equal:\n"
        f"$$x = {angle}^\\circ \\text{{ [corr }}\\angle\\text{{s, }}{l1} // {l2}\\text{{]}}$$"
    )
    ans = f"x = {angle}° [corr ∠s, {l1} // {l2}]"
    return {
        "id": f"g7_line_25_{rng.randint(100000, 999999)}",
        "subskill": "25_corresponding_angles_solve_for_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check Angle Positions", "body": "Both angles are in the upper-right corner of their intersection."},
                {"title": "Apply Parallel Lines Theorem", "body": f"x = {angle}° [corr ∠s, {l1} // {l2}]."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_25",
        "hints": {
            "tier_1": "Are these two angles corresponding, alternate, or co-interior?",
            "tier_2": "They are corresponding angles (F-shape).",
            "tier_3": f"x = {angle}° [corr ∠s, {l1} // {l2}]."
        },
        "misconception_tags": ["omitted_parallel_line_reason"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
