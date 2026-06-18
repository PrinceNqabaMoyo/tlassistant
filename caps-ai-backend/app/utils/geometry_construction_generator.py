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


def _classify_angle_type(deg: int) -> str:
    if deg == 0 or deg == 360:
        return 'revolution'
    if 0 < deg < 90:
        return 'acute'
    if deg == 90:
        return 'right'
    if 90 < deg < 180:
        return 'obtuse'
    if deg == 180:
        return 'straight'
    if 180 < deg < 360:
        return 'reflex'
    return 'revolution'


def _gen_degree_unit_familiar_angles_table(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    table = {
        'right angle': 90,
        'straight angle': 180,
        'revolution': 360,
        'half a right angle': 45,
        'a third of a right angle': 30,
        'a quarter of a right angle': 22.5,
        'half a straight angle': 90,
        'three quarters of a revolution': 270,
        'a third of a revolution': 120,
    }

    items = list(table.items())
    rng.shuffle(items)

    if difficulty == 'easy':
        pick_n = 4
    elif difficulty == 'medium':
        pick_n = 6
    else:
        pick_n = 8

    picked = items[:pick_n]

    if qtype == 'mcq':
        name, value = rng.choice(picked)
        wrong = set()
        candidates = [0, 22.5, 30, 45, 60, 90, 120, 180, 270, 360]
        while len(wrong) < 3:
            w = rng.choice(candidates)
            if w != value:
                wrong.add(w)
        options = [str(value), *[str(x) for x in wrong]]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"How many degrees is a {name}?",
            options=options,
            correct_answer=str(value),
            explanation=f"A {name} is {value}°.",
            parameters={'name': name, 'degrees': value},
        )

    if qtype == 'scaffold':
        name, value = rng.choice(picked)
        steps = [
            {'title': 'Recall common angles', 'content': 'Memorise the key angle facts (90°, 180°, 360°, and common fractions of these).'},
            {'title': 'Match the description', 'content': 'Use the description (half/third/quarter) to scale the base angle.'},
        ]
        checkpoints = [
            {
                'id': 'c1_base',
                'kind': 'mcq',
                'prompt': 'Which base angle is used for “a right angle”?',
                'options': ['90°', '180°', '360°'],
                'correct_answer': '90°',
                'explanation': 'A right angle is 90°.',
            },
            {
                'id': 'c2_answer',
                'kind': 'typed',
                'prompt': f"Write the size of a {name} in degrees (include the ° symbol if you want).",
                'correct_answer': f"{value}",
                'explanation': f"A {name} is {value}°.",
            },
        ]
        return _make_scaffold(
            prompt=f"Fill in the missing degree measure: {name} = ?",
            steps=steps,
            checkpoints=checkpoints,
            final_answer=str(value),
            explanation=f"A {name} is {value}°.",
            parameters={'name': name, 'degrees': value},
        )

    name, value = rng.choice(picked)
    return _make_typed(
        prompt=f"Write the size of a {name} in degrees.",
        correct_answer=str(value),
        explanation=f"A {name} is {value}°.",
        parameters={'name': name, 'degrees': value},
    )


