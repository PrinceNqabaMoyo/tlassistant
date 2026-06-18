import re
import time

from flask import current_app, jsonify, request

from . import payments_bp
from ...utils.firebase_admin_client import get_firestore_client, verify_firebase_id_token
from ...utils.supabase_storage import create_private_object_signed_url, delete_private_object, upload_private_object
from ...services.email_service import send_pop_notification_async


MAX_POP_FILE_SIZE_BYTES = 10 * 1024 * 1024
ACCEPTED_POP_FILE_TYPES = {'application/pdf', 'image/jpeg', 'image/png'}


def _json_error(message, status_code):
    return jsonify({'success': False, 'error': message}), status_code


def _sanitize_file_name(value=''):
    return re.sub(r'[^a-zA-Z0-9._-]', '_', str(value or 'upload'))


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


def _get_bucket_name():
    bucket_name = current_app.config.get('SUPABASE_POP_BUCKET')
    if not bucket_name:
        raise RuntimeError('SUPABASE_POP_BUCKET is not configured on the backend.')
    return bucket_name


def _read_uploaded_file():
    uploaded_file = request.files.get('file')
    if not uploaded_file or not uploaded_file.filename:
        raise ValueError('Please attach a POP file before uploading.')

    mime_type = uploaded_file.mimetype or 'application/octet-stream'
    if mime_type not in ACCEPTED_POP_FILE_TYPES:
        raise ValueError('Only PDF, JPG, and PNG files are accepted for proof of payment uploads.')

    file_bytes = uploaded_file.read()
    if not file_bytes:
        raise ValueError('The selected POP file is empty. Please choose a valid file and try again.')
    if len(file_bytes) > MAX_POP_FILE_SIZE_BYTES:
        raise ValueError('The selected file is too large. Please upload a file smaller than 10 MB.')

    return uploaded_file, mime_type, file_bytes


def _is_admin_user(user_id, email=None):
    if email in ['princenqaba@gmail.com', 'princenqabamoyo@outlook.com']:
        return True

    firestore_client = get_firestore_client()
    user_snapshot = firestore_client.collection('users').document(user_id).get()
    if not user_snapshot.exists:
        return False

    user_data = user_snapshot.to_dict() or {}
    return bool(user_data.get('isOwner') or user_data.get('isSuperAdmin') or user_data.get('role') == 'admin')


@payments_bp.route('/pop-upload', methods=['POST'])
def upload_pop():
    try:
        decoded_token = _verify_request_user()
        uploaded_file, mime_type, file_bytes = _read_uploaded_file()
        safe_file_name = f"{int(time.time() * 1000)}_{_sanitize_file_name(uploaded_file.filename)}"
        object_path = f"proofs_of_payment/{decoded_token['uid']}/{safe_file_name}"
        bucket_name = _get_bucket_name()

        upload_private_object(bucket_name, object_path, file_bytes, mime_type)

        user_email = decoded_token.get('email', f"User {decoded_token['uid']}")
        send_pop_notification_async(user_email, uploaded_file.filename, object_path)

        return jsonify({
            'success': True,
            'upload': {
                'storagePath': object_path,
                'fileName': uploaded_file.filename,
                'mimeType': mime_type,
                'fileSizeBytes': len(file_bytes),
                'storageProvider': 'supabase',
                'storageBucket': bucket_name,
            },
        })
    except PermissionError as error:
        return _json_error(str(error), 401)
    except ValueError as error:
        return _json_error(str(error), 400)
    except Exception as error:
        return _json_error(str(error), 500)


@payments_bp.route('/pop-delete', methods=['POST'])
def delete_pop():
    try:
        decoded_token = _verify_request_user()
        payload = request.get_json(silent=True) or {}
        storage_path = str(payload.get('storagePath') or '').strip()
        if not storage_path:
            raise ValueError('Missing POP storage path.')

        expected_prefix = f"proofs_of_payment/{decoded_token['uid']}/"
        if not storage_path.startswith(expected_prefix):
            raise PermissionError('You can only remove POP files that belong to your account.')

        delete_private_object(_get_bucket_name(), storage_path)
        return jsonify({'success': True})
    except PermissionError as error:
        return _json_error(str(error), 403)
    except ValueError as error:
        return _json_error(str(error), 400)
    except Exception as error:
        return _json_error(str(error), 500)


@payments_bp.route('/pop-view-url', methods=['POST'])
def create_pop_view_url():
    try:
        decoded_token = _verify_request_user()
        if not _is_admin_user(decoded_token['uid'], decoded_token.get('email')):
            raise PermissionError('Only admins can view POP files.')

        payload = request.get_json(silent=True) or {}
        storage_path = str(payload.get('storagePath') or '').strip()
        if not storage_path:
            raise ValueError('Missing POP storage path.')

        signed_url = create_private_object_signed_url(_get_bucket_name(), storage_path, expires_in=900)
        return jsonify({'success': True, 'url': signed_url})
    except PermissionError as error:
        return _json_error(str(error), 403)
    except ValueError as error:
        return _json_error(str(error), 400)
    except Exception as error:
        return _json_error(str(error), 500)
