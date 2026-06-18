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


def _make_scaffold(*, prompt: str, steps: List[str], checkpoints: List[Dict[str, Any]], final_answer: str, explanation: str, **extra) -> Dict[str, Any]:
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


def _pick_int(rng: random.Random, low: int, high: int) -> int:
    return rng.randint(low, high)


def _csv_equations_table() -> Dict[str, Any]:
    # From Integers Studio doc (csv): equation, solution, required property
    headers = ['Equation', 'Solution', 'Required property of negative numbers']
    rows = [
        ['17 + x = 10', 'x = -7 means 17 + (-7) = 10', 'Adding negative number = subtracting corresponding positive number'],
        ['5 - x = 9', 'x = -4 means 5 - (-4) = 9', 'Subtracting negative number = adding corresponding positive number'],
        ['20 + 3x = 5', 'x = -5 means 3×(-5) = -15', 'Product of a positive and a negative is negative'],
    ]
    return {'headers': headers, 'rows': rows}


def _gen_properties_table_cell(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    table = _csv_equations_table()
    # Ask about the missing x and the property for a randomly picked row.
    idx = rng.randrange(0, len(table['rows']))
    row = table['rows'][idx]

    equation = row[0]
    solution = row[1]
    prop = row[2]

    which = rng.choice(['x', 'property'])

    if which == 'x':
        # Extract x from solution string: "x = -7 means ..."
        # Keep it simple and deterministic.
        x_value = solution.split('means')[0].strip().replace('x =', '').strip()
        prompt = f"From the table, what value of x makes the equation true: {equation}?"
        explanation = f"According to the table: {solution}."
        correct = x_value
    else:
        prompt = f"From the table, which property of negative numbers is illustrated by: {equation} ({solution})?"
        explanation = f"The table states the required property: {prop}."
        correct = prop

    if qtype == 'mcq':
        if which == 'x':
            wrong = [
                str(int(correct) * -1) if str(correct).lstrip('-').isdigit() else '7',
                str(int(correct) - 1) if str(correct).lstrip('-').isdigit() else '-4',
                str(int(correct) + 1) if str(correct).lstrip('-').isdigit() else '-5',
            ]
            options = list(dict.fromkeys([correct, *wrong]))[:4]
        else:
            options = list(
                dict.fromkeys(
                    [
                        prop,
                        'Adding negative number = subtracting corresponding positive number',
                        'Subtracting negative number = adding corresponding positive number',
                        'Product of two negative numbers is positive',
                    ]
                )
            )[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, table=table)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Locate the correct row in the table (write row number 1-3):',
                'correct_answer': str(idx + 1),
                'explanation': 'Match the equation to the row.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Now write the required answer:',
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Find the matching equation.', 'Read the solution/property from the row.', 'Write the answer exactly.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, table=table)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, table=table)


