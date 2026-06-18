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


def _sequence_terms_arithmetic(a1: int, d: int, n: int) -> List[int]:
    return [a1 + d * i for i in range(n)]


def _sequence_terms_geometric(a1: int, r: int, n: int) -> List[int]:
    out = [a1]
    for _ in range(n - 1):
        out.append(out[-1] * r)
    return out


def _gen_next_terms_arithmetic(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a1 = rng.randint(-10, 20) if difficulty != 'easy' else rng.randint(0, 20)
    d_choices = [1, 2, 3, 4, 5] if difficulty == 'easy' else ([2, 3, 4, 5, 6, 7] if difficulty == 'medium' else [3, 4, 5, 6, 8, 9])
    d = rng.choice(d_choices) * rng.choice([-1, 1]) if difficulty != 'easy' else rng.choice(d_choices)

    shown_n = 5
    ask_n = 3
    terms = _sequence_terms_arithmetic(a1, d, shown_n + ask_n)
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"This is an arithmetic sequence with constant difference {d}."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = ', '.join(str(t + d) for t in nxt)
        opt3 = ', '.join(str(t - d) for t in nxt)
        opt4 = ', '.join(str(t + rng.choice([-1, 1])) for t in nxt)
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the constant difference between the first two terms: {shown[1]} − {shown[0]}?",
                'correct_answer': str(shown[1] - shown[0]),
                'explanation': 'Subtract consecutive terms to find the constant difference.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Add the difference to the last shown term: {shown[-1]} + ({d}) = ?",
                'correct_answer': str(nxt[0]),
                'explanation': 'Add the constant difference to get the next term.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next {ask_n} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the difference between consecutive terms.',
            'Check it is constant.',
            'Add the difference repeatedly to extend the sequence.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})


def _gen_next_terms_geometric(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    r_choices = [2, 3] if difficulty == 'easy' else ([2, 3, 4, -2] if difficulty == 'medium' else [2, 3, 4, 5, -2, -3])
    r = rng.choice(r_choices)

    a1_choices = [1, 2, 3, 4, 6] if difficulty != 'hard' else [1, 2, 3, 4, 6, 8, 9]
    a1 = rng.choice(a1_choices)
    if difficulty == 'hard' and r < 0:
        a1 *= rng.choice([-1, 1])

    shown_n = 5
    ask_n = 3
    terms = _sequence_terms_geometric(a1, r, shown_n + ask_n)
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"This is a geometric sequence with constant ratio {r} (multiply each term by {r})."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = ', '.join(str(t * r) for t in nxt)
        opt3 = ', '.join(str(int(t / r)) if r != 0 else str(t) for t in nxt)
        opt4 = ', '.join(str(t + rng.choice([-1, 1]) * abs(r)) for t in nxt)
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the ratio between the first two terms: {shown[1]} ÷ {shown[0]}?",
                'correct_answer': str(r),
                'explanation': 'Divide consecutive terms to find the constant ratio.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Multiply the last shown term by the ratio: {shown[-1]} × ({r}) = ?",
                'correct_answer': str(nxt[0]),
                'explanation': 'Multiply by the constant ratio to get the next term.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next {ask_n} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the ratio between consecutive terms (divide).',
            'Check it stays the same.',
            'Multiply by the ratio repeatedly to extend the sequence.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})


def _gen_growing_difference(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Pattern where differences increase by a constant each time (e.g., +7, +9, +11, ...)
    start = rng.randint(0, 20)
    first_diff = rng.choice([3, 5, 7]) if difficulty == 'easy' else rng.choice([5, 7, 9])
    diff_step = 2 if difficulty != 'hard' else rng.choice([1, 2, 3])

    shown_n = 5
    ask_n = 3

    diffs = [first_diff + diff_step * i for i in range(shown_n + ask_n - 1)]
    terms = [start]
    for d in diffs:
        terms.append(terms[-1] + d)

    shown = terms[:shown_n]
    nxt = terms[shown_n:shown_n + ask_n]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... The differences increase each time. Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"The differences are {', '.join(str(d) for d in diffs[:shown_n - 1])} and they increase by {diff_step} each time."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = ', '.join(str(t + diff_step) for t in nxt)
        opt3 = ', '.join(str(t - diff_step) for t in nxt)
        opt4 = ', '.join(str(t + rng.choice([-1, 1]) * first_diff) for t in nxt)
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'start': start, 'first_diff': first_diff, 'diff_step': diff_step, 'shown': shown, 'next': nxt})

    if qtype == 'scaffold':
        d1 = shown[1] - shown[0]
        d2 = shown[2] - shown[1]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Find the first difference: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(d1),
                'explanation': 'Subtract consecutive terms to find the differences.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Find the next difference: {shown[2]} − {shown[1]} = ?",
                'correct_answer': str(d2),
                'explanation': 'Differences are changing in this pattern.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"How does the difference change: {d2} − {d1} = ?",
                'correct_answer': str(d2 - d1),
                'explanation': 'The differences increase by a constant amount.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next {ask_n} terms (comma-separated):",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the differences between consecutive terms.',
            'Look for how the differences themselves change.',
            'Use the changing-differences rule to extend the sequence.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'start': start, 'first_diff': first_diff, 'diff_step': diff_step, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'start': start, 'first_diff': first_diff, 'diff_step': diff_step, 'shown': shown, 'next': nxt})


def _gen_linear_nth_term(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Term = m*n + c
    m = rng.choice([2, 3, 4, 5]) if difficulty != 'hard' else rng.choice([3, 4, 5, 6, 7])
    c = rng.randint(-5, 10) if difficulty != 'easy' else rng.randint(0, 10)

    n_ask = rng.choice([7, 10, 28, 54, 100]) if difficulty != 'easy' else rng.choice([7, 10, 12, 20])
    term = m * n_ask + c

    prompt = (
        f"A sequence follows the rule: term = {m} × (position) + {c}. "
        f"Find term number {n_ask}."
    )
    correct = str(term)
    explanation = f"Substitute position {n_ask}: {m}×{n_ask}+{c} = {term}."

    if qtype == 'mcq':
        options = [correct, str(term + m), str(term - m), str(m * (n_ask + 1) + c)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'m': m, 'c': c, 'n': n_ask})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute {m} × {n_ask} = ?",
                'correct_answer': str(m * n_ask),
                'explanation': 'Multiply the position by the coefficient.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now add {c}: {m * n_ask} + ({c}) = ?",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify the rule that links position to term.',
            'Substitute the required position.',
            'Calculate step-by-step (multiply, then add).',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'m': m, 'c': c, 'n': n_ask})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'m': m, 'c': c, 'n': n_ask})


