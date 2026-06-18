from flask import request, jsonify

from . import math_bp
from ...utils.grade12_finance_generator import generate_questions


@math_bp.route('/grade12/finance/generate', methods=['POST'])
def generate_grade12_finance():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')

        if not isinstance(count, int) or count < 1 or count > 20:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        questions = generate_questions(
            subskill=subskill,
            difficulty=difficulty,
            question_type=question_type,
            count=count,
            seed=seed,
        )

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
