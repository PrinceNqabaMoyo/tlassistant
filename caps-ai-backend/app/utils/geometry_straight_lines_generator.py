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


def _make_scaffold(*, prompt: str, steps: List[Dict[str, str]], checkpoints: List[Dict[str, Any]], final_answer: str, explanation: str, **extra) -> Dict[str, Any]:
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


def _gen_definitions(rng: random.Random, qtype: str) -> Dict[str, Any]:
    items = [
        (
            'line_segment',
            'A line segment has a definite starting point and a definite endpoint, so it can be measured.',
        ),
        (
            'line',
            'A line goes on indefinitely in both directions (no endpoints), so it cannot be measured.',
        ),
        (
            'ray',
            'A ray has one endpoint and goes on indefinitely in one direction.',
        ),
    ]

    key, correct = rng.choice(items)

    if qtype == 'mcq':
        options = [
            'A line segment has a definite starting point and a definite endpoint, so it can be measured.',
            'A line goes on indefinitely in both directions (no endpoints), so it cannot be measured.',
            'A ray has one endpoint and goes on indefinitely in one direction.',
        ]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"Which statement best describes a {key.replace('_', ' ')}?",
            options=options,
            correct_answer=correct,
            explanation=correct,
            parameters={'object': key},
        )

    return _make_typed(
        prompt=f"Describe what a {key.replace('_', ' ')} is.",
        correct_answer=correct,
        explanation=correct,
        parameters={'object': key},
    )


def _gen_measurable(rng: random.Random, qtype: str) -> Dict[str, Any]:
    prompt = 'Which of the following can be measured with a ruler?'
    correct = 'A line segment'
    explanation = 'A line segment has two endpoints and a finite length, so it can be measured. A line and a ray extend indefinitely.'

    if qtype == 'typed':
        return _make_typed(
            prompt=prompt,
            correct_answer=correct,
            explanation=explanation,
            parameters={},
        )

    options = ['A line', 'A ray', 'A line segment', 'All of them']
    rng.shuffle(options)
    return _make_mcq(
        prompt=prompt,
        options=options,
        correct_answer=correct,
        explanation=explanation,
        parameters={},
    )


def _gen_parallel(rng: random.Random, qtype: str) -> Dict[str, Any]:
    if qtype == 'scaffold':
        steps = [
            {'title': 'Recall the definition', 'content': 'Parallel lines stay the same distance apart.'},
            {'title': 'Think about meeting', 'content': 'If they stayed the same distance apart, they would never cross.'},
        ]
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'mcq',
                'prompt': 'Parallel lines are ...',
                'options': [
                    'a constant distance apart',
                    'a constant distance apart only near the middle',
                    'always perpendicular',
                    'always curved',
                ],
                'correct_answer': 'a constant distance apart',
                'explanation': 'Parallel lines remain the same distance apart everywhere.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'mcq',
                'prompt': 'Do two parallel lines meet (intersect) somewhere?',
                'options': ['Yes', 'No'],
                'correct_answer': 'No',
                'explanation': 'If they met, the distance between them would become zero, which contradicts being constant.',
            },
        ]
        return _make_scaffold(
            prompt='Do parallel lines meet somewhere? Explain briefly.',
            steps=steps,
            checkpoints=checkpoints,
            final_answer='No',
            explanation='Parallel lines stay the same distance apart, so they do not intersect.',
            parameters={},
        )

    prompt = 'Do parallel lines meet somewhere?'
    correct = 'No'
    explanation = 'Parallel lines are a constant distance apart, so they never intersect.'

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={})

    options = ['Yes', 'No']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={})


def _gen_perpendicular(rng: random.Random, qtype: str) -> Dict[str, Any]:
    variant = rng.choice(['definition', 'angles'])

    if variant == 'definition':
        prompt = 'What does it mean when two lines are perpendicular?'
        correct = 'They meet to form a right angle (90°).'
        explanation = 'Perpendicular lines intersect at 90°.'

        if qtype == 'typed':
            return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'variant': variant})

        options = ['They never meet', 'They meet to form a right angle (90°).', 'They are the same line', 'They are always parallel']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'variant': variant})

    prompt = 'How many angles are formed where two perpendicular lines meet?'
    correct = '4'
    explanation = 'Two lines that intersect form four angles around the intersection point.'

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'variant': variant})

    options = ['1', '2', '3', '4']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'variant': variant})


def _gen_true_false_concepts(rng: random.Random, qtype: str) -> Dict[str, Any]:
    statements = [
        (
            'Can two line segments be parallel?',
            'Yes',
            'Yes. If they have the same direction and stay the same distance apart (and do not meet), they are parallel line segments.',
        ),
        (
            'Can a line be parallel on its own?',
            'No',
            'No. Parallel is a relationship between two (or more) lines/segments.',
        ),
        (
            'Can you draw two different rays that start at the same point and are parallel?',
            'No',
            'No. Rays from the same starting point either overlap (same direction) or spread apart and will not stay a constant distance apart.',
        ),
    ]

    prompt, correct, explanation = rng.choice(statements)

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={})

    options = ['Yes', 'No']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={})


def generate_grade7_geometry_straight_lines_question(
    *,
    subskill: str = 'geometry_straight_lines',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    supported_subskills = {
        'definitions',
        'measurable',
        'parallel_lines',
        'perpendicular_lines',
        'concept_checks',
    }

    if subskill not in supported_subskills:
        subskill = 'definitions'

    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    if question_type == 'scaffold' and subskill != 'parallel_lines':
        question_type = 'typed'

    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if subskill == 'definitions':
        q = _gen_definitions(rng, question_type)
    elif subskill == 'measurable':
        q = _gen_measurable(rng, question_type)
    elif subskill == 'parallel_lines':
        q = _gen_parallel(rng, question_type)
    elif subskill == 'perpendicular_lines':
        q = _gen_perpendicular(rng, question_type)
    else:
        q = _gen_true_false_concepts(rng, question_type)

    out = {
        'id': _make_id('g7_geo_straight_lines'),
        'topic': 'geometry_straight_lines',
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
