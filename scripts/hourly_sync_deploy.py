"""
Hourly Code Check, GitHub Sync & Dual Redeployment Pipeline
===========================================================
Automates the hourly cycle for Fundile TLAssistant:
1. Inspects repository for local modifications and remote updates.
2. Verifies frontend build and regenerates architecture HTML (Rule 0c).
3. Synchronizes updates to GitHub (commit & push to origin/main).
4. Redeploys frontend to Firebase Hosting if frontend files changed.
5. Redeploys backend to Hugging Face Spaces if backend files changed.

Usage:
  python scripts/hourly_sync_deploy.py --once       # Run single check & deploy cycle
  python scripts/hourly_sync_deploy.py --daemon     # Run recurring loop every hour
  python scripts/hourly_sync_deploy.py --dry-run    # Inspect changes without deploying
"""

import os
import sys
import time
import argparse
import subprocess
import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

FRONTEND_PATTERNS = [
    "src/",
    "public/",
    "index.html",
    "vite.config.js",
    "package.json",
    "package-lock.json",
    "firestore.rules",
]

BACKEND_PATTERNS = [
    "caps-ai-backend/",
]

def log(msg, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = {
        "INFO": "[INFO]",
        "SUCCESS": "[SUCCESS]",
        "WARN": "[WARN]",
        "ERROR": "[ERROR]",
        "CYCLE": "[CYCLE]"
    }.get(level, "[INFO]")
    print(f"[{timestamp}] {prefix} {msg}", flush=True)

def run_cmd(cmd, cwd=ROOT_DIR, capture=True, check=False):
    """Run shell command with clean logging."""
    try:
        if capture:
            res = subprocess.run(
                cmd,
                cwd=cwd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            return res.returncode, res.stdout.strip(), res.stderr.strip()
        else:
            res = subprocess.run(cmd, cwd=cwd, shell=True)
            return res.returncode, "", ""
    except Exception as e:
        return 1, "", str(e)

def get_git_status():
    """Returns list of modified/untracked files."""
    code, out, _ = run_cmd("git status --porcelain")
    if code != 0 or not out:
        return []
    lines = [line.strip() for line in out.splitlines() if line.strip()]
    changed_files = []
    for line in lines:
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            changed_files.append(parts[1])
    return changed_files

def check_remote_updates():
    """Fetches origin and checks if remote has new commits."""
    log("Checking remote GitHub tracking branch (origin/main)...")
    code, _, err = run_cmd("git fetch origin main --quiet")
    if code != 0:
        log(f"git fetch failed or offline: {err}", "WARN")
        return False, 0

    code, out, _ = run_cmd("git rev-list HEAD..origin/main --count")
    if code == 0 and out.isdigit():
        behind_count = int(out)
        return True, behind_count
    return True, 0

def has_file_match(file_list, patterns):
    for f in file_list:
        f_norm = f.replace("\\", "/")
        for p in patterns:
            if f_norm.startswith(p) or f_norm == p.rstrip("/"):
                return True
    return False

def execute_hourly_cycle(dry_run=False, skip_fe=False, skip_be=False, skip_push=False):
    log("=" * 65, "CYCLE")
    log("Starting Hourly Code Check, GitHub Sync & Redeployment Cycle", "CYCLE")
    log(f"Working Directory: {ROOT_DIR}")
    
    # 1. Check for remote updates
    remote_ok, behind_count = check_remote_updates()
    if remote_ok and behind_count > 0:
        log(f"Remote branch has {behind_count} new commits. Pulling updates...", "INFO")
        if not dry_run:
            pull_code, pull_out, pull_err = run_cmd("git pull --rebase origin main")
            if pull_code != 0:
                log(f"git pull rebase failed: {pull_err}", "ERROR")
            else:
                log("Successfully pulled latest commits from origin/main.", "SUCCESS")

    # 2. Check local working tree modifications
    changed_files = get_git_status()
    log(f"Detected {len(changed_files)} changed/untracked file(s) in repository.")
    for f in changed_files[:10]:
        log(f"  • {f}")
    if len(changed_files) > 10:
        log(f"  ... and {len(changed_files) - 10} more files.")

    has_frontend_changes = has_file_match(changed_files, FRONTEND_PATTERNS)
    has_backend_changes = has_file_match(changed_files, BACKEND_PATTERNS)
    has_architecture_changes = "fundile-architecture.json" in changed_files

    if not changed_files and behind_count == 0:
        log("No code changes or remote commits detected. Heartbeat OK. Next check in 1 hour.", "SUCCESS")
        return True

    if dry_run:
        log("[DRY-RUN] Summary of scheduled actions:", "INFO")
        log(f"  • Frontend redeploy needed: {has_frontend_changes and not skip_fe}")
        log(f"  • Backend redeploy needed:  {has_backend_changes and not skip_be}")
        log(f"  • GitHub sync needed:       {not skip_push}")
        return True

    # 3. Synchronize Architecture Manifest (Rule 0c) if updated
    if has_architecture_changes or (ROOT_DIR / "generate_architecture_html.py").exists():
        log("Regenerating architecture HTML (Rule 0c)...")
        arch_code, arch_out, arch_err = run_cmd("python generate_architecture_html.py")
        if arch_code == 0:
            log("Architecture HTML synchronized successfully.", "SUCCESS")
        else:
            log(f"Warning: generate_architecture_html.py exited with code {arch_code}: {arch_err}", "WARN")

    # 4. Verify Frontend Production Build
    if has_frontend_changes and not skip_fe:
        log("Running frontend production build (npm run build)...")
        build_code, build_out, build_err = run_cmd("npm run build")
        if build_code != 0:
            log(f"Build failed! Aborting deployment to prevent broken production release: {build_err}", "ERROR")
            return False
        log("Frontend production build passed successfully.", "SUCCESS")

    # 5. Synchronize with GitHub (Commit & Push)
    if not skip_push:
        log("Staging verified updates for GitHub sync...")
        run_cmd("git add .")
        
        # Verify if there is anything to commit
        status_code, status_out, _ = run_cmd("git diff --cached --quiet")
        if status_code != 0: # Changes are staged
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            commit_msg = f"chore(sync): automated hourly code check, verified build & architecture sync [{ts}]"
            log(f"Committing updates: '{commit_msg}'")
            commit_code, commit_out, commit_err = run_cmd(f'git commit -m "{commit_msg}"')
            if commit_code != 0:
                log(f"Git commit failed: {commit_err}", "WARN")
            else:
                log("Pushing updates to origin/main...")
                push_code, push_out, push_err = run_cmd("git push origin main")
                if push_code == 0:
                    log("GitHub repository synchronized with origin/main.", "SUCCESS")
                else:
                    log(f"git push failed: {push_err}", "WARN")
        else:
            log("No staged differences to commit.", "INFO")

    # 6. Deploy Frontend (Firebase Hosting)
    if has_frontend_changes and not skip_fe:
        log("Deploying frontend production bundle to Firebase Hosting...")
        deploy_fe_code, deploy_fe_out, deploy_fe_err = run_cmd("npx firebase deploy --only hosting --non-interactive")
        if deploy_fe_code == 0:
            log("Frontend successfully redeployed to Firebase Hosting!", "SUCCESS")
        else:
            log(f"Firebase hosting deployment failed: {deploy_fe_err}\n{deploy_fe_out}", "WARN")

    # 7. Deploy Backend (Hugging Face Spaces)
    if has_backend_changes and not skip_be:
        deploy_script = ROOT_DIR / "caps-ai-backend" / "deploy_hf.py"
        if deploy_script.exists():
            log("Deploying backend updates to Hugging Face Spaces (snombi/tlassistant)...")
            deploy_be_code, deploy_be_out, deploy_be_err = run_cmd(f'python "{deploy_script}"', cwd=ROOT_DIR / "caps-ai-backend")
            if deploy_be_code == 0:
                log("Backend successfully redeployed to Hugging Face Spaces!", "SUCCESS")
            else:
                log(f"Backend deployment to Hugging Face Spaces exited: {deploy_be_err}\n{deploy_be_out}", "WARN")

    log("Hourly Code Check, GitHub Sync & Redeployment Cycle Completed Successfully.", "SUCCESS")
    log("=" * 65, "CYCLE")
    return True

def main():
    parser = argparse.ArgumentParser(description="Fundile Hourly Code Check, GitHub Sync & Dual Redeployment Pipeline")
    parser.add_argument("--once", action="store_true", help="Run once and exit (default)")
    parser.add_argument("--daemon", action="store_true", help="Run continuously in an hourly loop")
    parser.add_argument("--interval", type=int, default=3600, help="Interval in seconds for daemon mode (default: 3600)")
    parser.add_argument("--dry-run", action="store_true", help="Inspect changes without committing or deploying")
    parser.add_argument("--skip-fe", action="store_true", help="Skip frontend build and Firebase redeployment")
    parser.add_argument("--skip-be", action="store_true", help="Skip backend Hugging Face redeployment")
    parser.add_argument("--skip-push", action="store_true", help="Skip git push to origin/main")

    args = parser.parse_args()

    if args.daemon:
        log(f"Starting pipeline in DAEMON mode (Interval: {args.interval}s / {args.interval/60:.0f} mins)...")
        while True:
            try:
                execute_hourly_cycle(
                    dry_run=args.dry_run,
                    skip_fe=args.skip_fe,
                    skip_be=args.skip_be,
                    skip_push=args.skip_push
                )
            except KeyboardInterrupt:
                log("Daemon stopped by user (KeyboardInterrupt). Exiting.", "INFO")
                break
            except Exception as ex:
                log(f"Unhandled exception during cycle: {ex}", "ERROR")

            log(f"Sleeping for {args.interval} seconds until next hourly cycle...")
            time.sleep(args.interval)
    else:
        execute_hourly_cycle(
            dry_run=args.dry_run,
            skip_fe=args.skip_fe,
            skip_be=args.skip_be,
            skip_push=args.skip_push
        )

if __name__ == "__main__":
    main()
