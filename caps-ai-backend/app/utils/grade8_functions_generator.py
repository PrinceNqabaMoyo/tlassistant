import random
import time
from typing import Any, Dict, List, Optional, Tuple


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


def _fmt_int(n: int) -> str:
    return str(int(n))


def _pick_int(rng: random.Random, low: int, high: int) -> int:
    return int(rng.randint(low, high))


def _flow_apply(x: int, ops: List[Tuple[str, int]]) -> int:
    v = x
    for sym, k in ops:
        if sym == '+':
            v += k
        elif sym == '-':
            v -= k
        elif sym == '×':
            v *= k
        else:
            raise ValueError('Unsupported operator')
    return v


def _ops_to_words(ops: List[Tuple[str, int]]) -> str:
    parts: List[str] = []
    for sym, k in ops:
        if sym == '+':
            parts.append(f"add {k}")
        elif sym == '-':
            parts.append(f"subtract {k}")
        elif sym == '×':
            parts.append(f"multiply by {k}")
    return ', then '.join(parts)


def _ops_to_symbolic(ops: List[Tuple[str, int]]) -> str:
    expr = 'x'
    for sym, k in ops:
        if sym == '×':
            if expr == 'x':
                expr = f"{k}x"
            else:
                expr = f"{k}({expr})"
        elif sym == '+':
            expr = f"({expr}) + {k}"
        elif sym == '-':
            expr = f"({expr}) - {k}"
    if expr.startswith('(') and expr.endswith(')'):
        expr = expr[1:-1]
    return f"y = {expr}"


def _gen_constant_or_variable(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    scenarios = [
        ('Your age', 'number of fingers on your hands', 'variable, constant'),
        ('Number of calls you make', 'airtime left on your cell phone', 'variable, variable'),
        ('Number of identical houses to be built', 'number of bricks required', 'variable, variable'),
        ('Number of learners at a school', 'length of the school day', 'variable, constant'),
        ('Number of learners at a school', 'number of classrooms needed', 'variable, variable'),
    ]
    a, b, ans = rng.choice(scenarios)
    prompt = (
        "For the two quantities below, state whether each is constant or variable. "
        "Answer format: '<quantity1>: constant/variable; <quantity2>: constant/variable'.\n\n"
        f"1) {a}\n2) {b}"
    )
    explanation = 'A constant quantity stays the same; a variable quantity can change.'

    correct = f"1: {ans.split(',')[0].strip()}; 2: {ans.split(',')[1].strip()}"

    if qtype == 'mcq':
        options = [
            correct,
            '1: constant; 2: constant',
            '1: variable; 2: variable',
            '1: constant; 2: variable',
        ]
        options = list(dict.fromkeys(options))
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'q1': a, 'q2': b})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'q1': a, 'q2': b})


def _gen_flow_table_outputs(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    ops_bank_1 = [('+', 5), ('-', 5), ('×', 2), ('×', 3)]
    op1 = rng.choice(ops_bank_1)

    use_two = difficulty != 'easy' and rng.random() < 0.75
    if use_two:
        op2 = rng.choice([('+', 8), ('+', 15), ('-', 7), ('×', 4)])
        ops = [op1, op2]
    else:
        ops = [op1]

    inputs = [rng.randint(-3, 3) for _ in range(5)] if difficulty != 'easy' else [rng.randint(0, 5) for _ in range(5)]
    inputs = [int(x) for x in inputs]
    outputs = [_flow_apply(x, ops) for x in inputs]

    op_txt = ' then '.join([f"{s}{k}" if s != '×' else f"×{k}" for s, k in ops])
    prompt = (
        "A flow diagram applies operations to each input to get an output.\n"
        f"Operator(s): {op_txt}\n\n"
        f"Input numbers: {', '.join(_fmt_int(x) for x in inputs)}\n"
        "Write the output numbers in order (comma-separated)."
    )

    correct = ', '.join(_fmt_int(y) for y in outputs)
    explanation = f"Apply the operator(s) to each input: { _ops_to_words(ops) }."

    if qtype == 'mcq':
        wrong1 = ', '.join(_fmt_int(y + 1) for y in outputs)
        wrong2 = ', '.join(_fmt_int(y - 1) for y in outputs)
        wrong3 = ', '.join(_fmt_int((_flow_apply(x, ops[:-1]) if len(ops) > 1 else _flow_apply(x, [('+', 0)]))) for x in inputs)
        options = list(dict.fromkeys([correct, wrong1, wrong2, wrong3]))
        while len(options) < 4:
            options.append(correct)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'inputs': inputs, 'ops': ops, 'outputs': outputs})

    if qtype == 'scaffold':
        steps = [
            'Work line by line: the first input matches the first output, etc.',
            'Apply each operator in order (left to right through the boxes).',
            'Write the outputs as a comma-separated list.'
        ]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"First output (for input {inputs[0]}):",
                'correct_answer': _fmt_int(outputs[0]),
                'explanation': 'Apply the operator(s) to the first input.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'All outputs (comma-separated):',
                'correct_answer': correct,
                'explanation': 'Apply the same operator(s) to each input.'
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'inputs': inputs, 'ops': ops, 'outputs': outputs})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'inputs': inputs, 'ops': ops, 'outputs': outputs})


