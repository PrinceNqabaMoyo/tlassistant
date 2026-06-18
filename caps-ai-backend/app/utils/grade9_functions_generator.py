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


def _build_linear_graph_payload(*, m: int, c: int) -> Dict[str, Any]:
    x_min, x_max = -10, 10
    y_values = [m * x + c for x in [x_min, x_max]]
    y_min = min(-10, min(y_values) - 2)
    y_max = max(10, max(y_values) + 2)
    y_min = int(max(-25, y_min))
    y_max = int(min(25, y_max))

    pts = [
        {'x': 0, 'y': c, 'label': '(0, y-intercept)'},
        {'x': 1, 'y': m + c, 'label': '(1, m+c)'},
    ]

    return {
        'type': 'linear',
        'm': m,
        'c': c,
        'x_range': [x_min, x_max],
        'y_range': [y_min, y_max],
        'grid_step': 1,
        'points': pts,
        'show_grid': True,
        'show_axes': True,
        'show_labels': True,
    }


def _gen_flow_table_outputs(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    ops_bank = [('+', 20), ('+', 15), ('-', 7), ('×', 5), ('×', 4)]
    op1 = rng.choice(ops_bank)
    use_two = difficulty != 'easy' and rng.random() < 0.8
    ops = [op1]
    if use_two:
        ops.append(rng.choice([('+', 20), ('+', 15), ('-', 7)]))

    if difficulty == 'easy':
        inputs = [rng.randint(-5, -1) for _ in range(5)]
    else:
        inputs = [rng.randint(-6, 6) for _ in range(6)]

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
        wrong3 = ', '.join(_fmt_int(_flow_apply(x, ops[:-1] if len(ops) > 1 else [('+', 0)])) for x in inputs)
        options = list(dict.fromkeys([correct, wrong1, wrong2, wrong3]))
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


def _gen_outputs_for_sets(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Based on Gr9 doc: 50 - 5x applied to Set A (1..9) and Set B (20..90 step 10)
    m = -5
    c = 50
    set_a = list(range(1, 10))
    set_b = list(range(20, 100, 10))

    which = 'A' if rng.random() < 0.5 else 'B'
    inputs = set_a if which == 'A' else set_b

    if difficulty == 'easy':
        inputs = inputs[:5]
    elif difficulty == 'medium':
        inputs = inputs[:7]

    outputs = [m * x + c for x in inputs]

    prompt = (
        "The rule is: y = 50 - 5x.\n\n"
        f"Use Set {which} input numbers: {', '.join(_fmt_int(x) for x in inputs)}\n"
        "Write the output numbers in order (comma-separated)."
    )

    correct = ', '.join(_fmt_int(y) for y in outputs)
    explanation = 'Substitute each input x into y = 50 - 5x.'

    if qtype == 'mcq':
        wrong1 = ', '.join(_fmt_int(y + 5) for y in outputs)
        wrong2 = ', '.join(_fmt_int(y - 5) for y in outputs)
        wrong3 = ', '.join(_fmt_int(abs(y)) for y in outputs)
        options = list(dict.fromkeys([correct, wrong1, wrong2, wrong3]))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'set': which, 'inputs': inputs, 'm': m, 'c': c})

    if qtype == 'scaffold':
        steps = [
            'Write the rule: y = 50 - 5x.',
            'Substitute each x value into the rule.',
            'Write outputs in the same order as the inputs.'
        ]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"First output when x = {inputs[0]}:",
                'correct_answer': _fmt_int(outputs[0]),
                'explanation': 'Compute 50 - 5x.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'All outputs (comma-separated):',
                'correct_answer': correct,
                'explanation': 'Compute for each input.'
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'set': which, 'inputs': inputs, 'm': m, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'set': which, 'inputs': inputs, 'm': m, 'c': c})


