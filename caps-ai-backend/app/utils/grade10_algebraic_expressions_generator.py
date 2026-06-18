import random
import time
from typing import Any, Dict, List, Optional


def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


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


def _gen_classify_number(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    pool = [
        ('-1/3', 'rational'),
        ('100', 'rational'),
        ('0.125', 'rational'),
        ('0.777777...', 'rational'),
        ('pi', 'irrational'),
        ('√2', 'irrational'),
        ('√3', 'irrational'),
    ]
    raw, expected = _choice(rng, pool)
    prompt = f"State whether the number is rational or irrational: {raw}"
    explanation = (
        'Fractions and integers are rational; terminating/recurring decimals are rational. '
        'π and non-perfect roots are irrational.'
    )

    if qtype == 'mcq':
        return _make_mcq(prompt=prompt, options=['rational', 'irrational'], correct_answer=expected, explanation=explanation, parameters={'value': raw})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Does the decimal terminate or recur? (yes/no/unknown)',
                'correct_answer': 'unknown' if expected == 'irrational' and ('√' in raw or raw == 'pi') else 'yes',
                'explanation': 'Rational numbers terminate or recur. Some symbolic forms are known to be irrational.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final classification (rational/irrational):',
                'correct_answer': expected,
                'explanation': explanation,
            },
        ]
        steps = [
            'Try to write the number as a fraction a/b.',
            'Or inspect the decimal: terminating/recurring → rational; otherwise → irrational.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=expected, explanation=explanation, parameters={'value': raw})

    return _make_typed(prompt=prompt, correct_answer=expected, explanation=explanation, parameters={'value': raw})


def _gen_rounding(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    dp = int(_choice(rng, [2, 3, 4] if difficulty != 'easy' else [2, 3]))
    int_part = int(_choice(rng, [0, 1, 2, 3, 7, 10, 12, 25]))
    digits = [int(_choice(rng, list(range(0, 10)))) for _ in range(dp + 2)]
    s = f"{int_part}." + ''.join(str(d) for d in digits)
    val = float(s)
    correct = f"{val:.{dp}f}"

    prompt = f"Round off to {dp} decimal places: {s}"
    explanation = f"Look at the digit in the {dp + 1}th decimal place to round to {dp} decimal places."

    if qtype == 'mcq':
        options = _make_unique_options(
            rng,
            correct,
            [
                f"{val + (10 ** (-dp)):.{dp}f}",
                f"{max(0.0, val - (10 ** (-dp))):.{dp}f}",
                f"{val:.{max(0, dp - 1)}f}",
            ],
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'value': s, 'dp': dp})

    if qtype == 'scaffold':
        next_digit = digits[dp]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the digit in the {dp + 1}th decimal place?",
                'correct_answer': str(next_digit),
                'explanation': 'This digit decides whether you round up/down.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Rounded value:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            f'Mark {dp} decimal places.',
            f'Look at the next digit (place {dp + 1}).',
            'Round and rewrite the number.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'value': s, 'dp': dp})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'value': s, 'dp': dp})


def _gen_surd_between_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    root_type = _choice(rng, ['sqrt', 'cbrt'] if difficulty != 'easy' else ['sqrt'])

    if root_type == 'sqrt':
        lo = int(_choice(rng, [1, 2, 3, 4, 5, 6, 7]))
        hi = lo + 1
        a = int(_choice(rng, list(range(lo * lo + 1, hi * hi))))
        prompt = f"Without a calculator, determine between which consecutive integers √{a} lies."
        correct = f"{lo} < √{a} < {hi}"
        explanation = f"Since {lo}^2 = {lo * lo} and {hi}^2 = {hi * hi}, and {lo * lo} < {a} < {hi * hi}, then {lo} < √{a} < {hi}."
        params = {'a': a, 'lo': lo, 'hi': hi, 'type': 'sqrt'}
    else:
        lo = int(_choice(rng, [1, 2, 3, 4]))
        hi = lo + 1
        a = int(_choice(rng, list(range(lo ** 3 + 1, hi ** 3))))
        prompt = f"Without a calculator, determine between which consecutive integers ∛{a} lies."
        correct = f"{lo} < ∛{a} < {hi}"
        explanation = f"Since {lo}^3 = {lo ** 3} and {hi}^3 = {hi ** 3}, and {lo ** 3} < {a} < {hi ** 3}, then {lo} < ∛{a} < {hi}."
        params = {'a': a, 'lo': lo, 'hi': hi, 'type': 'cbrt'}

    if qtype == 'mcq':
        opt1 = correct
        opt2 = f"{lo - 1} < √{a} < {lo}" if root_type == 'sqrt' else f"{lo - 1} < ∛{a} < {lo}"
        opt3 = f"{hi} < √{a} < {hi + 1}" if root_type == 'sqrt' else f"{hi} < ∛{a} < {hi + 1}"
        opt4 = f"{lo} < √{a} < {hi + 1}" if root_type == 'sqrt' else f"{lo} < ∛{a} < {hi + 1}"
        options = _make_unique_options(rng, opt1, [opt2, opt3, opt4])
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters=params)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the lower and upper perfect powers you compare with (e.g. 5^2 and 6^2):',
                'correct_answer': f"{lo}^{2 if root_type == 'sqrt' else 3} and {hi}^{2 if root_type == 'sqrt' else 3}",
                'explanation': 'Use consecutive squares/cubes around the radicand.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final inequality:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find consecutive perfect squares/cubes around the number inside the root.',
            'Translate the inequality back into an inequality for the root.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=params)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=params)


