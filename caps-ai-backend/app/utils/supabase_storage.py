import json
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from flask import current_app


def _get_supabase_url():
    url = current_app.config.get('SUPABASE_URL')
    if not url:
        raise RuntimeError('SUPABASE_URL is not configured on the backend.')
    return str(url).rstrip('/')


def _get_supabase_server_key():
    key = current_app.config.get('SUPABASE_SECRET_KEY') or current_app.config.get('SUPABASE_SERVICE_ROLE_KEY')
    if not key:
        raise RuntimeError('SUPABASE_SECRET_KEY or SUPABASE_SERVICE_ROLE_KEY is required on the backend.')
    return key


def _perform_storage_request(method, path, data=None, headers=None):
    base_url = _get_supabase_url()
    server_key = _get_supabase_server_key()
    request_headers = {
        'apikey': server_key,
        'Authorization': f'Bearer {server_key}',
        **(headers or {}),
    }

    request = Request(f'{base_url}{path}', data=data, headers=request_headers, method=method)

    try:
        with urlopen(request, timeout=60) as response:
            return response.getcode(), response.read(), response.headers
    except HTTPError as error:
        error_body = error.read().decode('utf-8', errors='ignore')
        raise RuntimeError(error_body or str(error.reason)) from error
    except URLError as error:
        raise RuntimeError(str(error.reason)) from error


def upload_private_object(bucket_name, object_path, file_bytes, content_type):
    encoded_bucket = quote(bucket_name, safe='')
    encoded_object_path = quote(object_path, safe='/')
    _perform_storage_request(
        'POST',
        f'/storage/v1/object/{encoded_bucket}/{encoded_object_path}',
        data=file_bytes,
        headers={
            'Content-Type': content_type or 'application/octet-stream',
            'x-upsert': 'false',
        },
    )


def delete_private_object(bucket_name, object_path):
    encoded_bucket = quote(bucket_name, safe='')
    encoded_object_path = quote(object_path, safe='/')
    _perform_storage_request('DELETE', f'/storage/v1/object/{encoded_bucket}/{encoded_object_path}')


def create_private_object_signed_url(bucket_name, object_path, expires_in=600):
    encoded_bucket = quote(bucket_name, safe='')
    encoded_object_path = quote(object_path, safe='/')
    _, response_body, _ = _perform_storage_request(
        'POST',
        f'/storage/v1/object/sign/{encoded_bucket}/{encoded_object_path}',
        data=json.dumps({'expiresIn': expires_in}).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
    )
    payload = json.loads(response_body.decode('utf-8') or '{}')
    signed_url_path = payload.get('signedURL') or payload.get('signedUrl') or payload.get('url')
    if not signed_url_path:
        raise RuntimeError('Supabase did not return a signed POP URL.')

    base_url = _get_supabase_url()
    if str(signed_url_path).startswith('http'):
        return signed_url_path
    if str(signed_url_path).startswith('/'):
        return f'{base_url}/storage/v1{signed_url_path}'
    return f'{base_url}/storage/v1/{str(signed_url_path).lstrip("/")}'
