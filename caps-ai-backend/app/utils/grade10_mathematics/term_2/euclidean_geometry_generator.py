"""Grade 10 Mathematics - Term 2 - Euclidean Geometry (deterministic, SymPy-backed).

Curriculum source: ``curriculum_docs/Mathematics_Gr10/Term 2/Euclidean Geometry_1.md``.

Euclidean Geometry is a highly visual topic. Every figure is a structured **Diagram Spec**
rather than an image, and marking compares structured values (angles, side lengths,
vertex labels) -- never pixels.

Subskills:
    angle_types              mcq      Identify angle types (acute, obtuse, etc.)
    angle_calculate          math_short  Calculate missing angles on straight line / around point
    parallel_transversal     math_short  Calculate angles formed by parallel lines and transversal
    triangle_angles          math_short  Triangle angle sum and exterior angles
    isosceles_base           math_short  Isosceles triangle base angles
    congruency               mcq      Identify congruency rule (RHS, SSS, SAS, AAS)
    similarity               mcq/mc   Identify similarity rule or calculate using proportions
    pythagoras               math_short  Calculate missing side using Pythagoras
    parallelogram_props      math_short  Calculate angles/sides in parallelograms
    special_quads            mcq      Identify properties of special quadrilaterals
    midpoint_theorem         math_short  Apply mid-point theorem

All answers are computed; given a seed the output is byte-identical.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from app.utils.grade10_mathematics import _diagram
from app.utils.grade10_mathematics._math_common import (
    build_generate,
    make_mcq,
    make_short,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_euclidean_geometry"
LO = "math10_euclidean_geometry"


def _rng(seed: Any = None) -> random.Random:
    """Return a seeded random.Random instance."""
    if seed is None:
        return random.Random()
    return random.Random(seed)


# --------------------------------------------------------------------------- #
# 1. Angle types (MCQ)
# --------------------------------------------------------------------------- #
def _build_angle_types(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Identify angle types: acute, obtuse, right, straight, reflex."""
    angle_types = [
        ("acute", "An angle between 0\u00b0 and 90\u00b0"),
        ("right", "An angle exactly equal to 90\u00b0"),
        ("obtuse", "An angle between 90\u00b0 and 180\u00b0"),
        ("straight", "An angle exactly equal to 180\u00b0"),
        ("reflex", "An angle between 180\u00b0 and 360\u00b0"),
    ]
    correct_type, description = r.choice(angle_types)
    distractors = [t for t, _ in angle_types if t != correct_type]
    options = [correct_type] + r.sample(distractors, 3)
    r.shuffle(options)
    angle_val = {
        "acute": r.randint(15, 75),
        "right": 90,
        "obtuse": r.randint(100, 170),
        "straight": 180,
        "reflex": r.randint(190, 350),
    }[correct_type]
    return with_metadata(
        make_mcq(
            prefix="eg_atypes",
            prompt=f"What type of angle is {angle_val}\u00b0?",
            choices=options,
            answer=correct_type,
            explanation=f"{angle_val}\u00b0 is {description}.",
        ),
        topic=TOPIC,
        subskill="angle_types",
        learning_objective_id=LO,
    )


