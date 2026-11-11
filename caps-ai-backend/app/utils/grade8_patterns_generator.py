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
    prompt = f"Square pattern: Step {n} has how many dots in an n × n square array?"
    correct = str(ans)
    explanation = f"Square numbers follow T_n = n². For Step {n}: {n}² = {ans}."
    diag_spec = {'kind': 'dot_pattern', 'step_counts': [1, 4, 9, 16], 'arrangement': 'dots', 'diagram_role': 'context', 'show_difference': False}

    if qtype == 'mcq':
        options = [correct, str((n + 1) * (n + 1)), str(n * (n + 1)), str(ans + 2 * n + 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})

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
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})


def _gen_triangular_numbers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 12, 15, 20, 35]) if difficulty == 'hard' else rng.choice([5, 6, 7, 10, 12, 15])
    ans = n * (n + 1) // 2
    prompt = f"Triangular pattern: How many dots are in Figure {n} of the triangular number sequence?"
    correct = str(ans)
    explanation = f"Triangular numbers follow T_n = n(n+1)/2. For Figure {n}: {n} × {n+1} ÷ 2 = {ans}."
    diag_spec = {'kind': 'triangular_dot_pattern', 'step_counts': [1, 3, 6, 10], 'arrangement': 'dots', 'diagram_role': 'context', 'show_difference': False}

    if qtype == 'mcq':
        options = [correct, str((n + 1) * (n + 2) // 2), str(n * (n - 1) // 2), str(ans + n + 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})

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
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})


def _gen_cube_stack(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 10]) if difficulty != 'easy' else rng.choice([4, 5, 6])
    ans = n ** 3
    prompt = (
        f"A geometric sequence of cube stacks is built from unit cubes: "
        f"Stack 1 has 1 cube (1×1×1), Stack 2 has 8 cubes (2×2×2 block), and Stack 3 has 27 cubes (3×3×3 block).\n\n"
        f"How many unit cubes are required to construct Stack {n}?"
    )
    correct = str(ans)
    explanation = f"The sequence follows cubic numbers T_n = n³. For Stack {n}: {n}³ = {n} × {n} × {n} = {ans}."
    diag_spec = {
        'kind': 'isometric_cube_stack',
        'diagram_role': 'context',
        'step_counts': [1, 8, 27],
        'stack_dimensions': ['1×1×1', '2×2×2', '3×3×3'],
    }

    if qtype == 'mcq':
        options = [correct, str((n + 1) ** 3), str(n ** 2), str(n * n * (n + 1))]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, diagram_spec=diag_spec, parameters={'n': n})


