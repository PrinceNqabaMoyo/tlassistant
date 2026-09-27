"""Diagram Spec — a structured, deterministic description of a maths figure.

The same JSON travels in two directions:

  * **Render**: the frontend ``DiagramRenderer`` turns a spec into a JSXGraph
    figure, so a diagram *is* the question surface (no hand-drawn image assets).
  * **Mark**: an interactive figure (e.g. "click the hypotenuse") emits the same
    vocabulary back (an edge key), so constructions are gradable deterministically.

Because the spec is plain JSON it is also the "descriptive parameter" the Pro-tier
agent reads to reason about a figure — never pixels.

Diagram labels are *display strings* (plain unicode such as ``"θ"``, ``"5"``,
``"50°"``), not LaTeX: JSXGraph text nodes render them directly.

Right-triangle canonical layout (the only orientation used for Term 1):

        C  (apex, top-right)
        |\\
   opp  | \\  hyp
        |  \\
    B───┴───A      A = θ vertex (bottom-left)
        adj        B = right-angle vertex (bottom-right)

Edge keys are vertex-pair strings: ``"AB"`` (adjacent), ``"BC"`` (opposite),
``"AC"`` (hypotenuse).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

# Role -> edge key for the canonical layout.
ROLE_EDGE = {"adjacent": "AB", "opposite": "BC", "hypotenuse": "AC"}
EDGE_ROLE = {v: k for k, v in ROLE_EDGE.items()}


def right_triangle(
    *,
    adjacent: str = "",
    opposite: str = "",
    hypotenuse: str = "",
    angle_label: str = "θ",
    show_right_angle: bool = True,
    vertex_labels: Optional[Dict[str, str]] = None,
    width: float = 4.0,
    height: float = 3.0,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a right-triangle diagram spec.

    ``adjacent`` / ``opposite`` / ``hypotenuse`` are the display labels for the
    three sides relative to ``angle_label`` (the angle at vertex A). Empty labels
    are omitted. ``vertex_labels`` optionally names the corners (e.g. A→"A").
    """
    points = {"A": [0.0, 0.0], "B": [float(width), 0.0], "C": [float(width), float(height)]}
    sides: List[Dict[str, Any]] = []
    for role, frm, to in (("adjacent", "A", "B"), ("opposite", "B", "C"), ("hypotenuse", "A", "C")):
        label = {"adjacent": adjacent, "opposite": opposite, "hypotenuse": hypotenuse}[role]
        sides.append({"edge": frm + to, "from": frm, "to": to, "role": role, "label": str(label)})
    spec: Dict[str, Any] = {
        "kind": "right_triangle",
        "points": points,
        "right_angle_at": "B" if show_right_angle else None,
        "angles": [{"at": "A", "label": str(angle_label)}] if angle_label else [],
        "sides": sides,
        "vertex_labels": dict(vertex_labels or {}),
        "caption": caption,
    }
    return spec


