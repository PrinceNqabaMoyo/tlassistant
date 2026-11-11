import sys
import subprocess

cmd = [sys.executable, "-u", "run.py"]
print(f"Starting backend: {cmd}")
p = subprocess.Popen(cmd, cwd="caps-ai-backend")
print(f"Backend started with PID {p.pid}")
