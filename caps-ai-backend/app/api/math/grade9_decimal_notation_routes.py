from flask import request, jsonify
from . import math_bp
from ...utils.grade9_decimal_notation_generator import generate_grade9_decimal_notation_question


@math_bp.route('/grade9/decimal-notation/generate', methods=['POST'])
def generate_grade9_decimal_notation():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'typed')
        count = data.get('count', 1)
        seed = data.get('seed')

        if not isinstance(count, int) or count < 1 or count > 20:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        questions = []
        for i in range(count):
            q_seed = None
            if seed is not None:
                try:
                    q_seed = int(seed) + i
                except Exception:
                    q_seed = None

            question = generate_grade9_decimal_notation_question(
                subskill=subskill,
                difficulty=difficulty,
                question_type=question_type,
                seed=q_seed,
            )
            questions.append(question)

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
