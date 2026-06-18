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


def _sequence_terms_geometric_int(a1: int, r: int, n: int) -> List[int]:
    out = [a1]
    for _ in range(n - 1):
        out.append(out[-1] * r)
    return out


def _gen_next_terms_arithmetic(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a1 = rng.randint(0, 20) if difficulty == 'easy' else rng.randint(-20, 30)
    d_choices = [2, 3, 4, 5] if difficulty == 'easy' else ([3, 4, 5, 6, 7] if difficulty == 'medium' else [4, 5, 6, 8, 9, 10])
    d = rng.choice(d_choices)
    if difficulty != 'easy' and rng.random() < 0.35:
        d *= -1

    shown_n = 4
    ask_n = 3
    terms = _sequence_terms_arithmetic(a1, d, shown_n + ask_n)
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"Arithmetic sequence: add {d} each time."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = ', '.join(str(t + d) for t in nxt)
        opt3 = ', '.join(str(t - d) for t in nxt)
        opt4 = ', '.join(str(t + rng.choice([-1, 1]) * (abs(d) + 1)) for t in nxt)
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
                'prompt': f"Find the constant difference: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(shown[1] - shown[0]),
                'explanation': 'Subtract consecutive terms to find the difference.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next term after {shown[-1]}: {shown[-1]} + ({d}) = ?",
                'correct_answer': str(nxt[0]),
                'explanation': 'Add the constant difference to extend the sequence.',
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
            'Add the difference repeatedly to get the next terms.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'shown': shown, 'next': nxt})


def _gen_next_terms_geometric(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    r_choices = [2, 3] if difficulty == 'easy' else ([2, 3, 4] if difficulty == 'medium' else [2, 3, 4, 5])
    r = rng.choice(r_choices)

    a1_choices = [1, 2, 3, 4, 5] if difficulty != 'hard' else [1, 2, 3, 4, 5, 6, 8]
    a1 = rng.choice(a1_choices)

    shown_n = 4
    ask_n = 3
    terms = _sequence_terms_geometric_int(a1, r, shown_n + ask_n)
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"Geometric sequence: multiply by {r} each time."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = ', '.join(str(t * r) for t in nxt)
        opt3 = ', '.join(str(t + r) for t in nxt)
        opt4 = ', '.join(str(t + rng.choice([-1, 1]) * r) for t in nxt)
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
                'prompt': f"Find the ratio: {shown[1]} ÷ {shown[0]} = ?",
                'correct_answer': str(r),
                'explanation': 'Divide consecutive terms to find the ratio.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next term after {shown[-1]}: {shown[-1]} × ({r}) = ?",
                'correct_answer': str(nxt[0]),
                'explanation': 'Multiply by the constant ratio to extend the sequence.',
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
            'Find the ratio between consecutive terms.',
            'Check it is constant.',
            'Multiply by the ratio repeatedly to get the next terms.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})


def _gen_square_numbers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    shown_n = 4
    ask_n = 3

    start_n = rng.choice([1, 2, 3]) if difficulty == 'easy' else rng.choice([1, 2, 3, 4])
    ns = list(range(start_n, start_n + shown_n + ask_n))
    terms = [n * n for n in ns]
    shown = terms[:shown_n]
    nxt = terms[shown_n:]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... (square numbers) Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = 'These are square numbers: n².'

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the rule for square numbers? (Use n^2)',
                'correct_answer': 'n^2',
                'explanation': 'Square numbers follow n².',
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
            'Recognise the sequence pattern.',
            'Identify it as square numbers (n²).',
            'Continue the squares.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n_start': start_n, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n_start': start_n, 'shown': shown, 'next': nxt})


def _gen_growing_difference(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Differences increase by 2 or 1: e.g. 3,6,11,18,... or 1,2,4,7,11,...
    start = rng.choice([0, 1, 2, 3, 5])
    first_diff = rng.choice([1, 2, 3]) if difficulty == 'easy' else rng.choice([2, 3, 4, 5])
    diff_step = rng.choice([1, 2]) if difficulty != 'hard' else rng.choice([1, 2, 3])

    shown_n = 5
    ask_n = 3

    diffs = [first_diff + diff_step * i for i in range(shown_n + ask_n - 1)]
    terms = [start]
    for d in diffs:
        terms.append(terms[-1] + d)

    shown = terms[:shown_n]
    nxt = terms[shown_n:shown_n + ask_n]

    prompt = f"Sequence: {'; '.join(str(t) for t in shown)}; ... The differences are changing. Write the next {ask_n} terms (comma-separated)."
    correct = ', '.join(str(t) for t in nxt)
    explanation = f"The differences are {', '.join(str(d) for d in diffs[:shown_n - 1])} and they increase by {diff_step} each time."

    if qtype == 'scaffold':
        d1 = shown[1] - shown[0]
        d2 = shown[2] - shown[1]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Find the first difference: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(d1),
                'explanation': 'Subtract consecutive terms to find differences.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Find the next difference: {shown[2]} − {shown[1]} = ?",
                'correct_answer': str(d2),
                'explanation': 'Differences are changing in this sequence.',
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
            'Find differences between consecutive terms.',
            'See how the differences change.',
            'Use that rule to extend the sequence.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'start': start, 'first_diff': first_diff, 'diff_step': diff_step, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'start': start, 'first_diff': first_diff, 'diff_step': diff_step, 'shown': shown, 'next': nxt})


def _gen_build_sequence_from_instruction(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['add', 'subtract', 'multiply', 'divide'])

    if kind in {'add', 'subtract'}:
        start = rng.choice([1, 5, 8, 10, 12, 20]) if difficulty == 'easy' else rng.randint(-20, 40)
        step = rng.choice([2, 3, 4, 5, 8, 10]) if difficulty != 'hard' else rng.choice([3, 4, 5, 6, 7, 8, 10, 12])
        step = step if kind == 'add' else -step
        terms = _sequence_terms_arithmetic(start, step, 8)
        op_text = f"add {abs(step)}" if step > 0 else f"subtract {abs(step)}"
        prompt = f"Start with {start} and {op_text} repeatedly. Write the first 8 terms (comma-separated)."
        correct = ', '.join(str(t) for t in terms)
        explanation = f"Start at {start}, then {op_text} each time."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'start': start, 'step': step, 'terms': terms})

    if kind == 'multiply':
        r = rng.choice([2, 3]) if difficulty != 'hard' else rng.choice([2, 3, 4])
        start = rng.choice([1, 2, 3, 4, 5])
        terms = _sequence_terms_geometric_int(start, r, 8)
        prompt = f"Start with {start} and multiply by {r} repeatedly. Write the first 8 terms (comma-separated)."
        correct = ', '.join(str(t) for t in terms)
        explanation = f"Multiply by {r} each time."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'start': start, 'r': r, 'terms': terms})

    # divide
    r = 2
    start = rng.choice([256, 128, 64]) if difficulty != 'hard' else rng.choice([512, 256, 128])
    terms = [start]
    for _ in range(7):
        terms.append(terms[-1] // r)
    prompt = f"Start with {start} and divide by {r} repeatedly. Write the first 8 terms (comma-separated)."
    correct = ', '.join(str(t) for t in terms)
    explanation = f"Divide by {r} each time."
    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'start': start, 'r': r, 'terms': terms})


def generate_grade9_patterns_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Numeric and Geometric Patterns'
    subskill = str(subskill or 'mixed')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'next_terms_arithmetic',
        'next_terms_geometric',
        'square_numbers',
        'growing_difference',
        'build_sequence_from_instruction',
    ]

    if subskill in {'patterns', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'next_terms_arithmetic': _gen_next_terms_arithmetic,
        'next_terms_geometric': _gen_next_terms_geometric,
        'square_numbers': _gen_square_numbers,
        'growing_difference': _gen_growing_difference,
        'build_sequence_from_instruction': _gen_build_sequence_from_instruction,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    # build-sequence is kept typed (it's already scaffold-ish)
    if subskill == 'build_sequence_from_instruction':
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g9_pat'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