def _gen_symbolic_from_words(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    candidates = [
        [('×', 4), ('-', 7)],
        [('-', 7), ('×', 5)],
        [('-', 7), ('×', 5), ('+', 3)],
        [('×', 10), ('+', 15)],
        [('+', 15), ('×', 10)],
        [('×', 2), ('+', 3), ('×', 5)],
    ]
    ops = rng.choice(candidates if difficulty != 'easy' else candidates[:3])

    prompt = (
        "Write a symbolic formula using x for the input and y for the output.\n\n"
        f"Procedure: { _ops_to_words(ops) }.\n\n"
        "Answer format: y = ..."
    )

    correct = _ops_to_symbolic(ops)
    explanation = 'Start with x and apply each operation in order, writing the result as an expression for y.'

    if qtype == 'mcq':
        if ops == [('×', 4), ('-', 7)]:
            wrongs = ['y = 4x + 7', 'y = 4(x - 7)', 'y = (x - 7) + 4']
        elif ops == [('-', 7), ('×', 5)]:
            wrongs = ['y = 5x - 7', 'y = 5(x + 7)', 'y = (x - 7) + 5']
        else:
            wrongs = ['y = x', 'y = x + 7', 'y = 7x + 3']

        options = list(dict.fromkeys([correct, *wrongs]))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'ops': ops})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'ops': ops})


def _gen_word_from_symbolic(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    formulas = [
        [('×', 7), ('+', 10)],
        [('×', 2), ('+', 3)],
        [('×', 5), ('-', 2)],
        [('×', 3), ('+', 4)],
    ]
    if difficulty != 'easy':
        formulas.extend(
            [
                [('×', 11), ('+', 2)],
                [('×', 9), ('-', 5)],
                [('×', 8), ('+', 1)],
                [('×', 6), ('-', 3)],
            ]
        )

    ops = rng.choice(formulas)

    formula = _ops_to_symbolic(ops)
    prompt = (
        "Write a word formula that matches the symbolic formula below.\n\n"
        f"{formula}\n\n"
        "Answer format: 'To get y, ...'"
    )

    word = f"To get y, { _ops_to_words(ops) }."
    word = word.replace('multiply by', 'multiply x by').replace(', then ', ' then ').replace('add ', 'add ').replace('subtract ', 'subtract ')
    correct = word
    explanation = 'Read the formula from left to right: coefficient means multiply, and +/− means add/subtract.'

    if qtype == 'mcq':
        options = [
            correct,
            'To get y, add the constant first, then multiply x.',
            'To get y, multiply x by the constant term and add the coefficient.',
            'To get y, subtract the constant instead of adding it.'
        ]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'formula': formula})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'formula': formula})


