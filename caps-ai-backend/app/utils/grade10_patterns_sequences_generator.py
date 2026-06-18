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
                'prompt': f"Find the common difference: {shown[1]} − {shown[0]} = ?",
                'correct_answer': str(shown[1] - shown[0]),
                'explanation': 'Subtract consecutive terms to find the common difference.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Write the general term for an arithmetic sequence: T_n = a + (n − 1)d. Here a = {a1}, d = {d}. Find T_n.",
                'correct_answer': f"T_n = {a1} + (n - 1)({d})",
                'explanation': 'Use T_n = a + (n − 1)d.',
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
            'Find the common difference d by subtracting consecutive terms.',
            'Use T_n = a + (n − 1)d for arithmetic sequences.',
            'Add d repeatedly to list the next terms.',
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
                'prompt': f"Find the common ratio: {shown[1]} ÷ {shown[0]} = ?",
                'correct_answer': str(r),
                'explanation': 'Divide consecutive terms to find the ratio.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Next term after {shown[-1]}: {shown[-1]} × ({r}) = ?",
                'correct_answer': str(nxt[0]),
                'explanation': 'Multiply by the ratio to extend the sequence.',
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
            'Find the common ratio r by dividing consecutive terms.',
            'Check the ratio stays the same.',
            'Multiply by r to get the next terms.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r': r, 'shown': shown, 'next': nxt})


def _gen_missing_terms_from_given_formula(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Based on doc examples: T_n = n^2 - 1, T_n = -n + 4, T_n = -13 + 2n
    choice = rng.choice(['n2_minus_1', 'neg_n_plus_4', 'minus_13_plus_2n'])

    if choice == 'n2_minus_1':
        prompt = "Given T_n = n^2 − 1, fill in the missing term: 0; 3; __; 15; 24. (Give the missing term.)"
        # n=1..5 gives 0,3,8,15,24
        correct = '8'
        explanation = "Substitute n = 3: T_3 = 3^2 − 1 = 9 − 1 = 8."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'formula': 'n^2 - 1', 'n': 3})

    if choice == 'neg_n_plus_4':
        prompt = "Given T_n = −n + 4, fill in the missing term: 3; 2; 1; 0; __; −2. (Give the missing term.)"
        # n=1..6 gives 3,2,1,0,-1,-2
        correct = '-1'
        explanation = "The missing term is T_5: T_5 = −5 + 4 = −1."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'formula': '-n + 4', 'n': 5})

    prompt = "Given T_n = −13 + 2n, fill in the missing terms: −11; __; −7; __; −3. (Give the two missing terms comma-separated.)"
    # n=1..5 gives -11,-9,-7,-5,-3
    correct = '-9, -5'
    explanation = "T_2 = −13 + 2(2) = −9 and T_4 = −13 + 2(4) = −5."
    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'formula': '-13 + 2n', 'n_missing': [2, 4]})


def _gen_tables_seating(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # From doc: people seated = 4 + 2(n - 1)
    if difficulty == 'easy':
        n = rng.choice([5, 8, 12])
    elif difficulty == 'medium':
        n = rng.choice([12, 15, 20])
    else:
        n = rng.choice([20, 25, 30])

    prompt = "Square tables are placed in a row. 1 table seats 4 people; each additional table adds 2 seats. Find the number of people that can sit at n tables when n = " + str(n) + "."
    correct_val = 4 + 2 * (n - 1)
    correct = str(correct_val)
    explanation = f"T_n = 4 + 2(n − 1). So T_{n} = 4 + 2({n} − 1) = {correct_val}."

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the first term (n=1)?',
                'correct_answer': '4',
                'explanation': 'One table seats 4 people.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the common difference (how many seats added per extra table)?',
                'correct_answer': '2',
                'explanation': 'Each extra table adds 2 seats.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the formula for this arithmetic pattern: T_n = 4 + 2(n − 1).',
                'correct_answer': 'T_n = 4 + 2(n - 1)',
                'explanation': 'Start with 4 and add 2 for each extra table beyond the first.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now substitute n = {n}. What is T_{n}?",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify the first term (when n=1).',
            'Identify how much the pattern increases each time.',
            'Write the nth-term formula.',
            'Substitute the given n value.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'mcq':
        opt1 = correct
        opt2 = str(4 + 2 * n)
        opt3 = str(2 * n)
        opt4 = str(4 + 3 * (n - 1))
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_matchsticks_squares_in_row(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # From doc: 1 square 4 sticks, 2 squares 7 sticks, 3 squares 10 sticks => T_n = 3n + 1
    if difficulty == 'easy':
        n = rng.choice([5, 10])
    elif difficulty == 'medium':
        n = rng.choice([15, 25])
    else:
        n = rng.choice([25, 40])

    prompt = f"A row of n squares is built with matchsticks. 1 square uses 4 sticks, 2 squares use 7 sticks, 3 squares use 10 sticks. How many matchsticks are needed for n = {n}?"
    correct_val = 3 * n + 1
    correct = str(correct_val)
    explanation = f"Each new square shares a side, so it adds 3 sticks. Formula: T_n = 3n + 1. For n={n}: 3({n}) + 1 = {correct_val}."

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the first term (n=1)?',
                'correct_answer': '4',
                'explanation': 'A single square uses 4 matchsticks.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What is the common difference between terms (how many sticks added per extra square)?',
                'correct_answer': '3',
                'explanation': 'Adding a square shares one side, so it adds 3 sticks.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write a formula for the number of sticks: T_n = 3n + 1.',
                'correct_answer': 'T_n = 3n + 1',
                'explanation': 'Linear pattern with common difference 3 and first term 4.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now substitute n = {n}. What is T_{n}?",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Write down the first few terms (4, 7, 10, ...).',
            'Find the common difference (3).',
            'Write a linear formula for T_n.',
            'Substitute the given n value.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n})

    if qtype == 'mcq':
        opt1 = correct
        opt2 = str(4 * n)
        opt3 = str(3 * n)
        opt4 = str(3 * (n - 1) + 4)
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def generate_grade10_patterns_sequences_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Patterns and Sequences'
    subskill = str(subskill or 'mixed')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    supported = [
        'next_terms_arithmetic',
        'next_terms_geometric',
        'missing_terms_from_given_formula',
        'tables_seating',
        'matchsticks_squares_in_row',
    ]

    if subskill in {'patterns', 'sequences', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'next_terms_arithmetic': _gen_next_terms_arithmetic,
        'next_terms_geometric': _gen_next_terms_geometric,
        'missing_terms_from_given_formula': _gen_missing_terms_from_given_formula,
        'tables_seating': _gen_tables_seating,
        'matchsticks_squares_in_row': _gen_matchsticks_squares_in_row,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    # missing-terms is already multi-step; keep it typed
    if subskill == 'missing_terms_from_given_formula':
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g10_pat'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
