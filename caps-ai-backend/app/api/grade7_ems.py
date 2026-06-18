from flask import Blueprint, request, jsonify
from app.utils.grade7_ems import (
    term1_money_and_needs,
    term1_businesses,
    term2_accounting_concepts,
    term2_income_and_expenses,
    term2_budgets,
    term3_entrepreneurship
)

grade7_ems_bp = Blueprint('grade7_ems', __name__)

GENERATORS = {
    # Term 1
    'grade7_ems_money_and_needs': term1_money_and_needs.generate,
    'grade7_ems_businesses': term1_businesses.generate,
    # Term 2
    'grade7_ems_accounting_concepts': term2_accounting_concepts.generate,
    'grade7_ems_income_and_expenses': term2_income_and_expenses.generate,
    'grade7_ems_budgets': term2_budgets.generate,
    # Term 3
    'grade7_ems_entrepreneurship': term3_entrepreneurship.generate,
}

def generate_questions(topic, subskill, difficulty, count=1, mode='scaffold', config=None):
    if config is None:
        config = {}
        
    generator_func = GENERATORS.get(topic)
    if not generator_func:
        raise ValueError(f"Unknown topic: {topic}")
        
    return generator_func(subskill=subskill, difficulty=difficulty, count=count, mode=mode, **config)

@grade7_ems_bp.route('/generate', methods=['POST'])
def generate_grade7_ems():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No JSON payload provided'}), 400

        topic = data.get('topic')
        subskills = data.get('subskills', ['concepts'])
        difficulty = data.get('difficulty', 'medium')
        count = data.get('count', 1)
        mode = data.get('mode', 'scaffold')
        config = data.get('config', {})

        if not topic:
            return jsonify({'success': False, 'error': 'Missing required parameter: topic'}), 400

        all_questions = []
        # Support passing multiple subskills and distributing count among them
        for subskill in subskills:
            try:
                questions = generate_questions(topic, subskill, difficulty, count=count, mode=mode, config=config)
                all_questions.extend(questions)
            except Exception as e:
                # Log the error but continue if possible
                print(f"Error generating subskill {subskill}: {str(e)}")

        if not all_questions:
            return jsonify({'success': False, 'error': 'Failed to generate any questions'}), 500

        return jsonify({
            'success': True,
            'topic': topic,
            'questions': all_questions
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@grade7_ems_bp.route('/assessment', methods=['POST'])
def generate_assessment_paper():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No JSON payload provided'}), 400

        term = data.get('term', 'term1')
        target_marks = data.get('target_marks', 50)
        mode = data.get('mode', 'assessment')
        
        from app.utils.grade7_ems.assessment_generator import generate_assessment
        questions = generate_assessment(term=term, target_marks=target_marks, mode=mode)
        
        return jsonify({
            'success': True,
            'term': term,
            'total_marks': sum(int(q.get('marks', 1)) for q in questions),
            'questions': questions
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
