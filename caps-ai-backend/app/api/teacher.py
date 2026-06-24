import json
import os
import re
import datetime
from flask import Blueprint, request, jsonify
from app.utils.firebase_admin_client import get_firestore_client

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

teacher_bp = Blueprint('teacher', __name__)

def get_teacher_tier_status(teacher_id, firestore_db):
    """Check if teacher qualifies for free tier (average 15+ subscribed students per class)."""
    try:
        classes_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_classes')
        classes = list(classes_ref.stream())
        if not classes:
            return {'qualifies': False, 'average': 0, 'total_classes': 0}

        total_students = 0
        for cls in classes:
            data = cls.to_dict()
            enrolled = data.get('enrolledStudents', [])
            # Count only students with active subscriptions
            active_count = 0
            for student_id in enrolled:
                user_doc = firestore_db.collection('users').document(student_id).get()
                if user_doc.exists:
                    user_data = user_doc.to_dict()
                    if user_data.get('subscriptionStatus') == 'active':
                        active_count += 1
            total_students += active_count

        average = total_students / len(classes) if classes else 0
        return {
            'qualifies': average >= 15,
            'average': round(average, 1),
            'total_classes': len(classes),
            'total_subscribed_students': total_students,
        }
    except Exception as e:
        print(f"Error checking teacher tier: {e}")
        return {'qualifies': False, 'average': 0, 'total_classes': 0}

@teacher_bp.route('/tier-status/<teacher_id>', methods=['GET'])
def get_teacher_tier(teacher_id):
    """Returns whether the teacher qualifies for the free tier."""
    try:
        firestore_db = get_firestore_client()
        result = get_teacher_tier_status(teacher_id, firestore_db)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/classes/<teacher_id>', methods=['GET'])
