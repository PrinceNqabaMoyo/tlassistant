from flask import Blueprint, request, jsonify

from app.services.agent_service import run_agent

agent_bp = Blueprint('agent', __name__)


@agent_bp.route('/chat', methods=['POST'])
def handle_agent_chat():
    """Topic-bound agent endpoint. No freeform chat.

    Required context keys: subject, grade, topic, subskill.
    Optional context keys: sample_answer, marking_points, wiki_content.
    """
    data = request.get_json() or {}
    user_input = data.get("input")
    user_tier = data.get("subscription", "standard")
    user_id = data.get("user_id")
    context = data.get("context", {})
    chat_history = data.get("chat_history", [])

    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    if not all(k in context for k in ("subject", "grade", "topic", "subskill")):
        return jsonify({"error": "Missing agent context. Required: subject, grade, topic, subskill"}), 400

    if user_tier != "pro":
        return jsonify({"error": "AI Chat requires Pro subscription"}), 403

    try:
        response = run_agent(
            user_input=user_input,
            context=context,
            chat_history=chat_history,
            user_id=user_id,
            tier=user_tier,
        )
        return jsonify(response)
    except Exception as e:
        print(f"Error during agent invocation: {e}")
        return jsonify({"error": str(e)}), 500