def _gen_expand_product(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Monomial·binomial OR binomial·binomial
    kind = _choice(rng, ['mono_bi', 'bi_bi'] if difficulty != 'easy' else ['mono_bi', 'bi_bi'])

    if kind == 'mono_bi':
        k = int(_choice(rng, [-5, -4, -3, -2, -1, 2, 3, 4, 5]))
        a = int(_choice(rng, [1, 2, 3, 4]))
        b = int(_choice(rng, [-9, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 9]))
        expr = f"{k}{'' if a == 1 else 'x'}" if a == 1 else f"{k}x^{a}"
        binom = f"(x {'+' if b >= 0 else '-'} {abs(b)})"
        prompt = f"Expand and simplify: {expr}{binom}"
        # k*x^a*(x + b) = k*x^(a+1) + k*b*x^a
        term1_pow = a + 1
        term2_pow = a
        term1 = f"{k}x^{term1_pow}" if term1_pow != 1 else f"{k}x"
        kb = k * b
        term2 = f"{kb}x^{term2_pow}" if term2_pow != 1 else f"{kb}x"
        if term2_pow == 0:
            term2 = str(kb)
        correct = f"{term1} {'+' if kb >= 0 else '-'} {str(abs(kb)) + ('' if term2_pow == 0 else ('x' if term2_pow == 1 else f'x^{term2_pow}'))}".replace('  ', ' ')
        explanation = 'Distribute the monomial across both terms in the bracket, then simplify.'
        params = {'k': k, 'a': a, 'b': b, 'kind': kind}
    else:
        a = int(_choice(rng, [1, 2, 3, 4]))
        b = int(_choice(rng, [-9, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 9]))
        c = int(_choice(rng, [1, 2, 3, 4]))
        d = int(_choice(rng, [-9, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 9]))
        p1 = f"({a}x {'+' if b >= 0 else '-'} {abs(b)})"
        p2 = f"({c}x {'+' if d >= 0 else '-'} {abs(d)})"
        prompt = f"Expand and simplify: {p1}{p2}"
        # (ax+b)(cx+d)=ac x^2 + (ad+bc)x + bd
        ac = a * c
        mid = a * d + b * c
        bd = b * d
        x2 = f"{ac}x^2"
        x1 = f"{mid}x"
        const = str(bd)
        correct = f"{x2} {'+' if mid >= 0 else '-'} {abs(mid)}x {'+' if bd >= 0 else '-'} {abs(bd)}"
        explanation = 'Multiply each term in the first bracket by each term in the second, then combine like terms.'
        params = {'a': a, 'b': b, 'c': c, 'd': d, 'kind': kind}

    if qtype == 'mcq':
        options = _make_unique_options(
            rng,
            correct,
            [
                correct.replace('+', '-').replace('--', '+'),
                correct.replace('x^2', 'x'),
                correct.replace('x', ''),
            ],
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters=params)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the expanded (uncombined) terms:',
                'correct_answer': 'Expand fully',
                'explanation': 'Distribute/multiply term-by-term first.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final simplified answer:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Multiply term-by-term (distributive property).',
            'Combine like terms.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=params)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=params)


def _gen_factor_common_or_dos(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = _choice(rng, ['common', 'difference_of_squares'])

    if kind == 'difference_of_squares':
        a = int(_choice(rng, [1, 2, 3, 4, 5]))
        b = int(_choice(rng, [2, 3, 4, 5, 6, 7]))
        expr = f"{a*a}x^2 - {b*b}" if a != 1 else f"x^2 - {b*b}"
        correct = f"({a}x - {b})({a}x + {b})" if a != 1 else f"(x - {b})(x + {b})"
        prompt = f"Factorise: {expr}"
        explanation = 'Recognize a difference of two squares: A^2 − B^2 = (A − B)(A + B).'
        params = {'a': a, 'b': b, 'kind': kind}
    else:
        g = int(_choice(rng, [2, 3, 4, 5, 6]))
        a = int(_choice(rng, [1, 2, 3, 4]))
        b = int(_choice(rng, [1, 2, 3, 4, 5]))
        expr = f"{g*a}x + {g*b}"
        correct = f"{g}({a}x + {b})" if a != 1 else f"{g}(x + {b})"
        prompt = f"Factorise: {expr}"
        explanation = 'Take out the greatest common factor.'
        params = {'g': g, 'a': a, 'b': b, 'kind': kind}

    if qtype == 'mcq':
        options = _make_unique_options(
            rng,
            correct,
            [
                correct.replace('+', '-').replace('--', '+'),
                correct.replace('x +', 'x -'),
                correct.replace('x -', 'x +'),
            ],
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters=params)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What strategy do you use? (common factor / difference of squares)',
                'correct_answer': 'difference of squares' if kind == 'difference_of_squares' else 'common factor',
                'explanation': 'Choose the correct pattern first.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final factorised form:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify the pattern (GCF or A^2 − B^2).',
            'Rewrite as a product of factors.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=params)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=params)


def _gen_factor_grouping(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # (px + py) + (qx + qy) => (x + y)(p + q)
    p = int(_choice(rng, [2, 3, 4, 5, 6, 7]))
    q = int(_choice(rng, [2, 3, 4, 5, 6, 7]))
    x_term = 'x'
    y_term = '2y' if difficulty == 'hard' else 'y'

    # Expression: px + p*y + qx + q*y
    expr = f"{p}{x_term} + {p}{y_term} + {q}{x_term} + {q}{y_term}"
    correct = f"({x_term} + {y_term})({p} + {q})"
    prompt = f"Factorise by grouping: {expr}"
    explanation = 'Group terms into pairs, factor each pair, then factor the common bracket.'
    params = {'p': p, 'q': q, 'y_term': y_term}

    if qtype == 'mcq':
        options = _make_unique_options(
            rng,
            correct,
            [
                f"({x_term} - {y_term})({p} + {q})",
                f"({x_term} + {y_term})({p} - {q})",
                f"({x_term} - {y_term})({p} - {q})",
            ],
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters=params)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the two groups you will factor:',
                'correct_answer': f"({p}{x_term} + {p}{y_term}) and ({q}{x_term} + {q}{y_term})",
                'explanation': 'Group terms with common factors into two pairs.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final factorised form:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Group into two pairs with common factors.',
            'Factor each pair.',
            'Factor out the common bracket.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=params)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=params)


def _gen_factor_trinomial(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Generate (x + m)(x + n) => x^2 + (m+n)x + mn
    m = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    n = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
    while m == 0 or n == 0:
        m = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
        n = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))

    b = m + n
    c = m * n
    expr = f"x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}"

    correct = f"(x {'+' if m >= 0 else '-'} {abs(m)})(x {'+' if n >= 0 else '-'} {abs(n)})"
    prompt = f"Factorise: {expr}"
    explanation = 'Find two numbers that multiply to c and add to b.'
    params = {'b': b, 'c': c, 'm': m, 'n': n}

    if qtype == 'mcq':
        wrong1 = f"(x {'+' if m >= 0 else '-'} {abs(m)})(x {'+' if -n >= 0 else '-'} {abs(n)})"
        wrong2 = f"(x {'+' if -m >= 0 else '-'} {abs(m)})(x {'+' if n >= 0 else '-'} {abs(n)})"
        wrong3 = f"(x {'+' if n >= 0 else '-'} {abs(n)})(x {'+' if m >= 0 else '-'} {abs(m)})"
        options = _make_unique_options(rng, correct, [wrong1, wrong2, wrong3])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters=params)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Find numbers m and n such that m·n = {c} and m+n = {b}. Write m,n:",
                'correct_answer': f"{m},{n}",
                'explanation': 'Try factor pairs of c until the sum matches b.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final factorised form:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'List factor pairs of the constant term.',
            'Choose the pair whose sum is the coefficient of x.',
            'Write the factors as two brackets.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=params)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=params)


def generate_grade10_algebraic_expressions_question(
    *,
    subskill: str = 'algebraic_expressions',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Algebraic expressions'
    subskill = str(subskill or 'algebraic_expressions')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'classify_real_numbers',
        'rounding_off',
        'estimate_surds_between_integers',
        'expand_products',
        'factor_common_or_difference_of_squares',
        'factorise_by_grouping',
        'factorise_trinomial',
    ]

    if subskill in {'algebraic_expressions', 'algebra', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'classify_real_numbers': _gen_classify_number,
        'rounding_off': _gen_rounding,
        'estimate_surds_between_integers': _gen_surd_between_integers,
        'expand_products': _gen_expand_product,
        'factor_common_or_difference_of_squares': _gen_factor_common_or_dos,
        'factorise_by_grouping': _gen_factor_grouping,
        'factorise_trinomial': _gen_factor_trinomial,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g10_algexp'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
