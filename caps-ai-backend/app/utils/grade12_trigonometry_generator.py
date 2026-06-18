import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed if seed is not None else 0)


def _make_id(prefix: str, rng: random.Random) -> str:
    return f"{prefix}_{rng.randint(100000, 999999)}"


def _make_unique_options(rng: random.Random, correct: str, candidates: List[str], target: int = 4) -> List[str]:
    opts: List[str] = [str(correct)]
    for c in candidates:
        if len(opts) >= target:
            break
        c = str(c)
        if c not in opts:
            opts.append(c)

    while len(opts) < target:
        opts.append(str(correct))
        opts = list(dict.fromkeys(opts))

    opts = opts[:target]
    rng.shuffle(opts)
    return opts


def _make_typed(*, rng: random.Random, prompt: str, correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        "id": _make_id("trig", rng),
        "topic": "grade12_trigonometry",
        "question_type": "typed",
        "question": prompt,
        "correct_answer": str(correct_answer),
        "explanation": explanation,
        **extra,
    }


def _make_mcq(*, rng: random.Random, prompt: str, options: List[str], correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        "id": _make_id("trig", rng),
        "topic": "grade12_trigonometry",
        "question_type": "mcq",
        "question": prompt,
        "options": options,
        "correct_answer": str(correct_answer),
        "explanation": explanation,
        **extra,
    }


def _make_scaffold(
    *,
    rng: random.Random,
    prompt: str,
    steps: List[str],
    checkpoints: List[Dict[str, Any]],
    final_answer: str,
    explanation: str,
    **extra,
) -> Dict[str, Any]:
    return {
        "id": _make_id("trig", rng),
        "topic": "grade12_trigonometry",
        "question_type": "scaffold",
        "question": prompt,
        "steps": steps,
        "checkpoints": checkpoints,
        "correct_answer": str(final_answer),
        "explanation": explanation,
        **extra,
    }


def _validate_question(q: Dict[str, Any]) -> None:
    required = {"id", "topic", "subskill", "difficulty", "question_type", "question", "correct_answer", "explanation"}
    missing = [k for k in required if k not in q]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

    if q["question_type"] not in {"typed", "mcq", "scaffold"}:
        raise ValueError("Invalid question_type")

    if q["question_type"] == "mcq":
        if not isinstance(q.get("options"), list) or len(q.get("options", [])) < 2:
            raise ValueError("MCQ must include options list")
        if str(q["correct_answer"]) not in [str(o) for o in q.get("options", [])]:
            raise ValueError("MCQ correct_answer must be one of options")

    if q["question_type"] == "scaffold":
        if not isinstance(q.get("steps"), list) or len(q.get("steps", [])) < 1:
            raise ValueError("Scaffold must include steps")
        if not isinstance(q.get("checkpoints"), list) or len(q.get("checkpoints", [])) < 1:
            raise ValueError("Scaffold must include checkpoints")


_SPECIAL_EXACT = {
    0: {"sin": "0", "cos": "1", "tan": "0"},
    30: {"sin": "1/2", "cos": "√3/2", "tan": "1/√3"},
    45: {"sin": "1/√2", "cos": "1/√2", "tan": "1"},
    60: {"sin": "√3/2", "cos": "1/2", "tan": "√3"},
    90: {"sin": "1", "cos": "0", "tan": "undef"},
}


def _reduce_angle_to_ref(deg: int) -> Dict[str, Any]:
    a = deg % 360
    if 0 <= a < 90:
        return {"quadrant": 1, "ref": a}
    if 90 < a < 180:
        return {"quadrant": 2, "ref": 180 - a}
    if 180 < a < 270:
        return {"quadrant": 3, "ref": a - 180}
    if 270 < a < 360:
        return {"quadrant": 4, "ref": 360 - a}
    if a in {90, 180, 270, 0}:
        return {"quadrant": 0, "ref": a}
    return {"quadrant": 0, "ref": a}


def _sign_for(q: int, fn: str) -> str:
    if q == 1:
        return "+"
    if q == 2:
        return "+" if fn == "sin" else "-"
    if q == 3:
        return "+" if fn == "tan" else "-"
    if q == 4:
        return "+" if fn == "cos" else "-"
    return "+"


