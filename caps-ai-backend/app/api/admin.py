import os
import datetime
from flask import Blueprint, jsonify, request
from app.utils.firebase_admin_client import get_firestore_client, verify_firebase_id_token

admin_bp = Blueprint('admin', __name__)

def _get_bearer_token():
    authorization = request.headers.get('Authorization', '')
    if not authorization.startswith('Bearer '):
        raise PermissionError('Missing Firebase bearer token.')
    token = authorization.split(' ', 1)[1].strip()
    if not token:
        raise PermissionError('Missing Firebase bearer token.')
    return token

def _verify_request_user():
    return verify_firebase_id_token(_get_bearer_token())

def _is_admin_user(user_id, email=None):
    if email in ['princenqaba@gmail.com', 'princenqabamoyo@outlook.com']:
        return True
    try:
        firestore_client = get_firestore_client()
        user_snapshot = firestore_client.collection('users').document(user_id).get()
        if not user_snapshot.exists:
            return False
        user_data = user_snapshot.to_dict() or {}
        return bool(user_data.get('isOwner') or user_data.get('isSuperAdmin') or user_data.get('role') == 'admin')
    except Exception:
        return False

@admin_bp.route('/delete-expired-solved-problems', methods=['POST'])
def delete_expired_solved_problems():
    """
    Deletes solved_freeform_problems documents where retentionDate has passed.
    Protected endpoint: Requires valid Firebase Bearer token and Admin privileges.
    """
    try:
        user_info = _verify_request_user()
        user_id = user_info.get('uid')
        email = user_info.get('email')
        if not _is_admin_user(user_id, email):
            return jsonify({'error': 'Unauthorized: Administrator privileges required.'}), 403
    except PermissionError as pe:
        return jsonify({'error': str(pe)}), 401
    except Exception as e:
        return jsonify({'error': f'Authentication failed: {str(e)}'}), 401

    print("Starting deletion of expired solved problems...")
    
    now = datetime.datetime.now(datetime.timezone.utc)
    app_id = os.getenv("FIREBASE_APP_ID", "default-app-id") 

    deleted_count = 0
    batch_size = 500 # Firestore limit for batch writes

    try:
        firestore_db = get_firestore_client()
        users_ref = firestore_db.collection('users')
        users_docs = users_ref.stream()

        for user_doc in users_docs:
            user_id = user_doc.id
            print(f"Processing user: {user_id}")
            
            problems_ref = firestore_db.collection('artifacts').document(app_id).collection('users').document(user_id).collection('solved_freeform_problems')
            query_ref = problems_ref.where('retentionDate', '<=', now.isoformat()) 

            while True:
                docs_to_delete = query_ref.limit(batch_size).stream()
                batch = firestore_db.batch()
                
                doc_count_in_batch = 0
                for doc_snapshot in docs_to_delete:
                    batch.delete(doc_snapshot.reference)
                    doc_count_in_batch += 1
                
                if doc_count_in_batch == 0:
                    break 

                batch.commit()
                deleted_count += doc_count_in_batch
                print(f"  Deleted {doc_count_in_batch} problems for user {user_id}. Total deleted: {deleted_count}")

                if doc_count_in_batch < batch_size:
                    break

        print(f"Finished deleting expired solved problems. Total deleted: {deleted_count}")
        return jsonify({"message": f"Successfully deleted {deleted_count} expired solved problems."}), 200

    except Exception as e:
        print(f"Error during deletion of expired solved problems: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