def _gen_cartesian_coordinates_point(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    px = rng.choice([-4, -3, -2, 2, 3, 4, 5])
    py = rng.choice([-4, -3, -2, 2, 3, 4, 5])
    dx = rng.choice([2, 3, 4])
    dy = rng.choice([1, 2, 3])
    nx = px + dx
    ny = py - dy

    if px > 0 and py > 0:
        quad = "Quadrant I"
    elif px < 0 and py > 0:
        quad = "Quadrant II"
    elif px < 0 and py < 0:
        quad = "Quadrant III"
    else:
        quad = "Quadrant IV"

    prompt = (
        f"Refer to the Cartesian coordinate plane showing point \\(P\\).\n\n"
        f"1. Write down the coordinates of point \\(P\\) in the standard ordered-pair form \\((x; y)\\).\n"
        f"2. State which quadrant (Quadrant I, II, III, or IV) contains point \\(P\\).\n"
        f"3. Determine the coordinates of the image point \\(P'\\) if \\(P\\) is translated \\({dx}\\) units right and \\({dy}\\) units down."
    )

    correct = f"1. P({px}; {py})\n2. {quad}\n3. P'({nx}; {ny})"
    sol = (
        f"Step 1: Read the coordinates of point P from the axes:\n"
        f"The horizontal x-coordinate is {px} and the vertical y-coordinate is {py}, so P({px}; {py}).\n\n"
        f"Step 2: Identify the quadrant:\n"
        f"Since x is {'positive' if px > 0 else 'negative'} ({px}) and y is {'positive' if py > 0 else 'negative'} ({py}), point P lies in {quad}.\n\n"
        f"Step 3: Apply the translation ({dx} units right adds {dx} to x; {dy} units down subtracts {dy} from y):\n"
        f"x' = {px} + {dx} = {nx}\n"
        f"y' = {py} - {dy} = {ny}\n"
        f"Therefore, P'({nx}; {ny})."
    )

    diagram_spec = {
        "kind": "cartesian_point",
        "point": [px, py],
        "label": "P",
        "show_coords": False,
        "show_cast": False,
        "show_angle": False,
        "show_projection": True,
    }

    if qtype == 'mcq':
        distractors = [
            f"1. P({py}; {px}), 2. {quad}, 3. P'({py + dx}; {px - dy})",
            f"1. P({-px}; {py}), 2. {quad}, 3. P'({-px + dx}; {py - dy})",
            f"1. P({px}; {-py}), 2. {quad}, 3. P'({px + dx}; {-py - dy})",
        ]
        options = [correct] + distractors
        rng.shuffle(options)
        res = _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=sol, parameters={'x': px, 'y': py})
    else:
        res = _make_typed(prompt=prompt, correct_answer=correct, explanation=sol, parameters={'x': px, 'y': py})

    res['diagram_spec'] = diagram_spec
    if isinstance(diagram_spec, dict):
        diagram_spec.setdefault("diagram_role", "context")
    res['sample_answer'] = sol
    res['worked_solution'] = sol
    res['marks'] = 4
    res['marking_schema'] = {
        'total_marks': 4,
        'marking_points': [
            {'id': 'mp_1', 'desc': f'1. Correct coordinates of P: ({px}; {py})', 'marks': 1, 'editable': True},
            {'id': 'mp_2', 'desc': f'2. Correct quadrant identification: {quad}', 'marks': 1, 'editable': True},
            {'id': 'mp_3', 'desc': f'3. Correct translated x-coordinate: {px} + {dx} = {nx}', 'marks': 1, 'editable': True},
            {'id': 'mp_4', 'desc': f"4. Correct translated y-coordinate and ordered pair P'({nx}; {ny})", 'marks': 1, 'editable': True},
        ],
        'deductions': [],
        'carry_forward_rule': 'consequential_accuracy',
    }
    return res


def generate_grade8_functions_question(
    *,
    subskill: str = 'functions_and_relationships',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Functions and relationships'
    subskill = str(subskill or 'functions_and_relationships')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'constant_or_variable',
        'flow_table_outputs',
        'symbolic_from_words',
        'word_from_symbolic',
        'cartesian_point',
        'cartesian_coordinates',
    ]

    if subskill in {'functions_and_relationships', 'functions', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'constant_or_variable': _gen_constant_or_variable,
        'flow_table_outputs': _gen_flow_table_outputs,
        'symbolic_from_words': _gen_symbolic_from_words,
        'word_from_symbolic': _gen_word_from_symbolic,
        'cartesian_point': _gen_cartesian_coordinates_point,
        'cartesian_coordinates': _gen_cartesian_coordinates_point,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g8_fun'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