# --------------------------------------------------------------------------- #
# 2. Angle calculate (math_short)
# --------------------------------------------------------------------------- #
def _build_angle_calculate(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Calculate missing angles on a straight line or around a point."""
    if r.choice([True, False]):
        # Straight line: two adjacent angles sum to 180
        a = r.randint(30, 150)
        b = 180 - a
        prompt = f"Two adjacent angles on a straight line are shown. One angle is {a}\u00b0. Calculate the other angle."
        answer = str(b)
        explanation = f"Angles on a straight line sum to 180\u00b0. {180}\u00b0 - {a}\u00b0 = {b}\u00b0."
        diagram = _diagram.angle_diagram(
            vertex="O",
            arms=["OA", "OB", "OC"],
            angle_value=float(a),
            angle_label=f"{a}\u00b0",
            supplementary_angles=[{"vertex": "O", "value": float(b), "label": f"{b}\u00b0"}],
        )
    else:
        # Around a point: three or four angles sum to 360
        a = r.randint(50, 120)
        b = r.randint(50, 120)
        c = r.randint(50, 120)
        d = 360 - a - b - c
        prompt = f"Three angles around a point are {a}\u00b0, {b}\u00b0 and {c}\u00b0. Calculate the fourth angle."
        answer = str(d)
        explanation = f"Angles around a point sum to 360\u00b0. {360}\u00b0 - {a}\u00b0 - {b}\u00b0 - {c}\u00b0 = {d}\u00b0."
        diagram = None
    q = make_short(
        prefix="eg_acalc",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    if diagram:
        q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="angle_calculate", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 3. Parallel lines and transversal (math_short)
# --------------------------------------------------------------------------- #
def _build_parallel_transversal(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Calculate angles using parallel-line properties."""
    given = r.randint(40, 140)
    # Alternate interior angle is equal
    if r.choice([True, False]):
        prompt = f"AB \u2225 CD and EF is a transversal. If one alternate interior angle is {given}\u00b0, what is the other alternate interior angle?"
        answer = str(given)
        explanation = f"Alternate interior angles are equal when lines are parallel. The answer is {given}\u00b0."
    # Corresponding angle is equal
    elif r.choice([True, False]):
        prompt = f"AB \u2225 CD and EF is a transversal. If one corresponding angle is {given}\u00b0, what is the other corresponding angle?"
        answer = str(given)
        explanation = f"Corresponding angles are equal when lines are parallel. The answer is {given}\u00b0."
    # Co-interior angles are supplementary
    else:
        answer_val = 180 - given
        prompt = f"AB \u2225 CD and EF is a transversal. If one co-interior angle is {given}\u00b0, what is the other co-interior angle?"
        answer = str(answer_val)
        explanation = f"Co-interior angles are supplementary (sum to 180\u00b0) when lines are parallel. {180}\u00b0 - {given}\u00b0 = {answer_val}\u00b0."
    diagram = _diagram.parallel_transversal(
        line1_label="AB",
        line2_label="CD",
        transversal_label="EF",
        given_angle=float(given),
        given_position=r.choice(["top_left_interior", "top_right_interior", "bottom_left_interior", "bottom_right_interior"]),
    )
    q = make_short(
        prefix="eg_pl",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="parallel_transversal", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 4. Triangle angles (math_short)
# --------------------------------------------------------------------------- #
def _build_triangle_angles(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Triangle angle sum and exterior angle theorem."""
    A = r.randint(30, 80)
    B = r.randint(30, 80)
    C = 180 - A - B
    if r.choice([True, False]):
        # Given two angles, find third
        prompt = f"In \u25b3ABC, angle A = {A}\u00b0 and angle B = {B}\u00b0. Calculate angle C."
        answer = str(C)
        explanation = f"Sum of angles in a triangle = 180\u00b0. {180}\u00b0 - {A}\u00b0 - {B}\u00b0 = {C}\u00b0."
    else:
        # Exterior angle theorem
        ext = A + B
        prompt = f"In \u25b3ABC, angle A = {A}\u00b0 and angle B = {B}\u00b0. Calculate the exterior angle at C."
        answer = str(ext)
        explanation = f"Exterior angle = sum of opposite interior angles. {A}\u00b0 + {B}\u00b0 = {ext}\u00b0."
    diagram = _diagram.triangle(
        vertices=["A", "B", "C"],
        points={"A": [0.0, 0.0], "B": [4.0, 0.0], "C": [2.5, 3.0]},
        angle_values={"A": float(A), "B": float(B), "C": float(C)},
        angle_labels={"A": f"{A}\u00b0", "B": f"{B}\u00b0"},
    )
    q = make_short(
        prefix="eg_tang",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="triangle_angles", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 5. Isosceles base angles (math_short)
# --------------------------------------------------------------------------- #
def _build_isosceles_base(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Isosceles triangle: base angles are equal."""
    apex = r.randint(40, 100)
    base = (180 - apex) // 2
    if r.choice([True, False]):
        prompt = f"In isosceles \u25b3ABC with AB = AC, the angle at A is {apex}\u00b0. Calculate each base angle."
        answer = str(base)
        explanation = f"Base angles of an isosceles triangle are equal. ({180}\u00b0 - {apex}\u00b0) / 2 = {base}\u00b0."
    else:
        prompt = f"In isosceles \u25b3ABC with AB = AC, one base angle is {base}\u00b0. Calculate the angle at A."
        answer = str(apex)
        explanation = f"Base angles are equal, so 2 \u00d7 {base}\u00b0 + angle A = 180\u00b0. Angle A = {apex}\u00b0."
    diagram = _diagram.triangle(
        vertices=["A", "B", "C"],
        points={"A": [2.0, 3.0], "B": [0.0, 0.0], "C": [4.0, 0.0]},
        equal_sides=[["AB", "AC"]],
        angle_values={"A": float(apex), "B": float(base), "C": float(base)},
        angle_labels={"A": f"{apex}\u00b0"},
    )
    q = make_short(
        prefix="eg_iso",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="isosceles_base", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 6. Congruency (MCQ)
# --------------------------------------------------------------------------- #
def _build_congruency(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Identify the congruency rule."""
    rules = [
        ("RHS", "Right angle, Hypotenuse, Side"),
        ("SSS", "Side, Side, Side"),
        ("SAS", "Side, Angle, Side (included angle)"),
        ("AAS", "Angle, Angle, Side"),
    ]
    correct, desc = r.choice(rules)
    distractors = [rule for rule, _ in rules if rule != correct]
    options = [correct] + r.sample(distractors, 3)
    r.shuffle(options)
    scenarios = {
        "RHS": "two right-angled triangles with equal hypotenuse and one equal side",
        "SSS": "two triangles with all three corresponding sides equal",
        "SAS": "two triangles with two corresponding sides equal and the included angles equal",
        "AAS": "two triangles with two corresponding angles equal and one corresponding side equal",
    }
    prompt = f"Which congruency rule applies when {scenarios[correct]}?"
    return with_metadata(
        make_mcq(
            prefix="eg_cong",
            prompt=prompt,
            choices=options,
            answer=correct,
            explanation=f"{correct}: {desc}.",
        ),
        topic=TOPIC,
        subskill="congruency",
        learning_objective_id=LO,
    )


# --------------------------------------------------------------------------- #
# 7. Similarity (MCQ)
# --------------------------------------------------------------------------- #
def _build_similarity(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Identify similarity rule or calculate using proportions."""
    if r.choice([True, False]):
        rules = [
            ("AAA", "All three corresponding angles are equal"),
            ("SSS", "All three corresponding sides are in proportion"),
        ]
        correct, desc = r.choice(rules)
        distractors = [rule for rule, _ in rules if rule != correct] + ["SAS", "AAS"]
        options = [correct] + r.sample(distractors, 3)
        r.shuffle(options)
        prompt = f"Which similarity rule applies when {desc.lower()}?"
        return with_metadata(
            make_mcq(
                prefix="eg_sim",
                prompt=prompt,
                choices=options,
                answer=correct,
                explanation=f"{correct}: {desc}.",
            ),
            topic=TOPIC,
            subskill="similarity",
            learning_objective_id=LO,
        )
    else:
        # Calculate using proportion
        scale = r.choice([2, 3, 4])
        side_small = r.randint(3, 12)
        side_large = side_small * scale
        other_small = r.randint(3, 10)
        other_large = other_small * scale
        prompt = f"Two triangles are similar with scale factor {scale}. If one side of the smaller triangle is {side_small} cm, the corresponding side of the larger triangle is {side_large} cm. Another side of the smaller triangle is {other_small} cm. What is the corresponding side of the larger triangle?"
        answer = str(other_large)
        explanation = f"Corresponding sides are in proportion: {side_large}/{side_small} = {scale}. So {other_small} \u00d7 {scale} = {other_large} cm."
        return with_metadata(
            make_short(
                prefix="eg_sim_calc",
                prompt=prompt,
                answer=answer,
                explanation=explanation,
            ),
            topic=TOPIC,
            subskill="similarity",
            learning_objective_id=LO,
        )


# --------------------------------------------------------------------------- #
# 8. Pythagoras (math_short)
# --------------------------------------------------------------------------- #
def _build_pythagoras(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Calculate missing side using Pythagoras theorem."""
    a = r.randint(3, 12)
    b = r.randint(4, 12)
    c = math.isqrt(a * a + b * b)
    # Ensure it's a perfect square for clean answers
    while c * c != a * a + b * b:
        a = r.randint(3, 12)
        b = r.randint(4, 12)
        c = math.isqrt(a * a + b * b)
    if r.choice([True, False]):
        prompt = f"In right-angled \u25b3ABC with B = 90\u00b0, AB = {a} and BC = {b}. Calculate AC."
        answer = str(c)
        explanation = f"AC\u00b2 = AB\u00b2 + BC\u00b2 = {a}\u00b2 + {b}\u00b2 = {a*a + b*b}. AC = {c}."
    else:
        prompt = f"In right-angled \u25b3ABC with B = 90\u00b0, AC = {c} and AB = {a}. Calculate BC."
        answer = str(b)
        explanation = f"BC\u00b2 = AC\u00b2 - AB\u00b2 = {c}\u00b2 - {a}\u00b2 = {c*c - a*a}. BC = {b}."
    diagram = _diagram.triangle(
        vertices=["A", "B", "C"],
        points={"A": [0.0, 0.0], "B": [float(a), 0.0], "C": [float(a), float(b)]},
        side_labels={"AB": str(a), "BC": str(b), "AC": ""},
        right_angle_at="B",
    )
    q = make_short(
        prefix="eg_pyth",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="pythagoras", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 9. Parallelogram properties (math_short)
# --------------------------------------------------------------------------- #
def _build_parallelogram_props(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Calculate angles or sides in a parallelogram."""
    A = r.randint(50, 130)
    B = 180 - A
    if r.choice([True, False]):
        prompt = f"In parallelogram ABCD, angle A = {A}\u00b0. Calculate angle B."
        answer = str(B)
        explanation = f"Consecutive angles in a parallelogram are supplementary (sum to 180\u00b0). Angle B = {180}\u00b0 - {A}\u00b0 = {B}\u00b0."
    else:
        prompt = f"In parallelogram ABCD, angle A = {A}\u00b0. Calculate angle C."
        answer = str(A)
        explanation = f"Opposite angles in a parallelogram are equal. Angle C = angle A = {A}\u00b0."
    diagram = _diagram.quadrilateral(
        shape_type="parallelogram",
        vertices=["A", "B", "C", "D"],
        points={"A": [0.0, 0.0], "B": [4.0, 0.0], "C": [5.5, 2.5], "D": [1.5, 2.5]},
        angle_values={"A": float(A), "B": float(B), "C": float(A), "D": float(B)},
        angle_labels={"A": f"{A}\u00b0"},
        parallel_pairs=[["AB", "CD"], ["AD", "BC"]],
    )
    q = make_short(
        prefix="eg_para",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="parallelogram_props", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# 10. Special quadrilaterals (MCQ)
# --------------------------------------------------------------------------- #
def _build_special_quads(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Identify properties of special quadrilaterals."""
    questions = [
        (
            "Which quadrilateral has diagonals that bisect each other at right angles?",
            "rhombus",
            ["rectangle", "parallelogram", "trapezium"],
            "A rhombus has diagonals that bisect each other perpendicularly.",
        ),
        (
            "Which quadrilateral has all sides equal and all angles equal to 90\u00b0?",
            "square",
            ["rhombus", "rectangle", "kite"],
            "A square is both a rhombus (equal sides) and a rectangle (90\u00b0 angles).",
        ),
        (
            "Which quadrilateral has exactly one pair of opposite sides parallel?",
            "trapezium",
            ["parallelogram", "rectangle", "rhombus"],
            "A trapezium has one pair of opposite sides parallel.",
        ),
        (
            "Which quadrilateral has two pairs of adjacent sides equal?",
            "kite",
            ["parallelogram", "rectangle", "trapezium"],
            "A kite has two pairs of adjacent sides that are equal.",
        ),
        (
            "Which quadrilateral has diagonals that are equal in length?",
            "rectangle",
            ["rhombus", "parallelogram", "kite"],
            "The diagonals of a rectangle are equal in length.",
        ),
    ]
    prompt, correct, distractors, explanation = r.choice(questions)
    options = [correct] + r.sample(distractors, 3)
    r.shuffle(options)
    return with_metadata(
        make_mcq(
            prefix="eg_sq",
            prompt=prompt,
            choices=options,
            answer=correct,
            explanation=explanation,
        ),
        topic=TOPIC,
        subskill="special_quads",
        learning_objective_id=LO,
    )


# --------------------------------------------------------------------------- #
# 11. Mid-point theorem (math_short)
# --------------------------------------------------------------------------- #
def _build_midpoint_theorem(r: random.Random, difficulty: str) -> Dict[str, Any]:
    """Apply the mid-point theorem."""
    base = r.randint(8, 24)
    half = base // 2
    prompt = f"In \u25b3ABC, D and E are the mid-points of AB and AC respectively. If BC = {base}, calculate DE."
    answer = str(half)
    explanation = f"Mid-point theorem: DE = \u00bd BC = {base} / 2 = {half}."
    diagram = _diagram.triangle(
        vertices=["A", "B", "C"],
        points={"A": [2.0, 4.0], "B": [0.0, 0.0], "C": [6.0, 0.0]},
        side_labels={"BC": str(base)},
    )
    q = make_short(
        prefix="eg_mid",
        prompt=prompt,
        answer=answer,
        explanation=explanation,
    )
    q["diagram_spec"] = diagram
    return with_metadata(q, topic=TOPIC, subskill="midpoint_theorem", learning_objective_id=LO)


# --------------------------------------------------------------------------- #
# Dispatcher
# --------------------------------------------------------------------------- #
SUBSKILL_BUILDERS = {
    "angle_types": _build_angle_types,
    "angle_calculate": _build_angle_calculate,
    "parallel_transversal": _build_parallel_transversal,
    "triangle_angles": _build_triangle_angles,
    "isosceles_base": _build_isosceles_base,
    "congruency": _build_congruency,
    "similarity": _build_similarity,
    "pythagoras": _build_pythagoras,
    "parallelogram_props": _build_parallelogram_props,
    "special_quads": _build_special_quads,
    "midpoint_theorem": _build_midpoint_theorem,
}

generate = build_generate(SUBSKILL_BUILDERS, default_subskill="angle_types")