def _gen_t_shape_numbers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    variants = [
        {"t1": 1, "d": 3, "arrangement": "tiles", "noun": "tiles"},
        {"t1": 4, "d": 3, "arrangement": "dots", "noun": "dots"},
        {"t1": 3, "d": 2, "arrangement": "tiles", "noun": "tiles"},
        {"t1": 2, "d": 4, "arrangement": "dots", "noun": "dots"},
        {"t1": 5, "d": 3, "arrangement": "tiles", "noun": "tiles"},
    ]
    v = rng.choice(variants)
    t1 = v["t1"]
    d = v["d"]
    c = t1 - d
    step_counts = [t1 + i * d for i in range(4)]
    n = rng.choice([8, 10, 12, 15, 20])
    ans = d * n + c
    c_fmt = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    rule_str = f"T_n = {d}n {c_fmt}" if c != 0 else f"T_n = {d}n"
    noun = v["noun"]

    prompt = (
        f"Refer to the geometric sequence of figures showing {noun} in Figure 1, Figure 2, and Figure 3: "
        f"\\({step_counts[0]};\\; {step_counts[1]};\\; {step_counts[2]};\\; \\dots\\)\n\n"
        f"1. State the constant difference \\(d\\) between consecutive figures.\n"
        f"2. Write down the general rule \\(T_n\\) for the number of {noun} in Figure \\(n\\).\n"
        f"3. Calculate the number of {noun} in Figure \\({n}\\)."
    )
    correct = f"1. d = {d}\n2. {rule_str}\n3. T_{n} = {ans} {noun}"
    explanation = (
        f"Step 1: Find the constant difference d between consecutive figures:\n"
        f"d = T_2 - T_1 = {step_counts[1]} - {step_counts[0]} = {d}\n\n"
        f"Step 2: Determine the general linear rule T_n = dn + c:\n"
        f"Substitute n = 1 and T_1 = {t1}: {d}(1) + c = {t1}, so c = {c}.\n"
        f"General rule: {rule_str}\n\n"
        f"Step 3: Substitute n = {n} into {rule_str}:\n"
        f"T_{n} = {d}({n}) {c_fmt} = {d * n} {c_fmt} = {ans} {noun}"
    )

    diag_spec = {
        "kind": "dot_pattern",
        "step_counts": step_counts,
        "arrangement": v["arrangement"],
        "show_difference": False,
    }

    if qtype == 'mcq':
        options = [
            correct,
            f"1. d = {d}; 2. T_n = {d}n + {abs(c) + 1}; 3. T_{n} = {d * n + abs(c) + 1}",
            f"1. d = {d + 1}; 2. {rule_str}; 3. T_{n} = {ans + d}",
            f"1. d = {d}; 2. {rule_str}; 3. T_{n} = {d * (n - 1) + c}",
        ]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        res = _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n, 'd': d, 't1': t1})
    elif qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f'What is the constant difference d in {step_counts[0]}, {step_counts[1]}, {step_counts[2]}, ... ?',
                'correct_answer': str(d),
                'explanation': f'Each figure adds {d} {noun}.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Use rule {rule_str} to calculate T_{n}:",
                'correct_answer': str(ans),
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the constant difference d between consecutive figures.',
            'Write a linear general rule T_n = dn + c.',
            f'Substitute n = {n} and calculate T_{n}.',
        ]
        res = _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n, 'd': d, 't1': t1})
    else:
        res = _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n, 'd': d, 't1': t1})

    res['diagram_spec'] = diag_spec
    if isinstance(diag_spec, dict):
        diag_spec.setdefault("diagram_role", "context")
    res['sample_answer'] = explanation
    res['worked_solution'] = explanation
    res['marks'] = 4
    res['marking_schema'] = {
        'total_marks': 4,
        'marking_points': [
            {'id': 'mp_1', 'desc': f'1. Constant difference d = {d}', 'marks': 1, 'editable': True},
            {'id': 'mp_2', 'desc': f'2. General linear rule {rule_str}', 'marks': 1, 'editable': True},
            {'id': 'mp_3', 'desc': f'3. Substitution of n = {n}: {d}({n}) {c_fmt}', 'marks': 1, 'editable': True},
            {'id': 'mp_4', 'desc': f'4. Final calculated value T_{n} = {ans} {noun}', 'marks': 1, 'editable': True},
        ],
        'deductions': [],
        'carry_forward_rule': 'consequential_accuracy',
    }
    return res


def _gen_tile_n_shape(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    return _gen_t_shape_numbers(rng, difficulty, qtype)


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
        'dot_pattern',
    ]

    if subskill in {'patterns', 'mixed'}:
        if seed is not None and (seed % 3 == 0):
            subskill = 'dot_pattern'
        else:
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
        'dot_pattern': _gen_t_shape_numbers,
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

    if 'diagram_spec' not in out or not out['diagram_spec']:
        out['diagram_spec'] = {
            'kind': 'sequence_strip' if subskill in ('next_terms_arithmetic', 'next_terms_geometric', 'growing_difference', 'linear_nth_term') else 'dot_pattern',
            'diagram_role': 'context',
            'subskill': subskill,
            'step_counts': [1, 4, 7, 10],
            'arrangement': 'tiles',
            'show_difference': False
        }
    if isinstance(out.get('diagram_spec'), dict):
        out['diagram_spec'].setdefault('diagram_role', 'context')

    _validate_question(out)
    return out
