from flask import Blueprint, request, jsonify
from app.services.orchestrator_service import (
    generate_study_plan,
    check_and_notify,
    initialize_orchestrator,
)

orchestrator_bp = Blueprint('orchestrator', __name__)


@orchestrator_bp.route('/study-plan', methods=['POST'])
def handle_study_plan():
    """Generates a weekly study plan for a student.
    Body: {"user_id": "..."}
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        result = generate_study_plan(user_id)
        return jsonify(result)
    except Exception as e:
        print(f"Error generating study plan: {e}")
        return jsonify({"error": str(e)}), 500


@orchestrator_bp.route('/check-notify', methods=['POST'])
def handle_check_and_notify():
    """Runs the daily check and creates notifications.
    Body: {"user_id": "..."}
    Returns the list of notifications created.
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        result = check_and_notify(user_id)
        return jsonify(result)
    except Exception as e:
        print(f"Error during check-and-notify: {e}")
        return jsonify({"error": str(e)}), 500


@orchestrator_bp.route('/run', methods=['POST'])
def handle_run_orchestrator():
    """Full orchestrator run: study plan + notifications.
    Body: {"user_id": "..."}
    Can also be called with {"all_users": true} for batch processing (admin only).
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        plan_result = generate_study_plan(user_id)
        notify_result = check_and_notify(user_id)
        return jsonify({
            "status": "ok",
            "study_plan": plan_result,
            "notifications": notify_result,
        })
    except Exception as e:
        print(f"Error during orchestrator run: {e}")
        return jsonify({"error": str(e)}), 500
