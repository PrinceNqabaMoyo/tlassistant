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


def _pct(rate: float) -> str:
    return f"{rate * 100:.2f}%"


def _fmt_money(amount: float) -> str:
    return f"R {amount:,.2f}".replace(",", " ")


def _make_typed(*, rng: random.Random, prompt: str, correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        "id": _make_id("fin", rng),
        "topic": "grade12_finance",
        "question_type": "typed",
        "question": prompt,
        "correct_answer": str(correct_answer),
        "explanation": explanation,
        **extra,
    }


def _make_mcq(*, rng: random.Random, prompt: str, options: List[str], correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        "id": _make_id("fin", rng),
        "topic": "grade12_finance",
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
        "id": _make_id("fin", rng),
        "topic": "grade12_finance",
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


def _solve_for_n_compound(P: float, A: float, i_eff: float) -> float:
    if P <= 0 or A <= 0:
        raise ValueError("P and A must be positive")
    if i_eff <= -1:
        raise ValueError("Interest rate must be > -100%")
    return math.log(A / P) / math.log(1 + i_eff)


def _subskill_compound_solve_n(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == "easy":
        P = float(rng.choice([8000, 12000, 15000, 20000, 50000]))
        i = rng.choice([0.06, 0.075, 0.085, 0.09, 0.12])
        years = rng.choice([4, 5, 6, 7, 8, 10, 11])
    elif difficulty == "medium":
        P = float(rng.choice([2250, 7000, 15000, 80000, 120000]))
        i = rng.choice([0.0699, 0.0711, 0.095, 0.105, 0.12])
        years = rng.choice([9, 10, 11, 12, 15, 18])
    else:
        P = float(rng.choice([2100, 12000, 50000, 80000, 150000]))
        i = rng.choice([0.0595, 0.075, 0.0852, 0.09, 0.15])
        years = rng.choice([7, 9, 11, 13, 17, 21])

    A = P * ((1 + i) ** years)
    n = _solve_for_n_compound(P, A, i)

    prompt = (
        f"An amount of {_fmt_money(P)} is invested at {_pct(i)} per annum compounded annually. "
        f"It grows to {_fmt_money(A)}. Determine the time period n (in years)."
    )

    correct = f"{n:.2f}"
    explanation = "Use A = P(1+i)^n. Then n = log(A/P) / log(1+i)."

    if qtype == "mcq":
        candidates = [f"{(n + 1):.2f}", f"{(n - 1):.2f}", f"{(math.log(A / P) / (1 + i)):.2f}"]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            subskill="compound_solve_for_n",
            difficulty=difficulty,
            parameters={"P": P, "A": A, "i": i},
        )

    if qtype == "scaffold":
        checkpoints = [
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "Compute the ratio A/P:",
                "correct_answer": f"{(A / P):.6f}",
                "explanation": "Divide the accumulated amount by the principal.",
            },
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "Write the formula for n using logs (change of base):",
                "correct_answer": "log(A/P)/log(1+i)",
                "explanation": "n = log(A/P) / log(1+i).",
            },
            {
                "id": _make_id("cp", rng),
                "kind": "typed",
                "prompt": "Calculate n (years) to 2 decimals:",
                "correct_answer": correct,
                "explanation": explanation,
            },
        ]
        steps = ["Substitute into A = P(1+i)^n.", "Divide by P.", "Use logarithms to solve for n."]
        return _make_scaffold(
            rng=rng,
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=correct,
            explanation=explanation,
            subskill="compound_solve_for_n",
            difficulty=difficulty,
            parameters={"P": P, "A": A, "i": i},
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=correct,
        explanation=explanation,
        subskill="compound_solve_for_n",
        difficulty=difficulty,
        parameters={"P": P, "A": A, "i": i},
    )


