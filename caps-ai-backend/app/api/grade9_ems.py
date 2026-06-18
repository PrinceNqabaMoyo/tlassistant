from flask import Blueprint, jsonify, request
from app.utils.grade9_ems import (
    term1_crj_cpj,
    term1_general_ledger,
    term1_economy,
    term2_debtors_journal,
    term2_economy,
    term3_creditors_journal,
    term3_debtors_ledger,
    term3_business,
    assessment_generator
)

grade9_ems_bp = Blueprint('grade9_ems', __name__)

@grade9_ems_bp.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data.get('topic', 'crj')
    mode = data.get('mode', 'practice')
    
    # Simple mapping
    if topic == 'crj':
        return jsonify(term1_crj_cpj.generate(subskill="crj", mode=mode))
    elif topic == 'cpj':
        return jsonify(term1_crj_cpj.generate(subskill="cpj", mode=mode))
    elif topic == 'general_ledger':
        return jsonify(term1_general_ledger.generate(mode=mode))
    elif topic == 'economic_systems':
        return jsonify(term1_economy.generate(mode=mode))
    elif topic == 'debtors_journal':
        return jsonify(term2_debtors_journal.generate(mode=mode))
    elif topic == 'price_theory':
        return jsonify(term2_economy.generate(mode=mode))
    elif topic == 'creditors_journal':
        return jsonify(term3_creditors_journal.generate(mode=mode))
    elif topic == 'debtors_ledger':
        return jsonify(term3_debtors_ledger.generate(mode=mode))
    elif topic == 'business_functions':
        return jsonify(term3_business.generate(mode=mode))
    elif topic == 'assessment':
        return jsonify(assessment_generator.generate(mode=mode, count=5))
    else:
        return jsonify({"error": f"Unknown topic: {topic}"}), 400