def _gen_table_from_graph(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Provide a linear graph and ask for outputs at given x values.
    m_choices = [-3, -2, -1, 1, 2, 3]
    c_choices = [-6, -4, -2, 0, 2, 4, 6]
    m = rng.choice(m_choices)
    c = rng.choice(c_choices)

    if difficulty == 'easy':
        xs = [-2, 0, 2]
    elif difficulty == 'medium':
        xs = [-3, -1, 1, 3]
    else:
        xs = [-4, -2, 0, 2, 4]

    ys = [m * x + c for x in xs]
    prompt = (
        "A straight-line graph is shown for a function.\n"
        "Use the graph to complete the table of values.\n\n"
        f"x values: {', '.join(_fmt_int(x) for x in xs)}\n"
        "Write the y values in the same order (comma-separated)."
    )

    correct = ', '.join(_fmt_int(y) for y in ys)
    explanation = 'Read off y for each x on the straight line (equivalently, use y = mx + c).' 

    graph = _build_linear_graph_payload(m=m, c=c)

    if qtype == 'mcq':
        wrong1 = ', '.join(_fmt_int(y + m) for y in ys)
        wrong2 = ', '.join(_fmt_int(y - m) for y in ys)
        wrong3 = ', '.join(_fmt_int(-y) for y in ys)
        options = list(dict.fromkeys([correct, wrong1, wrong2, wrong3]))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, graph=graph, parameters={'xs': xs, 'm': m, 'c': c})

    if qtype == 'scaffold':
        steps = [
            'Locate each x value on the x-axis.',
            'Move vertically to the line, then read the y value.',
            'Write the y values in the same order.'
        ]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"y value when x = {xs[0]}:",
                'correct_answer': _fmt_int(ys[0]),
                'explanation': 'Read off the first point on the graph.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'All y values (comma-separated):',
                'correct_answer': correct,
                'explanation': 'Read off each point.'
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, graph=graph, parameters={'xs': xs, 'm': m, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, graph=graph, parameters={'xs': xs, 'm': m, 'c': c})


def _gen_symbolic_from_words(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    candidates = [
        [('×', 5), ('+', 20)],
        [('×', 4), ('+', 15)],
        [('×', 3), ('-', 7)],
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
        options = list(dict.fromkeys([correct, 'y = x', 'y = 5x - 20', 'y = 20x + 5']))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'ops': ops})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'ops': ops})


def _gen_word_from_symbolic(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    ops_bank = [
        [('×', 5), ('+', 20)],
        [('×', 3), ('+', 4)],
        [('×', 2), ('-', 5)],
        [('×', -3), ('+', 4)],
    ]
    ops = rng.choice(ops_bank)
    formula = _ops_to_symbolic(ops)

    prompt = (
        "Write a word formula that matches the symbolic formula below.\n\n"
        f"{formula}\n\n"
        "Answer format: 'To get y, ...'"
    )

    word = f"To get y, { _ops_to_words(ops) }."
    word = word.replace('multiply by', 'multiply x by').replace(', then ', ' then ')
    correct = word
    explanation = 'Read the formula: coefficient means multiply, and +/− means add/subtract.'

    if qtype == 'mcq':
        options = [
            correct,
            'To get y, add first, then multiply x.',
            'To get y, subtract the coefficient.',
            'To get y, multiply x by the constant term.'
        ]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'formula': formula})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'formula': formula})


def generate_grade9_functions_relationships_question(
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
        'outputs_for_sets',
        'flow_table_outputs',
        'table_from_graph',
        'symbolic_from_words',
        'word_from_symbolic',
    ]

    if subskill in {'functions_and_relationships', 'functions', 'relationships', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'outputs_for_sets': _gen_outputs_for_sets,
        'flow_table_outputs': _gen_flow_table_outputs,
        'table_from_graph': _gen_table_from_graph,
        'symbolic_from_words': _gen_symbolic_from_words,
        'word_from_symbolic': _gen_word_from_symbolic,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g9_fun'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
