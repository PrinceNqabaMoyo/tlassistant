import random
import time
from typing import Any, Dict, List, Optional


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


def _sequence_terms_arithmetic(a1: int, d: int, n: int) -> List[int]:
    return [a1 + d * i for i in range(n)]


def _sequence_terms_quadratic(a: int, b: int, c: int, n: int) -> List[int]:
    return [a * (k + 1) * (k + 1) + b * (k + 1) + c for k in range(n)]


def _second_differences(seq: List[int]) -> List[int]:
    first = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    return [first[i + 1] - first[i] for i in range(len(first) - 1)]


def _format_linear_tn(p: int, q: int) -> str:
    if q == 0:
        return f"T_n = {p}n"
    if q > 0:
        return f"T_n = {p}n + {q}"
    return f"T_n = {p}n - {abs(q)}"


def _format_quadratic_tn(a: int, b: int, c: int) -> str:
    parts: List[str] = []
    parts.append(f"{a}n^2")
    if b != 0:
        parts.append(f"+ {b}n" if b > 0 else f"- {abs(b)}n")
    if c != 0:
        parts.append(f"+ {c}" if c > 0 else f"- {abs(c)}")
    return 'T_n = ' + ' '.join(parts)


def _choose_nonzero(rng: random.Random, candidates: List[int]) -> int:
    x = rng.choice(candidates)
    while x == 0:
        x = rng.choice(candidates)
    return x


def _gen_linear_next_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = rng.randint(0, 30)
        d = rng.choice([2, 3, 4, 5])
    elif difficulty == 'medium':
        a1 = rng.randint(-20, 40)
        d = rng.choice([-8, -6, -5, -4, -3, 3, 4, 5, 6, 8])
    else:
        a1 = rng.randint(-50, 60)
        d = rng.choice([-12, -10, -9, -8, -7, -6, 6, 7, 8, 9, 10, 12])

    shown_n = 4
    ask_n = 3
    terms = _sequence_terms_arithmetic(a1, d, shown_n + ask_n)
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"Linear (arithmetic) sequence: add {d} each time."

    if qtype == 'mcq':
        candidates = [
            ', '.join(str(t + d) for t in nxt),
            ', '.join(str(t - d) for t in nxt),
            ', '.join(str(t + (1 if d >= 0 else -1) * (abs(d) + 1)) for t in nxt),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt},
        )

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Find the common difference d = T2 − T1: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(shown[1] - shown[0]),
                'explanation': 'Subtract consecutive terms to find the common difference.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the general term: T_n = a + (n − 1)d. Here a={a1}, d={d}.",
                'correct_answer': f"T_n = {a1} + (n - 1)({d})",
                'explanation': 'Use T_n = a + (n − 1)d.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Next {ask_n} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find d by subtracting consecutive terms (T2 − T1).',
            'Write T_n = a + (n − 1)d.',
            'Add d repeatedly to get the next terms.',
        ]
        return _make_scaffold(
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=correct,
            explanation=explanation,
            parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt},
        )

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})


