"""Grade 9 Mathematics - Geometry of Straight Lines Archetypes (26 to 50).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/03. Geometry of straight lines.md

Covers:
  - Error analysis: omitting parallel line reference in reasons
  - Converses and proving lines are parallel (alternate, corresponding, co-interior)
  - Dual transversal systems forming triangles
  - Zigzag parallel lines requiring auxiliary parallel lines (numeric and algebraic)
  - Perpendicular transversals
  - Angle bisectors of supplementary and vertically opposite angles
  - Multi-step combinations: straight line + transversal angles
  - Three parallel lines cut by transversals
  - Ratio of co-interior and straight line adjacent angles
  - Systems of equations on transversals
  - Fractions in straight line and co-interior angle equations
  - Authentic real-world contexts: railway tracks, bridge trusses
  - Compound multi-line geometric synthesis challenges
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .geometry_straight_lines_svg import (
    draw_intersecting_lines_svg,
    draw_parallel_transversal_svg,
    draw_parallel_zigzag_svg,
    draw_straight_line_adjacent_angles_svg,
)


def arch_26_error_analysis_omitting_parallel_line_reference_in_reason(rng: random.Random) -> Dict[str, Any]:
    """Error analysis: student omitted stating parallel lines in reason."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([52, 64, 73, 81])
    svg = draw_parallel_transversal_svg({"G4": f"{theta}°", "H1": "x"}, seed=seed)

    return {
        "subskill": "26_error_analysis_omitting_parallel_line_reference_in_reason",
        "question_text": (
            f"A learner solved for angle $x$ from the parallel lines ($AB \\parallel CD$) below:\n\n"
            f"**Learner's Statement and Reason:**\n"
            f"$x = {theta}^\\circ$ [alt $\\angle$s]\n\n"
            f"Explain why this geometric reason is incomplete under national examination standards, "
            f"and state the value of $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Explain error: Must specify which lines are parallel [alt ∠s, AB || CD]", "marks": 1},
            {"step": f"State accurate angle value: x = {theta}°", "marks": 1},
        ],
        "hints": [
            "Whenever you use alternate, corresponding, or co-interior angles, you must explicitly name the parallel lines in your reason, e.g. [alt $\\angle$s, $AB \\parallel CD$].",
            "Without naming the parallel lines, the reason is mathematically incomplete.",
            f"The value of $x$ is ${theta}^\\circ$.",
        ],
    }


