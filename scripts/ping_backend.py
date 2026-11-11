import urllib.request
import json

try:
    with urllib.request.urlopen("http://127.0.0.1:5001/api/health", timeout=3) as resp:
        print("Health status code:", resp.status)
        print("Health body:", resp.read().decode())
except Exception as e:
    print("Health check failed:", e)

# Test an API endpoint
try:
    with urllib.request.urlopen("http://127.0.0.1:5001/", timeout=3) as resp:
        print("Root status code:", resp.status)
except Exception as e:
    print("Root ping:", e)