def _gen_linear_find_general_term(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = rng.randint(0, 20)
        d = rng.choice([2, 3, 4, 5])
    elif difficulty == 'medium':
        a1 = rng.randint(-10, 25)
        d = rng.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    else:
        a1 = rng.randint(-30, 40)
        d = rng.choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])

    shown = _sequence_terms_arithmetic(a1, d, 4)

    b = d
    c = a1 - d
    correct = f"T_n = {b}n + {c}" if c >= 0 else f"T_n = {b}n - {abs(c)}"

    prompt = f"Given the linear sequence: {'; '.join(str(t) for t in shown)}; ... Find the general term T_n."
    explanation = 'For a linear (arithmetic) sequence: T_n = a + (n − 1)d. Then simplify.'

    if qtype == 'mcq':
        candidates = [
            f"T_n = {b}n + {a1}",
            f"T_n = {b}n + {c + d}",
            f"T_n = {b}n - {abs(c + d)}" if c + d < 0 else f"T_n = {b}n + {c + d}",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Find d = T2 − T1: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(d),
                'explanation': 'Subtract consecutive terms to find d.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write T_n = a + (n − 1)d using a={a1}, d={d}:",
                'correct_answer': f"T_n = {a1} + (n - 1)({d})",
                'explanation': 'Substitute a and d into the formula.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Simplify to the form T_n = pn + q:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find d.', 'Use T_n = a + (n − 1)d.', 'Expand and simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown})


def _gen_linear_terms_from_tn(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = _choose_nonzero(rng, [1, 2, 3, 4, 5])
        q = rng.randint(-10, 10)
        n_max = 5
    elif difficulty == 'medium':
        p = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
        q = rng.randint(-20, 20)
        n_max = 6
    else:
        p = _choose_nonzero(rng, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
        q = rng.randint(-40, 40)
        n_max = 7

    tn = _format_linear_tn(p, q)
    terms = [p * n + q for n in range(1, n_max + 1)]
    correct = ', '.join(str(t) for t in terms)
    prompt = f"Given {tn}, write the first {n_max} terms of the sequence (comma-separated)."
    explanation = 'Substitute n = 1, 2, 3, … into T_n.'

    if qtype == 'mcq':
        candidates = [
            ', '.join(str(p * n + (q + 1)) for n in range(1, n_max + 1)),
            ', '.join(str((p + 1) * n + q) for n in range(1, n_max + 1)),
            ', '.join(str(p * n - q) for n in range(1, n_max + 1)),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'n_max': n_max})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Compute T1:",
                'correct_answer': str(p * 1 + q),
                'explanation': 'Substitute n = 1 into T_n.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Compute T2:",
                'correct_answer': str(p * 2 + q),
                'explanation': 'Substitute n = 2 into T_n.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the first {n_max} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Substitute n = 1, 2, 3, …', 'List the terms in order.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'n_max': n_max})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'n_max': n_max})


def _gen_linear_solve_for_n(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = _choose_nonzero(rng, [1, 2, 3, 4, 5])
        q = rng.randint(-10, 10)
        n = rng.randint(2, 12)
    elif difficulty == 'medium':
        p = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
        q = rng.randint(-20, 20)
        n = rng.randint(3, 18)
    else:
        p = _choose_nonzero(rng, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
        q = rng.randint(-40, 40)
        n = rng.randint(4, 25)

    tn = _format_linear_tn(p, q)
    value = p * n + q
    prompt = f"Given {tn}, find n if T_n = {value}."
    correct = str(n)
    explanation = 'Solve the linear equation p·n + q = value.'

    if qtype == 'mcq':
        candidates = [str(n + 1), str(max(1, n - 1)), str(n + 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'value': value})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the equation using T_n = {value}:",
                'correct_answer': f"{p}n + {q} = {value}" if q >= 0 else f"{p}n - {abs(q)} = {value}",
                'explanation': 'Set the expression equal to the given value.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Solve for n:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Set T_n equal to the given value.', 'Solve the linear equation for n.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'value': value})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'p': p, 'q': q, 'value': value})


def _gen_linear_number_of_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = rng.randint(-10, 20)
        d = _choose_nonzero(rng, [-5, -4, -3, 3, 4, 5])
        n = rng.randint(6, 18)
    elif difficulty == 'medium':
        a1 = rng.randint(-25, 35)
        d = _choose_nonzero(rng, [-8, -7, -6, -5, 5, 6, 7, 8])
        n = rng.randint(8, 25)
    else:
        a1 = rng.randint(-50, 60)
        d = _choose_nonzero(rng, [-12, -10, -9, -8, 8, 9, 10, 12])
        n = rng.randint(10, 40)

    an = a1 + (n - 1) * d
    shown = _sequence_terms_arithmetic(a1, d, 3)
    prompt = f"Linear sequence: {shown[0]}; {shown[1]}; {shown[2]}; ... ; {an}. How many terms are in the sequence?"
    correct = str(n)
    explanation = 'Use T_n = a + (n − 1)d, substitute T_n, then solve for n.'

    if qtype == 'mcq':
        candidates = [str(n - 1), str(n + 1), str(n + 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'an': an})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Find d = T2 − T1:",
                'correct_answer': str(d),
                'explanation': 'Subtract consecutive terms to find d.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the equation using T_n = {an} and a = {a1}:",
                'correct_answer': f"{an} = {a1} + (n - 1)({d})",
                'explanation': 'Substitute into T_n = a + (n − 1)d.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Solve for n (number of terms):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find the common difference d.', 'Use T_n = a + (n − 1)d.', 'Solve for n.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'an': an})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'an': an})


def _gen_quadratic_identify_and_a(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a = rng.choice([1, 2])
        b = rng.randint(-2, 4)
        c = rng.randint(-5, 8)
    elif difficulty == 'medium':
        a = rng.choice([1, 2, 3])
        b = rng.randint(-6, 6)
        c = rng.randint(-10, 10)
    else:
        a = rng.choice([2, 3, 4])
        b = rng.randint(-10, 10)
        c = rng.randint(-15, 15)

    terms = _sequence_terms_quadratic(a, b, c, 5)
    sec = _second_differences(terms)
    sec_const = all(s == sec[0] for s in sec)

    prompt = f"Sequence: {'; '.join(str(t) for t in terms)}; ... Is it quadratic? If yes, give the constant second difference."
    correct = str(sec[0])
    explanation = 'A sequence is quadratic if the second differences are constant.'

    if qtype == 'mcq':
        candidates = [str(sec[0] + 2), str(sec[0] - 2), str(sec[0] * 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            parameters={'a': a, 'b': b, 'c': c, 'terms': terms, 'second_differences': sec, 'is_quadratic': sec_const},
        )

    if qtype == 'scaffold':
        first = [terms[i + 1] - terms[i] for i in range(len(terms) - 1)]
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"First differences (comma-separated):",
                'correct_answer': ', '.join(str(x) for x in first),
                'explanation': 'Subtract consecutive terms.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Second differences (comma-separated):",
                'correct_answer': ', '.join(str(x) for x in sec),
                'explanation': 'Subtract consecutive first differences.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Constant second difference (if constant):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find first differences.', 'Find second differences.', 'If constant, sequence is quadratic; record the constant.']
        return _make_scaffold(
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=correct,
            explanation=explanation,
            parameters={'a': a, 'b': b, 'c': c, 'terms': terms, 'second_differences': sec, 'is_quadratic': sec_const},
        )

    return _make_typed(
        prompt=prompt,
        correct_answer=correct,
        explanation=explanation,
        parameters={'a': a, 'b': b, 'c': c, 'terms': terms, 'second_differences': sec, 'is_quadratic': sec_const},
    )


def _gen_quadratic_general_term_given_abc(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a = rng.choice([1, 2])
        b = rng.randint(-3, 5)
        c = rng.randint(-5, 8)
    elif difficulty == 'medium':
        a = rng.choice([1, 2, 3])
        b = rng.randint(-7, 7)
        c = rng.randint(-10, 10)
    else:
        a = rng.choice([2, 3, 4])
        b = rng.randint(-12, 12)
        c = rng.randint(-15, 15)

    terms = _sequence_terms_quadratic(a, b, c, 4)

    correct = _format_quadratic_tn(a, b, c)
    prompt = f"Given the quadratic sequence: {'; '.join(str(t) for t in terms)}; ... Write a possible general term T_n in the form an^2 + bn + c."
    explanation = 'Quadratic sequences have general term T_n = an^2 + bn + c.'

    if qtype == 'mcq':
        candidates = []
        candidates.append(f"T_n = {a}n^2 + {b + 1}n + {c}")
        candidates.append(f"T_n = {a}n^2 + {b}n + {c + 1}")
        candidates.append(f"T_n = {a + 1}n^2 + {b}n + {c}")
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            parameters={'a': a, 'b': b, 'c': c, 'terms': terms},
        )

    if qtype == 'scaffold':
        sec = _second_differences(terms + [_sequence_terms_quadratic(a, b, c, 5)[-1]])
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the general form:',
                'correct_answer': 'T_n = an^2 + bn + c',
                'explanation': 'Quadratic sequences use T_n = an^2 + bn + c.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Second differences are constant for quadratic sequences (yes/no):',
                'correct_answer': 'yes',
                'explanation': 'Quadratic sequences have constant second differences.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'A valid general term T_n:',
                'correct_answer': correct,
                'explanation': 'One valid answer is the generating quadratic.',
            },
        ]
        steps = ['Recognise quadratic: constant second difference.', 'Use T_n = an^2 + bn + c.', 'Give a suitable expression.']
        return _make_scaffold(
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer=correct,
            explanation=explanation,
            parameters={'a': a, 'b': b, 'c': c, 'terms': terms, 'second_differences': sec},
        )

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'terms': terms})


def _gen_quadratic_terms_from_tn(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a = rng.choice([1, 2])
        b = rng.randint(-3, 4)
        c = rng.randint(-6, 8)
        n_max = 5
    elif difficulty == 'medium':
        a = rng.choice([1, 2, 3])
        b = rng.randint(-7, 7)
        c = rng.randint(-12, 12)
        n_max = 6
    else:
        a = rng.choice([2, 3, 4])
        b = rng.randint(-12, 12)
        c = rng.randint(-20, 20)
        n_max = 7

    tn = _format_quadratic_tn(a, b, c)
    terms = [a * n * n + b * n + c for n in range(1, n_max + 1)]
    correct = ', '.join(str(t) for t in terms)
    prompt = f"Given {tn}, write the first {n_max} terms of the sequence (comma-separated)."
    explanation = 'Substitute n = 1, 2, 3, … into T_n.'

    if qtype == 'mcq':
        candidates = [
            ', '.join(str(a * n * n + b * n + (c + 1)) for n in range(1, n_max + 1)),
            ', '.join(str(a * n * n + (b + 1) * n + c) for n in range(1, n_max + 1)),
            ', '.join(str((a + 1) * n * n + b * n + c) for n in range(1, n_max + 1)),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'n_max': n_max})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute T1:',
                'correct_answer': str(a * 1 * 1 + b * 1 + c),
                'explanation': 'Substitute n = 1 into T_n.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute T2:',
                'correct_answer': str(a * 2 * 2 + b * 2 + c),
                'explanation': 'Substitute n = 2 into T_n.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the first {n_max} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Substitute n = 1, 2, 3, …', 'List the terms in order.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'n_max': n_max})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'n_max': n_max})


def _gen_quadratic_solve_for_n(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a = rng.choice([1, 2])
        b = rng.randint(-4, 4)
        c = rng.randint(-10, 10)
        n = rng.randint(2, 10)
    elif difficulty == 'medium':
        a = rng.choice([1, 2, 3])
        b = rng.randint(-8, 8)
        c = rng.randint(-20, 20)
        n = rng.randint(3, 15)
    else:
        a = rng.choice([2, 3, 4])
        b = rng.randint(-14, 14)
        c = rng.randint(-30, 30)
        n = rng.randint(4, 20)

    tn = _format_quadratic_tn(a, b, c)
    value = a * n * n + b * n + c
    prompt = f"Given {tn}, find n if T_n = {value}. (Give the positive integer solution.)"
    correct = str(n)
    explanation = 'Substitute and solve the quadratic equation. The generated question has an integer solution.'

    if qtype == 'mcq':
        candidates = [str(n + 1), str(max(1, n - 1)), str(n + 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'value': value})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Write the equation using T_n = {value}:",
                'correct_answer': f"{a}n^2 + {b}n + {c} = {value}" if b >= 0 and c >= 0 else f"{a}n^2 {'+ ' + str(b) + 'n' if b >= 0 else '- ' + str(abs(b)) + 'n'} {'+ ' + str(c) if c >= 0 else '- ' + str(abs(c))} = {value}",
                'explanation': 'Set T_n equal to the given value.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Solve for n (positive integer):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Set T_n equal to the given value.', 'Solve for n (positive integer).']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'value': value})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'value': value})


