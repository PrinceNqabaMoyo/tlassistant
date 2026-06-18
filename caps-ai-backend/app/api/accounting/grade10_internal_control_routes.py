from flask import jsonify, request

from . import accounting_bp
from ...utils.grade10_accounting.internal_control_generator import generate_questions


@accounting_bp.route('/grade10/internal-control/generate', methods=['POST'])
def generate_grade10_internal_control():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')

        questions = generate_questions(
            subskill=subskill,
            difficulty=difficulty,
            question_type=question_type,
            count=count,
            seed=seed,
        )

        return jsonify({
            'success': True,
            'topic': 'grade10_accounting_internal_control',
            'subskill': subskill,
            'difficulty': difficulty,
            'questions': questions,
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
