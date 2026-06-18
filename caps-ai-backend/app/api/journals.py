from flask import Blueprint, request, jsonify

from app.services.journal_service import (
    get_available_journals,
    validate_cash_receipts_journal,
    validate_cash_payments_journal,
    mark_journal_submission
)

journals_bp = Blueprint('journals', __name__)

@journals_bp.route('/available', methods=['GET'])
def get_journals_route():
    """Get available journal templates."""
    try:
        journals = get_available_journals()
        return jsonify({"journals": journals})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@journals_bp.route('/validate', methods=['POST'])
def validate_journal_route():
    """Validate a journal submission."""
    try:
        data = request.get_json()
        journal_data = data.get("journal_data")
        journal_type = data.get("journal_type", "CRJ")
        
        if journal_type.upper() == "CRJ":
            result = validate_cash_receipts_journal(journal_data)
        elif journal_type.upper() == "CPJ":
            result = validate_cash_payments_journal(journal_data)
        else:
            return jsonify({"error": f"Unknown journal type: {journal_type}"}), 400
        
        return jsonify({"validation_result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@journals_bp.route('/mark', methods=['POST'])
def mark_journal_route():
    """Mark a journal submission against expected answer."""
    try:
        data = request.get_json()
        question_text = data.get("question_text", "")
        student_journal = data.get("student_journal")
        expected_journal = data.get("expected_journal")
        journal_type = data.get("journal_type", "CRJ")
        
        if not student_journal or not expected_journal:
            return jsonify({"error": "Missing journal data"}), 400
        
        result = mark_journal_submission(question_text, student_journal, expected_journal, journal_type)
        return jsonify({"marking_result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