def _subskill_nominal_effective_convert(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == "easy":
        i_nom = rng.choice([0.08, 0.09, 0.105, 0.12])
        m = rng.choice([2, 4, 12])
    elif difficulty == "medium":
        i_nom = rng.choice([0.0699, 0.0711, 0.0852, 0.095, 0.115])
        m = rng.choice([4, 12, 52])
    else:
        i_nom = rng.choice([0.06, 0.075, 0.085, 0.1055, 0.12])
        m = rng.choice([12, 52, 365])

    i_eff = (1 + i_nom / m) ** m - 1

    prompt = (
        f"A nominal interest rate of {_pct(i_nom)} p.a. is compounded {m} times per year. "
        f"Determine the effective annual interest rate i (as a percentage)."
    )

    correct = f"{i_eff * 100:.2f}%"
    explanation = "Use 1+i = (1 + i^(m)/m)^m. Then i = (1 + i^(m)/m)^m - 1."

    if qtype == "mcq":
        candidates = [
            f"{(i_nom * 100):.2f}%",
            f"{(i_nom / m * 100):.2f}%",
            f"{(i_eff * 100 + 0.5):.2f}%",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            subskill="nominal_to_effective",
            difficulty=difficulty,
            parameters={"i_nom": i_nom, "m": m},
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=correct,
        explanation=explanation,
        subskill="nominal_to_effective",
        difficulty=difficulty,
        parameters={"i_nom": i_nom, "m": m},
    )


def _subskill_future_value_annuity(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == "easy":
        x = float(rng.choice([200, 500, 750, 1000]))
        i = rng.choice([0.06, 0.08, 0.10])
        n = rng.choice([4, 5, 6, 8])
    elif difficulty == "medium":
        x = float(rng.choice([500, 700, 900, 1200]))
        i = rng.choice([0.075, 0.085, 0.095, 0.10])
        n = rng.choice([8, 10, 12, 15])
    else:
        x = float(rng.choice([700, 1000, 1500, 2000]))
        i = rng.choice([0.0852, 0.09, 0.105])
        n = rng.choice([12, 15, 18, 24])

    F = x * (((1 + i) ** n - 1) / i)

    prompt = (
        f"At the end of each year for {n} years, a deposit of {_fmt_money(x)} is made into an account. "
        f"The account earns {_pct(i)} p.a. compounded annually. Determine the future value F after {n} years."
    )

    correct = _fmt_money(F)
    explanation = "Use F = x((1+i)^n - 1)/i (future value of an annuity-immediate)."

    if qtype == "mcq":
        candidates = [
            _fmt_money(x * (1 + i) ** n),
            _fmt_money(x * n),
            _fmt_money(F * 0.9),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            subskill="future_value_annuity",
            difficulty=difficulty,
            parameters={"x": x, "i": i, "n": n},
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=correct,
        explanation=explanation,
        subskill="future_value_annuity",
        difficulty=difficulty,
        parameters={"x": x, "i": i, "n": n},
    )


def _subskill_payment_from_future_value(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == "easy":
        i = rng.choice([0.06, 0.08, 0.10])
        n = rng.choice([4, 5, 6, 8])
        F = float(rng.choice([5000, 8000, 12000, 20000]))
    elif difficulty == "medium":
        i = rng.choice([0.075, 0.085, 0.095])
        n = rng.choice([8, 10, 12, 15])
        F = float(rng.choice([25000, 40000, 60000, 80000]))
    else:
        i = rng.choice([0.0852, 0.09, 0.105])
        n = rng.choice([12, 15, 18, 24])
        F = float(rng.choice([100000, 150000, 200000, 300000]))

    x = (F * i) / ((1 + i) ** n - 1)

    prompt = (
        f"An amount of {_fmt_money(F)} is needed after {n} years. Deposits are made at the end of each year into an account "
        f"earning {_pct(i)} p.a. compounded annually. Determine the annual deposit x."
    )

    correct = _fmt_money(x)
    explanation = "Use x = Fi / ((1+i)^n - 1)."

    if qtype == "mcq":
        candidates = [
            _fmt_money(F / n),
            _fmt_money((F * i) / ((1 + i) ** n)),
            _fmt_money(x * 1.1),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            rng=rng,
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            subskill="payment_from_future_value",
            difficulty=difficulty,
            parameters={"F": F, "i": i, "n": n},
        )

    return _make_typed(
        rng=rng,
        prompt=prompt,
        correct_answer=correct,
        explanation=explanation,
        subskill="payment_from_future_value",
        difficulty=difficulty,
        parameters={"F": F, "i": i, "n": n},
    )


SUBSKILLS = {
    "compound_solve_for_n": _subskill_compound_solve_n,
    "nominal_to_effective": _subskill_nominal_effective_convert,
    "future_value_annuity": _subskill_future_value_annuity,
    "payment_from_future_value": _subskill_payment_from_future_value,
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
        if qtype == "scaffold":
            # only supported on some subskills; fallback to typed where not provided
            pass

        q_rng = _rng((seed or 0) + 10007 * (i + 1))
        q = SUBSKILLS[sk](q_rng, difficulty, qtype)
        q["subskill"] = sk
        q["difficulty"] = difficulty
        _validate_question(q)
        out.append(q)

    return out