def cartesian_point(
    *,
    x: float,
    y: float,
    point_label: str = "P",
    angle_label: str = "θ",
    show_dropline: bool = True,
    show_radius: bool = True,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a Cartesian-plane spec: a plotted point with the line from O and the
    angle measured anti-clockwise from the positive x-axis."""
    return {
        "kind": "cartesian_point",
        "point": [float(x), float(y)],
        "point_label": str(point_label),
        "angle_label": str(angle_label),
        "show_dropline": bool(show_dropline),
        "show_radius": bool(show_radius),
        "caption": caption,
    }


def number_line(
    *,
    min_val: float = -5,
    max_val: float = 5,
    point_at: float = 0,
    closed: bool = True,
    ray_direction: str = "positive",
    ticks: float = 1,
    label: str = "",
) -> Dict[str, Any]:
    """Build a number-line diagram spec for inequalities.

    ``ray_direction``: ``"positive"`` | ``"negative"`` | ``"both"`` | ``"none"``
    """
    return {
        "kind": "number_line",
        "min": float(min_val),
        "max": float(max_val),
        "point": {"at": float(point_at), "closed": bool(closed)},
        "ray": {"direction": str(ray_direction)} if ray_direction != "none" else None,
        "ticks": float(ticks),
        "label": str(label),
    }


def dot_pattern(
    *,
    family: str = "tables",
    figure_index: int = 1,
    count_rule: str = "",
    caption: str = "",
) -> Dict[str, Any]:
    """Build a parametric diagram pattern spec for sequences.

    ``family`` names the figure family (``"tables"``, ``"matchsticks"``, ``"stadium"``).
    ``count_rule`` is a LaTeX string describing the count (e.g. ``"4 + 2(n-1)"``).
    """
    return {
        "kind": "dot_pattern",
        "family": str(family),
        "figure_index": int(figure_index),
        "count_rule": str(count_rule),
        "caption": str(caption),
    }


def angle_diagram(
    *,
    vertex: str = "B",
    arms: List[str] = None,
    angle_value: float = 60.0,
    angle_label: str = "",
    angle_arc: bool = True,
    supplementary_angles: List[Dict[str, Any]] = None,
    caption: str = "",
) -> Dict[str, Any]:
    """Build an angle diagram spec showing an angle with arc and optional supplementary angles.

    ``arms`` is a list of arm labels (e.g. ["BA", "BC"]).
    ``angle_value`` is the interior angle measure in degrees.
    ``supplementary_angles`` is a list of dicts with keys: vertex, value, label.
    """
    return {
        "kind": "angle_diagram",
        "vertex": str(vertex),
        "arms": list(arms or []),
        "angle_value": float(angle_value),
        "angle_label": str(angle_label) if angle_label else f"{angle_value}°",
        "angle_arc": bool(angle_arc),
        "supplementary_angles": list(supplementary_angles or []),
        "caption": str(caption),
    }


def parallel_transversal(
    *,
    line1_label: str = "AB",
    line2_label: str = "CD",
    transversal_label: str = "EF",
    given_angle: float = 50.0,
    given_position: str = "top_left_exterior",
    unknown_angles: List[Dict[str, Any]] = None,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a parallel-lines-with-transversal diagram spec.

    ``given_position`` tells which angle is known:
        ``"top_left_exterior"``, ``"top_right_exterior"``, ``"top_left_interior"``,
        ``"top_right_interior"``, ``"bottom_left_interior"``,
        ``"bottom_right_interior"``, ``"bottom_left_exterior"``,
        ``"bottom_right_exterior"``.
    ``unknown_angles`` is a list of dicts with keys: position, label, answer.
    """
    return {
        "kind": "parallel_transversal",
        "line1_label": str(line1_label),
        "line2_label": str(line2_label),
        "transversal_label": str(transversal_label),
        "given_angle": float(given_angle),
        "given_position": str(given_position),
        "unknown_angles": list(unknown_angles or []),
        "caption": str(caption),
    }


def triangle(
    *,
    vertices: List[str] = None,
    points: Dict[str, List[float]] = None,
    side_labels: Dict[str, str] = None,
    angle_labels: Dict[str, str] = None,
    angle_values: Dict[str, float] = None,
    equal_sides: List[List[str]] = None,
    right_angle_at: str = None,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a general triangle diagram spec.

    ``vertices`` is a list of 3 vertex names, e.g. ["A", "B", "C"].
    ``points`` maps vertex name to [x, y] coordinates.
    ``side_labels`` maps edge key (e.g. "AB") to a display label.
    ``angle_labels`` maps vertex name to a display label for the angle at that vertex.
    ``angle_values`` maps vertex name to the angle measure in degrees.
    ``equal_sides`` is a list of lists of edge keys that have equal length tick marks,
        e.g. [["AB", "AC"]] for an isosceles triangle.
    ``right_angle_at`` marks a right angle at the given vertex.
    """
    return {
        "kind": "triangle",
        "vertices": list(vertices or ["A", "B", "C"]),
        "points": dict(points or {}),
        "side_labels": dict(side_labels or {}),
        "angle_labels": dict(angle_labels or {}),
        "angle_values": dict(angle_values or {}),
        "equal_sides": list(equal_sides or []),
        "right_angle_at": str(right_angle_at) if right_angle_at else None,
        "caption": str(caption),
    }


def quadrilateral(
    *,
    shape_type: str = "parallelogram",
    vertices: List[str] = None,
    points: Dict[str, List[float]] = None,
    side_labels: Dict[str, str] = None,
    angle_labels: Dict[str, str] = None,
    angle_values: Dict[str, float] = None,
    equal_sides: List[List[str]] = None,
    parallel_pairs: List[List[str]] = None,
    diagonals: bool = False,
    diagonal_intersection: str = "",
    caption: str = "",
) -> Dict[str, Any]:
    """Build a quadrilateral diagram spec.

    ``shape_type`` is one of: ``"parallelogram"``, ``"rectangle"``, ``"rhombus"``,
        ``"square"``, ``"trapezium"``, ``"kite"``, ``"general"``.
    ``parallel_pairs`` lists pairs of edge keys that are parallel,
        e.g. [["AB", "CD"], ["AD", "BC"]].
    ``diagonals`` toggles whether to draw the diagonals.
    ``diagonal_intersection`` is the label for the intersection point.
    """
    return {
        "kind": "quadrilateral",
        "shape_type": str(shape_type),
        "vertices": list(vertices or ["A", "B", "C", "D"]),
        "points": dict(points or {}),
        "side_labels": dict(side_labels or {}),
        "angle_labels": dict(angle_labels or {}),
        "angle_values": dict(angle_values or {}),
        "equal_sides": list(equal_sides or []),
        "parallel_pairs": list(parallel_pairs or []),
        "diagonals": bool(diagonals),
        "diagonal_intersection": str(diagonal_intersection),
        "caption": str(caption),
    }


def circle_subtended_angle(
    *,
    center: str = "O",
    center_coords: Optional[List[float]] = None,
    radius: float = 3.0,
    chord_arc: Optional[List[str]] = None,
    inscribed_vertices: Optional[List[str]] = None,
    points: Optional[Dict[str, List[float]]] = None,
    lines: Optional[List[List[str]]] = None,
    angles: Optional[List[Dict[str, Any]]] = None,
    vertex_labels: Optional[Dict[str, str]] = None,
    show_radii: bool = True,
    show_chord: bool = False,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a diagram spec for the 'Angle at Center is Twice Angle at Circumference' theorem.

    Default coordinates place O at origin, chord endpoints A and B on the lower circumference,
    and inscribed vertex C (or C & D) on the upper circumference.
    """
    pts = dict(points or {})
    if center not in pts:
        pts[center] = list(center_coords or [0.0, 0.0])

    # Default points if not provided: A=-40°, B=50°, C=140°
    if not pts.get("A"):
        pts["A"] = [round(radius * 0.766, 2), round(-radius * 0.643, 2)]  # ~ -40°
    if not pts.get("B"):
        pts["B"] = [round(-radius * 0.766, 2), round(-radius * 0.643, 2)]  # ~ 220° (-140°)
    if not pts.get("C"):
        pts["C"] = [0.0, float(radius)]  # 90° (apex)

    default_lines = []
    if show_radii:
        default_lines.extend([[center, "A"], [center, "B"]])
    if show_chord:
        default_lines.append(["A", "B"])
    default_lines.extend([["C", "A"], ["C", "B"]])

    return {
        "kind": "circle_subtended_angle",
        "center": str(center),
        "radius": float(radius),
        "points": pts,
        "lines": list(lines if lines is not None else default_lines),
        "angles": list(angles or []),
        "vertex_labels": dict(vertex_labels or {k: k for k in pts.keys()}),
        "caption": str(caption),
    }


def circle_cyclic_quad(
    *,
    center: str = "O",
    center_coords: Optional[List[float]] = None,
    radius: float = 3.0,
    vertices: Optional[List[str]] = None,
    points: Optional[Dict[str, List[float]]] = None,
    lines: Optional[List[List[str]]] = None,
    angles: Optional[List[Dict[str, Any]]] = None,
    vertex_labels: Optional[Dict[str, str]] = None,
    diagonals: bool = False,
    exterior_vertex: Optional[str] = None,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a diagram spec for Cyclic Quadrilateral theorems:
    - Opposite angles supplementary (sum to 180°)
    - Exterior angle equals interior opposite angle
    - Angles in the same segment equal (with diagonals)
    """
    verts = list(vertices or ["A", "B", "C", "D"])
    pts = dict(points or {})
    if center not in pts:
        pts[center] = list(center_coords or [0.0, 0.0])

    if not pts.get("A"):
        pts["A"] = [-1.8, 2.4]  # ~ 125°
    if not pts.get("B"):
        pts["B"] = [-2.8, -1.0]  # ~ 200°
    if not pts.get("C"):
        pts["C"] = [1.5, -2.6]  # ~ 300°
    if not pts.get("D"):
        pts["D"] = [2.7, 1.3]  # ~ 25°

    default_lines = [
        [verts[0], verts[1]],
        [verts[1], verts[2]],
        [verts[2], verts[3]],
        [verts[3], verts[0]],
    ]
    if diagonals:
        default_lines.extend([[verts[0], verts[2]], [verts[1], verts[3]]])
    if exterior_vertex and pts.get(exterior_vertex):
        default_lines.append([verts[2], exterior_vertex])

    return {
        "kind": "circle_cyclic_quad",
        "center": str(center),
        "radius": float(radius),
        "vertices": verts,
        "points": pts,
        "lines": list(lines if lines is not None else default_lines),
        "angles": list(angles or []),
        "vertex_labels": dict(vertex_labels or {k: k for k in pts.keys() if k != center}),
        "diagonals": bool(diagonals),
        "caption": str(caption),
    }


def circle_tangent_secant(
    *,
    center: str = "O",
    center_coords: Optional[List[float]] = None,
    radius: float = 3.0,
    tangent_point: str = "T",
    points: Optional[Dict[str, List[float]]] = None,
    lines: Optional[List[List[str]]] = None,
    angles: Optional[List[Dict[str, Any]]] = None,
    vertex_labels: Optional[Dict[str, str]] = None,
    show_radius_to_tangent: bool = False,
    caption: str = "",
) -> Dict[str, Any]:
    """Build a diagram spec for Tangent theorems:
    - Tangent-Chord Theorem (angle between tangent and chord = angle in alternate segment)
    - Tangent perpendicular to radius at point of contact (OT ⟂ tangent)
    - Tangents from external point
    """
    pts = dict(points or {})
    if center not in pts:
        pts[center] = list(center_coords or [0.0, 0.0])

    # Contact point T at bottom: [0, -radius]
    if not pts.get(tangent_point):
        pts[tangent_point] = [0.0, -float(radius)]
    # Tangent line ends P (left) and Q (right)
    if not pts.get("P"):
        pts["P"] = [-4.0, -float(radius)]
    if not pts.get("Q"):
        pts["Q"] = [4.0, -float(radius)]
    # Inscribed triangle vertices A and B
    if not pts.get("A"):
        pts["A"] = [-2.4, 1.8]  # ~ 140°
    if not pts.get("B"):
        pts["B"] = [2.4, 1.8]  # ~ 40°

    default_lines = [
        ["P", "Q"],  # tangent line
        [tangent_point, "A"],
        [tangent_point, "B"],
        ["A", "B"],  # inscribed triangle TAB
    ]
    if show_radius_to_tangent:
        default_lines.append([center, tangent_point])

    return {
        "kind": "circle_tangent_secant",
        "center": str(center),
        "radius": float(radius),
        "points": pts,
        "lines": list(lines if lines is not None else default_lines),
        "angles": list(angles or []),
        "vertex_labels": dict(vertex_labels or {k: k for k in pts.keys() if k != center}),
        "caption": str(caption),
    }