def _gen_clock_degree_movement(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['minute', 'hour']) if difficulty != 'easy' else 'minute'
    if kind == 'minute':
        prompt = 'How many degrees does the minute hand move in 1 hour?'
        correct = '360'
        explanation = 'In one hour the minute hand makes one full revolution: 360°.'
        if qtype == 'mcq':
            options = ['360', '30', '180', '90']
            rng.shuffle(options)
            return _make_mcq(prompt=prompt, options=options, correct_answer='360', explanation=explanation)
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)

    prompt = 'How many degrees does the hour hand move in 1 hour?'
    correct = '30'
    explanation = 'The hour hand moves 360° in 12 hours, so in 1 hour it moves 360 ÷ 12 = 30°.'
    if qtype == 'mcq':
        options = ['30', '360', '12', '60']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer='30', explanation=explanation)
    if qtype == 'scaffold':
        steps = [
            {'title': 'Use 12 hours', 'content': 'A clock has 12 equal hour steps around a full 360°.'},
            {'title': 'Divide', 'content': 'Compute 360 ÷ 12 to get degrees per hour.'},
        ]
        checkpoints = [
            {
                'id': 'c1_full',
                'kind': 'typed',
                'prompt': 'How many degrees are in one full revolution?',
                'correct_answer': '360',
                'explanation': 'A full turn is 360°.',
            },
            {
                'id': 'c2_divide',
                'kind': 'typed',
                'prompt': 'Compute 360 ÷ 12.',
                'correct_answer': '30',
                'explanation': '360 ÷ 12 = 30.',
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)
    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_classify_angles_by_degree(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        deg = rng.choice([30, 45, 60, 90, 120, 180])
    elif difficulty == 'medium':
        deg = rng.choice([10, 25, 75, 95, 135, 170, 185, 220, 300])
    else:
        deg = rng.randint(1, 359)
        if deg in {90, 180}:
            deg += 1

    correct = _classify_angle_type(deg)

    if qtype == 'mcq':
        options = ['acute', 'right', 'obtuse', 'straight', 'reflex']
        if correct not in options:
            correct = 'reflex'
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"Classify this angle: {deg}°.",
            options=options,
            correct_answer=correct,
            explanation=f"{deg}° is a {correct} angle.",
            parameters={'degrees': deg},
        )

    return _make_typed(
        prompt=f"Classify this angle as acute/right/obtuse/straight/reflex: {deg}°.",
        correct_answer=correct,
        explanation=f"{deg}° is a {correct} angle.",
        parameters={'degrees': deg},
    )


def _gen_reflex_angle_strategy(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    small = rng.choice([20, 35, 45, 60, 75, 110, 135, 150]) if difficulty != 'hard' else rng.randint(1, 179)
    reflex = 360 - small

    if qtype == 'mcq':
        options = [str(reflex), str(180 - (small % 180)), str(360), str(small)]
        options = list(dict.fromkeys(options))
        while len(options) < 4:
            options.append(str(rng.randint(181, 359)))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"A protractor shows the smaller angle is {small}°. What is the reflex angle?",
            options=options,
            correct_answer=str(reflex),
            explanation=f"Reflex angle = 360° − {small}° = {reflex}°.",
            parameters={'small_angle': small, 'reflex_angle': reflex},
        )

    if qtype == 'scaffold':
        steps = [
            {'title': 'Know the total', 'content': 'Angles around a point add to 360°.'},
            {'title': 'Subtract', 'content': 'Reflex angle = 360° − smaller angle.'},
        ]
        checkpoints = [
            {
                'id': 'c1_total',
                'kind': 'typed',
                'prompt': 'How many degrees are around a point?',
                'correct_answer': '360',
                'explanation': 'Angles around a point add to 360°.',
            },
            {
                'id': 'c2_sub',
                'kind': 'typed',
                'prompt': f"Compute 360 − {small}.",
                'correct_answer': str(reflex),
                'explanation': f"360 − {small} = {reflex}.",
            },
        ]
        return _make_scaffold(
            prompt=f"A protractor shows the smaller angle is {small}°. Find the reflex angle.",
            steps=steps,
            checkpoints=checkpoints,
            final_answer=str(reflex),
            explanation=f"Reflex angle = 360° − {small}° = {reflex}°.",
            parameters={'small_angle': small, 'reflex_angle': reflex},
        )

    return _make_typed(
        prompt=f"A protractor shows the smaller angle is {small}°. What is the reflex angle?",
        correct_answer=str(reflex),
        explanation=f"Reflex angle = 360° − {small}° = {reflex}°.",
        parameters={'small_angle': small, 'reflex_angle': reflex},
    )


def _gen_protractor_reading_choose_scale(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        scenario = rng.choice(['anticlockwise', 'clockwise'])
    else:
        scenario = rng.choice(['anticlockwise', 'clockwise'])

    correct = 'Use the scale that starts at 0° on the angle arm you are measuring from.'
    distractors = [
        'Always use the outer scale.',
        'Always use the inner scale.',
        'Use the scale with bigger numbers.',
    ]

    if qtype == 'typed':
        return _make_typed(
            prompt=f"When measuring {scenario}, which protractor scale should you read?",
            correct_answer=correct,
            explanation='Choose the scale where 0° lies on the reference arm (the arm you start from).',
        )

    options = [correct, *distractors]
    rng.shuffle(options)
    return _make_mcq(
        prompt=f"When measuring {scenario}, which protractor scale should you read?",
        options=options,
        correct_answer=correct,
        explanation='You choose the scale by finding which one starts at 0° on the angle arm.',
    )


def _gen_construct_angle_to_given_line_steps(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    blanks = {
        'baseline': 'base line',
        'vertex': 'marked point',
        'degree_mark': 'correct degree mark',
        'two_points': 'two points',
    }

    prompt = (
        'Fill in the missing words:\n'
        'Step 2: Place the protractor with its ____ on the line and its origin exactly on top of the _____.\n'
        'Step 3: Make a small, clear mark at the _____.\n'
        'Step 4: Use a ruler to line up the two _____ and draw a straight line that passes exactly through them.'
    )

    if qtype == 'mcq':
        options = ['base line', 'centre hole', 'edge', 'diameter']
        rng.shuffle(options)
        return _make_mcq(
            prompt='Step 2 blank 1: Place the protractor with its ____ on the line.',
            options=options,
            correct_answer='base line',
            explanation='The baseline must align with the reference line.',
        )

    if qtype == 'scaffold':
        steps = [
            {'title': 'Align baseline + origin', 'content': 'Baseline on the reference line; origin exactly on the marked point.'},
            {'title': 'Mark the degree', 'content': 'Make a clear mark where the degree scale shows the desired angle.'},
            {'title': 'Draw through 2 points', 'content': 'Use a ruler to draw a ray through the origin and the degree mark.'},
        ]
        checkpoints = [
            {
                'id': 'c1_blank2',
                'kind': 'typed',
                'prompt': 'Step 2 blank 2: the protractor origin goes on top of the _____.',
                'correct_answer': blanks['vertex'],
                'explanation': 'The origin is at the angle vertex (the marked point).',
            },
            {
                'id': 'c2_blank3',
                'kind': 'typed',
                'prompt': 'Step 3 blank: make a mark at the _____.',
                'correct_answer': blanks['degree_mark'],
                'explanation': 'You mark the point at the correct degree reading.',
            },
        ]
        return _make_scaffold(
            prompt=prompt,
            steps=steps,
            checkpoints=checkpoints,
            final_answer='base line; marked point; correct degree mark; two points',
            explanation='Correct fill is: base line; marked point; correct degree mark; two points.',
            parameters=blanks,
        )

    return _make_typed(
        prompt=prompt,
        correct_answer='base line; marked point; correct degree mark; two points',
        explanation='Correct fill is: base line; marked point; correct degree mark; two points.',
        parameters=blanks,
    )


def _gen_parallel_perpendicular_language_symbols(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['perpendicular', 'parallel'])
    if kind == 'perpendicular':
        prompt = 'Which symbol means “perpendicular”?'
        correct = '⊥'
        options = ['⊥', '//', '=', '≈']
        explanation = 'The symbol ⊥ means perpendicular (meeting at 90°).'
    else:
        prompt = 'Which symbol means “parallel”?'
        correct = '//'
        options = ['⊥', '//', '∠', '+']
        explanation = 'The symbol // means parallel (never meeting, same direction).'

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)


def _gen_circle_radius_concepts(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    prompt = 'What is the radius of a circle?'
    correct = 'The distance from the centre of the circle to the edge.'
    explanation = 'A radius is a line segment from the centre to the circumference.'

    if qtype == 'mcq':
        options = [
            correct,
            'The distance around the circle.',
            'The distance across the circle through the centre.',
            'Any line inside the circle.',
        ]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_compass_set_radius_steps(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    prompt = 'You want to draw a circle of radius 2 cm. What should you set on the compass using a ruler?'
    correct = 'Set the distance between the compass point and the pencil tip to 2 cm.'
    explanation = 'The radius equals the compass opening (point to pencil).'

    if qtype == 'mcq':
        options = [
            correct,
            'Set the distance between the two arms to 4 cm.',
            'Set the distance from the centre to the edge to 4 cm.',
            'Set the pencil length to 2 cm.',
        ]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = [
            {'title': 'Use a ruler', 'content': 'Place the compass point on 0 cm and open until the pencil is at 2 cm.'},
            {'title': 'Keep the opening fixed', 'content': 'Do not change the opening while drawing the circle.'},
        ]
        checkpoints = [
            {
                'id': 'c1_what_distance',
                'kind': 'mcq',
                'prompt': 'Which distance equals the radius when using a compass?',
                'options': [
                    'point to pencil',
                    'around the circle',
                    'diameter',
                    'edge to edge without centre',
                ],
                'correct_answer': 'point to pencil',
                'explanation': 'The compass opening equals the radius.',
            },
            {
                'id': 'c2_final',
                'kind': 'typed',
                'prompt': 'Write the instruction in one sentence.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_construct_equilateral_triangle_from_segment(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    prompt = 'Two circles with the same radius are drawn with centres at A and B. They intersect at C. What type of triangle is ABC?'
    correct = 'equilateral'
    explanation = 'AC = AB (radius), and BC = AB (radius), so all three sides are equal.'

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)

    options = ['equilateral', 'isosceles', 'right-angled', 'scalene']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer='equilateral', explanation=explanation)


def _gen_construct_parallelogram_from_two_segments(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    prompt = 'In a construction, PS = QR and RS = QP. What quadrilateral is PQRS?'
    correct = 'parallelogram'
    explanation = 'If both pairs of opposite sides are equal in length, the quadrilateral is a parallelogram.'

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)

    options = ['parallelogram', 'kite', 'trapezium', 'rectangle']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer='parallelogram', explanation=explanation)


def generate_grade7_geometry_construction_question(
    *,
    subskill: str,
    difficulty: str,
    question_type: str,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    normalized_subskill = (subskill or '').strip().lower()
    normalized_difficulty = (difficulty or 'easy').strip().lower()
    normalized_qtype = (question_type or 'typed').strip().lower()

    if normalized_difficulty not in {'easy', 'medium', 'hard'}:
        normalized_difficulty = 'easy'

    if normalized_qtype not in {'typed', 'mcq', 'scaffold'}:
        normalized_qtype = 'typed'

    typed_capable = {
        'degree_unit_familiar_angles_table',
        'clock_degree_movement',
        'classify_angles_by_degree',
        'reflex_angle_strategy',
        'protractor_reading_choose_scale',
        'construct_angle_to_given_line_steps',
        'parallel_perpendicular_language_symbols',
        'circle_radius_concepts',
        'compass_set_radius_steps',
        'construct_equilateral_triangle_from_segment',
        'construct_parallelogram_from_two_segments',
    }

    scaffold_capable = {
        'degree_unit_familiar_angles_table',
        'clock_degree_movement',
        'reflex_angle_strategy',
        'construct_angle_to_given_line_steps',
        'compass_set_radius_steps',
    }

    if normalized_subskill in {'', 'geometry_construction', 'construction_of_geometric_figures'}:
        if normalized_qtype == 'scaffold':
            normalized_subskill = rng.choice(sorted(scaffold_capable))
        else:
            normalized_subskill = rng.choice(sorted(typed_capable))

    if normalized_qtype == 'scaffold' and normalized_subskill not in scaffold_capable:
        normalized_qtype = 'typed'

    generators = {
        'degree_unit_familiar_angles_table': _gen_degree_unit_familiar_angles_table,
        'clock_degree_movement': _gen_clock_degree_movement,
        'classify_angles_by_degree': _gen_classify_angles_by_degree,
        'reflex_angle_strategy': _gen_reflex_angle_strategy,
        'protractor_reading_choose_scale': _gen_protractor_reading_choose_scale,
        'construct_angle_to_given_line_steps': _gen_construct_angle_to_given_line_steps,
        'parallel_perpendicular_language_symbols': _gen_parallel_perpendicular_language_symbols,
        'circle_radius_concepts': _gen_circle_radius_concepts,
        'compass_set_radius_steps': _gen_compass_set_radius_steps,
        'construct_equilateral_triangle_from_segment': _gen_construct_equilateral_triangle_from_segment,
        'construct_parallelogram_from_two_segments': _gen_construct_parallelogram_from_two_segments,
    }

    if normalized_subskill not in generators:
        normalized_subskill = 'degree_unit_familiar_angles_table'

    base = generators[normalized_subskill](rng, normalized_difficulty, normalized_qtype)

    q = {
        'id': _make_id('g7_geo_construct'),
        'topic': 'Construction of Geometric Figures',
        'subskill': normalized_subskill,
        'difficulty': normalized_difficulty,
        **base,
    }

    _validate_question(q)
    return q
