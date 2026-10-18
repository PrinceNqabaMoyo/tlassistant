import sys
from pathlib import Path
import requests
import google.auth.transport.requests
from google.oauth2 import service_account

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / 'caps-ai-backend'))

from app.utils.firebase_admin_client import _resolve_credentials_path

def deploy_rules():
    rules_path = ROOT_DIR / 'firestore.rules'
    if not rules_path.exists():
        print(f"Error: {rules_path} does not exist")
        sys.exit(1)

    rules_content = rules_path.read_text(encoding='utf-8')

    creds_path = _resolve_credentials_path()
    creds = service_account.Credentials.from_service_account_file(
        str(creds_path),
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    req = google.auth.transport.requests.Request()
    creds.refresh(req)

    project_id = 'caps-ai-math-assistant-app'
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }

    # 1. Create Ruleset
    print("[*] Uploading new firestore.rules ruleset...")
    create_url = f'https://firebaserules.googleapis.com/v1/projects/{project_id}/rulesets'
    create_body = {
        'source': {
            'files': [
                {
                    'name': 'firestore.rules',
                    'content': rules_content
                }
            ]
        }
    }
    resp = requests.post(create_url, json=create_body, headers=headers)
    if resp.status_code != 200:
        print(f"[!] Failed to create ruleset ({resp.status_code}): {resp.text}")
        sys.exit(1)

    ruleset_data = resp.json()
    ruleset_name = ruleset_data['name']
    print(f"[+] Successfully created ruleset: {ruleset_name}")

    # 2. Update Release
    print("[*] Releasing new ruleset to cloud.firestore...")
    release_url = f'https://firebaserules.googleapis.com/v1/projects/{project_id}/releases/cloud.firestore'
    release_body = {
        'release': {
            'name': f'projects/{project_id}/releases/cloud.firestore',
            'rulesetName': ruleset_name
        }
    }
    patch_resp = requests.patch(release_url, json=release_body, headers=headers)
    if patch_resp.status_code != 200:
        print(f"[!] Failed to update release ({patch_resp.status_code}): {patch_resp.text}")
        sys.exit(1)

    print("[SUCCESS] Cloud Firestore security rules successfully deployed and active!")

if __name__ == '__main__':
    deploy_rules()
