
import math
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
    required = {
        'id',
        'topic',
        'subskill',
        'difficulty',
        'question_type',
        'question',
        'correct_answer',
        'explanation',
    }
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


def _simplify_surd_coeff(radicand: int) -> Tuple[int, int]:
    outside = 1
    inside = radicand
    k = 2
    while k * k <= inside:
        while inside % (k * k) == 0:
            inside //= (k * k)
            outside *= k
        k += 1
    return outside, inside


def _gen_exponent_laws(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = int(_choice(rng, [2, 3, 5, 7, 10]))
    m = int(_choice(rng, [1, 2, 3, 4, 5, 6]))
    n = int(_choice(rng, [1, 2, 3, 4, 5, 6]))
    op = _choice(rng, ['mul', 'div'])

    if op == 'mul':
        expr = f"{base}^{m} * {base}^{n}"
        ans = f"{base}^{m + n}"
        explanation = f"Same base → add exponents: {m} + {n} = {m + n}."
    else:
        expr = f"{base}^{m} / {base}^{n}"
        exp = m - n
        ans = f"{base}^{exp}" if exp >= 0 else f"1/{base}^{abs(exp)}"
        explanation = f"Same base → subtract exponents: {m} − {n} = {exp}. Write final answer with positive exponent."

    prompt = f"Simplify (final answer with positive exponent): {expr}"

    if qtype == 'mcq':
        distract = [f"{base}^{m - n}", f"{base}^{m + n}", f"{base}^{m * n}"]
        options = _make_unique_options(rng, ans, [d for d in distract if d != ans])
        return _make_mcq(prompt=prompt, options=options, correct_answer=ans, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Which rule applies? (add/subtract exponents)',
                'correct_answer': 'add' if op == 'mul' else 'subtract',
                'explanation': 'Multiply same base: add exponents. Divide same base: subtract exponents.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Simplified answer:',
                'correct_answer': ans,
                'explanation': explanation,
            },
        ]
        steps = ['Identify same base.', 'Apply exponent law.', 'Rewrite with positive exponents if needed.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=ans, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=ans, explanation=explanation)


def _gen_rational_exponent_to_radical(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = int(_choice(rng, [4, 8, 9, 16, 25, 27, 32, 64]))
    n = int(_choice(rng, [2, 3, 4, 5]))
    m = int(_choice(rng, [1, 2, 3]))

    prompt = f"Write as a radical: {a}^{m}/{n}"
    ans = f"{n}√({a}^{m})"
    explanation = f"Use a^(m/n) = {n}√(a^m)."

    if qtype == 'mcq':
        options = _make_unique_options(rng, ans, [f"{m}√({a}^{n})", f"{n}√({a}^{n})", f"{n}√({a}^{m + 1})"])
        return _make_mcq(prompt=prompt, options=options, correct_answer=ans, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'What is n (the root index) in a^(m/n)?',
                'correct_answer': str(n),
                'explanation': 'n is the root index (degree).',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write as a radical:',
                'correct_answer': ans,
                'explanation': explanation,
            },
        ]
        steps = ['Use a^(m/n) = n√(a^m).', 'Rewrite in radical form.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=ans, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=ans, explanation=explanation)


def _gen_simplify_surd(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    rad = int(_choice(rng, [8, 12, 18, 20, 27, 32, 45, 48, 50, 72, 75, 80, 98, 108, 147]))
    outside, inside = _simplify_surd_coeff(rad)

    if inside == 1:
        ans = str(outside)
    elif outside == 1:
        ans = f"√{inside}"
    else:
        ans = f"{outside}√{inside}"

    prompt = f"Simplify in simplest surd form: √{rad}"
    explanation = f"Write {rad} as {outside * outside}×{inside}. Then √{rad} = √({outside}^2×{inside}) = {outside}√{inside}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, ans, [f"{outside}√{rad}", f"√{outside}{inside}", f"{outside + 1}√{inside}"])
        return _make_mcq(prompt=prompt, options=options, correct_answer=ans, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the radicand as (perfect square)×(remainder):',
                'correct_answer': f"{outside * outside}*{inside}",
                'explanation': f"{rad} = {outside * outside}×{inside}.",
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final simplest surd form:',
                'correct_answer': ans,
                'explanation': explanation,
            },
        ]
        steps = ['Factorise the radicand.', 'Take out the perfect square.', 'Write the simplified surd.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=ans, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=ans, explanation=explanation)


def _gen_rationalise_denominator(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = _choice(rng, ['single', 'binomial'])

    if kind == 'single':
        a = int(_choice(rng, [2, 3, 5, 6, 7, 10]))
        n = int(_choice(rng, [2, 3, 5, 7, 10]))
        prompt = f"Rationalise the denominator: {n}/√{a}"
        ans = f"{n}√{a}/{a}"
        explanation = f"Multiply top and bottom by √{a}: ({n}/√{a})*(√{a}/√{a}) = {n}√{a}/{a}."
    else:
        a = int(_choice(rng, [2, 3, 5, 7, 8]))
        b = int(_choice(rng, [1, 2, 3, 4, 5]))
        prompt = f"Rationalise the denominator: 1/(√{a} + {b})"
        ans = f"(√{a} - {b})/({a} - {b * b})"
        explanation = f"Multiply by the conjugate (√{a} - {b}). Denominator becomes (√{a})^2 - {b}^2 = {a} - {b * b}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, ans, [ans.replace('-', '+'), ans.replace('√', ''), '1'])
        return _make_mcq(prompt=prompt, options=options, correct_answer=ans, explanation=explanation)

    if qtype == 'scaffold':
        multiplier = f"√{a}" if kind == 'single' else f"√{a} - {b}"
        steps = ['Choose a multiplier that removes the surd.', 'Multiply numerator and denominator.', 'Simplify.']
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'What do you multiply by?',
                'correct_answer': multiplier,
                'explanation': 'Use √a/√a for a single surd, or the conjugate for a binomial denominator.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': ans,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=ans, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=ans, explanation=explanation)


def _gen_exponential_application(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    context = _choice(rng, ['bacteria', 'fish', 'city'])

    if context == 'bacteria':
        p0 = int(_choice(rng, [10, 12, 15, 20]))
        r = float(_choice(rng, [0.4, 0.8]))
        t = int(_choice(rng, [5, 8, 12]))
        unit = 'hours'
    elif context == 'fish':
        p0 = int(_choice(rng, [821, 950, 1200]))
        r = float(_choice(rng, [0.02, 0.03]))
        t = int(_choice(rng, [6, 12, 24]))
        unit = 'months'
    else:
        p0 = int(_choice(rng, [3885840, 1200000, 2500000]))
        r = float(_choice(rng, [0.007, 0.01]))
        t = int(_choice(rng, [10, 13, 20]))
        unit = 'years'

    p = p0 * ((1.0 + r) ** t)
    ans = str(int(round(p)))

    r_pct = int(round(r * 100))
    prompt = f"A population starts at {p0} and grows by {r_pct}% per {unit[:-1]}. How many will there be after {t} {unit}? (Round to nearest whole number)"
    explanation = f"Use P = P0(1+r)^t = {p0}(1+{r})^{t} ≈ {ans}."

    if qtype == 'mcq':
        x = int(ans)
        options = _make_unique_options(rng, ans, [str(int(round(x * 0.9))), str(int(round(x * 1.1))), str(int(round(x * 1.2)))])
        return _make_mcq(prompt=prompt, options=options, correct_answer=ans, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the model (P = P0(1+r)^t):',
                'correct_answer': f"P={p0}(1+{r})^{t}",
                'explanation': 'Use the exponential growth/decay model.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final population (nearest whole number):',
                'correct_answer': ans,
                'explanation': explanation,
            },
        ]
        steps = ['Identify P0, r and t.', 'Substitute into P = P0(1+r)^t.', 'Evaluate (calculator).', 'Round to nearest whole number.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=ans, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=ans, explanation=explanation)


def generate_grade11_exponents_surds_question(
    *,
    subskill: str = 'exponents_surds',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Exponents and surds'
    subskill = str(subskill or 'exponents_surds')
    difficulty = str(difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = str(question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    supported = [
        'exponent_laws',
        'rational_exponent_to_radical',
        'simplify_surd',
        'rationalise_denominator',
        'exponential_application',
    ]

    if subskill in {'exponents_surds', 'exponents and surds', 'exponents & surds', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'exponent_laws': _gen_exponent_laws,
        'rational_exponent_to_radical': _gen_rational_exponent_to_radical,
        'simplify_surd': _gen_simplify_surd,
        'rationalise_denominator': _gen_rationalise_denominator,
        'exponential_application': _gen_exponential_application,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g11_exp_surds', rng),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }
    _validate_question(out)
    return out

