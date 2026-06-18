from flask import Blueprint, jsonify
from app.utils.firebase_admin_client import get_firestore_client

school_admin_bp = Blueprint('school_admin', __name__)

@school_admin_bp.route('/teachers', methods=['GET'])
def get_all_teachers():
    """Get all users with teacher role."""
    try:
        firestore_db = get_firestore_client()
        users_ref = firestore_db.collection('users')
        teachers = []
        for doc in users_ref.stream():
            data = doc.to_dict()
            if data.get('role') == 'teacher':
                teachers.append({"id": doc.id, **data})
        return jsonify({"teachers": teachers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@school_admin_bp.route('/classes', methods=['GET'])
def get_all_classes():
    """Aggregate all teacher classes across the system."""
    try:
        firestore_db = get_firestore_client()
        users_ref = firestore_db.collection('users')
        all_classes = []
        for user_doc in users_ref.stream():
            user_id = user_doc.id
            classes_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(user_id).collection('teacher_classes')
            for cls in classes_ref.stream():
                data = cls.to_dict()
                all_classes.append({
                    "id": cls.id,
                    "teacherId": user_id,
                    **data
                })
        return jsonify({"classes": all_classes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@school_admin_bp.route('/marks-summary', methods=['GET'])
def get_marks_summary():
    """Aggregate marks across all classes for reporting."""
    try:
        firestore_db = get_firestore_client()
        # Placeholder: actual marks collection structure would be needed
        return jsonify({"message": "Marks summary endpoint - implement when marks schema is finalized"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@school_admin_bp.route('/subscription-check', methods=['GET'])
def check_subscriptions():
    """Check which students have active subscriptions."""
    try:
        firestore_db = get_firestore_client()
        users_ref = firestore_db.collection('users')
        subscribed = 0
        unsubscribed = 0
        for doc in users_ref.stream():
            data = doc.to_dict()
            if data.get('role') == 'student':
                if data.get('subscriptionStatus') == 'active':
                    subscribed += 1
                else:
                    unsubscribed += 1
        return jsonify({"subscribed": subscribed, "unsubscribed": unsubscribed}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
