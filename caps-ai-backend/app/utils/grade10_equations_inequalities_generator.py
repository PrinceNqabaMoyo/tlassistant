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
    return _choice(rng, ['x', 'y', 'a', 'p', 't'])


def _linear_coeffs(rng: random.Random, difficulty: str) -> Tuple[int, int, int, int]:
    if difficulty == 'easy':
        a = int(_choice(rng, [1, 2, 3, 4, 5]))
        b = int(_choice(rng, [-10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10]))
        x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]))
    elif difficulty == 'medium':
        a = int(_choice(rng, [2, 3, 4, 5, 6, 7, 8]))
        b = int(_choice(rng, [-15, -12, -10, -8, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12, 15]))
        x = int(_choice(rng, [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
    else:
        a = int(_choice(rng, [3, 4, 5, 6, 7, 8, 9, 10, 12]))
        b = int(_choice(rng, [-20, -18, -15, -12, -10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18, 20]))
        x = int(_choice(rng, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    c = a * x + b
    return a, b, c, x


def _gen_linear_equation(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)
    a, b, c, x = _linear_coeffs(rng, difficulty)

    lhs = f"{a}{var}" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else ''))
    prompt = f"Solve for {var}: {lhs} = {c}"
    correct = str(x)
    explanation = f"Move the constant term, then divide by {a}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [str(x + 1), str(x - 1), str(x + 2), str(x - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        rhs_after = c - b
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"After moving the constant term, what is the new right-hand side (so that {a}{var} = ___ )?",
                'correct_answer': str(rhs_after),
                'explanation': 'Add/subtract the constant on both sides.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Now solve {a}{var} = {rhs_after}. What is {var}?",
                'correct_answer': correct,
                'explanation': f"Divide by {a}.",
            },
        ]
        steps = ['Expand if needed.', 'Collect like terms.', 'Isolate the variable.', 'Check by substitution.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_quadratic_factorised(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)
    r1 = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    r2 = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    if difficulty == 'easy':
        r2 = r1

    b = -(r1 + r2)
    c = r1 * r2

    poly = f"{var}^2" + (f" + {b}{var}" if b > 0 else (f" - {abs(b)}{var}" if b < 0 else '')) + (f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else ''))
    prompt = f"Solve for {var}: {poly} = 0"

    roots = sorted([r1, r2])
    correct = f"{roots[0]}, {roots[1]}" if roots[0] != roots[1] else str(roots[0])
    explanation = 'Factorise (or recognise a perfect square), then set each factor equal to zero.'

    if qtype == 'mcq':
        if roots[0] == roots[1]:
            options = _make_unique_options(rng, correct, [str(roots[0] + 1), str(roots[0] - 1), str(roots[0] + 2), str(roots[0] - 2)])
        else:
            options = _make_unique_options(rng, correct, [f"{roots[0]}, {roots[1] + 1}", f"{roots[0] - 1}, {roots[1]}", f"{roots[0] + 1}, {roots[1] - 1}"])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Give the solutions for {var} (write like: -1, 3):",
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Write in the form ax^2 + bx + c = 0.', 'Factorise.', 'Solve and check.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_linear_inequality(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    var = _pick_var(rng)
    a = int(_choice(rng, [1, 2, 3, 4] if difficulty != 'hard' else [2, 3, 4, 5, 6]))
    b = int(_choice(rng, [-12, -10, -8, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 8, 10, 12]))
    x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    sign = _choice(rng, ['<', '<=', '>', '>='])

    c = a * x + b
    lhs = f"{a}{var}" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else ''))
    prompt = f"Solve for {var}: {lhs} {sign} {c}"

    correct = f"{var} {sign} {x}"
    explanation = 'Isolate the variable. If you multiply/divide by a negative number, reverse the sign.'

    if qtype == 'mcq':
        options = list(dict.fromkeys([correct, f"{var} {sign} {x + 1}", f"{var} {sign} {x - 1}", f"{var} {('<' if sign in ['>', '>='] else '>')} {x}"]))
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options[:4], correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the solution in the form '{var} {sign} number':",
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Collect like terms.', 'Isolate the variable.', 'Reverse the sign if dividing by a negative.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_literal_make_subject(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    form = _choice(rng, ['triangle', 'speed', 'linear'])

    if form == 'triangle':
        prompt = 'The area of a triangle is A = 1/2 b h. Make h the subject of the formula.'
        correct = 'h=2A/b'
        explanation = 'Multiply both sides by 2, then divide by b.'
    elif form == 'speed':
        prompt = 'The speed formula is v = D/t. Make t the subject of the formula.'
        correct = 't=D/v'
        explanation = 'Multiply both sides by t, then divide by v.'
    else:
        prompt = 'Given y = (x + 2)/4, make x the subject of the formula.'
        correct = 'x=4y-2'
        explanation = 'Multiply by 4, then subtract 2.'

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [correct.replace('=', ' = '), 'h=A/(2b)', 't=v/D', 'x=4y+2'])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final rearranged formula (no spaces):',
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Identify the target subject.', 'Do inverse operations to isolate it.', 'Simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def generate_grade10_equations_inequalities_question(
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
        'solve_linear',
        'solve_quadratic_factorise',
        'solve_linear_inequality',
        'literal_make_subject',
    ]

    if subskill in {'equations_inequalities', 'equations and inequalities', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'solve_linear': _gen_linear_equation,
        'solve_quadratic_factorise': _gen_quadratic_factorised,
        'solve_linear_inequality': _gen_linear_inequality,
        'literal_make_subject': _gen_literal_make_subject,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g10_eqineq', rng),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
