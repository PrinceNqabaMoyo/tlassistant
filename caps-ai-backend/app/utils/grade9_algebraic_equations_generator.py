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


def _fmt_int(n: int) -> str:
    return str(int(n))


def _normalize(s: str) -> str:
    return str(s).strip().replace('−', '-').replace(' ', '')


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


def _gen_solve_one_step(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    pattern = _choice(rng, ['ax_equals_c', 'x_plus_b', 'x_minus_b'])

    if pattern == 'ax_equals_c':
        a = int(_choice(rng, [2, 3, 4, 5, 6, 8, 10] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
        x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6] if difficulty != 'easy' else [1, 2, 3, 4, 5, 6]))
        c = a * x
        eq = f"{a}x = {c}"
        correct = _fmt_int(x)
        explanation = f"Divide both sides by {a}: x = {c} ÷ {a} = {x}."
        inverse_step = f"Divide both sides by {a}."
    elif pattern == 'x_plus_b':
        b = int(_choice(rng, [2, 3, 4, 5, 7, 8, 10] if difficulty != 'hard' else [1, 2, 3, 4, 5, 7, 8, 10, 12, 15]))
        x = int(_choice(rng, [-12, -10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12]))
        c = x + b
        eq = f"x + {b} = {c}"
        correct = _fmt_int(x)
        explanation = f"Subtract {b} from both sides: x = {c} − {b} = {x}."
        inverse_step = f"Subtract {b} from both sides."
    else:
        b = int(_choice(rng, [2, 3, 4, 5, 7, 8, 10] if difficulty != 'hard' else [1, 2, 3, 4, 5, 7, 8, 10, 12, 15]))
        x = int(_choice(rng, [-12, -10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12]))
        c = x - b
        eq = f"x - {b} = {c}"
        correct = _fmt_int(x)
        explanation = f"Add {b} to both sides: x = {c} + {b} = {x}."
        inverse_step = f"Add {b} to both sides."

    prompt = f"Solve for x: {eq}"

    if qtype == 'mcq':
        x_int = int(correct)
        options = _make_unique_options(rng, correct, [_fmt_int(x_int + 1), _fmt_int(x_int - 1), _fmt_int(x_int + 2), _fmt_int(x_int - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What single inverse operation should you do first?',
                'correct_answer': inverse_step,
                'explanation': 'Use the inverse of the operation applied to x.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final value of x:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify what is being done to x.',
            'Do the inverse operation on both sides.',
            'Check by substitution.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})


def _gen_solve_two_step(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = int(_choice(rng, [2, 3, 4, 5, 6] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9]))
    b = int(_choice(rng, [-15, -12, -10, -8, -7, -5, -3, -2, 2, 3, 5, 7, 8, 10, 12, 15]))
    x = int(_choice(rng, [-8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8] if difficulty != 'easy' else [1, 2, 3, 4, 5, 6, 8]))
    c = a * x + b

    eq = f"{a}x" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else '')) + f" = {c}"
    prompt = f"Solve for x: {eq}"
    correct = _fmt_int(x)
    rhs_after = c - b
    explanation = f"Undo the +/− constant first, then divide by {a}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [_fmt_int(x + 1), _fmt_int(x - 1), _fmt_int(x + 2), _fmt_int(x - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'After moving the constant term, what does the equation become on the right-hand side?',
                'correct_answer': _fmt_int(rhs_after),
                'explanation': 'Isolate the ax term by adding/subtracting the constant on both sides.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now solve {a}x = {rhs_after}. What is x?",
                'correct_answer': correct,
                'explanation': f"Divide both sides by {a}.",
            },
        ]
        steps = [
            'Undo the constant term (add/subtract on both sides).',
            'Undo the multiplication (divide on both sides).',
            'Check by substitution.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})


def _gen_brackets_linear(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    k = int(_choice(rng, [2, 3, 4, 5] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7]))
    a = int(_choice(rng, [1, 2, 3, 4] if difficulty != 'hard' else [1, 2, 3, 4, 5, 6]))
    b = int(_choice(rng, [-12, -10, -8, -7, -5, -3, -2, 2, 3, 5, 7, 8, 10, 12]))
    x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6] if difficulty != 'easy' else [1, 2, 3, 4, 5, 6]))

    rhs = k * (a * x + b)
    eq = f"{k}({a}x" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else '')) + f") = {rhs}"

    prompt = f"Solve for x: {eq}"
    correct = _fmt_int(x)
    explanation = f"Divide both sides by {k} to remove the brackets multiplier, then solve the remaining linear equation."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [_fmt_int(x + 1), _fmt_int(x - 1), _fmt_int(x + 2), _fmt_int(x - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'k': k, 'a': a, 'b': b, 'rhs': rhs})

    if qtype == 'scaffold':
        after_div = rhs // k
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"First divide both sides by {k}. What is the new right-hand side?",
                'correct_answer': _fmt_int(after_div),
                'explanation': 'Undo multiplication outside brackets by dividing both sides.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Now solve for x:',
                'correct_answer': correct,
                'explanation': 'Solve the resulting linear equation.',
            },
        ]
        steps = [
            'Undo the multiplication outside the brackets.',
            'Undo the constant term.',
            'Undo the coefficient of x.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'k': k, 'a': a, 'b': b, 'rhs': rhs})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'k': k, 'a': a, 'b': b, 'rhs': rhs})


def _gen_inspection_table(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = int(_choice(rng, [1, 2, 3, 4, 5] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8]))
    b = int(_choice(rng, [-10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10]))

    if difficulty == 'easy':
        x_vals = [-2, -1, 0, 1, 2, 3, 4]
    elif difficulty == 'medium':
        x_vals = [-3, -2, -1, 0, 1, 2, 3, 4]
    else:
        x_vals = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

    x_solution = int(_choice(rng, x_vals))
    rhs = a * x_solution + b

    if bool(_choice(rng, [True, False])):
        rhs = rhs + int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]))
        if rhs == a * x_solution + b:
            rhs += 1

    eq = f"{a}x" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else '')) + f" = {rhs}"

    prompt = f"Use inspection (try values) to find x: {eq}"

    solved = None
    for xv in x_vals:
        if a * xv + b == rhs:
            solved = xv
            break

    if solved is None:
        correct = 'no solution in the given set'
        explanation = 'Try each given x value. None makes the left side equal the right side.'
    else:
        correct = _fmt_int(solved)
        explanation = f"Test the given x values until {a}×{solved} {('+' if b >= 0 else '-') } {abs(b)} equals {rhs}."

    if qtype == 'mcq':
        options = [str(v) for v in x_vals]
        options.append('no solution in the given set')
        options = list(dict.fromkeys(options))
        rng.shuffle(options)
        if str(correct) not in options:
            options.append(str(correct))
        options = options[:6]
        if str(correct) not in options:
            options[0] = str(correct)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(correct), explanation=explanation, parameters={'a': a, 'b': b, 'rhs': rhs, 'x_values': x_vals})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute the left side when x = {x_vals[0]}.",
                'correct_answer': _fmt_int(a * x_vals[0] + b),
                'explanation': 'Substitute and calculate.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What value of x works (or write "no solution in the given set")?',
                'correct_answer': str(correct),
                'explanation': explanation,
            },
        ]
        steps = [
            'Substitute values for x from the list.',
            'Calculate the left-hand side each time.',
            'Stop when both sides are equal.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(correct), explanation=explanation, parameters={'a': a, 'b': b, 'rhs': rhs, 'x_values': x_vals})

    return _make_typed(prompt=prompt, correct_answer=str(correct), explanation=explanation, parameters={'a': a, 'b': b, 'rhs': rhs, 'x_values': x_vals})


def _gen_word_problem_linear(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    scenarios = [
        ('A room rental costs a deposit of R{deposit} and then R{rate} per day. You have R{total}. For how many days can you rent?', '80x + 400 = 720'),
        ('A car rental costs a fixed fee of R{deposit} plus R{rate} per day. If the total cost is R{total}, how many days is that?', '260x + 310 = 2910'),
    ]

    deposit = int(_choice(rng, [200, 250, 300, 320, 400] if difficulty != 'hard' else [180, 200, 250, 300, 320, 400, 450]))
    rate = int(_choice(rng, [50, 60, 70, 80, 90, 120, 150] if difficulty != 'easy' else [60, 70, 80, 90, 120]))

    days = int(_choice(rng, [4, 5, 6, 7, 8, 9, 10, 12] if difficulty != 'hard' else [3, 4, 5, 6, 7, 8, 9, 10, 12, 14]))
    total = deposit + rate * days

    template, _ = _choice(rng, scenarios)
    prompt = template.format(deposit=deposit, rate=rate, total=total)

    eq = f"{rate}x + {deposit} = {total}"
    correct = _fmt_int(days)
    explanation = f"Set up {eq}. Subtract {deposit}: {rate}x = {total - deposit}. Divide by {rate}: x = {days}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [_fmt_int(days + 1), _fmt_int(days - 1), _fmt_int(days + 2), _fmt_int(days - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'rate': rate, 'deposit': deposit, 'total': total, 'equation': eq})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the equation in the form ax + b = c:',
                'correct_answer': eq,
                'explanation': 'Fixed cost is b, daily cost is ax.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Solve for x (number of days):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify fixed cost (deposit) and variable cost (per day).',
            'Write an equation for total cost.',
            'Solve using inverse operations.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'rate': rate, 'deposit': deposit, 'total': total, 'equation': eq})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'rate': rate, 'deposit': deposit, 'total': total, 'equation': eq})


def _gen_exponent_same_base(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = int(_choice(rng, [2, 3, 5, 10] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 10]))
    x_val = int(_choice(rng, [-3, -2, -1, 0, 1, 2, 3, 4, 5] if difficulty != 'easy' else [0, 1, 2, 3, 4]))
    shift = int(_choice(rng, [-3, -2, -1, 1, 2, 3] if difficulty != 'easy' else [-2, -1, 1, 2]))

    power = x_val + shift
    rhs = base ** power

    prompt = f"Solve for x: {base}^(x {'+' if shift >= 0 else '-'} {abs(shift)}) = {rhs}"
    correct = _fmt_int(x_val)
    explanation = f"Rewrite {rhs} as {base}^{power}, then equate exponents: x {'+' if shift >= 0 else '-'} {abs(shift)} = {power} so x = {x_val}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [_fmt_int(x_val + 1), _fmt_int(x_val - 1), _fmt_int(x_val + 2), _fmt_int(x_val - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'shift': shift, 'rhs': rhs})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Write {rhs} as {base}^k. What is k?",
                'correct_answer': _fmt_int(power),
                'explanation': 'Find the exponent that makes the power equal the right-hand side.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Now solve for x:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Isolate the exponential term.',
            'Write both sides with the same base.',
            'Equate exponents and solve.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'base': base, 'shift': shift, 'rhs': rhs})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'shift': shift, 'rhs': rhs})


def _gen_power_equation_variable_base(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    power = int(_choice(rng, [2, 3, 4, 5] if difficulty != 'hard' else [2, 3, 4, 5, 6]))
    x_val = int(_choice(rng, [2, 3, 4, 5, 6] if difficulty != 'easy' else [2, 3, 4, 5]))
    rhs = x_val ** power

    prompt = f"Solve for x: x^{power} = {rhs}"
    correct = _fmt_int(x_val)
    explanation = f"Recognize {rhs} as {x_val}^{power}, so x = {x_val}."

    if qtype == 'mcq':
        options = _make_unique_options(rng, correct, [_fmt_int(x_val + 1), _fmt_int(x_val - 1), _fmt_int(x_val + 2), _fmt_int(x_val - 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'power': power, 'rhs': rhs})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Which number to the power {power} gives {rhs}?",
                'correct_answer': correct,
                'explanation': 'Use known powers (squares/cubes/etc.).',
            },
        ]
        steps = [
            'Recall common powers.',
            'Find the base that matches the given power.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'power': power, 'rhs': rhs})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'power': power, 'rhs': rhs})


def generate_grade9_algebraic_equations_question(
    *,
    subskill: str = 'algebraic_equations',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Algebraic equations'
    subskill = str(subskill or 'algebraic_equations')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'inspection_table',
        'solve_one_step',
        'solve_two_step',
        'solve_brackets',
        'word_problem_linear',
        'exponent_equation_same_base',
        'power_equation_variable_base',
    ]

    if subskill in {'algebraic_equations', 'equations', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'inspection_table': _gen_inspection_table,
        'solve_one_step': _gen_solve_one_step,
        'solve_two_step': _gen_solve_two_step,
        'solve_brackets': _gen_brackets_linear,
        'word_problem_linear': _gen_word_problem_linear,
        'exponent_equation_same_base': _gen_exponent_same_base,
        'power_equation_variable_base': _gen_power_equation_variable_base,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g9_eq'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
