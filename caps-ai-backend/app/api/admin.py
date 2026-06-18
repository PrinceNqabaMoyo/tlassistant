import os
import datetime
from flask import Blueprint, jsonify
from app.utils.firebase_admin_client import get_firestore_client

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/delete-expired-solved-problems', methods=['POST'])
def delete_expired_solved_problems():
    """
    Deletes solved_freeform_problems documents where retentionDate has passed.
    This endpoint is intended to be called by a scheduled job, not directly by the frontend.
    """
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