def arch_27_prove_lines_parallel_alternate_angles_converse(rng: random.Random) -> Dict[str, Any]:
    """Find value of x that makes AB || CD via converse of alternate angles."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([25, 30, 35, 40])
    b = rng.choice([10, 15, 20])
    # 2x + b = x + (x_val + b)
    d = x_val + b
    svg = draw_parallel_transversal_svg({"G4": f"2x + {b}°", "H1": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "27_prove_lines_parallel_alternate_angles_converse",
        "question_text": (
            f"In the diagram below, transversal $EF$ intersects lines $AB$ and $CD$.\n\n"
            f"Alternate interior angles are $\\hat{{G}}_4 = (2x + {b})^\\circ$ and $\\hat{{H}}_1 = (x + {d})^\\circ$.\n"
            f"What value of $x$ proves that $AB$ is parallel to $CD$ ($AB \\parallel CD$)?"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set alternate angles equal: 2x + {b} = x + {d} [converse alt ∠s =]", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Lines $AB$ and $CD$ will be parallel if their alternate interior angles are equal: $2x + {b} = x + {d}$.",
            f"Subtract $x$ and subtract ${b}$: $x = {d} - {b} = {x_val}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_28_prove_lines_parallel_corresponding_angles_converse(rng: random.Random) -> Dict[str, Any]:
    """Find x that makes AB || CD via converse of corresponding angles."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 25, 30, 35])
    b = 15
    d = x_val + b
    svg = draw_parallel_transversal_svg({"G2": f"2x + {b}°", "H2": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "28_prove_lines_parallel_corresponding_angles_converse",
        "question_text": (
            f"Transversal $EF$ intersects lines $AB$ and $CD$ as shown below.\n\n"
            f"Corresponding angles are given as $\\hat{{G}}_2 = (2x + {b})^\\circ$ and $\\hat{{H}}_2 = (x + {d})^\\circ$.\n"
            f"Determine the value of $x$ for which line $AB$ is parallel to line $CD$ ($AB \\parallel CD$):"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Equate corresponding angles: 2x + {b} = x + {d} [converse corresp ∠s =]", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"If corresponding angles are equal, the lines are parallel: $2x + {b} = x + {d}$.",
            f"$x = {d} - {b} = {x_val}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_29_prove_lines_parallel_cointerior_angles_converse(rng: random.Random) -> Dict[str, Any]:
    """Find x that makes AB || CD via converse of co-interior angles."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 25, 30])
    rem = 180 - 5 * x_val
    b = 20
    d = rem - b
    svg = draw_parallel_transversal_svg({"G4": f"2x + {b}°", "H2": f"3x + {d}°"}, seed=seed)

    return {
        "subskill": "29_prove_lines_parallel_cointerior_angles_converse",
        "question_text": (
            f"In the diagram below, lines $AB$ and $CD$ are cut by a transversal.\n\n"
            f"Co-interior angles are $\\hat{{G}}_4 = (2x + {b})^\\circ$ and $\\hat{{H}}_2 = (3x + {d})^\\circ$.\n"
            f"Find the value of $x$ that proves $AB \\parallel CD$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set sum of co-interior angles to 180: (2x + {b}) + (3x + {d}) = 180 [converse co-int ∠s suppl]", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Lines are parallel if co-interior angles add up to $180^\\circ$: $(2x + {b}) + (3x + {d}) = 180$.",
            f"$5x + {b + d} = 180 \\implies 5x = {180 - (b + d)}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_30_parallel_lines_dual_transversal_triangle_formed(rng: random.Random) -> Dict[str, Any]:
    """Two transversals create top vertex angle equal to sum of alternate angles."""
    seed = rng.randint(1, 1_000_000)
    theta1 = rng.choice([32, 40, 48])
    theta2 = rng.choice([45, 53, 60])
    ans = theta1 + theta2
    svg = draw_parallel_zigzag_svg(f"{theta1}°", "x", f"{theta2}°", seed=seed)

    return {
        "subskill": "30_parallel_lines_dual_transversal_triangle_formed",
        "question_text": (
            f"In the figure below, line $AB$ is parallel to line $CD$ ($AB \\parallel CD$).\n\n"
            f"Two transversal segments meet at vertex $P$, forming angles of ${theta1}^\\circ$ and ${theta2}^\\circ$ "
            f"with the parallel lines.\n"
            f"Calculate the size of interior angle $x$ at vertex $P$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Draw auxiliary parallel line through P parallel to AB", "marks": 1},
            {"step": f"Use alternate angles to find x = {theta1}° + {theta2}° = {ans}°", "marks": 1},
        ],
        "hints": [
            "Draw a dashed construction line through $P$ parallel to both $AB$ and $CD$.",
            f"The angle at $P$ is divided into two alternate angles: ${theta1}^\\circ$ and ${theta2}^\\circ$.",
            f"$x = {theta1}^\\circ + {theta2}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_31_parallel_lines_zigzag_auxiliary_line_numeric(rng: random.Random) -> Dict[str, Any]:
    """Zigzag line between parallel lines: internal angle is alpha + beta."""
    seed = rng.randint(1, 1_000_000)
    alpha = rng.choice([35, 42, 50])
    beta = rng.choice([30, 38, 45])
    ans = alpha + beta
    svg = draw_parallel_zigzag_svg(f"{alpha}°", "x", f"{beta}°", seed=seed)

    return {
        "subskill": "31_parallel_lines_zigzag_auxiliary_line_numeric",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Using an auxiliary parallel line through vertex $P$, calculate the size of angle $x$ in degrees, "
            f"given that the top angle is ${alpha}^\\circ$ and the bottom angle is ${beta}^\\circ$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Construct auxiliary line through P parallel to AB and CD", "marks": 1},
            {"step": f"Calculate angle x: {alpha}° + {beta}° = {ans}° [alt ∠s]", "marks": 1},
        ],
        "hints": [
            "Construct a line through $P$ parallel to $AB$.",
            f"The top part of angle $x$ is alternate to ${alpha}^\\circ$, and the bottom part is alternate to ${beta}^\\circ$.",
            f"$x = {alpha}^\\circ + {beta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_32_parallel_lines_zigzag_auxiliary_line_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Zigzag line: 2x + 10 = alpha + beta."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([25, 30, 35])
    # 2x + 10 = total => total = 2*x_val + 10
    total = 2 * x_val + 10
    alpha = rng.choice([30, 35, 40])
    beta = total - alpha
    svg = draw_parallel_zigzag_svg(f"{alpha}°", "2x + 10°", f"{beta}°", seed=seed)

    return {
        "subskill": "32_parallel_lines_zigzag_auxiliary_line_algebraic",
        "question_text": (
            f"In the parallel line diagram below ($AB \\parallel CD$):\n\n"
            f"The angle at vertex $P$ is expressed algebraically as $(2x + 10)^\\circ$.\n"
            f"If the top angle is ${alpha}^\\circ$ and the bottom angle is ${beta}^\\circ$, calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set up equation via auxiliary parallel line: 2x + 10 = {alpha} + {beta} = {total}", "marks": 1},
            {"step": f"Solve for x: 2x = {total - 10} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Angle at $P$ equals the sum of the two alternate angles: $2x + 10 = {alpha} + {beta} = {total}$.",
            f"$2x = {total} - 10 = {total - 10}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_33_parallel_lines_perpendicular_transversal(rng: random.Random) -> Dict[str, Any]:
    """Transversal perpendicular to one parallel line is perpendicular to the other."""
    seed = rng.randint(1, 1_000_000)
    svg = draw_parallel_transversal_svg({"G4": "90°", "H2": "x"}, seed=seed)

    return {
        "subskill": "33_parallel_lines_perpendicular_transversal",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Transversal $EF$ is perpendicular to line $AB$ at point $G$ (forming an angle of $90^\\circ$).\n"
            f"Calculate the size of co-interior angle $x$ in degrees:"
        ),
        "correct_answer": "90",
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "State co-interior angle equation: 90° + x = 180° [co-int ∠s, AB || CD]", "marks": 1},
            {"step": "Calculate x = 90°", "marks": 1},
        ],
        "hints": [
            "Co-interior angles on parallel lines sum to $180^\\circ$: $90^\\circ + x = 180^\\circ$.",
            "$x = 180^\\circ - 90^\\circ = 90^\\circ$.",
            "This proves that a line perpendicular to one parallel line is perpendicular to all parallel lines.",
        ],
    }


def arch_34_bisector_of_adjacent_supplementary_angles(rng: random.Random) -> Dict[str, Any]:
    """Angle bisector of supplementary angle: theta + 2x = 180."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([60, 70, 80, 100])
    # remaining angle is 180 - theta, bisector divides it in half
    ans = (180 - theta) // 2
    svg = draw_straight_line_adjacent_angles_svg(f"{theta}°", f"{180 - theta}°", seed=seed)

    return {
        "subskill": "34_bisector_of_adjacent_supplementary_angles",
        "question_text": (
            f"On straight line $AB$, an adjacent angle measures ${theta}^\\circ$.\n\n"
            f"If the adjacent supplementary angle is bisected (cut exactly in half) by ray $MD$, "
            f"calculate the size of each half-angle in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Find full supplementary angle: 180° - {theta}° = {180 - theta}° [∠s on a str line]", "marks": 1},
            {"step": f"Divide by 2 to find bisected angle: {180 - theta}° / 2 = {ans}°", "marks": 1},
        ],
        "hints": [
            f"The full adjacent angle is $180^\\circ - {theta}^\\circ = {180 - theta}^\\circ$.",
            f"An angle bisector divides the angle into two equal parts: ${180 - theta}^\\circ \\div 2$.",
            f"Each half-angle measures ${ans}^\\circ$.",
        ],
    }


def arch_35_bisector_of_vertically_opposite_angles(rng: random.Random) -> Dict[str, Any]:
    """Vertically opposite angle is theta; ray bisects it."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([68, 76, 84, 92, 108])
    ans = theta // 2
    svg = draw_intersecting_lines_svg({"top": f"{theta}°", "bottom": f"{theta}°"}, seed=seed)

    return {
        "subskill": "35_bisector_of_vertically_opposite_angles",
        "question_text": (
            f"Two straight lines intersect at vertex $O$, creating vertically opposite angles of ${theta}^\\circ$.\n\n"
            f"If an angle bisector ray splits one of these angles into two equal halves, "
            f"what is the size of each half-angle in degrees?"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Calculate half of angle: {theta}° / 2 = {ans}°", "marks": 1},
        ],
        "hints": [
            f"An angle bisector divides an angle of ${theta}^\\circ$ into two equal angles.",
            f"${theta}^\\circ \\div 2 = {ans}^\\circ$.",
            f"The size is ${ans}^\\circ$.",
        ],
    }


def arch_36_multi_step_parallel_transversal_with_straight_line_combo(rng: random.Random) -> Dict[str, Any]:
    """Find angle on line, then use alternate interior angle."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([110, 115, 125, 130])
    # G1 = theta => G4 = theta (vert opp) => H1 = theta (alt)
    ans = theta
    svg = draw_parallel_transversal_svg({"G1": f"{theta}°", "H1": "x"}, seed=seed)

    return {
        "subskill": "36_multi_step_parallel_transversal_with_straight_line_combo",
        "question_text": (
            f"In the diagram below, lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Given that exterior angle $\\hat{{G}}_1 = {theta}^\\circ$, calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Find vertically opposite angle G4 = {theta}° [vert opp ∠s]", "marks": 1},
            {"step": f"Use alternate angle to find x = {theta}° [alt ∠s, AB || CD]", "marks": 1},
        ],
        "hints": [
            f"Angle $\\hat{{G}}_4$ is vertically opposite to $\\hat{{G}}_1$, so $\\hat{{G}}_4 = {theta}^\\circ$.",
            f"Angle $x$ and $\\hat{{G}}_4$ are alternate interior angles [alt $\\angle$s, $AB \\parallel CD$].",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_37_multi_step_parallel_transversal_with_vert_opp_combo(rng: random.Random) -> Dict[str, Any]:
    """Combine vert opp and corresponding angles."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([50, 60, 70, 80])
    svg = draw_parallel_transversal_svg({"G3": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "37_multi_step_parallel_transversal_with_vert_opp_combo",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"If $\\hat{{G}}_3 = {theta}^\\circ$ as shown in the diagram below, "
            f"calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Find corresponding angle H3 = {theta}° [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Find vertically opposite angle x = {theta}° [vert opp ∠s]", "marks": 1},
        ],
        "hints": [
            f"Corresponding angle $\\hat{{H}}_3 = \\hat{{G}}_3 = {theta}^\\circ$ [corresp $\\angle$s, $AB \\parallel CD$].",
            f"Angle $x$ is vertically opposite to $\\hat{{H}}_3$: $x = {theta}^\\circ$ [vert opp $\\angle$s].",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_38_three_parallel_lines_two_transversals_numeric(rng: random.Random) -> Dict[str, Any]:
    """Three parallel lines cut by transversal: transitive alternate angles."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([48, 56, 64, 72])
    svg = draw_parallel_transversal_svg({"G2": f"{theta}°", "H2": f"{theta}°"}, seed=seed)

    return {
        "subskill": "38_three_parallel_lines_two_transversals_numeric",
        "question_text": (
            f"Three lines $L_1, L_2,$ and $L_3$ are all parallel to each other ($L_1 \\parallel L_2 \\parallel L_3$).\n\n"
            f"A single transversal intersects all three lines. If the angle on $L_1$ is ${theta}^\\circ$, "
            f"calculate the size of the corresponding angle on $L_3$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Apply transitivity of parallel lines: angle = {theta}° [corresp ∠s, L1 || L3]", "marks": 1},
        ],
        "hints": [
            "Since $L_1 \\parallel L_2$ and $L_2 \\parallel L_3$, it follows that $L_1 \\parallel L_3$.",
            f"Corresponding angles on parallel lines are equal.",
            f"The angle size is ${theta}^\\circ$.",
        ],
    }


def arch_39_three_parallel_lines_two_transversals_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Algebraic angle equality across parallel lines: 3x - 15 = x + 25."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 25, 30])
    b = 15
    d = 2 * x_val - b
    svg = draw_parallel_transversal_svg({"G2": f"3x - {b}°", "H2": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "39_three_parallel_lines_two_transversals_algebraic",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Given corresponding angles $(3x - {b})^\\circ$ and $(x + {d})^\\circ$:\n"
            f"Calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Equate: 3x - {b} = x + {d} [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Solve: 2x = {d + b} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Corresponding angles are equal: $3x - {b} = x + {d}$.",
            f"$2x = {d + b}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_40_parallel_lines_ratio_cointerior_angles(rng: random.Random) -> Dict[str, Any]:
    """Co-interior angles in ratio 2:3. Find smaller angle."""
    seed = rng.randint(1, 1_000_000)
    # 2k + 3k = 180 => 5k = 180 => k = 36 => angles are 72 and 108
    smaller = 72
    svg = draw_parallel_transversal_svg({"G4": "72°", "H2": "108°"}, seed=seed)

    return {
        "subskill": "40_parallel_lines_ratio_cointerior_angles",
        "question_text": (
            f"Two co-interior angles on parallel lines ($AB \\parallel CD$) are in the ratio $2 : 3$.\n\n"
            f"Calculate the size of the **smaller** co-interior angle in degrees:"
        ),
        "correct_answer": str(smaller),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Set up ratio equation: 2k + 3k = 180 => 5k = 180 => k = 36°", "marks": 1},
            {"step": f"Calculate smaller angle: 2 * 36° = {smaller}°", "marks": 1},
        ],
        "hints": [
            "Co-interior angles add up to $180^\\circ$ [co-int $\\angle$s, $AB \\parallel CD$].",
            "Let the angles be $2k$ and $3k$: $2k + 3k = 180^\\circ \\implies 5k = 180^\\circ \\implies k = 36^\\circ$.",
            f"The smaller angle is $2 \\times 36^\\circ = {smaller}^\\circ$.",
        ],
    }


def arch_41_adjacent_angles_straight_line_ratio(rng: random.Random) -> Dict[str, Any]:
    """Adjacent angles on straight line in ratio 1:3. Find smaller angle."""
    seed = rng.randint(1, 1_000_000)
    # 1k + 3k = 180 => 4k = 180 => k = 45
    ans = 45
    svg = draw_straight_line_adjacent_angles_svg("45°", "135°", seed=seed)

    return {
        "subskill": "41_adjacent_angles_straight_line_ratio",
        "question_text": (
            f"Two adjacent angles on a straight line are in the ratio $1 : 3$.\n\n"
            f"Calculate the size of the **smaller** angle in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Set up equation: k + 3k = 180 => 4k = 180", "marks": 1},
            {"step": f"Solve: k = {ans}°", "marks": 1},
        ],
        "hints": [
            "Angles on a straight line sum to $180^\\circ$: $k + 3k = 180^\\circ$.",
            "$4k = 180^\\circ \\implies k = 45^\\circ$.",
            f"The smaller angle is ${ans}^\\circ$.",
        ],
    }


def arch_42_algebraic_system_two_variables_transversal(rng: random.Random) -> Dict[str, Any]:
    """System on parallel lines: 2x + 10 = 70 => x = 30."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 25, 30])
    angle_val = 2 * x_val + 10
    svg = draw_parallel_transversal_svg({"G4": f"2x + 10°", "H1": f"{angle_val}°"}, seed=seed)

    return {
        "subskill": "42_algebraic_system_two_variables_transversal",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"If alternate interior angles are $\\hat{{G}}_4 = (2x + 10)^\\circ$ and $\\hat{{H}}_1 = {angle_val}^\\circ$, "
            f"calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Equate: 2x + 10 = {angle_val} [alt ∠s, AB || CD]", "marks": 1},
            {"step": f"Solve: 2x = {angle_val - 10} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Set alternate angles equal: $2x + 10 = {angle_val}$.",
            f"$2x = {angle_val - 10}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_43_converse_test_determine_if_lines_are_parallel(rng: random.Random) -> Dict[str, Any]:
    """Converse check: calculate required angle to make lines parallel."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([54, 62, 73, 85])
    svg = draw_parallel_transversal_svg({"G2": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "43_converse_test_determine_if_lines_are_parallel",
        "question_text": (
            f"In the diagram below, transversal $EF$ crosses lines $AB$ and $CD$.\n\n"
            f"Angle $\\hat{{G}}_2 = {theta}^\\circ$. What exact size must corresponding angle $x$ be (in degrees) "
            f"to guarantee that line $AB$ is parallel to line $CD$?"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State required angle: x = {theta}° [converse corresp ∠s =]", "marks": 1},
        ],
        "hints": [
            "For two lines to be parallel, their corresponding angles must be equal.",
            f"Therefore, angle $x$ must equal ${theta}^\\circ$.",
            f"The value is ${theta}$.",
        ],
    }


def arch_44_formal_euclidean_proof_step_vert_opp_transversal(rng: random.Random) -> Dict[str, Any]:
    """Two-step proof: G2 = theta => H4 = theta."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([55, 65, 75])
    svg = draw_parallel_transversal_svg({"G2": f"{theta}°", "H4": "x"}, seed=seed)

    return {
        "subskill": "44_formal_euclidean_proof_step_vert_opp_transversal",
        "question_text": (
            f"In the diagram below, $AB \\parallel CD$.\n\n"
            f"Given $\\hat{{G}}_2 = {theta}^\\circ$, calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Find corresponding angle H2 = {theta}° [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Find vertically opposite angle x = {theta}° [vert opp ∠s]", "marks": 1},
        ],
        "hints": [
            f"$\\hat{{H}}_2 = \\hat{{G}}_2 = {theta}^\\circ$ [corresp $\\angle$s, $AB \\parallel CD$].",
            f"Angle $x$ is vertically opposite to $\\hat{{H}}_2$, so $x = {theta}^\\circ$.",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_45_parallel_lines_exterior_alternate_angles(rng: random.Random) -> Dict[str, Any]:
    """Exterior alternate angles: G1 = H4 = theta."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([48, 57, 66, 75])
    svg = draw_parallel_transversal_svg({"G1": f"{theta}°", "H4": "x"}, seed=seed)

    return {
        "subskill": "45_parallel_lines_exterior_alternate_angles",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Exterior alternate angles are $\\hat{{G}}_1 = {theta}^\\circ$ and $\\hat{{H}}_4 = x$ as shown below.\n"
            f"Calculate the value of angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State exterior alternate angle equality: x = {theta}°", "marks": 1},
        ],
        "hints": [
            f"Angle $\\hat{{G}}_4$ is vertically opposite to $\\hat{{G}}_1$, so $\\hat{{G}}_4 = {theta}^\\circ$.",
            f"Angle $x$ is alternate to $\\hat{{G}}_4$, so $x = {theta}^\\circ$.",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_46_straight_line_adjacent_angles_with_algebraic_fractions(rng: random.Random) -> Dict[str, Any]:
    """Solve x/2 + 20 + x/3 + 10 = 180 => 5x/6 = 150 => x = 180."""
    seed = rng.randint(1, 1_000_000)
    x_val = 180
    svg = draw_straight_line_adjacent_angles_svg("x/2 + 20°", "x/3 + 10°", seed=seed)

    return {
        "subskill": "46_straight_line_adjacent_angles_with_algebraic_fractions",
        "question_text": (
            f"In the diagram below, $AB$ is a straight line.\n\n"
            f"The two adjacent angles are given by $(\\frac{{x}}{{2}} + 20)^\\circ$ and $(\\frac{{x}}{{3}} + 10)^\\circ$.\n"
            f"Calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Set up equation: (x/2 + 20) + (x/3 + 10) = 180 [∠s on a str line]", "marks": 1},
            {"step": "Multiply by LCD = 6: 3x + 120 + 2x + 60 = 1080 => 5x = 900", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Adjacent angles on a straight line sum to $180^\\circ$: $\\frac{x}{2} + 20 + \\frac{x}{3} + 10 = 180$.",
            "Combine constants: $\\frac{x}{2} + \\frac{x}{3} = 150$. Multiply by $6$: $3x + 2x = 900$.",
            f"$5x = 900 \\implies x = {x_val}$.",
        ],
    }


def arch_47_parallel_lines_cointerior_fractions(rng: random.Random) -> Dict[str, Any]:
    """Co-interior angles with fractions: x/2 + 15 + x/4 + 45 = 180 => 3x/4 = 120 => x = 160."""
    seed = rng.randint(1, 1_000_000)
    x_val = 160
    svg = draw_parallel_transversal_svg({"G4": "x/2 + 15°", "H2": "x/4 + 45°"}, seed=seed)

    return {
        "subskill": "47_parallel_lines_cointerior_fractions",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Co-interior angles are $(\\frac{{x}}{{2}} + 15)^\\circ$ and $(\\frac{{x}}{{4}} + 45)^\\circ$.\n"
            f"Calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Set up equation: (x/2 + 15) + (x/4 + 45) = 180 [co-int ∠s, AB || CD]", "marks": 1},
            {"step": "Multiply by LCD = 4: 2x + 60 + x + 180 = 720 => 3x = 480", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Co-interior angles sum to $180^\\circ$: $(\\frac{x}{2} + 15) + (\\frac{x}{4} + 45) = 180$.",
            "Multiply every term by $4$: $2x + 60 + x + 180 = 720 \\implies 3x = 480$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_48_real_world_context_railway_track_transversal(rng: random.Random) -> Dict[str, Any]:
    """Railway track context: two parallel rails crossed by road."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([62, 68, 74, 80])
    ans = 180 - theta
    svg = draw_parallel_transversal_svg({"G4": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "48_real_world_context_railway_track_transversal",
        "question_text": (
            f"A straight road crosses a set of two parallel railway tracks ($AB \\parallel CD$).\n\n"
            f"The angle between the road and the first rail is ${theta}^\\circ$ as shown in the diagram below.\n"
            f"Calculate the size of the co-interior angle $x$ (in degrees) formed with the second rail:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State co-interior relation: {theta}° + x = 180° [co-int ∠s, AB || CD]", "marks": 1},
            {"step": f"Calculate x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            f"Because the two rails are parallel, the angles on the same side of the road between the rails are co-interior: ${theta}^\\circ + x = 180^\\circ$.",
            f"$x = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_49_real_world_context_bridge_truss_parallel_struts(rng: random.Random) -> Dict[str, Any]:
    """Bridge truss: parallel top and bottom chords crossed by diagonal strut."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([38, 45, 52, 60])
    svg = draw_parallel_transversal_svg({"G4": f"{theta}°", "H1": "x"}, seed=seed)

    return {
        "subskill": "49_real_world_context_bridge_truss_parallel_struts",
        "question_text": (
            f"A steel railway bridge truss consists of two horizontal parallel steel beams ($AB \\parallel CD$).\n\n"
            f"A diagonal support strut connects the beams, making an angle of ${theta}^\\circ$ with the top beam.\n"
            f"Calculate the size of the alternate angle $x$ (in degrees) that the strut makes with the bottom beam:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Identify alternate interior angles: x = {theta}° [alt ∠s, AB || CD]", "marks": 1},
        ],
        "hints": [
            "The diagonal strut acts as a transversal between the two parallel beams.",
            f"The angles form a Z-shape and are alternate interior angles: $x = {theta}^\\circ$.",
        ],
    }


def arch_50_compound_multi_line_geometric_synthesis(rng: random.Random) -> Dict[str, Any]:
    """Synthesis challenge: multi-angle chain on parallel lines."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([65, 70, 75, 80])
    ans = 180 - theta
    svg = draw_parallel_transversal_svg({"G1": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "50_compound_multi_line_geometric_synthesis",
        "question_text": (
            f"In the geometric network below, lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Given exterior angle $\\hat{{G}}_1 = {theta}^\\circ$, deduce the size of angle $x$ in degrees "
            f"by combining two geometric theorems:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Deduce H1 = {theta}° [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Calculate x = 180° - {theta}° = {ans}° [∠s on a str line]", "marks": 1},
        ],
        "hints": [
            f"Step 1: Corresponding angle $\\hat{{H}}_1 = \\hat{{G}}_1 = {theta}^\\circ$ [corresp $\\angle$s, $AB \\parallel CD$].",
            f"Step 2: Angles $\\hat{{H}}_1$ and $x$ lie on straight line $CD$: $\\hat{{H}}_1 + x = 180^\\circ$.",
            f"$x = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }
