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
