import os
import requests
from threading import Thread

def send_pop_notification_async(user_email: str, file_name: str, storage_path: str):
    """
    Spawns a background thread to send the email via Resend API.
    """
    thread = Thread(target=_send_pop_notification, args=(user_email, file_name, storage_path))
    thread.daemon = True
    thread.start()

def _send_pop_notification(user_email: str, file_name: str, storage_path: str):
    """
    Sends an email to payments@fundile.com using the Resend HTTP API.
    """
    resend_api_key = os.getenv('RESEND_API_KEY')
    
    # We send TO payments@fundile.com, FROM payments@fundile.com
    recipient = "payments@fundile.com"
    sender = "Fundile System <payments@fundile.com>"

    if not resend_api_key:
        print("RESEND_API_KEY not set. Skipping POP notification email.", flush=True)
        return

    body = f"""Hello Sales/Payments Team,

A user has just submitted a new Proof of Payment for review.

User Email: {user_email}
File Name: {file_name}
Storage Path: {storage_path}

Please log in to the Fundile User Management Dashboard to review this Proof of Payment.

Best regards,
Fundile System
"""

    headers = {
        "Authorization": f"Bearer {resend_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": sender,
        "to": [recipient],
        "subject": f"New Proof of Payment Uploaded by {user_email}",
        "text": body
    }

    try:
        response = requests.post("https://api.resend.com/emails", headers=headers, json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            print(f"Successfully sent POP notification email to {recipient} via Resend API.", flush=True)
        else:
            print(f"Error from Resend API: {response.status_code} - {response.text}", flush=True)
    except Exception as e:
        print(f"Error sending POP notification email via Resend: {str(e)}", flush=True)