def _gen_square_numbers_geometric(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 12, 15, 20]) if difficulty != 'easy' else rng.choice([5, 6, 7, 10, 12])
    ans = n * n
    prompt = f"Square pattern: Type {n} has how many panes/dots (n²)?"
    correct = str(ans)
    explanation = f"Square numbers follow n². So {n}² = {ans}."

    if qtype == 'mcq':
        options = [correct, str((n + 1) * (n + 1)), str(n * (n + 1)), str(ans + 2 * n + 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Write the rule for square patterns: n². Now compute {n}² = ?",
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = [
            'Recognise a square pattern (n by n).',
            'Use the rule n².',
            'Substitute n and calculate.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_triangular_numbers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 12, 15, 20, 35]) if difficulty == 'hard' else rng.choice([5, 6, 7, 10, 12, 15])
    ans = n * (n + 1) // 2
    prompt = f"Triangular pattern: How many circles are in picture {n}?"
    correct = str(ans)
    explanation = f"Triangular numbers follow n(n+1)/2. So {n}×{n+1}÷2 = {ans}."

    if qtype == 'mcq':
        options = [correct, str((n + 1) * (n + 2) // 2), str(n * (n - 1) // 2), str(ans + n + 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute n(n+1): {n}×{n+1} = ?",
                'correct_answer': str(n * (n + 1)),
                'explanation': 'Multiply consecutive numbers.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now divide by 2: {n * (n + 1)} ÷ 2 = ?",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Use the triangular number rule: n(n+1)/2.',
            'Multiply n by (n+1).',
            'Divide by 2 to get the total.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_cube_stack(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 10]) if difficulty != 'easy' else rng.choice([4, 5, 6])
    ans = n ** 3
    prompt = f"Cube stack: Stack {n} forms an {n}×{n}×{n} cube. How many small cubes?"
    correct = str(ans)
    explanation = f"Number of cubes is n³. So {n}³ = {ans}."

    if qtype == 'mcq':
        options = [correct, str((n + 1) ** 3), str(n ** 2), str(n * n * (n + 1))]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_t_shape_numbers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Doc table: 1,4,7,10,... => 3n - 2
    n = rng.choice([5, 6, 15, 20]) if difficulty != 'easy' else rng.choice([5, 6, 10, 12])
    ans = 3 * n - 2
    prompt = f"T-shape pattern: number of tiles is 1, 4, 7, 10, ... Find the number of tiles in pattern {n}."
    correct = str(ans)
    explanation = f"This is linear with constant difference 3, so the rule is 3n − 2. For n={n}: 3×{n}−2={ans}."

    if qtype == 'mcq':
        options = [correct, str(3 * n + 2), str(3 * n - 1), str(3 * (n - 1) - 2)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the constant difference in 1, 4, 7, 10, ... ?',
                'correct_answer': '3',
                'explanation': 'Each pattern adds 3 tiles.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Use rule 3n − 2. Compute 3×{n} − 2 = ?",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the constant difference between patterns.',
            'Write a linear rule in terms of n.',
            'Substitute n and calculate.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_tile_n_shape(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Matches doc's rearrangement labels: 3×1+2=5, 3×2+2=8, 3×3+2=11
    n = rng.choice([17, 23, 50]) if difficulty != 'easy' else rng.choice([10, 12, 17, 23])
    ans = 3 * n + 2
    prompt = f"Tile 'n' pattern: the rule is 3×n + 2. How many tiles in figure {n}?"
    correct = str(ans)
    explanation = f"Use the rule 3n + 2. For n={n}: 3×{n}+2={ans}."

    if qtype == 'mcq':
        options = [correct, str(3 * n - 2), str(2 * n + 3), str(3 * (n + 1) + 2)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def generate_grade8_patterns_question(
    *,
    subskill: str = 'patterns',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Numeric and Geometric Patterns'
    subskill = str(subskill or 'patterns')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'next_terms_arithmetic',
        'next_terms_geometric',
        'growing_difference',
        'linear_nth_term',
        'square_numbers',
        'triangular_numbers',
        'cube_numbers',
        't_shape_numbers',
        'tile_n_shape',
    ]

    if subskill in {'patterns', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'next_terms_arithmetic': _gen_next_terms_arithmetic,
        'next_terms_geometric': _gen_next_terms_geometric,
        'growing_difference': _gen_growing_difference,
        'linear_nth_term': _gen_linear_nth_term,
        'square_numbers': _gen_square_numbers_geometric,
        'triangular_numbers': _gen_triangular_numbers,
        'cube_numbers': _gen_cube_stack,
        't_shape_numbers': _gen_t_shape_numbers,
        'tile_n_shape': _gen_tile_n_shape,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g8_pat'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