def _gen_add_sub_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    lo = -50 if difficulty == 'hard' else -20
    hi = 50 if difficulty == 'hard' else 20

    # Include chained operations at higher difficulty
    if difficulty == 'easy':
        a = _pick_int(rng, lo, hi)
        b = _pick_int(rng, lo, hi)
        op = rng.choice(['+', '-'])
        expr = f"{a} {op} ({b})"
        ans = a + b if op == '+' else a - b
    else:
        a = _pick_int(rng, lo, hi)
        b = _pick_int(rng, lo, hi)
        c = _pick_int(rng, lo, hi)
        op1 = rng.choice(['+', '-'])
        op2 = rng.choice(['+', '-'])
        expr = f"{a} {op1} ({b}) {op2} ({c})"
        ans = a + b if op1 == '+' else a - b
        ans = ans + c if op2 == '+' else ans - c

    prompt = f"Calculate: {expr}"
    explanation = 'Use integer rules. Remember: subtracting is adding the opposite.'

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Rewrite any subtraction as adding the opposite (write an equivalent expression):',
                'correct_answer': expr.replace(' - ', ' + (-').replace(')', '))', 1) if ' - ' in expr else expr,
                'explanation': 'Convert subtraction to addition of the additive inverse.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': str(ans),
                'explanation': explanation,
            }
        ]
        steps = ['Rewrite subtraction as adding the opposite.', 'Combine step-by-step.', 'Write the final integer.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(ans), explanation=explanation, parameters={'expr': expr})

    if qtype == 'mcq':
        options = [str(ans), str(ans + 1), str(ans - 1), str(-ans)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(ans), explanation=explanation, parameters={'expr': expr})

    return _make_typed(prompt=prompt, correct_answer=str(ans), explanation=explanation, parameters={'expr': expr})


def _gen_mult_div_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a_mag = rng.randint(2, 12) if difficulty != 'hard' else rng.randint(5, 25)
    b_mag = rng.randint(2, 12) if difficulty != 'hard' else rng.randint(5, 25)
    a = a_mag * rng.choice([-1, 1])
    b = b_mag * rng.choice([-1, 1])

    op = rng.choice(['×', '÷'])
    if op == '×':
        ans = a * b
        prompt = f"Calculate: ({a}) × ({b})"
        explanation = 'Same signs give positive; different signs give negative.'
    else:
        # Ensure divisible by construction: (b * k) ÷ b = k
        k = rng.randint(2, 12) if difficulty != 'hard' else rng.randint(3, 20)
        a = b * k
        ans = int(a / b)
        prompt = f"Calculate: ({a}) ÷ ({b})"
        explanation = 'Division sign rules match multiplication sign rules.'

    if qtype == 'mcq':
        options = [str(ans), str(-ans), str(ans + 1), str(ans - 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})


def _gen_distributive(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Examples like: 4 × (20 + (-5)) and expanded form.
    a = rng.choice([-1, 1]) * rng.randint(2, 12)
    b = rng.choice([-1, 1]) * rng.randint(5, 30)
    c = rng.choice([-1, 1]) * rng.randint(5, 30)

    left = a * (b + c)

    prompt = f"Calculate using the distributive property: ({a}) × ({b} + ({c}))"
    explanation = f"Distribute: {a}×{b} + {a}×{c} = {a*b} + {a*c} = {left}."

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute {a}×{b}:",
                'correct_answer': str(a * b),
                'explanation': 'Multiply first term.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute {a}×{c}:",
                'correct_answer': str(a * c),
                'explanation': 'Multiply second term.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Now add the two products:',
                'correct_answer': str(left),
                'explanation': 'Add the partial products.'
            },
        ]
        steps = ['Multiply each term in the bracket by the outside factor.', 'Add the results.', 'Write the final answer.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(left), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    if qtype == 'mcq':
        options = [str(left), str(a * b + a * c + 1), str(a * (b - c)), str(-left)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(left), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=str(left), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})


def _gen_mixed_operations(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Mixed operations with brackets, like Q15-ish but smaller.
    a = rng.choice([-1, 1]) * rng.randint(2, 12)
    b = rng.choice([-1, 1]) * rng.randint(2, 20)
    c = rng.choice([-1, 1]) * rng.randint(2, 20)
    d = rng.choice([-1, 1]) * rng.randint(2, 12)

    expr = f"({a}) × ({b} + ({c})) − ({d})"
    ans = a * (b + c) - d

    prompt = f"Calculate: {expr}"
    explanation = 'Use order of operations: brackets, then multiplication/division, then addition/subtraction.'

    if qtype == 'mcq':
        options = [str(ans), str(ans + 2), str(ans - 2), str(-ans)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(ans), explanation=explanation, parameters={'expr': expr})

    if qtype == 'scaffold':
        inside = b + c
        prod = a * inside
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute inside brackets: {b} + ({c}) =",
                'correct_answer': str(inside),
                'explanation': 'Add the integers inside the bracket first.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Multiply by {a}: {a} × {inside} =",
                'correct_answer': str(prod),
                'explanation': 'Multiply after the bracket.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now subtract ({d}): {prod} − ({d}) =",
                'correct_answer': str(ans),
                'explanation': 'Finish with subtraction (or add the opposite).'
            },
        ]
        steps = ['Evaluate brackets.', 'Multiply.', 'Complete final subtraction/addition.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(ans), explanation=explanation, parameters={'expr': expr})

    return _make_typed(prompt=prompt, correct_answer=str(ans), explanation=explanation, parameters={'expr': expr})


def generate_grade9_integers_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Integers'
    subskill = str(subskill or 'mixed').lower()
    difficulty = str(difficulty or 'easy').lower()
    question_type = str(question_type or 'typed').lower()

    supported = [
        'properties_table',
        'add_sub_integers',
        'multiply_divide_integers',
        'distributive_property',
        'mixed_operations',
    ]

    if subskill in {'integers', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'properties_table': _gen_properties_table_cell,
        'add_sub_integers': _gen_add_sub_integers,
        'multiply_divide_integers': _gen_mult_div_integers,
        'distributive_property': _gen_distributive,
        'mixed_operations': _gen_mixed_operations,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g9_int'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
