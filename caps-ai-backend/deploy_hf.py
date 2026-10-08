import os
import sys
import subprocess

def ensure_huggingface_hub():
    """Ensure the huggingface_hub library is installed."""
    try:
        import huggingface_hub
        print("huggingface_hub is already installed.")
    except ImportError:
        print("huggingface_hub is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub"])
        print("Installation complete.\n")

def deploy_to_huggingface():
    """Uploads the current directory to the specified Hugging Face Space."""
    from huggingface_hub import HfApi, login

    # --- CONFIGURATION ---
    # Replace these with your actual Hugging Face details
    HF_USERNAME = "snombi"  # e.g. "princ"
    HF_SPACE_NAME = "tlassistant" # e.g. "caps-ai-backend"
    REPO_ID = f"{HF_USERNAME}/{HF_SPACE_NAME}"
    from pathlib import Path

    BACKEND_DIR = Path(__file__).resolve().parent
    
    # Files and folders to IGNORE during upload (keeps the deployment clean)
    IGNORE_PATTERNS = [
        "venv/*",
        ".venv/*",
        ".git/*",
        "__pycache__/*",
        "*/__pycache__/*",
        "*/**/__pycache__/*",
        "*.pyc",
        "*.zip",
        "deploy_hf.py",  # Don't upload this script itself
        ".env",          # Never upload local secrets
        "curriculum_docs/*",
        "curriculum_docs_auto/*",
        "tests/*",
        "chroma_db_langchain/*",
        "*.sqlite3",
        "node_modules/*",
        ".cache/*",
    ]

    print("=== Hugging Face Deployment Pipeline ===")
    print(f"Target Space: {REPO_ID}")
    print(f"Source Directory: {BACKEND_DIR}\n")

    # The API will automatically use the token from `huggingface-cli login` if you've run it before.
    # Otherwise, it will prompt you.
    api = HfApi()
    
    try:
        # Check if the user is authenticated
        api.whoami()
        print("Authentication successful!")
    except Exception:
        print("You are not logged in to Hugging Face.")
        print("Please grab an Access Token from https://huggingface.co/settings/tokens (Ensure it has WRITE permissions).")
        token = input("Enter your Hugging Face Write Token: ").strip()
        login(token)
        print("Login successful!\n")

    print(f"Uploading backend files to {REPO_ID}...")
    print("(This process handles replacements of changed files automatically)")

    try:
        # Upload the backend folder (caps-ai-backend) to the Space root
        api.upload_folder(
            folder_path=str(BACKEND_DIR),
            repo_id=REPO_ID,
            repo_type="space",
            commit_message="Pipeline Deployment: Grades 7-12 Senior & FET Phase updates, curriculum sync",
            ignore_patterns=IGNORE_PATTERNS,
            delete_patterns="*", # This ensures files deleted locally are also deleted on Hugging Face
        )
        print("\n[SUCCESS] Deployment completed successfully!")
        print(f"Check your space at: https://huggingface.co/spaces/{REPO_ID}")
    except Exception as e:
        print(f"\n[FAILED] Deployment failed: {e}")

if __name__ == "__main__":
    ensure_huggingface_hub()
    

    deploy_to_huggingface()
