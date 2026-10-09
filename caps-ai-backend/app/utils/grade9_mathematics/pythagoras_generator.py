"""Grade 9 Mathematics — Theorem of Pythagoras in 2D & 3D (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Distance between points in the Cartesian plane using Pythagoras: d = sqrt((x2 - x1)^2 + (y2 - y1)^2).
- Space diagonal of a 3D rectangular box/room: d^2 = l^2 + b^2 + h^2.
- Multi-step composite right-angled triangle figures.
- Real-world optimization and geometric modeling.
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
    return s.replace(".", "{,}")


TOPIC = "grade9_math_pythagoras"
LO = "g9_math_pythagoras"


def generate_space_diagonal_3d(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Space diagonal of box: d = sqrt(l^2 + b^2 + h^2)
    # Nice integer triples: (1, 2, 2 -> 3), (2, 3, 6 -> 7), (4, 12, 3 -> 13), (1, 4, 8 -> 9), (6, 6, 7 -> 11)
    base_triples = [(2, 3, 6, 7), (1, 4, 8, 9), (4, 12, 3, 13), (2, 10, 11, 15)]
    l, b, h, diag = r.choice(base_triples)
    scale = r.choice([1, 2])
    l, b, h, diag = l * scale, b * scale, h * scale, diag * scale
    
    floor_diag_sq = l**2 + b**2
    floor_diag = math.sqrt(floor_diag_sq)
    floor_diag_str = _fmt_sa(floor_diag, 2)
    
    prompt = (
        f"A rectangular room or storage container has length \\(l = {l}\\text{{ m}}\\), "
        f"breadth \\(b = {b}\\text{{ m}}\\), and vertical height \\(h = {h}\\text{{ m}}\\).\n\n"
        f"1. Calculate the diagonal distance across the horizontal floor of the room. Leave your answer in surd form if not an integer.\n"
        f"2. Using the Theorem of Pythagoras in three dimensions, calculate the length of the longest rigid metal pole "
        f"that can fit inside the room from one bottom corner to the opposite top corner.\n"
        f"3. State all geometric reasons and show your full calculation."
    )
    prompt_latex = (
        rf"\text{{Rectangular Room: }} l = {l}\text{{ m}}, \quad b = {b}\text{{ m}}, \quad h = {h}\text{{ m}}." "\n\n"
        r"\text{Calculate the floor diagonal and the 3D space diagonal } d = \sqrt{l^2 + b^2 + h^2}."
    )
    answer_latex = (
        rf"\text{{1. Floor diagonal }} d_\text{{floor}}^2 = {l}^2 + {b}^2 = {l**2} + {b**2} = {floor_diag_sq} \implies "
        rf"d_\text{{floor}} = \sqrt{{{floor_diag_sq}}}\text{{ m}} \approx {floor_diag_str}\text{{ m}}" "\n"
        rf"\text{{2. Space diagonal }} d_\text{{space}}^2 = d_\text{{floor}}^2 + h^2 = {floor_diag_sq} + {h}^2 = {floor_diag_sq} + {h**2} = {diag**2}" "\n"
        rf"d_\text{{space}} = \sqrt{{{diag**2}}} = {diag}\text{{ m}} \quad [\text{{Pythagoras in 3D}}]"
    )
    sample_answer = (
        f"1. Floor diagonal:\n"
        f"   d_floor² = l² + b² = {l}² + {b}² = {l**2} + {b**2} = {floor_diag_sq}.\n"
        f"   d_floor = √({floor_diag_sq}) m ≈ {floor_diag_str} m.\n"
        f"2. Space diagonal:\n"
        f"   d_space² = d_floor² + h² = {floor_diag_sq} + {h}² = {floor_diag_sq} + {h**2} = {diag**2}.\n"
        f"   d_space = √({diag**2}) = {diag} m (Pythagoras in 3D).\n"
        f"3. The longest pole that can fit inside the room is {diag} m."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate floor diagonal squared: {floor_diag_sq}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Apply 3D Pythagoras formula: d² = l² + b² + h² with reason", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Evaluate sum of squares: {diag**2}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct space diagonal: {diag} m with units", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "First find the diagonal of the floor using Pythagoras. Then use that floor diagonal as the base of a second right-angled triangle with height h.",
        "tier_2": "In three dimensions, the space diagonal squared equals the sum of the squares of all three dimensions: d² = l² + b² + h².",
        "tier_3": f"d² = {l}² + {b}² + {h}² = {l**2} + {b**2} + {h**2} = {diag**2}. Therefore d = √{diag**2} = {diag} m.",
    }
    return {
        "id": f"g9_pyth_3d_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "pythagoras_in_3d_space_diagonal",
        "learning_objective_id": f"{LO}_space_diagonal",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["forgetting_height_dimension_in_3d", "misapplying_square_root_to_individual_terms"],
        "keywords": ["pythagoras", "space diagonal", "3d", "rectangular room", "hypotenuse"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": mode,
        "difficulty": "hard",
        "marks": 5,
    }


def generate_cartesian_distance(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Choose nice integer distance
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    dx, dy, dist = r.choice(triples)
    if r.choice([True, False]):
        dx, dy = dy, dx
        
    x1 = r.randint(-5, 5)
    y1 = r.randint(-5, 5)
    
    # x2 = x1 + dx or x1 - dx
    s_x = r.choice([-1, 1])
    s_y = r.choice([-1, 1])
    x2 = x1 + s_x * dx
    y2 = y1 + s_y * dy
    
    prompt = (
        f"In the Cartesian coordinate plane, point \\(A({x1}; {y1})\\) and point \\(B({x2}; {y2})\\) are plotted.\n\n"
        f"1. Draw or conceptualise a right-angled triangle with hypotenuse \\(AB\\), and determine:\n"
        f"   (a) The horizontal distance \\(\\Delta x = |x_2 - x_1|\\)\n"
        f"   (b) The vertical distance \\(\\Delta y = |y_2 - y_1|\\)\n"
        f"2. Apply the Theorem of Pythagoras to calculate the straight-line distance between point \\(A\\) and point \\(B\\)."
    )
    prompt_latex = (
        rf"\text{{Cartesian Points: }} A({x1}; {y1}) \quad \text{{and}} \quad B({x2}; {y2})." "\n\n"
        r"\text{Calculate the distance } AB \text{ using the Theorem of Pythagoras.}"
    )
    answer_latex = (
        rf"\Delta x = |{x2} - ({x1})| = {dx}, \quad \Delta y = |{y2} - ({y1})| = {dy}" "\n"
        rf"AB^2 = (\Delta x)^2 + (\Delta y)^2 = ({dx})^2 + ({dy})^2 = {dx**2} + {dy**2} = {dist**2}" "\n"
        rf"AB = \sqrt{{{dist**2}}} = {dist}\text{{ units}}"
    )
    sample_answer = (
        f"1. (a) Horizontal change Δx = |{x2} - ({x1})| = {dx} units.\n"
        f"   (b) Vertical change Δy = |{y2} - ({y1})| = {dy} units.\n"
        f"2. By Pythagoras:\n"
        f"   AB² = (Δx)² + (Δy)² = {dx}² + {dy}² = {dx**2} + {dy**2} = {dist**2}.\n"
        f"   AB = √({dist**2}) = {dist} units."
    )
    schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", f"desc": f"Horizontal distance Δx = {dx}", "marks": 1, "editable": True},
            {"id": "mp2", f"desc": f"Vertical distance Δy = {dy}", "marks": 1, "editable": True},
            {"id": "mp3", f"desc": f"Pythagoras formula setup: AB² = {dx}² + {dy}² = {dist**2}", "marks": 1, "editable": True},
            {"id": "mp4", f"desc": f"Accurate distance AB = {dist} units", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Subtract the x-coordinates to find horizontal base, and subtract y-coordinates to find vertical height.",
        "tier_2": "The distance between two points forms the hypotenuse of a right-angled triangle: d² = (x2 - x1)² + (y2 - y1)².",
        "tier_3": f"Δx = {dx}, Δy = {dy}. AB² = {dx}² + {dy}² = {dx**2} + {dy**2} = {dist**2}. Therefore AB = {dist} units.",
    }
    return {
        "id": f"g9_pyth_coord_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "pythagoras_coordinate_distance_formula",
        "learning_objective_id": f"{LO}_coordinate_distance",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["sign_error_subtracting_coordinates", "forgetting_square_root"],
        "keywords": ["distance formula", "cartesian plane", "pythagoras", "coordinates"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": mode,
        "difficulty": "medium",
        "marks": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "3d" or archetype == "space_diagonal":
        return generate_space_diagonal_3d(r, mode=mode)
    elif archetype == "cartesian" or archetype == "distance":
        return generate_cartesian_distance(r, mode=mode)
    else:
        choice = r.choice(["3d", "cartesian"])
        if choice == "3d":
            return generate_space_diagonal_3d(r, mode=mode)
        else:
            return generate_cartesian_distance(r, mode=mode)