def _gen_classify_sequence(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Generate one of: linear / quadratic / neither
    kind = rng.choice(['linear', 'quadratic', 'neither'])
    if difficulty == 'easy':
        shown_n = 5
    elif difficulty == 'medium':
        shown_n = 6
    else:
        shown_n = 7

    if kind == 'linear':
        a1 = rng.randint(-15, 25)
        d = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
        terms = _sequence_terms_arithmetic(a1, d, shown_n)
        correct = 'linear'
    elif kind == 'quadratic':
        a = rng.choice([1, 2, 3])
        b = rng.randint(-6, 6)
        c = rng.randint(-10, 10)
        terms = _sequence_terms_quadratic(a, b, c, shown_n)
        correct = 'quadratic'
    else:
        # Neither: use a simple geometric-ish progression to avoid constant 2nd differences.
        start = rng.randint(1, 5)
        r = rng.choice([2, 3])
        terms = [start * (r ** i) for i in range(shown_n)]
        correct = 'neither'

    prompt = f"Sequence: {'; '.join(str(t) for t in terms)}. Classify it as linear, quadratic, or neither."
    explanation = 'Linear: constant first difference. Quadratic: constant second difference. Otherwise: neither.'

    if qtype == 'mcq':
        options = ['linear', 'quadratic', 'neither']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'terms': terms, 'kind': kind})

    if qtype == 'scaffold':
        first = [terms[i + 1] - terms[i] for i in range(len(terms) - 1)]
        second = [first[i + 1] - first[i] for i in range(len(first) - 1)]
        is_linear = all(x == first[0] for x in first)
        is_quad = all(x == second[0] for x in second)
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'First differences (comma-separated):',
                'correct_answer': ', '.join(str(x) for x in first),
                'explanation': 'Subtract consecutive terms.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Second differences (comma-separated):',
                'correct_answer': ', '.join(str(x) for x in second),
                'explanation': 'Subtract consecutive first differences.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Classification (linear/quadratic/neither):',
                'correct_answer': correct,
                'explanation': f"First differences constant? {'yes' if is_linear else 'no'}. Second differences constant? {'yes' if is_quad else 'no'}.",
            },
        ]
        steps = ['Compute first differences.', 'Compute second differences.', 'Use constancy to classify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'terms': terms, 'kind': kind})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'terms': terms, 'kind': kind})


def _gen_context_matches(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Round-robin: each pair plays once => games = n(n-1)/2
    if difficulty == 'easy':
        n = rng.randint(6, 12)
    elif difficulty == 'medium':
        n = rng.randint(10, 20)
    else:
        n = rng.randint(15, 30)

    games = n * (n - 1) // 2
    prompt = f"In a tournament with {n} teams, each team plays every other team once. How many games are played in total?"
    correct = str(games)
    explanation = 'Each game is a unique pair of teams. Number of pairs is n(n − 1)/2.'

    if qtype == 'mcq':
        candidates = [str(games + n), str(games - (n - 1)), str(n * (n - 1))]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'How many teams can the first team play?',
                'correct_answer': str(n - 1),
                'explanation': 'It cannot play itself, so it can play the other n − 1 teams.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Why do we divide by 2?',
                'correct_answer': 'each game counted twice',
                'explanation': 'Counting team-by-team counts each game once for each of its two teams.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Total games:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Count all team-vs-other-team matchups.', 'Divide by 2 to correct double counting.', 'Compute the total.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_context_towers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Simple quadratic pattern: blocks in level n is n^2 + 1
    if difficulty == 'easy':
        ask_n = rng.randint(5, 9)
    elif difficulty == 'medium':
        ask_n = rng.randint(8, 14)
    else:
        ask_n = rng.randint(12, 20)

    shown = [n * n + 1 for n in range(1, 5)]
    value = ask_n * ask_n + 1
    prompt = (
        "A tower is built in stages. The number of blocks in stages 1 to 4 are: "
        f"{shown[0]}, {shown[1]}, {shown[2]}, {shown[3]}. "
        f"How many blocks are in stage {ask_n}?"
    )
    correct = str(value)
    explanation = 'This pattern follows T_n = n^2 + 1.'

    if qtype == 'mcq':
        candidates = [str(ask_n * ask_n - 1), str((ask_n + 1) * (ask_n + 1) + 1), str(ask_n * ask_n + 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'ask_n': ask_n})

    if qtype == 'scaffold':
        first = [shown[i + 1] - shown[i] for i in range(len(shown) - 1)]
        second = [first[i + 1] - first[i] for i in range(len(first) - 1)]
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'First differences (comma-separated):',
                'correct_answer': ', '.join(str(x) for x in first),
                'explanation': 'Subtract consecutive terms.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Second differences (comma-separated):',
                'correct_answer': ', '.join(str(x) for x in second),
                'explanation': 'Subtract consecutive first differences.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'A suitable general term:',
                'correct_answer': 'T_n = n^2 + 1',
                'explanation': 'The sequence matches n^2 + 1 for n = 1, 2, 3, 4.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Compute T_{ask_n}:",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Compute differences to see it is quadratic.', 'Propose a formula.', f'Substitute n = {ask_n}.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'ask_n': ask_n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'ask_n': ask_n})


def _gen_quadratic_proof_style_scaffold(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Guided reasoning about: if T_n = an^2 + bn + c then second diff = 2a
    if difficulty == 'easy':
        a = rng.choice([1, 2])
    elif difficulty == 'medium':
        a = rng.choice([1, 2, 3])
    else:
        a = rng.choice([2, 3, 4])

    b = rng.randint(-5, 5)
    c = rng.randint(-10, 10)
    terms = _sequence_terms_quadratic(a, b, c, 6)
    sec = _second_differences(terms)
    prompt = (
        "Consider the quadratic sequence with general term T_n = an^2 + bn + c. "
        "Use the example sequence below to justify the relationship between a and the constant second difference. "
        f"Example terms: {'; '.join(str(t) for t in terms)}."
    )
    correct = str(2 * a)
    explanation = 'For T_n = an^2 + bn + c, the constant second difference is 2a.'

    # Force scaffold type; if called as typed/mcq, still return scaffold to keep intent.
    checkpoints = [
        {
            'id': _make_id('cp', rng),
            'kind': 'typed',
            'prompt': 'Second differences (comma-separated):',
            'correct_answer': ', '.join(str(x) for x in sec),
            'explanation': 'Compute first differences, then differences of those.',
        },
        {
            'id': _make_id('cp', rng),
            'kind': 'typed',
            'prompt': 'Constant second difference:',
            'correct_answer': str(sec[0]),
            'explanation': 'All second differences match.',
        },
        {
            'id': _make_id('cp', rng),
            'kind': 'typed',
            'prompt': 'If the constant second difference is k, then a = ?',
            'correct_answer': 'k/2',
            'explanation': 'Rearrange k = 2a to a = k/2.',
        },
        {
            'id': _make_id('cp', rng),
            'kind': 'typed',
            'prompt': 'So for this example, what is 2a?',
            'correct_answer': correct,
            'explanation': explanation,
        },
    ]
    steps = ['Compute second differences.', 'Observe they are constant.', 'Use k = 2a to link the coefficient a to the second difference.']
    return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'terms': terms, 'second_differences': sec})


_SUBSKILLS = {
    'linear_next_terms': _gen_linear_next_terms,
    'linear_general_term': _gen_linear_find_general_term,
    'linear_terms_from_tn': _gen_linear_terms_from_tn,
    'linear_solve_for_n': _gen_linear_solve_for_n,
    'linear_number_of_terms': _gen_linear_number_of_terms,
    'quadratic_second_difference': _gen_quadratic_identify_and_a,
    'quadratic_general_term': _gen_quadratic_general_term_given_abc,
    'quadratic_terms_from_tn': _gen_quadratic_terms_from_tn,
    'quadratic_solve_for_n': _gen_quadratic_solve_for_n,
    'classify_sequence': _gen_classify_sequence,
    'context_matches': _gen_context_matches,
    'context_towers': _gen_context_towers,
    'quadratic_proof_style_scaffold': _gen_quadratic_proof_style_scaffold,
}


def generate_questions(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'mixed',
    count: int = 5,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold', 'mixed'}:
        question_type = 'mixed'

    if count < 1:
        count = 1
    if count > 30:
        count = 30

    rng = random.Random(seed if seed is not None else int(time.time()))

    if subskill == 'mixed' or not subskill:
        subskills = list(_SUBSKILLS.keys())
    else:
        subskills = [subskill] if subskill in _SUBSKILLS else list(_SUBSKILLS.keys())

    questions: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen_subskill = rng.choice(subskills)
        gen = _SUBSKILLS[chosen_subskill]

        if question_type == 'mixed':
            chosen_qtype = rng.choice(['typed', 'mcq', 'scaffold'])
        else:
            chosen_qtype = question_type

        q = gen(rng, difficulty, chosen_qtype)
        q = {
            'id': _make_id('g11_patseq', rng),
            'topic': 'Patterns and Sequences',
            'subskill': chosen_subskill,
            'difficulty': difficulty,
            **q,
        }
        _validate_question(q)
        questions.append(q)

    return questions