def _subskill_reduction_to_A(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Based on: Given sin 31° = A, write other ratios in terms of A.
    # We'll keep it deterministic and symbolic.
    base_angle = rng.choice([13, 17, 23, 29, 31, 37])
    fn_base = rng.choice(["sin", "cos"])
    A = "A"

    # Pick a target transform that is standard in the doc: 180±θ, 360±θ, -θ, 90±θ
    transforms = [
        ("sin", 180 - base_angle, f"sin {180 - base_angle}°"),
        ("cos", -(90 - base_angle), f"cos({-(90 - base_angle)}°)"),
        ("cos", 360 - (base_angle), f"cos {360 - base_angle}°"),
        ("tan", 180 + base_angle, f"tan {180 + base_angle}°"),
        ("tan", base_angle, f"tan {base_angle}°"),
    ]
    fn, angle, label = rng.choice(transforms)

    given = f"{fn_base} {base_angle}° = {A}"

    # We will express in terms of A using co-function + sign rules.
    # To keep the engine simple/deterministic: we use known identities and leave sqrt form.
    # If given is sin θ = A, then cos θ = ±√(1-A^2).
    # If given is cos θ = A, then sin θ = ±√(1-A^2).
    if fn_base == "sin":
        cos_theta = "±√(1-A^2)"
        tan_theta = "A/(±√(1-A^2))"
    else:
        cos_theta = "A"
        tan_theta = "(±√(1-A^2))/A"

    if fn_base == "sin":
        base_sin = "A"
        base_cos = cos_theta
    else:
        base_cos = "A"
        base_sin = "±√(1-A^2)"

    # Apply reduction for the selected expression
    red = _reduce_angle_to_ref(angle)
    ref = red["ref"]
    quadrant = red["quadrant"]

    # choose expression in terms of base angle when possible
    # if ref == base_angle then we can directly map; otherwise leave as ref reduction statement.
    sign = _sign_for(quadrant, fn) if quadrant != 0 else "+"

    if ref == base_angle:
        if fn == "sin":
            expr = base_sin
        elif fn == "cos":
            expr = base_cos
        else:
            expr = tan_theta if fn_base == "sin" else "(±√(1-A^2))/A"
        answer = expr if sign == "+" else f"-{expr}"
        explanation = "Use reduction formulae (CAST) to write the angle in terms of the reference angle, then use sin^2θ+cos^2θ=1."  # noqa: E501
    else:
        answer = f"{sign} {fn} {ref}°"
        explanation = "First reduce to the reference angle using CAST (sign) and co-function rules if needed."  # noqa: E501

    prompt = f"Given: {given}. Write {label} in terms of A."

    if qtype == "mcq":
        options = _make_unique_options(rng, str(answer), [str(A), str(base_sin), str(base_cos)])
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=str(answer),
            explanation=explanation,
            subskill="reduction_in_terms_of_A",
            difficulty=difficulty,
        )

    if qtype == "scaffold":
        checkpoints = [
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "State the reference angle (in degrees):",
                "correct_answer": str(ref),
                "explanation": "Use the nearest axis and subtract from 180°/360° as needed.",
            },
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "State the sign of the ratio using CAST (+ or -):",
                "correct_answer": str(sign),
                "explanation": "Use quadrant sign rules (CAST).",
            },
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "Write the final answer in terms of A:",
                "correct_answer": str(answer),
                "explanation": explanation,
            },
        ]
        steps = [
            "Reduce the angle to a reference angle in [0°,90°].",
            "Determine the sign from the quadrant (CAST).",
            "Use sin^2θ+cos^2θ=1 if you need the co-function in terms of A.",
        ]
        return _make_scaffold(
            rng=rng,
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=str(answer),
            explanation=explanation,
            subskill="reduction_in_terms_of_A",
            difficulty=difficulty,
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=str(answer),
        explanation=explanation,
        subskill="reduction_in_terms_of_A",
        difficulty=difficulty,
    )


def _subskill_eval_special_angles(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Evaluate a reduced exact value (no calculator), similar to doc examples.
    fn = rng.choice(["sin", "cos", "tan"])
    base = rng.choice([30, 45, 60])
    k = rng.choice([0, 1, 2])
    variant = rng.choice(["360+", "360-", "180+", "180-", "-"])

    if variant == "360+":
        angle = 360 * (k + 1) + base
        ref = base
        quadrant = 1
    elif variant == "360-":
        angle = 360 * (k + 1) - base
        ref = base
        quadrant = 4
    elif variant == "180+":
        angle = 180 + base
        ref = base
        quadrant = 3
    elif variant == "180-":
        angle = 180 - base
        ref = base
        quadrant = 2
    else:
        angle = -base
        ref = base
        quadrant = 0

    sign = _sign_for(quadrant, fn) if quadrant != 0 else ("-" if fn in {"sin", "tan"} else "+")
    exact = _SPECIAL_EXACT[ref][fn]

    if exact == "undef":
        answer = "undef"
    else:
        answer = exact if sign == "+" else f"-{exact}"

    prompt = f"Evaluate without using a calculator: {fn}({angle}°)"
    explanation = "Use reduction formulae to a special angle (30°,45°,60°) and apply CAST for the sign."  # noqa: E501

    if qtype == "mcq":
        candidates = [exact, f"-{exact}", "0", "1"]
        options = _make_unique_options(rng, str(answer), candidates)
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=str(answer),
            explanation=explanation,
            subskill="evaluate_special_angles",
            difficulty=difficulty,
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=str(answer),
        explanation=explanation,
        subskill="evaluate_special_angles",
        difficulty=difficulty,
    )


