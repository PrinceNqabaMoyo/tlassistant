from flask import Blueprint, request, jsonify
from langchain_core.messages import HumanMessage, AIMessage

from app.services.agent_service import agent_executors, format_structured_answer

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('', methods=['POST'])
def handle_agent_query():
    if not agent_executors:
        return jsonify({"error": "Agents not initialized"}), 500
    
    data = request.get_json()
    user_input = data.get("input")
    chat_history_json = data.get("chat_history", [])
    user_role = data.get("user_role", "Student") # Default to Student if no role is provided
    user_tier = data.get("subscription", "standard")
    user_id = data.get("user_id")

    # Gate access for students without Pro subscription
    if user_role.lower() == "student" and user_tier != "pro":
        return jsonify({"error": "AI Chat requires Pro subscription"}), 403

    # Capitalize the user role to match the agent_executors dictionary keys
    capitalized_role = user_role.capitalize()
    agent_executor = agent_executors.get(capitalized_role)
    
    if not agent_executor:
        return jsonify({"error": f"Invalid user role: {user_role}"}), 400

    final_input_for_agent = user_input

    if isinstance(user_input, dict):
        question_text = user_input.get("question", "A student submitted the following answer to a previous question:")
        answer_data = user_input.get("answer", {})
        formatted_answer_str = format_structured_answer(answer_data)
        final_input_for_agent = f'Question: "{question_text}"\n\n{formatted_answer_str}'

    chat_history = []
    for msg in chat_history_json:
        try:
            role = msg['role']
            content = msg['content']
            if role == 'human':
                chat_history.append(HumanMessage(content=content))
            else:
                chat_history.append(AIMessage(content=content))
        except KeyError as e:
            print(f"KeyError: Missing key {e} in chat history message: {msg}")
            continue

    try:
        invoke_payload = {"input": final_input_for_agent, "chat_history": chat_history}
        if user_id:
            invoke_payload["user_id"] = user_id
        response = agent_executor.invoke(invoke_payload)
        return jsonify({"output": response.get('output')})
    except Exception as e:
        print(f"Error during agent invocation: {e}")
        return jsonify({"error": str(e)}), 500
