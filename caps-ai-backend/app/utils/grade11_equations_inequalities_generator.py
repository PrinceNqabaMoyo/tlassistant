import random
import time
from typing import Any, Dict, List, Optional, Tuple


def _make_id(prefix: str, rng: random.Random) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{rng.randint(1000, 9999)}"


def _make_typed(*, prompt: str, correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'typed',
        'question': prompt,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_mcq(*, prompt: str, options: List[str], correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'mcq',
        'question': prompt,
        'options': options,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_scaffold(
    *,
    prompt: str,
    steps: List[str],
    checkpoints: List[Dict[str, Any]],
    final_answer: str,
    explanation: str,
    **extra,
) -> Dict[str, Any]:
    return {
        'question_type': 'scaffold',
        'question': prompt,
        'steps': steps,
        'checkpoints': checkpoints,
        'correct_answer': str(final_answer),
        'explanation': explanation,
        **extra,
    }


def _validate_question(q: Dict[str, Any]) -> None:
    required = {'id', 'topic', 'subskill', 'difficulty', 'question_type', 'question', 'correct_answer', 'explanation'}
    missing = [k for k in required if k not in q]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

    if q['question_type'] not in {'typed', 'mcq', 'scaffold'}:
        raise ValueError('Invalid question_type')

    if q['question_type'] == 'mcq':
        if not isinstance(q.get('options'), list) or len(q.get('options', [])) < 2:
            raise ValueError('MCQ must include options list')
        if str(q['correct_answer']) not in [str(o) for o in q.get('options', [])]:
            raise ValueError('MCQ correct_answer must be one of options')

    if q['question_type'] == 'scaffold':
        if not isinstance(q.get('steps'), list) or len(q.get('steps', [])) < 1:
            raise ValueError('Scaffold must include steps')
        if not isinstance(q.get('checkpoints'), list) or len(q.get('checkpoints', [])) < 1:
            raise ValueError('Scaffold must include checkpoints')


def _choice(rng: random.Random, xs: List[Any]) -> Any:
    return xs[int(rng.randrange(0, len(xs)))]


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


def _pick_var(rng: random.Random) -> str:
    return _choice(rng, ['x', 'y', 't', 'p'])


def _format_signed(n: int, var: Optional[str] = None) -> str:
    if var:
        if n == 1:
            return var
        if n == -1:
            return f"-{var}"
        return f"{n}{var}"
    return str(n)


def _format_ax2_bx_c(a: int, b: int, c: int, var: str) -> str:
    parts: List[str] = []

    if a == 1:
        parts.append(f"{var}^2")
    elif a == -1:
        parts.append(f"-{var}^2")
    else:
        parts.append(f"{a}{var}^2")

    if b != 0:
        sign = '+' if b > 0 else '-'
        parts.append(f" {sign} {abs(b)}{var}")

    if c != 0:
        sign = '+' if c > 0 else '-'
        parts.append(f" {sign} {abs(c)}")

    return ''.join(parts)


def _gen_completing_square(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)

    if difficulty == 'easy':
        p = int(_choice(rng, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        q = int(_choice(rng, [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]))
    elif difficulty == 'medium':
        p = int(_choice(rng, [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
        q = int(_choice(rng, [-15, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 15]))
    else:
        p = int(_choice(rng, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        q = int(_choice(rng, [-20, -18, -16, -15, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 15, 16, 18, 20]))

    b = -2 * p
    c = p * p + q

    poly = _format_ax2_bx_c(1, b, c, var)
    prompt = f"Complete the square: {poly}"
    correct = f"({var} {('-' if p > 0 else '+')} {abs(p)})^2 {('+' if q >= 0 else '-') } {abs(q)}" if q != 0 else f"({var} {('-' if p > 0 else '+')} {abs(p)})^2"
    correct = correct.replace('  ', ' ')

    explanation = 'Take half of the coefficient of the linear term, square it, and add/subtract to form a perfect square.'

    if qtype == 'mcq':
        candidates = [
            f"({var} {('-' if p > 0 else '+')} {abs(p)})^2 + {abs(q)}",
            f"({var} {('-' if p > 0 else '+')} {abs(p)})^2 - {abs(q)}",
            f"({var} {('+' if p > 0 else '-')} {abs(p)})^2 {('+' if q >= 0 else '-') } {abs(q)}",
        ]
        options = _make_unique_options(rng, correct, [c for c in candidates if c != correct])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        half_b = b / 2
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"What is half of the coefficient of {var}? (i.e. {b}/2)",
                'correct_answer': str(int(half_b)),
                'explanation': 'Half the linear coefficient.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the expression as a perfect square plus/minus a constant:",
                'correct_answer': correct,
                'explanation': 'Use (x - p)^2 = x^2 - 2px + p^2.',
            },
        ]
        steps = ['Group x terms.', 'Take half of the x coefficient.', 'Square it and adjust with a constant.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_quadratic_formula(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)

    if difficulty == 'easy':
        a = int(_choice(rng, [1, 1, 1, 2]))
        b = int(_choice(rng, [-6, -4, -2, 2, 4, 6]))
        c = int(_choice(rng, [-8, -6, -4, -2, 2, 4, 6, 8]))
    elif difficulty == 'medium':
        a = int(_choice(rng, [1, 2, 3]))
        b = int(_choice(rng, [-10, -8, -6, -4, -2, 2, 4, 6, 8, 10]))
        c = int(_choice(rng, [-12, -9, -6, -3, 3, 6, 9, 12]))
    else:
        a = int(_choice(rng, [2, 3, 4, 5]))
        b = int(_choice(rng, [-15, -12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 10, 12, 15]))
        c = int(_choice(rng, [-20, -18, -15, -12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 10, 12, 15, 18, 20]))

    # Ensure discriminant is a perfect square so answers are exact integers.
    # Pick roots then build coefficients.
    r1 = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    r2 = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    b = -a * (r1 + r2)
    c = a * r1 * r2

    poly = _format_ax2_bx_c(a, b, c, var)
    prompt = f"Solve for {var}: {poly} = 0"
    roots = sorted([r1, r2])
    correct = f"{roots[0]}, {roots[1]}" if roots[0] != roots[1] else str(roots[0])
    explanation = 'Use the quadratic formula x = (−b ± √(b^2 − 4ac)) / (2a).'

    if qtype == 'mcq':
        candidates = [
            f"{roots[0] + 1}, {roots[1]}",
            f"{roots[0]}, {roots[1] + 1}",
            f"{roots[0] - 1}, {roots[1]}",
            f"{roots[0]}, {roots[1] - 1}",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        disc = b * b - 4 * a * c
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Compute the discriminant Δ = b^2 − 4ac. What is Δ?",
                'correct_answer': str(disc),
                'explanation': 'Substitute into Δ = b^2 − 4ac.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Give the solutions for {var} (write like: -1, 3):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Identify a, b, c.', 'Compute Δ.', 'Substitute into quadratic formula.', 'Simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_quadratic_inequality(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)

    a = int(_choice(rng, [1, 1, 1, 2])) if difficulty == 'easy' else int(_choice(rng, [1, 2, -1, -2]))
    r1 = int(_choice(rng, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    r2 = int(_choice(rng, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    if r1 == r2:
        r2 = -r1 if r1 != 0 else 2

    b = -a * (r1 + r2)
    c = a * r1 * r2

    sign = _choice(rng, ['<', '>', '<=', '>='])

    poly = _format_ax2_bx_c(a, b, c, var)
    prompt = f"Solve for {var}: {poly} {sign} 0"

    lo, hi = sorted([r1, r2])
    if a > 0:
        inside = sign in {'<', '<='}
    else:
        inside = sign in {'>', '>='}

    if inside:
        if sign in {'<', '>'}:
            correct = f"{lo} < {var} < {hi}"
        else:
            correct = f"{lo} <= {var} <= {hi}"
    else:
        if sign in {'<', '>'}:
            correct = f"{var} < {lo} or {var} > {hi}"
        else:
            correct = f"{var} <= {lo} or {var} >= {hi}"

    explanation = 'Find the roots, then use a sign chart (or parabola shape) to decide where the expression is positive/negative.'

    if qtype == 'mcq':
        candidates = [
            f"{lo} < {var} < {hi}",
            f"{var} < {lo} or {var} > {hi}",
            f"{lo} <= {var} <= {hi}",
            f"{var} <= {lo} or {var} >= {hi}",
        ]
        options = _make_unique_options(rng, correct, [c for c in candidates if c != correct])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"What are the roots (write like: -1, 3)?",
                'correct_answer': f"{lo}, {hi}",
                'explanation': 'Solve the equation by factorising or using the quadratic formula.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the solution set:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Solve the corresponding equation.', 'Mark roots on a number line.', 'Test an interval or use parabola shape.', 'Write solution set.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_simultaneous_linear(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Construct a consistent system with integer solution.
    x = int(_choice(rng, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    y = int(_choice(rng, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))

    a1 = int(_choice(rng, [1, 2, 3] if difficulty == 'easy' else [2, 3, 4, 5]))
    b1 = int(_choice(rng, [1, 2, 3] if difficulty == 'easy' else [2, 3, 4, 5]))
    a2 = int(_choice(rng, [1, 2, 3] if difficulty == 'easy' else [2, 3, 4, 5]))
    b2 = int(_choice(rng, [1, 2, 3] if difficulty == 'easy' else [2, 3, 4, 5]))

    c1 = a1 * x + b1 * y
    c2 = a2 * x + b2 * y

    prompt = f"Solve the system: {a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2}"
    correct = f"x={x}, y={y}"
    explanation = 'Use elimination or substitution to solve for one variable, then substitute back.'

    if qtype == 'mcq':
        candidates = [
            f"x={x + 1}, y={y}",
            f"x={x}, y={y + 1}",
            f"x={x - 1}, y={y}",
            f"x={x}, y={y - 1}",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Give the final solution (format: x=..., y=...):',
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Choose elimination or substitution.', 'Solve for one variable.', 'Substitute and solve for the other.', 'Check in both equations.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def generate_grade11_equations_inequalities_question(
    *,
    subskill: str = 'equations_inequalities',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Equations and inequalities'
    subskill = str(subskill or 'equations_inequalities')
    difficulty = str(difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = str(question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    supported = [
        'completing_square',
        'quadratic_formula',
        'quadratic_inequalities',
        'simultaneous_linear',
    ]

    if subskill in {'equations_inequalities', 'equations and inequalities', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'completing_square': _gen_completing_square,
        'quadratic_formula': _gen_quadratic_formula,
        'quadratic_inequalities': _gen_quadratic_inequality,
        'simultaneous_linear': _gen_simultaneous_linear,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g11_eqineq', rng),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
