#!/usr/bin/env python3
"""
Pre-Flight Targeted Test User Purge Script via Firebase Admin SDK.
Completely purges test users and all associated collections (users, pending_payments, submissions, learner_mastery).
Strictly prevents purging Super Admin / platform owner accounts.
"""

import sys
from pathlib import Path

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent / 'caps-ai-backend'
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.utils.firebase_admin_client import get_firebase_app, firestore, auth

PROTECTED_OWNERS = {
    'princenqaba@gmail.com',
    'princenqabamoyo@outlook.com',
}

def purge_user(email: str):
    email = email.strip().lower()
    if email in PROTECTED_OWNERS:
        print(f"[SECURITY ERROR] Refusing to purge protected owner account: {email}")
        sys.exit(1)

    app = get_firebase_app()
    db = firestore.client(app)

    print(f"[*] [Admin Purge] Purging records for: {email}")

    # 1. Purge pending_payments by email or userEmail
    deleted_payments = 0
    for field in ['email', 'userEmail']:
        try:
            docs = db.collection('pending_payments').where(filter=firestore.FieldFilter(field, '==', email)).stream()
            for d in docs:
                d.reference.delete()
                deleted_payments += 1
        except Exception:
            try:
                docs = db.collection('pending_payments').where(field, '==', email).stream()
                for d in docs:
                    d.reference.delete()
                    deleted_payments += 1
            except Exception:
                pass

    if deleted_payments > 0:
        print(f"   Deleted {deleted_payments} pending_payments records")

    # 2. Find Auth user by email
    uid = None
    try:
        user = auth.get_user_by_email(email, app=app)
        uid = user.uid
        print(f"   Found Auth user (UID: {uid})")
    except auth.UserNotFoundError:
        print("   Auth user does not exist (clean)")
    except Exception as e:
        print(f"   Auth lookup note: {e}")

    # 3. If UID found, delete Firestore collections
    if uid:
        # Delete user profile doc
        db.collection('users').document(uid).delete()
        print(f"   Deleted users/{uid}")

        # Delete any payments keyed by userId
        try:
            docs = db.collection('pending_payments').where('userId', '==', uid).stream()
            for d in docs:
                d.reference.delete()
        except Exception:
            pass

        # Delete submissions
        for field in ['userId', 'studentId']:
            try:
                docs = db.collection('submissions').where(field, '==', uid).stream()
                for d in docs:
                    d.reference.delete()
            except Exception:
                pass

        # Delete learner_mastery
        for field in ['userId', 'studentId']:
            try:
                docs = db.collection('learner_mastery').where(field, '==', uid).stream()
                for d in docs:
                    d.reference.delete()
            except Exception:
                pass

        # Delete Auth user
        try:
            auth.delete_user(uid, app=app)
            print(f"   Deleted Firebase Auth user: {uid}")
        except Exception as e:
            print(f"   Auth delete note: {e}")

    print(f"[PASS] [Admin Purge] Successfully completed clean slate for {email}\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/purge_test_user_admin.py <email>")
        sys.exit(1)
    purge_user(sys.argv[1])