def _subskill_compound_expand(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Expand using compound angle formulae.
    fn = rng.choice(["sin", "cos"])
    a = rng.choice(["α", "theta", "x"]).replace("theta", "θ")
    b = rng.choice(["β", "phi", "y"]).replace("phi", "φ")
    op = rng.choice(["+", "-"])

    if fn == "cos" and op == "-":
        answer = f"cos {a} cos {b} + sin {a} sin {b}"
        label = f"cos({a} - {b})"
    elif fn == "cos" and op == "+":
        answer = f"cos {a} cos {b} - sin {a} sin {b}"
        label = f"cos({a} + {b})"
    elif fn == "sin" and op == "-":
        answer = f"sin {a} cos {b} - cos {a} sin {b}"
        label = f"sin({a} - {b})"
    else:
        answer = f"sin {a} cos {b} + cos {a} sin {b}"
        label = f"sin({a} + {b})"

    prompt = f"Expand using compound angle identities: {label}"
    explanation = "Apply the standard compound-angle identity for sin/cos of a sum/difference."  # noqa: E501

    if qtype == "mcq":
        wrong_1 = answer.replace("+", "±")
        wrong_2 = answer.replace("+", "-") if "+" in answer else answer.replace("-", "+")
        wrong_3 = f"{label}"
        options = _make_unique_options(rng, answer, [wrong_1, wrong_2, wrong_3])
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=answer,
            explanation=explanation,
            subskill="compound_angle_expand",
            difficulty=difficulty,
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=answer,
        explanation=explanation,
        subskill="compound_angle_expand",
        difficulty=difficulty,
    )


def _subskill_identity_simplify(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Simplify to a single ratio, aligned to the doc style.
    variant = rng.choice(["tan_in_terms", "p_to_single", "cos_over_1_plus_sin"]) 

    if variant == "tan_in_terms":
        prompt = "Simplify to a single trigonometric ratio: sin θ / cos θ"
        answer = "tan θ"
        explanation = "Use tanθ = sinθ/cosθ (cosθ ≠ 0)."
    elif variant == "cos_over_1_plus_sin":
        prompt = "Simplify: cos θ / (1 + sin θ)"
        answer = "(1 - sin θ)/cos θ"
        explanation = "Multiply numerator and denominator by (1 - sinθ) and use 1 - sin^2θ = cos^2θ."  # noqa: E501
    else:
        prompt = "Simplify: tan^2 θ + (cos^2 θ - 1)/cos^2 θ"
        answer = "0"
        explanation = "Since (cos^2θ - 1)/cos^2θ = -sin^2θ/cos^2θ = -tan^2θ, they cancel."  # noqa: E501

    if qtype == "mcq":
        options = _make_unique_options(rng, answer, ["1", "tan θ", "sec^2 θ", "-tan θ"])
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=answer,
            explanation=explanation,
            subskill="identity_simplify",
            difficulty=difficulty,
        )

    if qtype == "scaffold":
        checkpoints = [
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "State the identity you will use:",
                "correct_answer": "tanθ = sinθ/cosθ" if "sin θ / cos θ" in prompt else "sin^2θ + cos^2θ = 1",
                "explanation": "Pick a standard identity to rewrite the expression.",
            },
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "Write the simplified final answer:",
                "correct_answer": str(answer),
                "explanation": explanation,
            },
        ]
        steps = ["Rewrite using identities.", "Simplify algebraically.", "State restrictions if relevant."]
        return _make_scaffold(
            rng=rng,
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=str(answer),
            explanation=explanation,
            subskill="identity_simplify",
            difficulty=difficulty,
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=str(answer),
        explanation=explanation,
        subskill="identity_simplify",
        difficulty=difficulty,
    )


SUBSKILLS = {
    "reduction_in_terms_of_A": _subskill_reduction_to_A,
    "evaluate_special_angles": _subskill_eval_special_angles,
    "identity_simplify": _subskill_identity_simplify,
    "compound_angle_expand": _subskill_compound_expand,
}


def list_subskills() -> List[str]:
    return sorted(SUBSKILLS.keys())


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)

    if not isinstance(count, int):
        try:
            count = int(count)
        except Exception:
            count = 1

    n_questions = max(1, min(20, count))

    if subskill and subskill != "mixed" and subskill not in SUBSKILLS:
        raise ValueError(f"Unknown subskill: {subskill}. Available: {list_subskills()}")

    out: List[Dict[str, Any]] = []
    keys = list_subskills()

    for i in range(n_questions):
        sk = subskill
        if not sk or sk == "mixed":
            sk = keys[i % len(keys)]

        qtype = question_type
        if qtype in {None, "mixed"}:
            qtype = "mcq" if (i % 3 == 2) else "typed"

        q_rng = _rng((seed or 0) + 10009 * (i + 1))
        q = SUBSKILLS[sk](q_rng, difficulty, qtype)
        q["subskill"] = sk
        q["difficulty"] = difficulty
        _validate_question(q)
        out.append(q)

    return out
