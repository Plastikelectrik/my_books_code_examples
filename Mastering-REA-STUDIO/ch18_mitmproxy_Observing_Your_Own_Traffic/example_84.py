import json
import os
import urllib.request

url = os.environ.get("KETTLE_URL",
                     "http://127.0.0.1:8800/api/recipes")
req = urllib.request.Request(url)
req.add_header("X-Kettle-Token", "lab-token-123")
with urllib.request.urlopen(req, timeout=5) as resp:
    data = json.load(resp)
for r in data["recipes"]:
    print(r["tea"], r["temp"], r["seconds"])