def get_teacher_classes(teacher_id):
    """Get all classes for a teacher."""
    try:
        firestore_db = get_firestore_client()
        classes_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_classes')
        classes = []
        for doc in classes_ref.stream():
            classes.append({"id": doc.id, **doc.to_dict()})
        return jsonify({"classes": classes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/homework/<teacher_id>', methods=['GET'])
def get_teacher_homework(teacher_id):
    """Get all homework for a teacher."""
    try:
        firestore_db = get_firestore_client()
        hw_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_homework')
        homework = []
        for doc in hw_ref.stream():
            homework.append({"id": doc.id, **doc.to_dict()})
        return jsonify({"homework": homework}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/assessments/<teacher_id>', methods=['GET'])
def get_teacher_assessments(teacher_id):
    """Get all assessments for a teacher."""
    try:
        firestore_db = get_firestore_client()
        assess_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_assessments')
        assessments = []
        for doc in assess_ref.stream():
            assessments.append({"id": doc.id, **doc.to_dict()})
        return jsonify({"assessments": assessments}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/create-assessment', methods=['POST'])
def create_assessment():
    """
    Generates a new assessment with questions, a detailed marking scheme/rubric, and a worked solution.
    """
    data = request.get_json()
    topic = data.get("topic")
    grade = data.get("grade")
    num_questions = data.get("num_questions", 3)

    if not all([topic, grade]):
        return jsonify({"error": "Missing required parameters: topic and grade"}), 400

    if not GOOGLE_API_KEY:
        return jsonify({"error": "AI service not configured"}), 500

    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
    except Exception:
        return jsonify({"error": "AI service not available (missing LLM package)."}), 503

    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3, convert_system_message_to_human=True, google_api_key=GOOGLE_API_KEY)
    
    prompt_template = f"""
    You are an expert in creating educational materials for the South African CAPS curriculum.
    Your task is to generate an assessment for a Grade {grade} student on the topic of "{topic}".
    The assessment should contain exactly {num_questions} questions.

    For each question, you must provide:
    1. The question text.
    2. The question type (e.g., "short_answer_with_steps", "long_answer").
    3. A detailed marking scheme.
    4. A complete, step-by-step worked solution. The steps in the solution MUST be separated by a comma and a space.

    You MUST respond with ONLY a valid JSON object. Do not include any other text, explanations, or markdown formatting like ```json.
    The JSON object must have a single key "assessment" which is an array of question objects.
    Each question object must have the following keys: "question_text", "question_type", "marking_scheme", and "solution".
    The "marking_scheme" must be an array of objects, each with a "point" (the step or keyword) and "marks" (the value for that point).
    The "solution" must be a string containing the full worked-out answer, with each logical step separated by a comma and a space.

    Example of the required JSON structure:
    {{
      "assessment": [
        {{
          "question_text": "Solve for x: 2x + 5 = 15",
          "question_type": "short_answer_with_steps",
          "marking_scheme": [
            {{ "point": "Subtracts 5 from both sides (2x = 10)", "marks": 1 }},
            {{ "point": "Divides both sides by 2 (x = 5)", "marks": 1 }}
          ],
          "solution": "2x + 5 = 15, 2x = 15 - 5, 2x = 10, x = 10 / 2, x = 5"
        }},
        {{
          "question_text": "Define 'photosynthesis'.",
          "question_type": "long_answer",
          "marking_scheme": [
            {{ "point": "Mentions 'light energy' or 'sunlight'", "marks": 1 }},
            {{ "point": "Mentions 'carbon dioxide' and 'water'", "marks": 1 }},
            {{ "point": "Mentions 'glucose' or 'sugar' as a product", "marks": 1 }}
          ],
          "solution": "Photosynthesis is the process used by plants, algae, and some bacteria to convert light energy into chemical energy, through a process that converts carbon dioxide and water into glucose (sugar) and oxygen."
        }}
      ]
    }}
    """

    try:
        response = llm.invoke(prompt_template)
        ai_response_str = response.content
        
        # --- NEW: Robust JSON Extraction Logic ---
        # Find the start and end of the JSON block
        json_match = re.search(r'\{.*\}', ai_response_str, re.DOTALL)
        
        if not json_match:
            # If no JSON block is found at all, raise the error
            raise json.JSONDecodeError("No valid JSON object found in the AI's response.", ai_response_str, 0)
            
        json_str = json_match.group(0)
        assessment_data = json.loads(json_str)
        
        return jsonify(assessment_data)

    except json.JSONDecodeError:
        # This error is now more specific to a truly malformed JSON response
        return jsonify({"error": "Failed to decode the AI's JSON response. The response may be malformed."}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# --- Validation Helpers ---
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 5000
MAX_STUDENTS_PER_CLASS = 60
ALLOWED_SUBJECTS = {
    'accounting', 'business studies', 'ems', 'economics', 'mathematics',
    'maths', 'physical sciences', 'life sciences', 'geography', 'history',
    'english', 'afrikaans', 'isiZulu', 'isiXhosa', 'sesotho', 'setswana'
}
ALLOWED_GRADES = {'10', '11', '12'}

def sanitize_string(value, max_length):
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    if len(cleaned) > max_length:
        return None
    # Strip control chars except newlines/tabs
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', cleaned)
    return cleaned

def validate_class_payload(data):
    name = sanitize_string(data.get('name'), MAX_TITLE_LENGTH)
    subject = sanitize_string(data.get('subject'), 50)
    grade = sanitize_string(data.get('grade'), 10)
    description = sanitize_string(data.get('description', ''), MAX_DESCRIPTION_LENGTH)

    if not name or not subject or not grade:
        return None, "Missing required fields: name, subject, grade"
    if subject.lower() not in ALLOWED_SUBJECTS:
        return None, f"Invalid subject: {subject}"
    if grade not in ALLOWED_GRADES:
        return None, f"Invalid grade: {grade}"
    return {"name": name, "subject": subject, "grade": grade, "description": description}, None

def validate_homework_payload(data):
    title = sanitize_string(data.get('title'), MAX_TITLE_LENGTH)
    description = sanitize_string(data.get('description', ''), MAX_DESCRIPTION_LENGTH)
    class_id = sanitize_string(data.get('classId'), 100)
    due_date = sanitize_string(data.get('dueDate'), 50)

    if not title or not class_id or not due_date:
        return None, "Missing required fields: title, classId, dueDate"
    return {"title": title, "description": description, "classId": class_id, "dueDate": due_date}, None

def validate_assessment_payload(data):
    title = sanitize_string(data.get('title'), MAX_TITLE_LENGTH)
    description = sanitize_string(data.get('description', ''), MAX_DESCRIPTION_LENGTH)
    class_id = sanitize_string(data.get('classId'), 100)
    due_date = sanitize_string(data.get('dueDate'), 50)
    duration = data.get('durationMinutes', 60)

    if not title or not class_id or not due_date:
        return None, "Missing required fields: title, classId, dueDate"
    if not isinstance(duration, int) or not (10 <= duration <= 180):
        return None, "durationMinutes must be an integer between 10 and 180"
    return {"title": title, "description": description, "classId": class_id, "dueDate": due_date, "durationMinutes": duration}, None


# --- Write Endpoints with Validation ---
@teacher_bp.route('/classes/<teacher_id>', methods=['POST'])
def create_teacher_class(teacher_id):
    """Create a new class for a teacher with server-side validation."""
    data = request.get_json(silent=True) or {}
    payload, error = validate_class_payload(data)
    if error:
        return jsonify({"error": error}), 400

    try:
        firestore_db = get_firestore_client()
        class_id = f"class-{int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)}"
        class_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_classes').document(class_id)
        class_ref.set({
            **payload,
            "teacherId": teacher_id,
            "createdAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "enrolledStudents": []
        })
        return jsonify({"id": class_id, **payload}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/classes/<teacher_id>/<class_id>/enroll', methods=['POST'])
def enroll_student(teacher_id, class_id):
    """Enroll a student into a class with validation."""
    data = request.get_json(silent=True) or {}
    student_id = sanitize_string(data.get('studentId'), 100)
    if not student_id:
        return jsonify({"error": "Missing studentId"}), 400

    try:
        firestore_db = get_firestore_client()
        class_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_classes').document(class_id)
        class_doc = class_ref.get()
        if not class_doc.exists:
            return jsonify({"error": "Class not found"}), 404

        enrolled = class_doc.to_dict().get('enrolledStudents', [])
        if len(enrolled) >= MAX_STUDENTS_PER_CLASS:
            return jsonify({"error": f"Class is full (max {MAX_STUDENTS_PER_CLASS})"}), 400
        if student_id not in enrolled:
            enrolled.append(student_id)
            class_ref.update({"enrolledStudents": enrolled})
        return jsonify({"enrolledStudents": enrolled}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/homework/<teacher_id>', methods=['POST'])
def create_teacher_homework(teacher_id):
    """Create homework with server-side validation."""
    data = request.get_json(silent=True) or {}
    payload, error = validate_homework_payload(data)
    if error:
        return jsonify({"error": error}), 400

    try:
        firestore_db = get_firestore_client()
        hw_id = f"hw-{int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)}"
        hw_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_homework').document(hw_id)
        hw_ref.set({
            **payload,
            "showMarksImmediately": bool(data.get('showMarksImmediately', False)),
            "teacherId": teacher_id,
            "createdAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "status": "active"
        })
        return jsonify({"id": hw_id, **payload}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@teacher_bp.route('/assessments/<teacher_id>', methods=['POST'])
def create_teacher_assessment(teacher_id):
    """Create assessment with server-side validation."""
    data = request.get_json(silent=True) or {}
    payload, error = validate_assessment_payload(data)
    if error:
        return jsonify({"error": error}), 400

    try:
        firestore_db = get_firestore_client()
        assess_id = f"assess-{int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)}"
        assess_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(teacher_id).collection('teacher_assessments').document(assess_id)
        assess_ref.set({
            **payload,
            "showMarksImmediately": bool(data.get('showMarksImmediately', False)),
            "teacherId": teacher_id,
            "createdAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "status": "active"
        })
        return jsonify({"id": assess_id, **payload}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
